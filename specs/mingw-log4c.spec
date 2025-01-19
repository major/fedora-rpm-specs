%{?mingw_package_header}

Name:		mingw-log4c
Version:	1.2.4
Release:	26%{?dist}
Summary:	Library for logging application messages

# main license is LGPLv2
# src/sd/stack.c under MIT licence
# Automatically converted from old format: LGPLv2 and MIT - review is highly recommended.
License:	LicenseRef-Callaway-LGPLv2 AND LicenseRef-Callaway-MIT
URL:		http://log4c.sourceforge.net/
Source0:	http://downloads.sourceforge.net/log4c/log4c-%{version}.tar.gz

BuildArch:	noarch

BuildRequires: make
BuildRequires:	mingw32-filesystem >= 95
BuildRequires:	mingw32-gcc
BuildRequires:	mingw32-binutils
BuildRequires:	mingw32-expat

BuildRequires:	mingw64-filesystem >= 95
BuildRequires:	mingw64-gcc
BuildRequires:	mingw64-binutils
BuildRequires:	mingw64-expat

%description
Log4c is a C language library for flexible logging to files, syslog and other
destinations. It is modeled after the Log for Java library (log4j),
staying as close to their API as is reasonable.


%package -n mingw32-log4c
Summary:	MinGW compiled log4c library for the Win32 target

%description -n mingw32-log4c
Log4c is a C language library for flexible logging to files, syslog and other
destinations. It is modeled after the Log for Java library (log4j),
staying as close to their API as is reasonable.

This package is MinGW compiled log4c library for the Win32 target.


%package -n mingw64-log4c
Summary:	MinGW compiled log4c library for the Win64 target

%description -n mingw64-log4c
Log4c is a C language library for flexible logging to files, syslog and other
destinations. It is modeled after the Log for Java library (log4j),
staying as close to their API as is reasonable.

This package is MinGW compiled log4c library for the Win64 target.


%{?mingw_debug_package}


%prep
%setup -q -n log4c-%{version}


%build
%mingw_configure --disable-static
%mingw_make %{?_smp_mflags}


%install
%mingw_make_install DESTDIR=%{buildroot}
# example config file below shouldn't live in /etc/
rm %{buildroot}%{mingw32_sysconfdir}/log4crc.sample
rm %{buildroot}%{mingw64_sysconfdir}/log4crc.sample
# no libtool file
rm %{buildroot}%{mingw32_libdir}/*.la
rm %{buildroot}%{mingw64_libdir}/*.la
# .def is not neded to be as executable
chmod -x %{buildroot}%{mingw32_libdir}/*.def
chmod -x %{buildroot}%{mingw64_libdir}/*.def
# no duplicities in documentation
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}


%files -n mingw32-log4c
%doc COPYING AUTHORS ChangeLog NEWS README build_win32/log4crc.sample
%{mingw32_bindir}/liblog4c-3.dll
%{mingw32_bindir}/log4c-config
%{mingw32_includedir}/*
%{mingw32_libdir}/liblog4c.dll.a
%{mingw32_libdir}/liblog4c.def
%{mingw32_libdir}/pkgconfig/log4c.pc
%{mingw32_datadir}/aclocal/log4c.m4

%files -n mingw64-log4c
%doc COPYING AUTHORS ChangeLog NEWS README build_win64/log4crc.sample
%{mingw64_bindir}/liblog4c-3.dll
%{mingw64_bindir}/log4c-config
%{mingw64_includedir}/*
%{mingw64_libdir}/liblog4c.dll.a
%{mingw64_libdir}/liblog4c.def
%{mingw64_libdir}/pkgconfig/log4c.pc
%{mingw64_datadir}/aclocal/log4c.m4


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.4-25
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 1.2.4-18
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 1.2.4-12
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Nov 05 2013 František Dvořák <valtri@civ.zcu.cz> - 1.2.4-2
- Proper licensing

* Sun Oct 06 2013 František Dvořák <valtri@civ.zcu.cz> - 1.2.4-1
- Initial version
