Name:           tiled
Summary:        Tiled Map Editor

Version:        1.11.1
Release:        2%{?dist}

# tiled itself is GPLv2+, libtiled and tmxviewer are BSD
License:        GPL-2.0-or-later AND BSD-2-Clause

URL:            http://www.mapeditor.org
Source0:        https://github.com/mapeditor/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  libzstd-devel
BuildRequires:  make
BuildRequires:  qbs
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  python3-devel
BuildRequires:  zlib-devel

# qbs.i386 is disabled in F39+
ExcludeArch:    %{ix86}

%description
Tiled is a general purpose tile map editor. It is built to be easy to use,
yet flexible enough to work with varying game engines, whether your game
is an RPG, platformer or Breakout clone. Tiled is free software and written
in C++, using the Qt application framework.

This package contains the tiled application and tmxviewer, a simple application
to view Tiled maps.

%package devel
Summary:        Development headers for Tiled
License:        GPL-2.0-or-later
URL:            http://www.mapeditor.org
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Development headers for the Tiled map editor.


%package plugin-python
Summary:        Python plugin for Tiled
License:        GPL-2.0-or-later
URL:            http://www.mapeditor.org
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description plugin-python
A plugin for tiled which allows to write Python plugins.

%define pluginwarning Warning: This plugin does not offer full compatibility with Tileds features.


%package plugin-rpmap

Summary:        MapTool plugin for Tiled
License:        GPL-2.0-or-later
URL:            http://www.mapeditor.org
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description plugin-rpmap
A plugin for tiled which allows to save maps as rpmap MapTool maps.

%{pluginwarning}


%package plugin-tbin
Summary:        tBIN plugin for Tiled
License:        GPL-2.0-or-later
URL:            http://www.mapeditor.org
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description plugin-tbin
A plugin for tiled which allows support for the tBIN map format.

%{pluginwarning}


%package plugin-droidcraft
Summary:        Droidcraft plugin for Tiled
License:        GPL-2.0-or-later
URL:            http://www.mapeditor.org
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description plugin-droidcraft
A plugin for tiled which allows to save maps as .dat droidcraft maps.

%{pluginwarning}


%package plugin-flare
Summary:        Flare plugin for Tiled
License:        GPL-2.0-or-later
URL:            http://www.mapeditor.org
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description plugin-flare
A plugin for tiled which allows to save maps as .txt flare maps.

%{pluginwarning}


%package plugin-replica-island
Summary:        Replica Island plugin for Tiled
License:        GPL-2.0-or-later
URL:            http://www.mapeditor.org
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description plugin-replica-island
A plugin for tiled which allows to save maps as .bin Replica Island maps.

%{pluginwarning}


%package plugin-t-engine4
Summary:        T-Engine4 plugin for Tiled
License:        GPL-2.0-or-later
URL:            http://www.mapeditor.org
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description plugin-t-engine4
A plugin for tiled which allows to export maps as .lua T-Engine4 maps.

%{pluginwarning}


%package plugin-defold
Summary:        Defold plugin for Tiled
License:        GPL-2.0-or-later
URL:            http://www.mapeditor.org
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description plugin-defold
A plugin for tiled which allows to export maps as .tilemap Defold maps.

%{pluginwarning}


%package plugin-gmx
Summary:        GameMaker Studio 1.4 plugin for Tiled
License:        GPL-2.0-or-later
URL:            http://www.mapeditor.org
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description plugin-gmx
A plugin for tiled which allows to export maps
as GameMaker Studio 1.4 room files (.gmx).

%{pluginwarning}


%package plugin-yy
Summary:        GameMaker Studio 2.3 plugin for Tiled
License:        GPL-2.0-or-later
URL:            http://www.mapeditor.org
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description plugin-yy
A plugin for tiled which allows to export maps
as GameMaker Studio 2.3 room files (.yy).

%{pluginwarning}


%package plugin-tscn
Summary:        Godot 4 scene plugin for Tiled
License:        GPL-2.0-or-later
URL:            http://www.mapeditor.org
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description plugin-tscn
A plugin for tiled which allows to export maps
as Godot Engine 4 scene files (.tscn).

%{pluginwarning}


%prep
%setup -q

%patch -P1 -p1 -b .fix-build-against-qt6.8

# Remove copy of zlib
rm -rf src/zlib


%build
qbs setup-toolchains --detect
qbs setup-qt --detect

%global qbs_args config:release qbs.debugInformation:true qbs.installPrefix:"%{_prefix}" projects.Tiled.useRPaths:false projects.Tiled.installHeaders:true projects.Tiled.libDir:"%{_lib}"
qbs build %{qbs_args}


%install
qbs install --no-build --install-root %{buildroot} %{qbs_args}

# Clean build artefacts
find -name ".uic" -or -name ".moc" -or -name ".rcc" -delete

# locale files
%find_lang %{name} --with-qt

# Removed development file (this version does not install headers anyway)
# rm %{buildroot}/%{_libdir}/lib%{name}.so


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.mapeditor.Tiled.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/org.mapeditor.Tiled.appdata.xml


%ldconfig_scriptlets


%files -f %{name}.lang
%doc AUTHORS NEWS.md README.md COPYING LICENSE.GPL LICENSE.BSD
%{_bindir}/%{name}
%{_bindir}/terraingenerator
%{_bindir}/tmxrasterizer
%{_bindir}/tmxviewer
%{_datadir}/icons/hicolor/*/apps/*%{name}*
%{_datadir}/icons/hicolor/*/mimetypes/*%{name}*
%{_datadir}/applications/org.mapeditor.Tiled.desktop
%{_datadir}/metainfo/org.mapeditor.Tiled.appdata.xml
%{_datadir}/mime/packages/org.mapeditor.Tiled.xml
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/translations
%{_libdir}/lib%{name}*

%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/plugins/

# Core plugins
%{_libdir}/%{name}/plugins/libcsv.so
%{_libdir}/%{name}/plugins/libgmx.so
%{_libdir}/%{name}/plugins/libjson.so
%{_libdir}/%{name}/plugins/liblua.so
%{_libdir}/%{name}/plugins/libjson1.so
%{_libdir}/%{name}/plugins/libdefoldcollection.so

%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/tmxrasterizer.1*
%{_mandir}/man1/tmxviewer.1*
%dir %{_datadir}/thumbnailers
%{_datadir}/thumbnailers/%{name}.thumbnailer

%files devel
%{_includedir}/%{name}/

%files plugin-rpmap
%{_libdir}/%{name}/plugins/librpmap.so

%files plugin-python
%{_libdir}/%{name}/plugins/libpython.so

%files plugin-tbin
%{_libdir}/%{name}/plugins/libtbin.so

%files plugin-droidcraft
%{_libdir}/%{name}/plugins/libdroidcraft.so

%files plugin-flare
%{_libdir}/%{name}/plugins/libflare.so

%files plugin-replica-island
%{_libdir}/%{name}/plugins/libreplicaisland.so

%files plugin-t-engine4
%{_libdir}/%{name}/plugins/libtengine.so

%files plugin-defold
%{_libdir}/%{name}/plugins/libdefold.so

%files plugin-gmx
%{_libdir}/%{name}/plugins/libgmx.so

%files plugin-yy
%{_libdir}/%{name}/plugins/libyy.so

%files plugin-tscn
%{_libdir}/%{name}/plugins/libtscn.so

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jan 11 2025 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.11.1-1
- Update to v1.11.1
- Drop Patch0 (Qt6 issues - backport from this release)

* Mon Oct 14 2024 Jan Grulich <jgrulich@redhat.com> - 1.11.0-4
- Rebuild (qt6)

* Thu Jul 25 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.11.0-3
- Switch from building with Qt5 to Qt6 (rhbz#2298214)
- Build in release mode (rhbz#2260307)

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jun 27 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.11.0-1
- Update to v1.11.0

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.10.2-3
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Aug 05 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.10.2-1
- Update to v1.10.2

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.10.1-2
- Rebuilt for Python 3.12

* Tue Apr 04 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.10.1-1
- Update to v1.10.1
- Drop Patch0 (change the default plugin dir - now supported upstream)
- Migrate license tag to SPDX

* Sat Mar 11 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.10.0-1
- Update to v1.10.0

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 01 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.9.2-2
- Fix loading modules on 64-bit platforms (again)

* Mon Sep 19 2022 Filipe Rosset <rosset.filipe@gmail.com> - 1.9.2-1
- Update to 1.9.2 fixes rhbz#2127562

* Fri Aug 26 2022 Filipe Rosset <rosset.filipe@gmail.com> - 1.9.1-1
- Update to 1.9.1 fixes rhbz#1953129

* Wed Aug 24 2022 Filipe Rosset <rosset.filipe@gmail.com> - 1.8.6-1
- Update to 1.8.6

* Tue Aug 23 2022 Filipe Rosset <rosset.filipe@gmail.com> - 1.8.2-5
- Fix FTBFS for rawhide version 1.8.2 using qbs

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.8.4-2
- Rebuilt for Python 3.11

* Tue Apr 05 2022 josef radinger <cheese@nosuchhost.net> - 1.8.4-1
- bump version
- add qt5-qtsvg to BuildRequires

* Sat Mar 12 2022 josef radinger <cheese@nosuchhost.net> - 1.8.2-2
- switch to qbs

* Tue Feb 22 2022 josef radinger <cheese@nosuchhost.net> - 1.8.2-1
- bump version

* Sun Feb 13 2022 josef radinger <cheese@nosuchhost.net> - 1.8.1-1
- bump version

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 16 2021 josef radinger <cheese@nosuchhost.net> - 1.7.2-1
- bump version

* Wed Aug 04 2021 josef radinger <cheese@nosuchhost.net> - 1.7.1-1
- bump version

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 07 2021 Python Maint <python-maint@redhat.com> - 1.7.0-2
- Rebuilt for Python 3.10

* Mon Jun 07 2021 josef radinger <cheese@nosuchhost.net> - 1.7.0-1
- bump version

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.5.0-2
- Rebuilt for Python 3.10

* Fri Apr 09 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.5.0-1
- Update to 1.5.0 (fixes rhbz#1942186)
- Use archful dependencies on main package

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 2021 Filipe Rosset <rosset.filipe@gmail.com> - 1.4.3-1
- Update to 1.4.3 fixez rhbz#1848155

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 18 2020 Filipe Rosset <rosset.filipe@gmail.com> - 1.3.4-1
- Update to 1.3.4 fixes rhbz#1809805 + fix spec file changelog

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 25 2020 Filipe Rosset <rosset.filipe@gmail.com> - 1.3.2-1
- update to 1.3.2 fixes rhbz#1669013

* Mon Dec 16 2019 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.3.1-1
- Update to upstream

* Mon Aug 19 2019 Miro Hroncok <mhroncok@redhat.com> - 1.2.0-4
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep 28 2018 Filipe Rosset <rosset.filipe@gmail.com> - 1.2.0-1
- Rebuilt for new upstream release 1.2.0, fixes rhbz #1552361
- Added Python3 support

* Fri Sep 28 2018 Filipe Rosset <rosset.filipe@gmail.com> - 1.1.6-1
- Rebuilt for new upstream release 1.1.6, fixes rhbz #1552361
- Remove upstreamed patch

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Filipe Rosset <rosset.filipe@gmail.com> - 1.1.2-1
- Rebuilt for new upstream release 1.1.2, fixes rhbz #1531028
- TMW plugin: Removed since it is no longer needed
- tBIN plugin: Added read/write support for the tBIN map format

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.3-2
- Remove obsolete scriptlets

* Thu Sep 21 2017 Erik Schilling <ablu.erikschilling@googlemail.com> - 1.0.3-1
- New release 1.0.3
- Added subpackage for gmx plugin

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Apr 21 2017 Filipe Rosset <rosset.filipe@gmail.com> - 0.18.2-1
- Rebuilt for new upstream release 0.18.2, fixes rhbz #1406593 #1435926

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 03 2016 Filipe Rosset <rosset.filipe@gmail.com> - 0.17.2-1
- Rebuilt for new upstream release 0.17.2, fixes rhbz #1392732

* Thu Sep 01 2016 Erik Schilling <ablu.erikschilling@googlemail.com> - 0.17.0-1
- New release 0.17.0
- Added subpackage for defold plugin

* Tue Apr 19 2016 Erik Schilling <ablu.erikschilling@googlemail.com> - 0.16.0-1
- New upstream release 0.16.0

* Sun Mar 06 2016 Erik Schilling <ablu.erikschilling@googlemail.com> - 0.15.2-1
- New bugfix release 0.15.2

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.15.0-2
- use %%qmake_qt5 to ensure proper build flags

* Sat Jan 09 2016 Erik Schilling <ablu.erikschilling@googlemail.com> - 0.15.0-1
- New upstream release 0.15.0

* Fri Nov 27 2015 Erik Schilling <ablu.erikschilling@googlemail.com> - 0.14.2-1
- New upstream release 0.14.2

* Mon Sep 21 2015 Erik Schilling <ablu.erikschilling@googlemail.com> - 0.14.0-1
- New upstream release

* Tue Sep 08 2015 Erik Schilling <ablu.erikschilling@googlemail.com> - 0.13.1-1
- New upstream release

* Sat Aug 15 2015 Erik Schilling <ablu.erikschilling@googlemail.com> - 0.13.0-1
- New upstream release

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 2 2015 Erik Schilling <ablu.erikschilling@googlemail.com> - 0.12.3-1
- New upstream release

* Fri May 22 2015 Erik Schilling <ablu.erikschilling@googlemail.com> - 0.12.2-1
- New upstream release

* Wed May 20 2015 Erik Schilling <ablu.erikschilling@googlemail.com> - 0.12.1-1
- New upstream release

* Fri May 15 2015 Erik Schilling <ablu.erikschilling@googlemail.com> - 0.12.0-1
- New upstream release

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.11.0-2
- Rebuilt for GCC 5 C++11 ABI change

* Sun Jan 11 2015 Erik Schilling <ablu.erikschilling@googlemail.com> - 0.11.0-1
- New upstream release

* Mon Oct 27 2014 Erik Schilling <ablu.erikschilling@googlemail.com> - 0.10.2-1
- New bugfix release

* Mon Sep 22 2014 Erik Schilling <ablu.erikschilling@googlemail.com> - 0.10.1-1
- New bugfix release

* Sun Sep 14 2014 Erik Schilling <ablu.erikschilling@googlemail.com> - 0.10.0-1
- New upstream release

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Mar 15 2014 Erik Schilling <ablu.erikschilling@googlemail.com> - 0.9.1-2
- Fixed detection of plugins on 64bit
- Splitted plugins into subpackages

* Sat Jul 27 2013 Erik Schilling <ablu.erikschilling@googlemail.com> 0.9.1-1
- New upstream release 0.9.1

* Sat Jan 12 2013 Erik Schilling <ablu.erikschilling@googlemail.com> 0.9.0-1
- New upstream release 0.9.0
- Dropped now obsolete patches and files

* Mon Sep 3 2012 Erik Schilling <ablu.erikschilling@googlemail.com> 0.8.1-3
- Fixed preserving of timestamps in install command.
- Fixed typo in permission setting.
- Talked with upstream about license mismatch in headers.
- Those headers were outdated.

* Mon Sep 3 2012 Erik Schilling <ablu.erikschilling@googlemail.com> 0.8.1-2
- Added note about which parts are licensed with which license.
- Made sure that the copy of zlib inside of the source is removed.
- Fixed handling of locales (using %%find_lang).
- Avoided plain asterisks in %%files.
- Made description clear about containing the tmxviewer.

* Sun Sep 2 2012 Erik Schilling <ablu.erikschilling@googlemail.com> 0.8.1-1
- First version for official fedora repos.
