# Force out of source build
%undefine __cmake_in_source_build

%global	        prerelease	beta1

Name:		luxcorerender
Version:	2.7
Release:	%autorelease %{?prerelease: -p -e %{prerelease}}
Summary:	LuxCore Renderer, an unbiased rendering system

License:	Apache-2.0
URL:		https://luxcorerender.org/
Source0:	https://github.com/%{name}/LuxCore/archive/%{name}_v%{version}%{?prerelease}.tar.gz
Source1:	https://github.com/%{name}/BlendLuxCore/archive/blendluxcore_v%{version}%{?prerelease}.tar.gz

# Upstream rejected appstream metainfo support
# https://github.com/LuxCoreRender/BlendLuxCore/issues/567
Source3:        org.%{name}.blendluxcore.metainfo.xml

# add python build dependency
Patch0:         LuxCore-boost-python3.patch
# Unbundle
Patch1:         LuxCore-unbundle.patch
# Use C++ Standard 17
# Changed all uses of the boost.bind placeholders to use the boost::placeholders namespace
# https://github.com/LuxCoreRender/LuxCore/issues/449
Patch2:         LuxCore-use-cxx-standard-17.patch
# Use system bcd
Patch3:         LuxCore-system-bcd.patch
# Include atomic header
Patch5:         LuxCore-atomic-header.patch
# Patch for OpenEXR and Imath 3.x
Patch7:         luxcorerender-openexr3.patch
# Path for OpenImageIO 2.3
Patch8:         luxcorerender-oiio-2.3.patch
# Patch for system libs when possible
Patch9:         luxcorerender-system.patch
Patch10:        luxcorerender-system2.patch
# https://github.com/LuxCoreRender/LuxCore/pull/611 (Currently under review)
# Replace boost::filesystem::ofstream with boost::nowide
Patch11:        luxcorerender-pr611-boost_181.patch
# Patch for fmtlib 10
Patch12:        luxcorerender-fmt10.patch

# Upstream only uses 64 bit archtecture
ExclusiveArch:  x86_64

BuildRequires:  bison
BuildRequires:  blender-rpm-macros
BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  dos2unix
BuildRequires:  doxygen
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  bcd-devel
BuildRequires:  boost-devel
BuildRequires:  embree3-devel
BuildRequires:  freeimage-devel
BuildRequires:  json-devel
BuildRequires:  oidn-devel
BuildRequires:  opensubdiv-devel
BuildRequires:  openvdb-devel
BuildRequires:  pkgconfig(blosc)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(glfw3)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libcdio)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  cmake(OpenEXR)
BuildRequires:  cmake(Imath)
BuildRequires:  cmake(OpenColorIO)
BuildRequires:  cmake(OpenImageIO) < 3.0
# Disable pyside2 due to incompatibility with python 3.12
%if 0%{?fedora} < 39
BuildRequires:  pkgconfig(pyside2)
BuildRequires:  pkgconfig(python3)
BuildRequires:	pkgconfig(shiboken2)
%endif
BuildRequires:  pkgconfig(spdlog)
BuildRequires:  pkgconfig(tbb)
BuildRequires:  pkgconfig(yaml-cpp)
BuildRequires:  python3dist(pillow)
%{!?_without_opencl:
BuildRequires:  pkgconfig(OpenCL)
}

Requires:       %{name}-core = %{version}-%{release}
Obsoletes:      LuxRender < 2.0
Provides:       LuxRender = 2.0

%description
LuxCoreRender is a rendering system for physically correct image synthesis.

%package        core
Summary:        Core binaries for %{name}
Obsoletes:      LuxRender-core < 2.0
Provides:       LuxRender-core = 2.0
Obsoletes:      %{name}-libs < 2.3-1
Conflicts:      %{name}-libs < 2.3-1
Obsoletes:      LuxRender-lib < 2.0
Provides:       LuxRender-lib = 2.0

%description    core
The %{name}-core package contains core binaries for using %{name}.

%package        -n blender-%{name}
Summary:        Blender export plugin to %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
#Requires:       blender(ABI)%%{?blender_api: = %%{blender_api}}
Obsoletes:      LuxRender-blender < 2.0
Provides:       LuxRender-blender = 2.0

%description    -n blender-%{name}
The blender-%{name} package contains the plugin for Blender
to export into %{name}

%package        devel
Summary:        Development files for %{name}
Provides:       LuxRender-devel = %{version}-%{release}
Obsoletes:      LuxRender-devel < 2.0

%description        devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        examples
Summary:        Example of application using %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    examples
The %{name}-examples package contains sample binaries using %{name}.

%if 0%{?fedora} < 39
%package        -n python3-%{name}
Summary:        Python 3 interface to %{name}
Requires:       blender-%{name}%{?_isa} = %{version}-%{release}
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
The python3-%{name} contains Python 3 API for the library.
%endif

%package static
Summary:	luxcorerender static libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libraries for the LuxCore render.

%prep
%autosetup -p1 -a1 -n LuxCore-%{name}_v%{version}%{?prerelease}

# Fix bundled deps
rm -rf pywheel pyunittests
rm -rf samples/luxcoreui/deps/glfw-*
rm -rf deps/{bcd-*,expat-*,eigen-*,json-*,opencolorio-*,opensubdiv-*,spdlog-*,openvdb-*,yaml-cpp-*}
# keep imgui-1.46 nfd bundled for now

# Switch to WIP system bcd
sed -i -e 's/bcd/bcdio bcdcore/' CMakeLists.txt tests/luxcoreimplserializationdemo/CMakeLists.txt src/luxcore/CMakeLists.txt

# Link to system version
sed -i -e 's/opencolorio/OpenColorIO/' CMakeLists.txt src/luxcore/CMakeLists.txt tests/luxcoreimplserializationdemo/CMakeLists.txt
sed -i -e 's/OpenColorIO/OpenColorIO spdlog fmt/' CMakeLists.txt tests/luxcoreimplserializationdemo/CMakeLists.txt
sed -i -e 's/opensubdiv/osdCPU/' CMakeLists.txt src/luxcore/CMakeLists.txt tests/luxcoreimplserializationdemo/CMakeLists.txt

# Explicitly avoid using static boost library: seems needed on boost 1.78
%if 0%{?fedora} >= 37
sed -i -e '\@set.*Boost_USE_STATIC_LIBS@s|ON|OFF|' cmake/Dependencies.cmake
%endif

# Fix all Python shebangs recursively in .
%py3_shebang_fix .

%build
#Building lux
%cmake \
	-DBUILD_SHARED_LIBS=ON \
	-DBOOST_SEARCH_PATH=%{_libdir} \
	-DCMAKE_C_FLAGS="%{optflags} -Wl,--as-needed" \
	-DCMAKE_CXX_FLAGS="%{optflags} -Wl,--as-needed -DSPDLOG_FMT_EXTERNAL" \
	-DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE \
	-DOpenGL_GL_PREFERENCE=GLVND \
	-DPYTHON_V=%{python3_version_nodots} \
	-DEMBREE_INCLUDE_PATH=%{_includedir}/libembree3 \
        -DEMBREE_LIBRARY=%{_libdir}/libembree3.so \
	-DOIDN_INCLUDE_PATH=%{_includedir}/OpenImageDenoise
%cmake_build

%install
pushd %{_vpath_builddir}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}
        
install -Dpm 0755 bin/* %{buildroot}%{_bindir}/
install -Dpm 0755 lib/*.{a,so*} %{buildroot}%{_libdir}/
        
# Remove rpaths
chrpath --delete %{buildroot}%{_bindir}/*
chrpath --delete %{buildroot}%{_libdir}/*.so*
        
# Install include files
cp -pr generated/include/{luxcore,luxrays} %{buildroot}%{_includedir} #cfg.h
popd
cp -pr include/{luxcore,luxrays} %{buildroot}%{_includedir}/
rm %{buildroot}%{_includedir}/{luxcore,luxrays}/cfg.h.in
        
# Relocate pyluxcore
mkdir -p %{buildroot}%{python3_sitearch}
mv %{buildroot}%{_libdir}/pyluxcore.so %{buildroot}%{python3_sitearch}

# Import add-ons and preset
mkdir -p %{buildroot}%{blender_extensions}/%{name}
cp -a BlendLuxCore-blendluxcore_v%{version}%{?prerelease}/* \
  %{buildroot}%{blender_extensions}/%{name}

# change the search path in exporter so it finds pylux in its new location
# borrowed from Arch Linux
for file in `grep -rl import\ pyluxcore ${pkgdir}` ; 
        do sed -i 's/from .* import pyluxcore/import pyluxcore/g' $file;
done
rm -fr %{buildroot}%{blender_extensions}/%{name}/.gitignore

# Metainfo for blender addon
# Upstream rejected the appdata
install -p -m 644 -D %{SOURCE3} %{buildroot}%{_metainfodir}/org.%{name}.blendluxcore.metainfo.xml

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.%{name}.blendluxcore.metainfo.xml

%files
%license COPYING.txt
%doc AUTHORS.txt

%files core
%{_bindir}/{luxcoreconsole,luxcoredemo,luxcoreimplserializationdemo,luxcorescenedemo,luxcoreui}

# GPLv3
%files -n blender-%{name}
%doc README.md
%{_metainfodir}/org.%{name}.blendluxcore.metainfo.xml
%{blender_extensions}/%{name}

%if 0%{?fedora} < 39
%files -n python3-%{name}
%license COPYING.txt
%{python3_sitearch}/pyluxcore.so
%endif

%files devel
%{_includedir}/{luxcore,luxrays,slg}
%exclude %{python3_sitearch}/pyluxcore.so
%files static
%{_libdir}/lib{luxcore,luxrays,slg-core,slg-film,slg-kernels}.a

%changelog
%autochangelog
