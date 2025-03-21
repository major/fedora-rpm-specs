Name:           SDL3_image
Version:        3.2.4
Release:        %autorelease
Summary:        Image loading library for SDL
License:        Zlib AND (HPND-Pbmplus AND Zlib) AND Unlicense AND MIT AND (MIT OR Unlicense) AND LicenseRef-Fedora-Public-Domain
# License breakdown:
# ./examples/showanim.c: Zlib
# ./examples/showimage.c: Zlib
# ./include/SDL3_image/SDL_image.h: Zlib
# ./src/IMG*.c: Zlib
# Except:
# ./src/IMG_gif.c: HPND-Pbmplus AND Zlib
# ./src/miniz.h: Unlicense
# ./src/nanosvg.h: Zlib
# ./src/nanosvgrast.h: Zlib
# ./src/qoi.h: MIT
# ./src/stb_image.h: MIT OR Unlicense
# ./src/tiny_jpeg.h: Public Domain
URL:            https://github.com/libsdl-org/SDL_image

Source0:        %{url}/releases/download/release-%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  cmake(libavif)
BuildRequires:  cmake(libjpeg-turbo)
BuildRequires:  cmake(webp)
BuildRequires:  cmake(sdl3) >= 3.2.4
BuildRequires:  gcc
BuildRequires:  libjxl-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  SDL3-test

Provides:       bundled(miniz) = 1.15
# Some custom version of it:
Provides:       bundled(nanosvg)

%description
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library designed
to provide fast access to the graphics frame buffer and audio device.

This is a simple library to load images of various formats as SDL surfaces.
It can load BMP, GIF, JPEG, LBM, PCX, PNG, PNM (PPM/PGM/PBM), QOI, TGA, XCF,
XPM, and simple SVG format images. It can also load AVIF, JPEG-XL, TIFF, and
WebP images.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       cmake-filesystem

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%prep
%autosetup -p1

%build
%cmake \
  -DSDLIMAGE_AVIF=ON \
  -DSDLIMAGE_AVIF_SAVE=ON \
  -DSDLIMAGE_AVIF_SHARED=ON \
  -DSDLIMAGE_BACKEND_STB=ON \
  -DSDLIMAGE_BMP=ON \
  -DSDLIMAGE_DEPS_SHARED=ON \
  -DSDLIMAGE_GIF=ON \
  -DSDLIMAGE_INSTALL=ON \
  -DSDLIMAGE_INSTALL_CPACK=ON \
  -DSDLIMAGE_INSTALL_MAN=ON \
  -DSDLIMAGE_JPG=ON \
  -DSDLIMAGE_JPG_SAVE=ON \
  -DSDLIMAGE_JXL=ON \
  -DSDLIMAGE_LBM=ON \
  -DSDLIMAGE_PCX=ON \
  -DSDLIMAGE_PNG=ON \
  -DSDLIMAGE_PNG_SAVE=ON \
  -DSDLIMAGE_PNM=ON \
  -DSDLIMAGE_QOI=ON \
  -DSDLIMAGE_SAMPLES=ON \
  -DSDLIMAGE_SAMPLES_INSTALL=ON \
  -DSDLIMAGE_STRICT=OFF \
  -DSDLIMAGE_SVG=ON \
  -DSDLIMAGE_TESTS=ON \
  -DSDLIMAGE_TESTS_INSTALL=OFF \
  -DSDLIMAGE_TGA=ON \
  -DSDLIMAGE_TIF=ON \
  -DSDLIMAGE_TIF_SHARED=ON \
  -DSDLIMAGE_VENDORED=OFF \
  -DSDLIMAGE_WEBP=ON \
  -DSDLIMAGE_WEBP_SHARED=ON \
  -DSDLIMAGE_WERROR=OFF \
  -DSDLIMAGE_XCF=ON \
  -DSDLIMAGE_XPM=ON \
  -DSDLIMAGE_XV=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE.txt
%doc CHANGES.txt README.md
%{_libdir}/lib%{name}.so.0
%{_libdir}/lib%{name}.so.0.2.4

%files devel
%{_bindir}/showanim
%{_bindir}/showimage
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}/
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/sdl3-image.pc
%{_mandir}/man3/IMG_*.3*
%{_mandir}/man3/SDL_IMAGE_*.3*

%changelog
%autochangelog
