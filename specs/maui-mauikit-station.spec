Name:          maui-mauikit-station
Version:       4.0.0
Release:       2%{?dist}
License:       MIT AND GPL-3.0-or-later
Summary:       Convergent terminal emulator written using Maui
URL:           https://mauikit.org/apps/station/

Source0:       https://download.kde.org/stable/maui/station/%{version}/maui-station-%{version}.tar.xz

# Added missing licenses, removed unused license
# https://invent.kde.org/maui/maui-station/-/merge_requests/8
Patch0:        8.patch

BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6DBus)

BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6CoreAddons)

BuildRequires: cmake(MauiKitTerminal4)
BuildRequires: cmake(MauiKitFileBrowsing4)
BuildRequires: cmake(MauiKit4)

Requires:      hicolor-icon-theme

%description
%{summary}.


%prep
%autosetup -p1 -n maui-station-%{version}


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang station --with-man --with-qt --all-name

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.station.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%files -f station.lang
%license LICENSES/*
%{_bindir}/station
%{_datadir}/applications/org.kde.station.desktop
%{_datadir}/icons/hicolor/scalable/apps/station.svg
%{_metainfodir}/org.kde.station.appdata.xml

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Nov 8 2024 Steve Cossette <farchord@gmail.com> - 4.0.0-1
- 4.0.0
