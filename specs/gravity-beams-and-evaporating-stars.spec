%global repo_owner  dextero
%global repo_name   LD30

Name: gravity-beams-and-evaporating-stars
%global shortname %(echo "%{name}" | sed -e 's:\\([a-z]\\)[a-z]*:\\1:g' -e 's:-::g')

Version: 1.0
Release: 20%{?dist}
Summary: A game about hurling asteroids into the sun
License: MIT

URL:     https://github.com/%{repo_owner}/%{repo_name}
Source0: %{URL}/archive/%{version}/%{repo_name}-%{version}.tar.gz

Patch0: %{shortname}--chdir-at-game-start.patch
Patch1: %{shortname}--store-hiscores-in-XDG_DATA_HOME.patch

BuildRequires: cmake > 3.1
BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: libappstream-glib
BuildRequires: make
BuildRequires: SFML-devel

Requires: hicolor-icon-theme

%global fontlist font(dejavusans)
BuildRequires: fontconfig
BuildRequires: %{fontlist}
Requires: %{fontlist}


%description
You are a lone planet whose star is dying. Use your gravity beams to hurl
nearby asteroids into the star, feeding it some extra matter.
While saving the star, be sure to avoid being hit by the asteroids yourself.


%prep
%autosetup -p1 -n %{repo_name}-%{version}

# Inject the RPM data dir
sed -e 's|__DATA_DIR__|"%{_datadir}/%{name}"|' -i src/main.cpp


%build
%cmake
%cmake_build


%install
install -m 755 -d %{buildroot}%{_bindir}
install -m 755 bin/game %{buildroot}%{_bindir}/%{name}

install -m 755 -d %{buildroot}%{_datadir}/%{name}
cp -a data %{buildroot}%{_datadir}/%{name}/data

# Replace the bundled DejaVuSans font
# with a symlink to the system-provided one
ln -sf \
  $(fc-match -f "%%{file}\n" "DejaVu Sans") \
  %{buildroot}%{_datadir}/%{name}/data/DejaVuSans.ttf

install -m 755 -d %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/
install -m 644 -p \
  data/planet.png \
  %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

install -m 755 -d %{buildroot}%{_datadir}/applications/
install -m 644 \
  packaging/%{name}.desktop \
  %{buildroot}%{_datadir}/applications/

install -m 755 -d %{buildroot}%{_datadir}/metainfo/
install -m 644 -p \
  packaging/%{name}.appdata.xml \
  %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml

install -m 755 -d %{buildroot}%{_mandir}/man1/
install -m 644 -p \
  packaging/%{name}.man \
  %{buildroot}%{_mandir}/man1/%{name}.1


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet packaging/%{name}.appdata.xml


%files
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/metainfo/%{name}.appdata.xml
%{_mandir}/man1/%{name}.*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Nov 05 2023 Sérgio Basto <sergio@serjux.com> - 1.0-16
- Rebuild for SFML-2.6.1

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.0-13
- Fix CMake-related FTBFS

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Artur Iwicki <fedora@svgames.pl> - 1.0-8
- Update spec to work properly with new cmake macros

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 30 2020 Artur Iwicki <fedora@svgames.pl> - 1.0-6
- Modify Patch1 (store hiscores in XDG_DATA_DIR) - should fix crashes on Game Over

* Thu May 14 2020 Artur Iwicki <fedora@svgames.pl> - 1.0-5
- Add a BuildRequires: on font-config
- Use fc-match to find the system fonts, instead of using hard-coded paths
- Move desktop file and AppStream validation to %%check

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 22 2018 Artur Iwicki <fedora@svgames.pl> - 1.0-1
- Update to new upstream version

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-6.20180114git3f2aa58
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr 06 2018 Artur Iwicki <fedora@svgames.pl> - 0.5-20180114git3f2aa58
- Use the %%cmake macro during %%build
- Remove executable bit from man page

* Wed Apr 04 2018 Artur Iwicki <fedora@svgames.pl> - 0.4-20180114git3f2aa58
- Update to new upstream snapshot
- Remove Source1, Source2 and Source3 - files accepted upstream
- Move the appdata file from appdata/ to metainfo/
- Use a patch file to make the game chdir() at start (instead of sed wizardry)

* Tue Apr 03 2018 Artur Iwicki <fedora@svgames.pl> - 0-3.20180110git727d759
- Add a patch to store the game hi-scores in XDG_DATA_HOME

* Sun Jan 14 2018 Artur Iwicki <fedora@svgames.pl> - 0-2.20180110git727d759
- Add man page, desktop and appdata files

* Thu Jan 11 2018 Artur Iwicki <fedora@svgames.pl> - 0-1.20180110git727d759
- Initial packaging
