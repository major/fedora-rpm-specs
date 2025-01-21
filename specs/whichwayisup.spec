%global pkgversion %(echo %version|sed s/\\\\\.//g) 

Name:           whichwayisup
Version:        0.7.9
Release:        23%{?dist}
Summary:        2D platform game with a slight rotational twist

# All game content, sounds and graphics are licensed under
# Creative Commons 3.0 Attribution license.
# Automatically converted from old format: GPLv2 and CC-BY - review is highly recommended.
License:        GPL-2.0-only AND LicenseRef-Callaway-CC-BY
URL:            http://www.oletus.fi/static/whichwayisup/
Source0:        http://www.oletus.fi/static/whichwayisup/%{name}_b%{pkgversion}.zip
# Desktop file taken from Debian
Source1:        %{name}.desktop
# AppData file provided by Iwicki Artur
Source2:        %{name}.appdata.xml
# Man page taken from Debian
Source3:        %{name}.6
# Under certain circumstances whichwayisup detected keyboards as joysticks
# http://bugs.debian.org/710162
Patch0:         %{name}-0.7.9-check_for_joystick_axes_not_null.patch
# Initialize only required pygame modules
# http://bugs.debian.org/432015
Patch1:         %{name}-0.7.9-initialize_only_required_pygame_modules.patch
# Port game to python3
# https://bugs.debian.org/912500
Patch2:         %{name}-0.7.9-python3.patch

BuildArch:      noarch

BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
Requires:       python3-pygame
Requires:       bitstream-vera-sans-fonts
Requires:       hicolor-icon-theme

%description
A traditional and challenging 2D platform game with a slight rotational 
twist. Help a mysterious big-eared salaryman named Guy find his keys in a 
labyrinth of dangers and bad dialogue.

%prep
%autosetup -n %{name} -p1

# Fix script interpreter
sed -i 's!/usr/bin/env python3!/usr/bin/python3!' run_game.py

# Change data path
sed -i "s!libdir = .*!libdir = '%{_datadir}/%{name}/lib'!" run_game.py

# Fix end-of-line encoding
sed -i 's/\r//' changelog.txt

# Remove Thumbs.db
rm data/pictures/Thumbs.db


%build
# Empty


%install
# Install launcher script
install -d %{buildroot}%{_bindir}
install -m 755 -p run_game.py %{buildroot}%{_bindir}/%{name}

# Install game and data
install -d %{buildroot}%{_datadir}/%{name}
cp -pr data lib %{buildroot}%{_datadir}/%{name}

# Install icons
for i in 0 1 2 ; do
  px=$(expr 64 - ${i} \* 16)
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${px}x${px}/apps
  convert lib/whichway.ico[${i}] \
    %{buildroot}%{_datadir}/icons/hicolor/${px}x${px}/apps/%{name}.png
done

# Install desktop file
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE1}

# Install AppData file
install -d %{buildroot}%{_datadir}/metainfo
install -p -m 644 %{SOURCE2} %{buildroot}%{_datadir}/metainfo
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*.appdata.xml

# Install man page
install -d %{buildroot}%{_mandir}/man6
install -p -m 644 %{SOURCE3} %{buildroot}%{_mandir}/man6/

# Symlink system font
rm %{buildroot}%{_datadir}/%{name}/data/misc/Vera.ttf
ln -s %{_datadir}/fonts/bitstream-vera-sans-fonts/Vera.ttf \
    %{buildroot}%{_datadir}/%{name}/data/misc/Vera.ttf

%files
%doc README.txt changelog.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_metainfodir}/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man6/%{name}.6*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.7.9-22
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 23 2020 Andrea Musuruane <musuruan@gmail.com> - 0.7.9-12
- Fixed font path for F32+ (BZ #1836454)

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 Andrea Musuruane <musuruan@gmail.com> - 0.7.9-10
- Ported to python3 (BZ #1738142)

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Feb 24 2018 Andrea Musuruane <musuruan@gmail.com> - 0.7.9-6
- Used new AppData directory

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.9-4
- Remove obsolete scriptlets

* Sat Jul 08 2017 Andrea Musuruane <musuruan@gmail.com> - 0.7.9-3
- Added missing BR

* Mon Jun 26 2017 Andrea Musuruane <musuruan@gmail.com> - 0.7.9-2
- Removed wrapper script and changed data path in launcher script
- Added a patch from Debian to initialize only required pygame modules
- Added AppData file
- Removed Thumbs.db file (Windows Explorer thumbnail database)
- Fixed macro style
- Minor fixes

* Sun Jun 25 2017 Andrea Musuruane <musuruan@gmail.com> - 0.7.9-1
- First release

