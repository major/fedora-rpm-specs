%global waddir  %{_datadir}/doom

Name:           freedoom

Version:        0.13.0
Release:        3%{?dist}
Summary:        Doom styled first person shooter game

License:        BSD-3-Clause
URL:            https://freedoom.github.io/
Source0:        https://github.com/freedoom/freedoom/releases/download/v%{version}/freedoom-%{version}.zip
Source1:        freedoom1.desktop
Source2:        freedoom2.desktop
Source3:        freedoom.png
Source4:        freedoom1.appdata.xml
Source5:        freedoom2.appdata.xml

BuildArch:      noarch
BuildRequires:  desktop-file-utils libappstream-glib
Requires:       prboom hicolor-icon-theme

%description
Freedoom: Phase 1 is a Doom styled first person shooter game using the
Doom engine, featuring Four chapters, nine levels each, totalling 36
levels.

There is a massive back catalog, spanning over two decades, containing
thousands of Doom levels and other modifications (“mods”) made by fans
of the original Doom game. Freedoom aims to be compatible with these and
allows most to be played without the original Doom datafiles.
Freedoom: Phase 1 aims for compatibility with The Ultimate Doom,
also known as plain Doom or Doom 1. 


%package -n     freedoom2
Summary:        Doom2 styled first person shooter game
Requires:       prboom hicolor-icon-theme

%description -n freedoom2
Freedoom: Phase 2 is a Doom2 styled first person shooter game using the
Doom engine. Freedoom: Phase 2 has 32 levels in one long chapter,
featuring extra monsters and a double-barrelled shotgun.

There is a massive back catalog, spanning over two decades, containing
thousands of Doom levels and other modifications (“mods”) made by fans
of the original Doom game. Freedoom aims to be compatible with these and
allows most to be played without the original Doom datafiles.
Freedoom: Phase 2 aims for compatibility with Doom II and Final Doom.


%prep
%setup -q


%build
# Game data files.  Nothing to build!


%install
mkdir -p %{buildroot}/%{waddir}
install -p -m 0644 freedoom1.wad freedoom2.wad %{buildroot}/%{waddir}
desktop-file-install --dir %{buildroot}/%{_datadir}/applications %{SOURCE1}
desktop-file-install --dir %{buildroot}/%{_datadir}/applications %{SOURCE2}
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps/
install -p -m 644 %{SOURCE3} %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps/
mkdir -p %{buildroot}%{_datadir}/appdata
install -p -m 644 %{SOURCE4} %{SOURCE5} %{buildroot}%{_datadir}/appdata
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/*.xml
ln -s /usr/share/doom/freedoom2.wad %{buildroot}%{waddir}/freedoom.wad
# crete  cmdline launchers from desktop commands
mkdir -p %{buildroot}/%{_bindir}
echo "#!%{_bindir}/bash" > %{buildroot}/%{_bindir}/%{name}1
echo "#!%{_bindir}/bash" > %{buildroot}/%{_bindir}/%{name}2
cat  %{SOURCE1} | grep "Exec" | sed "s/Exec.//" >> %{buildroot}/%{_bindir}/%{name}1
cat  %{SOURCE2} | grep "Exec" | sed "s/Exec.//" >> %{buildroot}/%{_bindir}/%{name}2
chmod 755 %{buildroot}/%{_bindir}/%{name}1
chmod 755 %{buildroot}/%{_bindir}/%{name}2

%files
%doc README.html CREDITS.txt
%license COPYING.txt
%{waddir}/%{name}1.wad
%{_datadir}/appdata/%{name}1.appdata.xml
%{_datadir}/applications/%{name}1.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_bindir}/%{name}1

%files -n freedoom2
%doc README.html CREDITS.txt
%license COPYING.txt
%{waddir}/%{name}.wad
%{waddir}/%{name}2.wad
%{_datadir}/appdata/%{name}2.appdata.xml
%{_datadir}/applications/%{name}2.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_bindir}/%{name}2

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Feb 07 2024 Gwyn Ciesla <gwync@protonmail.com> - 0.13.0-1
- 0.13.0

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Mar 04 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.12.1-10
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Apr 07 2020 Jiri Vanek <jvanek@redhat.com> - 0.12.1-3
- added cmdline launchers

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 25 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.12.1-1
- 0.12.1

* Thu Oct 10 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.12.0-1
- 0.12.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.3-3
- Remove obsolete scriptlets

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 20 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.11.3-1
- 0.11.3.

* Tue May 23 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.11.2-1
- 0.11.2.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 01 2016 Jon Ciesla <limburgher@gmail.com> - 0.10.1-3
- Add symlink to fix third-party pwads.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 29 2016 Hans de Goede <hdegoede@redhat.com> - 0.10.1-1
- New upstream release 0.10.1 (rhbz#1295716)
- Split into freedoom and freedoom2 packages following upstream split of
  freedoom.wad into freedoom1.wad and freedoom2.wad (both are standalone
  playable games)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.7-7
- Add an AppData file for the software center

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Aug 26 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 0.7-1
- Update to latest upstream release
- No need to explicitly define buildroot, defattr or have a clean stage anymore
- Replace define with global as per current packaging guidelines
- Fix icon cache scriplets as per current packaging guidelines
- Fix the desktop file to follow the latest spec

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 26 2009 Wart <wart at kobold.org> 0.6.4-1
- Update to 0.6.4

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 22 2008 Wart <wart at kobold.org> 0.6.2-2
- Add coreutils requirement for rpm post scripts

* Wed Jun 4 2008 Wart <wart at kobold.org> 0.6.2-1
- Update to 0.6.2

* Sat Aug 11 2007 Wart <wart at kobold.org> 0.5-3
- Use correct .desktop file version

* Sat Mar 3 2007 Wart <wart at kobold.org> 0.5-2
- Use better sourceforge download url
- Use more precise desktop file categories

* Fri Sep 15 2006 Wart <wart at kobold.org> 0.5-1
- Update to 0.5

* Tue Mar 14 2006 Wart <wart at kobold.org> 0.4.1-3
- Use correct License: tag.
- Remove unnecessary comment.

* Mon Mar 13 2006 Wart <wart at kobold.org> 0.4.1-2
- Install wad in new location (see discussion on bz #185211)

* Sat Mar 11 2006 Wart <wart at kobold.org> 0.4.1-1
- Initial package for Fedora Extras
