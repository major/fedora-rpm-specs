Name:           plasma-phonebook
Version:        24.02.0
Release:        3%{?dist}
License:        CC0 and GPLv2 and GPLv3 and GPLv3+ and LGPLv2+
Summary:        Convergent Plasma Mobile phonebook application
Url:            https://invent.kde.org/plasma-mobile/%{name}
Source0:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz


BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  appstream
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  hicolor-icon-theme
BuildRequires:  desktop-file-utils

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Widgets)

BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6People)
BuildRequires:  cmake(KF6Contacts)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6KirigamiAddons)

Requires:       kf6-kirigami
Requires:       kf6-kcontacts
Requires:       kf6-kcoreaddons
Requires:       kpeoplevcard


%description
Contacts application which allows adding, modifying and removing contacts.

%prep
%autosetup -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name}

%files -f %{name}.lang
%doc README.md
%license LICENSES/{CC0-1.0.txt,GPL-2.0-only,GPL-3.0-only,GPL-3.0-or-later,LGPL-2.0-or-later,LicenseRef-KDE-Accepted-GPL}.txt
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/icons/hicolor/scalable/apps/org.kde.phonebook.svg
%{_kf6_datadir}/applications/org.kde.phonebook.desktop
%{_kf6_metainfodir}/org.kde.phonebook.metainfo.xml
%{_qt6_plugindir}/kpeople/actions/phonebook_kpeople_plugin.so

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 24.02.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.02.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Mar 02 2024 Steve Cossette <farchord@gmail.com> - 24.02.0-1
- 24.02.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.01.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.01.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.01.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jan 30 2023 Justin Zobel <justin@1707.io> - 23.01.0-1
- Update to 23.01.0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 01 2022 Justin Zobel <justin@1707.io> - 22.11-1
- Update to 22.11

* Wed Sep 28 2022 Justin Zobel <justin@1707.io> - 22.09-1
- Update to 22.09

* Wed Aug 31 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 22.06-1
- Initial package
