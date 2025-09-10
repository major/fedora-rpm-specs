Name:           qt5ct
Version:        1.9
Release:        %autorelease
Summary:        Qt5 Configuration Tool

License:        BSD-2-Clause
URL:            https://sourceforge.net/projects/qt5ct/
Source0:        https://downloads.sourceforge.net/qt5ct/qt5ct-%{version}.tar.bz2

Patch1:         0001-Wrap-forward-declaration-within-QT_NAMESPACE.patch
Patch2:         0002-build-refactor-CMake-build-rules.patch
Patch3:         0003-Add-KDE-theming-support.patch
Patch4:         0004-Make-KDE-theming-support-optional.patch
Patch5:         0005-Revert-Use-KDE-s-QtQuick-QtWidgets-style-bridge.patch
Patch6:         0006-enabled-QPlatformTheme-HoverEffect-hint-by-default.patch

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5ThemeSupport)
# Qt5ThemeSupportPrivate requires libQtThemeSupport.a
BuildRequires:  qt5-qtbase-static
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5IconThemes)

%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}

%description
qt5ct allows users to configure Qt5 settings (theme, font, icons, etc.) under
DE/WM without Qt integration.

%prep
%autosetup -p2


%build
%cmake -DQT5CT_IN_TREE=ON
%cmake_build


%install
%cmake_install
%find_lang %{name} --with-qt

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/colors/
%{_datadir}/%{name}/colors/*.conf
%dir %{_datadir}/%{name}/qss/
%{_datadir}/%{name}/qss/*.qss
%exclude %{_libdir}/libqt5ct-common.so
%{_libdir}/libqt5ct-common.so.%{version}
%{_qt5_plugindir}/platformthemes/libqt5ct.so
%{_qt5_plugindir}/styles/libqt5ct-style.so

%changelog
%autochangelog
