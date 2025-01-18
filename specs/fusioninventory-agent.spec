## Disabling debug package 
## Can't build as noarch due to dmidecode requires
%global debug_package %{nil}


Name:        fusioninventory-agent
Summary:     FusionInventory agent
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:     GPL-2.0-or-later
URL:         http://fusioninventory.org/

Version:     2.6
Release:     14%{?dist}
Source0:     https://github.com/fusioninventory/%{name}/releases/download/%{version}/FusionInventory-Agent-%{version}.tar.gz
Source1:     %{name}.cron
Source10:    %{name}.service

BuildRequires: coreutils
BuildRequires: findutils
BuildRequires: make
BuildRequires: perl-generators
BuildRequires: perl-interpreter
BuildRequires: perl(Config)
BuildRequires: perl(English)
BuildRequires: perl(inc::Module::Install)
BuildRequires: perl(Module::AutoInstall)
BuildRequires: perl(Module::Install::Include)
BuildRequires: perl(Module::Install::Makefile)
BuildRequires: perl(Module::Install::Metadata)
BuildRequires: perl(Module::Install::Scripts)
BuildRequires: perl(Module::Install::WriteAll)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
BuildRequires: sed
BuildRequires: systemd

Requires:  perl-FusionInventory-Agent = %{version}-%{release}
Requires:  cronie
%ifarch %{ix86} x86_64
Requires:  dmidecode
%endif

Requires(post):     systemd
Requires(preun):    systemd
Requires(postun):   systemd

# excluding internal requires and windows stuff
# excluding perl(setup) and windows stuff
%{?perl_default_filter}
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(setup\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Win32|setup\\)$

%description
FusionInventory Agent is an application designed to help a network
or system administrator to keep track of the hardware and software
configurations of computers that are installed on the network.

This agent can send information about the computer to a OCS Inventory NG
or GLPI server with the FusionInventory for GLPI plugin.

You can add additional packages for optional tasks:

* fusioninventory-agent-task-network
    Network Discovery and Inventory support
* fusioninventory-agent-inventory
    Local inventory support for FusionInventory
* fusioninventory-agent-task-deploy
    Software deployment support
* fusioninventory-agent-task-esx
    vCenter/ESX/ESXi remote inventory
* fusioninventory-agent-task-collect
    Custom information retrieval support
* fusioninventory-agent-task-wakeonlan
    Wake o lan task


%package -n perl-FusionInventory-Agent
Summary:        Libraries for Fusioninventory agent
BuildArch:      noarch
Requires:       perl(LWP)
Requires:       perl(Net::CUPS)
Requires:       perl(Net::SSLeay)
Requires:       perl(Proc::Daemon)
Requires:       perl(Socket::GetAddrInfo)

%description -n perl-FusionInventory-Agent
Libraries for Fusioninventory agent.

%package task-esx
Summary:    FusionInventory plugin to inventory vCenter/ESX/ESXi
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}

%description task-esx
fusioninventory-agent-task-ESX ask the running service agent to inventory an 
VMWare vCenter/ESX/ESXi server through SOAP interface


%package task-network
Summary:    NetDiscovery and NetInventory task for FusionInventory
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description task-network
fusioninventory-task-netdiscovery and fusioninventory-task-netinventory

%package task-deploy
Summary:    Software deployment support for FusionInventory agent
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}
Requires:   perl(Archive::Extract)

%description task-deploy
This package provides software deployment support for FusionInventory-agent

%package task-wakeonlan
Summary:    WakeOnLan task for FusionInventory
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}

%description task-wakeonlan
fusioninventory-task-wakeonlan

%package task-inventory
Summary:    Inventory task for FusionInventory
Requires:   %{name} = %{version}-%{release}
Requires:   perl(Net::CUPS)
Requires:   perl(Parse::EDID)

%description task-inventory
fusioninventory-task-inventory

%package task-collect
Summary:    Custom information retrieval support for FusionInventory agent
Requires:   %{name} = %{version}-%{release}

%description task-collect
This package provides custom information retrieval support for
FusionInventory agent

%package cron
Summary:    Cron for FusionInventory agent
Requires:   %{name} = %{version}-%{release}

%description cron
fusioninventory cron task


%prep
%setup -q -n FusionInventory-Agent-%{version}

# Remove bundled modules
rm -rf ./inc
sed -e '/^inc\//d' -i MANIFEST

sed \
    -e "s/logger = .*/logger = syslog/" \
    -e "s/logfacility = .*/logfacility = LOG_DAEMON/" \
    -e 's|#include "conf\.d/"|include "conf\.d/"|' \
    -i etc/agent.cfg

cat <<EOF | tee %{name}.conf
#
# Fusion Inventory Agent Configuration File
# used by hourly cron job to override the %{name}.cfg setup.
#
# /!\
# USING THIS FILE TO OVERRIDE SERVICE OPTIONS IS DEPRECATED!
# See %{_unitdir}/%{name}.service notice
#
# Add tools directory if needed (tw_cli, hpacucli, ipssend, ...)
PATH=/sbin:/bin:/usr/sbin:/usr/bin
# Global options (debug for verbose log)
OPTIONS="--debug "

# Mode, change to "cron" to activate
# - none (default on install) no activity
# - cron (inventory only) use the cron.hourly
OCSMODE[0]=none
# OCS Inventory or FusionInventory server URI
# OCSSERVER[0]=your.ocsserver.name
# OCSSERVER[0]=http://your.ocsserver.name/ocsinventory
# OCSSERVER[0]=http://your.glpiserveur.name/glpi/plugins/fusioninventory/
# corresponds with --local=%{_localstatedir}/lib/%{name}
# OCSSERVER[0]=local
# Wait before inventory (for cron mode)
OCSPAUSE[0]=120
# Administrative TAG (optional, must be filed before first inventory)
OCSTAG[0]=

EOF


%build
perl Makefile.PL \
     PREFIX=%{_prefix} \
     SYSCONFDIR=%{_sysconfdir}/fusioninventory \
     LOCALSTATEDIR=%{_localstatedir}/lib/%{name} \
     VERSION=%{version}-%{release}

make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'

%{_fixperms} %{buildroot}/*

mkdir -p %{buildroot}%{_localstatedir}/lib/%{name}
mkdir -p %{buildroot}%{_sysconfdir}/fusioninventory/conf.d
mkdir -p %{buildroot}%{_sysconfdir}/systemd/system/%{name}.service.d

install -m 644 -D  %{name}.conf  %{buildroot}%{_sysconfdir}/sysconfig/%{name}
install -m 755 -Dp %{SOURCE1}    %{buildroot}%{_sysconfdir}/cron.hourly/%{name}
install -m 644 -D  %{SOURCE10}   %{buildroot}%{_unitdir}/%{name}.service


%check
#make test

%post
%systemd_post fusioninventory-agent.service


%preun
%systemd_preun fusioninventory-agent.service


%postun
%systemd_postun_with_restart fusioninventory-agent.service


%files
%dir %{_sysconfdir}/fusioninventory
%config(noreplace) %{_sysconfdir}/fusioninventory/agent.cfg
%config(noreplace) %{_sysconfdir}/fusioninventory/conf.d
%config(noreplace) %{_sysconfdir}/fusioninventory/inventory-server-plugin.cfg
%config(noreplace) %{_sysconfdir}/fusioninventory/server-test-plugin.cfg
%config(noreplace) %{_sysconfdir}/fusioninventory/ssl-server-plugin.cfg
%config(noreplace) %{_sysconfdir}/fusioninventory/proxy-server-plugin.cfg
%config(noreplace) %{_sysconfdir}/fusioninventory/proxy2-server-plugin.cfg

%{_unitdir}/%{name}.service
%dir %{_sysconfdir}/systemd/system/%{name}.service.d
%{_bindir}/fusioninventory-agent
%{_bindir}/fusioninventory-injector
%{_mandir}/man1/fusioninventory-agent*
%{_mandir}/man1/fusioninventory-injector*
%dir %{_localstatedir}/lib/%{name}
%dir %{_datadir}/fusioninventory
%dir %{_datadir}/fusioninventory/lib
%dir %{_datadir}/fusioninventory/lib/FusionInventory
%dir %{_datadir}/fusioninventory/lib/FusionInventory/Agent
%dir %{_datadir}/fusioninventory/lib/FusionInventory/Agent/Task


%files -n perl-FusionInventory-Agent
%doc Changes LICENSE THANKS
#excluding sub-packages files
#%%exclude %%{_datadir}/fusioninventory/lib/FusionInventory/Agent/Task/*
%{_datadir}/fusioninventory

%files task-esx
%{_bindir}/fusioninventory-esx
%{_mandir}/man1/fusioninventory-esx.1*
%{_datadir}/fusioninventory/lib/FusionInventory/Agent/Task/ESX.pm
%{_datadir}/fusioninventory/lib/FusionInventory/Agent/SOAP

%files task-network
%{_bindir}/fusioninventory-netdiscovery
%{_bindir}/fusioninventory-netinventory
%{_mandir}/man1/fusioninventory-netdiscovery.1*
%{_mandir}/man1/fusioninventory-netinventory.1*
%{_datadir}/fusioninventory/lib/FusionInventory/Agent/Task/NetDiscovery.pm
%{_datadir}/fusioninventory/lib/FusionInventory/Agent/Task/NetInventory.pm

%files task-deploy
%{_datadir}/fusioninventory/lib/FusionInventory/Agent/Task/Deploy.pm
%{_datadir}/fusioninventory/lib/FusionInventory/Agent/Task/Deploy

%files task-wakeonlan
%{_bindir}/fusioninventory-wakeonlan
%{_mandir}/man1/fusioninventory-wakeonlan.1*
%{_datadir}/fusioninventory/lib/FusionInventory/Agent/Task/WakeOnLan.pm

%files task-inventory
%{_bindir}/fusioninventory-inventory
%{_bindir}/fusioninventory-remoteinventory
%{_mandir}/man1/fusioninventory-*inventory.1*
%{_datadir}/fusioninventory/lib/FusionInventory/Agent/Task/Inventory.pm
%{_datadir}/fusioninventory/lib/FusionInventory/Agent/Task/Inventory

%files task-collect
%{_datadir}/fusioninventory/lib/FusionInventory/Agent/Task/Collect.pm

%files cron
%{_sysconfdir}/cron.hourly/%{name}
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 2.6-13
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.6-6
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.6-3
- Perl 5.34 rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.6-2
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Fri Jan 29 2021 Marianne Lombard <jehane@fedoraproject.org> - 2.6-1
- Bump release to 2.6

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.5.2-4
- Perl 5.32 rebuild

* Thu Mar 12 2020 Petr Pisar <ppisar@redhat.com> - 2.5.2-3
- Specify all dependencies and unbundle Module::Install

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 17 2019 Johan Cwiklinski <jcwiklinski AT teclib DOT com> - 2.5.2-1
- Last upstream release
- Drop patch applied upstream

* Mon Aug 12 2019 Marianne Lombard <jehane@fedoraproject.org> - 2.5.1-4
- Fixing patch (thanks to E. Seyman - eseyman AT fedoraproject DOT org - help) and applying it
- Fix issue #1735227 : FTBFS

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 15 2019 Johan Cwiklinski <jcwiklinski AT teclib DOT com> - 2.5.1-2
- Add upstream HTTP server patch
- add missing configuration files

* Mon Jul 08 2019 Johan Cwiklinski <jcwiklinski AT teclib DOT com> - 2.5.1-1
- Last upstream release
- Remove patches applied upstream

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.5-5
- Perl 5.30 rebuild

* Tue May 07 2019 Johan Cwiklinski <jcwiklinski AT teclib DOT com> - 2.5-4
- Add patch to fix SSL on with http modules

* Thu May 02 2019 Guillaume Bougard <gbougard AT teclib DOT com> - 2.5-3
- Add patches to fix agent HTTP server plugins integration

* Thu Apr 18 2019 Johan Cwiklinski <jcwiklinski AT teclib DOT com> - 2.5-2
- Re-add tasks files in main perl package, to solve dependencies issues on package

* Mon Apr 15 2019 Johan Cwiklinski <jcwiklinski AT teclib DOT com> - 2.5-1
- Last upstream release
- Tasks files were provided also in main perl package
- Apply upstream minor fixes patch
- task-wakeonlan is back (see https://github.com/fusioninventory/fusioninventory-agent/issues/495#issuecomment-435110369 about dependancy issue)

* Tue Feb 26 2019 Johan Cwiklinski <johan AT x-tnd DOT be> - 2.4.3-2
- Remove yum plugin (and therefore dependency on yum)

* Mon Feb 25 2019 Johan Cwiklinski <jcwiklinski AT teclib DOT com> - 2.4.3-1
- Last upstream release

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 03 2018 Johan Cwiklinski <jcwiklinski AT teclib DOT com> - 2.4.2-1
- Last upstream release
- Drop patch applied upstream

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Johan Cwiklinski <jcwiklinski AT teclib DOT com> - 2.4.1-3
- Add upstream patch to fix wrong variable name

* Fri Jul 06 2018 Petr Pisar <ppisar@redhat.com> - 2.4.1-2
- Perl 5.28 rebuild

* Tue Jul 03 2018 Johan Cwiklinski <jcwiklinski AT teclib DOT com> - 2.4.1-1
- Last upstream release

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.4-6
- Perl 5.28 rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Johan Cwiklinski <jcwiklinski AT teclib DOT com> - 2.4-4
- Logrotate is no longer needed since we now use syslog

* Mon Jan 15 2018 Johan Cwiklinski <jcwiklinski AT teclib DOT com> - 2.4-3
- Change logging according to upstream recommandations

* Thu Jan 11 2018 Johan Cwiklinski <jcwiklinski AT teclib DOT com> - 2.4-2
- Drop systemd override conf file, thits is no longer needed

* Thu Jan 11 2018 Johan Cwiklinski <jcwiklinski AT teclib DOT com> - 2.4-1
- Last upstream release
- Put cron stuff in a separate sub-package
- Provide conf.d configuration directory

* Mon Oct 16 2017 Johan Cwiklinski <jcwiklinski AT teclib DOT com> - 2.3.21-3
- Do not provides perl(setup); BZ #1485919 - thanks to E. Seyman

* Thu Aug 10 2017 Johan Cwiklinski <jcwiklinski AT teclib DOT com> - 2.3.21-2
- Fix missing provides issue on perl(setup)

* Tue Aug 01 2017 Marianne Lombard <jehane@fedoraproject.org> - 2.3.21-1
- Last upstream release

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.3.20-2
- Perl 5.26 re-rebuild of bootstrapped packages

* Tue Jun 06 2017 Johan Cwiklinski <jcwiklinski AT teclib DOT com> - 2.3.20-1
- Last upstream release
- Drop patches, upstream has provided fixes

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.3.19-4
- Perl 5.26 rebuild

* Wed May 17 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.3.19-3
- Fix building on Perl without '.' in @INC

* Mon Feb 20 2017 Johan Cwiklinski <jcwiklinski AT teclib DOT com> - 2.3.19-2
- Fix setup.pm values

* Sat Feb 18 2017 Johan Cwiklinski <johan AT x-tnd DOT be> - 2.3.19-1
- Last upstream release

* Thu Feb 09 2017 Johan Cwiklinski <jcwiklinski AT teclib DOT com> - 2.3.18-3
- Change systemd unit to not use fork mode
- Re-add options in sysconfig file to get cron mode running

* Wed Jun 22 2016 Johan Cwiklinski <johan AT x-tnd DOT be> - 2.3.18-2
- Add task-collect subpackage
- Change package source according to upstream recomendations

* Tue Jun 21 2016 Johan Cwiklinski <johan AT x-tnd DOT be> - 2.3.18-1
- Last upstream release
- Handle macros in comments to make rpmlint happy
- Cleanup comments

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.3.17-3
- Perl 5.24 rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 7 2015 Marianne Lombard <jehane@fedoraproject.org> - 2.3.17
- new version
- Upstream switch to github, minor spec adaptation

* Wed Jul 8 2015 Marianne Lombard <jehane@fedoraproject.org> - 2.3.16-5
- fix for #1240964 

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.3.16-3
- Perl 5.22 rebuild

* Sun Mar 29 2015 Marianne Lombard <jehane@fedoraproject.org> - 2.3.16-2
- commenting un-used BuildRequires

* Sun Mar 1 2015 Marianne Lombard <jehane@fedoraprojetc.org> - 2.3.16
- update to 2.3.16
- adding BuildRequires needed by test

* Sun Mar 1 2015 Marianne Lombard <jehane@fedoraproject.org> - 2.3.15-4
- arch build (due to dmidecode dependancy in x86_64)

* Fri Feb 20 2015 Marianne Lombard <jehane@fedoraproject.org> - 2.3.15-3
- building as noarch

* Wed Feb 11 2015 Marianne Lombard <marianne@tuxette.fr> - 2.3.15-2
- fix description of subpackage
- using upstream systemd unit file

* Mon Feb 9 2015 Marianne Lombard <marianne@tuxette.fr> - 2.3.15
- new version and back in Fedora

* Mon Jan 19 2015 Marianne Lombard <marianne@tuxette.fr> - 2.3.14-2 
- enhancing spec according to review 

* Wed Dec 24 2014 Marianne Lombard <marianne@tuxette.fr> - 2.3.14
- new version

* Mon Dec 15 2014 Marianne Lombard <marianne@tuxette.fr> - 2.3.13
- new version
- updating spec according to fedora-review

* Tue Aug 5 2014 Marianne Lombard <marianne@tuxette.fr> - 2.3.12
- new version 

* Tue Aug 5 2014 Marianne Lombard <marianne@tuxette.fr> - 2.3.10.1-2
- adding missing requires 
- updating config file

* Mon Aug 4 2014 Marianne Lombard <marianne@tuxette.fr> - 2.3.10.1
- new version (bug fixes)

* Fri Aug 1 2014 Marianne Lombard <marianne@tuxette.fr> - 2.3.10
- new version

* Wed Jul 23 2014 Marianne Lombard <marianne@tuxette.fr> - 2.3.9.1
- new version

* Tue May 20 2014 Marianne Lombard <marianne@tuxette.fr> - 2.3.8-1
- enhancing spec according to Michael Schwendt review
- adding missing requires

* Fri May 16 2014 Marianne Lombard <marianne@tuxette.fr> - 2.3.8
- new version

* Wed May 14 2014 Marianne Lombard <marianne@tuxette.fr> - 2.3.7.1
- new version 

* Sat Feb 1 2014 Marianne Lombard <marianne@tuxette.fr> - 2.3.6
- new version, reintroduction in fedora and epel
- cleanup of the spec (removing sysVinit stuff, old BuildRequires, old releases stuff)
- adding sub-packages for task-* (using Guillaume Rousse OBS spec as model https://build.opensuse.org/package/view_file/home:guillomovitch/fusioninventory-agent/fusioninventory-agent.spec)
- task-wakeonlan is excluded (dependancy issue)

* Wed Aug  8 2012 Remi Collet <remi@fedoraproject.org> - 2.2.4-2
- dump release

* Wed Aug  8 2012 Remi Collet <remi@fedoraproject.org> - 2.2.4-1
- version 2.2.4 fixes various bugs as described in
  http://cpansearch.perl.org/src/FUSINV/FusionInventory-Agent-2.2.4/Changes
  http://cpansearch.perl.org/src/FUSINV/FusionInventory-Agent-2.2.3/Changes

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 25 2012 Petr Pisar <ppisar@redhat.com> - 2.2.2-4
- Perl 5.16 rebuild

* Tue Jun 05 2012 Remi Collet <remi@fedoraproject.org> - 2.2.2-3
- no need for debuginfo (not really arch, fix #828960)
- yum plugin is also noarch

* Thu May 31 2012 Remi Collet <remi@fedoraproject.org> - 2.2.2-2
- make package "arch"
- requires dmidecode when available (x86)
- add sub-package perl-FusionInventory-Agent (noarch)

* Wed May 30 2012 Remi Collet <remi@fedoraproject.org> - 2.2.2-1
- update to 2.2.2
  http://cpansearch.perl.org/src/FUSINV/FusionInventory-Agent-2.2.2/Changes
  http://cpansearch.perl.org/src/FUSINV/FusionInventory-Agent-2.2.1/Changes

* Fri May 11 2012 Remi Collet <remi@fedoraproject.org> - 2.2.0-2
- filter private provides/requires

* Thu May 10 2012 Remi Collet <remi@fedoraproject.org> - 2.2.0-1
- update to 2.2.0
  http://search.cpan.org/src/FUSINV/FusionInventory-Agent-2.2.0/Changes
- revert change in 2.2.0: don't loose arch information
  see http://forge.fusioninventory.org/issues/1581

* Sun Feb 26 2012 Remi Collet <remi@fedoraproject.org> - 2.1.14-1
- update to 2.1.14
  http://cpansearch.perl.org/src/FUSINV/FusionInventory-Agent-2.1.14/Changes

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 28 2011 Remi Collet <remi@fedoraproject.org> - 2.1.12-1
- update to 2.1.12
  http://cpansearch.perl.org/src/FUSINV/FusionInventory-Agent-2.1.12/Changes
- upstream patch for http://forge.fusioninventory.org/issues/1161

* Sat Aug 06 2011 Remi Collet <remi@fedoraproject.org> - 2.1.9-3
- adapt filter

* Mon Jul 25 2011 Petr Sabata <contyk@redhat.com> - 2.1.9-2
- Perl mass rebuild

* Sun Jun 26 2011 Remi Collet <Fedora@famillecollet.com> 2.1.9-1
- missing dist tag

* Wed Jun 15 2011 Remi Collet <Fedora@famillecollet.com> 2.1.9-1
- update to 2.1.9
  http://cpansearch.perl.org/src/FUSINV/FusionInventory-Agent-2.1.9/Changes

* Sat Jun 11 2011 Remi Collet <Fedora@famillecollet.com> 2.1.9-0.1.git9bd1238
- update to 2.1.9 from git
- improved init script for systemd
- improved comment for use with glpi-fusioninventory

* Thu Mar 31 2011 Remi Collet <Fedora@famillecollet.com> 2.1.8-2
- revert change for issue 656 which breaks compatibility

* Wed Mar 30 2011 Remi Collet <Fedora@famillecollet.com> 2.1.8-1
- update to 2.1.8
  http://cpansearch.perl.org/src/FUSINV/FusionInventory-Agent-2.1.8/Changes

* Thu Dec 30 2010 Remi Collet <Fedora@famillecollet.com> 2.1.7-2
- add the yum-plugin sub-package

* Mon Dec 13 2010 Remi Collet <Fedora@famillecollet.com> 2.1.7-1
- update to 2.1.7
  http://cpansearch.perl.org/src/FUSINV/FusionInventory-Agent-2.1.7/Changes

* Sun Nov 28 2010 Remi Collet <Fedora@famillecollet.com> 2.1.7-0.1.beta1
- update to 2.1.7 beta1

* Sat Nov 13 2010 Remi Collet <Fedora@famillecollet.com> 2.1.6-1.1
- fix perl filter on EL-6

* Wed Oct 06 2010 Remi Collet <Fedora@famillecollet.com> 2.1.6-1
- update to 2.1.6
  http://cpansearch.perl.org/src/FUSINV/FusionInventory-Agent-2.1.6/Changes
- fix init script for multi-server in daemon mode
- workaround for http://forge.fusioninventory.org/issues/414

* Wed Sep 15 2010 Remi Collet <Fedora@famillecollet.com> 2.1.5-1
- update to 2.1.5
  http://cpansearch.perl.org/src/FUSINV/FusionInventory-Agent-2.1.5/Changes

* Fri Sep 10 2010 Remi Collet <Fedora@famillecollet.com> 2.1.3-2
- add %%check

* Sat Sep 04 2010 Remi Collet <Fedora@famillecollet.com> 2.1.3-1
- update to 2.1.3
  http://cpansearch.perl.org/src/FUSINV/FusionInventory-Agent-2.1.3/Changes

* Wed Aug 25 2010 Remi Collet <Fedora@famillecollet.com> 2.1.2-1
- update to 2.1.2
  http://cpansearch.perl.org/src/FUSINV/FusionInventory-Agent-2.1.2/Changes

* Wed Aug 18 2010 Remi Collet <Fedora@famillecollet.com> 2.1.1-1
- update to 2.1.1

* Wed Aug 18 2010 Remi Collet <Fedora@famillecollet.com> 2.1-2.gita7532c0
- update to git snaphost which fix EL issues
- fix init script
- adapt perl filter for recent/old fedora or EL

* Mon Aug 16 2010 Remi Collet <Fedora@famillecollet.com> 2.1-1
- update to 2.1
- switch download URL back to CPAN
- add %%{perl_vendorlib}/auto
- filter perl(Win32*) from Requires
- add patch (from git) to reopen the file logger if needed

* Sat May 29 2010 Remi Collet <Fedora@famillecollet.com> 2.0.6-1
- update to 2.0.6
- swicth download URL to forge

* Wed May 12 2010 Remi Collet <Fedora@famillecollet.com> 2.0.5-1
- update to 2.0.5

* Tue May 11 2010 Remi Collet <Fedora@famillecollet.com> 2.0.4-4.gitf7c5492
- git snapshot fix perl 5.8.8 (EL5) issue

* Sat May 08 2010 Remi Collet <Fedora@famillecollet.com> 2.0.4-4.gitddfdeaf
- git snapshot fix daemon issue
- add FUSINVOPT for global options (p.e.--debug)

* Sat May 08 2010 Remi Collet <Fedora@famillecollet.com> 2.0.4-3
- add support for daemon mode

* Fri May 07 2010 Remi Collet <Fedora@famillecollet.com> 2.0.4-2
- info about perl-FusionInventory-Agent-Task-OcsDeploy
- spec cleanup
- french translation
- set Net::CUPS and Archive::Extract optionnal on RHEL4

* Fri May 07 2010 Remi Collet <Fedora@famillecollet.com> 2.0.4-1
- update to 2.0.4 which fixes important bugs when cron is used

* Sat May 01 2010 Remi Collet <Fedora@famillecollet.com> 2.0.3-1
- initial spec

