Name: flameshot
Version: 12.1.0
Release: 8%{?dist}

# Main code: GPL-3.0-or-later
# Logo: LAL-1.3
# Button icons: Apache-2.0
# capture/capturewidget.cpp and capture/capturewidget.h: GPL-2.0-only
# regiongrabber.cpp: LGPL-3.0-or-later
# Qt-Color-Widgets: LGPL-3.0-only OR GPL-3.0-only
# More information: https://github.com/flameshot-org/flameshot#license
License: GPL-3.0-or-later AND Apache-2.0 AND GPL-2.0-only AND LGPL-3.0-or-later AND (LGPL-3.0-only OR GPL-3.0-only) AND LAL-1.3
Summary: Powerful and simple to use screenshot software
URL: https://github.com/flameshot-org/%{name}
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake(KF5GuiAddons) >= 5.89.0
BuildRequires: cmake(Qt5Concurrent)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(Qt5Multimedia)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5Svg)
BuildRequires: cmake(Qt5Widgets)

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: fdupes
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: libappstream-glib
BuildRequires: ninja-build
BuildRequires: qtsingleapplication-qt5-devel

Requires: hicolor-icon-theme
Requires: qt5-qtsvg%{?_isa}

# XDG portals are required to take screenshots on Wayland:
# https://github.com/flameshot-org/flameshot/issues/1910
Recommends: xdg-desktop-portal%{?_isa}
Recommends: (xdg-desktop-portal-gnome%{?_isa} if gnome-shell%{?_isa})
Recommends: (xdg-desktop-portal-kde%{?_isa} if plasma-workspace-wayland%{?_isa})
Recommends: (xdg-desktop-portal-wlr%{?_isa} if wlroots%{?_isa})

Provides: bundled(qt-color-widgets) = 2.2.0

%description
Powerful and simple to use screenshot software with built-in
editor with advanced features.

%prep
%autosetup -p1
rm -rf external/{QHotkey,singleapplication}

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DUSE_WAYLAND_CLIPBOARD:BOOL=ON \
    -DUSE_EXTERNAL_SINGLEAPPLICATION:BOOL=ON \
    -DUSE_LAUNCHER_ABSOLUTE_PATH:BOOL=OFF
%cmake_build

%install
%cmake_install
%find_lang Internationalization --with-qt
%fdupes %{buildroot}%{_datadir}/icons

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files -f Internationalization.lang
%doc README.md
%license LICENSE
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%dir %{_datadir}/bash-completion/completions
%dir %{_datadir}/fish/vendor_completions.d
%dir %{_datadir}/zsh/site-functions
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_metainfodir}/*.metainfo.xml
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/fish/vendor_completions.d/%{name}.fish
%{_datadir}/zsh/site-functions/_%{name}
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/dbus-1/services/*.service
%{_datadir}/icons/hicolor/*/apps/*
%{_mandir}/man1/%{name}.1*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 12.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 12.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 12.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 12.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 12.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 12.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 12.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 04 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 12.1.0-1
- Updated to version 12.1.0.

* Wed Jun 22 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 12.0.0-1
- Updated to version 12.0.0.

* Sat Jan 22 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 11.0.0-3
- Backported upstream patch with Wayland clipboard fixes.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan 15 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 11.0.0-1
- Updated to version 11.0.0.

* Sun Nov 28 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.10.2-3
- Fixed issues with hotkeys on KDE Wayland.

* Sun Nov 28 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.10.2-2
- Backported upstream patch with version fixes.

* Sun Nov 14 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.10.2-1
- Updated to version 0.10.2.

* Mon Jul 26 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.10.1-1
- Updated to version 0.10.1.

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul 14 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.10.0-1
- Updated to version 0.10.0.

* Sun Feb 28 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.9.0-1
- Updated to version 0.9.0.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 15 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.8.5-1
- Updated to version 0.8.5.

* Tue Sep 29 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.8.3-1
- Updated to version 0.8.3.

* Thu Sep 24 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.8.1-1
- Updated to version 0.8.1.

* Sun Sep 20 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.8.0-1
- Updated to version 0.8.0.

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.0-3
- Added missing runtime requirements (rhbz#1724679).

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 26 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.0-1
- Updated to version 0.6.0.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Feb 24 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.5.1-1
- Updated to version 0.5.1.

* Mon Jan 08 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.5.0-2
- Minor SPEC fixes.

* Sat Jan 06 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.5.0-1
- Initial SPEC release.
