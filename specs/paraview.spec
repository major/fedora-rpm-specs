#LTO fails at the moment
%undefine _lto_cflags

%if 0%{?fedora}
%define _legacy_common_support 1
%endif

%global pv_maj 5
%global pv_min 12
%global pv_patch 1
%global pv_majmin %{pv_maj}.%{pv_min}
#global rcsuf RC3
%{?rcsuf:%global relsuf .%{rcsuf}}
%{?rcsuf:%global versuf -%{rcsuf}}

# No MPI (yet) in flatpaks
%if 0%{?flatpak}
%bcond_with mpich
%bcond_with openmpi
%else
%bcond_without mpich
# No openmpi on i668 with openmpi 5 in Fedora 40+
%if 0%{?fedora} >= 40
%ifarch %{ix86}
%bcond_with openmpi
%else
%bcond_without openmpi
%endif
%else
%bcond_without openmpi
%endif
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

# Enable VisitBridge plugin (bz#1546474)
%bcond_without VisitBridge

# We need jsoncpp >= 0.7
%global system_jsoncpp 1
%global vtk_use_system_jsoncpp -DVTK_MODULE_USE_EXTERNAL_VTK_jsoncpp:BOOL=ON

%bcond_without protobuf
%if %{with protobuf}
%global vtk_use_system_protobuf -DVTK_MODULE_USE_EXTERNAL_ParaView_protobuf:BOOL=ON
%else
%global vtk_use_system_protobuf -DVTK_MODULE_USE_EXTERNAL_ParaView_protobuf:BOOL=OFF
%endif

# We need pugixml >= 1.9
%global system_pugixml 1
%global vtk_use_system_pugixml -DVTK_MODULE_USE_EXTERNAL_VTK_pugixml:BOOL=ON

# Not packaged?
%bcond_with token
%if %{with token}
%global vtk_use_system_token -DVTK_MODULE_USE_EXTERNAL_VTK_token:BOOL=ON
%else
%global vtk_use_system_token -DVTK_MODULE_USE_EXTERNAL_VTK_token:BOOL=OFF
%endif

Name:           paraview
Version:        %{pv_maj}.%{pv_min}.%{pv_patch}
Release:        %autorelease
Summary:        Parallel visualization application

License:        BSD-3-Clause
URL:            https://www.paraview.org/
Source0:        https://www.paraview.org/files/v%{pv_majmin}/ParaView-v%{version}%{?versuf}.tar.gz
Source1:        paraview.xml
Source2:        FindPEGTL.cmake
# Fix cmake files install location
# https://gitlab.kitware.com/paraview/paraview/issues/19724
Patch0:         paraview-cmakedir.patch
# Fix doc build with Sphinx 6
Patch1:         paraview-sphinx6.patch
# Fix build with gcc 15
# https://gitlab.kitware.com/vtk/vtk-m/-/merge_requests/3271
# https://gitlab.kitware.com/vtk/vtk-m/-/merge_requests/3272
# FTBFS https://bugzilla.redhat.com/show_bug.cgi?id=2341002
Patch2:         paraview-gcc15.patch
# Fix build with newer freetype
# https://gitlab.kitware.com/vtk/vtk/-/issues/18033
Patch3:         paraview-freetype.patch

BuildRequires:  cmake >= 3.12
BuildRequires:  make
BuildRequires:  lz4-devel
BuildRequires:  cmake(Qt5)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5UiPlugin)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  qt5-qtwebkit-devel
BuildRequires:  /usr/bin/xmlpatterns-qt5
BuildRequires:  mesa-libOSMesa-devel
BuildRequires:  python3-devel
BuildRequires:  python3-netcdf4
BuildRequires:  python3-qt5
# Fails looking for PythonQt_QtBindings.h
# https://gitlab.kitware.com/paraview/paraview/issues/17365
#BuildRequires:  pythonqt-devel
%if %{with cgnslib}
BuildRequires:  cgnslib-devel
%endif
BuildRequires:  cli11-devel
BuildRequires:  gdal-devel
BuildRequires:  hdf5-devel
BuildRequires:  tk-devel
BuildRequires:  fast_float-devel
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
BuildRequires:  libappstream-glib
BuildRequires:  glibc-langpack-en

Requires: hdf5%{?_hdf5_version: = %{_hdf5_version}}
Requires: %{name}-data = %{version}-%{release}
Requires: python3-pygments
Requires: python3-six
Requires: python3-netcdf4
Requires: python3-numpy
Requires: python3-twisted
Requires: python3-autobahn
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
%global __requires_exclude ^lib(catalyst|LegacyGhostCellsGenerator|IceT|pq|QtTesting|StereoCursorViews|vtk).*$
%else
%global __requires_exclude ^lib(catalyst|LegacyGhostCellsGenerator|IceT|pq|QtTesting|StereoCursorViews|vtk|protobuf).*$
%endif

ExcludeArch: %{ix86}

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
        -DVTK_PYTHON_VERSION=3 \\\
        -DPARAVIEW_BUILD_WITH_EXTERNAL:BOOL=ON \\\
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
        %{?vtk_use_system_token} \\\
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
        -DPYTHON_INSTALL_DIR=PATH=$MPI_PYTHON3_SITEARCH \\\
        -DQtTesting_INSTALL_LIB_DIR=lib/%{name} \\\
        -DQtTesting_INSTALL_CMAKE_DIR=lib/%{name}/CMake \\\
        -DPARAVIEW_USE_MPI:BOOL=ON \\\
        -DICET_BUILD_TESTING:BOOL=ON \\\
%if %{with VisitBridge} \
        -DPARAVIEW_USE_VISITBRIDGE=ON \\\
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
%if %{with openmpi}
Install the paraview-openmpi package to get a version compiled with openmpi.
%endif
%if %{with mpich}
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

BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-sphinx
BuildRequires:  python3-twisted
BuildRequires:  python3-autobahn
BuildRequires:  python3-markupsafe

BuildArch:      noarch

%description    doc
%{summary}.

%global mpi_list %{nil}

%if %{with openmpi}
%global mpi_list %mpi_list openmpi
%package        openmpi
Summary:        Parallel visualization application

BuildRequires:  openmpi-devel
BuildRequires:  netcdf-openmpi-devel
BuildRequires:  python3-mpi4py-openmpi

Requires:       %{name}-data = %{version}-%{release}
Requires:       python3-autobahn
Requires:       python3-mpi4py-openmpi
Requires:       python3-numpy
Requires:       python3-pygments
Requires:       python3-six
Requires:       python3-twisted
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


%if %{with mpich}
%global mpi_list %mpi_list mpich
%package        mpich
Summary:        Parallel visualization application

BuildRequires:  mpich-devel
BuildRequires:  netcdf-mpich-devel
BuildRequires:  python3-mpi4py-mpich

Requires:       %{name}-data = %{version}-%{release}
Requires:       python3-autobahn
Requires:       python3-mpi4py-mpich
Requires:       python3-numpy
Requires:       python3-pygments
Requires:       python3-six
Requires:       python3-twisted
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
for x in vtk{cli11,doubleconversion,eigen,expat,fast_float,%{?with_fmt:fmt,}freetype,%{?_with_gl2ps:gl2ps,}glew,hdf5,jpeg,libproj,libxml2,lz4,lzma,mpi4py,netcdf,nlohmannjson,ogg,pegtl,png,sqlite,theora,tiff,utf8,zfp,zlib}
do
  rm -r VTK/ThirdParty/*/${x}
done
# Remove version requirements
sed -i -e '/VERSION *"/d' VTK/ThirdParty/fast_float/CMakeLists.txt
# jsoncpp
%if 0%{system_jsoncpp}
rm -r VTK/ThirdParty/jsoncpp/vtkjsoncpp
%endif
# Remove unused KWSys items
find VTK/Utilities/KWSys/vtksys/ -name \*.[ch]\* | grep -vE '^VTK/Utilities/KWSys/vtksys/([a-z].*|Configure|SharedForward|Status|String\.hxx|Base64|CommandLineArguments|Directory|DynamicLoader|Encoding|FStream|FundamentalType|Glob|MD5|Process|RegularExpression|System|SystemInformation|SystemTools)(C|CXX|UNIX)?\.' | xargs rm
cp %SOURCE2 VTK/CMake/FindPEGTL.cmake
# We want to build with a system vtk someday, but it doesn't work yet
#rm -r VTK

# $mpi will be evaluated in the loops below
%global _vpath_builddir %{_vendor}-%{_target_os}-build-${mpi:-serial}


%conf
# Try to limit memory consumption on some arches
%ifarch %{arm}
%global optflags %(echo %{optflags} | sed 's/-g /-g1 /')
%endif
%cmake -Wno-dev \
        -DCMAKE_INSTALL_CMAKEDIR:PATH=%{_lib}/cmake \
        -DCMAKE_INSTALL_LIBDIR:PATH=%{_lib}/%{name} \
        -DPARAVIEW_BUILD_DEVELOPER_DOCUMENTATION:BOOL=ON \
        -DQtTesting_INSTALL_LIB_DIR=%{_lib}/%{name} \
        -DQtTesting_INSTALL_CMAKE_DIR=%{_lib}/%{name}/CMake \
        %{paraview_cmake_options}

for mpi in %{mpi_list}
do
  module load mpi/$mpi-%{_arch}
  %cmake -Wno-dev %{paraview_cmake_mpi_options}
  module purge
done


%build
%cmake_build -t ParaViewDoxygenDoc ParaViewPythonDoc
%cmake_build
export LANG=en_US.UTF-8
# Built-in Python modules were not found, set pythonpath as workaround
export PYTHONPATH=$PWD/%{_lib}/paraview/python%{python3_version}/site-packages:%{python3_sitelib}:%{python3_sitearch}

for mpi in %{mpi_list}
do
  module load mpi/$mpi-%{_arch}
  %cmake_build
  module purge
done


%install
# Fix permissions
find . \( -name \*.txt -o -name \*.xml -o -name '*.[ch]' -o -name '*.[ch][px][px]' \) -print0 | xargs -0 chmod -x

# Create some needed directories
install -d %{buildroot}%{_datadir}/applications
install -d %{buildroot}%{_datadir}/mime/packages
install -m644 %SOURCE1 %{buildroot}%{_datadir}/mime/packages

for mpi in %{mpi_list}
do
  module load mpi/$mpi-%{_arch}
  %cmake_install

  # Remove mpi copy of doc and man pages and  data
  rm -rf %{buildroot}%{_libdir}/${mpi}/share/{metainfo,applications,doc,icons,man,mimeinfo,paraview,vtkm-*}

  # Set rpaths of every library
  for i in `find %{buildroot}$MPI_LIB -name "*.so*" -type f -print`; do
      patchelf --print-rpath --set-rpath $MPI_LIB $i
  done
  module purge
done
# unset mpi to reset _vpath_builddir
unset mpi

#Install the normal version
%cmake_install

desktop-file-validate %{buildroot}%{_datadir}/applications/org.paraview.ParaView.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/org.paraview.ParaView.appdata.xml

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


%pre
#Handle changing from directory to file
if [ -d %{_libdir}/paraview/paraview ]; then
  rm -r %{_libdir}/paraview/paraview
fi


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
%license Copyright.txt
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

%if %{with openmpi}
%files openmpi
%{_libdir}/openmpi/bin/[ps]*
%{_libdir}/openmpi/lib/%{name}/
%exclude %{_libdir}/openmpi/lib/%{name}/*.a
%license %{_libdir}/openmpi/share/licenses/

%files openmpi-devel
%{_includedir}/openmpi-%{_arch}/%{name}/
%{_libdir}/openmpi/bin/vtk*
%{_libdir}/openmpi/lib/cmake/
%{_libdir}/openmpi/lib/%{name}/*.a
%endif


%if %{with mpich}
%files mpich
%{_libdir}/mpich/bin/[ps]*
%{_libdir}/mpich/lib/%{name}/
%exclude %{_libdir}/mpich/lib/%{name}/*.a
%license %{_libdir}/mpich/share/licenses/

%files mpich-devel
%{_includedir}/mpich-%{_arch}/%{name}/
%{_libdir}/mpich/bin/vtk*
%{_libdir}/mpich/lib/cmake/
%{_libdir}/mpich/lib/%{name}/*.a
%endif


%changelog
%autochangelog
