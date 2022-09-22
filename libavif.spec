# Build with aom
%bcond_without aom
# Build SVT-AV1
%ifarch x86_64
%bcond_without svt
%endif

Name:           libavif
Version:        0.10.1
Release:        %autorelease
Summary:        Library for encoding and decoding .avif files

License:        BSD
URL:            https://github.com/AOMediaCodec/libavif
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  nasm
%if %{with aom}
BuildRequires:  pkgconfig(aom)
%endif
BuildRequires:  pkgconfig(dav1d)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(rav1e)
%{?with_svt:BuildRequires:  pkgconfig(SvtAv1Enc)}
BuildRequires:  pkgconfig(zlib)

%description
This library aims to be a friendly, portable C implementation of the AV1 Image
File Format, as described here:

https://aomediacodec.github.io/av1-avif/

%package devel
Summary:        Development files for libavif
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package holds the development files for libavif.

%package tools
Summary:        Tools to encode and decode AVIF files

%description tools
This library aims to be a friendly, portable C implementation of the AV1 Image
File Format, as described here:

https://aomediacodec.github.io/av1-avif/

This package holds the commandline tools to encode and decode AVIF files.

%package     -n avif-pixbuf-loader
Summary:        AVIF image loader for GTK+ applications
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
Requires:       gdk-pixbuf2

%description -n avif-pixbuf-loader
Avif-pixbuf-loader contains a plugin to load AVIF images in GTK+ applications.

%prep
%autosetup -p1

%build
%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    %{?with_aom:-DAVIF_CODEC_AOM=1} \
    -DAVIF_CODEC_DAV1D=1 \
    -DAVIF_CODEC_RAV1E=1 \
    %{?with_svt:-DAVIF_CODEC_SVT=1} \
    -DAVIF_BUILD_APPS=1 \
    -DAVIF_BUILD_GDK_PIXBUF=1
%cmake_build

%install
%cmake_install

%files
%license LICENSE
# Do not glob the soname
%{_libdir}/libavif.so.14*

%files devel
%{_libdir}/libavif.so
%{_includedir}/avif/
%{_libdir}/cmake/libavif/
%{_libdir}/pkgconfig/libavif.pc

%files tools
%doc CHANGELOG.md README.md
%{_bindir}/avifdec
%{_bindir}/avifenc

%files -n avif-pixbuf-loader
%{_libdir}/gdk-pixbuf-2.0/*/loaders/libpixbufloader-avif.so

%changelog
%autochangelog
