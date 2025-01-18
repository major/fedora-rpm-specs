Name:           OpenMesh
Version:        6.3
Release:        21%{?dist}
Summary:        A generic and efficient polygon mesh data structure
License:        BSD-3-Clause
URL:            http://www.openmesh.org/
Source0:        https://www.graphics.rwth-aachen.de/media/openmesh_static/Releases/%{version}/OpenMesh-%{version}.tar.bz2
Source1:        README.Fedora
# Fedora specifics
Patch0:         OpenMesh-4.1-fedora.patch
# Fix build with GCC7, from upstream
Patch1:         OpenMesh-acb62194f4268651250cda546dc8c93610893877.patch

BuildRequires: make
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libICE-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  freeglut-devel
BuildRequires:  qt4-devel
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  desktop-file-utils
BuildRequires:  texlive-newunicodechar

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

%prep
%setup -q
%patch -P0 -p1 -b .fedora
%patch -P1 -p1 -b .gcc7
cp -p %{SOURCE1} .

# Generate desktop files
for xb in DecimaterGui ProgViewer QtViewer SubdividerGui Synthesizer; do
    cat > om_${xb}.desktop <<EOF
[Desktop Entry]
Name=$xb
Exec=%{_libdir}/%{name}/$xb
Terminal=false
Type=Application
StartupNotify=true
Categories=Utility;Science
EOF
done

%build
%{cmake} -DCMAKE_BUILD_TYPE=RELEASE
%{cmake_build}
make -C %{_vpath_builddir} %{?_smp_mflags}
make -C %{_vpath_builddir} doc %{?_smp_mflags}

%install
make -C %{_vpath_builddir}/src/OpenMesh/Apps install DESTDIR=%{buildroot}
make -C %{_vpath_builddir}/src/OpenMesh/Core install DESTDIR=%{buildroot}
make -C %{_vpath_builddir}/src/OpenMesh/Tools install DESTDIR=%{buildroot}

# Get rid of static libraries
rm %{buildroot}%{_libdir}/*.a

# Tools have names that are too generic. Install them in a different place
mkdir -p %{buildroot}%{_libdir}/%{name}
mv %{buildroot}%{_bindir}/* %{buildroot}%{_libdir}/%{name}/
# and generate om_ prefixed symlinks
pushd %{buildroot}%{_libdir}/%{name}/
for b in *; do
    ln -s %{_libdir}/%{name}/$b %{buildroot}%{_bindir}/om_$b
done
popd

# Install desktop files
for xb in DecimaterGui ProgViewer QtViewer SubdividerGui Synthesizer; do
    desktop-file-install --dir=%{buildroot}%{_datadir}/applications om_${xb}.desktop
done

%ldconfig_scriptlets

%files
%doc CHANGELOG.md README.md README.Fedora VERSION
%license LICENSE
%{_libdir}/libOpenMesh*.so.*

%files tools
%{_datadir}/applications/om_*.desktop
%{_libdir}/OpenMesh/
%{_bindir}/om_*

%files devel
%{_includedir}/OpenMesh/
%{_libdir}/libOpenMesh*.so

%files doc
%doc LICENSE
%doc %{_vpath_builddir}/Build/share/OpenMesh/Doc/html/*

%changelog
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
