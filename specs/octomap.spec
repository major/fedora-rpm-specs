%global soversion 1.9

Name:           octomap
Version:        1.9.8
Release:        7%{?dist}
Summary:        Efficient Probabilistic 3D Mapping Framework Based on Octrees

# octovis is GPLv2, octomap and dynamic-edt-3d are BSD
# Automatically converted from old format: BSD and GPLv2 - review is highly recommended.
License:        LicenseRef-Callaway-BSD AND GPL-2.0-only
URL:            http://octomap.github.io/
Source0:        https://github.com/OctoMap/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

# This patch moves CMake configuration files from datadir to libdir.
# It also disables -Werror to work around warnings described in #1862718
# Not submitted upstream
Patch0:         %{name}-1.9.8-libdir.patch
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libQGLViewer-qt5-devel
BuildRequires:  libXext-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel

%description
The OctoMap library implements a 3D occupancy grid mapping approach,
providing data structures and mapping algorithms in C++ particularly suited
for robotics. The map implementation is based on an octree.

%package devel
Summary:  Development files and libraries for %name
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files and development libraries
for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package doc
Summary:  HTML Documentation for %{name}
BuildArch: noarch

%description doc
This package contains doxygen-generated API documentation for %{name}

%package octovis
Summary: A visualization tool for Octomap

%description octovis
octovis is visualization tool for the OctoMap library based on Qt and
libQGLViewer
%package octovis-devel
Summary: Development files and libraries for %{name}
Requires: octomap-octovis%{?_isa} = %{version}-%{release}
Requires: octomap-devel%{?_isa} = %{version}-%{release}

%description octovis-devel
This package contains the header files and development libraries
for octovis. If you like to develop programs using octovis,
you will need to install octovis-devel.

%package -n dynamic-edt-3d
Summary:  Dynamic Euclidian Distance Transform Implementation

%description -n dynamic-edt-3d
The dynamicEDT3D library implements an incrementally updatable Euclidean
distance transform (EDT) in 3D. It comes with a wrapper to use the OctoMap
3D representation and hooks into the change detection of the OctoMap library
to propagate changes to the EDT.

%package -n dynamic-edt-3d-devel
Summary:  Development files and libraries for dynamic-edt-3d
Requires: dynamic-edt-3d%{?_isa} = %{version}-%{release}
Requires: octomap-devel%{?_isa} = %{version}-%{release}

%description -n dynamic-edt-3d-devel
This package contains the header files and development libraries
for dynamic-edt-3d. If you like to develop programs using dynamic-edt-3d,
you will need to install dynamic-edt-3d-devel.


%prep
%setup -q
%patch -P0 -p0 -b .libdir
# Remove bundled QGLViewer
rm -fr octovis/src/extern/

%build
%cmake \
  -DCMAKE_BUILD_TYPE=None

%cmake_build
%cmake_build --target docs

%install
%cmake_install

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
# Color octree comes out to be wrong size on ix86; ignore for now
%ctest --output-on-failure || exit 0

%ldconfig_scriptlets

%ldconfig_scriptlets -n %{name}-octovis

%ldconfig_scriptlets -n dynamic-edt-3d

%files
%license octomap/LICENSE.txt
%doc octomap/README.md octomap/CHANGELOG.txt octomap/AUTHORS.txt
%exclude %{_bindir}/octovis
%{_bindir}/*
%{_libdir}/liboctomap.so.%{version}
%{_libdir}/liboctomap.so.%{soversion}
%{_libdir}/liboctomath.so.%{version}
%{_libdir}/liboctomath.so.%{soversion}
%{_datadir}/%{name}
%{_datadir}/ament_index/resource_index/packages/octomap

%files devel
%{_includedir}/octomap
%{_libdir}/liboctomap.so
%{_libdir}/liboctomath.so
%{_libdir}/pkgconfig/octomap.pc
%{_libdir}/%{name}

%files doc
%license octomap/LICENSE.txt
%doc octomap/doc/html

%files octovis
%license octovis/LICENSE.txt
%doc octovis/README.md
%{_bindir}/octovis
%{_libdir}/liboctovis.so.%{version}
%{_libdir}/liboctovis.so.%{soversion}
%{_datadir}/octovis
%{_datadir}/ament_index/resource_index/packages/octovis

%files octovis-devel
%{_includedir}/octovis
%{_libdir}/liboctovis.so
%{_libdir}/octovis

%files -n dynamic-edt-3d
%license dynamicEDT3D/LICENSE.txt
%doc dynamicEDT3D/README.txt
%{_libdir}/libdynamicedt3d.so.%{version}
%{_libdir}/libdynamicedt3d.so.%{soversion}
%{_datadir}/dynamic_edt_3d
%{_datadir}/ament_index/resource_index/packages/dynamicEDT3D

%files -n dynamic-edt-3d-devel
%{_includedir}/dynamicEDT3D
%{_libdir}/libdynamicedt3d.so
%{_libdir}/pkgconfig/dynamicEDT3D.pc
%{_libdir}/dynamicEDT3D

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.9.8-6
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Feb 21 2023 Rich Mattes <richmattes@gmail.com> - 1.9.8-1
- Update to release 1.9.8

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 29 2022 Rich Mattes <richmattes@gmail.com> - 1.9.7-3
- Disable -Werror to work around warnings described in rhbz#1862718

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 06 2021 Rich Mattes <richmattes@gmail.com> - 1.9.7-1
- Update to release 1.9.7 (rhbz#1956597)

* Mon Feb 22 2021 Rich Mattes <richmattes@gmail.com> - 1.9.6-1
- Update to release 1.9.6 (rhbz#1919615)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Apr 18 2020 Rich Mattes <richmattes@gmail.com> - 1.9.5-2
- Fix CMake exports

* Sat Apr 18 2020 Rich Mattes <richmattes@gmail.com> - 1.9.5-1
- Update to release 1.9.5 (rhbz#1446806)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 03 2019 Rich Mattes <richmattes@gmail.com> - 1.8.1-8
- Update pkgconfig libdir (#1707514)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb 26 2017 Rich Mattes <richmattes@gmail.com> - 1.8.1-1
- Update to release 1.8.1 (rhbz#1413233)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jul 18 2016 Rich Mattes <richmattes@gmail.com> - 1.8.0-1
- Update to release 1.8.0 (rhbz#1329028)

* Sun Apr 03 2016 Rich Mattes <richmattes@gmail.com> - 1.7.2-1
- Update to release 1.7.2 (rhbz#1321432)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 31 2016 Rich Mattes <richmattes@gmail.com> - 1.7.1-1
- Update to release 1.7.1
- Switch to license macro
- Add changelog and readmes to documentation

* Fri Jan 01 2016 Rich Mattes <richmattes@gmail.com> - 1.7.0-1
- Update to release 1.7.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.6.8-2
- Rebuilt for GCC 5 C++11 ABI change

* Mon Oct 06 2014 Rich Mattes <richmattes@gmail.com> - 1.6.8-1
- Update to release 1.6.8

* Wed Sep 03 2014 Rich Mattes <richmattes@gmail.com> - 1.6.7-1
- Update to release 1.6.7

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 02 2014 Rich Mattes <richmattes@gmail.com> - 1.6.6-4
- Remove sbindir macro from ldconfig scriptlets

* Fri Jun 27 2014 Rich Mattes <richmattes@gmail.com> - 1.6.6-3
- Use sbindir macro

* Sat Jun 21 2014 Rich Mattes <richmattes@gmail.com> - 1.6.6-2
- Expand sub-package descriptions
- Clean up package separation

* Mon Jun 09 2014 Rich Mattes <richmattes@gmail.com> - 1.6.6-1
- Initial build (rhbz#1107422)
