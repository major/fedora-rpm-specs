%{?mingw_package_header}

%global mingw_pkg_name libsqlite3x

%global veryear 2007
%global vermon  10
%global verday  18

Name:           mingw-%{mingw_pkg_name}
Version:        %{veryear}%{vermon}%{verday}
Release:        42%{?dist}
Summary:        MinGW Windows C++ Wrapper for the SQLite3 embeddable SQL database engine

License:        zlib
URL:            http://www.wanderinghorse.net/computing/sqlite/
Source0:        http://www.wanderinghorse.net/computing/sqlite/%{mingw_pkg_name}-%{veryear}.%{vermon}.%{verday}.tar.gz
Source1:        libsqlite3x-autotools.tar.gz
Patch1:         libsqlite3x-prep.patch
Patch2:         libsqlite3x-includes.patch

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-sqlite
BuildRequires:  mingw64-sqlite
BuildRequires:  dos2unix
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  mingw32-filesystem >= 52
BuildRequires:  mingw64-filesystem >= 52
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw32-binutils
BuildRequires:  mingw64-binutils
BuildRequires:  mingw32-winpthreads
BuildRequires:  mingw64-winpthreads

%description
sqlite3 is a slick embedded SQL server written in C. It's easy to use,
powerful, and quite fast. sqlite3x is a C++ wrapper API for working
with sqlite3 databases that uses exceptions.

#Mingw32
%package -n      mingw32-%{mingw_pkg_name}
Summary:         MinGW Windows C++ Wrapper for the SQLite3 embeddable SQL database engine

%description -n mingw32-%{mingw_pkg_name}
sqlite3 is a slick embedded SQL server written in C. It's easy to use,
powerful, and quite fast. sqlite3x is a C++ wrapper API for working
with sqlite3 databases that uses exceptions.

%package -n     mingw32-libsq3
Summary:        MinGW Windows C++ Wrapper for the SQLite3 embeddable SQL database engine
Requires:       mingw32-%{mingw_pkg_name} = %{version}-%{release}

%description -n mingw32-libsq3
sqlite3 is a slick embedded SQL server written in C. It's easy to use,
powerful, and quite fast. sq3 is a C++ wrapper API for working
with sqlite3 databases that does not use exceptions.

#Mingw64
%package -n      mingw64-%{mingw_pkg_name}
Summary:         MinGW Windows C++ Wrapper for the SQLite3 embeddable SQL database engine

%description -n mingw64-%{mingw_pkg_name}
sqlite3 is a slick embedded SQL server written in C. It's easy to use,
powerful, and quite fast. sqlite3x is a C++ wrapper API for working
with sqlite3 databases that uses exceptions.

%package -n     mingw64-libsq3
Summary:        MinGW Windows C++ Wrapper for the SQLite3 embeddable SQL database engine
Requires:       mingw64-%{mingw_pkg_name} = %{version}-%{release}

%description -n mingw64-libsq3
sqlite3 is a slick embedded SQL server written in C. It's easy to use,
powerful, and quite fast. sq3 is a C++ wrapper API for working
with sqlite3 databases that does not use exceptions.

%{?mingw_debug_package}

%prep
%setup -q -n %{mingw_pkg_name}-%{veryear}.%{vermon}.%{verday} -a 1
dos2unix *.hpp *.cpp
%patch -P1 -p0 -b .prep
%patch -P2 -p0 -b .incl
aclocal
libtoolize -f
autoheader
autoconf
automake -a -c
%{mingw_configure} --disable-static
iconv -f iso8859-1 -t utf-8  < README > R
mv R README


%build
%{mingw_make}


%install
%{mingw_make} install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%files -n mingw32-libsqlite3x
%doc AUTHORS README Doxygen-index.txt
%{mingw32_bindir}/libsqlite3x-1.dll
%{mingw32_includedir}/sqlite3x
%{mingw32_libdir}/libsqlite3x.dll.a
%{mingw32_libdir}/pkgconfig/libsqlite3x.pc

%files -n mingw32-libsq3
%doc AUTHORS README Doxygen-index.txt
%{mingw32_bindir}/libsq3-1.dll
%{mingw32_includedir}/sq3
%{mingw32_libdir}/libsq3.dll.a
%{mingw32_libdir}/pkgconfig/libsq3.pc

%files -n mingw64-libsqlite3x
%doc AUTHORS README Doxygen-index.txt
%{mingw64_bindir}/libsqlite3x-1.dll
%{mingw64_includedir}/sqlite3x
%{mingw64_libdir}/libsqlite3x.dll.a
%{mingw64_libdir}/pkgconfig/libsqlite3x.pc

%files -n mingw64-libsq3
%doc AUTHORS README Doxygen-index.txt
%{mingw64_bindir}/libsq3-1.dll
%{mingw64_includedir}/sq3
%{mingw64_libdir}/libsq3.dll.a
%{mingw64_libdir}/pkgconfig/libsq3.pc

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20071018-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20071018-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20071018-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20071018-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20071018-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20071018-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 02 2022 Thomas Sailer <fedora@tsailer.ch> - 20071018-36
- Replace mingw-pthreads with mingw-winpthreads

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20071018-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 20071018-35
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20071018-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20071018-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20071018-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20071018-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20071018-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 20071018-29
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20071018-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20071018-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20071018-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20071018-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20071018-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20071018-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20071018-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20071018-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20071018-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jul 29 2013 Thomas Sailer <t.sailer@alumni.ethz.ch> - 20071018-19
- Rebuild to fix mingw64 unresolved symbols

* Sun Jan 27 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 20071018-18
- Rebuild against mingw-gcc 4.8 (win64 uses SEH exceptions now)

* Mon Aug 13 2012 Thomas Sailer <t.sailer@alumni.ethz.ch> - 20071018-17
- enable mingw64 build

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20071018-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 07 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 20071018-15
- Renamed the source package to mingw-libsqlite3x (RHBZ #800923)
- Use mingw macros without leading underscore
- Dropped unneeded RPM tags
- Dropped .la files
- Add explicit dependency on mingw32-pthreads

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 20071018-14
- Rebuild against the mingw-w64 toolchain

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20071018-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Apr 22 2011 Kalev Lember <kalev@smartlink.ee> - 20071018-12
- Rebuilt for pseudo-reloc version mismatch (#698827)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20071018-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul  8 2010 Thomas Sailer <t.sailer@alumni.ethz.ch> - 20071018-10
- conform to licensing guide update

* Thu Jul 30 2009 Jesse Keating <jkeating@redhat.com> - 20071018-9
- Bump for F12 mass rebulid.

* Mon Jun 22 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 20071018-8
- add debuginfo packages

* Tue Apr 28 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 20071018-7
- reorder BR/BA
- remove (duplicate) docs
- change License tag

* Mon Apr 27 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 20071018-6
- add missing BR

* Mon Mar 23 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 20071018-5
- unify main and devel subpackage

* Mon Mar 23 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 20071018-4
- copy from native package
