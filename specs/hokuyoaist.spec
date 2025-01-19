%undefine __cmake_in_source_build
%global commit b87a88aa66853d3c9d901d4e6be729c5fe69aae0
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global soversion 3

Name:           hokuyoaist
Version:        3.0.2
Release:        55%{?dist}
Summary:        Hokuyo Laser SCIP driver

# Automatically converted from old format: LGPLv3 - review is highly recommended.
License:        LGPL-3.0-only
URL:            https://github.com/gbiggs/hokuyoaist
Source0:        https://github.com/gbiggs/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
Patch0:         %{name}-3.0.2-fedora.patch
Patch1:         %{name}-3.0.2-const.patch
Patch2:         0c9870d-fix-boost-lib.patch
Patch3:         51d99dbc-python3-support.patch
Patch4:         %{name}-3.0.2-boostpython.patch

BuildRequires:  gcc-c++
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  flexiport-devel
BuildRequires:  graphviz
BuildRequires:  python3-devel
BuildRequires:  python3-sphinx

# Older gearbox versions include the hokuyo_aist library, but the hokuyo 
# library in gearbox 10.11 was relicensed to EPL.  This package conflcts 
# with gearbox versions that included the hokuyo_aist support (9.11), 
# but can be installed in parallel with gearbox version 10.11 (which
# is built without hokuyo_aist support)
Conflicts:      gearbox < 10.11

%description
This library provides a driver for Hokuyo laser scanner devices using the 
SCIP protocol version 1 or 2. It has been tested with the Hokuyo URG-04LX, 
UBG-04LX, UHG-08LX, UTM-30LX and UXM-30LX-E but it should work with any 
scanner that conforms to these protocol versions, including the URG-04LX-F01 
and the URG-04LX-UG01 (Simple-URG).

%package devel
Summary: Header files and libraries for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development libraries and header files for %{name}

%package -n python3-%{name}
%{?python_provide:%python_provide python3-%{name}}
Summary: Python bindings for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n python3-%{name}
Python bindings for %{name}

%prep
%setup -qn %{name}-%{commit}
%patch -P0 -p0 -b .fedora
%patch -P1 -p1 -b .const
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p0 -b .boostpython
# Fix the library and pkgconfig install paths.
#sed -i 's/\"lib\"/\"%{_lib}\"/' CMakeLists.txt 
# The "breathe" module is not available, so don't use it
sed -i 's/extensions/#extensions/' doc/conf.py.in
# Correct the project version in the CMakeLists.txt
sed -i 's/3.0.1/3.0.2/' CMakeLists.txt

%build
%cmake -DBUILD_EXAMPLES=OFF -DBOOST_LIB_SUFFIX="" -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

# Get rid of hidden junk doxygen generates, and remove the installed
# documentation so we can install it with the doc macro
rm -rf %{_vpath_builddir}/doc/html/.buildinfo
rm -rf %{_vpath_builddir}/doc/html/.doctrees
rm -rf %{buildroot}%{_docdir}/%{name}-3

%files
%doc COPYING COPYING.LESSER
%{_libdir}/*.so.%{version}
%{_libdir}/*.so.%{soversion}

%files devel
%doc %{_vpath_builddir}/doc/html
%{_datadir}/%{name}-3
%{_includedir}/%{name}-3
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/%{name}

%files -n python3-%{name}
%{python3_sitearch}/*.so

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 3.0.2-54
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 3.0.2-52
- Rebuilt for Python 3.13

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Jonathan Wakely <jwakely@redhat.com> - 3.0.2-49
- Rebuilt for Boost 1.83

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 3.0.2-47
- Rebuilt for Python 3.12

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 3.0.2-46
- Rebuilt for Boost 1.81

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 24 2022 Jonathan Wakely <jwakely@redhat.com> - 3.0.2-43
- Remove obsolete boost-python3-devel build dependency (#2100748)

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.0.2-42
- Rebuilt for Python 3.11

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 3.0.2-41
- Rebuilt for Boost 1.78

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Aug 06 2021 Jonathan Wakely <jwakely@redhat.com> - 3.0.2-39
- Rebuilt for Boost 1.76

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.0.2-37
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 3.0.2-35
- Rebuilt for Boost 1.75

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-34
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 29 2020 Jonathan Wakely <jwakely@redhat.com> - 3.0.2-32
- Rebuilt for Boost 1.73

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0.2-31
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.2-29
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 3.0.2-26
- Rebuilt for Boost 1.69

* Sat Dec 08 2018 Miro Hrončok <mhroncok@redhat.com> - 3.0.2-25
- Use python3-sphinx to build the docs

* Sat Nov 24 2018 Rich Mattes <richmattes@gmail.com> - 3.0.2-24
- Fix FTBFS (rhbz#1604332)
- Remove python2 package (rhbz#1634623)
- Enable upstream python3 support

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 3.0.2-21
- Rebuilt for Boost 1.66

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.0.2-20
- Python 2 binary package renamed to python2-hokuyoaist
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 3.0.2-17
- Rebuilt for s390x binutils bug

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 3.0.2-16
- Rebuilt for Boost 1.64

* Sun Mar 05 2017 Rich Mattes <richmattes@gmail.com> - 3.0.2-15
- Import upstream patches to fix FTBFS (rhbz#1423714) (rhbz#1307619)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-13
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 3.0.2-11
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 3.0.2-10
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 3.0.2-8
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 29 2015 Kalev Lember <kalevlember@gmail.com> - 3.0.2-6
- Rebuilt for GCC 5 ABI change

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 3.0.2-5
- Rebuild for boost 1.57.0

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Petr Machata <pmachata@redhat.com> - 3.0.2-2
- Rebuild for boost 1.55.0

* Tue Mar 25 2014 Rich Mattes <richmattes@gmail.com> - 3.0.2-1
- Update to release 3.0.2
- Add python bindings

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-3.20120729git69df78b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-2.20120729git69df78b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 29 2012 Rich Mattes <richmattes@gmail.com> - 3.0.1-1.20120729git69df78b
- Fix release numbering
