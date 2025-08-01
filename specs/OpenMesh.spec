%global major_version 11
%global minor_version 0
%global patch_version 0
%global pkg_version %{major_version}.%{minor_version}.%{patch_version}
%global short_version %{major_version}.%{minor_version}

Name:           OpenMesh
Version:        %{pkg_version}
Release:        5%{?dist}
Summary:        A generic and efficient polygon mesh data structure
License:        BSD-3-Clause
URL:            http://www.openmesh.org/
Source0:        https://www.graphics.rwth-aachen.de/media/openmesh_static/Releases/%{short_version}/OpenMesh-%{version}.tar.bz2
Source1:        README.Fedora

# Re-enable the possibility to use find_package(GTest), the gtest-devel package,
# for unit tests, instead of using CMake FetchContent and git to retrieve the GTest sources.
Patch0:         OpenMesh-11.0.0-gtest.patch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  desktop-file-utils
BuildRequires:  texlive-latex-bin
BuildRequires:  texlive-dvips-bin
BuildRequires:  texlive-makeindex-bin
BuildRequires:  texlive-newunicodechar
BuildRequires:  rdfind
BuildRequires:  symlinks
BuildRequires:  gtest-devel
BuildRequires:  eigen3-devel

%description
OpenMesh is a generic and efficient data structure for representing
and manipulating polygonal meshes.

%package devel
Summary:        Development headers and libraries for OpenMesh
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains development headers and libraries necessary to
compile programs against OpenMesh.

%package doc
Summary:        Doxygen documentation for OpenMesh
BuildArch:      noarch

%description doc
This package contains the Doxygen documentation for OpenMesh.

%package tools
Summary:        OpenMesh tools
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description tools
This package contains the applications that ship with OpenMesh.

%global OpenMesh_apps Analyzer commandlineAdaptiveSubdivider commandlineDecimater commandlineSubdivider DecimaterGui Dualizer mconvert mkbalancedpm ProgViewer QtViewer Smoothing SubdividerGui Synthesizer

%prep
%setup -q
%patch 0 -p1 -b .gtest
cp -p %{SOURCE1} .

# Generate desktop files
for xb in %{OpenMesh_apps}; do
    cat > om_${xb}.desktop <<EOF
[Desktop Entry]
Name=OpenMesh $xb
Exec=%{_libdir}/%{name}/$xb
Terminal=false
Type=Application
StartupNotify=true
Categories=Utility;Science
EOF
done

%build
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%{cmake} -DCMAKE_BUILD_TYPE=RELEASE -DQT_VERSION=6 -DOPENMESH_BUILD_UNIT_TESTS=ON \
%if "%{?_lib}" == "lib64"
    %{?_cmake_lib_suffix64} \
%endif

%{cmake_build}
%{cmake_build} -t doc

# deduplicate documentation files (to avoid an rpmlint error in OpenMesh-doc.noarch)
rdfind -makesymlinks true %{_vpath_builddir}/Build/share/OpenMesh/Doc/html
symlinks -rc %{_vpath_builddir}/Build/share/OpenMesh/Doc/html

%check
%ifnarch s390x
%ctest -j1 # Run tests sequentially to avoid I/O conflicts
%endif

%install
%cmake_install

# Get rid of static libraries
rm %{buildroot}%{_libdir}/*.a

# Get rid of unit tests
rm %{buildroot}%{_bindir}/unittests*

# Move OpenMesh pkgconfig file
mkdir -p %{buildroot}%{_libdir}/pkgconfig
mv %{buildroot}/*/*/pkgconfig/openmesh.pc %{buildroot}%{_libdir}/pkgconfig/openmesh.pc

# Move OpenMeshConfig-release.cmake and OpenMeshConfig.cmake to libdir
mkdir -p %{buildroot}%{_libdir}/cmake/OpenMesh
mv %{buildroot}/%{_datadir}/OpenMesh/cmake/OpenMeshConfig*cmake %{buildroot}%{_libdir}/cmake/OpenMesh/

# Tools have names that are too generic. Install them in a different place
mkdir -p %{buildroot}%{_libdir}/%{name}
mv %{buildroot}%{_bindir}/* %{buildroot}%{_libdir}/%{name}/
# and generate om_ prefixed symlinks
pushd %{buildroot}%{_libdir}/%{name}/
for b in *; do
    ln -s ../%{_lib}/%{name}/$b %{buildroot}%{_bindir}/om_$b
done
popd

touch tools-files.txt

# Install desktop files
for xb in %{OpenMesh_apps}; do
    desktop-file-install --dir=%{buildroot}%{_datadir}/applications om_${xb}.desktop
    echo "%{_libdir}/%{name}/$xb" >> tools-files.txt
    echo "%{_bindir}/om_$xb" >> tools-files.txt
    echo "%{_datadir}/applications/om_${xb}.desktop" >> tools-files.txt
done

%ldconfig_scriptlets

%files
%doc CHANGELOG.md README.md README.Fedora
%license LICENSE
%{_libdir}/libOpenMesh*.so.%{short_version}

%files -f tools-files.txt tools

%files devel
%{_includedir}/OpenMesh/
%{_libdir}/libOpenMesh*.so
%{_libdir}/pkgconfig/openmesh.pc
%{_libdir}/cmake/OpenMesh

%files doc
%doc LICENSE
%doc %{_vpath_builddir}/Build/share/OpenMesh/Doc/html/*

%changelog
* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon May 19 2025 Laurent Rineau <laurent.rineau@cgal.org> - 11.0.0-4
- Fix ctest invocation to prevent parallel execution during I/O tests

* Tue May 06 2025 Cristian Le <git@lecris.dev> - 11.0.0-3
- Allow CMake 4.0 build
- Use standard cmake macros

* Tue Mar 11 2025 Laurent Rineau <laurent.rineau@cgal.org> - 11.0.0-2
- add missing build requirements for the OpenMesh test suite
- temporarily disable the tests on s390x, because the I/O functions of OpenMesh
  seem to be broken on that architecture, for now.

* Tue Mar 11 2025 Laurent Rineau <laurent.rineau@cgal.org> - 11.0.0-1
- Update to version 11.0.0
- drop the two patches
- use Qt6 instead of Qt5
- build the unit tests and add a check section

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 05 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 6.3-11
- Adapt to new CMake scripts.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-10
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 17 2019 Gwyn Ciesla <gwync@protonmail.com> - 6.3-7
- Rebuilt for new freeglut

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 28 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 6.3-3
- Added gcc buildrequires.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 12 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 6.3-1
- Update to 6.3.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Sep 21 2015 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.1-1
- Update to 4.1.

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.2-4
- Rebuilt for GCC 5 C++11 ABI change

* Tue Feb 24 2015 Dominik Mierzejewski <rpm@greysector.net> - 3.2-3
- Rebuild with gcc-5.0 (blocks IQmol rebuild)

* Sun Aug 24 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.2-2
- Review fixes.

* Wed Aug 20 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.2-1
- Initial package.
