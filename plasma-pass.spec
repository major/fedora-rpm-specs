%undefine __cmake_in_source_build

%global kf5_version_min 5.82.0

Name:           plasma-pass
Version:        1.2.0
Release:        9%{?dist}
Summary:        Plasma applet to access passwords from the Pass password manager
License:        LGPLv2+
URL:            https://invent.kde.org/plasma/%{name}.git
Source0:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz

# Exclude QML plugins from provides()
%global __provides_exclude_from ^(%{_kf5_qmldir}/.*\\.so|%{_kf5_qtplugindir}/.*\\.so)$


BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  desktop-file-utils

BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Widgets)

BuildRequires:  cmake(KF5Plasma) >= %{kf5_version_min}
BuildRequires:  cmake(KF5I18n) >= %{kf5_version_min}
BuildRequires:  cmake(KF5ItemModels) >= %{kf5_version_min}
BuildRequires:  cmake(KF5Service) >= %{kf5_version_min}
BuildRequires:  cmake(KF5CoreAddons) >= %{kf5_version_min}
BuildRequires:  cmake(KF5Package) >= %{kf5_version_min}

BuildRequires: cmake(QGpgme)

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
%cmake_kf5
%cmake_build

%install
%cmake_install

%check
desktop-file-validate %{buildroot}/%{_datadir}/kservices5/plasma-applet-org.kde.plasma.pass.desktop


%find_lang plasma_applet_org.kde.plasma.pass

%files -f plasma_applet_org.kde.plasma.pass.lang
%license COPYING
%doc README.md
%{_kf5_sysconfdir}/xdg/plasma-pass.categories
%dir %{_kf5_qmldir}/org/kde/plasma/private/plasmapass/
%{_kf5_qmldir}/org/kde/plasma/private/plasmapass/*
%dir %{_kf5_datadir}/plasma/plasmoids/org.kde.plasma.pass/
%{_kf5_datadir}/plasma/plasmoids/org.kde.plasma.pass/*
%{_kf5_datadir}/kservices5/*.desktop
%{_kf5_metainfodir}/*.xml


%changelog
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
