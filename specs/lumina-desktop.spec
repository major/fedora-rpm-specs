# TODO: themes
%global srcname     lumina

Summary:            A lightweight, portable desktop environment
Name:               %{srcname}-desktop
Version:            1.6.2
Release:            14%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License:            LicenseRef-Callaway-BSD
URL:                http://%{name}.org
Source0:            https://github.com/lumina-desktop/%{srcname}/archive/v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
# Qt requirements
BuildRequires:      qt5-qtbase-devel
BuildRequires:      qt5-qttools-devel
BuildRequires:      qt5-qtmultimedia-devel
BuildRequires:      qt5-qtdeclarative-devel
BuildRequires:      qt5-qtsvg-devel
BuildRequires:      qt5-qtx11extras-devel
BuildRequires:      qt5-linguist

# X component requirements
BuildRequires:      xcb-util-image-devel
BuildRequires:      xcb-util-wm-devel
BuildRequires:      libxcb-devel
BuildRequires:      xcb-util-devel
BuildRequires:      libXcomposite-devel
BuildRequires:      libXdamage-devel
BuildRequires:      libXrender-devel
# theme-engine
BuildRequires:      libXcursor-devel
BuildRequires:      qt5-qtbase-private-devel
BuildRequires:      qt5-qtbase-static

BuildRequires:      pam-devel
BuildRequires:      desktop-file-utils
BuildRequires:      make

# Runtime requirements
Requires:           firstboot(windowmanager)
Requires:           %{name}-filesystem = %{version}-%{release}
Requires:           %{name}-data = %{version}-%{release}
Requires:           %{srcname}-open%{?_isa} = %{version}-%{release}
Requires:           %{srcname}-info%{?_isa} = %{version}-%{release}
Requires:           %{srcname}-themeengine%{?_isa} = %{version}-%{release}

# Desktop extensions
%if 0%{?fedora}
# core utils
Suggests:           %{srcname}-config%{?_isa} = %{version}-%{release}
Suggests:           %{srcname}-search%{?_isa} = %{version}-%{release}
Suggests:           %{srcname}-xconfig%{?_isa} = %{version}-%{release}
# desktop utils
Suggests:           %{srcname}-archiver%{?_isa} = %{version}-%{release}
Suggests:           %{srcname}-fileinfo%{?_isa} = %{version}-%{release}
Suggests:           %{srcname}-fm%{?_isa} = %{version}-%{release}
Suggests:           %{srcname}-mediaplayer%{?_isa} = %{version}-%{release}
Suggests:           %{srcname}-photo%{?_isa} = %{version}-%{release}
Suggests:           %{srcname}-screenshot%{?_isa} = %{version}-%{release}
Suggests:           %{srcname}-textedit%{?_isa} = %{version}-%{release}
# others
Suggests:           %{srcname}-icons = %{version}-%{release}
Suggests:           la-capitaine-icon-theme
%endif

%description
The Lumina Desktop Environment is a lightweight system interface
that is designed for use on any Unix-like operating system.

%package            filesystem
Summary:            Common folders for Lumina Desktop
BuildArch:          noarch
Obsoletes:          %{name}-libs < 1.2.0

%description        filesystem
This package provides the common folders for the Lumina Desktop Environment.

%package            data
Summary:            Data for Lumina Desktop
BuildArch:          noarch
Requires:           %{name}-filesystem = %{version}-%{release}

%description        data
This package provides the data files for the Lumina Desktop
Environment: Colors, desktop background, theme templates.

%package -n         %{srcname}-open
Summary:            xdg-open style utility for Lumina Desktop
Requires:           %{name}-filesystem = %{version}-%{release}

%description -n     %{srcname}-open
This package provides %{srcname}-open, which handles opening of
files and URLs according to the system-wide mimetype association.
It also provides an optional selector if more than one application
is assigned with the given url or file type.

%package -n         %{srcname}-info
Summary:            Basic information utility for Lumina Desktop
Requires:           %{name}-filesystem = %{version}-%{release}

%description -n     %{srcname}-info
This package provides %{srcname}-info, which is a simple
utility that displays various information about the Lumina
installation, like paths, contributors, license or version.

%package -n         %{srcname}-themeengine
# Automatically converted from old format: MIT - review is highly recommended.
License:            MIT
Summary:            Theme engine for Lumina Desktop
Requires:           %{name}-filesystem = %{version}-%{release}

%description -n     %{srcname}-themeengine
This package provides %{srcname}-theme-engine.

%package -n         %{srcname}-config
Summary:            Configuration utility for Lumina Desktop
Requires:           %{name}-filesystem = %{version}-%{release}

%description -n     %{srcname}-config
This package provides %{srcname}-config, which allows changing
various aspects of %{srcname} and fluxbox, like the wallpaper being
used, theme, icons, panel (and plugins), startup and default
applications, desktop menu and more.

%package -n         %{srcname}-xconfig
Summary:            X server display configuration tool for Lumina Desktop
Requires:           %{name}-filesystem = %{version}-%{release}

%description -n     %{srcname}-xconfig
This package provides %{srcname}-xconfig, which is a simple
multi-head aware display configuration tool for configuring
the X server.

%package -n         %{srcname}-search
Summary:            Search utility for Lumina Desktop
Requires:           %{name}-filesystem = %{version}-%{release}

%description -n     %{srcname}-search
This package provides %{srcname}-search, which is a simple
search utility that allows to search for applications or
files and directories in the home directory and launch
or open them.

%package -n         %{srcname}-archiver
Summary:            Archiver for Lumina Desktop
Requires:           %{name}-filesystem = %{version}-%{release}

%description -n     %{srcname}-archiver
Front-end to tar, used for managing/creating archives.

%package -n         %{srcname}-fileinfo
Summary:            Desktop file editor for Lumina Desktop
Requires:           %{name}-filesystem = %{version}-%{release}

%description -n     %{srcname}-fileinfo
File properties viewer, and simple XDG application registration creator.

%package -n         %{srcname}-fm
Summary:            File manager for Lumina Desktop
Requires:           %{name}-filesystem = %{version}-%{release}

%description -n     %{srcname}-fm
This package provides %{srcname}-fm, which is a simple file manager
with support for multiple view modes, tabbed browsing,
including an integrated slideshow-based picture viewer.

%package -n         %{srcname}-mediaplayer
Summary:            Mediaplayer for Lumina Desktop
Requires:           %{name}-filesystem = %{version}-%{release}

%description -n     %{srcname}-mediaplayer
Simple media player with hooks for streaming from online radio services.

%package -n         %{srcname}-photo
Summary:            Image viewer for Lumina Desktop
Requires:           %{name}-filesystem = %{version}-%{release}

%description -n     %{srcname}-photo
Simple image viewer.

%package -n         %{srcname}-screenshot
Summary:            Screenshot utility for Lumina Desktop
Requires:           %{name}-filesystem = %{version}-%{release}

%description -n     %{srcname}-screenshot
This package provides %{srcname}-screenshot, which is a simple
screenshot utility that allows to snapshot the whole desktop
or a single window after a configurable delay.

Optionally the window border can be hidden when taking a
screenshot of a single window.

%package -n         %{srcname}-textedit
Summary:            Text file editor for Lumina Desktop
Requires:           %{name}-filesystem = %{version}-%{release}

%description -n     %{srcname}-textedit
Plaintext editor with syntax highlighting, tab support, and find/replace functionality.

%package -n         material-design-dark
# Automatically converted from old format: Apache 2.0 - review is highly recommended.
License:            Apache-2.0
Summary:            Material Design icon theme (dark)
BuildArch:          noarch

%description -n     material-design-dark
Optional icons theme recommended for Lumina Desktop (dark version).

%package -n         material-design-light
# Automatically converted from old format: Apache 2.0 - review is highly recommended.
License:            Apache-2.0
Summary:            Material Design icon theme (light)
BuildArch:          noarch

%description -n     material-design-light
Optional icons theme recommended for Lumina Desktop (light version).

%package -n         %{srcname}-icons
# Automatically converted from old format: CC-BY - review is highly recommended.
License:            LicenseRef-Callaway-CC-BY
Summary:            Icon set for Lumina Desktop
BuildArch:          noarch

%description -n     %{srcname}-icons
Optional icons theme recommended for Lumina Desktop (new).

########################################################################################
%prep
%autosetup -n%{srcname}-%{version} -p 0
desktop-file-edit --remove-key=Categories --remove-only-show-in=Lumina --add-only-show-in=X-Lumina \
 src-qt5/core/%{srcname}-info/%{srcname}-support.desktop
for i in `grep -lir 'OnlyShowIn=Lumina' src-qt5`
do
 desktop-file-edit --remove-only-show-in=Lumina --add-only-show-in=X-Lumina $i
done


%build
%qmake_qt5 *.pro \
 CONFIG+=configure \
 LIBPREFIX="%{_libdir}" \
 L_BINDIR="%{_bindir}" \
 L_LIBDIR=%{_libdir} \
 L_SHAREDIR=%{_datadir} \
 L_ETCDIR=%{_sysconfdir} \
 L_INCLUDEDIR=%{_includedir} \
 L_MANDIR=%{_mandir} \
 QT5LIBDIR="%{_qt5_prefix}" \
 QMAKE_LFLAGS+="-Wl,--as-needed"
# make translations
for i in `find . -type d -name i18n`; do lrelease-qt5 -silent -nounfinished $i/*.ts; done
%make_build


%install
%if 0%{?rhel}
install -d %{buildroot}%{_sysconfdir}
%endif
%make_install INSTALL_ROOT=%{buildroot}
install -d %{buildroot}%{_datadir}/%{name}/i18n
for i in `find . -type d -name i18n`
do
 install -m0644 -D $i/*.qm -t %{buildroot}%{_datadir}/%{name}/i18n/
done

# split locales into subpackages
%find_lang %{name} --with-qt
%find_lang %{srcname}-info --with-qt
%find_lang %{srcname}-open --with-qt
%find_lang %{srcname}-config --with-qt
%find_lang %{srcname}-search --with-qt
%find_lang %{srcname}-xconfig --with-qt
%find_lang l-archiver --with-qt
%find_lang l-fileinfo --with-qt
%find_lang %{srcname}-fm --with-qt
%find_lang l-mediap --with-qt
%find_lang l-photo --with-qt
%find_lang l-screenshot --with-qt
%find_lang l-te --with-qt

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{srcname}-*.desktop

########################################################################################

%files -f %{name}.lang
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/start-%{name}
%{_bindir}/%{srcname}-sudo
%{_bindir}/%{srcname}-pingcursor
%config %{_sysconfdir}/%{srcname}Desktop.conf.dist
%{_datadir}/icons/hicolor/scalable/apps/Lumina-DE.svg
%{_datadir}/xsessions/Lumina-DE.desktop
%{_datadir}/applications/%{srcname}-support.desktop
%{_mandir}/man1/%{name}.1.gz
%{_mandir}/man8/start-%{name}.8.gz

%files filesystem
# each binary expects its locale files in the common folder
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/i18n

%files data
%{_datadir}/%{name}/
%exclude %{_datadir}/%{name}/i18n

%files -n %{srcname}-open -f %{srcname}-open.lang
%{_bindir}/%{srcname}-open
%{_mandir}/man1/%{srcname}-open.1.gz

%files -n %{srcname}-info -f %{srcname}-info.lang
%{_bindir}/%{srcname}-info
%{_datadir}/applications/%{srcname}-info.desktop
%{_mandir}/man1/%{srcname}-info.1.gz

%files -n %{srcname}-themeengine
%license src-qt5/core/lumina-theme-engine/LICENSE
%{_bindir}/lthemeengine*
%{_libdir}/qt5/plugins/platformthemes/*
%{_libdir}/qt5/plugins/styles/*
%{_datadir}/applications/lthemeengine.desktop
%{_datadir}/lthemeengine/

%files -n %{srcname}-config -f %{srcname}-config.lang
%{_bindir}/%{srcname}-config
%{_datadir}/applications/%{srcname}-config.desktop
%{_mandir}/man1/%{srcname}-config.1.gz

%files -n %{srcname}-xconfig -f %{srcname}-xconfig.lang
%{_bindir}/%{srcname}-xconfig
%{_datadir}/applications/%{srcname}-xconfig.desktop
%{_mandir}/man1/%{srcname}-xconfig.1.gz

%files -n %{srcname}-search -f %{srcname}-search.lang
%{_bindir}/%{srcname}-search
%{_datadir}/applications/%{srcname}-search.desktop
%{_mandir}/man1/%{srcname}-search.1.gz

%files -n %{srcname}-archiver -f l-archiver.lang
%{_bindir}/%{srcname}-archiver
%{_datadir}/applications/%{srcname}-archiver.desktop
%{_mandir}/man1/%{srcname}-archiver.1.gz

%files -n %{srcname}-fileinfo -f l-fileinfo.lang
%{_bindir}/%{srcname}-fileinfo
%{_datadir}/applications/%{srcname}-fileinfo.desktop
%{_mandir}/man1/%{srcname}-fileinfo.1.gz

%files -n %{srcname}-fm -f %{srcname}-fm.lang
%{_bindir}/%{srcname}-fm
%{_datadir}/icons/hicolor/scalable/apps/Insight-FileManager.svg
%{_datadir}/applications/%{srcname}-fm.desktop
%{_mandir}/man1/%{srcname}-fm.1.gz

%files -n %{srcname}-mediaplayer -f l-mediap.lang
%{_bindir}/%{srcname}-mediaplayer
%{_datadir}/applications/%{srcname}-mediaplayer.desktop
%{_datadir}/applications/%{srcname}-mediaplayer-pandora.desktop
%{_mandir}/man1/%{srcname}-mediaplayer.1.gz

%files -n %{srcname}-photo -f l-photo.lang
%{_bindir}/%{srcname}-photo
%{_datadir}/applications/%{srcname}-photo.desktop
%{_mandir}/man1/%{srcname}-photo.1.gz

%files -n %{srcname}-screenshot -f l-screenshot.lang
%{_bindir}/%{srcname}-screenshot
%{_datadir}/applications/%{srcname}-screenshot.desktop
%{_mandir}/man1/%{srcname}-screenshot.1.gz

%files -n %{srcname}-textedit -f l-te.lang
# W: dangling-symlink /usr/bin/lte /usr/bin/lumina-textedit
%exclude %{_bindir}/lte
%{_bindir}/%{srcname}-textedit
%{_datadir}/applications/%{srcname}-textedit.desktop
%{_mandir}/man1/%{srcname}-textedit.1.gz

%files -n material-design-dark
%license icon-theme/material-design-dark/LICENSE
%{_datadir}/icons/material-design-dark/
%exclude %{_datadir}/icons/material-design-dark/LICENSE

%files -n material-design-light
%license icon-theme/material-design-light/LICENSE
%{_datadir}/icons/material-design-light/
%exclude %{_datadir}/icons/material-design-light/LICENSE

%files -n %{srcname}-icons
%license icon-theme/lumina-icons/LICENSE
%{_datadir}/icons/lumina-icons/
%exclude %{_datadir}/icons/lumina-icons/LICENSE

########################################################################################
%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.6.2-13
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Oct 18 2022 TI_Eugene <ti.eugene@gmail.com) - 1.6.2-7
- Hard dependencies on fluxbox and *oxygen* removed

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 14 2022 Jan Grulich <jgrulich@redhat.com> - 1.6.2-5
- Rebuild (qt5)

* Tue May 17 2022 Jan Grulich <jgrulich@redhat.com> - 1.6.2-4
- Rebuild (qt5)

* Tue Mar 08 2022 Jan Grulich <jgrulich@redhat.com> - 1.6.2-3
- Rebuild (qt5)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild


* Wed Dec 29 2021 TI_Eugene <ti.eugene@gmail.com) - 1.6.2-1
- Version bump
- Patch removed

* Tue Oct 05 2021 TI_Eugene <ti.eugene@gmail.com) - 1.6.1-1
- Version Bump
- Sources URL changed
- new binaries: lumina-checkpass, lumina-pingcursor
- Required pam-devel added
- Suggested la-capitaine-icon-theme added
- lumina-icons package added

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 23 07:53:45 CET 2020 Jan Grulich <jgrulich@redhat.com> - 1.6.0-5
- rebuild (qt5)

* Fri Sep 11 2020 Jan Grulich <jgrulich@redhat.com> - 1.6.0-4
- rebuild (qt5)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 06 2020 Rex Dieter <rdieter@fedoraproject.org> - 1.6.0-2
- rebuild (qt5)

* Sat Feb 01 2020 TI_Eugene <ti.eugene@gmail.com> - 1.6.0-1
- Version bump

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 09 2019 Jan Grulich <jgrulich@redhat.com> - 1.5.0-3
- rebuild (qt5)

* Wed Sep 25 2019 Jan Grulich <jgrulich@redhat.com> - 1.5.0-2
- rebuild (qt5)

* Wed Aug 21 2019 TI_Eugene <ti.eugene@gmail.com> - 1.5.0-1
- Version bump

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6.p1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5.p1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4.p1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3.p1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Sep 3 2017 TI_Eugene <ti.eugene@gmail.com> - 1.3.0-2.p1
- *.desktop patches tuned

* Sun Sep 3 2017 TI_Eugene <ti.eugene@gmail.com> - 1.3.0-1.p1
- Version bump
- Added mediaplayer, xdg-entry and icons subpackages
- Extra locales source removed

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4.p1.Ld700dea
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3.p1.Ld700dea
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 19 2017 Raphael Groner <projects.rg@smart.ms>
- fix dependency to filesystem subpackage, it is noarch
- add archiver subpackage to suggestions

* Tue Apr 11 2017 TI_Eugene <ti.eugene@gmail.com> - 1.2.0-1.p1.Ld700dea
- Version bump
- Added archiver subpackage
- libs subpackage renamed into filesystem
- Removed empty devel subpackage

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2.p1.Ld700dea
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 09 2016 Raphael Groner <projects.rg@smart.ms> - 1.1.0-1.p1.Ld700dea
- new version
- add subpackage for calculator
- fix for rhbz#1389486, R: lumina-open

* Mon Sep 26 2016 Raphael Groner <projects.rg@smart.ms> - 1.0.0-5.p2.Lbc08e90
- fix typo

* Sun Sep 25 2016 Raphael Groner <projects.rg@smart.ms> - 1.0.0-4.p2.Lbc08e90
- thin out dependencies, no assumptions about used applications

* Sat Sep 24 2016 Raphael Groner <projects.rg@smart.ms> - 1.0.0-3.p2.Lbc08e90
- drop ExcludeArch
- try to fix unused-direct-shlib-dependency

* Sat Aug 27 2016 Raphael Groner <projects.rg@smart.ms> - 1.0.0-2.p2.Lbc08e90
- update to patchset 2
- fix E: script-without-shebang
- [epel] fix creation of folder etc

* Sun Aug 14 2016 Raphael Groner <projects.rg@smart.ms> - 1.0.0-1.p1.Lbc08e90
- use official upstream release
- clean up build deps
- update translations from git
- drop langpacks and include in binary subpackages
- disable weak dependencies for epel

* Sun Aug 07 2016 Raphael Groner <projects.rg@smart.ms> - 1.0.0-0.3.Beta4.Tfbab63e
- Beta4

* Sun Aug 07 2016 Raphael Groner <projects.rg@smart.ms> - 1.0.0-0.2.Beta2.Tfbab63e
- avoid dangling-symlink /usr/bin/lte
- drop implicit BR: gcc
- drop Group tags
- compile translations and split into individual langpacks

* Fri Jul 15 2016 Raphael Groner <projects.rg@smart.ms> - 1.0.0-0.1.Beta2
- version 1.0.0 Beta2
- prepare for review
- split more subpackages: i18n, wallpapers

* Wed Dec 23 2015 Neal Gompa <ngompa13@gmail.com>
- Update to 0.8.8
- Bring it closer to Fedora guidelines
- Break out Lumina Desktop package into subpackages
- Unify 32-bit and 64-bit packaging

* Tue Oct 27 2015 Jesse Smith <jsmith@resonatingmedia.com>
- Update to 0.8.7

* Thu Aug 20 2015 Jesse Smith <jsmith@resonatingmedia.com>
- Updated for 32-bit

* Thu Jul 30 2015 Jesse Smith <jsmith@resonatingmedia.com>
- Initial build
