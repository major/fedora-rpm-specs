Name:           SDL2_image
Version:        2.8.12
Release:        %autorelease
Summary:        Image loading library for SDL

# IMG_png.c is LGPLv2+ and zlib, rest is just zlib
# nanosvg is zlib
# miniz is Public Domain
# Automatically converted from old format: LGPLv2+ and zlib - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+ AND Zlib
URL:            https://github.com/libsdl-org/SDL_image
Source0:        https://github.com/libsdl-org/SDL_image/releases/download/release-%{version}/SDL2_image-%{version}.tar.gz

BuildRequires:  automake
BuildRequires:  chrpath
BuildRequires:  gcc
BuildRequires:  libavif-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libjxl-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libwebp-devel
BuildRequires:  make
BuildRequires:  SDL2-devel

Provides:       bundled(miniz) = 1.15
# Some custom version of it
Provides:       bundled(nanosvg)

%description
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio
device.  This package contains a simple library for loading images of
various formats (BMP, PPM, PCX, GIF, JPEG, PNG) as SDL surfaces.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1
sed -i -e 's/\r//g' README.txt CHANGES.txt

%build
./autogen.sh
%configure --disable-dependency-tracking \
           --disable-jpg-shared \
           --disable-png-shared \
           --disable-tif-shared \
           --disable-webp-shared \
           --disable-jxl-shared \
           --disable-avif-shared \
           --disable-static
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
%make_build

%install
%make_install
mkdir -p %{buildroot}%{_bindir}
./libtool --mode=install /usr/bin/install showimage %{buildroot}%{_bindir}/showimage2
chrpath -d %{buildroot}%{_bindir}/showimage2

rm -f %{buildroot}%{_libdir}/*.la

%files
%license LICENSE.txt
%doc CHANGES.txt
%{_bindir}/showimage2
%{_libdir}/libSDL2_image-2.0.so.*

%files devel
%doc README.txt
%{_libdir}/libSDL2_image.so
%{_includedir}/SDL2/SDL_image.h
%dir %{_libdir}/cmake
%{_libdir}/cmake/SDL2_image/
%{_libdir}/pkgconfig/SDL2_image.pc

%changelog
%autochangelog
