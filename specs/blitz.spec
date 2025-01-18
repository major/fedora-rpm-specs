Name: blitz
Version: 1.0.2
Release: 20%{?dist}
Summary: C++ class library for matrix scientific computing

License: LGPL-3.0-only OR BSD-3-Clause OR Artistic-2.0

URL: https://github.com/blitzpp/blitz
Source0: https://github.com/blitzpp/blitz/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Modifications of the Fedora package are listed here:
# * Arch dependent header moved to lib/blitz/include
#   https://sourceforge.net/tracker/?func=detail&aid=3534421&group_id=63961&atid=505791
Source1: README.fedora
Patch0: blitz-cmake-path.patch

BuildRequires: gcc-c++
BuildRequires: gcc-gfortran doxygen texinfo graphviz
BuildRequires: cmake
BuildRequires: python3 texinfo-tex
BuildRequires: make

%description
Blitz++ is a C++ class library for scientific computing which provides 
performance on par with Fortran 77/90. It uses template techniques to achieve 
high performance. Blitz++ provides dense arrays and vectors, random number 
generators, and small vectors

%package devel
Summary: Libraries, includes, etc. used to develop an application with %{name}
Requires: %{name} = %{version}-%{release}
%description devel
These are the header files and libraries needed to develop a %{name}
application

%package doc
Summary: The Blitz html docs
BuildArch: noarch

%description doc
HTML documentation files for the Blitz Library

%prep
%setup -q
%patch -P0 -p1
cp %SOURCE1 .

%build
%cmake 
%cmake_build

# blitz.pc is created directly by configure
# I use sed to add %%libdir/blitz to the include directories of the library
# so that different bzconfig.h can be installed for different archs
# 
# The problem is reported here
# https://sourceforge.net/tracker/?func=detail&aid=2273091&group_id=63961&atid=505791
#%{__sed} -i -e "s/Cflags: -I\${includedir}/Cflags: -I\${includedir} -I\${libdir}\/blitz\/include/" blitz.pc

%install
%cmake_install

#mkdir -p %{buildroot}%{_libdir}/blitz/include/blitz
#mv %{buildroot}%{_includedir}/blitz/gnu %{buildroot}%{_libdir}/blitz/include/blitz

# Put in doc only the source code
rm -rf examples/.deps
rm -rf examples/Makefile*

%check
ctest -V %{?_smp_mflags}

%files
%doc AUTHORS README.md README.fedora
%license LEGAL COPYING COPYING.LESSER LICENSE
%{_libdir}/libblitz.so.*

%files devel
%doc examples
%{_libdir}/pkgconfig/*
%{_includedir}/blitz
%{_includedir}/random
%{_libdir}/cmake/*
%{_libdir}/libblitz.so
%exclude %{_libdir}/libblitz.a

%files doc
%doc AUTHORS README.md README.fedora
%license COPYING COPYING.LESSER LICENSE

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Dec 08 2024 Sergio Pascual <sergiopr at fedoraproject.org> - 1.0.2-19
- SPDX license review

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.2-18
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Mar 03 2022 Sergio Pascual <sergiopr@fedoraproject.org> - 1.0.2-11
- Fix cmake-of-source-build (bz #2045224)
- Fix wrong date in changelog

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 18 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 1.0.2-6
- EVR bump to rebuild

* Tue Aug 18 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 1.0.2-5
- Fix cmake out-of-source-build (bz #1863269)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 12 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 1.0.2-2
- Enable tests (patch by Tony REIX <tony.reix@atos.net>) 
- Add example code in -doc subpackage

* Sun Mar 01 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 1.0.2-1
- New version 1.0.2
- Building using cmake

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 2019 Sergio Pascual <sergiopr@fedoraproject.org> - 1.0.1-4
- Patch to use python2 instead of python

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 06 2018 Sergio Pascual <sergiopr@fedoraproject.org> - 1.0.1-1
- Change upstream url
- New version 1.0.1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.10-8
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jul 06 2012 Sergio Pascual <sergiopr at fedoraproject.org> - 0.10-2
- Licensing updated: LGPLv3+ or BSD os Artistic 2.0

* Sun Jul 01 2012 Sergio Pascual <sergiopr at fedoraproject.org> - 0.10-1
- New upstream source 

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 22 2009 Sergio Pascual <sergiopr at fedoraproject.org> - 0.9-13
- Using pregenerated documentation

* Sun Jul 26 2009 Sergio Pascual <sergiopr at fedoraproject.org> - 0.9-12
- Noarch doc subpackage

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May  7 2009 Ville Skyttä <ville.skytta at iki.fi> - 0.9-10
- Build with $RPM_OPT_FLAGS.
- Disable autotools dependency tracking during build for cleaner build logs
  and possible slight build speedup.

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 20 2009 Sergio Pascual <sergiopr at fedoraproject.org> - 0.9-8
- New patch (from upstream) to build with gcc4.3 

* Mon Mar 03 2008 Sergio Pascual <spr@astrax.fis.ucm.es> - 0.9-7
- Patch to build with gcc4.3

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9-6
- Autorebuild for GCC 4.3

* Mon Jan 07 2008 Sergio Pascual <spr@astrax.fis.ucm.es> 0.9-5
- Excluding /usr/share/info/dir

* Sat Dec 22 2007 Sergio Pascual <sergiopr at fedoraproject.com> 0.9-4
- Removed conflicting Makefiles from examples (bug #340751)
- Arch dependent gnu/bzconfig.h moved to %%libdir/blitz/include/blitz/gnu

* Wed Oct 17 2007 Sergio Pascual <spr@astrax.fis.ucm.es> 0.9-3
- Removed macro in changelog

* Tue Oct 16 2007 Sergio Pascual <spr@astrax.fis.ucm.es> 0.9-2
- Excluding /usr/share/info/dir

* Wed Oct 03 2007 Sergio Pascual <spr@astrax.fis.ucm.es> 0.9-1
- Changed wrong date in changelog
- Changed license to gplv2 (some .h files haven't got the license text)
- Changed _datadir/info/* to _infodir/%%{name}*

* Tue Oct 02 2007 Sergio Pascual <spr@astrax.fis.ucm.es> 0.9-0.2
- Adding requires pkgconfig
- Changed license tag
- Removing requires(pre,un)

* Thu May 03 2007 Sergio Pascual <spr@astrax.fis.ucm.es> 0.9-0.1
- Initial RPM file
