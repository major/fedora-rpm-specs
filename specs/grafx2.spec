%global recoilver 6.1.0
%global sixfivezerotwover 0.1

Name:		grafx2
Version:	2.8
Release:	11%{?dist}
Summary:	A bitmap paint program specialized in 256 color drawing
URL:		http://grafx2.chez.com/
# recoil is GPLv2+, grafX2 is GPLv2 only
# two files are CeCILL v2
# 6502 has license permission to be used as GPLv2 in this program, see 6502-RELICENSE
# src/libraw2crtc.*
License:	GPL-2.0-only AND CECILL-2.0
# Source0:	https://gitlab.com/GrafX2/grafX2/-/archive/v%%{version}/grafX2-v%%{version}.tar.bz2
# We need to remove src/realpath.c as there is no license for it.
Source0:	grafX2-v%{version}-clean.tar.bz2
Source1:	https://sourceforge.net/projects/recoil/files/recoil/%{recoilver}/recoil-%{recoilver}.tar.gz
Source2:	grafx2.appdata.xml
Source3:	https://github.com/redcode/6502/releases/download/v%{sixfivezerotwover}/6502-v%{sixfivezerotwover}.tar.xz
# http://pulkomandy.tk/projects/GrafX2/ticket/162
Source4:	6502-RELICENSE
# Replacement file for unlicensed realpath.c
Source5:	realpath-linux.c
Patch0:		grafX2-v2.8-recoil6.patch
# https://gitlab.com/GrafX2/grafX2/-/commit/103fc6bd49ac5e4c34013f056f441686a6c0c019
# https://gitlab.com/GrafX2/grafX2/-/commit/77f24ad3a435a59e5e8a44716cc766f81ab46b23
Patch1:		grafX2-v2.8-fix-tiff-saving.patch
# https://gitlab.com/GrafX2/grafX2/-/commit/7e5daa65a8699f6640bf51272c925f4307164f9f
Patch2:		grafX2-v2.8-fix-ttf.patch
# https://gitlab.com/GrafX2/grafX2/-/commit/a851e49f861c7b9bdf1b89c0dd55b8fc12676009
Patch3:		grafX2-v2.8-fix-coords.patch
BuildRequires:	SDL2-devel, SDL2_image-devel, SDL2_ttf-devel, zlib-devel, libtiff-devel
BuildRequires:	libpng-devel, freetype-devel, libX11-devel, lua-devel, gcc, make
BuildRequires:	fontconfig-devel, desktop-file-utils
Provides:	bundled(recoil) = %{recoilver}
Provides:	bundled(6502) = %{sixfivezerotwover}

%description
GrafX2 is a bitmap paint program inspired by the Amiga programs ​Deluxe Paint
and Brilliance. Specialized in 256-color drawing, it includes a very large
number of tools and effects that make it particularly suitable for pixel
art, game graphics, and generally any detailed graphics painted with a
mouse.

%prep
%setup -q -n grafX2-v%{version}
%patch -P0 -p1 -b .r6
%patch -P1 -p1 -b .fix-tiff-saving
%patch -P2 -p1 -b .ttf-fix
%patch -P3 -p1 -b .fix-coords

cp %{SOURCE5} src/realpath.c

sed -i 's|-O$(OPTIM)|%{optflags}|g' src/Makefile
sed -i 's|$(LUALOPT)|$(LUALOPT) %{build_ldflags}|g' src/Makefile

# Use the newer recoil
sed -i 's|RECOILVER = 5.1.1|RECOILVER = %{recoilver}|g' src/Makefile
sed -i 's|RECOILVER=5.1.1|RECOILVER=%{recoilver}|g' 3rdparty/Makefile

cp %{SOURCE4} .

mkdir -p 3rdparty/archives/
cp -a %{SOURCE1} %{SOURCE3} 3rdparty/archives/

%build
cd src
make %{?_smp_mflags} API=sdl2

%install
cd src
make API=sdl2 DESTDIR=%{buildroot} PREFIX=%{_prefix} CP="cp -a" install

# install appdata file
mkdir -p %{buildroot}%{_metainfodir}
cp %{SOURCE2} %{buildroot}%{_metainfodir}

pushd %{buildroot}%{_bindir}
ln -s grafx2-sdl2 grafx2
popd

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/grafx2.desktop

%files
%license LICENSE 6502-RELICENSE
%doc doc/README.txt doc/quickstart.rtf
%{_bindir}/grafx2*
%{_metainfodir}/grafx2.appdata.xml
%{_datadir}/applications/grafx2.desktop
%{_datadir}/grafx2/
%{_datadir}/icons/hicolor/scalable/apps/*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 29 2022 Tom Callaway <spot@fedoraproject.org> - 2.8-5
- merge in some upstream fixes
- use SDL2

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Apr 21 2021 Tom Callaway <spot@fedoraproject.org> - 2.8-1
- update to 2.8

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 25 2021 Tom Callaway <spot@fedoraproject.org> - 2.7-1
- update to 2.7

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 13 2018 Tom Callaway <spot@fedoraproject.org> - 2.5-2
- fix license tag
- add appdata file
- comment patches

* Tue Jun 12 2018 Tom Callaway <spot@fedoraproject.org> - 2.5-1
- initial package
