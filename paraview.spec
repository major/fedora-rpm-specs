#LTO fails at the moment
%undefine _lto_cflags

%global __cmake_in_source_build 1
%if 0%{?fedora}
%define _legacy_common_support 1
%endif

%{!?build_openmpi:%global build_openmpi 1}
%{!?build_mpich:%global build_mpich 1}
%global pv_maj 5
%global pv_min 11
%global pv_patch 1
%global pv_majmin %{pv_maj}.%{pv_min}
#global rcsuf RC1
%{?rcsuf:%global relsuf .%{rcsuf}}
%{?rcsuf:%global versuf -%{rcsuf}}

# Python2 prefix for building on rhel
%if 0%{?rhel}
%global py2_prefix python
%else
%global py2_prefix python2
%endif

# cgnslib is too old on EL8
%if 0%{?el8}
%bcond_with cgnslib
%else
%bcond_without cgnslib
%endif
%if %{with cgnslib}
%global vtk_use_system_cgnslib -DVTK_MODULE_USE_EXTERNAL_ParaView_cgns:BOOL=ON
%else
%global vtk_use_system_cgnslib -DVTK_MODULE_USE_EXTERNAL_ParaView_cgns:BOOL=OFF
%endif

# VTK currently requires unreleased fmt 8.1.0
%bcond_with fmt

# VTK currently is carrying local modifications to gl2ps
%bcond_with gl2ps
%if !%{with gl2ps}
%global vtk_use_system_gl2ps -DVTK_MODULE_USE_EXTERNAL_VTK_gl2ps:BOOL=OFF
%endif

# Default to Qt5 on Fedora and RHEL 8+
%if 0%{?fedora} || 0%{?rhel} >= 8
%bcond_without qt5
%else
%bcond_with qt5
%endif

# Enable VisitBridge plugin (bz#1546474)
%bcond_without VisitBridge

# We need jsoncpp >= 0.7
%if 0%{?fedora} || 0%{?rhel} >= 8
%global system_jsoncpp 1
%global vtk_use_system_jsoncpp -DVTK_MODULE_USE_EXTERNAL_VTK_jsoncpp:BOOL=ON
%else
%global system_jsoncpp 0
%global vtk_use_system_jsoncpp -DVTK_MODULE_USE_EXTERNAL_VTK_jsoncpp:BOOL=OFF
%endif

%bcond_without protobuf
%if %{with protobuf}
%global vtk_use_system_protobuf -DVTK_MODULE_USE_EXTERNAL_ParaView_protobuf:BOOL=ON
%else
%global vtk_use_system_protobuf -DVTK_MODULE_USE_EXTERNAL_ParaView_protobuf:BOOL=OFF
%endif

# We need pugixml >= 1.9
%if 0%{?fedora} || 0%{?rhel} >= 8
# ParaView 5.7.0 disabled building with external pugixml
%global system_pugixml 1
%global vtk_use_system_pugixml -DVTK_MODULE_USE_EXTERNAL_VTK_pugixml:BOOL=ON
%else
%global system_pugixml 0
%global vtk_use_system_pugixml -DVTK_MODULE_USE_EXTERNAL_VTK_pugixml:BOOL=OFF
%endif

Name:           paraview
Version:        5.11.1
Release:        2%{?dist}
Summary:        Parallel visualization application

License:        BSD
URL:            https://www.paraview.org/
Source0:        https://www.paraview.org/files/v%{pv_majmin}/ParaView-v%{version}%{?versuf}.tar.gz
Source1:        paraview.xml
Source2:        FindPEGTL.cmake
# Fix cmake files install location
# https://gitlab.kitware.com/paraview/paraview/issues/19724
Patch0:         paraview-cmakedir.patch
# Fix build with newer freetype
# https://gitlab.kitware.com/vtk/vtk/-/issues/18033
Patch3:         paraview-freetype.patch

BuildRequires:  cmake >= 3.12
BuildRequires:  make
BuildRequires:  lz4-devel
%if %{with qt5}
BuildRequires:  cmake(Qt5)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5UiPlugin)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  qt5-qtwebkit-devel
BuildRequires:  /usr/bin/xmlpatterns-qt5
%else
BuildRequires:  qt-devel
BuildRequires:  qt-webkit-devel
%endif
BuildRequires:  mesa-libOSMesa-devel
%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires:  python3-devel
BuildRequires:  python3-netcdf4
BuildRequires:  python3-qt5
# Fails looking for PythonQt_QtBindings.h
# https://gitlab.kitware.com/paraview/paraview/issues/17365
#BuildRequires:  pythonqt-devel
%else
BuildRequires:  python2-devel
BuildRequires:  python2-netcdf4
# Fails looking for PythonQt_QtBindings.h
# https://gitlab.kitware.com/paraview/paraview/issues/17365
#BuildRequires:  pythonqt-devel
%if %{with qt5}
BuildRequires:  %{py2_prefix}-qt5
%endif
%endif
%if %{with cgnslib}
BuildRequires:  cgnslib-devel
%endif
BuildRequires:  cli11-devel
BuildRequires:  gdal-devel
BuildRequires:  hdf5-devel
BuildRequires:  tk-devel
BuildRequires:  freetype-devel, libtiff-devel, zlib-devel
BuildRequires:  expat-devel
BuildRequires:  glew-devel
BuildRequires:  readline-devel
BuildRequires:  openssl-devel
BuildRequires:  gnuplot
BuildRequires:  wget
BuildRequires:  boost-devel
BuildRequires:  double-conversion-devel
BuildRequires:  eigen3-devel
%if %{with fmt}
BuildRequires:  fmt-devel >= 8.1.0
%endif
%if 0%{with gl2ps}
BuildRequires:  gl2ps-devel >= 1.3.8
%endif
BuildRequires:  hwloc-devel
%if %{system_jsoncpp}
BuildRequires:  jsoncpp-devel >= 0.7.0
%endif
# Requires patched libharu https://github.com/libharu/libharu/pull/157
#BuildRequires:  libharu-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtheora-devel
BuildRequires:  libxml2-devel
BuildRequires:  libXt-devel
BuildRequires:  netcdf-cxx-devel
BuildRequires:  cmake(nlohmann_json)
BuildRequires:  patchelf
BuildRequires:  PEGTL-devel
BuildRequires:  proj-devel
%if %{with protobuf}
BuildRequires:  protobuf-devel
%endif
%if %{system_pugixml}
BuildRequires:  pugixml-devel >= 1.9
%endif
BuildRequires:  sqlite-devel
BuildRequires:  utf8cpp-devel
# For validating desktop and appdata files
BuildRequires:  desktop-file-utils
%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires:  libappstream-glib
%endif
BuildRequires:  glibc-langpack-en

Requires: hdf5%{?_hdf5_version: = %{_hdf5_version}}
Requires: %{name}-data = %{version}-%{release}
%if 0%{?fedora} || 0%{?rhel} >= 8
#Recommends: python3-pygments
Requires: python3-pygments
Requires: python3-six
Requires: python3-netcdf4
Requires: python3-numpy
Requires: python3-twisted
Requires: python3-autobahn
%else
Requires: %{py2_prefix}-pygments
Requires: python2-six
Requires: python2-netcdf4
Requires: python2-numpy
Requires: %{py2_prefix}-twisted
Requires: %{py2_prefix}-autobahn
%endif
# ParaView requires svg support via icon plugins, so no direct linking involved
Requires: qt5-qtsvg%{?_isa}
Requires: qt5-qtx11extras%{?_isa}

# Bundled KWSys
# https://fedorahosted.org/fpc/ticket/555
# Components used are specified in VTK/Utilities/KWSys/CMakeLists.txt
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
# Bundled cgnslib
%if !%{with cgnslib}
Provides: bundled(cgnslib) = 4.1
%endif
%if !%{with fmt}
Provides: bundled(fmt) = 8.1.0
%endif
# Bundled jsoncpp
%if !0%{system_jsoncpp}
Provides: bundled(jsoncpp) = 0.7.0
%endif
# Bundled protobuf
%if !%{with protobuf}
Provides: bundled(protobuf) = 2.3.0
%endif
%if !0%{system_pugixml}
Provides: bundled(pugixml) = 1.9
%endif
# Bundled vtk
# https://bugzilla.redhat.com/show_bug.cgi?id=697842
Provides: bundled(vtk) = 6.3.0
Provides: bundled(catalyst) = 2.0
Provides: bundled(diy2)
Provides: bundled(exprtk) = 2.71
Provides: bundled(h5part) = 1.6.6
Provides: bundled(kissfft)
Provides: bundled(icet)
Provides: bundled(ioss) = 20210512
Provides: bundled(libharu)
Provides: bundled(libproj4)
Provides: bundled(qttesting)
Provides: bundled(verdict) = 1.4.0
Provides: bundled(xdmf2)

# Do not provide anything in paraview's library directory
%global __provides_exclude_from ^(%{_libdir}/paraview/|%{_libdir}/.*/lib/paraview/).*$
# Do not require anything provided in paraview's library directory
# This list needs to be maintained by hand
%if %{with protobuf}
%global __requires_exclude ^lib(catalyst|IceT|pq|QtTesting|vtk).*$
%else
%global __requires_exclude ^lib(catalyst|IceT|pq|QtTesting|vtk|protobuf).*$
%endif


#-- Plugin: VRPlugin - Virtual Reality Devices and Interactor styles : Disabled - Requires VRPN
#-- Plugin: MantaView - Manta Ray-Cast View : Disabled - Requires Manta
#-- Plugin: ForceTime - Override time requests : Disabled - Build is failing
#-- Plugin: VaporPlugin - Plugin to read NCAR VDR files : Disabled - Requires vapor

# We want to build with a system vtk someday, but it doesn't work yet
# -DPARAVIEW_USE_EXTERNAL_VTK:BOOL=ON \\\
# -DVTK_DIR=%%{_libdir}/vtk \\\

# Add -DOMPI_SKIP_MPICXX to work around issue with MPI linkage and exodus
# https://gitlab.kitware.com/paraview/paraview/-/issues/20060
%global paraview_cmake_options \\\
        -DCMAKE_BUILD_TYPE=RelWithDebInfo \\\
        -DCMAKE_CXX_FLAGS_RELWITHDEBINFO:STRING="-DNDEBUG -DOMPI_SKIP_MPICXX" \\\
        -DOpenGL_GL_PREFERENCE=GLVND \\\
        -DPARAVIEW_BUILD_SHARED_LIBS:BOOL=ON \\\
        -DPARAVIEW_VERSIONED_INSTALL:BOOL=OFF \\\
        -DPARAVIEW_ENABLE_GDAL:BOOL=ON \\\
        -DPARAVIEW_USE_PYTHON:BOOL=ON \\\
        -DPARAVIEW_INSTALL_DEVELOPMENT_FILES:BOOL=ON \\\
%if 0%{?fedora} || 0%{?rhel} >= 8 \
        -DVTK_PYTHON_VERSION=3 \\\
%else \
        -DVTK_PYTHON_VERSION=2 \\\
%endif \
        -DPARAVIEW_BUILD_WITH_EXTERNAL:BOOL=ON \\\
        -DVTK_MODULE_USE_EXTERNAL_ParaView_vtkcatalyst:BOOL=OFF \\\
        %{?vtk_use_system_cgnslib} \\\
        -DVTK_MODULE_USE_EXTERNAL_VTK_exprtk:BOOL=OFF \\\
%if !%{with fmt} \
        -DVTK_MODULE_USE_EXTERNAL_VTK_fmt:BOOL=OFF \\\
%endif \
        %{?vtk_use_system_gl2ps} \\\
        -DVTK_MODULE_USE_EXTERNAL_VTK_ioss:BOOL=OFF \\\
        %{?vtk_use_system_jsoncpp} \\\
        -DVTK_MODULE_USE_EXTERNAL_VTK_libharu=OFF \\\
        %{?vtk_use_system_protobuf} \\\
        %{?vtk_use_system_pugixml} \\\
        -DVTK_MODULE_USE_EXTERNAL_VTK_verdict:BOOL=OFF \\\
        -DBUILD_EXAMPLES:BOOL=ON \\\
        -DBUILD_TESTING:BOOL=OFF \\\
        -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON

%global paraview_cmake_mpi_options \\\
        -DCMAKE_PREFIX_PATH:PATH=$MPI_HOME \\\
        -DCMAKE_INSTALL_PREFIX:PATH=$MPI_HOME \\\
        -DCMAKE_INSTALL_CMAKEDIR:PATH=lib/cmake \\\
        -DCMAKE_INSTALL_INCLUDEDIR:PATH=../../include/$MPI_COMPILER/%{name} \\\
        -DCMAKE_INSTALL_LIBDIR:PATH=lib/%{name} \\\
        -DHDF5_INCLUDE_DIRS:PATH=$MPI_INCLUDE \\\
%if 0%{?fedora} || 0%{?rhel} >= 8 \
        -DPYTHON_INSTALL_DIR=PATH=$MPI_PYTHON3_SITEARCH \\\
%else \
        -DPYTHON_INSTALL_DIR=PATH=$MPI_PYTHON2_SITEARCH \\\
%endif \
        -DVTK_MODULE_USE_EXTERNAL_VTK_diy2=OFF \\\
        -DVTK_MODULE_USE_EXTERNAL_VTK_icet=OFF \\\
        -DQtTesting_INSTALL_LIB_DIR=lib/%{name} \\\
        -DQtTesting_INSTALL_CMAKE_DIR=lib/%{name}/CMake \\\
        -DPARAVIEW_USE_MPI:BOOL=ON \\\
        -DICET_BUILD_TESTING:BOOL=ON \\\
%if %{with VisitBridge} \
        -DPARAVIEW_USE_VISITBRIDGE=ON \\\
        -DVTK_MODULE_USE_EXTERNAL_ParaView_VisItLib:BOOL=OFF \\\
        -DVISIT_BUILD_READER_CGNS=ON \\\
%endif \
        %{paraview_cmake_options}

%description
ParaView is an open-source, multi-platform data analysis and visualization
application. ParaView users can quickly build visualizations to analyze their
data using qualitative and quantitative techniques. The data exploration can
be done interactively in 3D or programmatically using ParaView’s batch
processing capabilities.

ParaView was developed to analyze extremely large datasets using distributed
memory computing resources. It can be run on supercomputers to analyze
datasets of petascale size as well as on laptops for smaller data.

NOTE: The version in this package has NOT been compiled with MPI support.
%if %{build_openmpi}
Install the paraview-openmpi package to get a version compiled with openmpi.
%endif
%if %{build_mpich}
Install the paraview-mpich package to get a version compiled with mpich.
%endif


%package        data
Summary:        Data files for ParaView

Requires:       %{name} = %{version}-%{release}

BuildArch:      noarch

%description    data
%{summary}.


%package        devel
Summary:        Development files for %{name}

Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       vtk-devel%{?_isa}

Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        doc
Summary:        Documentation files for ParaView

BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  hardlink

%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-sphinx
BuildRequires:  python3-twisted
BuildRequires:  python3-autobahn
BuildRequires:  python3-markupsafe
%else
BuildRequires:  python2-devel
BuildRequires:  python2-numpy
BuildRequires:  python2-sphinx
BuildRequires:  python2-markupsafe
# Unavailable on rhel
BuildRequires:  %{py2_prefix}-twisted
BuildRequires:  %{py2_prefix}-autobahn
%endif

BuildArch:      noarch

%description    doc
%{summary}.


%if %{build_openmpi}
%package        openmpi
Summary:        Parallel visualization application

BuildRequires:  openmpi-devel
BuildRequires:  netcdf-openmpi-devel
%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires:  python3-mpi4py-openmpi
%else
BuildRequires:  mpi4py-openmpi
%endif

Requires:       %{name}-data = %{version}-%{release}
%if 0%{?fedora} || 0%{?rhel} >= 8
Requires:       python3-autobahn
Requires:       python3-mpi4py-openmpi
Requires:       python3-numpy
Requires:       python3-pygments
Requires:       python3-six
Requires:       python3-twisted
%else
Requires:       %{py2_prefix}-autobahn
Requires:       python2-numpy
Requires:       %{py2_prefix}-pygments
Requires:       python2-six
Requires:       %{py2_prefix}-twisted
Requires:       mpi4py-openmpi
%endif
# ParaView requires svg support via icon plugins, so no direct linking involved
Requires:       qt5-qtsvg%{?_isa}
Requires:       qt5-qtx11extras%{?_isa}

%description    openmpi
This package contains copies of the ParaView server binaries compiled with
OpenMPI.  These are named pvserver_openmpi, pvbatch_openmpi, etc.

You will need to load the openmpi-%{_arch} module to setup your path properly.


%package        openmpi-devel
Summary:        Development files for %{name}-openmpi

Requires:       %{name}-openmpi%{?_isa} = %{version}-%{release}

Provides:       %{name}-openmpi-static = %{version}-%{release}
Provides:       %{name}-openmpi-static%{?_isa} = %{version}-%{release}

%description    openmpi-devel
The %{name}-openmpi-devel package contains libraries and header files for
developing applications that use %{name}-openmpi.
%endif


%if %{build_mpich}
%package        mpich
Summary:        Parallel visualization application

BuildRequires:  mpich-devel
BuildRequires:  netcdf-mpich-devel
%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires:  python3-mpi4py-mpich
%else
BuildRequires:  mpi4py-mpich
%endif

Requires:       %{name}-data = %{version}-%{release}
%if 0%{?fedora} || 0%{?rhel} >= 8
Requires:       python3-autobahn
Requires:       python3-mpi4py-mpich
Requires:       python3-numpy
Requires:       python3-pygments
Requires:       python3-six
Requires:       python3-twisted
%else
Requires:       %{py2_prefix}-autobahn
Requires:       python2-numpy
Requires:       %{py2_prefix}-pygments
Requires:       python2-six
Requires:       %{py2_prefix}-twisted
Requires:       mpi4py-mpich
%endif
# ParaView requires svg support via icon plugins, so no direct linking involved
Requires:       qt5-qtsvg%{?_isa}
Requires:       qt5-qtx11extras%{?_isa}

%description    mpich
This package contains copies of the ParaView server binaries compiled with
mpich.  These are named pvserver_mpich, pvbatch_mpich, etc.

You will need to load the mpich-%{_arch} module to setup your path properly.


%package        mpich-devel
Summary:        Development files for %{name}-mpich

Requires:       %{name}-mpich%{?_isa} = %{version}-%{release}

Provides:       %{name}-mpich-static = %{version}-%{release}
Provides:       %{name}-mpich-static%{?_isa} = %{version}-%{release}

%description    mpich-devel
The %{name}-mpich-devel package contains libraries and header files for
developing applications that use %{name}-mpich.
%endif


%prep
%autosetup -p1 -n ParaView-v%{version}%{?versuf}

%if %{with VisitBridge}
cp -p Utilities/VisItBridge/README.md Utilities/VisItBridge/README-VisItBridge.md

# See https://gitlab.kitware.com/paraview/paraview/issues/17456
rm -f Utilities/VisItBridge/databases/readers/Vs/VsStaggeredField.C
%endif

# Install python properly
sed -i -s '/VTK_INSTALL_PYTHON_USING_CMAKE/s/TRUE/FALSE/' CMakeLists.txt
#Remove included thirdparty sources just to be sure
for x in %{?_with_cgnslib:vtkcgns} %{?_with_protobuf:vtkprotobuf}
do
  rm -r ThirdParty/*/${x}
done
%if %{system_pugixml}
rm -r VTK/ThirdParty/pugixml/vtkpugixml
%endif
# TODO - loguru
# TODO - verdict - This is a kitware library so low priority
for x in vtk{cli11,doubleconversion,eigen,expat,%{?with_fmt:fmt,}freetype,%{?_with_gl2ps:gl2ps,}glew,hdf5,jpeg,libproj,libxml2,lz4,lzma,mpi4py,netcdf,ogg,pegtl,png,sqlite,theora,tiff,zfp,zlib}
do
  rm -r VTK/ThirdParty/*/${x}
done
# jsoncpp
%if 0%{system_jsoncpp}
rm -r VTK/ThirdParty/jsoncpp/vtkjsoncpp
%endif
# Remove unused KWSys items
find VTK/Utilities/KWSys/vtksys/ -name \*.[ch]\* | grep -vE '^VTK/Utilities/KWSys/vtksys/([a-z].*|Configure|SharedForward|Status|String\.hxx|Base64|CommandLineArguments|Directory|DynamicLoader|Encoding|FStream|FundamentalType|Glob|MD5|Process|RegularExpression|System|SystemInformation|SystemTools)(C|CXX|UNIX)?\.' | xargs rm
cp %SOURCE2 VTK/CMake/FindPEGTL.cmake
# We want to build with a system vtk someday, but it doesn't work yet
#rm -r VTK

%build
# Try to limit memory consumption on some arches
%ifarch %{arm}
%global optflags %(echo %{optflags} | sed 's/-g /-g1 /')
%endif
%ifarch ppc64le
%global _smp_mflags -j2
%endif
mkdir %{_target_platform}
pushd %{_target_platform}
%cmake -Wno-dev .. \
        -DCMAKE_INSTALL_CMAKEDIR:PATH=%{_lib}/cmake \
        -DCMAKE_INSTALL_LIBDIR:PATH=%{_lib}/%{name} \
        -DPARAVIEW_BUILD_DEVELOPER_DOCUMENTATION:BOOL=ON \
        -DQtTesting_INSTALL_LIB_DIR=%{_lib}/%{name} \
        -DQtTesting_INSTALL_CMAKE_DIR=%{_lib}/%{name}/CMake \
        %{paraview_cmake_options}
%make_build
export LANG=en_US.UTF-8
# Built-in Python modules were not found, set pythonpath as workaround
export PYTHONPATH=$PWD/%{_lib}/paraview/python%{python3_version}/site-packages:%{python3_sitelib}:%{python3_sitearch}
%make_build ParaViewDoxygenDoc ParaViewPythonDoc
popd
%if %{build_openmpi}
mkdir %{_target_platform}-openmpi
pushd %{_target_platform}-openmpi
%{_openmpi_load}
%cmake -Wno-dev .. \
        %{paraview_cmake_mpi_options}
%make_build
%{_openmpi_unload}
popd
%endif
%if %{build_mpich}
mkdir %{_target_platform}-mpich
pushd %{_target_platform}-mpich
%{_mpich_load}
# EL7 mpich module doesn't set PYTHONPATH
# https://bugzilla.redhat.com/show_bug.cgi?id=1148992
[ -z "$PYTHONPATH" ] && export PYTHONPATH=$MPI_PYTHON_SITEARCH
%cmake -Wno-dev .. \
        %{paraview_cmake_mpi_options}
%make_build
%{_mpich_unload}
popd
%endif


%install
# Fix permissions
find . \( -name \*.txt -o -name \*.xml -o -name '*.[ch]' -o -name '*.[ch][px][px]' \) -print0 | xargs -0 chmod -x

# Create some needed directories
install -d %{buildroot}%{_datadir}/applications
install -d %{buildroot}%{_datadir}/mime/packages
install -m644 %SOURCE1 %{buildroot}%{_datadir}/mime/packages

%if %{build_openmpi}
%{_openmpi_load}

# Install openmpi version
%make_install -C %{_target_platform}-openmpi

# Remove mpi copy of doc and man pages and  data
rm -rf %{buildroot}%{_libdir}/openmpi/share/{metainfo,applications,doc,icons,man,mimeinfo,paraview,vtkm-*}

# Set rpaths of every library
for i in `find %{buildroot}$MPI_LIB -name "*.so*" -type f -print`; do
    patchelf --print-rpath --set-rpath $MPI_LIB $i
done

%{_openmpi_unload}
%endif

%if %{build_mpich}
%{_mpich_load}

# Install mpich version
%make_install -C %{_target_platform}-mpich

# Remove mpi copy of doc and man pages and data
rm -rf %{buildroot}%{_libdir}/mpich/share/{metainfo,applications,doc,icons,man,mimeinfo,paraview,vtkm-*}

# Set rpaths of every library
for i in `find %{buildroot}$MPI_LIB -name "*.so*" -type f -print`; do
    patchelf --print-rpath --set-rpath $MPI_LIB $i
done

%{_mpich_unload}
%endif

#Install the normal version
%make_install -C %{_target_platform}

desktop-file-validate %{buildroot}%{_datadir}/applications/org.paraview.ParaView.desktop
%if 0%{?fedora} || 0%{?rhel} >= 8
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/org.paraview.ParaView.appdata.xml
%endif

#Cleanup only vtk conflicting binaries
rm %{buildroot}%{_bindir}/vtk{ParseJava,ProbeOpenGLVersion,Wrap{Hierarchy,Java,Python}}*

# Build autodocs and move documentation-files to proper location
mkdir -p %{buildroot}%{_pkgdocdir}
install -pm 0644 README.md %{buildroot}%{_pkgdocdir}
install -pm 0644 Utilities/VisItBridge/README-VisItBridge.md %{buildroot}%{_pkgdocdir}
mv %{buildroot}%{_docdir}/ParaView/* %{buildroot}%{_pkgdocdir}
rm -rf %{buildroot}%{_docdir}/ParaView
find %{buildroot}%{_pkgdocdir} -name '.*' -print0 | xargs -0 rm -frv
find %{buildroot}%{_pkgdocdir} -name '*.map' -or -name '*.md5' -print -delete
hardlink -cfv %{buildroot}%{_pkgdocdir}

%if 0%{?rhel} && 0%{?rhel} <= 7
%post
update-desktop-database &> /dev/null ||:

%postun
update-desktop-database &> /dev/null ||:
%endif

%pre
#Handle changing from directory to file
if [ -d %{_libdir}/paraview/paraview ]; then
  rm -r %{_libdir}/paraview/paraview
fi

%if 0%{?rhel} && 0%{?rhel} <= 7
%post data
/bin/touch --no-create %{_datadir}/mime/packages &>/dev/null || :
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun data
if [ $1 -eq 0 ] ; then
  update-mime-database %{_datadir}/mime &> /dev/null || :
  /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
  /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans data
update-mime-database %{_datadir}/mime &> /dev/null || :
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
%endif

%files
%{_bindir}/%{name}
%{_bindir}/%{name}.conf
%{_bindir}/pvbatch
# Currently disabled upstream
#{_bindir}/pvblot
%{_bindir}/pvdataserver
%{_bindir}/pvpython
%{_bindir}/pvrenderserver
%{_bindir}/pvserver
%{_bindir}/smTestDriver
%{_libdir}/%{name}/
%exclude %{_libdir}/%{name}/*.a

%files data
%license Copyright.txt License_v1.2.txt
%dir %{_pkgdocdir}
%{_pkgdocdir}/README.md
%{_pkgdocdir}/README-VisItBridge.md
%{_datadir}/metainfo/org.paraview.ParaView.appdata.xml
%{_datadir}/applications/org.paraview.ParaView.desktop
%{_datadir}/icons/hicolor/*/apps/paraview.png
%license %{_datadir}/licenses/ParaView/
%{_datadir}/mime/packages/paraview.xml
%{_datadir}/%{name}/

%files devel
%{_bindir}/paraview-config
%{_bindir}/vtkWrapClientServer
%{_bindir}/vtkProcessXML
%{_includedir}/%{name}/
%{_libdir}/cmake/
%{_libdir}/%{name}/*.a

%files doc
%{_pkgdocdir}

%if %{build_openmpi}
%files openmpi
%{_libdir}/openmpi/bin/[ps]*
%{_libdir}/openmpi/lib/%{name}/
%exclude %{_libdir}/openmpi/lib/%{name}/*.a
%{_libdir}/openmpi/share/licenses/

%files openmpi-devel
%{_includedir}/openmpi-%{_arch}/%{name}/
%{_libdir}/openmpi/bin/vtk*
%{_libdir}/openmpi/lib/cmake/
%{_libdir}/openmpi/lib/%{name}/*.a
%endif


%if %{build_mpich}
%files mpich
%{_libdir}/mpich/bin/[ps]*
%{_libdir}/mpich/lib/%{name}/
%exclude %{_libdir}/mpich/lib/%{name}/*.a
%{_libdir}/mpich/share/licenses/

%files mpich-devel
%{_includedir}/mpich-%{_arch}/%{name}/
%{_libdir}/mpich/bin/vtk*
%{_libdir}/mpich/lib/cmake/
%{_libdir}/mpich/lib/%{name}/*.a
%endif


%changelog
* Thu May 11 2023 Sandro Mani <manisandro@gmail.com> - 5.11.1-2
- Rebuild (gdal)

* Sat Apr 01 2023 Orion Poplawski <orion@nwra.com> - 5.11.1-1
- Update to 5.11.1

* Fri Jan 20 2023 Orion Poplawski <orion@nwra.com> - 5.11.0-3
- Add patch for gcc 13

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Nov 19 2022 Orion Poplawski <orion@nwra.com> - 5.11.0-1
- Update to 5.11.0

* Sat Nov 12 2022 Sandro Mani <manisandro@gmail.com> - 5.10.1-6
- Rebuild (gdal)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.10.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 29 2022 Orion Poplawski <orion@nwra.com> - 5.10.1-4
- Add upstream patch to fix VTK build with netcdf 4.9.0

* Wed Jun 29 2022 Python Maint <python-maint@redhat.com> - 5.10.1-3
- Rebuilt for Python 3.11

* Fri May 20 2022 Sandro Mani <manisandro@gmail.com> - 5.10.1-2
- Rebuild for gdal-3.5.0 and/or openjpeg-2.5.0

* Tue Mar 22 2022 Orion Poplawski <orion@nwra.com> - 5.10.1-1
- Update to 5.10.1

* Tue Mar 22 2022 Sandro Mani <manisandro@gmail.com> - 5.10.0-0.5
- Rebuild for cgnslib-4.3.0

* Thu Feb 10 2022 Orion Poplawski <orion@nwra.com> - 5.10.0-0.4
- Rebuild for glew 2.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.10.0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 22 2021 Orion Poplawski <orion@nwra.com> - 5.10.0-1
- Update to 5.10.0

* Tue Nov 30 2021 Orion Poplawski <orion@nwra.com> - 5.10.0-0.2.RC2
- Update to 5.10.0 RC2

* Sun Nov 21 2021 Orion Poplawski <orion@nwra.com> - 5.10.0-0.1.RC1
- Update to 5.10.0 RC1

* Thu Nov 11 2021 Sandro Mani <manisandro@gmail.com> - 5.9.1-8
- Rebuild (gdal)

* Fri Nov 05 2021 Adrian Reber <adrian@lisas.de> - 5.9.1-7
- Rebuilt for protobuf 3.19.0

* Wed Nov 03 2021 Björn Esser <besser82@fedoraproject.org> - 5.9.1-6
- Rebuild (jsoncpp)

* Fri Oct 22 2021 Adrian Reber <adrian@lisas.de> - 5.9.1-5
- Rebuilt for protobuf 3.18.1

* Tue Aug 10 2021 Orion Poplawski <orion@nwra.com> - 5.9.1-4
- Rebuild for hdf5 1.10.7/netcdf 4.8.0

* Mon Aug 02 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild
- Set installation directory of MPI Python3 files
- Fix rpaths of MPI libraries

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 5.9.1-2
- Rebuilt for Python 3.10

* Mon May 31 2021 Orion Poplawski <orion@nwra.com> - 5.9.1-1
- Update to 5.9.1

* Fri May 07 2021 Sandro Mani <manisandro@gmail.com> - 5.9.0-6
- Rebuild (gdal)

* Thu Apr 29 2021 Sandro Mani <manisandro@gmail.com> - 5.9.0-5
- Rebuild (cgnslib)

* Thu Apr 29 2021 Orion Poplawski <orion@nwra.com> - 5.9.0-4
- Remove vtkProbeOpenGLVersion conflict with vtk-devel (bz#1954777)

* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 5.9.0-3
- Rebuilt for removed libstdc++ symbol (#1937698)

* Mon Feb 01 2021 Orion Poplawski <orion@nwra.com> - 5.9.0-2
- Exclude libcatalyst from requires (bz#1923074)

* Wed Jan 27 2021 Orion Poplawski <orion@nwra.com> - 5.9.0-1
- Update to 5.9.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.8.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 12 14:20:33 CET 2021 Adrian Reber <adrian@lisas.de> - 5.8.1-7
- Rebuilt for protobuf 3.14

* Sun Dec 06 2020 Jeff Law law <law@redhat.com> - 5.8.1-6
- Fix missing #includes for gcc-11 and deprecated Qt construct

* Wed Nov 11 13:03:59 CET 2020 Sandro Mani <manisandro@gmail.com> - 5.8.1-5
- Rebuild (proj, gdal)

* Sun Nov  1 2020 Orion Poplawski <orion@nwra.com> - 5.8.1-4
- Add -DOMPI_SKIP_MPICXX to work around Exodus II MPI linkage issue (bz#1892171)

* Sat Oct 31 2020 Orion Poplawski <orion@nwra.com> - 5.8.1-3
- Add patch to fix build with newer freetype

* Wed Sep 23 2020 Adrian Reber <adrian@lisas.de> - 5.8.1-2
- Rebuilt for protobuf 3.13

* Wed Aug 05 2020 Orion Poplawski <orion@nwra.com> - 5.8.1-1
- Update to 5.8.1
- Disable LTO for now

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.8.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 Jeff Law <law@redhat.com> - 5.8.0-10
- Use __cmake_in_source_build

* Thu Jul 16 2020 Orion Poplawski <orion@nwra.com> - 5.8.0-9
- Build with GDAL support (bz#1857498)

* Fri Jul 10 2020 Orion Poplawski <orion@nwra.com> - 5.8.0-8
- Require qt5-qtsvg for icons

* Thu Jun 25 2020 Orion Poplawski <orion@cora.nwra.com> - 5.8.0-7
- Rebuild for hdf5 1.10.6

* Sun Jun 21 2020 Adrian Reber <adrian@lisas.de> - 5.8.0-6
- Rebuilt for protobuf 3.12

* Fri Jun 19 2020 Orion Poplawski <orion@nwra.com> - 5.8.0-5
- Drop _python_bytecompile_extra

* Sat May 30 2020 Björn Esser <besser82@fedoraproject.org> - 5.8.0-4
- Rebuild (jsoncpp)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 5.8.0-3
- Rebuilt for Python 3.9

* Fri May 08 2020 Björn Esser <besser82@fedoraproject.org> - 5.8.0-2
- Rebuild (cgnslib)
- Add patch to fix build with CGNS >= 4.1.1

* Thu Feb 27 2020 Orion Poplawski <orion@nwra.com> - 5.8.0-1
- Update to 5.8.0

* Mon Feb 17 2020 Sandro Mani <manisandro@gmail.com> - 5.6.0-16
- Rebuild (cgnslib)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 18 2019 Orion Poplawski <orion@cora.nwra.com> - 5.6.0-14
- Rebuild for protobuf 3.11

* Fri Dec 13 2019 Orion Poplawski <orion@nwra.com> - 5.6.0-13
- Set QT_QPA_PLATFORM=xcb in desktop file to help with wayland issues (bz#1769060)

* Thu Nov 14 2019 Björn Esser <besser82@fedoraproject.org> - 5.6.0-12
- Rebuild (jsoncpp)

* Tue Sep 24 2019 Than Ngo <than@redhat.com> - 5.6.0-11
- fixed #1751749, drop %%{_target_cpu} which caused different output on different architectures

* Sun Sep 22 2019 Orion Poplawski <orion@nwra.com> - 5.6.0-10
- Rebuild for double-conversion 3.1.5

* Tue Aug 20 2019 Orion Poplawski <orion@nwra.com> - 5.6.0-9
- Add upstream patch to support Python 3.8

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 5.6.0-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 03 2019 Björn Esser <besser82@fedoraproject.org> - 5.6.0-6
- Rebuild (jsoncpp)

* Mon May  6 2019 Orion Poplawski <orion@nwra.com> - 5.6.0-5
- Add upstream patch to allow Open With to work (bugz#1635276)

* Mon Mar 18 2019 Orion Poplawski <orion@nwra.com> - 5.6.0-4
- Rebuild for hdf5 1.10.5, netcdf 4.6.3

* Tue Mar 12 2019 Sandro Mani <manisandro@gmail.com> - 5.6.0-3
- Rebuild (cgnslib)

* Wed Feb 27 2019 Orion Poplawski <orion@nwra.com> - 5.6.0-2
- Build with Python 3

* Fri Feb 15 2019 Orion Poplawski <orion@nwra.com> - 5.6.0-1
- Update to 5.6.0
- Drop old Obsoletes/Provides
- Enable openmpi build for s390x
- Fix appdata install location
- Consolidate license and readmes into -data sub-package
- Move static libraries into -devel and provide -static

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 21 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 5.5.2-20
- Rebuild for protobuf 3.6

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 5.5.2-19
- Add BR:glibc-langpack-en
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Thu Aug 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 5.5.2-18
- Rebuilt for glew 2.1.0

* Sat Aug 18 2018 Orion Poplawski <orion@nwra.com> - 5.5.2-17
- Add upstream patch to fix doc build with cmake 3.12

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Orion Poplawski <orion@nwra.com> - 5.5.2-1
- Update to 5.5.2

* Sun Jun 17 2018 Orion Poplawski <orion@nwra.com> - 5.5.1-1
- Update to 5.5.1
- Add upstream patch for Qt 5.11

* Fri Apr 13 2018 Orion Poplawski <orion@nwra.com> - 5.5.0-1
- Update to 5.5.0

* Wed Mar 07 2018 Antonio Trande <sagitter@fedoraproject.org> - 5.4.1-15
- Add qt5-qtx11extras request

* Thu Feb 22 2018 Antonio Trande <sagitter@fedoraproject.org> - 5.4.1-14
- Fix Python2 scripts

* Tue Feb 20 2018 Antonio Trande <sagitter@fedoraproject.org> - 5.4.1-13
- Enable VisitBridge support (bz#1546474)
- Patched for building VisItBridge plugin

* Mon Feb 19 2018 Antonio Trande <sagitter@fedoraproject.org> - 5.4.1-12
- Rebuild for hdf5-1.8.20
- Remove obsolete scriptlets

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 5.4.1-11
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 14 2018 Björn Esser <besser82@fedoraproject.org> - 5.4.1-9
- Update patch for jsoncpp-1.8.4 with upstreamed version
- Fix warnings when building local srpm

* Sun Jan 14 2018 Björn Esser <besser82@fedoraproject.org> - 5.4.1-8
- Add patch to fix build with jsoncpp-1.8.4

* Tue Dec 26 2017 Björn Esser <besser82@fedoraproject.org> - 5.4.1-7
- Rebuilt for jsoncpp.so.20

* Wed Nov 29 2017 Igor Gnatenko <ignatenko@redhat.com> - 5.4.1-6
- Rebuild for protobuf 3.5

* Mon Nov 13 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 5.4.1-5
- Rebuild for protobuf 3.4

* Fri Sep 01 2017 Björn Esser <besser82@fedoraproject.org> - 5.4.1-4
- Fix 'Bad pre-release versioning scheme'

* Fri Sep 01 2017 Björn Esser <besser82@fedoraproject.org> - 5.4.1-3.3
- Rebuilt for jsoncpp-1.8.3

* Mon Aug 28 2017 Orion Poplawski <orion@cora.nwra.com> - 5.4.1-3.2
- Update to 5.4.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Orion Poplawski <orion@cora.nwra.com> - 5.4.0-3
- Fix protobuf requires filter (bug #1472770)

* Wed Jul 5 2017 Orion Poplawski <orion@cora.nwra.com> - 5.4.0-2
- Update description (bug #1467571)

* Fri Jun 16 2017 Orion Poplawski <orion@cora.nwra.com> - 5.4.0-1
- Update to 5.4.0

* Mon Apr 10 2017 Orion Poplawski <orion@cora.nwra.com> - 5.3.0-2
- Build with Qt5 on Fedora 26+ (bug #1437858)
- Drop old cmake config options

* Mon Mar 13 2017 Orion Poplawski <orion@cora.nwra.com> - 5.3.0-1
- Update to 5.3.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-5.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 26 2017 Orion Poplawski <orion@cora.nwra.com> - 5.2.0-5
- Rebuild with system protobuf 3.2.0

* Tue Jan 10 2017 Orion Poplawski <orion@cora.nwra.com> - 5.2.0-4
- Filter bundled protobuf from requires if needed

* Sun Jan 8 2017 Orion Poplawski <orion@cora.nwra.com> - 5.2.0-3
- Use bundled protobuf for now

* Wed Dec 28 2016 Rich Mattes <richmattes@gmail.com> - 5.2.0-2
- Rebuild for eigen3-3.3.1

* Sat Nov 19 2016 Orion Poplawski <orion@cora.nwra.com> - 5.2.0-1.1
- Rebuild for protobuf 3.1.0

* Thu Nov 17 2016 Orion Poplawski <orion@cora.nwra.com> - 5.2.0-1
- Update to 5.2.0 final

* Mon Nov 7 2016 Orion Poplawski <orion@cora.nwra.com> - 5.2.0-0.8.RC4
- Update to 5.2.0-RC4

* Fri Nov 4 2016 Orion Poplawski <orion@cora.nwra.com> - 5.2.0-0.7.RC3
- Build with bundled gl2ps

* Sat Oct 29 2016 Orion Poplawski <orion@cora.nwra.com> - 5.2.0-0.7.RC3
- Update to 5.2.0-RC3
- Drop libjsoncpp patch applied upstream

* Fri Oct 21 2016 Björn Esser <fedora@besser82.io> - 5.2.0-0.6.RC2
- Add needed (Build)Requires
- Remove cluttering files from %%{_pkgdocdir}

* Wed Oct 19 2016 Björn Esser <fedora@besser82.io> - 5.2.0-0.5.RC2
- Add needed Requires
- Reintroduce doc-subpkg
- Use unified %%{_pkgdocdir} and unified %%license
- Build documentation
- Proper Obsoletes versioning
- Spec-file improvements

* Wed Oct 19 2016 Björn Esser <fedora@besser82.io> - 5.2.0-0.4.RC2
- Drop obsolete stuff
- Use up-to-date macros
- Use semantic build-tree sub-dirs: 's!fedora!%%{_target_platform}!'

* Tue Oct 18 2016 Björn Esser <fedora@besser82.io> - 5.2.0-0.3.RC2
- Update to 5.2.0-RC2
- Drop patches merged by upstream
- Update libjsoncpp_so_11.patch

* Tue Oct 18 2016 Orion Poplawski <orion@cora.nwra.com> - 5.2.0-0.2.RC1
- Drop unneeded data dir
- Update bundled lib cleanup
- Do not use -f with rm to detect changes

* Mon Oct 17 2016 Björn Esser <fedora@besser82.io> - 5.2.0-0.1.RC1
- Update to 5.2.0-RC1
- Drop patches merged by upstream
- Add libjsoncpp_so_11.patch
- Create data-dir, if not created by `%%make_install`
- Drop %%clean-section
- Clean trailing whitespaces

* Mon Oct 03 2016 Björn Esser <fedora@besser82.io> - 5.1.2-2
- Rebuilt for libjsoncpp.so.11

* Fri Sep 16 2016 Orion Poplawski <orion@cora.nwra.com> - 5.1.2-1
- Add upstream fix to not ship libFmmMesh.a
- Use cmake3 and %%cmake3 for EPEL compatibility

* Wed Aug 10 2016 Orion Poplawski <orion@cora.nwra.com> - 5.1.2-1
- Update to 5.1.2
- Use CMAKE_PREFIX_PATH to find mpi versions of libraries
- Ship installed static libraries, they are needed (bug #1304881)

* Wed Jun 29 2016 Orion Poplawski <orion@cora.nwra.com> - 5.1.0-1.1
- Rebuild for hdf5 1.8.17

* Mon Jun 20 2016 Orion Poplawski <orion@cora.nwra.com> - 5.1.0-1
- Update to 5.1.0
- Drop vtk-gcc6 patch fixed upstream
- Note more bundled libraries

* Mon Mar 28 2016 Orion Poplawski <orion@cora.nwra.com> - 5.0.1-1
- Update to 5.0.1 final

* Fri Mar 25 2016 Björn Esser <fedora@besser82.io> - 5.0.1-0.3.RC2
- Update to 5.0.1-RC2
- Drop Patch1 (paraview-lz4), applied upstream
- Use %%license and %%doc properly

* Fri Mar 25 2016 Björn Esser <fedora@besser82.io> - 5.0.1-0.2.RC1
- Rebuilt for libjsoncpp.so.1

* Thu Mar 3 2016 Orion Poplawski <orion@cora.nwra.com> - 5.0.1-0.1.RC1
- Update to 5.0.1-RC1
- Drop paraview-gcc6 patch applied upstream

* Mon Feb 1 2016 Orion Poplawski <orion@cora.nwra.com> - 5.0.0-1
- Update to 5.0.0 final
- Drop non_x86 patch, fixed upstream
- Add vtk-gcc6, paraview-gcc6 patches to support gcc6

* Fri Jan 22 2016 Orion Poplawski <orion@cora.nwra.com> - 5.0.0-0.6.RC3
- Rebuild for netcdf 4.4.0

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 5.0.0-0.5.RC3
- Rebuilt for Boost 1.60

* Thu Jan 7 2016 Orion Poplawski <orion@cora.nwra.com> - 5.0.0-0.4.RC3
- Validate appdata

* Tue Jan 5 2016 Orion Poplawski <orion@cora.nwra.com> - 5.0.0-0.3.RC3
- Update to 5.0.0-RC3
- Add patch to fix build on non-x86 systems
- Add patch to fix jsoncpp usage on ARM

* Fri Dec 18 2015 Orion Poplawski <orion@cora.nwra.com> - 5.0.0-0.2.RC2
- Update to 5.0.0-RC2
- Drop jsoncpp patch applied upstream

* Thu Dec 10 2015 Orion Poplawski <orion@cora.nwra.com> - 5.0.0-0.1.RC1
- Update to 5.0.0-RC1

* Thu Oct 29 2015 Orion Poplawski <orion@cora.nwra.com> - 4.4.0-2
- No longer set MPI_COMPILER as it is no longer needed and breaks with cmake
  3.4.0

* Fri Sep 18 2015 Orion Poplawski <orion@cora.nwra.com> - 4.4.0-1
- Update to 4.4.0
- Drop type, netcdf, and topological-sort-cmake patches applied upstream
- Use system eigen3, python-pygments, python-six (bug #1251289)
- Use bundled jsoncpp for F23 or earlier

* Thu Sep 17 2015 Orion Poplawski <orion@cora.nwra.com> - 4.3.1-15
- Rebuild for openmpi 1.10.0
- Add patch for jsoncpp 0.10 support

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 4.3.1-14
- Rebuilt for Boost 1.59

* Sat Aug 22 2015 Orion Poplawski <orion@cora.nwra.com> - 4.3.1-13
- Note bundled kwsys, remove unused kwsys files

* Wed Aug 19 2015 Orion Poplawski <orion@cora.nwra.com> - 4.3.1-12
- Do not ship static libraries

* Mon Aug 17 2015 Orion Poplawski <orion@cora.nwra.com> - 4.3.1-11
- Filter provides/requires to exclude private libraries

* Fri Aug 14 2015 Orion Poplawski <orion@cora.nwra.com> - 4.3.1-10
- Add patch for protobuf 2.6 support (fixes FTBFS bug #1239759)

* Mon Aug 10 2015 Sandro Mani <manisandro@gmail.com> - 4.3.1-9
- Rebuild for RPM MPI Requires Provides Change

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 4.3.1-7
- rebuild for Boost 1.58

* Fri Jul 10 2015 Jason L Tibbitts III <tibbs@math.uh.edu> - 4.3.1-6
- Add Exec= line to the desktop file (bug #1242012)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 30 2015 Orion Poplawski <orion@cora.nwra.com> - 4.3.1-4
- Use upstream desktop file (bug #1216255)

* Wed Apr 29 2015 Kalev Lember <kalevlember@gmail.com> - 4.3.1-3
- Rebuilt for protobuf soname bump

* Wed Feb 04 2015 Petr Machata <pmachata@redhat.com> - 4.3.1-2
- Bump for rebuild.

* Tue Jan 27 2015 Orion Poplawski <orion@cora.nwra.com> - 4.3.1-1
- Update to 4.3.1

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 4.2.0-3
- Rebuild for boost 1.57.0

* Thu Jan 8 2015 Orion Poplawski <orion@cora.nwra.com> - 4.2.0-2
- Rebuild for hdf 1.8.14
- Add patch to fix compilation error

* Wed Oct 1 2014 Orion Poplawski <orion@cora.nwra.com> - 4.2.0-1
- Update to 4.2.0 final

* Thu Sep 18 2014 Orion Poplawski <orion@cora.nwra.com> - 4.2.0-0.1.rc1
- Update to 4.2.0-RC1
- Drop paraview-install, paraview-4.0.1-Protobuf, and paraview-pqViewFrameActionGroup
  patches fixed upstream
- Build against system pugixml

* Mon Sep 08 2014 Rex Dieter <rdieter@fedoraproject.org> 4.1.0-9
- update scriptlets

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 21 2014 Orion Poplawski <orion@cora.nwra.com> - 4.1.0-7
- Install missing headers (bug #1100911)
- Install TopologicalSort.cmake (bug #1116521)
- Adjust ParaViewPlugins.cmake for Fedora packaging (bug #118520)

* Tue Jun 10 2014 Orion Poplawski <orion@cora.nwra.com> - 4.1.0-6
- Rebuild for hdf 1.8.13

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Orion Poplawski <orion@cora.nwra.com> - 4.1.0-3
- Install missing pqViewFrameActionGroup.h header (bug #1100905)

* Thu May 22 2014 Petr Machata <pmachata@redhat.com> - 4.1.0-3
- Rebuild for boost 1.55.0

* Mon Feb 24 2014 Orion Poplawski <orion@cora.nwra.com> - 4.1.0-2
- Rebuild for mpich-3.1

* Tue Jan 21 2014 Orion Poplawski <orion@cora.nwra.com> - 4.1.0-1
- Update to 4.1.0 final
- Drop cstddef patch applied upstream

* Mon Dec 30 2013 Orion Poplawski <orion@cora.nwra.com> - 4.1.0-0.1.rc2
- Rebase install patch
- Add patch to include needed cstddef for gcc 4.8.2
- Set VTK_INSTALL_DATA_DIR
- Set QtTesting_* install macros

* Fri Dec 27 2013 Orion Poplawski <orion@cora.nwra.com> - 4.1.0-0.1.rc2
- Update to 4.1.0-RC2

* Fri Oct 18 2013 Orion Poplawski <orion@cora.nwra.com> - 4.0.1-3
- Require vtk-devel for vtkProcessShader

* Mon Oct 14 2013 Orion Poplawski <orion@cora.nwra.com> - 4.0.1-2
- Remove conflicts with vtk-devel (bug #1018432)

* Mon Aug 12 2013 Orion Poplawski <orion@cora.nwra.com> - 4.0.1-1
- Update to 4.0.1
- Drop jpeg patch fixed upstream

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.98.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 3.98.1-7
- Rebuild for boost 1.54.0

* Sat Jul 20 2013 Deji Akingunola <dakingun@gmail.com> - 3.98.1-6
- Rename mpich2 sub-packages to mpich and rebuild for mpich-3.0

* Thu May 16 2013 Orion Poplawski <orion@cora.nwra.com> - 3.98.1-5
- Rebuild for hdf5 1.8.11

* Tue Apr 30 2013 Jon Ciesla <limburgher@gmail.com> - 3.98.1-4
- Drop desktop vendor tag.

* Thu Mar 7 2013 Orion Poplawski <orion@cora.nwra.com> - 3.98.1-3
- Remove builddir path from VTKConfig.cmake (bug #917425)

* Sun Feb 24 2013 Orion Poplawski <orion@cora.nwra.com> - 3.98.1-2
- Remove only vtk conflicting binaries (bug #915116)
- Do not move python libraries

* Wed Feb 20 2013 Orion Poplawski <orion@cora.nwra.com> - 3.98.1-1
- Update to 3.98.1
- Drop pvblot patch
- Add upstream patch to fix jpeg_mem_src support

* Mon Jan 28 2013 Orion Poplawski <orion@cora.nwra.com> - 3.98.0-3
- Drop kwProcessXML patch, leave as vtkkwProcessXML with rpath

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 3.98.0-2
- rebuild due to "jpeg8-ABI" feature drop

* Mon Dec 17 2012 Orion Poplawski <orion@cora.nwra.com> - 3.98.0-1
- Update to 3.98.0
- Remove source of more bundled libraries
- Drop include, gcc47, vtkboost, and hdf5 patches
- Rebase kwprocessxml_rpath and system library patches
- Add patch to fix install locations
- Add patch to use system protobuf
- Add BR gl2ps-devel >= 1.3.8
- Disable pvblot for now
- Build with hdf5 1.8.10

* Thu Nov 1 2012 Orion Poplawski <orion@cora.nwra.com> - 3.14.1-5
- Rebuild for mpich2 1.5
- Add patch to compile with current boost

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.14.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Orion Poplawski <orion@cora.nwra.com> - 3.14.1-3
- Don't ship vtkWrapHierarchy, conflicts with vtk (Bug 831834)

* Tue May 15 2012 Orion Poplawski <orion@cora.nwra.com> - 3.14.1-2
- Rebuild with hdf5 1.8.9

* Mon Apr 9 2012 Orion Poplawski <orion@cora.nwra.com> - 3.14.1-1
- Update to 3.14.1
- Add BR hwloc-devel

* Tue Apr 3 2012 Orion Poplawski <orion@cora.nwra.com> - 3.14.0-4
- Add patch to buid kwProcessXML as a forwarded executable (bug #808490)

* Thu Mar 29 2012 Orion Poplawski <orion@cora.nwra.com> - 3.14.0-3
- Only remove vtk conflicting binaries (bug #807756)

* Wed Feb 29 2012 Orion Poplawski <orion@cora.nwra.com> - 3.14.0-2
- Add patch to make vtk use system libraries

* Wed Feb 29 2012 Orion Poplawski <orion@cora.nwra.com> - 3.14.0-1
- Update to 3.14.0
- Rebase gcc47 patch
- Try to handle python install problems manually

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12.0-8
- Rebuilt for c++ ABI breakage

* Thu Jan 26 2012 Orion Poplawski <orion@cora.nwra.com> - 3.12.0-7
- Build with gcc 4.7
- Add patch to support gcc 4.7
- Build with new libOSMesa

* Tue Dec 27 2011 Orion Poplawski <orion@cora.nwra.com> - 3.12.0-6
- vtkPV*Python.so needs to go into the paraview python dir
- Drop chrpath

* Fri Dec 16 2011 Orion Poplawski <orion@cora.nwra.com> - 3.12.0-5
- Oops, install vtk*Python.so, not libvtk*Python.so

* Mon Dec 12 2011 Orion Poplawski <orion@cora.nwra.com> - 3.12.0-4
- Install more libvtk libraries by hand and manually remove rpath

* Fri Dec 9 2011 Orion Poplawski <orion@cora.nwra.com> - 3.12.0-3
- Add patch from Petr Machata to build with boost 1.48.0

* Thu Dec 1 2011 Orion Poplawski <orion@cora.nwra.com> - 3.12.0-2
- Enable PARAVIEW_INSTALL_DEVELOPMENT and re-add -devel sub-package
- Install libvtk*Python.so by hand for now

* Thu Nov 10 2011 Orion Poplawski <orion@cora.nwra.com> - 3.12.0-1
- Update to 3.12.0

* Fri Oct 28 2011 Orion Poplawski <orion@cora.nwra.com> - 3.10.1-6
- Fixup forward paths for mpi versions (bug #748221)

* Thu Jun 23 2011 Orion Poplawski <orion@cora.nwra.com> - 3.10.1-5
- Add BR qtwebkit-devel, fixes FTBS bug 716151

* Tue May 17 2011 Orion Poplawski <orion@cora.nwra.com> - 3.10.1-4
- Rebuild for hdf5 1.8.7

* Tue Apr 19 2011 Orion Poplawski <orion@cora.nwra.com> - 3.10.1-3
- No need to move python install with 3.10.1

* Tue Apr 19 2011 Dan Horák <dan[at]danny.cz> - 3.10.1-2
- no openmpi on s390(x)

* Mon Apr 18 2011 Orion Poplawski <orion@cora.nwra.com> - 3.10.1-1
- Update to 3.10.1
- Drop build patch fixed upstream

* Mon Apr 4 2011 Orion Poplawski <orion@cora.nwra.com> - 3.10.0-1
- Update to 3.10.0
- Drop lib and py27 patches fixed upstream
- Add patch for gcc 4.6.0 support
- Update system hdf5 handling
- Cleanup unused build options
- Build more plugins

* Tue Mar 29 2011 Deji Akingunola <dakingun@gmail.com> - 3.8.1-5
- Rebuild for mpich2 soname bump

* Wed Oct 20 2010 Adam Jackson <ajax@redhat.com> 3.8.1-4
- Rebuild for new libOSMesa soname

* Thu Oct 7 2010 Orion Poplawski <orion@cora.nwra.com> - 3.8.1-3
- Remove any previous %%{_libdir}/paraview/paraview directories
  which prevent updates

* Tue Oct 5 2010 Orion Poplawski <orion@cora.nwra.com> - 3.8.1-2
- Disable install of third party libraries

* Fri Oct 1 2010 Orion Poplawski <orion@cora.nwra.com> - 3.8.1-1
- Update to 3.8.1
- Drop devel sub-package
- Drop installpath patch
- Drop hdf5-1.8 patch, build with hdf5 1.8 API
- Cleanup build

* Fri Jul 30 2010 Orion Poplawski <orion@cora.nwra.com> - 3.8.0-4
- Add patch to support python 2.7

* Tue Jul 27 2010 David Malcolm <dmalcolm@redhat.com> - 3.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Jun 4 2010 Orion Poplawski <orion@cora.nwra.com> - 3.8.0-2
- Drop doc sub-package

* Tue Jun 1 2010 Orion Poplawski <orion@cora.nwra.com> - 3.8.0-1
- Update to 3.8.0
- Update demo patch
- Update hdf5 patch
- Drop old documentation patches
- Add patch to add needed include headers
- Add patch from upstream to fix install path issue

* Sat Mar 13 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.6.2-4
- BR qt-assistant-adp-devel
- Don't Require qt4-assistant, should be qt-assistant-adp now, and it (or qt-x11
  4.6.x which Provides it) gets dragged in anyway by the soname dependencies

* Fri Feb 19 2010 Orion Poplawski <orion@cora.nwra.com> - 3.6.2-3
- More MPI packaging changes

* Tue Feb 16 2010 Orion Poplawski <orion@cora.nwra.com> - 3.6.2-2
- Conform to updated MPI packaging guidelines
- Build mpich2 version

* Mon Jan 4 2010 Orion Poplawski <orion@cora.nwra.com> - 3.6.2-1
- Update to 3.6.2

* Thu Nov 19 2009 Orion Poplawski <orion@cora.nwra.com> - 3.6.1-7
- New location for openmpi (fixes FTBFS bug #539179)

* Mon Aug 31 2009 Orion Poplawski <orion@cora.nwra.com> - 3.6.1-6
- Don't ship lproj, conflicts with vtk

* Thu Aug 27 2009 Orion Poplawski <orion@cora.nwra.com> - 3.6.1-5
- Specify PV_INSTALL_LIB_DIR as relative path, drop install prefix patch
- Update assitant patch to use assistant_adp, don't ship assistant-real

* Wed Aug 26 2009 Orion Poplawski <orion@cora.nwra.com> - 3.6.1-4
- Disable building various plugins that need OverView

* Tue Aug 25 2009 Orion Poplawski <orion@cora.nwra.com> - 3.6.1-3
- Disable building OverView - not ready yet

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 3.6.1-2
- rebuilt with new openssl

* Wed Jul 22 2009 Orion Poplawski <orion@cora.nwra.com> - 3.6.1-1
- Update to 3.6.1

* Thu May 7 2009 Orion Poplawski <orion@cora.nwra.com> - 3.4.0-5
- Update doc patch to look for help file in the right place (bug #499273)

* Tue Feb 24 2009 Orion Poplawski <orion@cora.nwra.com> - 3.4.0-4
- Rebuild with hdf5 1.8.2, gcc 4.4.0
- Update hdf5-1.8 patch to work with hdf5 1.8.2
- Add patch to allow build with Qt 4.5
- Move documentation into noarch sub-package

* Sat Jan 17 2009 Tomas Mraz <tmraz@redhat.com> - 3.4.0-3
- rebuild with new openssl

* Sun Nov 30 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 3.4.0-2
- Rebuild for Python 2.6

* Fri Oct 17 2008 Orion Poplawski <orion@cora.nwra.com> - 3.4.0-1
- Update to 3.4.0 final

* Thu Oct 2 2008 Orion Poplawski <orion@cora.nwra.com> - 3.4.0-0.20081002.1
- Update 3.4.0 CVS snapshot
- Update gcc43 patch
- Drop qt patch, upstream now allows compiling against Qt 4.4.*

* Mon Aug 11 2008 Orion Poplawski <orion@cora.nwra.com> - 3.3.1-0.20080811.1
- Update 3.3.1 CVS snapshot
- Update hdf5 patch to drop upstreamed changes
- Fix mpi build (bug #450598)
- Use rpath instead of ls.so conf files so mpi and non-mpi can be installed at
  the same time
- mpi package now just ships mpi versions of the server components
- Drop useless mpi-devel subpackage
- Update hdf5 patch to fix H5pubconf.h -> H5public.h usage

* Wed May 21 2008 - Orion Poplawski <orion@cora.nwra.com> - 3.3.0-0.20080520.1
- Update to 3.3.0 CVS snapshot
- Update qt and gcc43 patches, drop unneeded patches
- Add openssl-devel, gnuplot, and wget BRs
- Update license text filename
- Set VTK_USE_RPATH to off, needed with development versions
- Run ctest in %%check - still need to exclude more tests

* Wed Mar 5 2008 - Orion Poplawski <orion@cora.nwra.com> - 3.2.1-5
- Rebuild for hdf5 1.8.0 using compatability API define and new patch

* Mon Feb 18 2008 - Orion Poplawski <orion@cora.nwra.com> - 3.2.1-4
- Add patch to compile with gcc 4.3

* Fri Jan 18 2008 - Orion Poplawski <orion@cora.nwra.com> - 3.2.1-3
- Add patch to fix parallel make
- Obsolete demos package (bug #428528)

* Tue Dec 18 2007 - Orion Poplawski <orion@cora.nwra.com> - 3.2.1-2
- Name ld.so.conf.d file with .conf extension
- Drop parallel make for now

* Mon Dec 03 2007 - Orion Poplawski <orion@cora.nwra.com> - 3.2.1-1
- Update to 3.2.1
- Use macros for version numbers
- Add patches to fix documentation install location and use assistant-qt4,
  not install copies of Qt libraries, and not use rpath.
- Install ld.so.conf.d file
- Fixup desktop files

* Thu Aug 23 2007 - Orion Poplawski <orion@cora.nwra.com> - 3.0.2-2
- Update license tag to BSD
- Fix make %%{_smp_mflags}
- Rebuild for ppc32

* Wed Jul 11 2007 - Orion Poplawski <orion@cora.nwra.com> - 3.0.2-1
- Update to 3.0.2
- Turn mpi build back on
- Add devel packages
- Remove demo package no longer in upstream
- Use cmake macros

* Thu Mar 08 2007 - Orion Poplawski <orion@cora.nwra.com> - 2.4.4-6
- Don't build mpi version until upstream fixes the build system

* Fri Dec 22 2006 - Orion Poplawski <orion@cora.nwra.com> - 2.4.4-5
- Fix .so permissions
- Patch for const issue
- Patch for new cmake
- Build with openmpi

* Thu Dec 14 2006 - Jef Spaleta <jspaleta@gmail.com> - 2.4.4-4
- Bump and build for python 2.5

* Fri Oct  6 2006 - Orion Poplawski <orion@cora.nwra.com> - 2.4.4-3
- Install needed python libraries to get around make install bug

* Wed Oct  4 2006 - Orion Poplawski <orion@cora.nwra.com> - 2.4.4-2
- Re-enable OSMESA support for FC6
- Enable python wrapping

* Fri Sep 15 2006 - Orion Poplawski <orion@cora.nwra.com> - 2.4.4-1
- Update to 2.4.4

* Thu Jun 29 2006 - Orion Poplawski <orion@cora.nwra.com> - 2.4.3-8
- No OSMesa support in FC5
- Make data sub-package pull in main package (bug #193837)
- A patch from CVS to fix vtkXOpenRenderWindow.cxx
- Need lam-devel for FC6

* Fri Apr 21 2006 - Orion Poplawski <orion@cora.nwra.com> - 2.4.3-7
- Re-enable ppc

* Mon Apr 17 2006 - Orion Poplawski <orion@cora.nwra.com> - 2.4.3-6
- Exclude ppc due to gcc bug #189160

* Wed Apr 12 2006 - Orion Poplawski <orion@cora.nwra.com> - 2.4.3-5
- Cleanup permissions

* Mon Apr 10 2006 - Orion Poplawski <orion@cora.nwra.com> - 2.4.3-4
- Add icon and cleanup desktop file

* Mon Apr 10 2006 - Orion Poplawski <orion@cora.nwra.com> - 2.4.3-3
- Add VTK_USE_MANGLE_MESA for off screen rendering
- Cleanup source permisions
- Add an initial .desktop file
- Make requirement on -data specific to version
- Don't package Ice-T man pages and cmake files

* Thu Apr  6 2006 - Orion Poplawski <orion@cora.nwra.com> - 2.4.3-2
- Add mpi version

* Tue Apr  4 2006 - Orion Poplawski <orion@cora.nwra.com> - 2.4.3-1
- Initial Fedora Extras version
