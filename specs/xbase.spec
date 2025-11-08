%global __cmake_in_source_build 1

Name:		xbase
Summary:	XBase compatible database library
Version:	4.2.6
Release:	1%{?dist}
License:	LGPL-3.0-or-later
URL:		http://linux.techass.com/projects/xdb/
Source0:	http://downloads.sourceforge.net/xdb/%{name}64-%{version}.tar.gz
Patch0:		xbase-4.2.6-fix-sover.patch
Patch1:		xbase-4.2.6-no-local-no-namespace.patch
Patch2:		xbase-4.2.6-fix-mandir.patch
Patch3:		xbase-4.2.6-missing-includes.patch
BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	doxygen, libtool, cmake
Provides:	xbase64 = %{version}-%{release}

%description
XBase is an xbase (i.e. dBase, FoxPro, etc.) compatible C++ class library
originally by Gary Kunkel and others (see the AUTHORS file).

XBase is useful for accessing data in legacy dBase 3 and 4 database files as
well as a general light-weight database engine.  It includes support for
DBF (dBase version 3 and 4) data files, NDX and NTX indexes, and DBT
(dBase version 3 and 4).  It supports file and record locking under *nix
OS's.

%package devel
Summary:	XBase development libraries and headers
Requires:	%{name}%{?_isa} = %{version}-%{release}
Provides:	xbase64-devel = %{version}-%{release}

%description devel
Headers and libraries for compiling programs that use the XBase library.

%package utils
Summary:	XBase utilities / tools
License:	GPL-3.0-or-later
Provides:	xbase64-utils = %{version}-%{release}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description utils
This package contains various utilities for working with X-Base files:
checkndx (check an NDX file), copydbf (copy a DBF file structure), deletall
(mark all records for deletion), dumphdr (print an X-Base file header),
dumprecs (dump records for an X-Base file), packdbf (pack a database file),
reindex (rebuild an index), undelall (undeletes all deleted records in a file),
zap (remove all records from a DBF file).

%prep
%setup -q -n %{name}64-%{version}
%patch -P0 -p1 -b .fix-sover
%patch -P1 -p1 -b .no-local-no-namespace
%patch -P2 -p1 -b .fix-mandir
%patch -P3 -p1 -b .missing-includes

chmod -x NEWS README docs/html/*

%build
cd build/linux64
%cmake .
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
pushd build/linux64
%cmake_install
popd
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.la

# Fix files for multilib
touch -r COPYING docs/html/*.html

pushd $RPM_BUILD_ROOT%{_libdir}
ln -s libxbase64.so.%{version} libxbase.so.%{version}
ln -s libxbase64.so.4 libxbase.so.4
ln -s libxbase64.so libxbase.so
popd

pushd $RPM_BUILD_ROOT%{_includedir}
ln -s Xbase64 xbase
popd

%check
pushd build/linux64
make test
popd

%ldconfig_scriptlets

%files
%license COPYING
%doc NEWS README
%{_libdir}/*.so.*

%files devel
%doc docs/html
%{_includedir}/xbase*
%{_includedir}/Xbase64
%{_libdir}/libxbase*.so

%files utils
%{_bindir}/xb_cfg_check
%{_bindir}/xb_clearix
%{_bindir}/xb_copydbf
%{_bindir}/xb_dbfutil
%{_bindir}/xb_deletall
%{_bindir}/xb_dumpdbt
%{_bindir}/xb_dumprecs
%{_bindir}/xb_execsql
%{_bindir}/xb_import
%{_bindir}/xb_pack
%{_bindir}/xb_reindex
%{_bindir}/xb_tblinfo
%{_bindir}/xb_undelall
%{_mandir}/man1/xb_*.1*

%changelog
* Thu Nov  6 2025 Tom Callaway <spot@fedoraproject.org> - 4.2.6-1
- so, funny story. turns out this thing is still being actively developed.
  and... i just noticed. whoops. sorry.
- anyways, new achievement: Back From The Dead
- update to 4.2.6

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 3.1.2-32
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 20 2017 Tom Callaway <spot@fedoraproject.org> - 3.1.2-15
- fix gcc7 ftbfs

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Feb 16 2016 Tom Callaway <spot@fedoraproject.org> - 3.1.2-13
- fix gcc6 ftbfs

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.1.2-10
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.2-4
- Rebuilt for c++ ABI breakage

* Thu Jan  5 2012 Tom Callaway <spot@fedoraproject.org> - 3.1.2-3
- Fix gcc 4.7.0 compile

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 19 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 3.1.2-1
- update to 3.1.2

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jun  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.0.0-13
- add ppc64 detection in configure (it's in the x86_64 patch)

* Thu Jun  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.0.0-12
- fix x86_64 detection in configure (FTBFS)

* Tue Mar 11 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 2.0.0-11
- Fix gcc4.3 patch to not polute global header namespace with
  "using namespace std;"

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.0.0-10
- Autorebuild for GCC 4.3

* Fri Jan 25 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 2.0.0-9
- Fix building with gcc 4.3 (also fixes building of xbase using packages)

* Tue Oct 30 2007 Tom "spot" Callaway <tcallawa@redhat.com> 2.0.0-8
- fix multilib conflicts

* Fri Aug 17 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.0.0-7
- Update License tag for new Licensing Guidelines compliance
- Add patch by Bill Nottingham to fix building on ppc64 (bz 239131)
- Don't build and install a static version of the lib
- Put the utilities/tools in a -utils sub package (to make clear they are under
  a different license)

* Mon Sep 11 2006 Tom "spot" Callaway <tcallawa@redhat.com> 2.0.0-6
- rebuild

* Sun Jun  4 2006 Tom "spot" Callaway <tcallawa@redhat.com> 2.0.0-5
- fix header file

* Tue Feb 28 2006 Tom "spot" Callaway <tcallawa@redhat.com> 2.0.0-4
- bump for FC-5

* Sun Jul 10 2005 Tom "spot" Callaway <tcallawa@redhat.com> 2.0.0-3
- fix xbase-config --ld (bugzilla 162845)

* Fri Jul  1 2005 Tom "spot" Callaway <tcallawa@redhat.com> 2.0.0-2
- add BuildRequires: doxygen
- remove latex docs (html is fine)

* Thu Jun 16 2005 Tom "spot" Callaway <tcallawa@redhat.com> 2.0.0-1
- initial package for Fedora Extras
