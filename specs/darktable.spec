###
# To build darktable from Github master branch add cmake flag -DPROJECT_VERSION="%%{version}"
# darktable stable releases have src/version_gen.c file that makes
# -DPROJECT_VERSION="%%{version}" no longer needed
# src/version_gen.c file is not available in darktable master Github branch instead
###

Name: darktable
Version: 5.6.1
Release: %autorelease

Summary: Utility to organize and develop raw images
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later
URL: http://www.darktable.org/

Source0: https://github.com/darktable-org/darktable/releases/download/release-%{version}/%{name}-%{version}.tar.xz
#Source1: https://github.com/darktable-org/darktable/releases/download/release-%%{version}/%%{name}-%%{version}.tar.xz.asc
#Source2: https://keyserver.ubuntu.com/pks/lookup?op=get&search=0xf10f9686652b0e949fcd94c318dca123f949bd3b


# Lua 5.5 build support
Patch0: darktable-5.6.1-lua-5.5.patch

# https://github.com/darktable-org/lua-scripts/pull/678
Patch1: darktable-5.6.1-lua-5.5-scripts.patch

BuildRequires: cairo-devel
# clang is optional (OpenCL kernel build test)
BuildRequires: clang >= 7
BuildRequires: cmake >= 3.18
BuildRequires: colord-gtk-devel
BuildRequires: colord-devel
BuildRequires: cups-devel
BuildRequires: desktop-file-utils
BuildRequires: exiv2-devel >= 0.27.2
BuildRequires: gcc
BuildRequires: glib2-devel >= 2.56
BuildRequires: gmic-devel >= 2.7.0
BuildRequires: GraphicsMagick-devel
BuildRequires: gtk3-devel >= 3.24.15
BuildRequires: intltool
BuildRequires: iso-codes-devel >= 3.66
BuildRequires: gettext
BuildRequires: json-glib-devel
BuildRequires: lcms2-devel
BuildRequires: lensfun-devel
BuildRequires: libappstream-glib
BuildRequires: cmake(libavif) >= 0.9.3
BuildRequires: libcurl-devel >= 7.56
BuildRequires: libgphoto2-devel >= 2.5
BuildRequires: libheif-devel >= 1.13.0
BuildRequires: libicu-devel
BuildRequires: libjpeg-devel
BuildRequires: libjxl-devel >= 0.7.0
BuildRequires: libpng-devel >= 1.5.0
BuildRequires: librsvg2-devel >= 2.26
BuildRequires: libsecret-devel
BuildRequires: libtiff-devel
BuildRequires: libwebp-devel >= 0.3.0
# llvm-devel is optional (OpenCL kernel build test)
BuildRequires: llvm-devel >= 7
BuildRequires: pkgconfig(lua)
# opencl-headers is optional (OpenCL kernel build test)
BuildRequires: opencl-headers
BuildRequires: cmake(OpenEXR) > 3.0
BuildRequires: cmake(Imath) >= 3.1.0
%if (%{defined fedora} && 0%{?fedora} > 43)
BuildRequires: libarchive-devel >= 3.8.5
BuildRequires: onnxruntime-devel >= 1.18
%endif
BuildRequires: openjpeg2-devel
BuildRequires: osm-gps-map-devel >= 1.0
BuildRequires: perl-interpreter
BuildRequires: perl(FindBin)
BuildRequires: perl(lib)
BuildRequires: pkgconfig >= 0.22
BuildRequires: po4a
BuildRequires: perl-podlators
BuildRequires: portmidi-devel
BuildRequires: potrace-devel >= 1.16
BuildRequires: pugixml-devel >= 1.8
BuildRequires: cmake(SDL2)
BuildRequires: sqlite-devel >= 3.26
BuildRequires: zlib-devel >= 1.2.11

Requires: iso-codes >= 3.66

# Concerning rawspeed bundled library, see
# https://fedorahosted.org/fpc/ticket/550#comment:9
Provides: bundled(rawspeed)
# https://bugzilla.redhat.com/show_bug.cgi?id=2252432
Provides: bundled(libraw)

# Unsupported CPU architectures
# filled https://bugzilla.redhat.com/show_bug.cgi?id=2038684
# to be compliant to "Architecture Build Failures" paragraph of Fedora Packaging Guidelines 
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_architecture_build_failures
# =============
ExcludeArch: armv7hl i686 s390x


%description
darktable manages your camera raw files and images in a database, lets you
view them through lighttable mode and develop/enhance them in darkroom mode.

%package tools-noise
Summary:        The noise profiling tools to support new cameras
Requires:       ImageMagick
Requires:       gnuplot

%description tools-noise
darktable is a virtual lighttable and darkroom for photographers: it manages
your digital negatives in a database and lets you view them through a zoomable
lighttable. it also enables you to develop raw images and enhance them.

%package tools-basecurve
Summary:        The basecurve tool from tools/basecurve/
Requires:       ImageMagick
Requires:       dcraw
Requires:       perl-Image-ExifTool

%description tools-basecurve
darktable is a virtual lighttable and darkroom for photographers: it manages
your digital negatives in a database and lets you view them through a zoomable
lighttable. it also enables you to develop raw images and enhance them.

This package provides the basecurve tool from tools/basecurve/.
Another option to solve the same problem might be the darktable-chart module
from the darktable package.

%prep
#%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

# Remove bundled OpenCL headers.
rm -rf src/external/CL
sed -i -e 's, \"external/CL/\*\.h\" , ,' src/CMakeLists.txt


%build
%if (%{defined fedora} && 0%{?fedora} > 43)
%cmake \
        -DCMAKE_LIBRARY_PATH:PATH=%{_libdir} \
        -DUSE_GEO:BOOLEAN=ON \
        -DCMAKE_BUILD_TYPE:STRING=Release \
        -DBINARY_PACKAGE_BUILD=1 \
        -DBUILD_NOISE_TOOLS=ON \
        -DBUILD_CURVE_TOOLS=ON \
        -DRAWSPEED_ENABLE_LTO=ON \
        -DUSE_AI=ON \
        -DONNXRUNTIME_OFFLINE=ON
%elif (%{defined fedora} && 0%{?fedora} == 43)
%cmake \
        -DCMAKE_LIBRARY_PATH:PATH=%{_libdir} \
        -DUSE_GEO:BOOLEAN=ON \
        -DCMAKE_BUILD_TYPE:STRING=Release \
        -DBINARY_PACKAGE_BUILD=1 \
        -DBUILD_NOISE_TOOLS=ON \
        -DBUILD_CURVE_TOOLS=ON \
        -DRAWSPEED_ENABLE_LTO=ON
%endif


%cmake_build


%install
%cmake_install


%find_lang %{name}
rm -rf %{buildroot}%{_datadir}/doc/darktable
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.darktable.darktable.appdata.xml

%files -f %{name}.lang 
%license LICENSE
%doc doc/README.md
%{_bindir}/darktable
%{_bindir}/darktable-chart
%{_bindir}/darktable-cli

%{_bindir}/darktable-cltest
%{_bindir}/darktable-cmstest
%{_bindir}/darktable-generate-cache
%{_bindir}/darktable-rs-identify
%{_libdir}/darktable
%{_datadir}/darktable
%{_datadir}/applications/org.darktable.darktable.desktop
%{_datadir}/metainfo/org.darktable.darktable.appdata.xml
%{_datadir}/icons/hicolor/*/apps/darktable*
%{_mandir}/man1/darktable*.1*
%{_mandir}/*/man1/darktable*.1*

%files tools-noise
%dir %{_libexecdir}/darktable
%dir %{_libexecdir}/darktable/tools
%{_libexecdir}/darktable/tools/darktable-gen-noiseprofile
%{_libexecdir}/darktable/tools/darktable-noiseprofile
%{_libexecdir}/darktable/tools/profiling-shot.xmp
%{_libexecdir}/darktable/tools/subr.sh

%files tools-basecurve
%dir %{_libexecdir}/darktable
%dir %{_libexecdir}/darktable/tools
%{_libexecdir}/darktable/tools/darktable-curve-tool
%{_libexecdir}/darktable/tools/darktable-curve-tool-helper

%changelog
%autochangelog
