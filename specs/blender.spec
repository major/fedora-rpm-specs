%global blender_api 4.4
%global macrosdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)
%global _without_bundled_deps 1

# Build conditionals
%bcond clang      0   # Use Clang compiler
%bcond draco      1   # Draco mesh compression support
%bcond llvm       1   # Required for OSL support
%bcond manpage    1   # Generate manpage
%bcond materialx  0   # MaterialX support
%bcond nanovdb    1   # NanoVDB support
%bcond ninja      1   # Use Ninja build system
%bcond openshading 1  # OpenShadingLanguage support
%bcond openvdb    1   # OpenVDB support
%bcond sdl        0   # SDL backend
%bcond system_eigen3 1 # Use system Eigen3
%bcond vulkan     1   # Vulkan rendering support

# Architecture-specific features
%ifarch x86_64 aarch64 ppc64le
%global cyclesflag ON
    # x86_64/aarch64 specific features
    %ifarch x86_64 aarch64
    %bcond embree 1   # Intel Embree ray tracing
    %bcond hidapi 1   # HIDAPI support
    
    # x86_64 exclusive features
    %ifarch x86_64
    %bcond hip   1    # AMD HIP support
    %bcond hiprt 1    # HIP ray tracing (requires Fedora 43+)
    %bcond oidn  1    # OpenImageDenoise
    %bcond oneapi 0   # Intel OneAPI support
    %bcond opgl  1    # OpenPGL
    %global llvm_compat 18
    %endif
    %bcond usd   1    # Universal Scene Description
%else
    %bcond embree 0
    %bcond hidapi 0
    %bcond oidn  0
    %bcond opgl  0
    %bcond usd   0
%endif
%else
%global cyclesflag OFF
%endif

Name:           blender
Epoch:          1
Version:        4.4.1
Release:        %autorelease

Summary:        3D modeling, animation, rendering and post-production
# Blender source is under GPL-2.0-or-later by default
# Apache-2.0 for Blender Cycles rendering engine
# BSD License for Open Shading Language
# Zlib License for Bullets
# GPL-3.0-or-later for the whole project
# https://www.blender.org/about/license/
License:	%{shrink:
		Apache-2.0 AND
  		BSD-3-Clause AND
  		GPL-2.0-or-later AND
  		GPL-3.0-or-later AND
  		Zlib
		}
URL:            https://www.blender.org

Source0:        https://download.%{name}.org/source/%{name}-%{version}.tar.xz
# Custom RPM macros
Source1:        %{name}-macros-source

# Build requirements
BuildRequires:  boost-devel
BuildRequires:  ccache
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  git-core
BuildRequires:  libharu-devel
BuildRequires:  libtool
BuildRequires:  subversion-devel

# Conditional build deps
%if %{with clang}
BuildRequires:  clang%{?llvm_compat}-devel
%endif
%if %{with llvm}
BuildRequires:  llvm%{?llvm_compat}-devel
%endif
%if %{with ninja}
BuildRequires:  ninja-build
%endif

# System libraries
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
BuildRequires:  pkgconfig(libpcre2-32)
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
%if %{with nanovdb}
BuildRequires:  openvdb-nanovdb-devel
%endif
%if %{with openvdb}
BuildRequires:  openvdb-devel
%endif
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavformat)
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
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  pkgconfig(ao)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(freealut)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(opus)
BuildRequires:	pkgconfig(libpipewire-0.3)
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
%if %{with hiprt}
BuildRequires:  hiprt-devel
%endif
BuildRequires:	hipcc
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

%package rpm-macros
Summary:        RPM macros for third-party blender addons
BuildArch:      noarch

%description rpm-macros
Provides RPM macros for creating third-party addon packages for Blender.

%prep
%autosetup -p1

# System integration fixes
rm -f build_files/cmake/Modules/FindOpenJPEG.cmake
%py3_shebang_fix .
sed -i "s/date_time/date_time python%{python3_version_nodots}/" \
    build_files/cmake/platform/platform_unix.cmake
# Fix proper detection of numpy path
# https://projects.blender.org/blender/blender/issues/137635    
sed -i "s|core/include|_core/include|" CMakeLists.txt

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
    -DBUILD_SHARED_LIBS=OFF \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_SKIP_RPATH=ON \
    -DPYTHON_VERSION=%{python3_version} \
    -DWITH_COMPILER_CCACHE=ON \
    -DWITH_CYCLES=%{cyclesflag} \
%ifnarch x86_64
    -DWITH_CYCLES_EMBREE=OFF \
%endif
    -DWITH_INSTALL_PORTABLE=OFF \
    -DWITH_PYTHON_INSTALL=OFF \
    %{?with_manpage:-DWITH_DOC_MANPAGE=ON } \
    %{?with_materialx:-DMATERIALX_STDLIB_DIR=%{_datadir}/materialx} \
    %{!?with_materialx:-DWITH_MATERIALX=OFF} \
    %{?with_openshading:-DOSL_COMPILER=%{_bindir}/oslc} \
    %{?with_usd:-DUSD_LIBRARY=%{_libdir}/libusd_ms.so} \
    %{!?with_usd:-DWITH_USD=OFF} \
    -D_ffmpeg_INCLUDE_DIR=$(pkg-config --variable=includedir libavformat) \
    -DEMBREE_INCLUDE_DIR=%{_includedir} \
    -DXR_OPENXR_SDK_LOADER_LIBRARY=%{_libdir}/libopenxr_loader.so.1 \
%if %{with hip}
    -DHIP_HIPCC_EXECUTABLE=%{_bindir}/hipcc \
    -DWITH_CYCLES_HIP_BINARIES=ON \
    %{?with_hiprt:-DWITH_CYCLES_DEVICE_HIPRT=ON} \
%endif
    %{?with_oneapi:-DWITH_CYCLES_DEVICE_ONEAPI=ON} \
    -DWITH_OPENCOLLADA=OFF \
    -DWITH_LIBS_PRECOMPILED=OFF \
    -W no-dev

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

# Additional installs
install -Dm755 release/bin/%{name}-softwaregl %{buildroot}%{_bindir}/%{name}-softwaregl
mkdir -p %{buildroot}%{macrosdir}
install -pm 644 %{SOURCE1} %{buildroot}%{macrosdir}/macros.%{name}
sed -i 's/@VERSION@/%{blender_api}/g' %{buildroot}%{macrosdir}/macros.%{name}

# Metainfo
install -p -m 644 -D release/freedesktop/org.%{name}.Blender.metainfo.xml \
          %{buildroot}%{_metainfodir}/org.%{name}.Blender.metainfo.xml

# Localization and cleanup
%find_lang %{name}
find %{buildroot}%{_datadir}/%{name}/%{blender_api}/scripts -name "*.py" -exec chmod 755 {} \;
rm -rf %{buildroot}%{_docdir}/%{name}/*

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.%{name}.Blender.metainfo.xml

%files -f %{name}.lang
%license COPYING doc/license/*-license.txt release/text/copyright.txt
%doc release/text/readme.html
%{_bindir}/%{name}{,-softwaregl,-thumbnailer}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/%{blender_api}/
%{_datadir}/icons/hicolor/*/apps/%{name}*.*
%{_metainfodir}/org.%{name}.Blender.metainfo.xml
%{?with_manpage:%{_mandir}/man1/%{name}.*}

%files rpm-macros
%{macrosdir}/macros.%{name}

%changelog
%autochangelog
