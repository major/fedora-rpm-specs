%undefine __cmake_in_source_build

# State Nov 11 2020, LTO causes
# TestXMLHyperTreeGridIO.cxx.o (symbol from plugin): undefined reference to symbol
# '_ZZNSt8__detail18__to_chars_10_implIjEEvPcjT_E8__digits@@LLVM_11'
%global _lto_cflags %{nil}

# There is a circular dep with opencascade
%bcond bootstrap 0

# OSMesa and X support are mutually exclusive.
# TODO - buid separate OSMesa version if desired
%bcond_with OSMesa
# No more Java on i686
%ifarch %{java_arches}
%bcond_without java
%else
%bcond_with java
%endif
%if 0%{?flatpak}
%bcond_with mpich
%bcond_with openmpi
%else
# No openmpi on i668 with openmpi 5 in Fedora 40+
# No mpi4py on i686
%if 0%{?fedora} >= 40
%ifarch %{ix86}
%bcond_with mpich
%bcond_with openmpi
%else
%bcond_without mpich
%bcond_without openmpi
%endif
%else
%bcond_without mpich
%bcond_without openmpi
%endif
%endif
# s390x on EL8 does not have xorg-x11-drv-dummy
%if 0%{?rhel}
%ifarch s390x
%bcond_with    xdummy
%else
%bcond_without xdummy
%endif
%else
%bcond_without xdummy
%endif

%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9
%bcond_without flexiblas
%endif

# Try disabling LTO on ppc64le
%ifarch ppc64le
%global _lto_cflags %{nil}
%endif

# VTK currently is carrying local modifications to gl2ps
%bcond_with gl2ps

%bcond_without fmt

#global rc rc2

Summary: The Visualization Toolkit - A high level 3D visualization library
Name: vtk
Version: 9.5.0%{?rc:~%{rc}}
Release: %autorelease
License: BSD-3-Clause
%global srcver %{lua:local ver = rpm.expand('%version');ver = ver:gsub('~','.');print(ver)}
Source0: https://www.vtk.org/files/release/9.5/VTK-%{srcver}.tar.gz
Source1: https://www.vtk.org/files/release/9.5/VTKData-%{srcver}.tar.gz
Source2: xorg.conf
# Patch required libharu version (Fedora 33+ contains the needed VTK patches)
Patch: vtk-libharu.patch
# Tk 9.0 - based on b7c22497712be6751fbefe155533ae34d5e381f5
Patch: vtk-tk9.patch
# always_inline fails on ppc64le
# https://gitlab.kitware.com/vtk/vtk/-/issues/19622
# https://bugzilla.redhat.com/show_bug.cgi?id=2386242
Patch: vtk-ppc64-no-always-inline.patch

URL: https://vtk.org/

BuildRequires:  cmake
# Allow for testing with different cmake generators.
# make still seems to be faster than ninja, but has failed at times.
%global cmake_gen %{nil}
BuildRequires:  gcc-c++
%if %{with java}
BuildRequires: java-devel
%else
Obsoletes:     %{name}-java < %{version}-%{release}
Obsoletes:     %{name}-java-devel < %{version}-%{release}
%endif
BuildRequires:  alembic-devel
%if %{with flexiblas}
BuildRequires:  flexiblas-devel
%else
BuildRequires:  blas-devel
BuildRequires:  lapack-devel
%endif
BuildRequires:  boost-devel
BuildRequires:  cgnslib-devel
BuildRequires:  cli11-devel
BuildRequires:  double-conversion-devel
BuildRequires:  eigen3-devel
BuildRequires:  expat-devel
BuildRequires:  fast_float-devel
BuildRequires:  ffmpeg-free-devel
%if %{with fmt}
BuildRequires:  fmt-devel >= 8.1.0
%endif
BuildRequires:  freeglut-devel
BuildRequires:  freetype-devel
BuildRequires:  gdal-devel
%if %{with gl2ps}
BuildRequires:  gl2ps-devel
%endif
BuildRequires:  hdf5-devel
BuildRequires:  json-devel
BuildRequires:  jsoncpp-devel
BuildRequires:  libarchive-devel
BuildRequires:  libGL-devel
BuildRequires:  libharu-devel >= 2.4.0
BuildRequires:  libICE-devel
BuildRequires:  libjpeg-devel
BuildRequires:  liblas-devel
BuildRequires:  libpng-devel
BuildRequires:  libpq-devel
BuildRequires:  libtheora-devel
BuildRequires:  libtiff-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  libxml2-devel
BuildRequires:  libX11-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libXext-devel
BuildRequires:  libXt-devel
BuildRequires:  lz4-devel
BuildRequires:  mariadb-connector-c-devel
%{?with_OSMesa:BuildRequires: mesa-libOSMesa-devel}
BuildRequires:  netcdf-cxx-devel
%if %{without bootstrap}
BuildRequires:  opencascade-devel
%endif
BuildRequires:  openslide-devel
# Currently does not provide OpenVDBConfig.cmake
#BuildRequires:  openvdb-devel
BuildRequires:  openvr-devel
BuildRequires:  openxr-devel
BuildRequires:  PDAL-devel
BuildRequires:  PEGTL-devel
BuildRequires:  proj-devel
BuildRequires:  pugixml-devel
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  cmake(Qt6UiPlugin)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  R-devel
BuildRequires:  sqlite-devel
BuildRequires:  tcl-devel
BuildRequires:  tk-devel
BuildRequires:  unixODBC-devel
BuildRequires:  utf8cpp-devel
BuildRequires:  zfp-devel
BuildRequires:  zlib-devel
BuildRequires:  chrpath
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  gnuplot
BuildRequires:  wget
%if %{with mpich}
BuildRequires:  mpich-devel
%ifnarch %{ix86}
BuildRequires:  python%{?python3_pkgversion}-mpi4py-mpich
%endif
BuildRequires:  netcdf-mpich-devel
%endif
%if %{with openmpi}
BuildRequires:  openmpi-devel
BuildRequires:  python%{?python3_pkgversion}-mpi4py-openmpi
BuildRequires:  netcdf-openmpi-devel
%endif
# For %check
%if %{with xdummy}
BuildRequires:  xorg-x11-drv-dummy
BuildRequires:  mesa-dri-drivers
%endif
Requires: hdf5 = %{_hdf5_version}

# Almost every BR needs to be required by the -devel packages
%global vtk_devel_requires \
Requires: cmake \
%if %{with flexiblas} \
Requires: flexiblas-devel%{?_isa} \
%else \
Requires: blas-devel%{?_isa} \
Requires: lapack-devel%{?_isa} \
%endif \
Requires: blas-devel%{?_isa} \
Requires: boost-devel%{?_isa} \
Requires: cgnslib-devel%{?_isa} \
# cli11 is noarch and header-only \
Requires: cli11-static \
Requires: double-conversion-devel%{?_isa} \
# eigen3 is noarch and header-only \
Requires: eigen3-static \
Requires: expat-devel%{?_isa} \
# fast_float is noarch and header-only \
Requires: fast_float-devel \
Requires: ffmpeg-free-devel%{?_isa} \
%if %{with fmt} \
Requires: fmt-devel%{?_isa} \
%endif \
Requires: freeglut-devel%{?_isa} \
Requires: freetype-devel%{?_isa} \
Requires: gdal-devel%{?_isa} \
%if %{with gl2ps} \
Requires: gl2ps-devel%{?_isa} \
%endif \
Requires: json-devel%{?_isa} \
Requires: jsoncpp-devel%{?_isa} \
Requires: lapack-devel%{?_isa} \
Requires: libarchive-devel%{?_isa} \
Requires: libGL-devel%{?_isa} \
Requires: libharu-devel%{?_isa} >= 2.3.0-9 \
Requires: libjpeg-devel%{?_isa} \
Requires: liblas-devel%{?_isa} \
Requires: libogg-devel%{?_isa} \
Requires: libpng-devel%{?_isa} \
Requires: libpq-devel%{?_isa} \
Requires: libtheora-devel%{?_isa} \
Requires: libtiff-devel%{?_isa} \
Requires: libxkbcommon-devel%{?_isa} \
Requires: libxml2-devel%{?_isa} \
Requires: libX11-devel%{?_isa} \
Requires: libXcursor-devel%{?_isa} \
Requires: libXext-devel%{?_isa} \
Requires: libXt-devel%{?_isa} \
Requires: lz4-devel%{?_isa} \
Requires: mariadb-connector-c-devel%{?_isa} \
%if %{with OSMesa} \
Requires: mesa-libOSMesa-devel%{?_isa} \
%endif \
Requires: netcdf-cxx-devel%{?_isa} \
%if %{without bootstrap} \
Requires: opencascade-devel%{?_isa} \
%endif \
Requires: openslide-devel%{?_isa} \
#Requires: openvdb-devel%{?_isa} \
Requires: openvr-devel%{?_isa} \
Requires: openxr-devel%{?_isa} \
Requires: PDAL-devel%{?_isa} \
Requires: PEGTL-devel%{?_isa} \
Requires: proj-devel%{?_isa} \
Requires: pugixml-devel%{?_isa} \
# bz #1183210 + #1183530 \
Requires: python%{python3_pkgversion}-devel \
Requires: sqlite-devel%{?_isa} \
Requires: cmake(Qt6) \
Requires: cmake(Qt6Core5Compat) \
Requires: cmake(Qt6Quick) \
Requires: cmake(Qt6UiPlugin) \
Requires: unixODBC-devel%{?_isa} \
Requires: utf8cpp-devel \
Requires: zfp-devel%{?_isa} \
Requires: zlib-devel%{?_isa} \

# Bundled KWSys
# https://fedorahosted.org/fpc/ticket/555
# Components used are specified in Utilities/KWSys/CMakeLists.txt
Provides: bundled(kwsys-base64)
Provides: bundled(kwsys-commandlinearguments)
Provides: bundled(kwsys-directory)
Provides: bundled(kwsys-dynamicloader)
Provides: bundled(kwsys-encoding)
Provides: bundled(kwsys-fstream)
Provides: bundled(kwsys-fundamentaltype)
Provides: bundled(kwsys-glob)
Provides: bundled(kwsys-md5)
Provides: bundled(kwsys-process)
Provides: bundled(kwsys-regularexpression)
Provides: bundled(kwsys-status)
Provides: bundled(kwsys-system)
Provides: bundled(kwsys-systeminformation)
Provides: bundled(kwsys-systemtools)
# Other bundled libraries
Provides: bundled(diy2)
Provides: bundled(exodusII) = 2.0.0
Provides: bundled(exprtk) = 2.71
Provides: bundled(fides)
%if !%{with fmt}
Provides: bundled(fmt) = 8.1.0
%endif
Provides: bundled(ftgl) = 1.32
%if !%{with gl2ps}
Provides: bundled(gl2ps) = 1.4.0
%endif
Provides: bundled(h5part) = 1.6.6
Provides: bundled(ioss) = 20221014
Provides: bundled(itlib-small-vector) = 1.0.4
Provides: bundled(kissfft)
Provides: bundled(loguru) = 2.1
Provides: bundled(metaio)
Provides: bundled(scn) = 4.0.0
# kitware library https://gitlab.kitware.com/utils/token
Provides: bundled(token) = 23.09
Provides: bundled(verdict) = 1.4.0
Provides: bundled(viskores) = 1.0.0
Provides: bundled(vpic)
Provides: bundled(xdmf2) = 2.1
Provides: bundled(xdmf3)

Obsoletes: %{name}-tcl < 8.2.0-1
Obsoletes: %{name}-qt-tcl < 8.2.0-1

%description
VTK is an open-source software system for image processing, 3D
graphics, volume rendering and visualization. VTK includes many
advanced algorithms (e.g., surface reconstruction, implicit modeling,
decimation) and rendering techniques (e.g., hardware-accelerated
volume rendering, LOD control).

NOTE: The version in this package has NOT been compiled with MPI support.
%if %{with mpich}
Install the %{name}-mpich package to get a version compiled with mpich.
%endif
%if %{with openmpi}
Install the %{name}-openmpi package to get a version compiled with openmpi.
%endif

%package devel
Summary: VTK header files for building C++ code
Requires: %{name}%{?_isa} = %{version}-%{release}
%if %{with java}
Requires: %{name}-java%{?_isa} = %{version}-%{release}
%endif
Requires: python%{python3_pkgversion}-%{name}%{?_isa} = %{version}-%{release}
Requires: hdf5-devel%{?_isa}
Requires: netcdf-cxx-devel%{?_isa}
%{vtk_devel_requires}

%description devel
This provides the VTK header files required to compile C++ programs that
use VTK to do 3D visualization.

%package -n python%{python3_pkgversion}-%{name}
Summary: Python 3 bindings for VTK
Requires: vtk%{?_isa} = %{version}-%{release}
%{?python_provide:%python_provide python%{python3_pkgversion}-vtk}
Provides: %{py3_dist vtk} = %{version}
Provides: python%{python3_version}dist(vtk) = %{version}
Obsoletes: python3-vtk-qt < 8.2.0-27
Provides:  python%{python3_pkgversion}-vtk-qt = %{version}-%{release}

%description -n python%{python3_pkgversion}-%{name}
Python 3 bindings for VTK.

%if %{with java}
%package java
Summary: Java bindings for VTK
Requires: %{name}%{?_isa} = %{version}-%{release}

%description java
Java bindings for VTK.

%package java-devel
Summary: Java development for VTK
Requires: %{name}-java%{?_isa} = %{version}-%{release}
Requires: java-devel

%description java-devel
Java development for VTK.
%endif

%package qt
Summary: Qt bindings for VTK
Requires: %{name}%{?_isa} = %{version}-%{release}

%description qt
Qt bindings for VTK.

%global mpi_list %{nil}

%if %{with mpich}
%global mpi_list %mpi_list mpich
%package mpich
Summary: The Visualization Toolkit - mpich version

Obsoletes: %{name}-mpich-tcl < 8.2.0-1
Obsoletes: %{name}-mpich-qt-tcl < 8.2.0-1
%if %{without java}
Obsoletes:     %{name}-mpich-java < %{version}-%{release}
Obsoletes:     %{name}-mpich-java-devel < %{version}-%{release}
%endif

%description mpich
VTK is an open-source software system for image processing, 3D
graphics, volume rendering and visualization. VTK includes many
advanced algorithms (e.g., surface reconstruction, implicit modeling,
decimation) and rendering techniques (e.g., hardware-accelerated
volume rendering, LOD control).

NOTE: The version in this package has been compiled with mpich support.

%package mpich-devel
Summary: VTK header files for building C++ code with mpich
Requires: %{name}-mpich%{?_isa} = %{version}-%{release}
%if %{with java}
Requires: %{name}-mpich-java%{?_isa} = %{version}-%{release}
%endif
Requires: python%{python3_pkgversion}-%{name}-mpich%{?_isa} = %{version}-%{release}
Requires: mpich-devel
Requires: hdf5-mpich-devel%{?_isa}
Requires: netcdf-mpich-devel%{?_isa}
%{vtk_devel_requires}

%description mpich-devel
This provides the VTK header files required to compile C++ programs that
use VTK to do 3D visualization.

NOTE: The version in this package has been compiled with mpich support.

%package -n python%{python3_pkgversion}-%{name}-mpich
Summary: Python 3 bindings for VTK with mpich
Requires: %{name}-mpich%{?_isa} = %{version}-%{release}
Obsoletes: python3-vtk-mpich-qt < 8.2.0-15
Provides:  python%{python3_pkgversion}-vtk-mpich-qt = %{version}-%{release}

%description -n python%{python3_pkgversion}-%{name}-mpich
python 3 bindings for VTK with mpich.

%if %{with java}
%package mpich-java
Summary: Java bindings for VTK with mpich
Requires: %{name}-mpich%{?_isa} = %{version}-%{release}

%description mpich-java
Java bindings for VTK with mpich.

%package mpich-java-devel
Summary: Java development for VTK with mpich
Requires: %{name}-mpich-java%{?_isa} = %{version}-%{release}
Requires: java-devel

%description mpich-java-devel
Java development for VTK with mpich.
%endif

%package mpich-qt
Summary: Qt bindings for VTK with mpich
Requires: %{name}-mpich%{?_isa} = %{version}-%{release}

%description mpich-qt
Qt bindings for VTK with mpich.
%endif

%if %{with openmpi}
%global mpi_list %mpi_list openmpi
%package openmpi
Summary: The Visualization Toolkit - openmpi version

Obsoletes: %{name}-openmpi-tcl < 8.2.0-1
Obsoletes: %{name}-openmpi-qt-tcl < 8.2.0-1
%if %{without java}
Obsoletes:     %{name}-mpich-java < %{version}-%{release}
Obsoletes:     %{name}-mpich-java-devel < %{version}-%{release}
%endif

%description openmpi
VTK is an open-source software system for image processing, 3D
graphics, volume rendering and visualization. VTK includes many
advanced algorithms (e.g., surface reconstruction, implicit modeling,
decimation) and rendering techniques (e.g., hardware-accelerated
volume rendering, LOD control).

NOTE: The version in this package has been compiled with openmpi support.

%package openmpi-devel
Summary: VTK header files for building C++ code with openmpi
Requires: %{name}-openmpi%{?_isa} = %{version}-%{release}
%if %{with java}
Requires: %{name}-openmpi-java%{?_isa} = %{version}-%{release}
%endif
Requires: python%{python3_pkgversion}-%{name}-openmpi%{?_isa} = %{version}-%{release}
Requires: openmpi-devel
Requires: hdf5-openmpi-devel%{?_isa}
Requires: netcdf-openmpi-devel%{?_isa}
%{vtk_devel_requires}

%description openmpi-devel
This provides the VTK header files required to compile C++ programs that
use VTK to do 3D visualization.

NOTE: The version in this package has been compiled with openmpi support.

%package -n python%{python3_pkgversion}-%{name}-openmpi
Summary: Python 3 bindings for VTK with openmpi
Requires: %{name}-openmpi%{?_isa} = %{version}-%{release}
Obsoletes: python3-vtk-openmpi-qt < 8.2.0-15
Provides:  python%{python3_pkgversion}-vtk-openmpi-qt = %{version}-%{release}

%description -n python%{python3_pkgversion}-%{name}-openmpi
Python 3 bindings for VTK with openmpi.

%if %{with java}
%package openmpi-java
Summary: Java bindings for VTK with openmpi
Requires: %{name}-openmpi%{?_isa} = %{version}-%{release}

%description openmpi-java
Java bindings for VTK with openmpi.

%package openmpi-java-devel
Summary: Java development for VTK with openmpi
Requires: %{name}-openmpi-java%{?_isa} = %{version}-%{release}
Requires: java-devel

%description openmpi-java-devel
Java development for VTK with openmpi.
%endif

%package openmpi-qt
Summary: Qt bindings for VTK with openmpi
Requires: %{name}-openmpi%{?_isa} = %{version}-%{release}

%description openmpi-qt
Qt bindings for VTK with openmpi.
%endif

%package data
Summary: VTK data files for tests/examples
BuildArch: noarch
Obsoletes: vtkdata < 6.1.0-3

%description data
VTK data files for tests and examples.

%package doc
Summary: API documentation for VTK
BuildArch: noarch

%description doc
Generated API documentation for VTK

%package testing
Summary: Testing programs for VTK
Requires: %{name}%{?_isa} = %{version}-%{release}, %{name}-data = %{version}

%description testing
Testing programs for VTK

%package examples
Summary: Examples for VTK
Requires: %{name}%{?_isa} = %{version}-%{release}, %{name}-data = %{version}

%description examples
This package contains many well-commented examples showing how to use
VTK. Examples are available in the C++, Tcl, Python and Java
programming languages.


%prep
%autosetup -p1 -b 1 -n VTK-%{srcver}
# Remove included thirdparty sources just to be sure
# ls VTK-*/ThirdParty/*/vtk* -dl | grep ^d
# TODO - diy2 - not yet packaged
# TODO - exodusII - not yet packaged
# TODO - exprtk - not yet packaged
# TODO - fides - not yet packaged
# TODO - h5part - not yet packaged
# TODO - ioss - not yet packaged
# TODO - kissfft - not yet packaged
# TODO - loguru - not yet packaged
# TODO - scn - not yet packaged
# TODO - verdict - not yet packaged
# TODO - viskores - not yet packaged
# TODO - VPIC - not yet packaged
# TODO - xdmf2 - not yet packaged
# TODO - xdmf3 - not yet packaged
for x in vtk{cgns,cli11,doubleconversion,eigen,expat,fast_float,%{?with_fmt:fmt,}freetype,%{?with_gl2ps:gl2ps,}hdf5,jpeg,jsoncpp,libharu,libproj,libxml2,lz4,lzma,mpi4py,netcdf,nlohmannjson,ogg,pegtl,png,pugixml,sqlite,theora,tiff,utf8,zlib}
do
  rm -r ThirdParty/*/${x}
done
%ifarch %{ix86}
rm -r ThirdParty/xdmf3
%endif

# Remove version requirements
sed -i -e '/VERSION *"/d' ThirdParty/fast_float/CMakeLists.txt

# Remove version requirements
sed -i -e '/VERSION *"/d' ThirdParty/fast_float/CMakeLists.txt

# Remove unused KWSys items
find Utilities/KWSys/vtksys/ -name \*.[ch]\* | grep -vE '^Utilities/KWSys/vtksys/([a-z].*|Configure|SharedForward|Status|String\.hxx|Base64|CommandLineArguments|Directory|DynamicLoader|Encoding|FStream|FundamentalType|Glob|MD5|Process|RegularExpression|System|SystemInformation|SystemTools)(C|CXX|UNIX)?\.' | xargs rm

# Save an unbuilt copy of the Example's sources for %doc
mkdir vtk-examples
cp -a Examples vtk-examples
find vtk-examples -type f | xargs chmod -R a-x

# Requires OpenTURNS which is not packaged
# -DVTK_MODULE_ENABLE_VTK_FiltersOpenTURNS:STRING=YES
# fides and ADIOS2 require ADIOS2 which is not packaged
# ZSpace is Windows only, but is getting enabled anyway
# Xdmf3 fails on i686 - https://gitlab.kitware.com/vtk/vtk/-/issues/19402
%global vtk_cmake_options \\\
 -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \\\
 -DCMAKE_INSTALL_DOCDIR=share/doc/%{name} \\\
 -DCMAKE_INSTALL_JARDIR=share/java \\\
 -DCMAKE_INSTALL_LIBDIR:PATH=%{_lib} \\\
 -DCMAKE_INSTALL_JNILIBDIR:PATH=%{_lib}/%{name} \\\
 -DCMAKE_INSTALL_LICENSEDIR:PATH=share/licenses/%{name} \\\
 -DVTK_CUSTOM_LIBRARY_SUFFIX="" \\\
 -DVTK_VERSIONED_INSTALL:BOOL=OFF \\\
 -DVTK_GROUP_ENABLE_Imaging:STRING=YES \\\
 -DVTK_GROUP_ENABLE_Qt:STRING=YES \\\
 -DVTK_GROUP_ENABLE_Rendering:STRING=YES \\\
 -DVTK_GROUP_ENABLE_StandAlone:STRING=YES \\\
 -DVTK_GROUP_ENABLE_Views:STRING=YES \\\
 -DVTK_GROUP_ENABLE_Web:STRING=YES \\\
 -DVTK_MODULE_ENABLE_VTK_AcceleratorsVTKmFilters:STRING=YES \\\
 -DVTK_MODULE_ENABLE_VTK_CommonArchive:STRING=YES \\\
 -DVTK_MODULE_ENABLE_VTK_DomainsMicroscopy:STRING=YES \\\
 -DVTK_MODULE_ENABLE_VTK_GeovisGDAL:STRING=YES \\\
 -DVTK_MODULE_ENABLE_VTK_FiltersParallelStatistics:STRING=YES \\\
 -DVTK_MODULE_ENABLE_VTK_FiltersParallelVerdict:STRING=YES \\\
 -DVTK_MODULE_ENABLE_VTK_ImagingOpenGL2:STRING=YES \\\
 -DVTK_MODULE_ENABLE_VTK_InfovisBoost:STRING=YES \\\
 -DVTK_MODULE_ENABLE_VTK_InfovisBoostGraphAlgorithms:STRING=YES \\\
%if %{with bootstrap} \
 -DVTK_MODULE_ENABLE_VTK_IOOCCT:STRING=NO \\\
%endif \
 -DVTK_MODULE_ENABLE_VTK_IOFDS:STRING=YES \\\
 -DVTK_MODULE_ENABLE_VTK_IOH5part:STRING=YES \\\
 -DVTK_MODULE_ENABLE_VTK_IOH5Rage:STRING=YES \\\
 -DVTK_MODULE_ENABLE_VTK_IOMySQL:STRING=YES \\\
 -DVTK_MODULE_ENABLE_VTK_IOOMF:STRING=YES \\\
 -DVTK_MODULE_ENABLE_VTK_IOParallelLSDyna:STRING=YES \\\
 -DVTK_MODULE_ENABLE_VTK_IOTRUCHAS:STRING=YES \\\
 -DVTK_MODULE_ENABLE_VTK_IOVPIC:STRING=YES \\\
 -DVTK_MODULE_ENABLE_VTK_IOXdmf2:STRING=YES \\\
%ifarch %{ix86} \
 -DVTK_MODULE_ENABLE_VTK_IOXdmf3:STRING=NO \\\
%endif \
 -DVTK_MODULE_ENABLE_VTK_RenderingAnari:STRING=NO \\\
 -DVTK_MODULE_ENABLE_VTK_RenderingMatplotlib:STRING=YES \\\
 -DVTK_MODULE_ENABLE_VTK_RenderingVolumeAMR:STRING=YES \\\
 -DVTK_PYTHON_OPTIONAL_LINK:BOOL=OFF \\\
%if %{with OSMesa} \
 -DVTK_OPENGL_HAS_OSMESA:BOOL=ON \\\
%endif \
%if %{with java} \
 -DVTK_WRAP_JAVA:BOOL=ON \\\
 -DVTK_JAVA_SOURCE_VERSION=8 \\\
 -DVTK_JAVA_TARGET_VERSION=8 \\\
 -DJAVA_INCLUDE_PATH:PATH=$JAVA_HOME/include \\\
 -DJAVA_INCLUDE_PATH2:PATH=$JAVA_HOME/include/linux \\\
 -DJAVA_AWT_INCLUDE_PATH:PATH=$JAVA_HOME/include \\\
 -DJAVA_AWT_LIBRARY:PATH=$JAVA_HOME/lib/libjawt.so \\\
 -DJAVA_JNI_INCLUDE_PATH:PATH=$JAVA_HOME/include \\\
 -DJAVA_JVM_LIBRARY:PATH=$JAVA_HOME/lib/libjava.so \\\
%else \
 -DVTK_WRAP_JAVA:BOOL=OFF \\\
%endif \
 -DVTK_WRAP_PYTHON:BOOL=ON \\\
 -DVTK_USE_EXTERNAL=ON \\\
 -DVTK_BUILD_ALL_MODULES=ON \\\
 -DVTK_ENABLE_OSPRAY:BOOL=OFF \\\
 -DVTK_MODULE_ENABLE_VTK_fides:STRING=NO \\\
 -DVTK_MODULE_ENABLE_VTK_FiltersOpenTURNS:STRING=NO \\\
 -DVTK_MODULE_ENABLE_VTK_IOADIOS2:STRING=NO \\\
 -DVTK_MODULE_ENABLE_VTK_IOOpenVDB:STRING=NO \\\
%if !%{with fmt} \
 -DVTK_MODULE_USE_EXTERNAL_VTK_fmt:BOOL=OFF \\\
%endif \
%if !%{with gl2ps} \
 -DVTK_MODULE_USE_EXTERNAL_VTK_gl2ps:BOOL=OFF \\\
%endif \
 -DVTK_MODULE_USE_EXTERNAL_VTK_exprtk:BOOL=OFF \\\
 -DVTK_MODULE_USE_EXTERNAL_VTK_ioss:BOOL=OFF \\\
 -DVTK_MODULE_USE_EXTERNAL_VTK_scn:BOOL=OFF \\\
 -DVTK_MODULE_USE_EXTERNAL_VTK_token:BOOL=OFF \\\
 -DVTK_MODULE_USE_EXTERNAL_VTK_verdict:BOOL=OFF \\\
 -DVTK_MODULE_USE_EXTERNAL_VTK_vtkviskores:BOOL=OFF \\\
 -DVTK_USE_TK=ON \\\
  %{?with_flexiblas:-DBLA_VENDOR=FlexiBLAS}

# $mpi will be evaluated in the loops below
%global _vpath_builddir %{_vendor}-%{_target_os}-build-${mpi:-serial}


%conf
export CFLAGS="%{optflags} -D_UNICODE -DHAVE_UINTPTR_T"
export CXXFLAGS="%{optflags} -D_UNICODE -DHAVE_UINTPTR_T"
export CPPFLAGS=-DACCEPT_USE_OF_DEPRECATED_PROJ_API_H
%if %{with java}
export JAVA_HOME=%{_prefix}/lib/jvm/java
%ifarch %{arm} s390x riscv64
# getting "java.lang.OutOfMemoryError: Java heap space" during the build
export JAVA_TOOL_OPTIONS=-Xmx2048m
%endif
%ifarch %{arm} riscv64
# Likely running out of memory during build
%global _smp_ncpus_max 2
%endif
%endif


%cmake %{cmake_gen} \
 %{vtk_cmake_options} \
 -DVTK_BUILD_DOCUMENTATION:BOOL=ON \
 -DVTK_BUILD_EXAMPLES:BOOL=ON \
 -DVTK_BUILD_TESTING:BOOL=ON


   #-DVTK_MODULE_ENABLE_VTK_FiltersParallelStatistics:STRING=YES \

export CC=mpicc
export CXX=mpic++
for mpi in %{mpi_list}
do
  module load mpi/$mpi-%{_arch}
  # CMAKE_INSTALL_LIBDIR -> ARCHIVE_DESTINATION must not be an absolute path
  # VTK_MODULE_ENABLE_VTK_FiltersParallelStatistics need MPI modules at the moment
  %cmake %{cmake_gen} \
   %{vtk_cmake_options} \
   -DCMAKE_PREFIX_PATH:PATH=$MPI_HOME \
   -DCMAKE_INSTALL_PREFIX:PATH=$MPI_HOME \
   -DCMAKE_INSTALL_LIBDIR:PATH=lib \
   -DCMAKE_INSTALL_JNILIBDIR:PATH=lib/%{name} \
   -DVTK_MODULE_ENABLE_VTK_IOPIO:STRING=YES \
   -DVTK_USE_MPI:BOOL=ON
  module purge
done


%build
%cmake_build -- --output-sync
%cmake_build --target DoxygenDoc
for mpi in %{mpi_list}
do
  module load mpi/$mpi-%{_arch}
  %cmake_build -- --output-sync
  module purge
done

# Remove executable bits from sources (some of which are generated)
find . -name \*.c -or -name \*.cxx -or -name \*.h -or -name \*.hxx -or \
       -name \*.gif | xargs chmod -x


%install
%cmake_install

pushd %{_vpath_builddir}
# Gather list of non-java/python/qt libraries
ls %{buildroot}%{_libdir}/*.so.* \
  | grep -Ev '(Java|Qt|Python)' | sed -e's,^%{buildroot},,' > libs.list

# List of executable test binaries
find bin \( -name \*Tests -o -name Test\* -o -name VTKBenchMark \) \
         -printf '%f\n' > testing.list

# Install examples too, need to remove buildtime runpath manually
for file in `cat testing.list`; do
  install -p bin/$file %{buildroot}%{_bindir}
  chrpath -l -d %{buildroot}%{_bindir}/$file
done

# Fix up filelist paths
perl -pi -e's,^,%{_bindir}/,' testing.list

# Install data
mkdir -p %{buildroot}%{_datadir}/vtkdata
cp -alL ExternalData/* %{buildroot}%{_datadir}/vtkdata/

popd

for mpi in %{mpi_list}
do
  module load mpi/$mpi-%{_arch}
  %cmake_install

  # Gather list of non-java/pythonl/qt libraries
  ls %{buildroot}%{_libdir}/${mpi}/lib/*.so.* \
    | grep -Ev '(Java|Python|Qt)' | sed -e's,^%{buildroot},,' > %{_vpath_builddir}/libs.list

  # Move licenses since we cannot install them outside of CMAKE_INSTALL_PREFIX (MPI_HOME)
  mv %{buildroot}%{_libdir}/${mpi}/share/licenses/vtk %{buildroot}%{_defaultlicensedir}/%{name}-${mpi}
  module purge
done

# Remove exec bit from non-scripts and %%doc
for file in `find %{buildroot} -type f -perm 0755 \
  | xargs -r file | grep ASCII | awk -F: '{print $1}'`; do
  head -1 $file | grep '^#!' > /dev/null && continue
  chmod 0644 $file
done
find Utilities/Upgrading -type f -print0 | xargs -0 chmod -x

# Setup Wrapping docs tree
mkdir -p _docs
cp -pr --parents Wrapping/*/README* _docs/

# Make noarch data sub-package the same on all arches
# At the moment this only contains Java/Testing/Data/Baseline
rm -rf %{buildroot}%{_datadir}/vtkdata/Wrapping

# The fixed FindHDF5.cmake is patch of CMake now
rm -v %{buildroot}/%{_libdir}/cmake/%{name}/patches/99/FindHDF5.cmake
%if %{with mpich}
rm -v %{buildroot}/%{_libdir}/mpich/lib/cmake/%{name}/patches/99/FindHDF5.cmake
%endif
%if %{with openmpi}
rm -v %{buildroot}/%{_libdir}/openmpi/lib/cmake/%{name}/patches/99/FindHDF5.cmake
%endif

# https://bugzilla.redhat.com/show_bug.cgi?id=1902729
#  contains the $ORIGIN runpath specifier at the wrong position in [/usr/lib64/mpich/lib:$ORIGIN:$ORIGIN/../]
#  0x0008 ... the special '$ORIGIN' RPATHs are appearing after other
#             RPATHs; this is just a minor issue but usually unwanted
# The paths are equivalent and "this is just a minor issue", so we are allowing it below
#  0x0010 ... the RPATH is empty; there is no reason for such RPATHs
#             and they cause unneeded work while loading libraries
# This is appearing on mpi libraries, no idea why.
export QA_RPATHS=18


%check
cp %SOURCE2 .
%if %{with xdummy}
if [ -x /usr/libexec/Xorg ]; then
   Xorg=/usr/libexec/Xorg
else
   Xorg=/usr/libexec/Xorg.bin
fi
$Xorg -noreset +extension GLX +extension RANDR +extension RENDER -logfile ./xorg.log -config ./xorg.conf -configdir . :99 &
export DISPLAY=:99
%endif
export FLEXIBLAS=netlib
%ctest --verbose || :
%if %{with xdummy}
kill %1 || :
cat xorg.log
%endif


%files -f %{_vendor}-%{_target_os}-build-serial/libs.list
%license %{_defaultlicensedir}/%{name}/
%doc README.md _docs/Wrapping
%{_datadir}/vr_actions/
%{_datadir}/xr_actions/

%files devel
%doc Utilities/Upgrading
%{_bindir}/vtkParseJava
%{_bindir}/vtkProbeOpenGLVersion
%{_bindir}/vtkWrapHierarchy
%{_bindir}/vtkWrapJava
%{_bindir}/vtkWrapSerDes

%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/cmake/%{name}/
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/hierarchy/

%files -n python%{python3_pkgversion}-vtk
%{python3_sitearch}/*
%{_libdir}/*Python*.so.*
%{_bindir}/vtkpython
%{_bindir}/vtkWrapPython
%{_bindir}/vtkWrapPythonInit

%if %{with java}
%files java
%{_libdir}/*Java.so.*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*Java.so
%{_javadir}/vtk.jar
%endif

%files qt
%{_libdir}/lib*Qt*.so.*
%exclude %{_libdir}/*Python*.so.*

%if %{with mpich}
%files mpich -f %{_vendor}-%{_target_os}-build-mpich/libs.list
%license %{_defaultlicensedir}/%{name}-mpich/
%doc README.md _docs/Wrapping
%{_libdir}/mpich/share/vr_actions/
%{_libdir}/mpich/share/xr_actions/

%files mpich-devel
%{_libdir}/mpich/bin/vtkParseJava
%{_libdir}/mpich/bin/vtkProbeOpenGLVersion
%{_libdir}/mpich/bin/vtkWrapHierarchy
%{_libdir}/mpich/bin/vtkWrapJava
%{_libdir}/mpich/bin/vtkWrapSerDes
%{_libdir}/mpich/include/
%{_libdir}/mpich/lib/*.so
%{_libdir}/mpich/lib/cmake/
%dir %{_libdir}/mpich/lib/%{name}
%{_libdir}/mpich/lib/%{name}/hierarchy/

%files -n python%{python3_pkgversion}-vtk-mpich
%{_libdir}/mpich/lib/python%{python3_version}/
%{_libdir}/mpich/lib/*Python*.so.*
%{_libdir}/mpich/bin/pvtkpython
%{_libdir}/mpich/bin/vtkpython
%{_libdir}/mpich/bin/vtkWrapPython
%{_libdir}/mpich/bin/vtkWrapPythonInit

%if %{with java}
%files mpich-java
%{_libdir}/mpich/lib/*Java.so.*
%dir %{_libdir}/mpich/lib/%{name}
%{_libdir}/mpich/lib/%{name}/*Java.so
%{_libdir}/mpich/share/java/vtk.jar
%endif

%files mpich-qt
%{_libdir}/mpich/lib/lib*Qt*.so.*
%exclude %{_libdir}/mpich/lib/*Python*.so.*
%endif

%if %{with openmpi}
%files openmpi -f %{_vendor}-%{_target_os}-build-openmpi/libs.list
%license %{_defaultlicensedir}/%{name}-openmpi/
%doc README.md _docs/Wrapping
%{_libdir}/openmpi/share/vr_actions/
%{_libdir}/openmpi/share/xr_actions/

%files openmpi-devel
%{_libdir}/openmpi/bin/vtkParseJava
%{_libdir}/openmpi/bin/vtkProbeOpenGLVersion
%{_libdir}/openmpi/bin/vtkWrapHierarchy
%{_libdir}/openmpi/bin/vtkWrapJava
%{_libdir}/openmpi/bin/vtkWrapSerDes
%{_libdir}/openmpi/include/
%{_libdir}/openmpi/lib/*.so
%{_libdir}/openmpi/lib/cmake/
%dir %{_libdir}/openmpi/lib/%{name}
%{_libdir}/openmpi/lib/%{name}/hierarchy/

%files -n python%{python3_pkgversion}-vtk-openmpi
%{_libdir}/openmpi/lib/python%{python3_version}/
%{_libdir}/openmpi/lib/*Python*.so.*
%{_libdir}/openmpi/bin/pvtkpython
%{_libdir}/openmpi/bin/vtkpython
%{_libdir}/openmpi/bin/vtkWrapPython
%{_libdir}/openmpi/bin/vtkWrapPythonInit

%if %{with java}
%files openmpi-java
%{_libdir}/openmpi/lib/*Java.so.*
%dir %{_libdir}/openmpi/lib/%{name}
%{_libdir}/openmpi/lib/%{name}/*Java.so
%{_libdir}/openmpi/share/java/vtk.jar
%endif

%files openmpi-qt
%{_libdir}/openmpi/lib/lib*Qt*.so.*
%exclude %{_libdir}/openmpi/lib/*Python*.so.*
%endif

%files data
%{_datadir}/vtkdata

%files doc
%{_docdir}/%{name}/

%files testing -f %{_vendor}-%{_target_os}-build-serial/testing.list

%files examples
%doc vtk-examples/Examples


%changelog
%autochangelog
