Name:           flobopuyo
Version:        0.20
Release:        42%{?dist}
Summary:        2-player falling bubbles game

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.fovea.cc/flobopuyo-en
Source0:        http://www.fovea.cc/files/flobopuyo/%{name}-%{version}.tgz
Source1:        %{name}.desktop
Source2:        %{name}.appdata.xml
# Fix building on 64bit
# Patch by Michael Thomas aka Wart <wart at kobold dot org>
# https://lists.fedoraproject.org/archives/list/games@lists.fedoraproject.org/thread/ECMVJBXDAITOV35723OMGQSF3CLXKLZK/
Patch0:         %{name}-0.20-64bit.patch
# Patch by Andrea Musuruane
Patch1:         %{name}-0.20-Makefile.patch
# Fix segfaults on Fedora 24
# Patches by Sebastian Ott
# https://bugzilla.redhat.com/show_bug.cgi?id=1352557
# https://bugzilla.redhat.com/show_bug.cgi?id=1380525
Patch2:         %{name}-0.20-segfaults.patch
# Set proper window title
# https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=537352
Patch3:         %{name}-0.20-set_window_title.patch
# Fix a typo
# Patch taken from Debian
Patch4:         %{name}-0.20-fix_typo.patch

BuildRequires:  gcc-c++
BuildRequires:  flex 
BuildRequires:  bison 
BuildRequires:  SDL_mixer-devel 
BuildRequires:  SDL_image-devel 
BuildRequires:  libicns-utils
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
BuildRequires: make
Requires:       hicolor-icon-theme


%description
A two-player falling bubbles game.  The goal is to make groups of four or more
Puyos (colored bubbles) to make them explode and send bad ghost Puyos to your
opponent.  You win the game if your opponent reaches the top of the board. You
can play against computer or another human.


%prep
%setup -q
%patch -P0 -p0
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p0

# Fix end-of-line-encoding
sed -i 's/\r//' COPYING

# Remove AppleDouble files
rm data/sfx/._bi


%build
%set_build_flags macro
# It does not support parallel building
make PREFIX=%{_prefix}


%install
%make_install PREFIX=%{_prefix}

# Install man page
install -d -m 755 %{buildroot}%{_mandir}/man6
install -p -m 644 man/%{name}.6 %{buildroot}%{_mandir}/man6

# Install desktop file
desktop-file-install \
        --dir %{buildroot}%{_datadir}/applications \
        %{SOURCE1}

# Extract Mac OS X icons
icns2png -x mac/icon.icns

# Install icon
install -d -m 755 %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/
install -p -m 644 icon_128x128x32.png \
  %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png

# Install appdata
install -d -m 755 %{buildroot}%{_datadir}/metainfo
install -p -m 644 %{SOURCE2} \
  %{buildroot}%{_datadir}/metainfo
appstream-util validate-relax --nonet \
  %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml


%files
%doc TODO Changelog
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/metainfo/%{name}.appdata.xml
%{_mandir}/man6/%{name}.6*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.20-41
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 08 2019 Andrea Musuruane <musuruan@gmail.com> - 0.20-28
- Fixed FTBFS
- Used %%set_build_flags macro
- Added appdata file

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 Andrea Musuruane <musuruan@gmail.com> - 0.20-25
- Added gcc-c++ dependency
- Fixed LDFLAGS usage

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.20-23
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Nov 12 2016 Andrea Musuruane <musuruan@gmail.com> - 0.20-19
- Updated the patch to fix segfaults on Fedora 24 (closes #1380525)

* Sat Jul 16 2016 Andrea Musuruane <musuruan@gmail.com> - 0.20-18
- Updated URL
- Updated Source0
- Dropped obsolete Group, Buildroot, %%clean and %%defattr
- Dropped cleaning at the beginning of %%install
- Updated icon cache scriptlets
- Added a patch to fix a segfault on Fedora 24 (closes #1352557)
- Added a patch from Debian to set proper window title
- Added a patch from Debian to fix a typo

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.20-15
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 15 2013 Jon Ciesla <limburgher@gmail.com> - 0.20-11
- Drop desktop vendor tag.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Mar 24 2008 Andrea Musuruane <musuruan@gmail.com> 0.20-4
- Reverted license to GPLv2+

* Sun Mar 23 2008 Andrea Musuruane <musuruan@gmail.com> 0.20-3
- Fixed License tag
- Improved macro usage

* Sun Feb 10 2008 Andrea Musuruane <musuruan@gmail.com> 0.20-2
- Fixed license
- Added a patch to fix Makefile
- Added hicolor-icon-theme to Requires
- Fixed desktop file
- Fixed desktop file install
- Used converted mac icon
- Updated icon cache scriptlets to be compliant to new guidelines
- Improved macro usage
- Installed man page
- Cosmetic changes

* Wed Aug 16 2006 Wart <wart at kobold dot ort> 0.20-1
- Initial package for Fedora
