Name:           picasso
Version:        2.8.0
Release:        %{autorelease}
Summary:        2D vector graphic rendering library

# All code is under BSD-3-Clause except demos/platform_gix.c
# which is under LGPL-2.1-or-later
License:        BSD-3-Clause and LGPL-2.1-or-later
URL:            http://onecoolx.github.io/picasso/
#Source:        https://github.com/onecoolx/picasso/archive/v%%{version}/picasso-%%{version}.tar.gz
# Replace font with unknown license with one packaged in Fedora
# https://github.com/onecoolx/picasso/issues/14
# Obtained using
#> wget   https://github.com/onecoolx/picasso/archive/v%%{version}/picasso-%%{version}.tar.gz
#> tar -xf picasso-%%{version}.tar.gz
#> rm picasso-%%{version}/cfg/sunglobe.ttf
#> tar -cf picasso-%%{version}-clean.tar picasso-%%{version}
#> gzip picasso-%%{version}-clean.tar
Source:         picasso-%{version}-clean.tar.gz
# https://github.com/onecoolx/picasso/pull/16
Patch:          consistenttypes.patch
# Use Fedora build flags
Patch:          buildflags.patch
#  GifQuantizeBuffer() has moved
#  https://src.fedoraproject.org/rpms/giflib/pull-request/2#
Patch:          getarg.patch
Patch:          installdirs.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  giflib-devel
BuildRequires:  gtk2-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libwebp-devel
BuildRequires:  libpng-devel
BuildRequires:  zlib-ng-compat-devel
# Documentation
BuildRequires:  doxygen
# Fonts
Requires:       open-sans-fonts

%description
Picasso is a high quality vector graphic rendering library. It has high
performance and low footprint. Picasso provides a set of high level 2D
graphics API, which can be used to a GUI system, rendering postscript,
rendering svg images and so on. It support path, matrix, gradient, pattern,
image and truetype font.

%package devel
Summary: Development headers and libraries
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development headers and libraries for picasso.

%package demos
Summary: Demonstration programs
Requires: %{name}%{?_isa} = %{version}-%{release}

%description demos
Demonstration programs for picasso.

%package doc
Summary: Documentation in html format
BuildArch:  noarch

%description doc
Documentation for Picasso in html format.

%prep
%autosetup -n picasso-%{version} -p1
# Replace font with unknown license with one packaged in Fedora
# https://github.com/onecoolx/picasso/issues/14
sed -i 's|sunglobe.ttf|%{_datadir}/fonts/open-sans/OpenSans-Regular.ttf|g' cfg/font_config.cfg
# remove bundled libraries that are not used
rm -r third_party/giflib-5.1.3
rm -r third_party/libpng-1.6.17
rm -r third_party/libwebp-0.5.1
rm -r third_party/libjpeg-turbo-1.4.1
rm -r third_party/zlib-1.2.8
rm -r android

%build
%cmake -DOPT_FAST_COPY="ON"       \
       -DOPT_FONT_CONFIG="ON"     \
       -DOPT_FORMAT_ABGR="ON"     \
       -DOPT_FORMAT_ARGB="ON"     \
       -DOPT_FORMAT_BGR="ON"      \
       -DOPT_FORMAT_BGRA="ON"     \
       -DOPT_FORMAT_RGB="ON"      \
       -DOPT_FORMAT_RGB555="ON"   \
       -DOPT_FORMAT_RGB565="ON"   \
       -DOPT_FORMAT_RGBA="ON"     \
       -DOPT_FREE_TYPE2="ON"      \
       -DOPT_LOW_MEMORY="OFF"     \
       -DOPT_SYSTEM_MALLOC="ON"   \
       -DOPT_SYSTEM_GIF="ON"      \
       -DOPT_SYSTEM_JPEG="ON"     \
       -DOPT_SYSTEM_PNG="ON"      \
       -DOPT_SYSTEM_WEBP="ON"     \
       -DOPT_SYSTEM_ZLIB="ON"     \
       -DCMAKE_BUILD_TYPE=Release \
       -DCMAKE_LIBDIR=%{_libdir}  \
       -DCMAKE_SKIP_RPATH=YES

%cmake_build 
#Build documentation
doxygen
# While manpages are built, the names are generic and would conflict with other packages

%install
%cmake_install
mkdir -p %{buildroot}/%{_bindir}
install -pm755 %{__cmake_builddir}/clock %{buildroot}%{_bindir}/picasso-clock
install -pm755 %{__cmake_builddir}/flowers %{buildroot}%{_bindir}/picasso-flowers
install -pm755 %{__cmake_builddir}/subwaymap %{buildroot}%{_bindir}/picasso-subwaymap
install -pm755 %{__cmake_builddir}/tiger %{buildroot}%{_bindir}/picasso-tiger

%check
%ctest

%files
%license LICENSE
%doc README
%doc AUTHORS
%doc CREDITS
%{_libdir}/libpicasso2_sw.so.2.8.0
%{_libdir}/libpicasso2_sw.so.1
%{_libdir}/libpsx_image.so.2.8.0
%{_libdir}/libpsx_image.so.1
%dir %{_libdir}/picasso
%{_libdir}/picasso/libpsxm_image_png.so
%{_libdir}/picasso/libpsxm_image_jpeg.so
%{_libdir}/picasso/libpsxm_image_gif.so
%{_libdir}/picasso/libpsxm_image_webp.so

%files devel
%{_includedir}/picasso/
%{_libdir}/libpicasso2_sw.so
%{_libdir}/libpsx_image.so

%files demos
%{_bindir}/picasso-clock
%{_bindir}/picasso-flowers
%{_bindir}/picasso-subwaymap
%{_bindir}/picasso-tiger

%files doc
%license LICENSE
%doc doc/html

%changelog
%autochangelog
