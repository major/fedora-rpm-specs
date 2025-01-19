# This is really a noarch package, we're just building on all arches so we 
# can run unit tests across all arches.   The debuginfo will always be empty
# (no executables or libraries,) so we can disable it
%global debug_package %{nil}

Name:           metslib
Version:        0.5.3
Release:        33%{?dist}
Summary:        Metaheuristic modeling framework and optimization toolkit in modern C++

# Automatically converted from old format: GPLv3+ or CPL - review is highly recommended.
License:        GPL-3.0-or-later OR CPL-1.0
URL:            https://projects.coin-or.org/metslib
Source0:        http://www.coin-or.org/download/source/%{name}/%{name}-%{version}.tgz
# Removes all "libdir" paths from .pc file (which are unneeded).  Not upstream
Patch0:         %{name}-0.5.3-noarch.patch
# Port metslib to use boost random functionality instead of outdated tr1
# Based on https://github.com/PointCloudLibrary/pcl/commit/57ace9a92d1667eaa6193262032ff688e222ce0f
# Not upstream
Patch1:         %{name}-0.5.3-boost.patch
# Update abstract-search.hpp to remove deprecated exception specification
# Not upstream
Patch2:         %{name}-0.5.3-cpp17.patch

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  doxygen
BuildRequires:  boost-devel
BuildRequires:  graphviz

%description
%{summary}.

%package        devel
Summary:        Metaheuristic modeling framework and optimization toolkit in modern C++
Provides:       %{name}-static = %{version}-%{release}
BuildArch:      noarch
Requires:       boost-devel

%description    devel
METSlib is a metaheuristic modeling framework and optimization toolkit in
modern C++ released as Free/Libre/Open Source Software.

Model and algorithms are modular: any search algorithm can be applied to the
same model. On the other hand no assumption is made on the model, you can
work on any problem type: timetabling, assignment problems, vehicle routing,
bin-packing and so on.

Once you have implemented your model in the problem framework, the library
makes easy testing different Tabu Search strategies or even different
algorithms (Simulated Annealing or other local search based algorithms) with
a few lines of code.

%package doc
Summary:     Documentation for %{name}
BuildArch:   noarch

%description doc
The %{name}-doc package provides documentation for the %{name} library.

%prep
%setup -q
%patch -P0 -p0
%patch -P1 -p1 -b .boost
%patch -P2 -p1 -b .cpp17
# Disable -O3 optimization for unit tests
sed -i 's| -O3||g' configure

%build
export CXXFLAGS="%{optflags} --std=gnu++14"
%configure 
make %{?_smp_mflags}
doxygen doxydoc/doxygen.conf

%install
%make_install
# Move pkgconfig file to /usr/share/pkgconfig (since package is noarch)
mkdir -p %{buildroot}%{_datadir}
mv %{buildroot}%{_libdir}/pkgconfig %{buildroot}%{_datadir}

%check
export CXXFLAGS="%{optflags}" 
make test

%files devel
%doc AUTHORS COPYING NEWS README 
%{_includedir}/*
%{_datadir}/pkgconfig/*.pc

%files doc
%doc doxydoc/html COPYING

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 07 2024 Miroslav Suchý <msuchy@redhat.com> - 0.5.3-32
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 06 2022 Rich Mattes <richmattes@gmail.com> - 0.5.3-26
- Fix C++17 FTBFS

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 10 2021 Jeff Law <law@redhat.com> - 0.5.3-22
- Force C++14 as this code is not C++17 ready

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 0.5.3-12
- Rebuilt for s390x binutils bug

* Tue Jul 18 2017 Jonathan Wakely <jwakely@redhat.com> - 0.5.3-11
- Rebuilt for Boost 1.64

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 31 2016 Rich Mattes <richmattes@gmail.com> - 0.5.3-8
- Use boost for random functions

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 23 2013 Rich Mattes <richmattes@gmail.com> - 0.5.3-4
- Added -doc subpackage
- Fixed license to read GPLv3+ instead of GPLv3

* Thu Aug 22 2013 Rich Mattes <richmattes@gmail.com> - 0.5.3-3
- Remove -O3 from configure instead of configure.ac

* Sun Aug 11 2013 Rich Mattes <richmattes@gmail.com> - 0.5.3-2
- Removed metslib virtual provide
- Removed optimization flags from unit tests
- Added patch to remove libdir references from pkgconfig file

* Sun Aug 04 2013 Rich Mattes <richmattes@gmail.com> - 0.5.3-1
- Initial package
