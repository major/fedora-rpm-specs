Summary: Remote control through Wi-Fi or bluetooth connection
Name: anyremote
Version: 6.7.3
Release: 15%{?dist}
License: GPL-3.0-or-later
Source0: http://downloads.sourceforge.net/anyremote/%{name}-%{version}.tar.gz
URL: http://anyremote.sourceforge.net/
Requires: bc,wmctrl,ImageMagick,anyremote-data >= 6.7.3
BuildRequires: gcc, bluez-libs-devel >= 5.0, libX11-devel, libXi-devel, libXtst-devel, xorg-x11-proto-devel, glib2-devel >= 2.24.1, dbus-devel >= 1.2.24, dbus-glib-devel >= 0.86, avahi-devel >= 0.6.25
BuildRequires: make

%description
Remote control software for applications using Wi-Fi or Bluetooth.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files 
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz

%package data
Summary: Configuration files for anyRemote
Group: Applications/System

%description data
Configuration files for anyRemote

%files data
%defattr(-,root,root,-)
%{_datadir}/%{name}

%package doc
Summary: Documentation for anyRemote
Group: Applications/System

%description doc
Documentation for anyRemote

%files doc
%defattr(-,root,root,-)
%doc %{_defaultdocdir}/%{name}


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jun 24 2023 Sérgio Basto <sergio@serjux.com> - 6.7.3-10
- Migrate to SPDX license format

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.3-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild


* Fri Nov 8 2019 Mikhail Fedotov <anyremote at mail.ru> - 6.7.3
- Avoid usage of python2 in scripts.

* Sun Nov 18 2018 Mikhail Fedotov <anyremote at mail.ru> - 6.7.2
- Configuration file for Shotwell and Snappy were added. Weather script was 
  fixed.

* Mon Jan 22 2018 Mikhail Fedotov <anyremote at mail.ru> - 6.7.1
- Improve interoperability with GUI frontends. 

* Mon Jan 15 2018 Mikhail Fedotov <anyremote at mail.ru> - 6.7
- Some fixes. Configuration file for MPV was added. 

* Tue Mar 15 2016 Mikhail Fedotov <anyremote at mail.ru> - 6.6.1
- Bluez-related fixes. 

* Sat Feb 27 2016 Mikhail Fedotov <anyremote at mail.ru> - 6.6
- Scale images and cover pictures automatically and separately for each 
  connected client. Add Set(hints,...), Set(list,dir,...) and Set(text,file,...)
  commands. Added -cfgdir and -tmpdir commandline options. 

* Sat Dec 20 2014 Mikhail Fedotov <anyremote at mail.ru> - 6.5
- Avahi support.

* Sun Mar 02 2014 Mikhail Fedotov <anyremote at mail.ru> - 6.4
- Support for keyboard and mouse emulation events for Android client.

* Thu Sep 12 2013 Mikhail Fedotov <anyremote at mail.ru> - 6.3.2
- Configuration file for SMPlayer2 as added. FreeBSD and some other fixes.

* Wed Jun 12 2013 Mikhail Fedotov <anyremote at mail.ru> - 6.3.1
- Small enhancements and bugfixes.

* Sat Apr 27 2013 Mikhail Fedotov <anyremote at mail.ru> - 6.3
- Configuration file for DjView  was added. Multiconnection support. 
  Named cover auto-uploading.

* Tue Dec 18 2012 Mikhail Fedotov <anyremote at mail.ru> - 6.2
- Use $(TmpDir) in configuration files to store temporary file. 
  Use $(WaitSecons) variable to kill neverending scripts. 
  Use allowed_hosts file and $(AllowedOnly) variable to access control. 
  Avoided to use bash in favour of sh in configuration files.
  Support mutliple inheritance for modes. Configuration file for Foobnix was 
  added. Majority of audio player configuration files were reworked.

* Mon Oct 08 2012 Mikhail Fedotov <anyremote at mail.ru> - 6.1
- Support of XML services interface. Support Set(vibrate,duration) command. 
  Add possibility to disable GLIB usage (for OpenWRT build).
  Major code restructurization.

* Thu May 17 2012 Mikhail Fedotov <anyremote at mail.ru> - 6.0
- Support of build-in web server, no anyremote2html package needed anymore.
  Commands Set(parameter,icon_size|icon_padding,...) and 
  Get(icon_size|icon_padding) were added, command Set(skin,...,split,sizeXX...) and
  Set(parameter,lazy_repaint) were removed. Lot of configuration files were 
  updated.

* Thu Jan 05 2012 Mikhail Fedotov <anyremote at mail.ru> - 5.5
- Use popen() for get command results. Configuration file for guayadeque 
  (thanks to Fabian Frank) was added, support inheritance in mode definition, 
  add Set(popup,...) command, drop support of Set(text,wrap,..) command.
  Some configuration files reorganization.

* Sun Sep 4 2011 Mikhail Fedotov <anyremote at mail.ru> - 5.4.2
- Configuration file for Clementine (thanks to Lorenzo P�rez de Arce) and 
  DeadBeef (thanks to s_erge) were added.

* Tue Mar 15 2011 Mikhail Fedotov <anyremote at mail.ru> - 5.4.1
- Small bugfix. Configuration file for CMUS (thanks to Arthus Belliqueux) was added.

* Sat Feb 12 2011 Mikhail Fedotov <anyremote at mail.ru> - 5.4
- Fix work in AT-mode with Bluez 4.X

* Tue Oct 19 2010 Mikhail Fedotov <anyremote at mail.ru> - 5.3
- Support volume control through PulseAudio. Added configuration files for Miro player,
  MPRIS-compatible players. Some fixes in configuration files.

* Wed Aug 25 2010 Mikhail Fedotov <anyremote at mail.ru> - 5.2
- Enhanced support for Get(password) command. Properly handle ampersand in file
  names.

* Thu Jul 8 2010 Mikhail Fedotov <anyremote at mail.ru> - 5.1.3
- Some configuration files and documentation were corrected.
  Added configuration file for QMMP. 

* Sat Mar 13 2010 Mikhail Fedotov <anyremote at mail.ru> - 5.1.2
- Some configuration files and documentation were corrected.

* Wed Feb 03 2010 Mikhail Fedotov <anyremote at mail.ru> - 5.1.1
- Fixed Red Hat bugzilla bug 560182. Some configuration files and documentation
  were corrected.

* Mon Jan 04 2010 Mikhail Fedotov <anyremote at mail.ru> - 5.1
- Better support of Command Fusion's iViewer, tested on iPod Touch.
  Exclude keyjnote, kpdf, kuickshow, kview, noatun and KDE3-related 
  configuration files from the release. Added configuration file for Dragon player.
  Add KDE4 support in Kaffeine configuration file.

* Mon Sep 14 2009 Mikhail Fedotov <anyremote at mail.ru> - 5.0
- anyRemote was rewritten using multithreading and GLib.
  Native D-BUS support. Format of configuration file was significantly changed.

* Mon Mar 30 2009 Mikhail Fedotov <anyremote at mail.ru> - 4.18.1-1
- Add GuiAppModes tag to configuration files.

* Tue Mar 17 2009 Mikhail Fedotov <anyremote at mail.ru> - 4.18-1
- Get(password) and Get(ping) commands were added.
  Experimental support for iPhones/iPods with Command Fusion iViewer installed.

* Wed Feb 4 2009 Mikhail Fedotov <anyremote at mail.ru> - 4.17-1
- Fixed crash with all-in-one2.cfg. Added configuration files for Impressive
  (former KeyJnote, thanks to Cedric Barboiron).

* Tue Jan 27 2009 Mikhail Fedotov <anyremote at mail.ru> - 4.16-1
- Add possibility to set SDP service name. Corrections of configuration files.
  Configuration files for KsCD/KDE4 and Eye-of-Gnome were added.
  Created icon auto-upload feature.

* Fri Jan 16 2009 Mikhail Fedotov <anyremote at mail.ru> - 4.15-1
- Fixed crash issue in case of anyremote was runned without X.
  Fix hang in Load() command in case of empty file.

* Sat Jan 10 2009 Mikhail Fedotov <anyremote at mail.ru> - 4.14-1
- Small corrections in configuration files. Configuration files for AlsaPlayer, 
  Digikam (thanks to Marcus Hardt) and GPicView were added. 
  Syntax of Emulate() command was extended.

* Sun Dec 07 2008 Mikhail Fedotov <anyremote at mail.ru> - 4.13-1
- Small corrections in configuration files. Configuration file for WmCtrl and 
  Juk/KDE4 were added.

* Thu Nov 13 2008 Mikhail Fedotov <anyremote at mail.ru> - 4.12-1
- Added configuration file for XBMC (thanks to Everthon Valadao), Okular 
  Gwenview/KDE4 and Amarok2/KDE4. Support nonn-UTF8 encodings in 
  configurational files. Intergrated FreeBSD patch by Alex Samorukov.

* Mon Oct 20 2008 Mikhail Fedotov <anyremote at mail.ru> - 4.11-1
- Fixed issues with non-correct handling of files and directories names with 
  braces and brackets in some configuration files. 
  Several small changes in code.

* Mon Oct 6 2008 Mikhail Fedotov <anyremote at mail.ru> - 4.10-1
- Fixed issue with non-correct handling of files and directories names with 
  braces and brackets in some configuration files. A lot of changes in 
  documentation. Several small changes in code.

* Mon Sep 29 2008 Mikhail Fedotov <anyremote at mail.ru> - 4.9-1
- Get(version) command was introduced. Added possibility to create 
  user-specific phone initialization.

* Tue Sep 9 2008 Mikhail Fedotov <anyremote at mail.ru> - 4.8.1-1
- Small corrections.

* Thu Sep 4 2008 Mikhail Fedotov <anyremote at mail.ru> - 4.8-1
- Added configuration file for gThumb.
  Added GuiDescription field to configuration files.

* Thu Aug 7 2008 Mikhail Fedotov <anyremote at mail.ru> - 4.7.1-1
- Fix crash issue if no bluetooth service runned

* Tue Aug 5 2008 Mikhail Fedotov <anyremote at mail.ru> - 4.7-1
- Small enhancements

* Fri May 30 2008 Mikhail Fedotov <anyremote at mail.ru> - 4.6-1
- Small enhancements

* Sun May 18 2008 Mikhail Fedotov <anyremote at mail.ru> - 4.5-1
- Better integration with anyremote2http: -http command line 
  parameter was added.

* Fri Mar 07 2008 Mikhail Fedotov <anyremote at mail.ru> - 4.4-1.fc8
- Spec file correction. Some minor enhancemens.

* Sun Mar 02 2008 Mikhail Fedotov <anyremote at mail.ru> - 4.3-4.fc8
- Spec file correction. Move J2ME stuff out of the package.

* Tue Feb 26 2008 Mikhail Fedotov <anyremote at mail.ru> - 4.3-3.fc8
- Spec file correction

* Sun Feb 17 2008 Mikhail Fedotov <anyremote at mail.ru> - 4.3-2.fc8
- Spec file correction

* Fri Feb 15 2008 Mikhail Fedotov <anyremote at mail.ru> - 4.3-1.fc8
- Bugfixes and small enhancements.Support for touchscreen devices was improved

* Tue Jan 10 2008 Mikhail Fedotov <anyremote at mail.ru> - 4.2-1.fc8
- Spec file modified.
