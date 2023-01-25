Name:          flatpak-kcm
Version:       5.26.90
Release:       1%{?dist}
License:       BSD-2-Clause and BSD-3-Clause and CC0-1.0 and GPL-2.0-or-later
Summary:       Flatpak Permissions Management KCM
Url:           https://invent.kde.org/plasma/flatpak-kcm

%global        stable %stable_kf5
Source0:       http://download.kde.org/%{stable}/plasma/%{version}/%{name}-%{version}.tar.xz

BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf5-rpm-macros
BuildRequires: cmake(KF5Declarative)
BuildRequires: cmake(KF5KCMUtils)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(Qt5Svg)
BuildRequires: pkgconfig(flatpak)

%description
%{summary}.

%prep
%autosetup -p1

%build
%cmake_kf5
%cmake_build

%install
%cmake_install

%find_lang kcm_flatpak

%files -f kcm_flatpak.lang
%license LICENSES/*

%{_kf5_datadir}/kpackage/kcms/kcm_flatpak/contents/ui/main.qml
%{_kf5_datadir}/kpackage/kcms/kcm_flatpak/contents/ui/permissions.qml

%{_kf5_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_flatpak.so

%changelog
* Sun Jan 22 2023 Marc Deop <marcdeop@fedoraproject.org> - 5.26.90-1
- Initial Package
