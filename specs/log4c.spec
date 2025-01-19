Name:       log4c
Version:    1.2.4
Release:    33%{?dist}
Summary:    Library for logging application messages

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:    LicenseRef-Callaway-LGPLv2+
URL:        http://log4c.sourceforge.net/
Source0:    http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Double free or corruption with multiple log4c_init()/log4c_fini()
# https://bugzilla.redhat.com/show_bug.cgi?id=1095366
# Applied in upstream
Patch0:     reinit.patch
# Applied in upstream
Patch1:     format.patch

BuildRequires:  gcc-c++
BuildRequires:  doxygen
BuildRequires:  expat-devel
BuildRequires:  gcc
BuildRequires:  make

%description
Log4c is a C language library for flexible logging to files, syslog and other
destinations. It is modeled after the Log for Java library (log4j),
staying as close to their API as is reasonable.


%package devel
Summary:    Header files, libraries and development documentation for %{name}
Requires:   %{name} = %{version}-%{release}

%description devel
Log4c is a C language library for flexible logging to files, syslog and other
destinations. It is modeled after the Log for Java library (log4j),
staying as close to their API as is reasonable.

This package contains development files for %{name}. If you like to develop
programs using %{name}, you will need to install %{name}-devel.

%package doc
Summary:    Documentation for %{name}
BuildArch:  noarch

%description doc
Log4c is a C language library for flexible logging to files, syslog and other
destinations. It is modeled after the Log for Java library (log4j),
staying as close to their API as is reasonable.

This package contains %{name} documentation.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%configure --enable-doc --enable-test --disable-static
make %{?_smp_mflags}

%install
make install docdir=%{_pkgdocdir} DESTDIR=%{buildroot}
# example config file below shouldn't live in /etc/
mv %{buildroot}/etc/log4crc.sample %{buildroot}%{_pkgdocdir}/
rm %{buildroot}%{_libdir}/*.la
# munge log4c-config to prevent file conflicts on multilib systems,
# the default paths are not needed in the build flags anyway
sed -r -i \
    -e 's|^libdir=/usr/lib(64)?$|libdir=/usr/lib|' \
    -e 's|-L\$libdir ||' \
    -e 's|-I\$includedir ||' %{buildroot}%{_bindir}/log4c-config

%ldconfig_scriptlets

%files
%dir %{_pkgdocdir}/
%license %{_pkgdocdir}/COPYING
%{_pkgdocdir}/AUTHORS
%{_pkgdocdir}/ChangeLog
%{_pkgdocdir}/NEWS
%{_pkgdocdir}/README
%{_pkgdocdir}/log4crc.sample
%{_libdir}/liblog4c.so.3
%{_libdir}/liblog4c.so.3.*

%files devel
%{_libdir}/liblog4c.so
%{_libdir}/pkgconfig/*.pc
%{_bindir}/*
%{_includedir}/*
%{_datadir}/aclocal/log4c.m4
%{_mandir}/man1/*
%{_mandir}/man3/*

%files doc
%{_pkgdocdir}/html/


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.4-32
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jul 31 2023 František Dvořák <valtri@civ.zcu.cz> - 1.2.4-28
- Do not build pdf documentation (problem with doxygen-latext)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 14 2019 Steve Traylen <steve.traylen@cern.ch> - 1.2.4-19
- drop redundant _pkgdocdor
- whitespace cleanups in spec.
- Remove isa tags.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 06 2019 František Dvořák <valtri@civ.zcu.cz> - 1.2.4-17
- Update TeX BR (FTBFS)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 18 2018 František Dvořák <valtri@civ.zcu.cz> - 1.2.4-14
- Packaging updates (gcc BR)
- ps2pdf tool for doxygen (ghostscript BR)
- Format patch (FTBFS)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov 03 2016 František Dvořák <valtri@civ.zcu.cz> - 1.2.4-9
- Add %%{_pkgdocdir} directory

* Sat Feb 06 2016 František Dvořák <valtri@civ.zcu.cz> - 1.2.4-8
- Add BR: tex(tabu.sty) (FTBFS)
- Use %%license tag

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.2.4-6
- Add BR: tex(adjustbox.sty) (Fix FTBFS).

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 08 2014 František Dvořák <valtri@civ.zcu.cz> - 1.2.4-2
- Patch to fix library reinitialization (bug #1095366)

* Thu Oct 03 2013 František Dvořák <valtri@civ.zcu.cz> - 1.2.4-1
- Release log4c 1.2.4
- Add -doc subpackage

* Sun Jul 28 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.2.3-2
- Simplify install of docs.

* Sat Apr 06 2013 František Dvořák <valtri@civ.zcu.cz> - 1.2.3-1
- Release log4c 1.2.3
- Added pkgconfig file and the manpage for log4c-config

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Dec 08 2012 František Dvořák <valtri@civ.zcu.cz> - 1.2.2-2
- Unify log4c-config to make log4c-devel installable on multilib systems

* Tue Dec 04 2012 František Dvořák <valtri@civ.zcu.cz> - 1.2.2-1
- Release log4c 1.2.2
- Removed the m4 patch, now in upstream
- Arch-specific dependencies
- Correct description in devel subpackage
- Fixes from repeated review (license file, deprecated tags, ...)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Sep 05 2009 Alex (Fedora Packaging Account) <fedora@alexhudson.com> - 1.2.1-7
- Added patch to fix underquoting in M4 file (bug #507427)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 30 2009 Alex Hudson <fedora@alexhudson.com> - 1.2.1-3
- depend on automake for the m4 macro
- import into Fedora

* Mon Jan 26 2009 Alex Hudson <fedora@alexhudson.com> - 1.2.1-2
- new build-dep on expat for better config file parsing
- tidy source0 and use of macros
- .la files are removed after the build

* Tue Jan 13 2009 Alex Hudson <fedora@alexhudson.com> - 1.2.1-1
- Initial packaging attempt
