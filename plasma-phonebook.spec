
%global kf5_min_version 5.88.0

Name:           plasma-phonebook
Version:        22.06
Release:        1%{?dist}
License:        CC0 and GPLv2 and GPLv3 and GPLv3+ and LGPLv2+
Summary:        Convergent Plasma Mobile phonebook application
Url:            https://invent.kde.org/plasma-mobile/%{name}
Source0:        https://download.kde.org/stable/plasma-mobile/%{version}/%{name}-%{version}.tar.xz


BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  appstream
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros          >= %{kf5_min_version}
BuildRequires:  hicolor-icon-theme
BuildRequires:  desktop-file-utils

BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Core)

BuildRequires:  cmake(KF5Kirigami2)     >= %{kf5_min_version}
BuildRequires:  cmake(KF5Contacts)      >= %{kf5_min_version}
BuildRequires:  cmake(KF5CoreAddons)    >= %{kf5_min_version}
BuildRequires:  cmake(KF5People)        >= %{kf5_min_version}
BuildRequires:  cmake(KF5PeopleVCard)   >= %{kf5_min_version}
BuildRequires:  cmake(KF5Config)        >= %{kf5_min_version}
BuildRequires:  cmake(KF5I18n)          >= %{kf5_min_version}
BuildRequires:  cmake(KF5Codecs)        >= %{kf5_min_version}

Requires:       kf5-kirigami2
Requires:       kf5-kcontacts
Requires:       kf5-kcoreaddons
Requires:       kpeoplevcard


%description
Contacts application which allows adding, modifying and removing contacts.

%prep
%autosetup -p1

%build
%cmake_kf5
%cmake_build

%install
%cmake_install
%find_lang %{name}

%files -f %{name}.lang
%doc README.md
%license LICENSES/{CC0-1.0.txt,GPL-2.0-only,GPL-3.0-only,GPL-3.0-or-later,LGPL-2.0-or-later,LicenseRef-KDE-Accepted-GPL}.txt
%{_kf5_bindir}/%{name}
%{_kf5_datadir}/icons/hicolor/scalable/apps/org.kde.phonebook.svg
%{_kf5_datadir}/applications/org.kde.phonebook.desktop
%{_kf5_metainfodir}/org.kde.phonebook.metainfo.xml
%{_qt5_plugindir}/kpeople/actions/phonebook_kpeople_plugin.so

%changelog
* Wed Aug 31 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 22.06-1
- Initial package
