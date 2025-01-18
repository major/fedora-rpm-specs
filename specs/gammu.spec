%undefine __cmake_in_source_build
%bcond_without tests

Name:           gammu
Version:        1.42.0
Release:        18%{?dist}
Summary:        Command Line utility to work with mobile phones

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://wammu.eu/gammu/
Source0:        https://github.com/gammu/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         gammu-1.3.7-udev.patch
Patch1:         a37e5d8054f863fa71e38e244dd4da13eee6e251.patch

BuildRequires:  gcc
BuildRequires:  cmake3
BuildRequires:  autoconf
BuildRequires:  pkgconfig
BuildRequires:  gettext-devel
BuildRequires:  doxygen
%ifnarch s390 s390x
BuildRequires:  libusb1-devel
%endif
# Enabling bluetooth function
BuildRequires:  bluez-libs-devel
# Enabling Database sms function
%if 0%{?rhel} && 0%{?rhel} < 8
BuildRequires:  postgresql-devel
BuildRequires:  mysql-devel
%else
BuildRequires:  libpq-devel
BuildRequires:  mariadb-connector-c-devel
%endif

%if 0%{?fedora}
BuildRequires:  libdbi-devel
%endif
BuildRequires:  unixODBC-devel
#for tests
%if 0%{?fedora}
BuildRequires:  libdbi-dbd-sqlite
%endif
BuildRequires:  libcurl-devel
BuildRequires:  glib2-devel
BuildREquires:  libgudev1-devel
%if 0%{?fedora} >= 41
BuildRequires:  bash-completion-devel
%else
BuildRequires:  bash-completion
%endif

%{?systemd_requires}
BuildRequires: systemd-rpm-macros

Requires:       bluez
Requires:       dialog
# drive sqlite is in use by default
%if 0%{?fedora}
Requires:       libdbi-dbd-sqlite
%endif
# we should force the exact EVR for an ISA - not only the same ABI
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}


%package    libs
Summary:    Libraries files for %{name}

%package    devel
Summary:    Development files for %{name}

Requires:   %{name} = %{version}-%{release}
Requires:   %{name}-libs%{?_isa} = %{version}-%{release}
Requires:   pkgconfig

%description
Gammu is command line utility and library to work with mobile phones
from many vendors. Support for different models differs, but basic
functions should work with majority of them. Program can work with
contacts, messages (SMS, EMS and MMS), calendar, todos, filesystem,
integrated radio, camera, etc. It also supports daemon mode to send and
receive SMSes.

Currently supported phones include:

* Many Nokia models.
* Alcatel BE5 (501/701), BF5 (715), BH4 (535/735).
* AT capable phones (Siemens, Nokia, Alcatel, IPAQ).
* OBEX and IrMC capable phones (Sony-Ericsson, Motorola).
* Symbian phones through gnapplet.

This package contains Gammu binary as well as some examples.

%description    libs
The %{name}-libs package contains libraries files that used by %{name}

%description    devel
The %{name}-devel  package contains Header and libraries files for
developing applications that use %{name}


%prep
%setup -q
%patch -P0 -p1 -b .udev
%patch -P1 -p1

%build
%cmake3                  \
    -DENABLE_BACKUP=ON      \
    -DWITH_NOKIA_SUPPORT=ON     \
    -DWITH_Bluez=ON         \
    -DWITH_IrDA=ON          \
    -DINSTALL_UDEV_RULES=ON \
    -DINSTALL_GNAPPLET=ON       \
    -DINSTALL_MEDIA=ON       \
    -DINSTALL_PHP_EXAMPLES=ON       \
    -DINSTALL_BASH_COMPLETION=ON       \
    -DINSTALL_DOC=ON       \
    -DINSTALL_LOC=ON       \
    -DBUILD_SHARED_LIBS=ON \
    -DINSTALL_UDEV_RULES=ON \
    -DSYSTEMD_FOUND=ON \
    -DWITH_SYSTEMD=ON \
    -DSYSTEMD_SERVICES_INSTALL_DIR=%{_unitdir} \
    ../
%cmake_build

%install
%cmake_install

# Install config file
install -d %{buildroot}%{_sysconfdir}
install -pm 0644 docs/config/smsdrc %{buildroot}%{_sysconfdir}/gammu-smsdrc

%find_lang %{name}
%find_lang lib%{name}

%check
%if %{with tests}
# add %%{?_smp_mflags} breaks the tests
%global _smp_mflags %{nil}
%ctest3
%endif

%post
%systemd_post gammu-smsd.service

%preun
%systemd_preun gammu-smsd.service

%postun
%systemd_postun_with_restart gammu-smsd.service

%ldconfig_scriptlets -n %{name}-libs


%files -f %{name}.lang
%docdir %{_docdir}/%{name}
%{_docdir}/%{name}/README.rst
%{_docdir}/%{name}/ChangeLog
%{_docdir}/%{name}/examples
%license %{_docdir}/%{name}/COPYING
%config(noreplace) %{_sysconfdir}/gammu-smsdrc
%{_bindir}/%{name}*
%{_bindir}/jadmaker
%{_mandir}/man1/*.gz
%{_mandir}/man5/*.gz
%{_mandir}/man7/*.gz
#{_mandir}/cs/man1/*.gz
#{_mandir}/cs/man5/*.gz
#{_mandir}/cs/man7/*.gz
%{bash_completions_dir}/%{name}
%{_unitdir}/gammu-smsd.service
%{_datadir}/%{name}
%{_udevrulesdir}/69-gammu-acl.rules
#{_udevrulesdir}/45-nokiadku2.rules

%files libs -f lib%{name}.lang
%{_libdir}/*.so.*

%files devel
%doc %{_docdir}/%{name}/manual
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{name}


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.42.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.42.0-17
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.42.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat May 11 2024 Sérgio Basto <sergio@serjux.com> - 1.42.0-15
- Fix build issue with bash-completion on rawhide

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.42.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.42.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 01 2023 Sérgio Basto <sergio@serjux.com> - 1.42.0-12
- Fix one missing rpm spec condition for EPEL 9

* Wed Nov 01 2023 Sérgio Basto <sergio@serjux.com> - 1.42.0-11
- EPEL 9 don't have LibDBI

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.42.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Feb 21 2023 Filipe Rosset <rosset.filipe@gmail.com> - 1.42.0-9
- Fix FTBFS rhbz#2145274 and rhbz#2171496

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.42.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.42.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.42.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.42.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.42.0-4
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Mon Feb 08 2021 Pavel Raiskup <praiskup@redhat.com> - 1.42.0-3
- rebuild for libpq ABI fix rhbz#1908268

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.42.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Oct 03 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 1.42.0-1
- Update to 1.42.0 (#1884935)

* Sun Aug 02 2020 Sérgio Basto <sergio@serjux.com> - 1.41.0-4
- modernize spec

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.41.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild
- Fix cmake build

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.41.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 27 2019 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 1.41.0-1
- Update to 1.41.0 (#1756318)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.40.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 14 2019 Sérgio Basto <sergio@serjux.com> - 1.40.0-1
- Update to 1.40.0 (#1670142)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.39.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.39.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 21 2018 Sérgio Basto <sergio@serjux.com> - 1.39.0-3
- Remove old udev rule nokiadku2 because use the unknown group pludev (#1592452)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.39.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Fedora Release Monitoring  <release-monitoring@fedoraproject.org> - 1.39.0-1
- Update to 1.39.0 (#1531519)

* Sat Dec 23 2017 Sérgio Basto <sergio@serjux.com> - 1.38.5-4
- Yet another Epel fix

* Sat Dec 23 2017 Sérgio Basto <sergio@serjux.com> - 1.38.5-3
- Yet another Epel fix

* Sat Dec 23 2017 Sérgio Basto <sergio@serjux.com> - 1.38.5-2
- Epel fix

* Sat Dec 23 2017 Sérgio Basto <sergio@serjux.com> - 1.38.5-1
- Update to 1.38.5 (#1504333)
- Use cmake 3 for epel7 compatibility

* Thu Sep 21 2017 Sérgio Basto <sergio@serjux.com> - 1.38.4-2
- Use mariadb-connector-c-devel instead of mysql-devel or mariadb-devel
  (#1493625)

* Sun Aug 20 2017 Sérgio Basto <sergio@serjux.com> - 1.38.4-1
- Update to 1.38.4 (#1386437)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.37.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.37.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.37.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 03 2016 Sérgio Basto <sergio@serjux.com> - 1.37.4-2
- Force the exact EVR for gammu and gammu-libs

* Sun Aug 28 2016 Sérgio Basto <sergio@serjux.com> - 1.37.4-1
- 1.37.4

* Sun May 29 2016 Sérgio Basto <sergio@serjux.com> - 1.37.3-2
- A little package review with help of fedora-review

* Sun May 29 2016 Sérgio Basto <sergio@serjux.com> - 1.37.3-1
- Update gammu to 1.37.3

* Tue May 24 2016 Sérgio Basto <sergio@serjux.com> - 1.37.2-1
- Update gammu to 1.37.2

* Thu Feb 04 2016 Sérgio Basto <sergio@serjux.com> - 1.37.0-2
- Add BR:libdbi-dbd-sqlite and also require it because drive sqlite is used by
  default.

* Thu Feb 04 2016 Sérgio Basto <sergio@serjux.com> - 1.37.0-1
- Update to 1.37.0 (#1304358)
- Enable ctest in check stage to debug reported errors from SMSD.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.36.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 08 2015 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 1.36.8-1
- Update to 1.36.8 (#1289548)

* Wed Dec 02 2015 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 1.36.7-1
- Update to 1.36.7 (#1287349)

* Thu Nov 26 2015 Sérgio Basto <sergio@serjux.com> - 1.36.6-3
- Took some ideas from gammu.spec in upstream.
- Update description.
- Add /etc/gammu-smsdrc

* Tue Nov 24 2015 Sérgio Basto <sergio@serjux.com> - 1.36.6-2
- Enabled udev rules
- Add support for unixODBC.
- Better organization of spec, IMO.
- Make sure that install all examples and documentation.
- Added BuildRequires: bash-completion to not change localization of
  bash-completion

* Tue Nov 24 2015 Sérgio Basto <sergio@serjux.com> - 1.36.6-1
- Update gammu to 1.36.6

* Tue Jun 23 2015 Sérgio Basto <sergio@serjux.com> - 1.36.2-1
- Update to gammu-1.36.2 .

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.35.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 03 2015 Sérgio Basto <sergio@serjux.com> - 1.35.0-1
- Update to 1.35.0
- Rebuild for wxPython3

* Thu Jan 01 2015 Sérgio Basto <sergio@serjux.com> - 1.34.0-1
- New upstream release.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.33.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.33.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jan 22 2014 Sérgio Basto <sergio@serjux.com> - 1.33.0-2
- Rebuild for newer libdbi

* Sat Sep 07 2013 Sérgio Basto <sergio@serjux.com> - 1.33.0-1
- Update to lastest release.
- Pack all docs.
- fixed W: mixed-use-of-spaces-and-tabs with vim :retab

* Sat Aug 31 2013 Sérgio Basto <sergio@serjux.com> - 1.30.0-1
- Add BuildRequires glib2-devel libgudev1-devel
- Change mysql to mariadb.
- Thu Sep 29 2011 Karel Volny <kvolny@redhat.com>
  - Update release.
  - Patch gammu-1.26.1-exec.patch no longer needed.
  - Some docs are no longer present.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.26.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.26.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.26.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 27 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 1.26.1-8
- Update bluez run time requirements

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.26.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Mar 23 2011 Dan Horák <dan@danny.cz> - 1.26.1-6
- rebuilt for mysql 5.5.10 (soname bump in libmysqlclient)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.26.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 31 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 1.26.1-4
- Remove -Werror* from build flags. Needs real fix.

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 1.26.1-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Thu Jun 10 2010 Dan Horák <dan[at]danny.cz> - 1.26.1-2
- build without USB on s390(x)
- fixed FTBFS #555451

* Thu Dec 03 2009 Xavier Lamien <laxathom@fedoraproject.org> - 1.26.1-1
- Update release.

* Fri Aug 21 2009 Xavier Lamien <laxathom@fedorarproject.org> - 1.25.92-1
- Update release.

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 1.25.0-2
- rebuilt with new openssl

* Thu Aug 13 2009 Xavier Lamien <laxathom@fedorarproject.org> - 1.25.0-1
- Update release.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.24.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May  7 2009 Ville Skyttä <ville.skytta at iki.fi> - 1.24.0-2
- Build with $RPM_OPT_FLAGS, use %%cmake macro.

* Wed Apr 29 2009 Xavier Lamien <lxtnow@gmail.com> - 1.24.0-1
- Update release.

* Tue Apr 14 2009 Xavier Lamien <lxtnow@gmail.com> - 1.23.92-1
- Update release.

* Sun Apr 12 2009 Xavier Lamien <lxntow@gmail.com> - 1.23.1-1
- Update release.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22.94-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 10 2009 Xavier Lamien <lxtnow@gmail.com> - 1.22.94-1
- Update release.

* Mon Jan 26 2009 Xavier Lamien <lxtnow@gmail.com> - 1.22.90-3
- Make _libdir in a good shape.

* Mon Jan 26 2009 Tomas Mraz <tmraz@redhat.com> - 1.22.90-2
- rebuild with new openssl and mysql

* Sun Jan 11 2009 Xavier Lamien <lxtnow[at]gmail.com> - 1.22.90-1
- Update release.

* Tue Dec 30 2008 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.22.1-2
- Update release.
- -DENABLE_SHARED=ON replaced by -DBUILD_SHARED_LIBS=ON

* Sat Oct 11 2008 Xavier Lamien <lxtnow[at]gmail.com> - 1.21.0-1
- Update release.

* Thu Sep 11 2008 Xavier Lamien <lxtnow[at]gmail.com> - 1.20.90-2
- Rebuild against new libbluetooth.

* Mon Aug 25 2008 Xavier Lamien <lxtnow[at]gmail.com> - 1.20.90-1
- Update release.

* Mon Aug 25 2008 Xavier Lamien <lxntow[at]gmail.com> - 1.20.0-1
- Update release.

* Mon Jun 02 2008 Xavier Lamien <lxtnow[at]gmail.com> - 1.19.0-2
- Added Require dialog.

* Thu Apr 17 2008 Xavier Lamien <lxtnow[at]gmail.com> - 1.19.0-1
- Updated Release.

* Fri Feb 29 2008 Xavier Lamien <lxtnow[at]gmail.com> - 1.18.91-1
- Updated Release.

* Thu Feb 28 2008 Xavier Lamien <lxtnow[at]gmail.com> - 1.18.0-1
- Updated Release.

* Sat Jan 26 2008 Xavier Lamien < lxtnow[at]gmail.com > - 1.17.92-1
- Updated Release.
- Included new binary file.

* Sat Dec 22 2007 Xavier Lamien < lxtnow[at]gmail.com > - 1.17.0-1
- Updated Release.

* Fri Oct 12 2007 Xavier Lamien < lxtnow[at]gmail.com > - 1.13.0-1
- Updated Release.

* Wed Aug 01 2007 Xavier Lamien < lxtnow[at]gmail.com > - 1.12.92-1
- Updated Release.

* Wed Jul 25 2007 Xavier Lamien < lxtnow[at]gmail.com > - 1.12.91-1
- Updated Release.

* Thu May 24 2007 Xavier Lamien < lxtnow[at]gmail.com > - 1.11.0-1
- Updated release.

* Wed May 23 2007 Xavier Lamien < lxtnow[at]gmail.com > - 1.10.6-1
- Updated release.

* Tue May 08 2007 Xavier Lamien < lxtnow[at]gmail.com > - 1.10.0-1
- Initial RPM release.
