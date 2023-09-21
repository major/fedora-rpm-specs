# Qt6 builds for testing
%bcond_with qt6

Name:           avogadro2-libs
Version:        1.97.0
Release:        %autorelease
Summary:        Avogadro2 libraries

# BSD is main license
# BSD is the license of avogenerators scripts
License: BSD and MIT
URL:     http://avogadro.openmolecules.net/
Source0: https://github.com/OpenChemistry/avogadrolibs/archive/%{version}/avogadrolibs-%{version}.tar.gz
Source1: https://github.com/OpenChemistry/avogenerators/archive/%{version}/avogenerators-%{version}.tar.gz

# External sources for data files
Source2: https://github.com/OpenChemistry/molecules/archive/refs/heads/master.zip#/avogadro2-libs-molecules-master.zip
Source3: https://github.com/OpenChemistry/crystals/archive/1.0.1/crystals-1.0.1.tar.gz#/avogadro2-libs-crystals-1.0.1.tar.gz

# Set installation path of Python files
Patch0: %{name}-set_pythonpath.patch
Patch1: %{name}-1.94.0-do_not_download_external_files.patch
Patch2: %{name}-bug1185.patch

BuildRequires:  boost-devel
BuildRequires:  python%{python3_pkgversion}-devel
%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif
BuildRequires:  cmake3
BuildRequires:  chrpath
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(openbabel-3)
BuildRequires:  mesa-libGLU-devel
BuildRequires:  hdf5-devel
BuildRequires:  mmtf-cpp-devel, jsoncpp-devel
BuildRequires:  spglib-devel
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
%autosetup -a 1 -N -n avogadrolibs-%{version}

unzip -qq %{SOURCE2} && mv molecules-master molecules
tar -xf %{SOURCE3} && mv crystals-1.0.1 crystals
# Rename LICENSE file
mv molecules/LICENSE molecules/LICENSE-molecules

%patch -P 0 -p0 -b .backup
%patch -P 1 -p0 -b .backup
%patch -P 2 -p1 -b .backup

# Make avogadro generators source code available for CMake
mv avogenerators-%{version} avogadrogenerators
mv avogadrogenerators/README.md avogadrogenerators/README-avogenerators.md
sed -e 's|../avogadrogenerators|avogadrogenerators|g' -i avogadro/qtplugins/quantuminput/CMakeLists.txt
#

mv thirdparty/libgwavi/README.md thirdparty/libgwavi/README-libgwavi.md

%build
mkdir -p build
export CXXFLAGS="%{optflags} -DH5_USE_110_API"
# RHBZ #1996330
%ifarch %{power64}
export CXXFLAGS="%{optflags} -DEIGEN_ALTIVEC_DISABLE_MMA"
%endif
%cmake3 -B build -DCMAKE_BUILD_TYPE:STRING=Release \
 -DINSTALL_INCLUDE_DIR:PATH=include/avogadro2 -DINSTALL_LIBRARY_DIR:PATH=%{_lib} \
 -Wno-dev \
 -DENABLE_GLSL:BOOL=ON \
 -DENABLE_PYTHON:BOOL=ON  \
 -DPYTHON_EXECUTABLE:FILEPATH=%{__python3} \
 -DPYTHON_VERSION:STRING=%{python3_version} \
%if 0%{?fedora}
 -DUSE_BOOST_PYTHON:BOOL=ON \
 -DUSE_LIBARCHIVE:BOOL=ON \
%else
 -DUSE_BOOST_PYTHON:BOOL=OFF \
 -DUSE_LIBARCHIVE:BOOL=OFF \
%endif
 -DENABLE_RPATH:BOOL=OFF \
 -DENABLE_TESTING:BOOL=OFF \
 -DUSE_MMTF:BOOL=ON \
 -DUSE_QT:BOOL=ON \
 -DUSE_MOLEQUEUE:BOOL=ON \
 -DUSE_VTK:BOOL=OFF \
 -DUSE_HDF5:BOOL=ON \
 -DUSE_SPGLIB:BOOL=ON \
 -DSPGLIB_LIBRARY:FILEPATH=%{_libdir}/libsymspg.so -DSPGLIB_INCLUDE_DIR:PATH=%{_includedir}/spglib \
 -DBUILD_GPL_PLUGINS:BOOL=ON \
 -DBUILD_STATIC_PLUGINS:BOOL=ON \
 -DBUILD_DOCUMENTATION:BOOL=ON \
 -DUSE_LIBMSYM:BOOL=OFF

%make_build -C build

pushd build/docs
doxygen
popd

%install
%make_install -C build

# Move scale.py* files into %%{python3_sitearch}/avogadro2
cp -a %{buildroot}%{_libdir}/avogadro2/scripts %{buildroot}%{python3_sitearch}/avogadro2/
%{__python3} %{_rpmconfigdir}/redhat/pathfix.py -pn -i "%{__python3}" %{buildroot}%{python3_sitearch}/avogadro2/scripts/*/*.py
ln -sf %{python3_sitearch}/avogadro2/scripts %{buildroot}%{_libdir}/avogadro2/scripts

chrpath -d %{buildroot}%{_libdir}/lib*.so
rm -rf %{buildroot}%{_datadir}/doc

%files
%doc README.md thirdparty/libgwavi/README-libgwavi.md avogadrogenerators/README-avogenerators.md
%license LICENSE molecules/LICENSE-molecules
%{_libdir}/libAvogadro*.so.1
%{_libdir}/libAvogadro*.so.%{version}
%dir %{_libdir}/avogadro2
%{_libdir}/avogadro2/scripts/
%{_libdir}/avogadro2/libgwavi.a
%{_libdir}/avogadro2/staticplugins/
%{python3_sitearch}/avogadro2/
%{_datadir}/avogadro2/

%files devel
%{_includedir}/avogadro2/
%{_libdir}/libAvogadro*.so
%{_libdir}/cmake/avogadrolibs/

%files doc
%doc README.md build/docs/html
%license LICENSE

%changelog
%autochangelog
