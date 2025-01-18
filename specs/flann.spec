%undefine __cmake_in_source_build
%global srcname flann
%global soversion 1.9

Name:           flann
Version:        1.9.2
Release:        11%{?dist}
Summary:        Fast Library for Approximate Nearest Neighbors

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://www.cs.ubc.ca/research/flann
Source0:        https://www.github.com/mariusmuja/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

# Prevent the buildsysem from running setup.py, and use system-installed libflann.so
# Not submitted upstream
Patch0:         flann-1.9.1-fixpyflann.patch
# Distutils -> Setuptools
Patch3:         flann-1.9.2-py3.12.patch
# Install cmake scripts to correct libdir
Patch4:         flann-1.9.2-cmakeinstall.patch
# Fix pkgconfig file generation
Patch5:         flann-1.9.2-pkgconfig.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  zlib-devel
BuildRequires:  lz4-devel

BuildRequires:  hdf5-devel
BuildRequires:  gtest-devel

BuildRequires:  latex2html
BuildRequires:  texlive-bibtex
BuildRequires:  texlive-latex
BuildRequires:  texlive-%{!?rhel:scheme-}tetex

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
FLANN is a library for performing fast approximate nearest neighbor searches
in high dimensional spaces. It contains a collection of algorithms found
to work best for nearest neighbor search and a system for automatically
choosing the best algorithm and optimum parameters depending on the data sets.

%package devel
Summary: Development headers and libraries for flann
Requires: %{name}%{?_isa} = %{version}-%{release}
# flann/flann_mpi.hpp requires boost/mpi.hpp, which is a convenience header
# inside of the boost-devel package
Requires: boost-devel
# The cmake files get very unhappy if they can't find the static libs
Requires: %{name}-static%{?_isa} = %{version}-%{release}
# lz4 headers are exposed in the public API
Requires: lz4-devel

%description devel
Development headers and libraries for flann.

%package static
Summary: Static libraries for flann
Requires: %{name}-devel%{?_isa} = %{version}-%{release}

%description static
Static libraries for flann.

%package -n python3-flann
Summary: Python bindings for flann
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: python3-numpy
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-flann
Python 3 bindings for flann

%prep
%setup 
%patch 0 -p0 -b .fixpyflann
%patch 3 -p0 -b .py3.12
%patch 4 -p0 -b .cmakeinstall
%patch 5 -p0 -b .pkgconfig

# Fix library install directory
sed -i 's/"lib"/"%{_lib}"/' cmake/flann_utils.cmake

%build
%cmake -DBUILD_MATLAB_BINDINGS=OFF -DCMAKE_BUILD_TYPE=Release -DBUILD_PYTHON_BINDINGS=ON 
%cmake_build
%cmake_build %{!?rhel:--target} doc

%install
%cmake_install
rm -rf %{buildroot}%{_datadir}/%{name}/python

# install the python bindings
cp -r src/python src/python3

cp %{_vpath_builddir}/src/python/setup.py src/python3

pushd src/python3
%{__python3} setup.py install --prefix=/usr --root=%{buildroot} --install-lib=%{python3_sitearch}
popd

# get rid of duplicate shared libraries
rm -rf %{buildroot}%{python3_sitearch}/pyflann/lib
# Remove example binaries
rm -rf %{buildroot}%{_bindir}*
# Remove installed documentation, we'll install it later with the doc macro
rm -rf %{buildroot}%{_datadir}/doc/flann

%files
%doc doc/manual.pdf
%{_libdir}/*.so.%{version}
%{_libdir}/*.so.%{soversion}

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/flann
%{_libdir}/cmake/flann

%files static
%{_libdir}/*.a

%files -n python3-%{srcname}
%{python3_sitearch}/pyflann
%{python3_sitearch}/flann-%{version}*.egg-info

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Oct 25 2024 Orion Poplawski <orion@nwra.com> - 1.9.2-10
- Rebuild for hdf5 1.14.5

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 1.9.2-9
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 1.9.2-7
- Rebuilt for Python 3.13

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Nov 24 2023 Rich Mattes <richmattes@gmail.com> - 1.9.2-4
- Fix pkgconfig file and add lz4-devel requirement to -devel package
- Resolves: rhbz#2240334

* Thu Aug 10 2023 Tom Callaway <spot@fedoraproject.org> - 1.9.2-3
- the cmake files need to find the static libs or they error out, so -devel depends on -static now

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 17 2023 Rich Mattes <richmattes@gmail.com> - 1.9.2-1
- Update to release 1.9.2
- Resolves: rhbz#2155011, rhbz#2219994

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 1.9.1-10
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.9.1-7
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.9.1-4
- Rebuilt for Python 3.10

* Thu May 13 2021 Jeff Law <jlaw@tachyum.com> - 1.9.1-3
- Re-enable LTO

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 06 2020 Rich Mattes <richmattes@gmail.com> - 1.9.1-1
- Update to release 1.9.1
- Fix CMake macros (rhbz#1863563)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-28
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.8.4-26
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.8.4-24
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.8.4-23
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 16 2019 Orion Poplawski <orion@nwra.com>
- Rebuild for hdf5 1.10.5

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Miro Hrončok <mhroncok@redhat.com> - 1.8.4-19
- Remove the Python 2 subpackage (#1634633)

* Wed Jul 18 2018 Rich Mattes <richmattes@gmail.com> - 1.8.4-18
- Fix CMake error with no sources in library target

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.8.4-17
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 18 2017 Jonathan Wakely <jwakely@redhat.com> - 1.8.4-13
- Rebuilt for Boost 1.64

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.8.4-10
- Rebuild for Python 3.6

* Thu Oct 20 2016 Rich Mattes <richmattes@gmail.com> - 1.8.4-9
- Add python3 subpackage (rhbz#1323226)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.4-8
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun Feb 14 2016 Rich Mattes <richmattes@gmail.com> - 1.8.4-7
- Fix build error with gcc6/c++11 (rhbz#1307504)
- Clean up spec file

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.8.4-5
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Apr 28 2013 Rich Mattes <richmattes@gmail.com> - 1.8.4-1
- Update to release 1.8.4

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.8.1-3
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.8.1-2
- Rebuild for Boost-1.53.0

* Wed Dec 19 2012 Rich Mattes <richmattes@gmail.com> - 1.8.1-1
- Update to release 1.8.1

* Wed Oct 10 2012 Dan Horák <dan[at]danny.cz> - 1.7.1-5
- TBB is available only on selected arches

* Fri Sep 28 2012 Rich Mattes <richmattes@gmail.com> - 1.7.1-4
- Enabled tbb support

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-2
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Rich Mattes <richmattes@gmail.com> - 1.7.1-1
- Update to release 1.7.1

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 19 2011 Rich Mattes <richmattes@gmail.com> - 1.6.11-1
- Update to release 1.6.11

* Fri May 13 2011 Rich Mattes <richmattes@gmail.com> - 1.6.9-1
- Update to 1.6.9
- Make flann-devel require boost-devel for boost/mpi.hpp

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Feb 05 2011 Dan Horák <dan[at]danny.cz> - 1.6.7-6
- further updates for 64-bit systems (s390x, sparc64)

* Fri Feb 04 2011 Rich Mattes <richmattes@gmail.com> - 1.6.7-5
- Fixed ppc64 library installation paths (675316)

* Thu Feb 03 2011 Rich Mattes <richmattes@gmail.com> - 1.6.7-4
- Disabled hdf and ctest requirements for el6
- Explicit python26 dependency for el5

* Wed Feb 02 2011 Rich Mattes <richmattes@gmail.com> - 1.6.7-3
- Added clean section, rm buildroot at beginning of install
- Switched to using buildroot macro throughout specfile

* Mon Jan 31 2011 Rich Mattes <richmattes@gmail.com> - 1.6.7-2
- Fix exit() in shared lib error

* Wed Dec 22 2010 - Rich Mattes <richmattes@gmail.com> - 1.6.7-1
- Initial build
