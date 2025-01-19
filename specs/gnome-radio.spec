Name:           gnome-radio
Version:        47.0
Release:        %autorelease
Summary:        GNOME Radio
 
License:        GPL-3.0-or-later
URL:            http://gnomeradio.org
Source0:        http://www.gnomeradio.org/src/gnome-radio-47.0.tar.xz

BuildRequires:  autoconf
BuildRequires:  automake
# BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  itstool
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
%autosetup

%build
%configure
%make_build

%install
%make_install

%files
%{_bindir}/gnome-internet-radio-locator
%{_bindir}/gnome-radio
%{_bindir}/org.gnome.Radio
%{_datadir}/applications/gnome-radio.desktop
%{_datadir}/gnome-radio/doc/AAMOT.txt.xz
%{_datadir}/gnome-radio/doc/Aamot-2020.txt.xz
%{_datadir}/gnome-radio/gnome-radio-47.0.dtd
%{_datadir}/gnome-radio/gnome-radio.xml
%{_datadir}/gnome-radio/org.gnome.Radio.dtd
%{_datadir}/gnome-radio/org.gnome.Radio.xml
%{_datadir}/icons/hicolor/scalable/apps/gnome-radio.svg
%{_datadir}/locale/ca/LC_MESSAGES/gnome-radio.mo
%{_datadir}/locale/cs/LC_MESSAGES/gnome-radio.mo
%{_datadir}/locale/da/LC_MESSAGES/gnome-radio.mo
%{_datadir}/locale/de/LC_MESSAGES/gnome-radio.mo
%{_datadir}/locale/el/LC_MESSAGES/gnome-radio.mo
%{_datadir}/locale/es/LC_MESSAGES/gnome-radio.mo
%{_datadir}/locale/eu/LC_MESSAGES/gnome-radio.mo
%{_datadir}/locale/fr/LC_MESSAGES/gnome-radio.mo
%{_datadir}/locale/fur/LC_MESSAGES/gnome-radio.mo
%{_datadir}/locale/hr/LC_MESSAGES/gnome-radio.mo
%{_datadir}/locale/hu/LC_MESSAGES/gnome-radio.mo
%{_datadir}/locale/id/LC_MESSAGES/gnome-radio.mo
%{_datadir}/locale/nb/LC_MESSAGES/gnome-radio.mo
%{_datadir}/locale/nl/LC_MESSAGES/gnome-radio.mo
%{_datadir}/locale/oc/LC_MESSAGES/gnome-radio.mo
%{_datadir}/locale/pl/LC_MESSAGES/gnome-radio.mo
%{_datadir}/locale/pt_BR/LC_MESSAGES/gnome-radio.mo
%{_datadir}/locale/ro/LC_MESSAGES/gnome-radio.mo
%{_datadir}/locale/sk/LC_MESSAGES/gnome-radio.mo
%{_datadir}/locale/sl/LC_MESSAGES/gnome-radio.mo
%{_datadir}/locale/sr/LC_MESSAGES/gnome-radio.mo
%{_datadir}/locale/sv/LC_MESSAGES/gnome-radio.mo
%{_datadir}/locale/tr/LC_MESSAGES/gnome-radio.mo
%{_datadir}/locale/uk/LC_MESSAGES/gnome-radio.mo
%{_datadir}/locale/zh_CN/LC_MESSAGES/gnome-radio.mo
%{_datadir}/man/man1/gnome-radio.1.gz
%{_datadir}/metainfo/gnome-radio.appdata.xml
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
