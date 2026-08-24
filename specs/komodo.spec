# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

Name:           komodo
Version:        1.6.0
Release:        1%{?dist}
Summary:        Todo manager that uses todo.txt specification
License:        GPL-2.0-or-later AND LGPL-2.0-or-later AND CC0-1.0 AND CC-BY-SA-4.0
URL:            https://apps.kde.org/komodo/
Source:         https://download.kde.org/stable/komodo/%{version}/komodo-%{version}.tar.xz
# Fixes an invalid icon entry in metainfo.xml
# https://invent.kde.org/utilities/komodo/-/merge_requests/84
Patch0:         komodo-1.6.0-fix-appstream-metadata.patch
# Adds soname versioning to the internal QML libraries
# https://invent.kde.org/utilities/komodo/-/merge_requests/85
Patch1:         komodo-1.6.0-versioned-soname.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6QQC2DesktopStyle)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Widgets)

Requires:       hicolor-icon-theme
Requires:       qt6qml(org.kde.kirigami)
Requires:       qt6qml(org.kde.kirigamiaddons.dateandtime)
Requires:       qt6qml(org.kde.kirigamiaddons.formcard)
Requires:       qt6qml(org.kde.kitemmodels)

%description
KomoDo is a todo manager that uses todo.txt specification. It parses any
compliant todo.txt files and turns them into easy to use list of tasks.
KomoDo has built-in help for the todo.txt specification.

Features
- Open and create new todo.txt files
- Add, delete and edit tasks
- Filter and search tasks

%prep
%autosetup -p1

%conf
%cmake_kf6

%build
%cmake_build

%install
%cmake_install
%find_lang %{name} --all-name --with-html

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.komodo.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.komodo.metainfo.xml

%files -f %{name}.lang
%license LICENSES/*
%doc README.md
%{_kf6_bindir}/komodo
%{_kf6_libdir}/libkomodo_models.so.0
%{_kf6_libdir}/libkomodo_models.so.0.1
%{_kf6_libdir}/libkomodo_ui.so.0
%{_kf6_libdir}/libkomodo_ui.so.0.1
%{_kf6_qmldir}/org/kde/komodo/
%{_kf6_datadir}/applications/org.kde.komodo.desktop
%{_kf6_datadir}/icons/hicolor/scalable/apps/org.kde.komodo.svg
%{_kf6_datadir}/qlogging-categories6/komodo.categories
%{_kf6_metainfodir}/org.kde.komodo.metainfo.xml

%changelog
* Sat Aug 22 2026 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 1.6.0-1
- Initial package for Fedora
