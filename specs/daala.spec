%global commit 24f889aaabe33bc390b993d737d830b8dd367e61
%global date 20250205
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:       daala
Version:    0^%{date}git%{shortcommit}
Release:    %autorelease
Summary:    Daala video compression
# tools/daalainfo.c: GNU General Public License
# tools/jpegyuv.c: BSD 3-Clause License
# tools/upload.py: Apache License 2.0
# tools/yuvjpeg.c: BSD 3-Clause License
# include/daala/daala_integer.h: BSD 3-Clause License
# src/tests/test_coef_coder.c: GNU General Public License v2.0 or later
# The rest is BSD 2-Clause License
License:    BSD-2-Clause AND BSD-3-Clause AND Apache-2.0 AND GPL-1.0-or-later
URL:        http://xiph.org/daala/

Source0:    https://gitlab.xiph.org/xiph/daala/-/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(check) >= 0.9.8
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(ogg) >= 1.3
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  wxGTK-devel

%description
A new video compression technology. The goal of the project is to provide a
video format that's free to implement, use and distribute, and a reference
implementation with technical performance superior to H.265.

%package    libs
Summary:    Daala video codec libraries

%description libs
A new video compression technology. The goal of the project is to provide a
video format that's free to implement, use and distribute, and a reference
implementation with technical performance superior to H.265.

%package    devel
Summary:    Development files for the Daala video codec libraries
Requires:   %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%package    tools
Summary:    Daala video codec tools

%description tools
A new video compression technology. The goal of the project is to provide a
video format that's free to implement, use and distribute, and a reference
implementation with technical performance superior to H.265.

The %{name}-tools package contains a test player and encoder plus programs for
testing %{name} support in your applications.

%prep
%autosetup -n %{name}-%{commit}

%build
autoreconf -vif
%configure \
    --disable-silent-rules \
    --disable-static \
    --enable-analyzer \
    --enable-float-pvq \
    --enable-tools

%make_build
%make_build tools

%install
%make_install
find %{buildroot} -name "*.la" -delete

# Install tools (list from tools_TARGETS in Makefile.am)
mkdir -p %{buildroot}%{_bindir}
install -m 755 -p \
    tools/bjontegaard \
    tools/block_size_analysis \
    tools/compute_basis \
    tools/compute_haar_basis \
    tools/cos_search \
    tools/divu_const \
    tools/downsample \
    tools/draw_zigzags \
    tools/dump_fastssim \
    tools/dump_msssim \
    tools/dump_psnr \
    tools/dump_psnrhvs \
    tools/dump_ssim \
    tools/gen_cdf \
    tools/gen_laplace_tables \
    tools/gen_sqrt_tbl \
    tools/jpegyuv \
    tools/.libs/daalainfo \
    tools/png2y4m \
    tools/to_monochrome \
    tools/trans2d \
    tools/trans_gain \
    tools/upsample \
    tools/vq_train \
    tools/y4m2png \
    tools/y4m2yuv \
    tools/yuv2yuv4mpeg \
    tools/yuvjpeg \
    %{buildroot}%{_bindir}/

# Let rpm pick up the docs in the files section
rm -fr %{buildroot}/%{_docdir}

# Install man pages
mkdir -p %{buildroot}/%{_mandir}
cp -fr doc/man/man3/ %{buildroot}/%{_mandir}
rm -f %{buildroot}/%{_mandir}/man3/_*_include_daala_.3

%check
# Tests are incredibly long, disable for now
make V=0 check

%files libs
%license COPYING
%doc AUTHORS
%{_libdir}/libdaalabase.so.0
%{_libdir}/libdaalabase.so.0.0.1
%{_libdir}/libdaaladec.so.0
%{_libdir}/libdaaladec.so.0.0.1
%{_libdir}/libdaalaenc.so.0
%{_libdir}/libdaalaenc.so.0.0.1

%files devel
%doc doc/html
%{_libdir}/libdaalabase.so
%{_libdir}/libdaaladec.so
%{_libdir}/libdaalaenc.so
%{_libdir}/pkgconfig/daaladec.pc
%{_libdir}/pkgconfig/daalaenc.pc
%{_includedir}/%{name}/
%{_mandir}/man3/*

%files tools
%{_bindir}/*

%changelog
%autochangelog
