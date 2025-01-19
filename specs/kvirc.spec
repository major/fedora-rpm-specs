%if 0%{?fedora} >= 40
%global qt_ver    6
%else
%global qt_ver    5
%endif

Name:             kvirc
Version:          5.2.6
Release:          2%{?dist}
Summary:          Free portable IRC client
# Automatically converted from old format: GPLv2+ with exceptions - review is highly recommended.
License:          LicenseRef-Callaway-GPLv2+-with-exceptions
URL:              https://www.kvirc.net/
%global forgeurl  https://github.com/kvirc/KVIrc
Source:           %{forgeurl}/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz
# https://fedoraproject.org/wiki/Packaging:CryptoPolicies
Patch:            kvirc-5.0.0_enforce_system_crypto.patch

BuildRequires:    enchant2-devel
BuildRequires:    audiofile-devel
BuildRequires:    glib2-devel
BuildRequires:    perl-devel
BuildRequires:    perl-ExtUtils-Embed
BuildRequires:    python3-devel
BuildRequires:    cmake3
BuildRequires:    ninja-build
BuildRequires:    extra-cmake-modules
BuildRequires:    desktop-file-utils
BuildRequires:    gettext
BuildRequires:    doxygen
BuildRequires:    graphviz
BuildRequires:    libtheora-devel
BuildRequires:    libvorbis-devel
BuildRequires:    zlib-devel
BuildRequires:    openssl-devel
BuildRequires:    cmake(KF%{qt_ver}CoreAddons)
BuildRequires:    cmake(KF%{qt_ver}I18n)
BuildRequires:    cmake(KF%{qt_ver}KIO)
BuildRequires:    cmake(KF%{qt_ver}Notifications)
BuildRequires:    cmake(KF%{qt_ver}Parts)
BuildRequires:    cmake(KF%{qt_ver}Service)
%if %{qt_ver} >= 6
BuildRequires:    cmake(KF%{qt_ver}StatusNotifierItem)
%endif
BuildRequires:    cmake(KF%{qt_ver}WindowSystem)
BuildRequires:    cmake(KF%{qt_ver}XmlGui)
BuildRequires:    cmake(Phonon4Qt%{qt_ver})
BuildRequires:    cmake(Qt%{qt_ver}Concurrent)
BuildRequires:    cmake(Qt%{qt_ver}Core)
BuildRequires:    cmake(Qt%{qt_ver}DBus)
BuildRequires:    cmake(Qt%{qt_ver}Multimedia)
BuildRequires:    cmake(Qt%{qt_ver}Network)
BuildRequires:    cmake(Qt%{qt_ver}PrintSupport)
BuildRequires:    cmake(Qt%{qt_ver}Sql)
BuildRequires:    cmake(Qt%{qt_ver}Svg)
BuildRequires:    cmake(Qt%{qt_ver}Widgets)
BuildRequires:    cmake(Qt%{qt_ver}Xml)
%if %{qt_ver} < 6
BuildRequires:    cmake(Qt5X11Extras)
%ifarch %{?qt5_qtwebengine_arches}
BuildRequires:    cmake(Qt5WebEngineWidgets)
%endif
%else
BuildRequires:    cmake(Qt6Core5Compat)
%ifarch %{?qt6_qtwebengine_arches}
BuildRequires:    cmake(Qt6WebEngineWidgets)
%endif
%endif

%description
KVIrc is a free portable IRC client based on the excellent
Qt GUI toolkit. KVirc is being written by Szymon Stefanek
and the KVIrc Development Team with the contribution of
many IRC addicted developers around the world.

%prep
%autosetup -p1 -n KVIrc-%{version}

%build
%{cmake3}  \
-GNinja \
-DCMAKE_SKIP_RPATH=ON \
-DQT_VERSION_MAJOR=%{qt_ver} \
-DWANT_ENV_FLAGS=ON \
-DWANT_DCC_VIDEO=OFF \
-DWANT_OGG_THEORA=ON \
-DWANT_GTKSTYLE=ON \
-DADDITIONAL_LINK_FLAGS='-Wl,--as-needed' \
%{nil}


%cmake_build

%install
%cmake_install

desktop-file-validate \
    %{buildroot}%{_datadir}/applications/net.kvirc.KVIrc5.desktop

ln -sf ../../%{name}/5.2/license/COPYING COPYING

# Delete zero length file
rm %{buildroot}%{_datadir}/kvirc/5.2/help/en/_db_widget.idx

rm %{buildroot}%{_bindir}/kvirc-config
rm %{buildroot}%{_libdir}/libkvilib.so

%find_lang %{name} --all-name

%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING
%doc RELEASES
%{_bindir}/%{name}
%{_libdir}/libkvilib.so.5*
%{_datadir}/applications/net.kvirc.KVIrc5.desktop
%{_libdir}/%{name}/
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/5.2
%dir %{_datadir}/%{name}/5.2/locale
%{_datadir}/%{name}/5.2/audio/
%{_datadir}/%{name}/5.2/config/
%{_datadir}/%{name}/5.2/defscript/
%{_datadir}/%{name}/5.2/help/
%{_datadir}/%{name}/5.2/modules/
%{_datadir}/%{name}/5.2/msgcolors/
%{_datadir}/%{name}/5.2/pics/
%{_datadir}/%{name}/5.2/themes/
%{_datadir}/%{name}/5.2/license/
%{_datadir}/icons/hicolor/*/apps/kvirc.*
%{_datadir}/icons/hicolor/*/mimetypes/application-x-kva.*
%{_datadir}/icons/hicolor/*/mimetypes/application-x-kvt.*
%{_datadir}/icons/hicolor/*/mimetypes/text-x-kvc.*
%{_datadir}/icons/hicolor/*/mimetypes/text-x-kvs.*
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/%{name}.1.gz

# Translation files
%lang(de) %{_mandir}/de/man1/%{name}.1.gz
%lang(fr) %{_mandir}/fr/man1/%{name}.1.gz
%lang(it) %{_mandir}/it/man1/%{name}.1.gz
%lang(pt) %{_mandir}/pt/man1/%{name}.1.gz
%lang(uk) %{_mandir}/uk/man1/%{name}.1.gz

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Dec 10 2024 Alexey Kurov <nucleo@fedoraproject.org> - 5.2.6-1
- KVIrc 5.2.6

* Mon Sep 16 2024 Alexey Kurov <nucleo@fedoraproject.org> - 5.2.4-1
- KVIrc 5.2.4

* Mon Sep  02 2024 Miroslav Suchý <msuchy@redhat.com> - 5.2.0-11
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 12 2024 Jitka Plesnikova <jplesnik@redhat.com> - 5.2.0-9
- Perl 5.40 rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 5.2.0-8
- Rebuilt for Python 3.13

* Tue May 21 2024 Jan Grulich <jgrulich@redhat.com> - 5.2.0-7
- Rebuild (qt6)

* Mon May  06 2024 Alexey Kurov <nucleo@fedoraproject.org> - 5.2.0-6
- migrate to enchant++ to avoid use of private API in enchant-provider.h

* Thu Apr 04 2024 Jan Grulich <jgrulich@redhat.com> - 5.2.0-5
- Rebuild (qt6)

* Sat Feb 17 2024 Jan Grulich <jgrulich@redhat.com> - 5.2.0-4
- Rebuild (qt6)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Alexey Kurov <nucleo@fedoraproject.org> - 5.2.0-2
- Require Qt6WebEngineWidgets for qt6_qtwebengine_arches

* Sun Jan 21 2024 Aleksei Bavshin <alebastr@fedoraproject.org> - 5.2.0-1
- Update to 5.2.0
- Build with Qt6/KF6 on f40
- Use cmake() for Qt and KF dependencies

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Nov 20 2023 Leigh Scott <leigh123linux@gmail.com> - 5.0.0-22
- Fix crash on startup when running wayland (rhbz#2250579)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 5.0.0-20
- Perl 5.38 rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 5.0.0-17
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 5.0.0-15
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 5.0.0-13
- Perl 5.34 rebuild

* Tue Jan 26 2021 Alexey Kurov <nucleo@fedoraproject.org> - 5.0.0-12
- Fix build with Qt 5.15+

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 5.0.0-9
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 13 2019 Alexey Kurov <nucleo@fedoraproject.org> - 5.0.0-7
- rebuild

* Tue Aug 13 2019 Alexey Kurov <nucleo@fedoraproject.org> - 5.0.0-6
- Disable python support [Bug 1738031]

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 5.0.0-4
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Björn Esser <besser82@fedoraproject.org> - 5.0.0-2
- Append curdir to CMake invokation. (#1668512)

* Wed Jan 02 2019 Alexey Kurov <nucleo@fedoraproject.org> - 5.0.0-1
- KVIrc 5.0.0
- Switch to BuildRequires: enchant2-devel

* Wed Aug 01 2018 Leigh Scott <leigh123linux@googlemail.com> - 5.0.0-0.16.beta1
- Switch to BuildRequires: openssl-devel
- Fix disconnection issue with openssl-devel

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-0.15.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 5.0.0-0.14.beta1
- Perl 5.28 rebuild

* Sun Feb 25 2018 Leigh Scott <leigh123linux@googlemail.com> - 5.0.0-0.13.beta1
- Install lang files properly
- Fix scriptlets
- Use ninja to build

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-0.12.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 09 2018 Leigh Scott <leigh123linux@googlemail.com> - 5.0.0-0.11.beta1
- Fix some rpmlint warnings/errors

* Tue Jan 09 2018 Leigh Scott <leigh123linux@googlemail.com> - 5.0.0-0.10.beta1
- KVIrc 5.0.0 beta1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-0.9.alpha2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-0.8.alpha2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 12 2017 Leigh Scott <leigh123linux@googlemail.com> - 5.0.0-0.7.alpha2
- Switch to compat-openssl10-devel
- Fix FTBFS (rhbz 1423830)

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 5.0.0-0.6.alpha2
- Perl 5.26 rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-0.5.alpha2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 5.0.0-0.4.alpha2
- Perl 5.24 rebuild

* Sun Mar 20 2016 Alexey Kurov <nucleo@fedoraproject.org> - 5.0.0-0.3.alpha2
- KVIrc 5.0.0 alpha2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-0.2.alpha1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan  3 2016 Alexey Kurov <nucleo@fedoraproject.org> - 5.0.0-0.1.alpha1
- KVIrc 4.9.1
- switch to Qt5 and KF5

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 4.2.0-15
- Perl 5.22 rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 4.2.0-14
- Rebuilt for GCC 5 C++11 ABI change

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 4.2.0-13
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Aug 12 2014 Rex Dieter <rdieter@fedoraproject.org> 4.2.0-11
- add mime scriptlet

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 24 2013 Alexey Kurov <nucleo@fedoraproject.org> - 4.2.0-8
- fix deprecated v4l interfaces in 3.9 kernel

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Oct 11 2012 Alexey Kurov <nucleo@fedoraproject.org> - 4.2.0-5
- rebuild for audiofile-0.3.4

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul  2 2012 Alexey Kurov <nucleo@fedoraproject.org> - 4.2.0-3
- fix epel build

* Mon Jul  2 2012 Alexey Kurov <nucleo@fedoraproject.org> - 4.2.0-2
- new tarball

* Sun Jul  1 2012 Alexey Kurov <nucleo@fedoraproject.org> - 4.2.0-1
- KVIrc 4.2.0
- drop BR: cryptopp-devel, esound-devel

* Thu Jan  5 2012 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.4-3
- fix build with gcc-4.7.0

* Tue Jul 12 2011 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.4-2
- BR: qt-webkit-devel

* Sun Mar 20 2011 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.4-1
- KVIrc 4.0.4

* Thu Feb 10 2011 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.2-8
- V4L1 disabled only for F15+

* Thu Feb 10 2011 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.2-7
- disabled V4L1 support

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.2-5
- fix the color issues with recent gtk packages kvirc#1010

* Thu Nov 25 2010 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.2-4
- depends on kdelibs version used at build time

* Tue Nov 23 2010 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.2-3
- fix join channel crash #656251, kvirc#1024

* Mon Aug  2 2010 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.2-2
- fix tray issue kvirc#872

* Mon Aug  2 2010 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.2-1
- KVIrc 4.0.2

* Tue Jul 27 2010 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.0-3
- fix for kvirc#858

* Tue Jul 27 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.0.0-2
- rebuild (python27)

* Mon Jun 28 2010 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.0-1
- KVIrc 4.0

* Sun Apr 18 2010 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.0-0.27.rc3
- fix in help borwser (r4258)

* Sat Apr 17 2010 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.0-0.26.rc3
- update to 4.0 rc3

* Fri Feb 26 2010 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.0-0.25.20100226svn4030
- svn snapshot 4030
- added -DCMAKE_SKIP_RPATH=ON to fix F13+ rpath issue

* Sun Feb 21 2010 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.0-0.24.20100221svn4000
- svn 4000 (SASL support implemented)

* Fri Feb 12 2010 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.0-0.23.20100212svn3956
- svn 3956 (should fix irc7 Excess Flood issue)

* Tue Dec 29 2009 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.0-0.21.rc2
- fix log files date format from svn 3762

* Sat Dec 19 2009 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.0-0.20.rc2
- KVIrc 4.0 release candidate 2
- added BR cryptopp-devel and -DWANT_NO_EMBEDDED_CODE=ON
- re-enabled pyhton module -DWITHOUT_PYTHON=OFF
- added BR python-devel

* Wed Sep  9 2009 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.0-0.17.rc1
- disabled pyhton module, added -DWITHOUT_PYTHON=ON
- removed BR python-devel

* Tue Sep  8 2009 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.0-0.16.rc1
- KVIrc 4.0 release candidate 1

* Mon Aug 31 2009 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.0-0.15.20090831svn3442
- svn snapshot 3442 that includes option for using environment variables
- Added -DUSE_ENV_FLAGS=ON for using default compiler flags

* Sat Aug 29 2009 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.0-0.13.20090827svn3429
- rebuilt with new openssl

* Thu Aug 27 2009 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.0-0.11.20090827svn3429
- svn snapshot 3429 that includes patch for openssl >=1.0

* Thu Aug 27 2009 Tomas Mraz <tmraz@redhat.com> - 4.0.0-0.10.20090826svn3426
- rebuilt with new openssl

* Wed Aug 26 2009 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.0-0.9.20090826svn3426
- svn snapshot 3426
- Added -DWANT_COEXISTENCE=OFF, binary name changed to kvirc
- Added -DWITH_ix86_ASM and -DMANUAL_REVISION
- Added BR: esound-devel

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.0-0.7.20090409svn3173
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Apr  9 2009 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.0-0.6.20090409svn3173
- svn snapshot 3173
- Summary changed to Free portable IRC client

* Mon Apr  6 2009 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.0-0.5.20090404svn3172
- patch for using standard compiler flags

* Sun Apr  5 2009 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.0-0.4.20090404svn3172
- symlink to COPYING

* Sat Apr  4 2009 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.0-0.3.20090404svn3172
- Exclude duplicate files
- svn snapshot 3172
- BR dbus-devel

* Sat Mar 28 2009 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.0-0.2.20090328svn3168
- Fixed owner of /usr/share/kvirc
- Changed release tag and license field
- Fixed owner of /usr/share/kvirc/4.0 and /usr/share/kvirc/4.0/locale
- caps dir included in package

* Sat Mar 28 2009 Alexey Kurov <nucleo@fedoraproject.org> - 4.0-0.5.svn3168
- Use update-desktop-database and gtk-update-icon-cache instead of xdg-utils

* Fri Mar 20 2009 Alexey Kurov <nucleo@fedoraproject.org> - 4.0-0.4.svn3151
- Initial RPM release
