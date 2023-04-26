%global blender_api 3.5
%global macrosdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)

%bcond_with     clang
%bcond_without  draco
# Needed to enable osl support for cycles rendering
%bcond_without  llvm
%bcond_without  openshading
%bcond_with     sdl
%bcond_without  system_eigen3
%bcond_without  wayland

%ifarch x86_64 aarch64 ppc64le
%global cyclesflag ON
# Only available on x86_64 and aarch64
%ifarch x86_64 aarch64
%bcond_without  embree
%bcond_without  hidapi
%ifarch x86_64
%bcond_without  oidn
%bcond_without  opgl
%endif
%bcond_without  usd
%else
%bcond_with     embree
%bcond_with     hidapi
%bcond_with     oidn
%bcond_with     opgl
%bcond_with     usd
%endif
%else
%global cyclesflag OFF
%endif

Name:           blender
Epoch:          1
Version:        3.5.0
Release:        %autorelease


Summary:        3D modeling, animation, rendering and post-production
License:        GPL-2.0-or-later
URL:            https://www.blender.org

Source0:        https://download.%{name}.org/source/%{name}-%{version}.tar.xz
# Upstream separated addons from the main source
Source1:        https://projects.%{name}.org/%{name}/%{name}-addons/archive/v%{version}.tar.gz#/%{name}-addons-%{version}.tar.gz
Source3:        macros.%{name}-rpm

# https://projects.blender.org/blender/blender/pulls/106575
Patch:		106575.patch

# Development stuff
BuildRequires:  boost-devel
BuildRequires:  ccache
%if %{with clang}
BuildRequires:  clang
%endif
%if %{with llvm}
BuildRequires:  llvm-devel
%endif
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  git-core
BuildRequires:  libharu-devel
BuildRequires:  libtool
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(blosc)
%if %{with system_eigen3}
BuildRequires:  pkgconfig(eigen3)
%endif
BuildRequires:  pkgconfig(epoxy) >= 1.5.10
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(gmp)
%if %{with hidapi}
BuildRequires:  pkgconfig(hidapi-hidraw)
%endif
BuildRequires:  pkgconfig(jemalloc)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(pugixml)
BuildRequires:  pkgconfig(python3) >= 3.7
%if %{with wayland}
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:	pkgconfig(libdecor-0) >= 0.1.0
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xkbcommon)
%endif
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(idna)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(zstandard)
BuildRequires:  subversion-devel

# Compression stuff
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(lzo2)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libzstd)

# 3D modeling stuff
BuildRequires:  cmake(ceres)
# Switch to embree3 for compatibility reason
%if %{with embree}
BuildRequires:  embree3-devel
%endif
BuildRequires:  opensubdiv-devel >= 3.4.4
%if %{with openshading}
# Use oslc compiler
BuildRequires:  openshadinglanguage-common-headers >= 1.12.6.2
BuildRequires:  pkgconfig(oslcomp)
%endif
%if %{with oidn}
BuildRequires:  cmake(OpenImageDenoise)
%endif
%if %{with opgl}
BuildRequires:  openpgl-devel
%endif
BuildRequires:  openCOLLADA-devel >= svn825
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(ftgl)
BuildRequires:  pkgconfig(glut)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  openxr-libs
BuildRequires:  pkgconfig(openxr)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(ode)
BuildRequires:  pkgconfig(sdl2)
%if %{with usd}
BuildRequires:  usd-devel
%endif
BuildRequires:  pkgconfig(xproto)

# Picture/Video stuff
BuildRequires:  cmake(Alembic)
BuildRequires:  ffmpeg-free-devel >= 5.1.2
BuildRequires:  lame-devel
BuildRequires:  libspnav-devel
BuildRequires:  openvdb-devel
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:	pkgconfig(libavformat)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(theora)
BuildRequires:  pkgconfig(vpx)
# OpenColorIO 2 and up required
BuildRequires:  pkgconfig(OpenColorIO) > 1
BuildRequires:  cmake(Imath)
BuildRequires:  cmake(OpenEXR)
BuildRequires:  pkgconfig(OpenImageIO)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(tbb)
BuildRequires:  potrace-devel

# Audio stuff
BuildRequires:  pkgconfig(ao)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(freealut)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(vorbis)

# Typography stuff
BuildRequires:  fontpackages-devel
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(tinyxml)
# Appstream stuff
BuildRequires:  libappstream-glib

Requires:       google-droid-sans-fonts
Requires:       hicolor-icon-theme
Requires:       shared-mime-info
Provides:       blender(ABI) = %{blender_api}

# Obsolete the standalone Blender player retired by upstream
Obsoletes:      blenderplayer < 1:2.80-1
Provides:       blenderplayer = 1:2.80-1

# Obsoletes separate Blender Fonts - rhbz#1889049
Obsoletes:      blender-fonts <  1:2.91.0-5

# Starting from 2.90, Blender support only 64-bits architectures
ExcludeArch:	%{ix86} %{arm}

%description
Blender is the essential software solution you need for 3D, from modeling,
animation, rendering and post-production to interactive creation and playback.

Professionals and novices can easily and inexpensively publish stand-alone,
secure, multi-platform content to the web, CD-ROMs, and other media.

%package rpm-macros
Summary:        RPM macros to build third-party blender addons packages
BuildArch:      noarch

%description rpm-macros
This package provides rpm macros to support the creation of third-party addon
packages to extend Blender.

%prep
%autosetup -p1 -a1

# integrate addons in source tree
mkdir scripts/addons
for d in addons; do
    mv %{name}-$d/* scripts/addons
    # wipe .gitea and .github
    rm -r %{name}-$d
done

# Delete the bundled FindOpenJPEG to make find_package use the system version
# instead (the local version hardcodes the openjpeg version so it is not update
# proof)
rm -f build_files/cmake/Modules/FindOpenJPEG.cmake

# Fix all Python shebangs recursively in .
%py3_shebang_fix .

# Work around CMake boost module needing the python version to find the library
sed -i "s/date_time/date_time python%{python3_version_nodots}/" \
    build_files/cmake/platform/platform_unix.cmake



%build
%cmake \
    -G Ninja \
    -D_ffmpeg_INCLUDE_DIR=%{_includedir}/ffmpeg \
%if %{with openshading}
    -D_osl_LIBRARIES=%{_libdir} \
    -DOSL_INCLUDE_DIR=%{_includedir} \
    -DOSL_COMPILER=%{_bindir}/oslc \
%endif
    -DBOOST_ROOT=%{_prefix} \
    -DBUILD_SHARED_LIBS=OFF \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_C_FLAGS="%{optflags} -Wl,--as-needed" \
    -DCMAKE_CXX_FLAGS="%{optflags} -Wl,--as-needed" \
    -DCMAKE_CXX_STANDARD=17 \
    -DCMAKE_SKIP_RPATH=ON \
%if %{with clang}
    -D_CLANG_LIBRARIES=%{_libdir}/libclang-cpp.so \
%endif
    -DEMBREE_INCLUDE_DIR=%{_includedir}/embree3 \
    -DEMBREE_LIBRARY=%{_libdir}/libembree3.so.3 \
    -DPYTHON_VERSION=%{python3_version} \
    -DWITH_COMPILER_CCACHE=ON \
    -DWITH_CYCLES=%{cyclesflag} \
    -DWITH_CYCLES_HIP_BINARIES=ON \
%ifnarch x86_64
    -DWITH_CYCLES_EMBREE=OFF \
%endif
    -DWITH_DOC_MANPAGE=ON \
%if %{with draco}
    -DWITH_DRACO=ON \
%endif
%if %{with wayland}
    -DWITH_GHOST_WAYLAND_DBUS=ON \
%endif
    -DWITH_INSTALL_PORTABLE=OFF \
    -DWITH_PYTHON_INSTALL=OFF \
    -DWITH_PYTHON_INSTALL_NUMPY=OFF \
    -DWITH_PYTHON_INSTALL_REQUESTS=OFF \
%if %{with sdl}
    -DWITH_GHOST_SDL=ON \
%endif
%if %{with system_eigen3}
    -DWITH_SYSTEM_EIGEN3=ON \
%endif
%if %{without usd}
    -DUSD_LIBRARY=%{_libdir}/libusd_usd_ms.so \
%else
    -DWITH_USD=OFF \
%endif
    -DXR_OPENXR_SDK_LOADER_LIBRARY=%{_libdir}/libopenxr_loader.so.1 \
    -DWITH_LIBS_PRECOMPILED=OFF

%cmake_build

%install
%cmake_install

# Deal with docs in the files section
rm -rf %{buildroot}%{_docdir}/%{name}/*

# rpm macros
mkdir -p %{buildroot}%{macrosdir}
sed -e 's/@VERSION@/%{blender_api}/g' %{SOURCE1} > %{buildroot}%{macrosdir}/macros.%{name}-rpm

# AppData
install -p -m 644 -D release/freedesktop/org.%{name}.Blender.appdata.xml \
          %{buildroot}%{_metainfodir}/org.%{name}.Blender.appdata.xml

# Localization
%find_lang %{name}

# rpmlint fixes
find %{buildroot}%{_datadir}/%{name}/%{blender_api}/scripts -name "*.py" -exec chmod 755 {} \;


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.%{name}.Blender.appdata.xml

%files -f %{name}.lang
%license COPYING
%license doc/license/*-license.txt
%license release/text/copyright.txt
%doc release/text/readme.html
%{_bindir}/%{name}
%{_bindir}/%{name}-thumbnailer
%{_datadir}/applications/%{name}.desktop
%exclude %{_datadir}/%{name}/%{blender_api}/datafiles/locale/
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/%{name}*.*
%{_mandir}/man1/%{name}.*
%{_metainfodir}/org.%{name}.Blender.appdata.xml

%files rpm-macros
%{macrosdir}/macros.%{name}-rpm

%changelog
%autochangelog
