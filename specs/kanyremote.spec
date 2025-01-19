Summary: KDE frontend for anyRemote
Name: kanyremote
Version: 8.1.1
Release: 4%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later
Source0: http://downloads.sourceforge.net/anyremote/%{name}-%{version}.tar.gz
Requires: python3-qt5-base, python3-bluez >= 0.22, bluez >= 4.64, anyremote >= 6.5
BuildRequires: gcc, desktop-file-utils
BuildRequires: make
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
URL: http://anyremote.sourceforge.net/
BuildArch: noarch

%description
kAnyRemote package is KDE GUI frontend for anyRemote
(http://anyremote.sourceforge.net/) - remote control software for applications 
using Bluetooth or Wi-Fi.

%prep
%setup -q

%build
%configure

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
desktop-file-install --vendor="" \
  --add-category="System" \
  --delete-original \
  --dir=$RPM_BUILD_ROOT%{_datadir}/applications/ \
  $RPM_BUILD_ROOT/%{_datadir}/applications/%{name}.desktop
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 8.1.1-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Mar 03 2024 Sérgio Basto <sergio@serjux.com> - 8.1.1-1
- Update kanyremote to 8.1.1

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild


* Wed Nov 11 2020 Mikhail Fedotov <anyremote at mail.ru> - 8.1
- Some fixes

* Tue Apr 30 2019 Mikhail Fedotov <anyremote at mail.ru> - 8.0
- Port to python3

* Wed Jan 10 2018 Mikhail Fedotov <anyremote at mail.ru> - 7.0
- Some fixes

* Thu Jul 20 2017 Mikhail Fedotov <anyremote at mail.ru> - 6.4
- Move to QT5

* Fri Jan 16 2015 Mikhail Fedotov <anyremote at mail.ru> - 6.3.5
- Avahi support

* Sun Oct 5 2014 Mikhail Fedotov <anyremote at mail.ru> - 6.3.4
- Fix some issues with QIcon class

* Fri Jul 18 2014 Mikhail Fedotov <anyremote at mail.ru> - 6.3.3
- Large application icon and AppData support.

* Mon Dec 2 2013 Mikhail Fedotov <anyremote at mail.ru> - 6.3.2
- Fixed RedHat bugzilla bug 1034914

* Mon Sep 16 2013 Mikhail Fedotov <anyremote at mail.ru> - 6.3.1
- Greek translation was added (Thanks to Ioannis Servetas)

* Fri Aug 16 2013 Mikhail Fedotov <anyremote at mail.ru> - 6.3
- Drop PyKDE dependency, small corrections, fixed RedHat bugzilla bug 988080.

* Mon Jun 10 2013 Mikhail Fedotov <anyremote at mail.ru> - 6.2
- Multiconnection and autostart support.

* Wed Oct 10 2012 Mikhail Fedotov <anyremote at mail.ru> - 6.1
- Drop lightthpd dependency. Translation updates

* Mon Aug 13 2012 Mikhail Fedotov <anyremote at mail.ru> - 6.0.1
- Translation update 

* Fri May 25 2012 Mikhail Fedotov <anyremote at mail.ru> - 6.0
- Update to work with anyremote v6.0, drop support of anyremote2html

* Sun Dec 4 2011 Mikhail Fedotov <anyremote at mail.ru> - 5.13
- Add --tray commandline option

* Fri Mar 11 2011 Mikhail Fedotov <anyremote at mail.ru> - 5.12
- Czech translation updated. Correctly works with anyRemote v5.4

* Fri Sep 17 2010 Mikhail Fedotov <anyremote at mail.ru> - 5.11.9
- Slovak translation updated 

* Wed Aug 4 2010 Mikhail Fedotov <anyremote at mail.ru> - 5.11.8
- Do not use /sbin/ip if it absent

* Fri Jul 16 2010 Mikhail Fedotov <anyremote at mail.ru> - 5.11.7
- Docs search path corrected.

* Tue Jul 6 2010 Mikhail Fedotov <anyremote at mail.ru> - 5.11.6
- Small correction.

* Fri Jul 2 2010 Mikhail Fedotov <anyremote at mail.ru> - 5.11.5
- Small correction.

* Tue Mar 9 2010 Mikhail Fedotov <anyremote at mail.ru> - 5.11.4
- Some correction in translations.

* Mon Feb 15 2010 Mikhail Fedotov <anyremote at mail.ru> - 5.11.3
- Some correction in translations. 128x128 java client icons handling.

* Mon Feb 01 2010 Mikhail Fedotov <anyremote at mail.ru> - 5.11.2
- Fixed RedHat bugzilla bug 560302

* Wed Jan 27 2010 Mikhail Fedotov <anyremote at mail.ru> - 5.11.1
- Small updates.

* Fri Jan 22 2010 Mikhail Fedotov <anyremote at mail.ru> - 5.11
- Command Fusion iViewer support.

* Mon Jul 6 2009 Mikhail Fedotov <anyremote at mail.ru> - 5.10.2
- Translations were updated.

* Thu Jul 2 2009 Mikhail Fedotov <anyremote at mail.ru> - 5.10
- Tool was rewritten on QT4. Enhanced handling of GuiAppBinary tag.
  Handle java client with 48x48 icons.

* Tue May 26 2009 Mikhail Fedotov <anyremote at mail.ru> - 5.9
- Slovak translation was added (thanks to Michal Toth)

* Fri Apr 9 2009 Mikhail Fedotov <anyremote at mail.ru> - 5.8.2
- Small enhancements 

* Tue Apr 7 2009 Mikhail Fedotov <anyremote at mail.ru> - 5.8.1
- Fix small bug 

* Mon Mar 30 2009 Mikhail Fedotov <anyremote at mail.ru> - 5.8
- Add GuiAppModes tag handling

* Wed Mar 11 2009 Mikhail Fedotov <anyremote at mail.ru> - 5.7
- Finnish and Swedish translation were added (thanks to Matti Jokinen)

* Wed Jan 21 2009 Mikhail Fedotov <anyremote at mail.ru> - 5.6.1-1
- Minor bugfix

* Mon Jan 19 2009 Mikhail Fedotov <anyremote at mail.ru> - 5.6-1
- Check java client version on the web site

* Sun Dec 21 2008 Mikhail Fedotov <anyremote at mail.ru> - 5.5.1-1
- Fix upload from web feature

* Sun Dec 14 2008 Mikhail Fedotov <anyremote at mail.ru> - 5.5-1
- Handle GuiAppVersion parameter in configuration files. Add possibility
  to download java client from Web. Small Ubuntu-specific fixes.

* Wed Dec 3 2008 Mikhail Fedotov <anyremote at mail.ru> - 5.4.1-1
- Fix detection of activity of bluetooth service

* Fri Oct 17 2008 Mikhail Fedotov <anyremote at mail.ru> - 5.4-1
- Enhanced edit configuration file window. Support application details 
  auto wrap. Added Bulgarian translation (thanks to Stanislav Popov)

* Wed Sep 24 2008 Mikhail Fedotov <anyremote at mail.ru> - 5.3-1
- Add icons to menu and buttons.

* Mon Sep 8 2008 Mikhail Fedotov <anyremote at mail.ru> - 5.2.1-1
- Small bugfixes.

* Thu Sep 4 2008 Mikhail Fedotov <anyremote at mail.ru> - 5.2-1
- Added "Details" field to the main window.
  Added French translation (thanks to Philippe Hensel).

* Tue Aug 19 2008 Mikhail Fedotov <anyremote at mail.ru> - 5.1-1
- Fixed crash on startup issue.
  Added Czech (thanks to Tomas Kaluza) and Dutch (thanks to Geert Vanhaute)
  translations.

* Mon Jul 21 2008 Mikhail Fedotov <anyremote at mail.ru> - 5.0-1
- Internationalization support.
  Added Polish (thanks to Marek Szuba), Austrian (thanks to Christian 
  Zehetnertran), German (thanks to Johann Bauer), Spanish (thanks to Carlos 
  Sanchez Mateo and Francisco), Brazilian Portuguese (thanks to Marcos 
  Venilton Batista),Italian (thanks to Massimo Robbiati) Hungarian (thanks to 
  Gyuris Szabolcs) and Russian translations.

* Sun May 25 2008 Mikhail Fedotov <anyremote at mail.ru> - 4.9-1
- Bugfixes and enhancements to better support anyremote-J2ME client v4.6 and
  anyremote2html v0.5.

* Sun Apr 20 2008 Mikhail Fedotov <anyremote at mail.ru> - 4.8-1
- Some small enhancements. Spec file correction.

* Tue Mar 11 2008 Mikhail Fedotov <anyremote at mail.ru> - 4.7-1.fc8
- Some small enhancements. Corrected to work properly with anyRemote v4.4.

* Tue Feb 26 2008 Mikhail Fedotov <anyremote at mail.ru> - 4.6-2.fc8
- Spec file correction

* Wed Feb 20 2008 Mikhail Fedotov <anyremote at mail.ru> - 4.6-1.fc8
- Handle absense of .anyRemote directory

* Sun Feb 17 2008 Mikhail Fedotov <anyremote at mail.ru> - 4.5-2.fc8
- Spec file correction

* Fri Feb 15 2008 Mikhail Fedotov <anyremote at mail.ru> - 4.5-1.fc8
- Motorola RIZR Z3 support enhanced

%files -f %{name}.lang
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}_flash.png 
%{_datadir}/pixmaps/%{name}_off.png 
%{_datadir}/pixmaps/%{name}_light.png  
%{_datadir}/pixmaps/%{name}_small.png  
%{_datadir}/pixmaps/%{name}_logo.svg  
%{_datadir}/pixmaps/%{name}.png
%{_defaultdocdir}/%{name}
