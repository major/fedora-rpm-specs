%global fonts font(freesans) font(freeserif)

Name:           trackballs
Version:        1.3.4
Release:        2%{?dist}
Summary:        Steer a marble ball through a labyrinth
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://trackballs.github.io/
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++ cmake
BuildRequires:  guile30-devel SDL2-devel SDL2_image-devel SDL2_mixer-devel
BuildRequires:  SDL2_ttf-devel zlib-devel libglvnd-devel gettext
BuildRequires:  desktop-file-utils libappstream-glib
BuildRequires:  fontconfig %{fonts}
Requires:       %{fonts}

%description
Trackballs is a game in which you steer a marble ball through tracks of varying
difficulty. The game features 3D graphics, an integrated level editor and high
quality sound effects and background music.


%prep
%setup -q
iconv -f ISO-8859-1 -t UTF8 share/%{name}.6 > share/%{name}.6.tmp
touch -r share/%{name}.6 share/%{name}.6.tmp
mv share/%{name}.6.tmp share/%{name}.6


%build
%cmake
%cmake_build


%install
%cmake_install
%find_lang %{name}

# Replace bundled fonts with symlinks to system fonts
ln -sf $(fc-match -f "%{file}" "freeserif:bold:italic") \
  $RPM_BUILD_ROOT%{_datadir}/trackballs/fonts/FreeSerifBoldItalic.ttf
ln -sf $(fc-match -f "%{file}" "freesans:bold") \
  $RPM_BUILD_ROOT%{_datadir}/trackballs/fonts/menuFont.ttf

mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
mv $RPM_BUILD_ROOT/%{_datadir}/metainfo/trackballs.appdata.xml \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop


%check
%ctest


%files -f %{name}.lang
%doc AUTHORS.md FAQ.md README.md
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man6/%{name}.6.gz
%{_docdir}/%{name}/*.html
%{_docdir}/%{name}/*.css
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/*/apps/%{name}.svg
%{_datadir}/appdata/%{name}.appdata.xml

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jul 30 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 1.3.4-1
- Update to 1.3.4
- Build against guile 3.x

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.3.1-11
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 20 2020 Tomas Korbar <tkorbar@redhat.com> - 1.3.1-1
- Rebase to 1.3.1 (rhbz#1510133)
- New Upstream (rhbz#1821064)
- Fix broken symlinks to system-fonts (rhbz#1821062)
- Use GNU Free fonts instead of Dejavu, matching the upstream bundled fonts

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.4-31
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Feb 22 2016 Hans de Goede <hdegoede@redhat.com> - 1.1.4-27
- Fix FTBFS (rhbz#1308193)
- Add appdata

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.1.4-24
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 16 2014 Hans de Goede <hdegoede@redhat.com> - 1.1.4-22
- Fix FTBFS (rhbz#1037364)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 12 2013 Jon Ciesla <limburgher@gmail.com> - 1.1.4-19
- Drop desktop vendor tag.
- Use compat-guile18

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jan 15 2012 Hans de Goede <hdegoede@redhat.com> - 1.1.4-17
- Drop guile-2.0 patch for now as Fedora is still at guile-1.8.x, and
  the guile-2.0 patch + gcc-4.7 breaks building with 1.8.x

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed May 18 2011 Hans de Goede <hdegoede@redhat.com> - 1.1.4-15
- Fix building and running with guile-2.0 (rhbz#704536)
- Fix "Esc" sometimes directly exiting the game instead of taking you back to
  the main menu

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 25 2011 Hans de Goede <hdegoede@redhat.com> 1.1.4-13
- Fix crash when exiting game (#667236)

* Mon Feb 22 2010 Hans de Goede <hdegoede@redhat.com> 1.1.4-12
- Fix FTBFS (automake rerunning due to patches, #564762)

* Mon Jan 18 2010 Hans de Goede <hdegoede@redhat.com> 1.1.4-11
- Fix a crash when trying to change to an unsupported resolution (#555877)
- Add widescreen monitor resolutions to the monitor resolution list

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 20 2009 Hans de Goede <hdegoede@redhat.com> 1.1.4-8
- Adjust font requires for font rename (rh 480476)

* Sat Dec 27 2008 Hans de Goede <hdegoede@redhat.com> 1.1.4-7
- Replace included gnu freefont copy with a symlink to dejavu (rh 477470)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.1.4-6
- Autorebuild for GCC 4.3

* Sun Jan 13 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.1.4-5
- Fix building with gcc 4.3

* Thu Jan  3 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.1.4-4
- Fix black vertices on ATI cards with OSS drivers

* Tue Sep 25 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.1.4-3
- Use opengl-games-utils wrapper to show error dialog when DRI is missing

* Wed Aug 15 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.1.4-2
- Update License tag for new Licensing Guidelines compliance

* Tue Jun  5 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.1.4-1
- New upstream release 1.1.4

* Sat Mar 10 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.1.2-4
- Fixup .desktop file categories for games-menus usage

* Tue Aug 29 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.1.2-3
- FE6 Rebuild

* Tue Aug 15 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.1.2-2
- Remove some redundant BR's

* Mon Aug 14 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.1.2-1
- Initial Fedora Extras version
