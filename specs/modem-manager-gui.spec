Name:          modem-manager-gui
Summary:       Graphical interface for ModemManager
Summary(de):   Grafische Oberfläche für ModemManager
Summary(ru):   Графический интерфейс для демона ModemManager

Version:       0.0.20
Release:       16%{?dist}
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:       GPL-3.0-only

URL:           https://linuxonly.ru/page/modem-manager-gui
Source0:       http://download.tuxfamily.org/gsf/source/modem-manager-gui-%{version}.tar.gz

# Fix the NetworkManager dispatcher script location
Patch1: 0001-Move-the-NetworkManager-dispatcher-script-out-of-etc.patch

# Appdata XML validation fails
Patch2: 0002-add-missing-appdata-tags.patch

# There have been a couple of Meson releases since the last MMGUI release
# and some of the stuff used in build scripts has been deprecated since
Patch3: 0003-fix-deprecated-meson-functions.patch

# MMGUI crashes with some new versions of NetworkManager.
# Patch taken from Debian:
# https://salsa.debian.org/debian/modem-manager-gui/-/raw/master/debian/patches/fix_segfault_on_DNS_entries.patch
Patch4: 0004-fix-segfault-on-DNS-entries.patch

# Use meson for build? Otherwise, use make.
%global build_using_meson 1

# Enable/disable plugins.
%global with_connman 0
%global with_ofono   1
%global with_ppp     1

BuildRequires: gcc
BuildRequires: desktop-file-utils
BuildRequires: gdbm-devel >= 1.10
BuildRequires: gettext
BuildRequires: glib2-devel >= 2.32.1
BuildRequires: gtk3-devel >= 3.4.0
BuildRequires: gtkspell3-devel >= 3.0.3
BuildRequires: itstool >= 1.2.0
BuildRequires: libappindicator-gtk3-devel >= 0.4.92
BuildRequires: libappstream-glib
BuildRequires: libnotify-devel >= 0.7.5
BuildRequires: pkgconfig
BuildRequires: po4a > 0.45

%if %{build_using_meson}
BuildRequires: meson >= 0.38
%else
BuildRequires: make
%endif

%if %{with_ofono}
%global ofono_version 1.9
BuildRequires: ofono-devel >= %{ofono_version}
%endif

Requires: filesystem
Requires: hicolor-icon-theme
Requires: mobile-broadband-provider-info >= 1.20120614
Requires: yelp >= 3.10

Requires: %{name}-cm%{?_isa} = %{version}-%{release}
Suggests: %{name}-cm-NetworkManager%{?_isa} = %{version}-%{release}
Requires: %{name}-mm%{?_isa} = %{version}-%{release}
Suggests: %{name}-mm-ModemManager%{?_isa} = %{version}-%{release}

%description
This program is a simple graphical interface for Modem Manager 
daemon dbus interface.
Current features:
- View device information: Operator name, Mode, IMEI, IMSI,
  Signal level.
- Send and receive SMS messages with long massages 
  concatenation and store messages in database.
- Send USSD requests and read answers in GSM7 and UCS2 formats
  converted to system UTF8 charset.
- Scan available mobile networks.

%description -l de
Dieses Programm ist eine einfache grafische Oberfläche für
die DBus-Schnittstelle des ModemManager-Daemons.
Funktionen:
- Geräteinformationen anzeigen: Name des Netzanbieters, Modus,
  IMEI, IMSI, Signalstärke.
- SMS senden und empfangen, Verkettung langer Nachrichten,
  Speichern der Nachrichten in der Datenbank.
- USSD-Befehle in den Formaten GSM7 und UCS2 senden und
  Antworten empfangen, Umwandlung in den UTF-8-Zeichensatz.
- Nach verfügbaren Mobilnetzwerken suchen.

%description -l ru
Данная программа является простым графическим интерфейсом для
демона Modem Manager, использующим интерфейс dbus.
Текущие возможности:
- Просмотр информации об устройстве: имени оператора, режима работы,
  IMEI, IMSI и уровня сигнала.
- Прием и отправка сообщений SMS с объединением длинных сообщений 
  и сохранением сообщений в базе данных.
- Отправка запросов USSD и прием ответов в кодировках GSM7 и UCS2
  с последующей конвертацией в системную кодировку UTF8.
- Сканирование доступных мобильных сетей.

%if %{with_connman}
%package cm-connman
Summary: Use connman to manage connections in %{name}
Requires: connman >= 1.12
Provides: %{name}-cm%{?_isa}
%description cm-connman
Plugin for %{name} allowing to use connman as the connection manager.
%endif

%package cm-NetworkManager
Summary: Use NetworkManager to manage connections in %{name}
Requires: NetworkManager >= 1.20
Requires: python3
Provides: %{name}-cm%{?_isa}
%description cm-NetworkManager
Plugin for %{name} allowing to use NetworkManager
as the connection manager.

%if %{with_ppp}
%package cm-pppd
Summary: Use pppd to manage connections in %{name}
Requires: ppp >= 2.4.5
Provides: %{name}-cm%{?_isa}
%description cm-pppd
Plugin for %{name} allowing to use pppd as the connection manager.
%endif

%package mm-ModemManager
Summary: Use ModemManager to manage modems in %{name}
Requires: ModemManager >= 0.7.0
Provides: %{name}-mm%{?_isa}
%description mm-ModemManager
Plugin for %{name} allowing to use ModemManager as the modem manager.

%if %{with_ofono}
%package mm-ofono
Summary: Use ofono to manage modems in %{name}
Requires: ofono >= %{ofono_version}
Provides: %{name}-mm%{?_isa}
%description mm-ofono
Plugin for %{name} allowing to use ofono as the modem manager. 
%endif


%prep
%autosetup -n %{name} -p1


%build
%if %{build_using_meson}
    %meson
    %meson_build
%else
    %configure
    %make_build
%endif


%install
# Override the system RPM macro to force a single-threaded install process.
# This is a workaround around bugs in /usr/bin/itstool, which cause it
# to behave non-deterministic during pararell builds.
%global _smp_mflags -j1

%if %{build_using_meson}
    %meson_install
%else
    %make_install
%endif

%find_lang %{name} --with-gnome

# Fix /usr/bin/env usage
sed -e 's|/usr/bin/env python3|/usr/bin/python3|' \
    -i %{buildroot}%{_prefix}/lib/NetworkManager/dispatcher.d/95-mmgui-timestamp-notifier

# Remove plugin for obsolete ModemManager version
rm %{buildroot}/%{_libdir}/%{name}/modules/libmodmm_mm06.so

%if !%{with_connman}
    find %{buildroot} -name '*connman*.so*' -printf 'Removed unused file: %p\n' -delete
%endif

%if !%{with_ofono}
    find %{buildroot} -name '*ofono*.so*' -printf 'Removed unused file: %p\n' -delete
%endif

%if !%{with_ppp}
    find %{buildroot} -name '*pppd*.so*' -printf 'Removed unused file: %p\n' -delete
%endif


%check
appstream-util validate --nonet %{buildroot}/%{_datadir}/metainfo/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop


%files -f %{name}.lang
%doc AUTHORS Changelog
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/icons/hicolor/symbolic/apps/%{name}-symbolic.svg
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/polkit-1/actions/ru.linuxonly.modem-manager-gui.policy
%{_datadir}/%{name}/
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/modules/
%{_mandir}/man1/%{name}.1.*
%{_mandir}/*/man1/%{name}.1.*

%if %{with_connman}
%files cm-connman
%{_libdir}/%{name}/modules/libmodcm_connman112.so
%endif

%files cm-NetworkManager
%{_libdir}/%{name}/modules/libmodcm_nm09.so
%{_prefix}/lib/NetworkManager/dispatcher.d/95-mmgui-timestamp-notifier

%if %{with_ppp}
%files cm-pppd
%{_libdir}/%{name}/modules/libmodcm_pppd245.so
%endif

%files mm-ModemManager
%{_libdir}/%{name}/modules/libmodmm_mm07.so

%if %{with_ofono}
%files mm-ofono
%{_libdir}/%{name}/modules/libmodmm_ofono109.so
%{_libdir}/ofono/plugins/libmmgui-ofono-history.so*
%endif


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.0.20-15
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jul 26 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.0.20-9
- Add a patch to fix segfault when processing DNS entries

* Fri Jul 22 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.0.20-8
- Add Patch3: fix use of deprecated Meson features

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 01 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.0.20-4
- Disable connman support (orphaned and retired) - fixes rhbz#1955847

* Mon Mar 29 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.0.20-3
- Re-enable ofono support (unretired in F34+)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Aug 02 2020 Artur Iwicki <fedora@svgames.pl> - 0.0.20-1
- Update to new upstream release v0.0.20
- Switch back to using Meson instead of Make
- Drop Patch0 (strncpy() fixes - accepted and merged upstream)
- Drop Patch1 and Patch2 (backports from this release)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.19.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Feb 02 2020 Artur Iwicki <fedora@svgames.pl> - 0.0.19.1-12
- Add a patch to fix Appdata XML validation errors

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.19.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 22 2019 Lubomir Rintel <lkundrak@v3.sk> - 0.0.19.1-10
- Move the NetworkManager dispatcher script out of /etc

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.19.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 25 2019 Artur Iwicki <fedora@svgames.pl> - 0.0.19.1-8
- Add upstream patches for memory corruption issues

* Sat Mar 09 2019 Artur Iwicki <fedora@svgames.pl> - 0.0.19.1-7
- Use make instead of meson for building

* Tue Feb 05 2019 Artur Iwicki <fedora@svgames.pl> - 0.0.19.1-6
- Force the installation phase to be single-threaded

* Sun Feb 03 2019 Artur Iwicki <fedora@svgames.pl> - 0.0.19.1-5
- Fix build failures due to Fedora dropping ofono
- Fix build failures due to strncpy() usages

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.19.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 07 2018 Artur Iwicki <fedora@svgames.pl> - 0.0.19.1-3
- Fix meson version requirement
- Add a sleep call to workaround subtly broken meson script

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.19.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Apr 28 2018 Artur Iwicki <fedora@svgames.pl> - 0.0.19.1-1
- Update to new upstream version
- Remove Patch0 (fix to linker errors) - issues fixed upstream

* Mon Mar 26 2018 Artur Iwicki <fedora@svgames.pl> - 0.0.19-4
- Add exact version-release requirement to Requires: %%{name}-cm and -mm
- Add line wrapping to -cm-NetworkManager description

* Sat Mar 24 2018 Artur Iwicki <fedora@svgames.pl> - 0.0.19-3
- Separate the connection management and the modem management plugins
  into individual packages

* Wed Mar 21 2018 Artur Iwicki <fedora@svgames.pl> - 0.0.19-2
- Add missing Requires:
- Fix 95-mmgui-timestamp-notifier using "#!/usr/bin/env python3"

* Tue Mar 20 2018 Artur Iwicki <fedora@svgames.pl> - 0.0.19-1
- Update to new upstream release

* Sun Feb 18 2018 Artur Iwicki <fedora@svgames.pl> - 0.0.18-8
- Add missing BuildRequires: for gcc
- Order BuildRequires: alphabetically

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Oct 18 2015 Mario Blättermann <mario.blaettermann@gmail.com> - 0.0.18-2
- New upstream version
- Patch1 is obsolete

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.17.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 25 2015 Mario Blättermann <mario.blaettermann@gmail.com> - 0.0.17.1-4
- Patch for broken libebook API

* Fri Jan 02 2015 Mario Blättermann <mario.blaettermann@gmail.com> - 0.0.17.1-3
- Reactivate bn_BD locale
- Use the %%license macro

* Thu Sep 18 2014 Mario Blättermann <mariobl@fedoraproject.org> - 0.0.17.1-2
- Appdata validation disabled due to vague guidelines

* Thu Sep 18 2014 Mario Blättermann <mariobl@fedoraproject.org> - 0.0.17.1-1
- New upstream version
- Added latest translations from Transifex
- Appdata file validation

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 03 2014 Mario Blättermann <mariobl@fedoraproject.org> - 0.0.16-4
- Remove the bn_BD translation because the locale doesn't exist in Fedora
- Added German and Russian man pages

* Thu Jan 02 2014 Mario Blättermann <mariobl@fedoraproject.org> - 0.0.16-3
- Fix folder ownership
- Move desktop-file-validate to %%check

* Sat Dec 28 2013 Mario Blättermann <mariobl@fedoraproject.org> - 0.0.16-2
- Added German translation

* Sat Oct 26 2013 Mario Blättermann <mariobl@fedoraproject.org> 0.0.16-1
- New upstream version
- Some spec file cleanup

* Sun Dec 16 2012 Alex <alex@linuxonly.ru>
- added additional pictures for 0.0.15 release

* Wed Aug 08 2012 Alex <alex@linuxonly.ru>
- released spec

