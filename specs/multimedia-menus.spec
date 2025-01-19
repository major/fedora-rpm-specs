Name:           multimedia-menus
Version:        0.4.2
Release:        12%{?dist}
Summary:        Categorization for the GNOME/KDE/MATE Sound&Video/Multimedia menu
# Licensing of individual parts is explained in licensing.txt file
# Automatically converted from old format: GPLv2+ and LGPLv2+ and GPL+ and LGPLv2 and LGPLv3+ and GPLv2 and MIT - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+ AND GPL-1.0-or-later AND LicenseRef-Callaway-LGPLv2 AND LGPL-3.0-or-later AND GPL-2.0-only AND LicenseRef-Callaway-MIT
URL:            https://pagure.io/multimedia-menus
Source0:        https://pagure.io/multimedia-menus/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  intltool
Requires:       redhat-menus hicolor-icon-theme dconf

%description
Categorized sub-menus for the GNOME/KDE/MATE Audio&Video/Multimedia menu, for
better usability and easy access of multimedia applications.


%prep
%setup -q


%build
make %{_smp_mflags}

%install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/xdg/menus/applications-merged/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/desktop-directories/
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/dconf/db/site.d/
cp -a multimedia-menus.dconf $RPM_BUILD_ROOT%{_sysconfdir}/dconf/db/site.d/00_multimedia-menus
install -p -m 644 multimedia-categories.menu \
  $RPM_BUILD_ROOT%{_sysconfdir}/xdg/menus/applications-merged/
cp -a desktop-directories/*.directory \
  $RPM_BUILD_ROOT%{_datadir}/desktop-directories/
cp -ar icons/* $RPM_BUILD_ROOT%{_datadir}/icons/

%post
dconf update

%postun
dconf update

%files
%doc AUTHORS changelog.txt licensing.txt COPYING*
%config(noreplace) %{_sysconfdir}/xdg/menus/applications-merged/multimedia-categories.menu
%config %{_sysconfdir}/dconf/db/site.d/00_%{name}
%{_datadir}/desktop-directories/multimedia-*.directory
%{_datadir}/icons/hicolor/*/apps/multimedia-*.png


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 0.4.2-11
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 11 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 0.4.2-1
- Fix typographical error for appfolder name in dconf

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 25 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 0.4.1-1
- Add X-AudioEditing to audio editors

* Wed Jun 17 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 0.4.0-1
- Add dconf db file for GNOME appfolders

* Wed Jun 17 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 0.3.4-17
- Moved source to pagure.io

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.4-11
- Remove obsolete scriptlets

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.3.4-5
- Updated the summary and description to include MATE RHBZ#982000

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan 16 2012 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.3.4-1
- Version bump with new translations

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 25 2010 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.3.3-1
- Version bump with new translations

* Sun Apr 18 2010 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.3.2-1
- Version bump with new translations

* Sun Sep 27 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.3.1-1
- Version bump with new translations

* Tue Sep 15 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.3-2
- Add missing BR: intltool

* Tue Sep 15 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.3-1
- Lots of translations! YAAY!
- Change URL to fedorahosted

* Tue Aug 04 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.2-1
- Version bump with fixes in category names

* Sat Jul 25 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.1-2
- Correct Source0
- Add dist tag

* Sat Jul 18 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.1-1
- Initial build
