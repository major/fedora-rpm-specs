%global blender_api 4.3
%global macrosdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)

%bcond clang	0
%bcond draco	1
# Needed to enable osl support for cycles rendering
%bcond llvm	1
%bcond manpage  1
%bcond materialx 0
%bcond ninja	1
%bcond openshading	1
%bcond openvdb  1
%bcond sdl	0
%bcond system_eigen3	1
%bcond vulkan 1

%ifarch x86_64 aarch64 ppc64le
%global cyclesflag ON
# Only available on x86_64 and aarch64
%ifarch x86_64 aarch64
%bcond embree	1
%bcond hidapi	1
%ifarch x86_64
%bcond hip	1
%bcond oidn	1
%bcond oneapi   0
%bcond opgl	1
%global llvm_compat 18
%endif
%bcond usd	1
%else
%bcond embree	0
%bcond hidapi	0
%bcond oidn	0
%bcond opgl	0
%bcond usd	0
%endif
%else
%global cyclesflag OFF
%endif

Name:           blender
Epoch:          1
Version:        4.3.2
Release:        %autorelease


Summary:        3D modeling, animation, rendering and post-production
License:        GPL-2.0-or-later
URL:            https://www.blender.org

Source0:        https://download.%{name}.org/source/%{name}-%{version}.tar.xz

# Rename macros extension to avoid clashing with upstream version
Source1:        %{name}-macros-source
# FFmpeg 7 compatibility for audaspace plugin
# https://projects.blender.org/blender/blender/pulls/121960.patch
Patch1:         121960.patch
# Fix crash on creating fluid domain with python 3.12 and up #130160
# https://projects.blender.org/blender/blender/pulls/130160.patch
Patch3:         130160.patch
# Upstream patches cherry-picked from main branch
Patch4:         PyAPI-support-Python-3.13.patch
Patch5:         Fix-Remove-internal-ffmpeg-API-usage-fix-ffmpeg-7-co.patch

# Development stuff
BuildRequires:  boost-devel
BuildRequires:  ccache
%if %{with clang}
BuildRequires:  clang%{?llvm_compat}-devel
%endif
%if %{with llvm}
BuildRequires:  llvm%{?llvm_compat}-devel
%endif
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  git-core
BuildRequires:  libharu-devel
BuildRequires:  libtool
%if %{with ninja}
BuildRequires:  ninja-build
%endif
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
%if %{with vulkan}
BuildRequires:  pkgconfig(shaderc)
BuildRequires:  pkgconfig(vulkan)
%endif
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:	pkgconfig(libdecor-0) >= 0.1.0
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  subversion-devel

# Python stuff
BuildRequires:  python3dist(setuptools)
# In build_files/utils/make_bpy_wheel.py, the call to setuptools.setup has
# install_requires=["cython", "numpy", "requests", "zstandard"]; these are
# therefore both build-time and runtime dependencies.
BuildRequires:  python3dist(cython)
Requires:       python3dist(cython)
BuildRequires:  python3dist(numpy)
Requires:       python3dist(numpy)
BuildRequires:  python3dist(requests)
Requires:       python3dist(requests)
BuildRequires:  python3dist(zstandard)
Requires:       python3dist(zstandard)
# In source/creator/CMakeLists.txt, an attempt is made to add direct
# dependencies on certifi, (chardet or charset_normalizer), idna, and urllib3,
# as indirect dependencies that enable necessary functionality in requests. As
# packaged, requests already has a hard dependency on charset_normalizer, idna,
# and urllib3 – and it would depend on certifi, but this is correctly patched
# out in favor of explicitly and unconditional using the system certificate
# bundle. We therefore do not need to add direct dependencies on any of the
# above.
#
# Many Python scripts that are installed, especially from the add-ons, depend
# on various external Python packages. As far as we know, there is no clear
# listing of these that we can use as a reference to generate depdendencies
# automatically. A listing appears in PYTHON_SUBPACKAGES in
# build_files/build_environment/install_linux_packages.py, but the entries are
# redundant with those appearing above.
#
# Some dependencies can be found easily because they are required for testing;
# others may be less obvious. In general, each should be both a BuildRequires
# (even if not used in testing, to avoid accidentally building a Blender
# package that builds from source but fails to install due to an unsatisfied
# Requires) and a Requires (so users are not faced with “No module named '...'”
# errors).
#
# Something like this can help search for possible dependencies:
#
# rpm2cpio blender-4.1.1-1.fc40.x86_64.rpm | pax -r
# p='^[[:blank:]]*(from[[:blank:]]+[^[:blank:]]+[[:blank:]]+)?import\b'
# rg -I -g '*.py' "${p}" ./usr | awk '{print $2}' | grep -vE '^\.' | sort -u |
#   tee imports.txt
#
# This is an imperfect heuristic, but the result is generally a list of
# absolute imports that might reflect external dependencies. Some come from
# Blender; many come from the Python standard library. Those that remain are
# candidates for this list.
#
# The ant_landscape add-on has a weak dependency (used only if available) on
# numexpr; so does the mesh_tissue add-on.
BuildRequires:  python3dist(numexpr)
Recommends:     python3dist(numexpr)
# The ant_landscape add-on has a weak dependency on psutil.
BuildRequires:  python3dist(psutil)
Recommends:     python3dist(psutil)
#
# The mesh_tissue add-on has a weak dependency on numba. Numba is not packaged
# for Fedora, and probably never will be, because it is tied closely to the
# implementation details of a particular Python interpreter version, and can
# take six months to a year to support a new Python release.
# BuildRequires:  python3dist(numba)
# Recommends:     python3dist(numba)
# Only if numba is not available (see above), the mesh_tissue add-on falls back
# to using ensurepip to install pip, and then using pip to try to install numba
# from PyPI into the user site-packages. This *might* work. It is probably
# better if pip is already available.
BuildRequires:  python3dist(pip)
Recommends:     python3dist(pip)
#
# The io_mesh_uv_layout add-on has a weak dependency on OpenImageIO. Currently,
# the OpenImageIO package does not produce the necessary Python metadata for a
# dependency on python3dist(openimageio) to work.
BuildRequires:  python3-openimageio
Recommends:     python3-openimageio
#
# The io_export_dxf add-on requires pydevd (PyDev.Debugger,
# https://pypi.org/project/pydevd/) for debugging when the BLENDER_DEBUG
# environment variable is set. Since this is a debug-only dependency, we would
# choose not to add it even if it were packaged.
#
# The io_import_dxf add-on has a weak dependency on pyproj.
BuildRequires:  python3dist(pyproj)
Recommends:     python3dist(pyproj)
#
# %%{_datadir}/blender/%%{blender_api}/scripts/modules/bl_i18n_utils/utils_spell_check.py
# has "import enchant", but we judge that these scripts are really for people
# working on the translations, and should not be required in normal uses of the
# RPM package.

# Compression stuff
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(lzo2)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libzstd)

# 3D modeling stuff
BuildRequires:  cmake(ceres)
%if %{with embree}
BuildRequires:  embree-devel
%endif
%if %{with materialx}
BuildRequires:  materialx-devel
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
%if %{with openvdb}
BuildRequires:  openvdb-devel
%endif
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:	pkgconfig(libavformat)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(theora)
BuildRequires:  pkgconfig(vpx)
# OpenColorIO 2 and up required
BuildRequires:  cmake(OpenColorIO) > 1
BuildRequires:  cmake(Imath)
BuildRequires:  cmake(OpenEXR)
BuildRequires:  cmake(OpenImageIO) >= 2.5.0.0
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(tbb) = 2020.3
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
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(tinyxml)
# Appstream stuff
BuildRequires:  libappstream-glib

# HIP stuff
# https://developer.blender.org/docs/handbook/building_blender/cycles_gpu_binaries/#linux
%if %{with hip}
BuildRequires:  rocm-core
BuildRequires:  rocm-device-libs
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-runtime-devel
%endif

# OneAPU stuff
%if %{with oneapi}
BuildRequires:  pkgconfig(level-zero)
%endif

Requires:       hicolor-icon-theme
Requires:       rsms-inter-fonts
Requires:       shared-mime-info
Provides:       blender(ABI) = %{blender_api}

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
# %%autosetup -a1 failed to extract all tarball #2495
# https://github.com/rpm-software-management/rpm/issues/2495
%autosetup -N
%autopatch -p1

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
%if %{with hip}
export HIP_PATH=`hipconfig -p`
export HIP_CLANG_PATH=`hipconfig -l`
# On F-41, hipcc wants llvm-objcopy
%if 0%{?fedora} <= 41
export PATH=${PATH}:${HIP_CLANG_PATH}
%endif
%endif

%cmake \
%if %{with ninja}
    -G Ninja \
%endif
    -D_ffmpeg_INCLUDE_DIR=$(pkg-config --variable=includedir libavformat) \
%if %{with materialx}
    -DMATERIALX_STDLIB_DIR=%{_datadir}/materialx \
%endif
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
    -DCMAKE_SKIP_RPATH=ON \
    -DEMBREE_INCLUDE_DIR=%{_includedir} \
    -DPYTHON_VERSION=%{python3_version} \
    -DWITH_COMPILER_CCACHE=ON \
    -DWITH_CYCLES=%{cyclesflag} \
%ifnarch x86_64
    -DWITH_CYCLES_EMBREE=OFF \
%endif
%if %{with manpage} 
    -DWITH_DOC_MANPAGE=ON \
%endif
    -DWITH_INSTALL_PORTABLE=OFF \
    -DWITH_PYTHON_INSTALL=OFF \
%if %{with sdl}
    -DWITH_GHOST_SDL=ON \
%endif
%if %{with system_eigen3}
    -DWITH_SYSTEM_EIGEN3=ON \
%endif
%if %{with usd}
    -DUSD_LIBRARY=%{_libdir}/libusd_ms.so \
%else
    -DWITH_USD=OFF \
%endif
    -DXR_OPENXR_SDK_LOADER_LIBRARY=%{_libdir}/libopenxr_loader.so.1 \
%if %{with hip}
    -DHIP_HIPCC_EXECUTABLE=${HIP_CLANG_PATH}/clang++ \
    -DWITH_CYCLES_HIP_BINARIES=ON \
%endif
%if %{with oneapi}
    -DWITH_CYCLES_DEVICE_ONEAPI=ON \
%endif
    -DWITH_OPENCOLLADA=OFF \
    -DWITH_LIBS_PRECOMPILED=OFF

%cmake_build

%install
%cmake_install

%if %{with manpage}
# See source/creator/CMakeLists.txt.
# This doesn’t work in %%cmake_install because the assumption is that the
# blender executable and the libraries are installed directly to the correct
# system-wide paths. It is easier to re-run the man-page generator manually
# than to patch out this assumption.
LD_LIBRARY_PATH='%{buildroot}%{_libdir}' %{python3} doc/manpage/blender.1.py \
    --blender '%{buildroot}%{_bindir}/blender' \
    --output '%{buildroot}%{_mandir}/man1/blender.1'
%endif

# Install fallback binary
install -Dm755 release/bin/%{name}-softwaregl %{buildroot}%{_bindir}/%{name}-softwaregl

# rpm macros
mkdir -p %{buildroot}%{macrosdir}
install -pm 644 %{SOURCE1} %{buildroot}%{macrosdir}/macros.%{name}
sed -e 's/@VERSION@/%{blender_api}/g' %{buildroot}%{macrosdir}/macros.%{name}

# Metainfo
install -p -m 644 -D release/freedesktop/org.%{name}.Blender.metainfo.xml \
          %{buildroot}%{_metainfodir}/org.%{name}.Blender.metainfo.xml

# Localization
%find_lang %{name}

# rpmlint fixes
find %{buildroot}%{_datadir}/%{name}/%{blender_api}/scripts -name "*.py" -exec chmod 755 {} \;

# Deal with docs in the files section
rm -rf %{buildroot}%{_docdir}/%{name}/*

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.%{name}.Blender.metainfo.xml

%files -f %{name}.lang
%license COPYING
%license doc/license/*-license.txt
%license release/text/copyright.txt
%doc release/text/readme.html
%{_bindir}/%{name}{,-softwaregl,-thumbnailer}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/%{blender_api}/
%{_datadir}/icons/hicolor/*/apps/%{name}*.*
%if %{with manpage}
%{_mandir}/man1/%{name}.*
%endif
%{_metainfodir}/org.%{name}.Blender.metainfo.xml

%files rpm-macros
%{macrosdir}/macros.%{name}

%changelog
%autochangelog
