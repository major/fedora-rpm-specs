%global commit b2655743d30ed3185f3c0e2626b33a1d29655216
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20210828

Name:           qwtplot3d
Epoch:          1
Version:        0.3.0
Release:        10.%{commitdate}git%{shortcommit}%{?dist}
Summary:        Extended version of the original QwtPlot3D library
License:        Zlib
URL:            https://github.com/SciDAVis/%{name}
Source0:        %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

Patch0:         %{name}-qt6-build.patch
Patch1:         %{name}-qt5-build.patch

# Qt6
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  qt6-rpm-macros
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qt5compat-devel
# Qt5
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5OpenGL)
BuildRequires:  qt5-rpm-macros
BuildRequires:  qt5-qtbase-devel
#
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  gl2ps-devel
BuildRequires:  gcc-c++
BuildRequires:  chrpath

%description
QwtPlot3D is not a program, but a feature-rich Qt/OpenGL-based C++
programming library, providing essentially a bunch of 3D-widgets for
programmers.

# Qt6
%package        -n %{name}-qt6
Summary:        Extended version of the original QwtPlot3D Qt6 library

%description    -n %{name}-qt6
QwtPlot3D is not a program, but a feature-rich Qt/OpenGL-based C++
programming library, providing essentially a bunch of 3D-widgets for
programmers.

%package        -n %{name}-qt6-devel
Summary:        Development files for %{name}
Requires:       %{name}-qt6%{?_isa} = %{epoch}:%{version}-%{release}

%description    -n %{name}-qt6-devel
The %{name}6-devel package contains Qt6 libraries and header files for
developing applications that use %{name}-qt6.
#

# Qt5
%package        -n %{name}-qt5
Summary:        Extended version of the original QwtPlot3D Qt5 library
Provides:       %{name}-qt5%{?_isa} = %{epoch}:%{version}-%{release}
Obsoletes:      %{name}-qt5 < 0:0.3.1a-18
Obsoletes:      %{name}-qt4 < 0:0.3.1a-18

%description    -n %{name}-qt5
QwtPlot3D is not a program, but a feature-rich Qt/OpenGL-based C++
programming library, providing essentially a bunch of 3D-widgets for
programmers.

%package        -n %{name}-qt5-devel
Summary:        Development files for %{name}
Requires:       %{name}-qt5%{?_isa} = %{epoch}:%{version}-%{release}
Provides:       %{name}-qt5-devel%{?_isa} = %{epoch}:%{version}-%{release}
Obsoletes:      %{name}-qt5-devel < 0:0.3.1a-18
Obsoletes:      %{name}-qt4-devel < 0:0.3.1a-18

%description    -n %{name}-qt5-devel
The %{name}6-devel package contains Qt5 libraries and header files for
developing applications that use %{name}-qt5.
#

%prep
%setup -qc -n %{name}-%{commit}

# Unbundle gl2ps
rm -rf %{name}-%{commit}/3rdparty/gl2ps

cp -a %{name}-%{commit} %{name}-qt5
mv %{name}-%{commit} %{name}-qt6

pushd %{name}-qt6
%patch -P 0 -p1 -b .backup
popd

pushd %{name}-qt5
%patch -P 1 -p1 -b .backup
popd

%build
pushd %{name}-qt6
export CXXFLAGS="%{build_cxxflags}"
%cmake -Wno-dev \
 -DPKG_CONFIG_ARGN:STRING="%(pkg-config --cflags Qt6Gui) %(pkg-config --cflags Qt6Core) %(pkg-config --cflags Qt6OpenGL)" \
 -DCMAKE_BUILD_TYPE:STRING=Release \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE -DCMAKE_COLOR_MAKEFILE:BOOL=ON \
 -DCMAKE_SHARED_LINKER_FLAGS_RELEASE:STRING="%{__global_ldflags} -lGLU" \
 -DCMAKE_INSTALL_LIBDIR:PATH=%{_qt6_libdir} -DCMAKE_INSTALL_INCLUDEDIR:PATH=%{_qt6_headerdir}/%{name}-qt6
%cmake_build
popd

pushd %{name}-qt5
export CXXFLAGS="%{build_cxxflags}"
%cmake -Wno-dev \
 -DPKG_CONFIG_ARGN:STRING="%(pkg-config --cflags Qt5Gui) %(pkg-config --cflags Qt5Core) %(pkg-config --cflags Qt5OpenGL)" \
 -DCMAKE_BUILD_TYPE:STRING=Release \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE -DCMAKE_COLOR_MAKEFILE:BOOL=ON \
 -DCMAKE_SHARED_LINKER_FLAGS_RELEASE:STRING="%{__global_ldflags} -lGLU" \
 -DCMAKE_INSTALL_LIBDIR:PATH=%{_qt5_libdir} -DCMAKE_INSTALL_INCLUDEDIR:PATH=%{_qt5_headerdir}/%{name}-qt5
%cmake_build
popd

%install
pushd %{name}-qt6
%cmake_install
# Install executable examples files
mkdir -p %{buildroot}%{_libexecdir}/%{name}-qt6
install -pm 755 %{__cmake_builddir}/examples/simpleplot/simpleplot %{buildroot}%{_libexecdir}/%{name}-qt6/
install -pm 755 %{__cmake_builddir}/examples/axes/axes %{buildroot}%{_libexecdir}/%{name}-qt6/
install -pm 755 %{__cmake_builddir}/examples/enrichments/enrichments %{buildroot}%{_libexecdir}/%{name}-qt6/
install -pm 755 %{__cmake_builddir}/examples/autoswitch/autoswitch %{buildroot}%{_libexecdir}/%{name}-qt6/
install -pm 755 %{__cmake_builddir}/examples/mesh2/mesh2 %{buildroot}%{_libexecdir}/%{name}-qt6/

mkdir -p %{buildroot}%{_qt6_headerdir}/%{name}-qt6
install -pm 644 include/*  %{buildroot}%{_qt6_headerdir}/%{name}-qt6/
mv %{buildroot}%{_qt6_headerdir}/%{name}-qt6/qwt3d_version.h.in %{buildroot}%{_qt6_headerdir}/%{name}-qt6/qwt3d_version.h
sed -e 's|@PROJECT_VERSION_MAJOR@|0|g' -i %{buildroot}%{_qt6_headerdir}/%{name}-qt6/qwt3d_version.h
sed -e 's|@PROJECT_VERSION_MINOR@|3|g' -i %{buildroot}%{_qt6_headerdir}/%{name}-qt6/qwt3d_version.h
sed -e 's|@PROJECT_VERSION_PATCH@|0|g' -i %{buildroot}%{_qt6_headerdir}/%{name}-qt6/qwt3d_version.h

# Remove rpaths
chrpath -d %{buildroot}%{_libexecdir}/%{name}-qt6/*
popd

pushd %{name}-qt5
%cmake_install
# Install executable examples files
mkdir -p %{buildroot}%{_libexecdir}/%{name}-qt5
install -pm 755 %{__cmake_builddir}/examples/simpleplot/simpleplot %{buildroot}%{_libexecdir}/%{name}-qt5/
install -pm 755 %{__cmake_builddir}/examples/axes/axes %{buildroot}%{_libexecdir}/%{name}-qt5/
install -pm 755 %{__cmake_builddir}/examples/enrichments/enrichments %{buildroot}%{_libexecdir}/%{name}-qt5/
install -pm 755 %{__cmake_builddir}/examples/autoswitch/autoswitch %{buildroot}%{_libexecdir}/%{name}-qt5/
install -pm 755 %{__cmake_builddir}/examples/mesh2/mesh2 %{buildroot}%{_libexecdir}/%{name}-qt5/

mkdir -p %{buildroot}%{_qt5_headerdir}/%{name}-qt5
install -pm 644 include/*  %{buildroot}%{_qt5_headerdir}/%{name}-qt5/
mv %{buildroot}%{_qt5_headerdir}/%{name}-qt5/qwt3d_version.h.in %{buildroot}%{_qt5_headerdir}/%{name}-qt5/qwt3d_version.h
sed -e 's|@PROJECT_VERSION_MAJOR@|0|g' -i %{buildroot}%{_qt5_headerdir}/%{name}-qt5/qwt3d_version.h
sed -e 's|@PROJECT_VERSION_MINOR@|3|g' -i %{buildroot}%{_qt5_headerdir}/%{name}-qt5/qwt3d_version.h
sed -e 's|@PROJECT_VERSION_PATCH@|0|g' -i %{buildroot}%{_qt5_headerdir}/%{name}-qt5/qwt3d_version.h

# Remove rpaths
chrpath -d %{buildroot}%{_libexecdir}/%{name}-qt5/*
popd

# Qt6
%files -n %{name}-qt6
%license %{name}-qt6/COPYING %{name}-qt6/LICENSE
%doc %{name}-qt6/README.md
%{_qt6_libdir}/lib%{name}-qt6.so.0.3.0
%{_qt6_libdir}/lib%{name}-qt6.so.0.3

%files -n %{name}-qt6-devel
%{_qt6_headerdir}/%{name}-qt6/
%{_qt6_libdir}/lib%{name}-qt6.so
%{_libexecdir}/%{name}-qt6/
#

# Qt5
%files -n %{name}-qt5
%license %{name}-qt5/COPYING %{name}-qt5/LICENSE
%doc %{name}-qt5/README.md
%{_qt5_libdir}/lib%{name}-qt5.so.0.3.0
%{_qt5_libdir}/lib%{name}-qt5.so.0.3

%files -n %{name}-qt5-devel
%{_qt5_headerdir}/%{name}-qt5/
%{_qt5_libdir}/lib%{name}-qt5.so
%{_libexecdir}/%{name}-qt5/
#

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.0-10.20210828gitb265574
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.0-9.20210828gitb265574
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat May 25 2024 Antonio Trande <sagitter@fedoraproject.org> - 1:0.3.0-8.20210828gitb265574
- Fix patch commands

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.0-7.20210828gitb265574
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.0-6.20210828gitb265574
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.0-5.20210828gitb265574
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jan 24 2023 Antonio Trande <sagitter@fedoraproject.org> - 1:0.3.0-4.20210828gitb265574
- Fix qwt3d_version.h (rhbz#2163530)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.0-3.20210828gitb265574
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Jan 08 2023 Antonio Trande <sagitter@fedoraproject.org> - 1:0.3.0-2.20210828gitb265574
- Fix Obsolete tags

* Sun Jan 01 2023 Antonio Trande <sagitter@fedoraproject.org> - 1:0.3.0-1.20210828gitb265574
- New upstream
- Remove old/unused CMake options
- Obsolete old qwtplot3d-qt4/qwtplot3d-qt5

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-34
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Feb 17 2018 Antonio Trande <sagitter@fedoraproject.org> - 0.2.7-28
- Use %%ldconfig_scriptlets

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Aug 20 2016 Antonio Trande <sagitter@fedoraproject.org> - 0.2.7-22
- Unbundle gl2ps (bz#1077865)
- Fix compiler/linker flags

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 25 2015 Christian Dersch <lupinix@fedoraproject.org> - 0.2.7-20
- Spec adjustments (use license tag, global instead of define)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.2.7-18
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 27 2012 Rex Dieter <rdieter@fedoraproject.org> 
- 0.2.7-12
- Building against qwtplot3d-qt4 fails (#805684)
- tighten subpkg deps

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Mar 05 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.2.7-8
- fixed failed build on gcc 4.4

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Apr 02 2008 Rex Dieter <rdieter@fedoraproject.org> - 0.2.7-6
- s/qt-devel/qt3-devel/

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.2.7-5
- Autorebuild for GCC 4.3

* Thu Aug 23 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.2.7-4
- fixed -qt4 symbolic links
- update license to zlib

* Thu Aug 23 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.2.7-3
- queued for mass rebuild for Fedora 8 - BuildID

* Wed Aug 08 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.2.7-2
- built and shipped qwtplot3d-qt4 and devel

* Mon Jul 30 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.2.7-1
- New upstream release
- Added optflags to the make process
- fix ownership

* Tue Jan 02 2007 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.2.6-2
- Added qt-devel to -devel subpackage requires

* Sun Dec 31 2006 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.2.6-1
- Initial RPM release
