%undefine __cmake_in_source_build
%global _docdir_fmt %{name}
%global abiver 4

Name:		ignition-math
Version:	4.0.0
Release:	17%{?dist}
Summary:	Small, Fast, High Performance Math Library

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:	Apache-2.0
URL:		http://ignitionrobotics.org/libraries/math
Source0:	http://gazebosim.org/distributions/ign-math/releases/%{name}%{abiver}-%{version}.tar.bz2
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:	cmake
BuildRequires:	doxygen
BuildRequires:  ignition-cmake-devel
BuildRequires:	graphviz
BuildRequires:	rubygem-ronn

# Work around math precision differences for non-sse processors
# Not yet submitted upstream
Patch0:         %{name}-4.0.0-387.patch

%description
Ignition Math is a component in the Ignition framework, a set of libraries
designed to rapidly develop robot applications. The library defines math
classes and functions used in other Ignition libraries and programs.

%package devel
Summary: Development files and libraries for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files and libraries
for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package doc
Summary: Development documentation for %{name}
BuildArch: noarch

%description doc
Generated API and development documentation for %{name}

%prep
%setup -q -n %{name}-%{version}
# Required to sneak in custom CFLAGS via CMAKE_C_FLAGS_ALL
sed -i 's/unset/#unset/g' CMakeLists.txt
%patch -P0 -p0 -b .387

%build
%cmake \
%ifnarch x86_64
  -DSSE2_FOUND=FALSE \
%endif
  -DSSE3_FOUND=FALSE \
  -DSSSE3_FOUND=FALSE \
  -DSSE4_1_FOUND=FALSE \
  -DSSE4_2_FOUND=FALSE \
  -DCMAKE_C_FLAGS_ALL="%{optflags}" \
  -DCMAKE_CXX_FLAGS_ALL="%{optflags}" \
  -DCMAKE_BUILD_TYPE=Release

%cmake_build
%cmake_build --target doc

%install
%cmake_install

%check
%ctest --verbose || exit 0

%files
%license COPYING
%doc README.md Changelog.md
%{_libdir}/*.so.%{version}
%{_libdir}/*.so.%{abiver}

%files devel
%{_libdir}/pkgconfig
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_includedir}/ignition

%files doc
%license COPYING
%doc %{_vpath_builddir}/doxygen/html

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 4.0.0-16
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 23 2018 Rich Mattes <richmattes@gmail.com> - 4.0.0-1
- Update to release 4.0 (rhbz#1652991)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 20 2017 Rich Mattes <richmattes@gmail.com> - 3.2.0-1
- Update to release 3.2.0

* Mon Aug 07 2017 Björn Esser <besser82@fedoraproject.org> - 3.0.0-5
- Rebuilt for AutoReq cmake-filesystem

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sun Feb 19 2017 Rich Mattes <richmattes@gmail.com> - 3.0.0-1
- Update to release 3.0.0
- Fix FTBFS (rhbz#1423733)
- Remove upstreamed patch
- Added a new fix for i686 non-SSE math

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jul 17 2016 Rich Mattes <richmattes@gmail.com> - 2.4.1-1
- Update to release 2.4.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Rich Mattes <richmattes@gmail.com> - 2.3.0-1
- Update to release 2.3.0

* Tue Oct 20 2015 Rich Mattes <richmattes@gmail.com> - 2.2.3-1
- Update to release 2.2.3

* Thu Aug 20 2015 Rich Mattes <richmattes@gmail.com> - 2.2.2-1
- Update to release 2.2.2

* Fri May 22 2015 Rich Mattes <richmattes@gmail.com> - 1.0.0-1
- Initial release (rhbz#1224390)
