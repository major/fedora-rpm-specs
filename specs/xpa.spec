%{!?tcl_version: %global tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl%{tcl_version}}

Name: xpa
Version: 2.1.20
Release: 5%{?dist}
Summary: The X Public Access messaging system

License: MIT
URL: http://hea-www.harvard.edu/RD/xpa/
Source0: https://github.com/ericmandel/xpa/archive/%{version}/%{name}-%{version}.tar.gz
Patch0: xpa-makefile.patch
Patch1: xpa-configure-c99.patch

BuildRequires: gcc
BuildRequires: make
BuildRequires: libXt-devel
BuildRequires: tcl-devel

Requires: tcl(abi) = 8.6

%description
The XPA messaging system provides seamless communication between many kinds 
of Unix programs, including X programs and Tcl/Tk programs. 
It also provides an easy way for users to communicate with these 
XPA-enabled programs by executing XPA client commands in the shell or by 
utilizing such commands in scripts.
This package contains command-line utilities for managing XPA.

%package devel
Summary: Headers for developing programs that will use %{name}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: %{name}-tcl%{?_isa} = %{version}-%{release}

%description devel
These are the header files and libraries needed to develop a %{name} 
application.

%package libs
Summary: The XPA messaging system runtime libraries
%description libs
The XPA messaging system provides seamless communication between many kinds 
of Unix programs, including X programs and Tcl/Tk programs. 
This package contains the %{name} run-time library

%package tcl
Summary: The XPA messaging system TCL interface
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Provides: tcl-xpa = %{version}-%{release}
%description tcl
The XPA messaging system provides seamless communication between many kinds 
of Unix programs, including X programs and Tcl/Tk programs. 
This package contains the %{name} TCL interface

%package doc
Summary: Documentation for %{name}
BuildArch: noarch

%description doc
This package contains the documentation for %{name}.

%prep
%autosetup -p1 -n %{name}-%{version}
# Remove ps files in html docs
rm -rf %{_builddir}/%{name}-%{version}/doc/*.ps

%build
%configure --includedir=%{_includedir}/xpa --datadir=%{_datadir}/xpa \
	--enable-shared --with-tcl=%{_libdir} \
	--with-x --enable-threaded-xpans
# Race condition
# the utilities are built before the shared library
# and linked with the static library
#make %{?_smp_mflags}
make 
#make %{?_smp_mflags} tclxpa
make tclxpa

%install
make INSTALL_ROOT=%{buildroot} install
mkdir -p %{buildroot}%{tcl_sitearch}/tclxpa
cp -a pkgIndex.tcl %{buildroot}%{tcl_sitearch}/tclxpa
mv %{buildroot}%{_libdir}/libtcl* %{buildroot}%{tcl_sitearch}/tclxpa

%ldconfig_scriptlets libs

%files
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/%{name}

%files libs
%license LICENSE
%{_libdir}/libxpa.so.*

%files tcl
%{tcl_sitearch}/tclxpa

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/xpa.pc
%{_includedir}/*
%{_mandir}/man3/*
%{_mandir}/mann/*
%exclude %{_libdir}/*.a

%files doc
%license LICENSE
%doc doc/*.html
#%doc doc/*.pdf

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Sergio Pascual <sergiopr@fedoraproject.org> - 2.1.20-1
- New upstream source (2.1.20)
- Use SPDX license (MIT)
- Add sources

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.19-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 10 2023 Peter Fordham <peter.fordham@gmail.com> - 2.1.19-9
- Port configure script to C99.

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.19-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.19-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.19-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jul 29 2019 Sergio Pascual <sergiopr@fedoraproject.org> - 2.1.19-1
- New upstream source (2.1.19)
- bz #1556557 is fixed upstream

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.18-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 04 2018 Sergio Pascual <sergiopr@fedoraproject.org> - 2.1.18-5
- Fix FTBFS (bz #1556557)
- License is MIT

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 16 2017 Sergio Pascual <sergiopr@fedoraproject.org> - 2.1.18-1
- New upstream source (2.1.18)
- Tarball from github
- Provide pkg-config file

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Nov 27 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 2.1.15-3
- Fix race condition, tools were built before the shared library

* Wed Oct 29 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 2.1.15-2
- isa macro in subpackage requires
- doc subpackage

* Mon Oct 27 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 2.1.15-1
- New upstream source (2.1.15)

* Sat Apr 16 2011 Sergio Pascual <sergiopr at fedoraproject.org> - 2.1.13-1
- New upstream source

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Feb 18 2010 Sergio Pascual <sergiopr at fedoraproject.org> - 2.1.12-1
- New upstream source

* Tue Dec 22 2009 Sergio Pascual <sergiopr at fedoraproject.org> - 2.1.11-1
- New upstream source

* Thu Sep 10 2009 Sergio Pascual <sergiopr at fedoraproject.org> - 2.1.10-1
- New upstream source

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 22 2008 Sergio Pascual <sergiopr at fedoraproject.org> 2.1.8-8
- Summary rewritten, description shortened

* Tue Jul 15 2008 Sergio Pascual <sergiopr at fedoraproject.org> 2.1.8-7
- Minor changes in the patch

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.1.8-6
- Autorebuild for GCC 4.3

* Thu Jan 03 2008 Sergio Pascual <sergiopr at fedoraproject.org> 2.1.8-5
- Following PackagingDrafts/Tcl

* Thu Jan 03 2008 Sergio Pascual <sergiopr at fedoraproject.org> 2.1.8-4
- Rebuilt for tcl 8.5

* Sat Dec 08 2007 Sergio Pascual <sergiopr at fedoraproject dot org> 2.1.8-3
- Tcl interface in a different subpackage
- pkgIndex.tcl added

* Wed Nov 14 2007 Sergio Pascual <sergiopr at fedoraproject dot org> 2.1.8-2
- Nested dir for headers fixed

* Tue Nov 13 2007 Sergio Pascual <sergiopr at fedoraproject dot org> 2.1.8-1
- New upstream source

* Sat Oct 13 2007 Sergio Pascual <sergiopr at fedoraproject dot org> 2.1.7-0.3.b2
- Splitted libraries in a new package

* Mon Aug 27 2007 Sergio Pascual <spr at astrax.fis.ucm.es> 2.1.7-0.2.b2.1
- Added /bin/awk to BuildReq

* Mon Aug 27 2007 Sergio Pascual <spr at astrax.fis.ucm.es> 2.1.7-0.2.b2
- Rebuild for Fedora 8 to get the build-id

* Wed Mar 21 2007 Sergio Pascual <spr at astrax.fis.ucm.es> 2.1.7-0.1.b2
- New upstream version 2.1.7b2

* Mon Feb 26 2007 Sergio Pascual <spr at astrax.fis.ucm.es> 2.1.6-9
- Back to tcl 8.4 due to stability problems

* Thu Feb 01 2007 Sergio Pascual <spr at astrax.fis.ucm.es> 2.1.6-8
- Rebuilt for devel (out of sync with tcl).

* Tue Sep 12 2006 Sergio Pascual <spr at astrax.fis.ucm.es> 2.1.6-7
- Rebuilt for FC6 (tag problem).

* Tue Sep 12 2006 Sergio Pascual <spr at astrax.fis.ucm.es> 2.1.6-6
- Rebuilt for FC6 (mass rebuild).

* Tue Jul 18 2006 Sergio Pascual <spr at astrax.fis.ucm.es> 2.1.6-5
- Changed BuildRequires to make common spec for FC-4 and up

* Thu Jun 22 2006 Sergio Pascual <spr at astrax.fis.ucm.es> 2.1.6-4
- Patch0 is modified so Makefile installs in $(libdir) instead of $(prefix)/lib

* Mon Jun 19 2006 Sergio Pascual <spr at astrax.fis.ucm.es> 2.1.6-3
- Added some space between package devel and description devel and
  between install and clean to improve the flow and readability of the file.

* Tue Jun 13 2006 Sergio Pascual <spr at astrax.fis.ucm.es> 2.1.6-2
- Specfile polished, minor fixes.

* Wed Feb 22 2006 Sergio Pascual <spr at astrax.fis.ucm.es> 2.1.6-1
- Initial spec file.
