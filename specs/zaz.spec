Name:           zaz
Version:        1.0.1
Release:        10%{?dist}
Summary:        A puzzle game where the player has to arrange balls in triplets

# Music released under CC-BY-SA
# Automatically converted from old format: GPLv3+ and CC-BY-SA - review is highly recommended.
License:        GPL-3.0-or-later AND LicenseRef-Callaway-CC-BY-SA
URL:            http://zaz.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# 128x128px icon by Zbigniew Jędrzejewski-Szmek
Source1:        %{name}.png
# Appdata by Richard Hughes
Source2:        %{name}.appdata.xml
# Debian man page
Source3:        %{name}.6
# Fix jumpy keyboard
# http://bugs.debian.org/649021
Patch0:         %{name}-1.0.0-jumpy_keyboard.patch
# Link with libvorbis
# https://bugs.debian.org/768718
Patch1:         %{name}-1.0.1-libvorbis.patch

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  mesa-libGL-devel
BuildRequires:  SDL_image-devel
BuildRequires:  libtheora-devel
BuildRequires:  libvorbis-devel
BuildRequires:  ftgl-devel >= 2.1.3
BuildRequires:  gettext
BuildRequires:  ImageMagick
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme
Requires:       gnu-free-mono-fonts
Requires:       gnu-free-sans-fonts
Requires:       oflb-dignas-handwriting-fonts


%description
Zaz is an arcade action puzzle game where the goal is to get rid of all 
incoming balls by rearranging their order and making triplets.

A 3D accelerator is needed for decent gameplay.


%prep
%autosetup -p1

# Fix permissions
chmod 644 src/*.{cpp,h}


%build
%configure
%make_build


%install
%make_install

# Symlink system fonts
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/FreeMonoBold.ttf
ln -s %{_datadir}/fonts/gnu-free/FreeMonoBold.ttf \
    $RPM_BUILD_ROOT%{_datadir}/%{name}/FreeMonoBold.ttf
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/FreeSans.ttf
ln -s %{_datadir}/fonts/gnu-free/FreeSans.ttf \
    $RPM_BUILD_ROOT%{_datadir}/%{name}/FreeSans.ttf
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/font1.ttf
ln -s %{_datadir}/fonts/oflb-dignas-handwriting/phranzysko_-_Digna_s_Handwriting.ttf \
    $RPM_BUILD_ROOT%{_datadir}/%{name}/font1.ttf

# Remove docs
rm -r $RPM_BUILD_ROOT/usr/share/doc/

# Remove obsolete pixmap
rm -rf $RPM_BUILD_ROOT%{_datadir}/pixmaps/

# Convert xpm icon to png to appease appdata
install -d $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
convert extra/%{name}.xpm \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps/%{name}.png

# Install 128x128px icon to appease appdata
install -d $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
install -p -m 0644 %{SOURCE1} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps

# Validate desktop file
desktop-file-validate \
   $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

# Install appdata
install -d $RPM_BUILD_ROOT%{_datadir}/metainfo
install -p -m 0644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/metainfo
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/metainfo/*.appdata.xml

# Install man page
install -d $RPM_BUILD_ROOT%{_mandir}/man6
install -p -m 0644 %{SOURCE3} $RPM_BUILD_ROOT%{_mandir}/man6/

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man6/*
%license COPYING data/copyright.txt
%doc AUTHORS ChangeLog


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.1-9
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 16 2021 Andrea Musuruane <musuruan@gmail.com> - 1.0.1-1
- Updated to new upstream release

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Feb 24 2018 Andrea Musuruane <musuruan@gmail.com> - 1.0.0-23
- Added gcc dependency
- Added a patch from Debian to link libvorbis
- Used new AppData directory
- Spec file clean up

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.0-21
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 03 2016 Andrea Musuruane <musuruan@gmail.com> - 1.0.0-15
- Fixed upstream homepage
- Added patches from Debian
- Added man page from Debian
- Added appdata thanks to Richard Hughes (#1185980)
- Added 128x128px icon thanks to Zbigniew Jędrzejewski-Szmek (#1185980)
- Spec file cleanup

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.0-13
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1.0.0-12
- Add an AppData file for the software center

* Fri Dec 19 2014 Andrea Musuruane <musuruan@gmail.com> - 1.0.0-11
- Converted xpm icon to png to appease appdata (#1175972)

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 14 2014 Andrea Musuruane <musuruan@gmail.com> - 1.0.0-9
- Fix FTBFS (#510432)
- Dropped obsolete Group, Buildroot, %%clean and %%defattr

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-4
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Sep 04 2010 Andrea Musuruane <musuruan@gmail.com> 1.0.0-1
- Updated to upstream 1.0.0

* Thu Jul 22 2010 Andrea Musuruane <musuruan@gmail.com> 0.8.0-1
- Updated to upstream 0.8.0

* Sat May 08 2010 Andrea Musuruane <musuruan@gmail.com> 0.7.0-1
- Updated to upstream 0.7.0

* Thu Feb 25 2010 Andrea Musuruane <musuruan@gmail.com> 0.3.3-1
- Updated to upstream 0.3.3

* Tue Dec 22 2009 Andrea Musuruane <musuruan@gmail.com> 0.3.0-3
- Consistent use of macros
- Fixed typo

* Wed Dec 09 2009 Andrea Musuruane <musuruan@gmail.com> 0.3.0-2
- Now Requires renamed Digna font package (BZ #542461)

* Sun Nov 29 2009 Andrea Musuruane <musuruan@gmail.com> 0.3.0-1
- First release

