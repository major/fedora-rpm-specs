%global app_id  org.kde.hashomatic

Name:           hash-o-matic
Version:        1.0.1
Release:        2%{?dist}
Summary:        KDE file checksum utility
License:        LGPL-2.0-or-later AND LGPL-2.1-or-later AND CC0-1.0 AND BSD-2-Clause
URL:            https://apps.kde.org/hashomatic/
Source:         https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)

BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6WindowSystem)

BuildRequires:  cmake(KPim6Libkleo)
BuildRequires:  cmake(Gpgmepp)
BuildRequires:  cmake(QGpgmeQt6)

Requires:       hicolor-icon-theme
Requires:       qt6qml(org.kde.coreaddons)
Requires:       qt6qml(org.kde.kirigami)
Requires:       qt6qml(org.kde.kirigamiaddons.formcard)

%description
Hash-o-matic is an application allowing to generate, compare, and verify
sha256, sha1 and md5 checksums for files.

%prep
%autosetup


%build
%cmake_kf6
%cmake_build


%install
%cmake_install

%find_lang hashomatic


%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/%{app_id}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/%{app_id}.metainfo.xml


%files -f hashomatic.lang
%license LICENSES/*
%doc README.md
%{_kf6_bindir}/hashomatic
%{_kf6_datadir}/applications/%{app_id}.desktop
%{_kf6_datadir}/icons/hicolor/scalable/apps/%{app_id}.svg
%{_kf6_datadir}/kio/servicemenus/hashFile.desktop
%{_kf6_metainfodir}/%{app_id}.metainfo.xml


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Aug 30 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 1.0.1-1
- Initial release
