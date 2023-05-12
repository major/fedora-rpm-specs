%global orgname org.kde.plasma-welcome

Name:           plasma-welcome
Version:        5.27.5
Release:        1%{?dist}
License:        GPLv2+ and BSD
Summary:        Plasma Welcome
Url:            https://invent.kde.org/plasma/%{name}

%global stable %stable_kf5
Source0:        http://download.kde.org/%{stable}/plasma/%{version}/%{name}-%{version}.tar.xz

# Upstream patches
# removes duplicate entry in xml file
Patch0:         4e86a974bed490ed639c5a94945035c5a201d8dc.patch

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
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5NetworkManagerQt)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5Plasma)
BuildRequires:  cmake(KUserFeedback)

Provides:       plasma-welcome-app = %{version}-%{release}
Obsoletes:      plasma-welcome-app < 5.27.0-2

%description
A Friendly onboarding wizard for Plasma.

%prep
%autosetup -n %{name}-%{version} -p1
# It is for generate pot file for translate so we can ignore it. Also CC0 license not allowed
rm Messages.sh

%build
%cmake_kf5
%cmake_build

%install
%cmake_install
%find_lang %{name} --all-name --with-html

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/%{orgname}.*.xml
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/%{orgname}.desktop

%files -f %{name}.lang
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
* Wed May 10 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.5-1
- 5.27.5

* Tue Apr 04 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.4-1
- 5.27.4

* Tue Mar 14 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.3-1
- 5.27.3

* Tue Feb 28 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.2-1
- 5.27.2

* Tue Feb 21 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.1-1
- 5.27.1

* Fri Feb 17 2023 Timothée Ravier <tim@siosm.fr> - 5.27.0-2
- Rename to Plasma Welcome to follow upstream naming (fedora#2170929)

* Thu Feb 09 2023 Marc Deop <marcdeop@fedoraproject.org> - 5.27.0-1
- 5.27.0

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
