%undefine __cmake_in_source_build
%global debug_package %{nil}
%global major_version 0

Name:           ignition-cmake
Version:        0.6.1
Release:        20%{?dist}
Summary:        CMake modules to be used by the Ignition projects
Epoch:          1

#Most of the sources are Apache, but a couple of the CMake Find* modules are licensed as BSD
# Automatically converted from old format: ASL 2.0 and BSD - review is highly recommended.
License:        Apache-2.0 AND LicenseRef-Callaway-BSD
URL:            https://ignitionrobotics.org/libs/cmake
Source0:        http://gazebosim.org/distributions/ign-cmake/releases/%{name}-%{version}.tar.bz2
Patch0:         %{name}-0.6.1-noarch.patch
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake

%description
This package is required to build ignition projects, as well as to link your
own projects against them. It provides modules that are used to find
dependencies of ignition projects and generate cmake targets for consumers of
ignition projects to link against.

%package devel
Summary: CMake modules to be used by the Ignition projects
BuildArch: noarch

%description devel
This package is required to build ignition projects, as well as to link your
own projects against them. It provides modules that are used to find
dependencies of ignition projects and generate cmake targets for consumers of
ignition projects to link against.

%prep
%autosetup -p0 -S gendiff

%build
%cmake -DBUILD_TESTING=OFF -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

%files devel
%{_datadir}/cmake/%{name}%{major_version}
%{_datadir}/ignition

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.6.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1:0.6.1-19
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.6.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.6.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.6.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.6.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.6.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.6.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.6.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.6.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.6.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.6.1-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 23 2018 Rich Mattes <richmattes@gmail.com> - 1:0.6.1-4
- Remove architecture check from version file

* Fri Nov 23 2018 Rich Mattes <richmattes@gmail.com> - 1:0.6.1-3
- Make package architecture dependent, CMake version check is architecture-dependent (https://gitlab.kitware.com/cmake/cmake/issues/16184)

* Fri Nov 23 2018 Rich Mattes <richmattes@gmail.com> - 1:0.6.1-2
- Make package noarch

* Fri Nov 23 2018 Rich Mattes <richmattes@gmail.com> - 1:0.6.1-1
- Add epoch and downgrade to 0.x release series, required for gazebo9 and its dependencies

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.3.pre3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat May 19 2018 Rich Mattes <richmattes@gmail.com> - 1.0.0-0.2.pre3
- Remove shebang from non-executable scripts

* Sun May 13 2018 Rich Mattes <richmattes@gmail.com> - 1.0.0-0.1.pre3
- Initial package
