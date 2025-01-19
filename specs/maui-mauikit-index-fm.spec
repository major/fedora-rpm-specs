Name:          maui-mauikit-index-fm
Version:       4.0.0
Release:       2%{?dist}
License:       BSD-3-Clause AND MIT AND GPL-2.0-or-later AND GPL-3.0-or-later AND CC0-1.0
Summary:       Simple file manager for desktops and Plasma Mobile
URL:           https://apps.kde.org/%{name}/

Source0:       https://download.kde.org/stable/maui/index/%{version}/index-fm-%{version}.tar.xz

BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Multimedia)
BuildRequires: cmake(Qt6Sql)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: qt6-qtdeclarative-devel

BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(MauiKitFileBrowsing4)
BuildRequires: cmake(MauiKit4)
BuildRequires: cmake(MauiKitArchiver4)
BuildRequires: cmake(MauiKitTerminal4)
BuildRequires: cmake(MauiKitDocuments4)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6Kirigami)
BuildRequires: cmake(KF6Purpose)

Requires:      hicolor-icon-theme

Requires:      maui-mauikit-filebrowsing
Requires:      maui-mauikit-archiver
Requires:      maui-mauikit-terminal
Requires:      maui-mauikit-documents
Requires:      kf6-purpose

%description
Index is a file manager that works on desktops, Android and Plasma Mobile.
Index lets you browse your system files and applications and preview your
music, text, image and video files and share them with external applications.


%prep
%autosetup -p1 -n index-fm-%{version}


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang index-fm --with-man --with-qt --all-name

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.index.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%files -f index-fm.lang
%license LICENSES/*
%{_kf6_bindir}/index
%{_kf6_datadir}/applications/org.kde.index.desktop
%{_kf6_datadir}/icons/hicolor/scalable/apps/index.svg
%{_metainfodir}/org.kde.index.appdata.xml
%{_kf6_datadir}/knotifications6/org.kde.index.notifyrc

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue May 14 2024 Steve Cossette <farchord@gmail.com> - 4.0.0-1
- 4.0.0
