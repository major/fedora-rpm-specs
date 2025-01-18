%global commit0 694d4ced7e97f349cd4f54dbfc8c8a69982a54e4
%global date 20200724
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:       daala
Version:    0
Release:    30%{?shortcommit0:.%{date}git%{shortcommit0}}%{?dist}
Summary:    Daala video compression
# Automatically converted from old format: BSD - review is highly recommended.
License:    LicenseRef-Callaway-BSD
URL:        http://xiph.org/daala/

Source0:    https://gitlab.xiph.org/xiph/%{name}/-/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz

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
%autosetup -n %{name}-%{commit0}

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
#make V=0 check

%ldconfig_scriptlets libs

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
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0-30.20200724git694d4ce
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 0-29.20200724git694d4ce
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-28.20200724git694d4ce
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-27.20200724git694d4ce
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-26.20200724git694d4ce
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-25.20200724git694d4ce
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2022 Scott Talbert <swt@techie.net> - 0-24.20200724git694d4ce
- Rebuild with wxWidgets 3.2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-23.20200724git694d4ce
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-22.20200724git694d4ce
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu May 05 2022 Simone Caronni <negativo17@gmail.com> - 0-21.20200724git694d4ce
- Update to latest snapshot.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-20.20200512git0b5ce2f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-19.20200512git0b5ce2f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-18.20200512git0b5ce2f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-17.20200512git0b5ce2f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 15 2020 Simone Caronni <negativo17@gmail.com> - 0-16.20200512git0b5ce2f
- Do not install trans command.

* Tue Jul 14 2020 Simone Caronni <negativo17@gmail.com> - 0-15.20200512git0b5ce2f
- Update to latest snapshot.
- Update SPEC file.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-14.20170616git7278368
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-13.20170616git7278368
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-12.20170616git7278368
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-11.20170616git7278368
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 04 2018 Scott Talbert <swt@techie.net> - 0-10.20170616git7278368
- Rebuild with wxWidgets 3.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-9.20170616git7278368
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 11 2017 Simone Caronni <negativo17@gmail.com> - 0-8.20170616git7278368
- Update to latest snapshot.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-7.20170324gitee07b32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-6.20170324gitee07b32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 30 2017 Simone Caronni <negativo17@gmail.com> - 0-5.20170324gitee07b32
- Update to latest snapshot.
- Make build verbose.
- Add tests, disable them for now as they are incredibly long (30 minutes).
- Fix daalainfo.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-4.20161216git28de40b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 17 2016 Simone Caronni <negativo17@gmail.com> - 0-3.20161216git28de40b
- Update to latest snapshot.
- Add docs and enable building of tools.

* Fri Nov 25 2016 Simone Caronni <negativo17@gmail.com> - 0-2.20161117git4eddbab
- Update to latest snapshot.
- Use make_build macro, license macro.

* Fri Nov 18 2016 Simone Caronni <negativo17@gmail.com> - 0-1.20161114git4403315
- First build.

