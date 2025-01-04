# spec file for ocsinventory-agent
#
# Copyright (c) 2007-2014 Remi Collet
# Copyright (c) 2016-2017 Philippe Beaumont
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/3.0/
#
# Please, preserve the changelog entries
#

# Can, optionaly, be define at build time (see README.RPM)
# - ocstag    : administrative tag
# - ocsserver : OCS Inventory NG communication serveur

# Avoid empty debuginfo package, arched only for dep
%global debug_package %{nil}

# Official release version
%global official_version 2.10.4

Name:      ocsinventory-agent
Summary:   Open Computer and Software Inventory Next Generation client

Version:   2.10.4
Release:   4%{?dist}

Source0:   https://github.com/OCSInventory-NG/UnixAgent/releases/download/v%{official_version}/Ocsinventory-Unix-Agent-%{official_version}.tar.gz

Source11:   %{name}.README

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:   GPL-2.0-or-later
URL:       http://www.ocsinventory-ng.org/

BuildRequires: coreutils
BuildRequires: findutils
BuildRequires: make
BuildRequires: perl-interpreter
BuildRequires: perl-generators
BuildRequires: perl(Config)
BuildRequires: perl(English)
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(inc::Module::Install)
BuildRequires: perl(Module::Install::Metadata)
BuildRequires: perl(Module::Install::Scripts)
BuildRequires: perl(Module::Install::WriteAll)
BuildRequires: perl(strict)
BuildRequires: sed

%if 0%{?rhel} >= 7
BuildRequires: systemd
Requires(post): systemd
%else
BuildRequires: systemd-rpm-macros
Requires(post): systemd
%endif

###
#  NOTE: rpmlint: the runtime requirments change depending on the arch
#        so while this package contains no binaries, it is arch dependant.
###
Requires: perl-Ocsinventory-Agent = %{version}-%{release}
%ifarch %{ix86} x86_64 ia64
Requires:  dmidecode
%endif

Requires:  logrotate

Obsoletes: ocsinventory-client < %{version}
Provides:  ocsinventory-client = %{version}-%{release}

%{?perl_default_filter}

%description
Open Computer and Software Inventory Next Generation is an application
designed to help a network or system administrator keep track of computer
configuration and software installed on the network. 

It also allows deploying software, commands or files on Windows and
Linux client computers.

%{name} provides the client for Linux (Unified Unix Agent).


%description -l fr
Open Computer and Software Inventory Next Generation est une application
destinée à aider l'administrateur système ou réseau à garder un oeil sur
la configuration des machines du réseau et sur les logiciels qui y sont
installés. 

Elle autorise aussi la télédiffusion (ou déploiement) de logiciels, 
de commandes ou de fichiers sur les clients Windows ou Linux.

%{name} fournit le client pour Linux (Agent Unix Unifié)


%package -n perl-Ocsinventory-Agent
Summary:   Libraries %{name}
BuildArch: noarch

Requires:  perl(Data::UUID)
Requires:  perl(Digest::MD5)
Requires:  perl(File::Temp)
Requires:  perl(HTTP::Request)
Requires:  perl(LWP) > 6
Requires:  perl(LWP::Protocol)
Requires:  perl(LWP::Protocol::http)
Requires:  perl(LWP::Protocol::https)
Requires:  perl(Net::IP)
Requires:  perl(Net::Netmask)
Requires:  perl(Net::SNMP)
Requires:  perl(Net::SSLeay)
Requires:  perl(XML::Simple)
Requires: net-tools
Requires: pciutils
Requires: smartmontools
Requires: which
%if 0%{?fedora} >= 25 || 0%{?rhel} >= 8
Recommends: perl(Net::Cups)
Recommends: perl(Net::Ping)
Recommends: perl(Parse::EDID)
Recommends: perl(Proc::Daemon)
Recommends: perl(Proc::PID::File)
Recommends: ipmitool
Suggests: monitor-edid
Suggests: nmap
Suggests: perl(Nmap::Parser)
%endif

Conflicts: %{name} < %{version}

%description  -n perl-Ocsinventory-Agent
Perl libraries for %{name}

%prep
%setup -q -n Ocsinventory-Unix-Agent-%{version}
#%%autopatch -p1
rm -f lib/Ocsinventory/Agent/Network.pm.orig

sed -e 's/\r//' -i snmp/mibs/local/6876.xml

# Remove bundled modules
rm -rf ./inc
if [[ -e MANIFEST ]]; then
  perl -MConfig -i -ne 'print $_ unless m{^inc/}' MANIFEST
fi

###
# NOTE: rpmlint will complain about these macros in comments
#       they are on purpose to permit the comments to match
#       what the values used by the build environment.
###
cat <<EOF >%{name}.conf
# 
# OCS Inventory "Unix Unified Agent" Configuration File
# used by the ocsinventory-agent.service and
# related timers.
#

# Add tools directory if needed (tw_cli, hpacucli, ipssend, ...)
PATH=/sbin:/bin:/usr/sbin:/usr/bin

%if 0%{?ocsserver:1}
# Mode, change to "none" to disable
OCSMODE[0]=cron

# used to override the %{name}.cfg setup.
OCSSERVER[0]=%{ocsserver}

# runs in addition to the remote report
# corresponds with --local=%{_localstatedir}/lib/%{name}
# OCSSERVER[1]=local
%else
# Mode, change to "cron" to activate
OCSMODE[0]=none

# can be used to override the %{name}.cfg setup.
# OCSSERVER[0]=your.ocsserver.name
# 
# corresponds with --local=%{_localstatedir}/lib/%{name}
# OCSSERVER[0]=local
%endif

# Wait before inventory 
OCSPAUSE[0]=100

# Administrative TAG (optional, must be filed before first inventory)
OCSTAG[0]=%{?ocstag}

# If you need an HTTP/HTTPS proxy, fill this out
# OCSPROXYSERVER[0]='http://user:pass@proxy:port'
EOF

cat <<EOF >%{name}.cfg
# 
# OCS Inventory "Unix Unified Agent" Configuration File
#
# options used by timers or /etc/sysconfig/%{name} overide these.
#

# Server URL, unconmment if needed
# server = your.ocsserver.name
local = %{_localstatedir}/lib/%{name}

# Administrative TAG (optional, must be filed before first inventory)
# tag = %{?ocsserver:yourtag}

# How to log, can be File,Stderr,Syslog
logger = Stderr
logfile = %{_localstatedir}/log/%{name}/%{name}.log
EOF

cp %{SOURCE11} README.RPM


%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
rm run-postinst

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete

# Move exe to root directory
mv %{buildroot}%{_bindir} %{buildroot}%{_sbindir}

mkdir -p %{buildroot}%{_localstatedir}/{log,lib}/%{name}
mkdir -p %{buildroot}%{_sysconfdir}/{logrotate.d,sysconfig,ocsinventory/softwares}

mkdir %{buildroot}%{_localstatedir}/lib/%{name}/download
cp -pr snmp %{buildroot}%{_localstatedir}/lib/%{name}/snmp

install -pm 644 %{name}.conf %{buildroot}%{_sysconfdir}/sysconfig/%{name}

mkdir -p %{buildroot}/%{_libexecdir}/%{name}
sed -e 's;/etc/;%{_sysconfdir}/;' \
    -e 's;/var/;%{_localstatedir}/;' \
    -e 's;/usr/sbin/;%{_sbindir}/;' \
    contrib/cron/ocsinventory-agent.cron > %{buildroot}%{_libexecdir}/%{name}/ocsinventory-agent.cron
cp contrib/cron/ocsinventory-agent.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

mkdir -p %{buildroot}/%{_unitdir}
cp contrib/cron/systemd/* %{buildroot}/%{_unitdir}/

install -m 644 %{name}.cfg %{buildroot}/%{_sysconfdir}/ocsinventory/%{name}.cfg
install -m 644 etc/ocsinventory-agent/modules.conf %{buildroot}/%{_sysconfdir}/ocsinventory/modules.conf

# Remove some unusefull files (which brings unresolvable deps)
rm -rf %{buildroot}%{perl_vendorlib}/Ocsinventory/Agent/Backend/OS/Win32*

# Drop extra files
rm -f %{buildroot}%{perl_vendorarch}/auto/Ocsinventory/Unix/Agent/.packlist
rm -f %{buildroot}%{perl_vendorarch}/../perllocal.pod

# Only need for manual installation
rm %{buildroot}%{perl_vendorlib}/Ocsinventory/Unix/postinst.pl

# Provided by ocsinventtory-ipdiscover
rm %{buildroot}%{_sbindir}/ipdiscover

# the source comes with some odd permissions set
# just fix them to make sense
find %{buildroot} -type f -exec chmod 644 {} \;
find %{buildroot} -type f -name .DS_Store -exec rm {} \;
find %{buildroot} -type f -name ._.DS_Store -exec rm {} \;

%post

# See if sysadmin requested ocs agent run on boot
%systemd_post ocsinventory-agent-onboot.timer

# See if sysadmin requested ocs agent hourly run
%systemd_post ocsinventory-agent-hourly.timer

# See if sysadmin requested ocs agent daily run
%systemd_post ocsinventory-agent-daily.timer

%files
%defattr(644,root,root,755)
%attr(0755, root, root) %{_sbindir}/%{name}
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%{_libexecdir}/%{name}/
%attr(0755, root, root) %{_libexecdir}/%{name}/ocsinventory-agent.cron
%dir %{_localstatedir}/log/%{name}
%{_mandir}/man1/%{name}*
%{_unitdir}/*

%files -n perl-Ocsinventory-Agent
%defattr(644,root,root,755)
%doc AUTHORS Changes README.md THANKS README.RPM
%doc etc/ocsinventory-agent/softwares/example.sh
%license LICENSE
%config(noreplace) %{_sysconfdir}/ocsinventory/%{name}.cfg
%config(noreplace) %{_sysconfdir}/ocsinventory/modules.conf
%{perl_vendorlib}/Ocsinventory
%attr(0755, root, root) %{perl_vendorlib}/Ocsinventory/Agent.pm
%{_mandir}/man3/Ocs*
%dir %{_localstatedir}/lib/%{name}
%{_localstatedir}/lib/%{name}/download
%{_localstatedir}/lib/%{name}/snmp
%dir %{_sysconfdir}/ocsinventory
%dir %{_sysconfdir}/ocsinventory/softwares


%changelog
* Thu Jan 2 2025 Pat Riehecky <riehecky@fnal.gov> - 2.10.4-4
- Make monitor-edid suggests rather than recommended because we have perl-parse-edid

* Wed Oct 30 2024 Pat Riehecky <riehecky@fnal.gov> - 2.10.4-2
- Make monitor-edid recommended rather than required

* Tue Oct 29 2024 Pat Riehecky <riehecky@fnal.gov> - 2.10.4-1
- Update to 2.10.4

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.10.2-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Mar 28 2024 Pat Riehecky <riehecky@fnal.gov> - 2.10.2-1
- Update to 2.10.2.

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Nov 28 2023 Pat Riehecky <riehecky@fnal.gov> - 2.10.0-4
- Fix requires for logrotate

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Oct 17 2022 Pat Riehecky <riehecky@fnal.gov> - 2.10.0-1
- Update to 2.10.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.9.3-2
- Perl 5.36 rebuild

* Tue May 31 2022 Pat Riehecky <riehecky@fnal.gov> - 2.9.3-1
- Update to 2.9.3

* Wed Jan 26 2022 Pat Riehecky <riehecky@fnal.gov> - 2.9.1-1
- Update to 2.9.1

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 13 2021 Pat Riehecky <riehecky@fnal.gov> - 2.9.0-2
- Fix gating permissions

* Mon Dec 13 2021 Pat Riehecky <riehecky@fnal.gov> - 2.9.0-1.1
- remove meaningless execute on README

* Mon Dec 13 2021 Pat Riehecky <riehecky@fnal.gov> - 2.9.0-1
- Update to 2.9.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.6.0-11
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.6.0-7
- Perl 5.32 rebuild

* Tue Mar 24 2020 Petr Pisar <ppisar@redhat.com> - 2.6.0-6
- Specify all dependencies

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-5
- Add OCSPROXYSERVER for http/s proxys

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-4.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 6 2020 Pat Riehecky <riehecky@fnal.gov> - 2.6.0-3.2
- More cleanup UTF8 parse
- Smarter use of local CA list

* Fri Dec 27 2019 Pat Riehecky <riehecky@fnal.gov> - 2.6.0-3.1
- Cleanup UTF8 parse
- drop system CA list, keep local CA list

* Wed Dec 18 2019 Pat Riehecky <riehecky@fnal.gov> - 2.6.0-3
- Use system CA certs if no custom client CA set

* Tue Dec 03 2019 Pat Riehecky <riehecky@fnal.gov> - 2.6.0-2.1
- Backport a few patches from upstream

* Thu Aug 15 2019 Pat Riehecky <riehecky@fnal.gov> - 2.6.0-2
- Return to Fedora
- Use systemd timers rather than cron for regular runs
- Add a handful of possible timers users might want

* Mon May 20 2019 Philippe Beaumont <philippe.beaumont@ocsinventory-ng.org> - 2.6.0-1
- Update to 2.6.0

* Mon Dec 31 2018 Philippe Beaumont <philippe.beaumont@ocsinventory-ng.org> - 2.4.2-3
- Remove Module::Install as dependancy

* Mon Dec 24 2018 Philippe Beaumont <philippe.beaumont@ocsinventory-ng.org> - 2.4.2-2
- Add core agent

* Tue Jul 31 2018 Philippe Beaumont <philippe.beaumont@ocsinventory-ng.org> - 2.4.2-1
- Update to 2.4.2

* Sun Feb 11 2018 Philippe Beaumont <philippe.beaumont@ocsinventory-ng.org> - 2.4.0-1
- Update to 2.4.0

* Mon Jan 15 2018 Philippe Beaumont <philippe.beaumont@ocsinventory-ng.org> - 2.3.0-2
- Add SSL dependancies

* Thu Jan 12 2017 Philippe Beaumont <philippe.beaumont@ocsinventory-ng.org> - 2.3.0-1
- Update to 2.3.0

* Sun Jan 01 2017 Philippe Beaumont <philippe.beaumont@ocsinventory-ng.org> - 2.3.0-0.1
- Update to 2.3RC1

* Thu May 22 2014 Remi Collet <remi@fedoraproject.org> - 2.1.1-2
- Update to 2.1.1

* Thu Feb 13 2014 Remi Collet <remi@fedoraproject.org> - 2.1-2
- more upstream patches
- add /var/lib/ocsinventory-agent/snmp and download folder
- move /etc/ocsinventory and /var/lib to subpackage

* Thu Feb 13 2014 Remi Collet <remi@fedoraproject.org> - 2.1-1
- Update to 2.1
- move perl library to perl-Ocsinventory-Agent
- make main package arched for dependency on dmidecode

* Fri Aug 02 2013 Petr Pisar <ppisar@redhat.com> - 2.0.5-8
- Perl 5.18 rebuild

* Sat Jul 27 2013 Jóhann B. Guðmundsson <johannbg@fedoraproject.org> - 2.0.5-7
- Add a missing requirement on crontabs to spec file

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 17 2012 Remi Collet <remi@fedoraproject.org> - 2.0.5-5
- fix provided configuration when build with ocsserver defined

* Sun Sep 23 2012 Remi Collet <remi@fedoraproject.org> - 2.0.5-4
- fix ifconfig output parser (#853982)
  https://bugs.launchpad.net/bugs/1045356

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 2.0.5-2
- Perl 5.16 rebuild

* Sat Apr 14 2012 Remi Collet <remi@fedoraproject.org> - 2.0.5-1
- update to 2.0.5

* Mon Feb 13 2012 Remi Collet <remi@fedoraproject.org> - 2.0.4-1
- update to 2.0.4

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 1.1.2.1-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Oct 13 2010 Remi Collet <Fedora@famillecollet.com> 1.1.2.1-1
- security update for CVE-2009-0667
  http://bugs.debian.org/590879
  http://www.debian.org/security/2009/dsa-1828

* Sat Oct 09 2010 Remi Collet <Fedora@famillecollet.com> 1.1.2-3
- remove perl-XML-SAX optional dep, which is broken on EL5
  and cause overload when installed on the OCS server

* Tue Jun 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.1.2-2
- Mass rebuild with perl-5.12.0

* Sun Jan 03 2010 Remi Collet <Fedora@famillecollet.com> 1.1.2-1
- update to 1.1.2

* Sun Dec 27 2009 Remi Collet <Fedora@famillecollet.com> 1.1.1-2
- missing perl(Net::IP) requires (+ some EL3 stuff: yes, I know)

* Tue Dec 22 2009 Remi Collet <Fedora@famillecollet.com> 1.1.1-1
- update to 1.1.1

* Sat Nov 28 2009 Remi Collet <Fedora@famillecollet.com> 1.1-2
- add Requires: which

* Sat Nov 07 2009 Remi Collet <Fedora@famillecollet.com> 1.1-1
- update to 1.1
- add missing modules.conf
- new Requires perl(Net::SSLeay), perl(Crypt::SSLeay), smartmontools
- download URL to launchpad

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May 14 2009 Remi Collet <Fedora@famillecollet.com> 1.0.1-4
- fix typo

* Thu May 14 2009 Remi Collet <Fedora@famillecollet.com> 1.0.1-3
- define PATH in config (workaround for #500594 + tool path if needed)
 
* Fri Apr 24 2009 Remi Collet <Fedora@famillecollet.com> 1.0.1-2
- update the README.RPM (new configuration file)
- change from URL to only servername in config comment

* Sun Mar 29 2009 Remi Collet <Fedora@famillecollet.com> 1.0.1-1
- update to 1.0.1

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Oct 20 2008 Remi Collet <Fedora@famillecollet.com> 0.0.9.2-2
- fix FTBFS (#465073)

* Sun Apr 20 2008 Remi Collet <Fedora@famillecollet.com> 0.0.9.2-1
- update to 0.0.9.2 (minor bug fix)

* Mon Apr 07 2008 Remi Collet <Fedora@famillecollet.com> 0.0.9.1-2
- add Requires monitor-edid

* Thu Apr 03 2008 Remi Collet <Fedora@famillecollet.com> 0.0.9.1-1
- update to 0.0.9.1 (minor bug fix)
- swicth back to nobundle sources

* Wed Apr 02 2008 Remi Collet <Fedora@famillecollet.com> 0.0.9-1
- update to 0.0.9 finale
- provides default config to file (need options.patch)
- add requires nmap (for ipdiscover)
- add BR perl(XML::SAX) (to avoid install of bundled one)

* Mon Mar 10 2008 Remi Collet <Fedora@famillecollet.com> 0.0.8.2-0.6.20080305
- rebuild against perl 5.10

* Fri Mar  7 2008 Remi Collet <Fedora@famillecollet.com> 0.0.8.2-0.5.20080305
- patches from review (Patrice Dumas)

* Wed Mar  5 2008 Remi Collet <Fedora@famillecollet.com> 0.0.8.2-0.4.20080305
- update to 2008-03-05
- add /etc/sysconfig/ocsinventory-agent config file for cron job

* Mon Mar  3 2008 Remi Collet <Fedora@famillecollet.com> 0.0.8.2-0.3.20080302
- only enable cron when server is configured

* Sun Mar  2 2008 Remi Collet <Fedora@famillecollet.com> 0.0.8.2-0.2.20080302
- from Review, see #435593

* Sun Mar  2 2008 Remi Collet <Fedora@famillecollet.com> 0.0.8.2-0.1.20080302
- update to 0.0.8.2 from CVS

* Fri Feb 22 2008 Remi Collet <Fedora@famillecollet.com> 0.0.8.2-0.1.20080222
- update to 0.0.8.2 from CVS

* Sun Feb 17 2008 Remi Collet <Fedora@famillecollet.com> 0.0.8.1-0.1.20080217
- update to 0.0.8.1 from CVS
- change config file used
   from /etc/ocsinventory-agent/ocsinv.conf 
     to /etc/ocsinventory/ocsinventory-agent.cfg

* Sat Jan 26 2008 Remi Collet <Fedora@famillecollet.com> 0.0.7-1
- update to 0.0.7

* Fri Dec 28 2007 Remi Collet <Fedora@famillecollet.com> 0.0.6.2-1
- update to 0.0.6.2

* Mon Apr 16 2007 Remi Collet <Fedora@famillecollet.com> 0.0.6-1
- update to 0.0.6

* Sat Feb 10 2007 Remi Collet <Fedora@famillecollet.com> 0.0.5-0.20070409
- cvs update 20070409
- create cron.daily file
- create logrotate.d file
- create ocsinv.conf
- cvs update 20070405
- cvs update 20070403

* Sat Feb 10 2007 Remi Collet <Fedora@famillecollet.com> 0.0.2-0.20070210
- initial spec
