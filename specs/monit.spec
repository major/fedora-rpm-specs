Name:           monit
Version:        5.34.4
Release:        1%{?dist}
Summary:        Manages and monitors processes, files, directories and devices

# Automatically converted from old format: AGPLv3
License:        AGPL-3.0-only
URL:            https://mmonit.com/monit/
Source0:        https://mmonit.com/monit/dist/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires: gcc
BuildRequires: flex
BuildRequires: openssl-devel
BuildRequires: pam-devel
BuildRequires: byacc
BuildRequires: systemd
BuildRequires: zlib-devel
BuildRequires: bison
BuildRequires: flex
BuildRequires: autoconf

%{?systemd_requires}
BuildRequires: systemd
BuildRequires: systemd-rpm-macros

%description
monit is a utility for managing and monitoring, processes, files, directories
and devices on a UNIX system. Monit conducts automatic maintenance and repair
and can execute meaningful causal actions in error situations.


%prep
%autosetup -p1

# Prevent-rerunning autoconf.
touch -r aclocal.m4 configure*
touch -r libmonit/aclocal.m4 libmonit/configure*

%build
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

install -p -D -m0600 monitrc $RPM_BUILD_ROOT%{_sysconfdir}/monitrc
install -p -D -m0755 monit $RPM_BUILD_ROOT%{_bindir}/monit

# systemd service file
mkdir -p ${RPM_BUILD_ROOT}%{_unitdir}
install -m0644 system/startup/monit.service ${RPM_BUILD_ROOT}%{_unitdir}/monit.service

# Let's include some good defaults
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/monit.d

%{__sed} -i 's/# set daemon  120.*/set daemon 60  # check services at 1-minute intervals/' \
    $RPM_BUILD_ROOT%{_sysconfdir}/monitrc

%{__sed} -i 's/#  include \/etc\/monit.d\/\*/include \/etc\/monit.d\/\*/' \
    $RPM_BUILD_ROOT%{_sysconfdir}/monitrc

%post
%systemd_post monit.service

# Moving old style configuration file to upstream's default location
[ -f %{_sysconfdir}/monit.conf ] &&
    touch -r %{_sysconfdir}/monitrc %{_sysconfdir}/monit.conf &&
    mv -f %{_sysconfdir}/monit.conf %{_sysconfdir}/monitrc 2> /dev/null || :

%preun
%systemd_preun monit.service

%postun
%systemd_postun_with_restart monit.service

%files
%doc CHANGES COPYING
%config(noreplace) %{_sysconfdir}/monitrc
%{_unitdir}/monit.service
%{_sysconfdir}/monit.d/
%{_bindir}/%{name}
%{_mandir}/man1/monit.1*

%changelog
* Sun Jan 12 2025 Stewart Adam <s.adam@diffingo.com> - 5.34.4-1
- Update to 5.34.4

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.33.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 17 2024 Miroslav Suchý <msuchy@redhat.com> - 5.33.0-4
- convert license to SPDX

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.33.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.33.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Stewart Adam <s.adam@diffingo.com> - 5.33.0-1
- Update to 5.33.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.32.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.32.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 12 2022 Florian Weimer <fweimer@redhat.com> - 5.32.0-3
- Port configure script to C99

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.32.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 6 2022 Stewart Adam <s.adam@diffingo.com> - 5.32.0-1
- Update to 5.32.0

* Thu Jan 20 2022 Stewart Adam <s.adam@diffingo.com> - 5.30.0-1
- Update to 5.30.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.26.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 5.26.0-6
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.26.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 5.26.0-4
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.26.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 3 2020 Stewart Adam <s.adam@diffingo.com> - 5.26.0-1
- Update to 5.26.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.25.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.25.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.25.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 5.25.1-5
- Rebuilt for libcrypt.so.2 (#1666033)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.25.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.25.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 5.25.1-2
- Rebuilt for switch to libxcrypt

* Tue Dec 26 2017 Stewart Adam <s.adam@diffingo.com> - 5.25.1-1
- Update to new upstream release 5.25.1 (#1311640, #1390112)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.19.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.19.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.19.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Oct 15 2016 Stewart Adam <s.adam@diffingo.com> - 5.19.0-1
- Update to upstream release 5.19.0, fixes #1325633
- Remove sysvinit conversion to systemd, fixes #1094916
- Remove logging to /var/log/monit.log in favor of logging to journald

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 12 2015 Stewart Adam <s.adam@diffingo.com> - 5.14-1
- Upgrading to new upstream release 5.14.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Dec 04 2013 Maxim Burgerhout <maxim@wzzrd.com> - 5.6.0-1
- Upgrading to new upstream release 5.6.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan 9 2012 Maxim Burgerhout <wzzrd@fedoraproject.org> - 5.3.1-3
- Fix systemd unit file

* Sun Jan 8 2012 Maxim Burgerhout <wzzrd@fedoraproject.org> - 5.3.1-2
- Rebuild for gcc 4.7

* Sun Nov 13 2011 Maxim Burgerhout <wzzrd@fedoraproject.org> - 5.3.1-1
- New upstream release 5.3.1
- Added systemd unit file and dropped sysv init support
- Dropped the patch that changed the default name of the configuration file
- Dropped the patch that silenced daemon startup

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.5-2
- Rebuilt for glibc bug#747377

* Sat May 07 2011 Maxim Burgerhout <wzzrd@fedoraproject.org> - 5.2.5-1
- Sync to upstream bugfix release; most important new features:
- Memory footprint decreased by 10%
- Logfile default umask changed to 0640
- New CLI command to test regexps for process names
- And various bugfixes

* Thu Aug 05 2010 Maxim Burgerhout <wzzrd@fedoraproject.org> - 5.2.3-1
- Update to new upstream version 5.2.3; new features in 5.2.3 include:
- MySQL protocol now support version 5.5
- Support for monitoring swap usage
- Allow process monitoring based on output of ps and regexps
- Various bugfixes

* Thu Aug 05 2010 Maxim Burgerhout <wzzrd@fedoraproject.org> - 5.1.1-2
- Enabled PAM authentication (bz #621599)

* Mon Jul 05 2010 Maxim Burgerhout <wzzrd@fedoraproject.org> - 5.1.1-1
- Version bump to 5.1.1 (needed new version of monit-no-startup-msg.patch)
- Ghosted the logfile

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 5.0.3-2
- rebuilt with new openssl

* Fri Aug 14 2009 Stewart Adam <s.adam at diffingo.com> - 5.0.3-1
- Update to 5.0.3 (thanks to Lubomir Rintel of Good Data for the patch)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 17 2009 Tomas Mraz <tmraz@redhat.com> 4.10.1-9
- rebuild with new openssl

* Mon Dec 22 2008 Stewart Adam <s.adam at diffingo.com> 4.10.1-8
- Tweak configuration defaults: include /etc/monit.d/*, log to /var/log/monit
  and set daemon time to 60s
- Don't use $desc in initscript
- Add patch to search for monit.conf by default (#475044)
- Add patch to remove redundant startup message

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 4.10.1-7
- Autorebuild for GCC 4.3

* Wed Dec 05 2007 Release Engineering <rel-eng at fedoraproject dot org> - 4.10.1-6
 - Rebuild for deps

* Wed Dec 5 2007 Stewart Adam <s.adam at diffingo.com> 4.10.1-5
- Rebuild to fix broken deps on libssl.so.6 and libcrypto.so.6

* Sat Nov 24 2007 Stewart Adam <s.adam at diffingo.com> 4.10.1-4
- Substitute RPM macros for their real values in monit.conf (#397671)

* Tue Nov 13 2007 Stewart Adam <s.adam at diffingo.com> 4.10.1-3
- Bump
- Fix changelog date for previous entry

* Mon Nov 12 2007 Stewart Adam <s.adam at diffingo.com> 4.10.1-2.1
- Switch back to OpenSSL since NSS isn't working too well with Monit

* Wed Nov 7 2007 Stewart Adam <s.adam at diffingo.com> 4.10.1-2
- License is actually GPLv3+
- s/%%{__install}/%%{__install} -p/
- NSS-ize

* Tue Nov 6 2007 Stewart Adam <s.adam at diffingo.com> 4.10.1-1
- Initial RPM release
