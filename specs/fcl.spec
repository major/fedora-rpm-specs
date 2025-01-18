%undefine __cmake_in_source_build
%define soversion 0.7

Name:           fcl
Version:        0.7.0
Release:        9%{?dist}
Summary:        Flexible Collision Library


# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/flexible-collision-library/fcl
Source0:        https://github.com/flexible-collision-library/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  eigen3-devel
BuildRequires:  flann-devel
BuildRequires:  gcc-c++
BuildRequires:  libccd-devel
BuildRequires:  octomap-devel
BuildRequires:  tinyxml-devel

%description
FCL is a library for performing three types of proximity queries on a pair
of geometric models composed of triangles.
* Collision detection: detecting whether the two models overlap, and
optionally, all of the triangles that overlap.
* Distance computation: computing the minimum distance between a pair
of models, i.e., the distance between the closest pair of points.
* Tolerance verification: determining whether two models are closer or
farther than a tolerance distance.
* Continuous collision detection: detecting whether the two moving models
overlap during the movement, and optionally, the time of contact.
* Contact information: for collision detection and continuous collision
detection, the contact information (including contact normals and contact
points) can be returned optionally.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{name}-%{version} -p 1

# Remove spurious executable permissions
find . -type f -perm /111 -name "*.h" -print -exec chmod -x '{}' \;
find . -type f -perm /111 -name "*.cpp" -print -exec chmod -x '{}' \;

# Use the distribution's default C++ standard version
sed -i 's/-std=c++11 //g' CMakeModules/CompilerSettings.cmake

%build
%cmake \
  -DCMAKE_BUILD_TYPE:STRING=Release \
  -DFCL_NO_DEFAULT_RPATH:BOOL=OFF \
  -DFCL_USE_HOST_NATIVE_ARCH:BOOL=OFF \
  -DFCL_USE_X64_SSE:BOOL=OFF
%cmake_build

%install
%cmake_install

%check
%ctest --output-on-failure || exit 0

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_libdir}/*.so.%{version}
%{_libdir}/*.so.%{soversion}
%{_datadir}/%{name}

%files devel
%{_includedir}/fcl
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/*
%{_libdir}/*.so

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 0.7.0-8
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 29 2022 Rich Mattes <richmattes@gmail.com> - 0.7.0-1
- Update to release 0.7.0 (rhbz#2003209)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jul 31 2021 Rich Mattes <richmattes@gmail.com> - 0.6.1-6
- Disable RPATH to fix FTBFS (rhbz#1987472)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 08 2020 Rich Mattes <richmattes@gmail.com> - 0.6.1-4
- Rebuild for flann-1.9.1

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Apr 18 2020 Rich Mattes <richmattes@gmail.com> - 0.6.1-1
- Update to release 0.6.1 (rhbz#1742044)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 0.5.0-9
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 07 2017 Björn Esser <besser82@fedoraproject.org> - 0.5.0-7
- Rebuilt for AutoReq cmake-filesystem

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Oct 21 2016 Rich Mattes <rmattes@fedoraproject.org> - 0.5.0-2
- Add License and Changelog to package
- Use git tag instead of git commit for source URL

* Sun Aug 14 2016 Rich Mattes <rmattes@fedoraproject.org> - 0.5.0-1
- Update to release 0.5.0
- Remove upstreamed patches
- Add missing license information from upstream commit
- Remove spurious executable permissions from source files

* Thu Jan 07 2016 Rich Mattes <rmattes@fedoraproject.org> - 0.3.2-2
- Add patch to correct install dirs and library versioning

* Sun Mar 01 2015 Rich Mattes <rmattes@fedoraproject.org> - 0.3.2-1
- Update to release 0.3.2

* Sun Jun 01 2014 Rich Mattes <rmattes@fedoraproject.org> - 0.3.1-1
- Initial build (rhbz#1103555)
