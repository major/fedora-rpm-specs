Name:		xbsql
Summary:	A SQL wrapper for xbase
Version:	0.11
Release:	48%{?dist}
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:	LicenseRef-Callaway-LGPLv2+
URL:		http://www.quaking.demon.co.uk/xbsql/
Source0: 	http://www.rekallrevealed.org/packages/%{name}-%{version}.tgz
BuildRequires:	make
BuildRequires:	gcc-c++, gcc
BuildRequires:	xbase-devel >= 3.1.2, ncurses-devel, readline-devel, bison, libtool
Patch0:		xbsql-0.11-ncurses64.patch
Patch1:		xbsql-0.11-xbase64.patch

%description
XBSQL is a wrapper library which provides an SQL-subset interface to Xbase 
DBMS.

%package devel
Summary: XBSQL development libraries and headers
Requires: %{name} = %{version}-%{release}
Requires: xbase-devel

%description devel
Headers and libraries for compiling programs that use the XBSQL library.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%configure --disable-rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags} CFLAGS="%{optflags}" CPPFLAGS="%{optflags}"

%install
make DESTDIR=$RPM_BUILD_ROOT install
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.la
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.a

%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS doc/*.html README
%{_libdir}/*.so.*
%{_bindir}/xql

%files devel
%{_includedir}/*
%{_libdir}/*.so

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.11-47
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 27 2021 Tom Callaway <spot@fedoraproject.org> - 0.11-39
- rebuild without rpath

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11-34
- Rebuild for readline 8.0

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Tom Callaway <spot@fedoraproject.org> - 0.11-32
- fix FTBFS

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.11-26
- Rebuild for readline 7.x

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.11-23
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 20 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 0.11-15
- don't package static lib (resolves bz 556100)
- use optflags when building

* Wed Aug 19 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 0.11-14
- update for new xbase

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Mar 11 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.11-11
- Rebuild against fixed (for gcc-4.3 compat) xbase

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.11-10
- Autorebuild for GCC 4.3

* Mon Aug 27 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.11-9
- license fix
- rebuild for BuildID

* Mon Sep 11 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.11-8
- missing BR: bison

* Mon Sep 11 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.11-7
- rebuild

* Tue Feb 28 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.11-6
- bump for FC-5

* Thu Aug 18 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.11-5
- fix 64 bit ncurses detection

* Thu Aug 18 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.11-4
- add the Requires: xbase-devel for the -devel package

* Mon Jul 18 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.11-3
- add BR: readline-devel

* Sun Jul 10 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.11-2
- shorten description
- add BuildRequires: ncurses-devel

* Fri Jun 17 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.11-1
- initial package for Fedora Extras
