%define _legacy_common_support 1
Name:           MagicPoint
Version:        1.13a
Release:        41%{?dist}
Summary:        X based presentation software
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://member.wide.ad.jp/wg/mgp/
Source0:        ftp://sh.wide.ad.jp/WIDE/free-ware/mgp/magicpoint-%{version}.tar.gz
Patch0:         magicpoint-1.11b-debian.patch
Patch1:         magicpoint-1.11b-64bit.patch
Patch2:         magicpoint-1.11b-embed.patch
Patch3:         magicpoint-1.13a-gcc-warnings.patch
Patch4:         magicpoint-1.13a-xwintoppm.patch
Patch5:         magicpoint-1.13a-no-m17n-config.patch
Patch6:         magicpoint-1.13a-mng.patch
Patch7:         magicpoint-1.13a-honor-cflags-for-unimap.patch
# giflib-5.x compatibility
Patch8:         magicpoint-1.13a-giflib5.patch
# libpng > 1.5.0 compatibility
Patch9:         magicpoint-1.13a-libpng.patch
Patch10:        magicpoint-1.13a-libmng-lib64.patch
Patch11: MagicPoint-c99.patch
BuildRequires:  make gcc
BuildRequires:  giflib-devel libpng-devel libmng-devel fontconfig-devel 
BuildRequires:  libXmu-devel libXft-devel m17n-lib-devel
BuildRequires:  imake bison flex perl-interpreter perl-generators sharutils
Requires:       sharutils
Obsoletes:      mgp < %{version}-%{release}, magicpoint < %{version}-%{release}
Provides:       mgp = %{version}-%{release}, magicpoint = %{version}-%{release}

%description
MagicPoint is an X11 based presentation tool. MagicPoint's
presentation files (typically .mgp files) are plain text so you can
create presentation files quickly with your favorite editor.


%prep
%autosetup -p1 -n magicpoint-%{version}


%build
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Wno-pointer-sign -Wno-unused-variable -Wno-unused-but-set-variable -Wno-unused-function -D_DEFAULT_SOURCE"
export CFLAGS="$RPM_OPT_FLAGS"
# Stop configure from checking for non-existing m17n-config shell script
export HAVE_M17NLIB="yes"
%configure --enable-locale --enable-xft2 --enable-gif --with-m17n-lib
xmkmf -a
# LIBDIR is used by the makefile to determine where to install data files
make CDEBUGFLAGS="$RPM_OPT_FLAGS" EXTRA_LDOPTIONS="$LDFLAGS" LIBDIR=%{_datadir}


%install
make install install.man DESTDIR=$RPM_BUILD_ROOT LIBDIR=%{_datadir}
install -m 755 contrib/mgp2html.pl $RPM_BUILD_ROOT%{_bindir}/mgp2html
install -m 755 contrib/mgp2latex.pl $RPM_BUILD_ROOT%{_bindir}/mgp2latex
# stop these from ending up in %%doc
rm sample/.cvsignore sample/*akefile*


%files
%doc README SYNTAX USAGE sample
%license COPYRIGHT
%{_bindir}/*
%{_datadir}/mgp
%{_mandir}/*/*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.13a-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.13a-40
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.13a-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Apr 22 2024 Hans de Goede <hdegoede@redhat.com> - 1.13a-38
- Fix binaries not being PIE
- Fix FTBFS
- Resolves: rhbz#2260962

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.13a-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.13a-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.13a-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Apr 11 2023 Florian Weimer <fweimer@redhat.com> - 1.13a-34
- Port to C99 (#2185873)

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.13a-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.13a-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.13a-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.13a-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Feb 15 2021 Hans de Goede <hdegoede@redhat.com> - 1.13a-29
- Fix FTBFS (rhbz1923401)
- Drop Imlib support, only works with obsolete Imlib1
- Fix m17n support
- Fix libmng support on lib64 using arches

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.13a-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.13a-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 16 2020 Jeff Law <law@redhat.com> - 1.13a-26
- Enable legacy common support

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.13a-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.13a-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.13a-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.13a-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 1.13a-21
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Sun Feb 11 2018 Sandro Mani <manisandro@gmail.com> - 1.13a-20
- Rebuild (giflib)
- Switch to imlib2
