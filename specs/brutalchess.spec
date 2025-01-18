%global pre     alpha

Name:           brutalchess
Version:        0.5.2
Release:        0.31.%{pre}%{?dist}
Summary:        Chess game with impressive 3D graphics

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://sf.net/projects/%{name}
# we don't want the original fonts due to legal reasoning
# http://sf.net/projects/%{name}/files/%{name}-%{pre}/%{name}-%{pre}-%{version}/%{name}-%{pre}-%{version}-src.tar.gz
Source0:        %{name}-%{pre}-%{version}-nofonts.tar.xz
Source1:        %{name}-nofonts.sh

Patch0:         https://sf.net/p/%{name}/patches/8/attachment/%{name}-freetype2.patch
# fonts: https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=584416
Patch1:         https://sf.net/p/%{name}/patches/7/attachment/%{name}-fonts.diff

# PGN resembling console output, http://sourceforge.net/p/brutalchess/patches/3
Patch2:         http://sf.net/p/%{name}/patches/_discuss/thread/96f1a752/0dc4/attachment/pgn-moveprint.diff
# Fix -l option, http://sourceforge.net/p/brutalchess/patches/2
Patch3:         http://sf.net/p/%{name}/patches/_discuss/thread/b91b1843/e6b7/attachment/fix-player2opt.diff

# FIXME crafty, https://sf.net/p/brutalchess/patches/4
# patch can't be applied cause of any potential security risk, there is currently no crafty package in Fedora

# extensions from slack to let the package actually be usable and build
Source10:       http://slackbuilds.org/slackbuilds/14.1/games/%{name}/%{name}.desktop
Source11:       http://slackbuilds.org/slackbuilds/14.1/games/%{name}/%{name}.png
Patch10:        http://slackbuilds.org/slackbuilds/14.1/games/%{name}/%{name}-%{version}-fix-FTBFS.patch
Patch11:        http://slackbuilds.org/slackbuilds/14.1/games/%{name}/%{name}-%{version}-gcc4.3.patch
Patch12:        http://slackbuilds.org/slackbuilds/14.1/games/%{name}/%{name}-%{version}-gcc4.7.patch

# disable feature: quake pieces are not available, http://bugs.debian.org/732227
Patch20:        brutalchess-noquake.patch

BuildRequires:  gcc-c++
BuildRequires:  SDL-devel SDL_image-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  freetype-devel
BuildRequires:  doxygen
BuildRequires:  desktop-file-utils
BuildRequires: make

Requires:       gnu-free-sans-fonts

# -doc subpkg was < 100k, not worth splitting out (yet) -- rex
Obsoletes: brutalchess-doc < 0.5.2-0.4
Provides:  %{name}-doc = %{version}-%{release}

%description
BrutalChess features full 3D graphics, an advanced particle engine, 
and several different levels of intelligent AI, inspired by the once 
popular "Battle Chess" released by Interplay circa 1988.


%prep
%setup -q
%patch -P0 -p0
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P10
%patch -P11
%patch -P12 -p1
%patch -P20 -p1
# update Doxyfile
doxygen -u
# proper font license
sed -i s,fonts,, Makefile.in
sed -i 's,\(fontsdir=\).*,\1"\${datadir}/fonts/",' configure
sed -i s,ZEROES__.TTF,gnu-free/FreeSans.ttf, src/gamecore.cpp
# W: wrong-file-end-of-line-encoding
sed -i 's/\r$//' NEWS README


%build
%configure
make %{?_smp_mflags}
doxygen


%install
%make_install

# misplaced content
rm -rv %{buildroot}%{_datadir}/%{name}/doc

# desktop
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE10}
install -d %{buildroot}%{_datadir}/pixmaps
cp -p %{SOURCE11} %{buildroot}%{_datadir}/pixmaps


%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%doc doc/html
%{_bindir}/*
%{_libexecdir}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/%{name}/


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-0.31.alpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.5.2-0.30.alpha
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-0.29.alpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-0.28.alpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-0.27.alpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-0.26.alpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-0.25.alpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-0.24.alpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-0.23.alpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-0.22.alpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-0.21.alpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-0.20.alpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-0.19.alpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-0.18.alpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-0.17.alpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 08 2018 Raphael Groner <projects.rg@smart.ms> - 0.5.2-0.16.alpha
- mesa header moved to another subpackage, rhbz#1551313

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-0.15.alpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-0.14.alpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-0.13.alpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-0.12.alpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-0.11.alpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-0.10.alpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-0.9.alpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.5.2-0.8.alpha
- Rebuilt for GCC 5 C++11 ABI change

* Mon Feb 09 2015 Raphael Groner <projects.rg (AT) smart.ms> - 0.5.2-0.7.alpha
- apply patches from upstream tracker: PGN, -l option

* Wed Jan 28 2015 Raphael Groner <projects.rg [AT] smart.ms> - 0.5.2-0.6.alpha
- introduce license macro

* Mon Dec 29 2014 Raphael Groner <projects.rg [AT] smart.ms> - 0.5.2-0.5.alpha
- remove wrong and improve fonts logic
- general files section
- remove useless title macro
- add noquake patch
- preserve timestamps of doc files
- remove confusing with-x flag

* Sun Dec 28 2014 Rex Dieter <rdieter@fedoraproject.org> - 0.5.2-0.4.alpha
- drop -doc subpkg (too small, not worth it)
- omit non-html doc generation
- add deps for font pkgs used

* Mon Dec 15 2014 Rex Dieter <rdieter@fedoraproject.org> 0.5.2-0.3.alpha
- fix Release: tag

* Fri Dec 12 2014 Raphael Groner <projects.rg [AT] smart.ms> - 0.5.2-3.alpha
- fixes for review

* Thu Dec 11 2014 Raphael Groner <projects.rg [AT] smart.ms> - 0.5.2-2.alpha
- fix broken BR for Xorg
- remove subpackages
- additional doc package

* Sat Oct 25 2014 Raphael Groner <projects.rg [AT] smart.ms> - 0.5.2-1.alpha
- original by Timur Kristóf (rhbz #701812)
- desktop stuff and gcc patches from Slackware
- link freetype2 properly
- replace fonts, patch adopted from Debian
- macro title in description
- enhance documentation with doxygen and latex
