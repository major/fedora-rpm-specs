# Break dependency cycles by disabling certain optional dependencies.
%bcond bootstrap 0

%global libargparse_url     https://github.com/maryla-uc/libargparse
%global libargparse_commit  81998ffafb9c2ac8cf488d31e536a2e6fd6b3fdf

# Break aom dependency cycle:
#   vmaf → aom → avif
%if %{with bootstrap}
# Build without aom
%bcond aom 0
# Build without SVT-AV1
%bcond svt 0
%else
# Build with aom
%bcond aom 1
# Build SVT-AV1
%bcond svt 1
%endif

%if (0%{?rhel} && 0%{?rhel} < 9) || 0%{?rhel} >= 10
%bcond rav1e 0
%else
%bcond rav1e 1
%endif
%bcond gtest 1
%bcond check 1

Name:           libavif
Version:        1.3.0
Release:        %autorelease
Summary:        Library for encoding and decoding .avif files

License:        BSD-2-Clause AND IJG AND Apache-2.0 AND BSD-3-Clause
URL:            https://github.com/AOMediaCodec/libavif
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source:         %{libargparse_url}/archive/%{libargparse_commit}/libargparse-%{libargparse_commit}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
%{?with_check:%{?with_gtest:BuildRequires:  gtest-devel}}
BuildRequires:  nasm
%{?with_aom:BuildRequires:  pkgconfig(aom)}
BuildRequires:  pkgconfig(dav1d)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libyuv)
%{?with_rav1e:BuildRequires:  pkgconfig(rav1e)}
%{?with_svt:BuildRequires:  pkgconfig(SvtAv1Enc)}
BuildRequires:  pkgconfig(zlib)

Obsoletes:      avif-pixbuf-loader < %{version}-%{release}

%description
This library aims to be a friendly, portable C implementation of the AV1 Image
File Format, as described here:

https://aomediacodec.github.io/av1-avif/

%package        devel
Summary:        Development files for libavif
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package holds the development files for libavif.

%package        tools
Summary:        Tools to encode and decode AVIF files

%description    tools
This library aims to be a friendly, portable C implementation of the AV1 Image
File Format, as described here:

https://aomediacodec.github.io/av1-avif/

This package holds the commandline tools to encode and decode AVIF files.

%prep
%autosetup -p1
mkdir -p ext/libargparse
tar --strip-components=1 -xvf %{S:1} -C ext/libargparse

%build
%cmake \
     -DCMAKE_BUILD_TYPE=RelWithDebInfo           \
     -DAVIF_BUILD_APPS=1                         \
     %{?with_check:-DAVIF_BUILD_TESTS=1 %{?with_gtest:-DAVIF_GTEST=SYSTEM}} \
     %{?with_aom:-DAVIF_CODEC_AOM=SYSTEM}        \
     -DAVIF_CODEC_DAV1D=SYSTEM                   \
     %{?with_rav1e:-DAVIF_CODEC_RAV1E=SYSTEM}    \
     %{?with_svt:-DAVIF_CODEC_SVT=SYSTEM}        \
     -DAVIF_LIBXML2=SYSTEM

%cmake_build

%install
%cmake_install

%if %{with check}
%check
%ctest
%endif

%files
%license LICENSE
# Do not glob the soname
%{_libdir}/libavif.so.16*

%files devel
%{_libdir}/libavif.so
%{_includedir}/avif/
%{_libdir}/cmake/libavif/
%{_libdir}/pkgconfig/libavif.pc

%files tools
%doc CHANGELOG.md README.md
%{_bindir}/avifdec
%{_bindir}/avifenc
%{_bindir}/avifgainmaputil

%changelog
%autochangelog
