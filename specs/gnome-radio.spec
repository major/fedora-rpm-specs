%global commit      0b39e21977d736bf5434a102c859cbf0446d3dfa
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date        20231110

Name:           gnome-radio
Version:        0.1.0
Release:        10.%{date}git%{shortcommit}%{?dist}
Summary:        GNOME Radio
 
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://gnomeradio.org
Source0:        https://gitlab.gnome.org/olekaam/radio/-/archive/%{commit}/radio-%{commit}.tar.bz2

BuildRequires:  autoconf
BuildRequires:  automake
# BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gtk-doc
BuildRequires:  intltool
# BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(champlain-gtk-0.12) >= 0.12.10
BuildRequires:  pkgconfig(geoclue-2.0) >= 1.0
BuildRequires:  pkgconfig(geocode-glib-2.0) >= 1.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.40
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.0
BuildRequires:  pkgconfig(gstreamer-player-1.0) >= 1.0
BuildRequires:  pkgconfig(gstreamer-tag-1.0) >= 1.0
BuildRequires:  pkgconfig(gstreamer-video-1.0) >= 1.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.30
BuildRequires:  pkgconfig(libgeoclue-2.0) >= 1.0
BuildRequires:  make
# Requires:       hicolor-icon-theme

%description
GNOME Radio is a free network radio software for the GNOME desktop.

%prep
%autosetup -p1 -n radio-%{commit}

%build
%configure
%make_build

%install
%make_install

%files
%{_bindir}/gtk-internet-radio-locator
%{_datadir}/appdata/gtk-internet-radio-locator.appdata.xml
%{_datadir}/applications/gtk-internet-radio-locator.desktop
%{_datadir}/gtk-internet-radio-locator/internet-radio-locator-1.5.dtd
%{_datadir}/gtk-internet-radio-locator/internet-radio-locator.xml
%{_datadir}/icons/hicolor/1024x1024/apps/gtk-internet-radio-locator.png
%{_datadir}/icons/hicolor/16x16/apps/gtk-internet-radio-locator.png
%{_datadir}/icons/hicolor/22x22/apps/gtk-internet-radio-locator.png
%{_datadir}/icons/hicolor/24x24/apps/gtk-internet-radio-locator.png
%{_datadir}/icons/hicolor/256x256/apps/gtk-internet-radio-locator.png
%{_datadir}/icons/hicolor/32x32/apps/gtk-internet-radio-locator.png
%{_datadir}/icons/hicolor/48x48/apps/gtk-internet-radio-locator.png
%{_datadir}/icons/hicolor/512x512/apps/gtk-internet-radio-locator.png
%{_datadir}/locale/ca/LC_MESSAGES/gtk-internet-radio-locator.mo
%{_datadir}/locale/cs/LC_MESSAGES/gtk-internet-radio-locator.mo
%{_datadir}/locale/de/LC_MESSAGES/gtk-internet-radio-locator.mo
%{_datadir}/locale/es/LC_MESSAGES/gtk-internet-radio-locator.mo
%{_datadir}/locale/fr/LC_MESSAGES/gtk-internet-radio-locator.mo
%{_datadir}/locale/hu/LC_MESSAGES/gtk-internet-radio-locator.mo
%{_datadir}/locale/id/LC_MESSAGES/gtk-internet-radio-locator.mo
%{_datadir}/locale/nb/LC_MESSAGES/gtk-internet-radio-locator.mo
%{_datadir}/locale/pl/LC_MESSAGES/gtk-internet-radio-locator.mo
%{_datadir}/locale/pt_BR/LC_MESSAGES/gtk-internet-radio-locator.mo
%{_datadir}/locale/sl/LC_MESSAGES/gtk-internet-radio-locator.mo
%{_datadir}/locale/sr/LC_MESSAGES/gtk-internet-radio-locator.mo
%{_datadir}/locale/sv/LC_MESSAGES/gtk-internet-radio-locator.mo
%{_mandir}/man1/gtk-internet-radio-locator.1.gz
%doc README AUTHORS

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-10.20231110git0b39e21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Aug 26 2024 Neel Chauhan <neel@neelc.org> - 0.1.0-8.20231110git0b39e21
 - Update to newer snapshot

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.1.0-8.20200723git28a53b9
- convert license to SPDX

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-7.20200723git28a53b9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-6.20200723git28a53b9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 14 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1.0-5.20200723git28a53b9
- build(update): commit 28a53b9

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-4.20190217gite982347
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3.20190217gite982347
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2.20190217gite982347
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1.0-1.20190217gite982347
- Initial package
