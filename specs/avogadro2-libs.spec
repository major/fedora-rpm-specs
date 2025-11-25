# Qt6 builds for testing
%bcond qt6 0

Name:           avogadro2-libs
Version:        1.102.1
Release:        %autorelease
Summary:        Avogadro2 libraries

# BSD is main license
License: BSD-3-Clause AND (Apache-2.0 AND MIT) AND CDDL-1.0
URL:     http://avogadro.openmolecules.net/
Source0: https://github.com/OpenChemistry/avogadrolibs/archive/%{version}/avogadrolibs-%{version}.tar.gz
Source1: https://github.com/OpenChemistry/avogenerators/archive/%{version}/avogenerators-%{version}.tar.gz

# External sources for data files
Source2: https://github.com/OpenChemistry/molecules/archive/refs/tags/%{version}/molecules-%{version}.tar.gz
Source3: https://github.com/OpenChemistry/crystals/archive/refs/tags/%{version}/crystals-%{version}.tar.gz
Source4: https://github.com/OpenChemistry/fragments/archive/refs/tags/%{version}/fragments-%{version}.tar.gz

BuildRequires:  boost-devel
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  cmake
BuildRequires:  chrpath
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(openbabel-3)
BuildRequires:  mesa-libGLU-devel
BuildRequires:  hdf5-devel
BuildRequires:  mmtf-cpp-devel, jsoncpp-devel
BuildRequires:  spglib-devel
BuildRequires:  JKQtPlotter-qt5-devel
%if %{with qt6}
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  qt6-qtsvg-devel
%else
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qtsvg-devel
%endif
%if 0%{?fedora}
BuildRequires:  libarchive-devel >= 3.4.0
%endif
Provides: %{name}-static = 0:%{version}-%{release}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{name}}

%description
Avogadro libraries provide 3D rendering, visualization, analysis
and data processing useful in computational chemistry, molecular modeling,
bioinformatics, materials science, and related areas.

%package  devel
Summary:  Development files of %{name}
%if %{with qt6}
Requires: qt6-qtbase-devel%{?_isa}
%else
Requires: qt5-qtbase-devel%{?_isa}
%endif
Requires: glew-devel%{?_isa}
Requires: libGL-devel%{?_isa}
Requires: mesa-libGLU-devel%{?_isa}
Requires: spglib-devel%{?_isa}
Requires: %{name}%{?_isa} = %{version}-%{release}

Provides: libgwavi-static

%description devel
This package contains libraries and header files for developing
applications that use %{name}.

%package doc
Summary: HTML documentation of %{name}
BuildArch: noarch
BuildRequires: doxygen, graphviz
BuildRequires: make
%description doc
HTML documentation of %{name}.

%prep
%autosetup -n avogadrolibs-%{version}

tar -xf %{SOURCE1} && mv avogenerators-%{version} avogadrogenerators
tar -xf %{SOURCE2} && mv molecules-%{version} molecules
tar -xf %{SOURCE3} && mv crystals-%{version} crystals
tar -xf %{SOURCE4} && mv fragments-%{version} fragments

# Rename LICENSE file
mv molecules/LICENSE molecules/LICENSE-molecules
mv fragments/LICENSE fragments/LICENSE-fragments
mv avogadrogenerators/README.md avogadrogenerators/README-avogenerators.md
sed -e 's|${AvogadroLibs_SOURCEDATA_DIR}/|${AvogadroLibs_SOURCE_DIR}/|g' -i avogadro/qtplugins/insertfragment/CMakeLists.txt
sed -e 's|${AvogadroLibs_SOURCEDATA_DIR}/|${AvogadroLibs_SOURCE_DIR}/|g' -i avogadro/qtplugins/quantuminput/CMakeLists.txt
sed -e 's|${AvogadroLibs_SOURCEDATA_DIR}/|${AvogadroLibs_SOURCE_DIR}/|g' -i avogadro/qtplugins/templatetool/CMakeLists.txt
#

mv thirdparty/libgwavi/README.md thirdparty/libgwavi/README-libgwavi.md
mv fragments/README.md fragments/README-fragments.md

%conf
export CXXFLAGS="%{optflags} -DH5_USE_110_API"
# RHBZ #1996330
%ifarch %{power64}
export CXXFLAGS="%{optflags} -DEIGEN_ALTIVEC_DISABLE_MMA"
%endif
%cmake -DCMAKE_BUILD_TYPE:STRING=Release \
 -DINSTALL_INCLUDE_DIR:PATH=include/avogadro2 -DINSTALL_LIBRARY_DIR:PATH=%{_lib} \
 -Wno-dev \
 -DENABLE_GLSL:BOOL=ON \
 -DUSE_PYTHON:BOOL=OFF  \
%if 0%{?fedora}
 -DUSE_LIBARCHIVE:BOOL=ON \
%else
 -DUSE_LIBARCHIVE:BOOL=OFF \
%endif
 -DENABLE_RPATH:BOOL=OFF \
 -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
 -DENABLE_TESTING:BOOL=OFF \
 -DUSE_MMTF:BOOL=ON \
 -DUSE_QT:BOOL=ON \
 -DQT_VERSION:STRING=%{?with_qt6:6}%{!?with_qt6:5} \
 -DUSE_MOLEQUEUE:BOOL=ON \
 -DUSE_VTK:BOOL=OFF \
 -DUSE_HDF5:BOOL=ON \
 -DUSE_SPGLIB:BOOL=ON \
 -DBUILD_GPL_PLUGINS:BOOL=ON \
 -DBUILD_STATIC_PLUGINS:BOOL=ON \
 -DBUILD_DOCUMENTATION:BOOL=ON \
 -DUSE_LIBMSYM:BOOL=OFF \
 -DOpenBabel3_INCLUDE_DIR:PATH=%{_includedir}/openbabel3

%build
%cmake_build
%cmake_build -t documentation

%install
%cmake_install

%py3_shebang_fix %{buildroot}%{_libdir}/avogadro2/scripts
rm -rf %{buildroot}%{_datadir}/doc
mkdir -p %{buildroot}%_pkgdocdir
cp -a %_vpath_builddir/docs/html %{buildroot}%_pkgdocdir/html


%files
%doc README.md thirdparty/libgwavi/README-libgwavi.md avogadrogenerators/README-avogenerators.md
%doc fragments/README-fragments.md
%license LICENSE molecules/LICENSE-molecules fragments/LICENSE-fragments
%{_libdir}/libAvogadro*.so.1
%{_libdir}/libAvogadro*.so.%{version}
%dir %{_libdir}/avogadro2
%{_libdir}/avogadro2/scripts/
%{_libdir}/avogadro2/libgwavi.a
%{_libdir}/avogadro2/staticplugins/
%{_datadir}/avogadro2/

%files devel
%{_includedir}/avogadro2/
%{_libdir}/libAvogadro*.so
%{_libdir}/cmake/avogadrolibs/

%files doc
%doc README.md
%_pkgdocdir/html
%license LICENSE

%changelog
%autochangelog
