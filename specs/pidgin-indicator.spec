
Name:    pidgin-indicator
Summary: StatusNotifierItem tray icon plugin for Pidgin
Version: 1.0.1
Release: 17%{?dist}

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     https://github.com/philipl/pidgin-indicator
Source0: https://github.com/philipl/pidgin-indicator/releases/download/%{version}/pidgin-indicator-%{version}.tar.bz2

BuildRequires: make
BuildRequires: gcc
BuildRequires: gettext
BuildRequires: intltool
BuildRequires: pkgconfig(appindicator-0.1)
BuildRequires: pkgconfig(pidgin)
BuildRequires: perl(XML::Parser)

Requires: pidgin

%if 0%{?fedora} > 23
Supplements: (pidgin and plasma-workspace)
%endif

%description
This plugin provides a StatusNotifierItem tray icon, for use in
KDE Plasma 5, Unity, Elementary and other environments.

It provides all the same functionality as the original tray icon
but not in exactly the same way:
* The smart click behavior that either shows the buddy list or
unread messages is now activated by a middle-click because
left click on an libappindicator always opens the menu.
* As the SNI-icon is a separate process from pidgin itself, there
are sometimes conflicts with Focus Stealing Prevention when you
use the indicator to go to unread messages. You may need to
disable FSP for Pidgin to get around this.
* Due to how libappindicator work, the middle-click action must
also be a menu item, so it's the new Show/Hide item at the top
of the menu.
* Due to libappindicator limitations, some of the special icons
cannot be shown next to menu items any more.


%prep
%autosetup


%build
%configure

%make_build


%install
%make_install

%find_lang pidgin-indicator

## unpackaged files
rm -fv %{buildroot}%{_libdir}/pidgin/indicator.la

%files -f pidgin-indicator.lang
%doc AUTHORS NEWS README.md
%license COPYING
%{_libdir}/pidgin/indicator.*
%{_datadir}/icons/hicolor/*/status/pidgin-indicator-nothing.png


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.1-16
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 03 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.0.1-1
- 1.0.1 (#1574489)

* Tue Feb 20 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.0-7
- BR: gcc, use %%make_build %%make_install

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0-5
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 24 2017 Rex Dieter <rdieter@fedoraproject.org> - 1.0-1
- 1.0

* Mon Mar 07 2016 Rex Dieter <rdieter@fedoraproject.org> 0.9-2
- Supplements: (pidgin and plasma-workspace), f24+

* Sat Mar 05 2016 Rex Dieter <rdieter@fedoraproject.org> 0.9-1
- 0.9

* Mon Jun 15 2015 Radek Vokal <rvokal@redhat.com> - 0.1-1
- Initial package build
