%global vips_version_base 8.17
%global vips_version %{vips_version_base}.2
%global vips_soname_major 42

Name:		vips
Version:	%{vips_version}
Release:	%autorelease
Summary:	C/C++ library for processing large images

License:	LGPL-2.1-or-later
URL:		https://www.libvips.org/
Source0:	https://github.com/libvips/libvips/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:	meson
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(libhwy)
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	pkgconfig(imagequant)
BuildRequires:	pkgconfig(OpenEXR)
BuildRequires:	pkgconfig(Imath)
BuildRequires:	pkgconfig(matio)
BuildRequires:	pkgconfig(cfitsio)
BuildRequires:	pkgconfig(pangoft2)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(cgif)
BuildRequires:	pkgconfig(spng)
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(libjxl)
BuildRequires:	pkgconfig(libheif)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(libwebp)
BuildRequires:	pkgconfig(libexif)
BuildRequires:	pkgconfig(libarchive)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(libopenjp2)
BuildRequires:	pkgconfig(openslide)
BuildRequires:	pkgconfig(poppler-glib)
BuildRequires:	pkgconfig(MagickWand)
BuildRequires:	nifticlib-devel

BuildRequires:	gcc-c++
BuildRequires:	pkgconfig
BuildRequires:	gettext
BuildRequires:	gi-docgen
BuildRequires:	doxygen

# bc command used in test suite
BuildRequires:	bc

# Not available as system library
Provides:	bundled(libnsgif)

# Optional plugins
Recommends: %{name}-jxl
Recommends: %{name}-heif
Recommends: %{name}-magick
Recommends: %{name}-openslide
Recommends: %{name}-poppler

%description
VIPS is an image processing library. It is good for very large images
(even larger than the amount of RAM in your machine), and for working
with color.

This package should be installed if you want to use a program compiled
against VIPS.


%package devel
Summary:	Development files for %{name}
Requires:	vips%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains the header files and
libraries necessary for developing programs using VIPS.


%package tools
Summary:	Command-line tools for %{name}
Requires:	vips%{?_isa} = %{version}-%{release}

%description tools
The %{name}-tools package contains command-line tools for working with VIPS.


%package doc
Summary:	Documentation for %{name}
BuildArch:	noarch
Conflicts:	%{name} < %{version}-%{release}, %{name} > %{version}-%{release}

%description doc
The %{name}-doc package contains extensive HTML documentation about VIPS and
its C++ API.


%package jxl
Summary:	JPEG XL support for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description jxl
The %{name}-jxl package contains the jxl module for VIPS, providing JPEG XL
support.


%package heif
Summary:	HEIF support for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description heif
The %{name}-heif package contains the heif module for VIPS, providing AVIF
support.


%package openslide
Summary:	OpenSlide support for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description openslide
The %{name}-openslide package contains the OpenSlide module for VIPS.


%package poppler
Summary:	Poppler support for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description poppler
The %{name}-poppler package contains the Poppler module for VIPS.


%package magick
Summary:	Magick support for %{name} using ImageMagick7
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description magick
The %{name}-magick package contains the Magick module for VIPS using
ImageMagick7.


%prep
%autosetup -p1


%build
# Upstream recommends enabling auto-vectorization of inner loops:
# https://github.com/libvips/libvips/pull/212#issuecomment-68177930
export CFLAGS="%{optflags} -ftree-vectorize"
export CXXFLAGS="%{optflags} -ftree-vectorize"
# TODO remove `-Dnifti-prefix-dir=/usr`:
# https://github.com/libvips/libvips/pull/2882#issuecomment-1165686117
# https://github.com/NIFTI-Imaging/nifti_clib/pull/140
%meson \
    -Dnifti-prefix-dir=/usr \
    -Dcpp-docs=true \
    -Ddocs=true \
    -Dpdfium=disabled \
    %{nil}

%meson_build


%install
%meson_install

# locale stuff
%find_lang vips%{vips_version_base}


%check
%meson_test


%files -f vips%{vips_version_base}.lang
%doc ChangeLog README.md
%license LICENSE
%{_libdir}/*.so.%{vips_soname_major}*
%{_libdir}/girepository-1.0
%dir %{_libdir}/vips-modules-%{vips_version_base}


%files devel
%{_includedir}/vips
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_datadir}/gir-1.0


%files tools
%{_bindir}/*
%{_mandir}/man1/*


%files doc
%{_docdir}/vips
%{_docdir}/vips-cpp
%license LICENSE


%files jxl
%{_libdir}/vips-modules-%{vips_version_base}/vips-jxl.so


%files heif
%{_libdir}/vips-modules-%{vips_version_base}/vips-heif.so


%files openslide
%{_libdir}/vips-modules-%{vips_version_base}/vips-openslide.so


%files poppler
%{_libdir}/vips-modules-%{vips_version_base}/vips-poppler.so


%files magick
%{_libdir}/vips-modules-%{vips_version_base}/vips-magick.so


%changelog
%autochangelog
