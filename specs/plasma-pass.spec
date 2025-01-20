Name:           plasma-pass
Version:        1.2.2
Release:        3%{?dist}
Summary:        Plasma applet to access passwords from the Pass password manager
License:        CC0-1.0 AND LGPL-2.1-or-later
URL:            https://invent.kde.org/plasma/%{name}.git
Source0:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz

# Exclude QML plugins from provides()
%global __provides_exclude_from ^(%{_kf5_qmldir}/.*\\.so|%{_kf5_qtplugindir}/.*\\.so)$


BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  desktop-file-utils

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt5Concurrent)

BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(Plasma5Support)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Package)

BuildRequires:  cmake(QGpgmeQt6)

BuildRequires:  gettext-devel
BuildRequires:  gpgmepp-devel
BuildRequires:  pkgconfig(liboath)


Requires:       plasmashell(desktop)
# Invokes the gpg2 executable to decrypt passwords
Requires:       gnupg2

# Does not use pass directly, but is a GUI for its store, also using
# the command line is currently the only way how to add new passwords.
Recommends:     pass

%description
Plasma Pass is a Plasma systray applet to easily access passwords from the Pass
password manager.

%prep
%autosetup


%build
%cmake_kf6 -DBUILD_WITH_QT6=ON
%cmake_build

%install
%cmake_install

%find_lang plasma_applet_org.kde.plasma.pass

%files -f plasma_applet_org.kde.plasma.pass.lang
%license LICENSES/*
%doc README.md
%{_kf6_qmldir}/org/kde/plasma/private/plasmapass/
%{_kf6_datadir}/plasma/plasmoids/org.kde.plasma.pass/
%{_kf6_datadir}/qlogging-categories6/plasma-pass.categories


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 25 2024 Alessandro Astone <ales.astone@gmail.com> - 1.2.2-1
- 1.2.2 (Qt6, not functional yet)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 07 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 1.2.0-2
- check section added.
- min kf5 ver changed to 5.82
- cpp BRs added.
- missing qt and kf5 BRs added.


* Mon Feb 15 2021 Daniel Vrátil <dvratil@fedoraproject.org> - 1.2.0-1
- Plasma Pass 1.2.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 2020 Daniel Vrátil <dvratil@fedoraproject.org> - 1.1.0-1
- Plasma Pass 1.1.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 26 2019 Daniel Vrátil <dvratil@fedoraproject.org> - 1.0.0-1
- Initial version
