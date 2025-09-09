%global somajor 1
# this is used for breaking a self-dependency on build, via
# two paths, first:
# libheif BuildRequires: pkgconfig(sdl2) == sdl2-compat-devel
# sdl2-compat-devel -> sdl2-compat
# sdl2-compat -> SDL3
# SDL3 -> libdecor
# libdecor -> gtk3
# gtk3 -> gtk-update-icon-cache
# gtk-update-icon-cache -> gdk-pixbuf2
# gdk-pixbuf2 -> glycin-libs
# glycin-libs -> glycin-loaders
# glycin-loaders -> libheif
# second:
# heif-pixbuf-loader BuildRequires: pkgconfig(gdk-pixbuf-2.0) == gdk-pixbuf2-devel
# gdk-pixbuf2-devel -> gdk-pixbuf2
# gdk-pixbuf2 -> glycin-libs
# glycin-libs -> glycin-loaders
# glycin-loaders -> libheif
%bcond bootstrap 0

Name:           libheif
Version:        1.20.2
Release:        %autorelease
Summary:        HEIF and AVIF file format decoder and encoder

License:        LGPL-3.0-or-later and MIT
URL:            https://github.com/strukturag/libheif
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         libheif-no-hevc-tests.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(aom)
BuildRequires:  pkgconfig(dav1d)
BuildRequires:  pkgconfig(libbrotlidec)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(openh264)
%if !%{with bootstrap}
BuildRequires:  pkgconfig(sdl2)
%endif
BuildRequires:  pkgconfig(zlib)
%ifnarch %{ix86}
BuildRequires:  pkgconfig(openjph) >= 0.18.0
%endif
%if ! (0%{?rhel} && 0%{?rhel} <= 9)
BuildRequires:  pkgconfig(libsharpyuv)
BuildRequires:  pkgconfig(rav1e)
BuildRequires:  pkgconfig(SvtAv1Enc)
%endif

%description
libheif is an ISO/IEC 23008-12:2017 HEIF and AVIF (AV1 Image File Format)
file format decoder and encoder.

%files
%license COPYING
%doc README.md
%{_libdir}/%{name}.so.%{somajor}{,.*}
%dir %{_libdir}/%{name}

# ----------------------------------------------------------------------

%if !%{with bootstrap}
%package -n     heif-pixbuf-loader
Summary:        HEIF image loader for GTK+ applications
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       gdk-pixbuf2%{?_isa}

%description -n heif-pixbuf-loader
This package provides a plugin to load HEIF files in GTK+ applications.

%files -n heif-pixbuf-loader
%{_libdir}/gdk-pixbuf-2.0/*/loaders/libpixbufloader-heif.so
%endif

# ----------------------------------------------------------------------

%package        tools
Summary:        Tools for manipulating HEIF files
License:        MIT
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       shared-mime-info

%description    tools
This package provides tools for manipulating HEIF files.

%files tools
%{_bindir}/heif-*
%{_mandir}/man1/heif-*
%{_datadir}/thumbnailers/heif.thumbnailer

# ----------------------------------------------------------------------

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files devel
%{_includedir}/%{name}/
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/%{name}.so

# ----------------------------------------------------------------------


%prep
%setup -q
%patch 0 -p1
rm -rf third-party/


%build
%cmake \
 -GNinja \
 -DBUILD_TESTING=ON \
 -DCMAKE_COMPILE_WARNING_AS_ERROR=OFF \
 -DPLUGIN_DIRECTORY=%{_libdir}/%{name} \
 -DWITH_DAV1D=ON \
 -DWITH_DAV1D_PLUGIN=OFF \
 -DWITH_JPEG_DECODER=ON \
 -DWITH_JPEG_ENCODER=ON \
 -DWITH_OpenH264_DECODER=ON \
 -DWITH_OpenH264_ENCODER=ON \
 -DWITH_OpenJPEG_DECODER=ON \
 -DWITH_OpenJPEG_DECODER_PLUGIN=OFF \
 -DWITH_OpenJPEG_ENCODER=ON \
 -DWITH_OpenJPEG_ENCODER_PLUGIN=OFF \
%ifnarch %{ix86}
 -DWITH_OPENJPH_DECODER=ON \
 -DWITH_OPENJPH_ENCODER=ON \
 -DWITH_OPENJPH_ENCODER_PLUGIN=OFF \
%endif
%if ! (0%{?rhel} && 0%{?rhel} <= 9)
 -DWITH_RAV1E=ON \
 -DWITH_RAV1E_PLUGIN=OFF \
 -DWITH_SvtEnc=ON \
 -DWITH_SvtEnc_PLUGIN=OFF \
%endif
%if %{with bootstrap}
 -DWITH_EXAMPLE_HEIF_VIEW=OFF \
%endif
 -DWITH_UNCOMPRESSED_CODEC=ON \
 -Wno-dev

%cmake_build


%install
%cmake_install

# fix multilib issues: Rename the provided file with platform-bits in name.
# Create platform independent file inplace of the provided one and conditionally
# include the required one.
# $1 - filename.h to process.
function multilibFileVersions(){
mv $1 ${1%%.h}-%{__isa_bits}.h

local basename=$(basename $1)

cat >$1 <<EOF
#include <bits/wordsize.h>

#if __WORDSIZE == 32
# include "${basename%%.h}-32.h"
#elif __WORDSIZE == 64
# include "${basename%%.h}-64.h"
#else
# error "unexpected value for __WORDSIZE macro"
#endif
EOF
}

multilibFileVersions %{buildroot}%{_includedir}/%{name}/heif_version.h


%check
%ctest


%changelog
%autochangelog
