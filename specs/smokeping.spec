Summary:          Latency Logging and Graphing System
Name:             smokeping
Version:          2.8.2
Release:          11%{?dist}
License:          GPL-2.0-or-later AND GPL-3.0-or-later AND MIT
URL:              https://oss.oetiker.ch/smokeping/
Source0:          https://oss.oetiker.ch/smokeping/pub/smokeping-%{version}.tar.gz
Source1:          smokeping.service
Source2:          smokeping-httpd.conf.d
Source3:          http://oss.oetiker.ch/smokeping-demo/img/smokeping.png
Source4:          http://oss.oetiker.ch/smokeping-demo/img/rrdtool.png
Source5:          smokeping-tmpfs.conf
Source6:          smokeping-fix-ownership
Source7:          README.fedora
Patch0:           smokeping-2.8.2-paths.patch
Patch1:           smokeping-2.7.0-config.patch
Patch2:           smokeping-2.6.7-silence.patch
Patch3:           smokeping-2.8.2-no-3rd-party.patch
Patch4:           smokeping-2.8.2-remove-date.patch
BuildRequires:    /usr/bin/pod2man
BuildRequires:    automake
BuildRequires:    coreutils
BuildRequires:    glibc-common
BuildRequires:    make
BuildRequires:    perl(Authen::Radius)
BuildRequires:    perl(CGI)
BuildRequires:    perl(CGI::Fast)
BuildRequires:    perl(Config::Grammar)
BuildRequires:    perl(Data::Dumper)
BuildRequires:    perl(Digest::HMAC_MD5)
BuildRequires:    perl(Digest::MD5)
BuildRequires:    perl(ExtUtils::MakeMaker)
BuildRequires:    perl(ExtUtils::Manifest)
BuildRequires:    perl(FCGI)
BuildRequires:    perl(File::Basename)
BuildRequires:    perl(Getopt::Long)
BuildRequires:    perl(IO::Pty)
BuildRequires:    perl(IO::Socket::SSL)
BuildRequires:    perl(LWP)
BuildRequires:    perl(LWP::UserAgent)
BuildRequires:    perl(Net::DNS)
BuildRequires:    perl(Net::LDAP)
BuildRequires:    perl(Net::OpenSSH)
BuildRequires:    perl(Net::SNMP)
BuildRequires:    perl(Net::Telnet)
BuildRequires:    perl(POSIX)
BuildRequires:    perl(Pod::Usage)
BuildRequires:    perl(RRDs)
BuildRequires:    perl(SNMP_Session)
BuildRequires:    perl(SNMP_util) >= 1.13
BuildRequires:    perl(Safe)
BuildRequires:    perl(Socket6)
BuildRequires:    perl(Storable)
BuildRequires:    perl(Sys::Hostname)
BuildRequires:    perl(Sys::Syslog)
BuildRequires:    perl(Time::HiRes)
BuildRequires:    perl(URI::Escape)
BuildRequires:    perl(strict)
BuildRequires:    perl(vars)
BuildRequires:    perl(warnings)
BuildRequires:    perl-generators
BuildRequires:    systemd-units
BuildRequires:    autoconf
Requires:         findutils
Requires:         fping >= 2.4b2
# only httpd supported without config changes
Requires:         httpd
Requires:         mod_fcgid
# not picked up for some reason
Requires:         perl(Config::Grammar)
Requires:         perl(SNMP_util) >= 1.13
Requires:         perl-interpreter >= 5.6.1
Requires:         rrdtool >= 1.0.33
Requires:         traceroute
Requires(pre):    httpd
Requires(pre):    shadow-utils
BuildArch:        noarch
%global __provides_exclude_from %{_datadir}/%{name}/
%global __requires_exclude ^perl\\((Authen::.*|Net::OpenSSH|Smokeping)
%{?perl_default_filter}

%description
SmokePing is a latency logging and graphing system. It consists of a
daemon process which organizes the latency measurements and a CGI
which presents the graphs.

%prep
%autosetup -p1
install -p -m 0644 %{SOURCE7} .
iconv -f ISO-8859-1 -t utf-8 -o CHANGES.utf8 CHANGES
touch -r CHANGES CHANGES.utf8 
mv CHANGES.utf8 CHANGES

# remove some external modules
rm -f lib/{SNMP_Session,SNMP_util,BER}.pm
rm -rf thirdparty/
[ -e VERSION ] || echo %{version} > VERSION

%build
autoreconf --force --install --verbose --make

%configure --with-htdocs-dir=%{_datadir}/smokeping/htdocs \
    --disable-silent-rules

%install
%make_install

# Some additional dirs and files
install -d %{buildroot}%{_localstatedir}/lib/smokeping/{rrd,images} \
    %{buildroot}/run/smokeping %{buildroot}%{_datadir}/smokeping/cgi
install -Dp -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/smokeping.service
install -Dp -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/httpd/conf.d/smokeping.conf
install  -p -m 0644 %{SOURCE3} %{SOURCE4} %{buildroot}%{_datadir}/smokeping/htdocs
install -Dp -m 0644 %{SOURCE5} %{buildroot}%{_tmpfilesdir}/smokeping.conf
install -Dp -m 0755 %{SOURCE6} %{buildroot}%{_libexecdir}/smokeping-fix-ownership

# Fix some files
for f in config basepage.html smokemail tmail smokeping_secrets ; do
    mv %{buildroot}%{_sysconfdir}/smokeping/$f.dist \
       %{buildroot}%{_sysconfdir}/smokeping/$f
done
mv %{buildroot}%{_sysconfdir}/smokeping/examples __examples
mv %{buildroot}%{_bindir}/smokeping_cgi %{buildroot}%{_datadir}/smokeping/cgi
ln -s smokeping_cgi %{buildroot}%{_datadir}/smokeping/cgi/smokeping.fcgi
rm -f %{buildroot}%{_datadir}/smokeping/htdocs/smokeping.fcgi.dist

%pre
getent passwd smokeping >/dev/null || \
    useradd -r -g apache -d /var/lib/smokeping -s /sbin/nologin \
    -c "Smokeping" smokeping
exit 0

%post
%systemd_post smokeping.service

%preun
%systemd_preun smokeping.service

%postun
%systemd_postun_with_restart smokeping.service

%files
%license COPYRIGHT LICENSE
%doc CHANGES CONTRIBUTORS README.md TODO README.fedora
%doc __examples/*
%{_sbindir}/smokeping
%{_bindir}/smokeinfo
%{_bindir}/tSmoke
%{_libexecdir}/smokeping-fix-ownership
%{_unitdir}/smokeping.service
%dir %{_sysconfdir}/smokeping
%attr(0640, root, apache) %config(noreplace) %{_sysconfdir}/smokeping/config
%config(noreplace) %{_sysconfdir}/smokeping/basepage.html
%config(noreplace) %{_sysconfdir}/smokeping/smokemail
%attr(0640, root, root) %config(noreplace) %{_sysconfdir}/smokeping/smokeping_secrets
%config(noreplace) %{_sysconfdir}/smokeping/tmail
%config(noreplace) %{_sysconfdir}/httpd/conf.d/smokeping.conf
%{_tmpfilesdir}/smokeping.conf
%{_datadir}/smokeping
%dir %{_localstatedir}/lib/smokeping
%attr(0755, smokeping, apache) %{_localstatedir}/lib/smokeping/rrd
%attr(0755, smokeping, apache) /run/smokeping
%attr(0755, apache, apache) %{_localstatedir}/lib/smokeping/images
%{_mandir}/man1/smokeping*.1*
%{_mandir}/man1/smokeinfo*.1*
%{_mandir}/man1/tSmoke.1*
%{_mandir}/man3/Smokeping_*.3*
%{_mandir}/man5/smokeping_*.5*
%{_mandir}/man7/smokeping_*.7*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Oct 28 2024 Terje Rosten <terjeros@gmail.com> - 2.8.2-10
- Fix docs (rhbz#2274326)
- Use modern filter setup

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jul 07 2024 Terje Rosten <terje.rosten@ntnu.no> - 2.8.2-8
- systemd service fix

* Sun Apr 21 2024 Charles R. Anderson <cra@alum.wpi.edu> - 2.8.2-7
- Convert License tag to SPDX format and add missing licenses

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Sep 04 2021 Terje Rosten <terje.rosten@ntnu.no> - 2.8.2-1
- 2.8.2

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Mar 11 2021 Terje Rosten <terje.rosten@ntnu.no> - 2.7.3-5
- Use /run over /var/run

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.7.3-4
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 09 2020 Terje Rosten <terje.rosten@ntnu.no> - 2.7.3-1
- 2.7.3
- Run service as smokeping user

* Tue Mar 31 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.7.2-6
- Specify all perl dependencies needed for build

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 16 2018 Terje Rosten <terje.rosten@ntnu.no> - 2.7.2-1
- 2.7.2

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Terje Rosten <terje.rosten@ntnu.no> - 2.7.1-1
- 2.7.1

* Tue Oct 24 2017 Terje Rosten <terje.rosten@ntnu.no> - 2.6.11-7
- Update docs, resolving rhbz#1500881

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Petr Pisar <ppisar@redhat.com> - 2.6.11-5
- perl dependency renamed to perl-interpreter
  <https://fedoraproject.org/wiki/Changes/perl_Package_to_Install_Core_Modules>

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.6.11-4
- Rebuild due to bug in RPM (RHBZ #1468476)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 13 2017 Ville Skyttä <ville.skytta@iki.fi> - 2.6.11-2
- Move tmpfiles.d config to %%{_tmpfilesdir}

* Tue Oct 25 2016 Terje Rosten <terje.rosten@ntnu.no> - 2.6.11-1
- 2.6.11
- fix service file (rhbz#1388583)

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Oct 30 2014 Terje Rosten <terje.rosten@ntnu.no> - 2.6.10-1
- 2.6.10

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 26 2014 Terje Rosten <terje.rosten@ntnu.no> - 2.6.9-3
- Fix build

* Wed Mar 26 2014 Terje Rosten <terje.rosten@ntnu.no> - 2.6.9-2
- Let MTA add date header (bz #1080949)

* Mon Aug 05 2013 Terje Rosten <terje.rosten@ntnu.no> - 2.6.9-1
- 2.6.9

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 26 2013 Petr Pisar <ppisar@redhat.com> - 2.6.8-5
- Perl 5.18 rebuild
- Build-require Smokeping.pm dependencies as it is run when generating
  documentation
- Escape solidus in POD link

* Wed Feb 20 2013 Terje Rosten <terje.rosten@ntnu.no> - 2.6.8-4
- Fix buildreq.

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Dec 15 2012 Terje Rosten <terje.rosten@ntnu.no> - 2.6.8-2
- httpd 2.4 in FC 18 needs care (bz #871480)

* Thu Sep 06 2012 Terje Rosten <terje.rosten@ntnu.no> - 2.6.8-1
- 2.6.8
- Fix fping issue (bz #854572)
- Explicit dep on httpd (not just webserver) (bz #854804)

* Tue Aug 28 2012 Terje Rosten <terje.rosten@ntnu.no> - 2.6.7-4
- Convert to new set of macros for scripts

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Feb 09 2012 Terje Rosten <terje.rosten@ntnu.no> - 2.6.7-2
- Fix perl filtering

* Sun Feb 05 2012 Terje Rosten <terje.rosten@ntnu.no> - 2.6.7-1
- Switch to mod_fcgid as default
- Refresh patchset
- 2.6.7

* Sun Jan 22 2012 Terje Rosten <terje.rosten@ntnu.no> - 2.4.2-16
- Add patch to fix CVE-2012-0790 (#783584)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep 9 2011 Tom Callaway <spot@fedoraproject.org> - 2.4.2-14
- Add missing systemd scriptlets

* Fri Sep 9 2011 Tom Callaway <spot@fedoraproject.org> - 2.4.2-13
- Convert to systemd

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 17 2011 Terje Rosten <terje.rosten@ntnu.no> - 2.4.2-11
- Add tmpfiles.d file to fix #656690

* Sun Aug 16 2009 Terje Rosten <terje.rosten@ntnu.no> - 2.4.2-10
- Add patch to fix #497746

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Oct 27 2008 Terje Rosten <terje.rosten@ntnu.no> - 2.4.2-7
- Add some SELinux information, thanks to wolfy for help
  with this and other improvements.

* Sat Oct 18 2008 Terje Rosten <terje.rosten@ntnu.no> - 2.4.2-6
- Fix README.fedora

* Sun Oct  5 2008 Terje Rosten <terje.rosten@ntnu.no> - 2.4.2-5
- move Qooxdoo::JSONRPC to separate package

* Tue Sep 16 2008 Terje Rosten <terje.rosten@ntnu.no> - 2.4.2-4
- Use mv macro
- Fix cut-n-paste error in rm lines
- Remove perl as buildreq

* Mon Sep 15 2008 Terje Rosten <terje.rosten@ntnu.no> - 2.4.2-3
- Fix perms on writeable dir for apache
- More sane handling of external perl modules
- Add smoketrace instructions and patches

* Sat Aug 23 2008 Terje Rosten <terje.rosten@ntnu.no> - 2.4.2-2
- Fix README.fedora
- New rpm is picky, fixed

* Sat Aug 23 2008 Terje Rosten <terje.rosten@ntnu.no> - 2.4.2-1
- 2.4.2

* Thu Jul  3 2008 Terje Rosten <terje.rosten@ntnu.no> - 2.4.1-1
- 2.4.1

* Mon Apr  7 2008 Terje Rosten <terje.rosten@ntnu.no> - 2.3.5-1
- 2.3.5
- More or less a complete rewrite

* Sun Jan 14 2007 Wil Cooley <wcooley@nakedape.cc> - 2.0.9-2
- Disable internal dependency generator; I was doing this in my ~/.rpmmacros,
  which probably isn't a good idea.

* Tue Dec 05 2006 Wil Cooley <wcooley@nakedape.cc> - 2.0.9-1
- Updated to 2.0.9.
- Use 'dist' variable like Fedora Extras instead of vendor_tag and dist_tag.
- Do chkconfig/service in the correct places with appropriate checks.

* Wed Nov 09 2005 Wil Cooley <wcooley@nakedape.cc> - 2.0.4-0.0
- Updated to 2.0.4.
- Filter requirements for some internally-provided or optional modules.

* Tue Jun 21 2005 Wil Cooley <wcooley@nakedape.cc> - 2.0-0.2rc5
- Added chkconfig in post and preun sections.
- Changed some permissions to make rpmlint less unhappy.

* Thu Jun 16 2005 Wil Cooley <wcooley@nakedape.cc> - 2.0-2.nac.0.5
- Updated for 2.0rc5.

* Wed Mar 17 2004 Wil Cooley <wcooley@nakedape.cc> 1.28-2.nac
- Rebuilt for 1.28.
- Removed unnecessary stuff for setting up Apache.

* Fri Mar 12 2004 Curtis Doty <Curtis@GreenKey.net>
- [1.27] rebuilt without issue

* Sun Jan 25 2004 Curtis Doty <Curtis@GreenKey.net>
- [1.25] merge with upstream and hanecak
- add dependency on new perl-PersistentPerl (SpeedyCGI)
- use working config in the right location
- more rabid decrufting of hard-coded references to rrdtool

* Mon Oct 06 2003 Curtis Doty <Curtis@GreenKey.net>
- [1.24] merge with upstream
- change default config and doc to reflect loss coloring accurately
- rebuild man pages and html to reflect above, but forget txt
- remove IfModule mod_alias.c since apache2 cannot handle

* Thu Oct  2 2003 Peter Hanecak <hanecak@megaloman.sk> 1.23-1
- changed group from Networking/Utilities to Applications/Internet

* Wed Jul 30 2003 Curtis Doty <Curtis@GreenKey.net>
- [1.23] bump and build
- fix on Shrike since libnet subsumed by perl-5.8 and we really only
  need Net:SNMP out of it anyways
- quick hacks to make apache 2 compatible

* Tue Dec 17 2002 Curtis Doty <Curtis@GreenKey.net>
- [1.18] with some cosmetic changes
- add perl-libnet dependency neede for at least Net::SMTP
- maxhight patch so apache puts temp files in imgcache dir not datadir
- prefer my config.dist

* Sat Nov 02 2002 Curtis Doty <Curtis@GreenKey.net>
- [1.16] with updated specfile
- fix perms on /var/smokeping so apache cannot write
- fork and distribute my own defailt config instead of patching the
  screwey one that comes in the tarball

* Tue Mar 12 2002 Curtis Doty <Curtis@GreenKey.net>
- [1.5] with a bunch of my additions including SysV init script

* Tue Feb 19 2002 Curtis Doty <Curtis@GreenKey.net>
- new rpm package [1.1]
