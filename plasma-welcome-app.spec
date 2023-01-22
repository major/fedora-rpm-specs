%global srcname plasma-welcome
%global orgname org.kde.plasma-welcome

Name:           plasma-welcome-app
Version:        5.26.90
Release:        2%{?dist}
License:        GPLv2+ and BSD
Summary:        Plasma Welcome App
Url:            https://invent.kde.org/plasma/%{srcname}

%global stable %stable_kf5
Source0:        http://download.kde.org/%{stable}/plasma/%{version}/%{srcname}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  qt5-qtbase-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros

BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5Svg)

BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KAccounts)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5NetworkManagerQt)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5Plasma)
BuildRequires:  cmake(KUserFeedback)


%description
Plasma Welcome App.

%prep
%autosetup -n %{srcname}-%{version} -p1
# It is for generate pot file for translate so we can ignore it. Also CC0 license not allowed
rm Messages.sh

%build
%cmake_kf5
%cmake_build

%install
%cmake_install
%find_lang %{srcname} --all-name --with-html

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/%{orgname}.*.xml
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/%{orgname}.desktop

%files -f %{srcname}.lang
%license src/LICENSES/{BSD-3-Clause.txt,GPL-2.0-or-later.txt,FSFAP.txt}
%doc README.md
%{_sysconfdir}/xdg/autostart/org.kde.plasma-welcome.desktop
%{_kf5_qmldir}/org/kde/plasma/welcome/GenericPage.qml
%{_kf5_qmldir}/org/kde/plasma/welcome/KCM.qml
%{_kf5_qmldir}/org/kde/plasma/welcome/qmldir
%{_kf5_bindir}/plasma-welcome
%{_kf5_datadir}/applications/%{orgname}.desktop
%{_kf5_metainfodir}/%{orgname}.*.xml


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.26.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 19 2023 Marc Deop <marcdeop@fedoraproject.org> - 5.26.90-1
- 5.26.90

* Tue Sep 20 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 0-1.20220922git2d3f9f7
- Commit build 2d3f9f7
- Feature: post-upgrade message
- BR cmake(KF5Plasma) added.

* Mon Sep 05 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 0-1.20220902git0163cda
- Initial build plasma welcome app
