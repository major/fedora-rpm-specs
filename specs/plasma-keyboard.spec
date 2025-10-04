%global gitdate 20250824.094649
%global commit0 6bf37e55a2fc3895e07f6d77236542a2ce0e763f
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           plasma-keyboard
Version:        1.0~%{gitdate}.%{shortcommit0}
Release:        2%{?dist}
Summary:        Virtual Keyboard for Qt based desktops

License:        LGPL-2.1-only AND GPL-2.0-only AND CC0-1.0 AND LGPL-3.0-only AND GPL-3.0-or-later AND GPL-2.0-or-later AND GPL-3.0-only
URL:            https://invent.kde.org/plasma/%{name}/

Source0:        https://invent.kde.org/plasma/%{name}/-/archive/%{commit0}/%{name}-%{commit0}.tar.gz

BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6VirtualKeyboard)
BuildRequires:  cmake(Qt6WaylandClient)

BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6Config)

BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  qt6-qtbase-private-devel

%description
The plasma-keyboard is a virtual keyboard
based on Qt Virtual Keyboard designed to
integrate in Plasma.

%package -n kcm-%{name}
Summary: KDE KCM for %{name}
Requires: %{name} = %{version}-%{release}
%description -n kcm-%{name}
%{summary}.

%prep
%autosetup -n %{name}-%{commit0}


%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang kcm_plasmakeyboard

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.plasma.keyboard.desktop

%files
%license LICENSES/*
%doc README.md
%{_bindir}/plasma-keyboard
%{_kf6_datadir}/applications/org.kde.plasma.keyboard.desktop
%{_kf6_qmldir}/QtQuick/VirtualKeyboard/
%{_kf6_qmldir}/org/kde/plasma/keyboard/
%{_kf6_datadir}/plasma/keyboard/

%files -n kcm-%{name} -f kcm_plasmakeyboard.lang
%{_kf6_qtplugindir}/plasma/kcms/systemsettings/kcm_plasmakeyboard.so
%{_datadir}/applications/kcm_plasmakeyboard.desktop

%changelog
* Thu Oct 02 2025 Jan Grulich <jgrulich@redhat.com> - 1.0~20250824.094649.6bf37e5-2
- Rebuild (qt6)

* Sat Feb 15 2025 Steve Cossette <farchord@gmail.com> - 1.0~20250824.094649.6bf37e5-1
- Initial
