Name:           games-menus
Version:        0.3.2
Release:        34%{?dist}
Summary:        Catagorized submenus for the MATE/KDE Games menu
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://www.redhat.com/archives/fedora-games-list/2007-March/msg00003.html
# No URL as we are upstream
Source0:        %{name}-%{version}.tar.gz
Patch0:         games-menus-0.3.2-it-spellfix.patch
BuildArch:      noarch
Requires:       redhat-menus hicolor-icon-theme
Provides:       dribble-menus = 1.2
Obsoletes:      dribble-menus <= 1.2

%description
Catagorized submenus for the MATE/KDE Games menu, for better usuability of the
games menu with lots of games installed


%prep
%setup -q
%patch -P0 -p1


%build
# nothing to build data only


%install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/xdg/menus/applications-merged
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor
install -p -m 644 games-categories.menu \
  $RPM_BUILD_ROOT%{_sysconfdir}/xdg/menus/applications-merged
cp -a desktop-directories $RPM_BUILD_ROOT%{_datadir}
cp -a icons/* $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/



%files
%doc copyright-info.txt COPYING* README
%config(noreplace) %{_sysconfdir}/xdg/menus/applications-merged/games-categories.menu
%{_datadir}/desktop-directories/*.directory
%{_datadir}/icons/hicolor/*/apps/package_games_*.png


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.3.2-33
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.2-17
- Remove obsolete scriptlets

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 21 2014 Hans de Goede <hdegoede@redhat.com> - 0.3.2-12
- s/GNOME/MATE/ in the description as this package does not work with GNOME3,
  but does work with MATE (rhbz#1097454)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jun 23 2010 Hans de Goede <hdegoede@redhat.com> 0.3.2-5
- Do not own /usr/share/desktop-directories (rh569439)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec  1 2008 Hans de Goede <hdegoede@redhat.com> 0.3.2-2
- Fix minor spelling error in Italian translation (rh 473385)

* Tue Feb  5 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.3.2-1
- Updated Slovak translation, thanks to Pavol Šimo

* Sun Feb  3 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.3.1-1
- Add Slovak translation, thanks to Pavol Šimo

* Tue Jan  8 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.3-1
- Make a new 0.3 tarbal with the French translations included, instead
  of patching the French translation in
- Not patching fixes the problem of .orig files being packaged (bz 427863)

* Mon Aug  6 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.2-4
- Update License tag for new Licensing Guidelines compliance

* Mon Mar 12 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.2-3
- Add French translation, thanks to Eric Tanguy

* Sat Mar 10 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.2-2
- Add Provides and Obsoletes: dribble-menus

* Fri Mar  9 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.2-1
- Polish, Italian and Dutch translations
- Fix URL, and package it as README
- Package copyright-info.txt and related files

* Sat Mar  3 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.1-1
- Initial release
