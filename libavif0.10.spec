# Build with aom
%bcond_without aom
# Build SVT-AV1
%ifarch x86_64
%bcond_without svt
%endif

Name:           libavif0.10
Version:        0.10.1
Release:        %autorelease
Summary:        Library for encoding and decoding .avif files

License:        BSD
URL:            https://github.com/AOMediaCodec/libavif
Source0:        %{url}/archive/v%{version}/libavif-%{version}.tar.gz

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

# Explicitly conflict with libavif package that used to ship the same soname as
# this libavif0.10 compat package
Conflicts: libavif < 0.11

%description
This library aims to be a friendly, portable C implementation of the AV1 Image
File Format, as described here:

https://aomediacodec.github.io/av1-avif/

%prep
%autosetup -p1 -n libavif-%{version}

%build
%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    %{?with_aom:-DAVIF_CODEC_AOM=1} \
    -DAVIF_CODEC_DAV1D=1 \
    -DAVIF_CODEC_RAV1E=1 \
    %{?with_svt:-DAVIF_CODEC_SVT=1} \
    -DAVIF_BUILD_APPS=0 \
    -DAVIF_BUILD_GDK_PIXBUF=0
%cmake_build

%install
%cmake_install

# Remove devel files that we don't need for the compat package
rm -rfv $RPM_BUILD_ROOT%{_libdir}/libavif.so
rm -rfv $RPM_BUILD_ROOT%{_includedir}/avif/
rm -rfv $RPM_BUILD_ROOT%{_libdir}/cmake/libavif/
rm -rfv $RPM_BUILD_ROOT%{_libdir}/pkgconfig/libavif.pc

%files
%license LICENSE
# Do not glob the soname
%{_libdir}/libavif.so.14*

%changelog
%autochangelog
