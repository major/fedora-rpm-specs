%define rdnn        org.kde.drawy

# libdrawyconfig has no SOVERSION upstream, and none of the drawy libraries are
# meant to be linked against by other packages (no CMake config or pkgconfig
# files are shipped).  Install them into a private directory that is not on the
# dynamic linker search path, as required by
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Unversioned_shared_objects/
%global privatelibdir %{_libdir}/%{name}

Name:           drawy
Version:        1.0.2
Release:        %autorelease
Summary:        Your handy, infinite, brainstorming tool
# primary license: GPL-3.0-or-later
# src/gui/pluginform/pluginform.{c,h}pp,
# src/gui/pluginform/pluginformutils.{c,h}pp,
# src/widgets/tools/customtool.{c,h}pp: GPL-2.0-or-later
# src/gui/pluginform/pluginformmanager.{c,h}pp,
# src/widgets/components/flowlayout.{c,h}pp,
# src/widgets/properties/widgets/{alignmentwidget,backgroundstylewidget,
# zorderwidget}.{c,h}pp, po/*: LGPL-2.0-or-later
# src/widgets/resources/fonts/{FuzzyBubbles,Inter}.ttf: OFL-1.1
# src/icons/*, doc/index.docbook: CC-BY-SA-4.0
License:        GPL-3.0-or-later AND GPL-2.0-or-later AND LGPL-2.0-or-later AND OFL-1.1 AND CC-BY-SA-4.0
URL:            https://invent.kde.org/graphics/drawy
Source:         %{url}/-/archive/v%{version}/drawy-v%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6SyntaxHighlighting)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  pkgconfig(libzstd)
# for the update-mime-database probed by ECM's FindSharedMimeInfo
BuildRequires:  shared-mime-info

# for desktop-file-validate command
BuildRequires:  desktop-file-utils
# for appstream-util command
BuildRequires:  libappstream-glib

# for ownership of icon parent directories
Requires:       hicolor-icon-theme
# for ownership of the MIME package directory
Requires:       shared-mime-info


%description
Drawy is a work-in-progress infinite whiteboard tool written in Qt/C++, which
aims to be a native-desktop alternative to the amazing web-based Excalidraw.


%prep
%autosetup -n drawy-v%{version}


%conf
# KDE_INSTALL_LIBDIR moves the private libraries out of the linker path.
# CMAKE_INSTALL_RPATH has to be set by hand: ECM would derive it from the
# install libdir, but KDEInstallDirs6 sets KDE_INSTALL_DIRS_NO_DEPRECATED, so
# KDECMakeSettings still sees the LIB_INSTALL_DIR=%{_libdir} that %%cmake puts
# in the cache, decides it is a system directory and emits no RPATH at all.
# KDE_INSTALL_QTPLUGINDIR is pinned so the Qt plugin does not follow the
# libraries into the private directory.
%cmake -DCMAKE_BUILD_TYPE=Release \
       -DKDE_INSTALL_LIBDIR=%{_lib}/%{name} \
       -DKDE_INSTALL_QTPLUGINDIR=%{_qt6_plugindir} \
       -DCMAKE_INSTALL_RPATH=%{privatelibdir}


%build
%cmake_build


%install
%cmake_install
%find_lang %{name} --with-html

# the shared libraries are internal to drawy and ship no CMake config or
# pkgconfig files, so drop the development symlink and headers
# (libdrawyconfig.so carries no SOVERSION and is the library itself, keep it)
rm %{buildroot}%{privatelibdir}/libdrawygui.so
rm -r %{buildroot}%{_includedir}/DrawyCore


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{rdnn}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{rdnn}.metainfo.xml


%files -f %{name}.lang
%license LICENSES/CC-BY-SA-4.0.txt LICENSES/GPL-2.0-or-later.txt
%license LICENSES/GPL-3.0-or-later.txt LICENSES/LGPL-2.0-or-later.txt
%license LICENSES/OFL-1.1.txt
%doc CHANGELOG.md README.md
%{_bindir}/drawy
%dir %{privatelibdir}
%{privatelibdir}/libdrawyconfig.so
%{privatelibdir}/libdrawygui.so.0
%{privatelibdir}/libdrawygui.so.%{version}
%{privatelibdir}/libdrawywidgets.so.0
%{privatelibdir}/libdrawywidgets.so.%{version}
%{privatelibdir}/libstandardformplugin.so.0
%{privatelibdir}/libstandardformplugin.so.%{version}
%{_qt6_plugindir}/drawypluginforms/
%{_datadir}/applications/%{rdnn}.desktop
%{_datadir}/config.kcfg/drawyglobalconfig.kcfg
%{_datadir}/icons/hicolor/*/apps/drawy.*
%{_datadir}/icons/hicolor/*/mimetypes/application-x-drawy.*
%{_datadir}/mime/packages/application-x-drawy.xml
%{_datadir}/qlogging-categories6/drawy.categories
%{_metainfodir}/%{rdnn}.metainfo.xml


%changelog
%autochangelog
