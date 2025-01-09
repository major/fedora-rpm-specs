Name:          francis
Version:       24.12.1
Release:       1%{?dist}
License:       BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-3.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later
Summary:       Time tracking app for KDE Plasma
URL:           https://apps.kde.org/francis/
Source:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

# upstream patches

BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Widgets)

BuildRequires: cmake(KF6Kirigami)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6KirigamiAddons)

Requires: hicolor-icon-theme
Requires: qt6qml(org.kde.coreaddons)
Requires: qt6qml(org.kde.kirigami)
Requires: qt6qml(org.kde.kirigamiaddons.formcard)
Requires: qt6qml(org.kde.notification)


%description
Francis is a time tracking app using the well-known
pomodoro technique to help you get more productive.


%prep
%autosetup -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{name} --with-man --with-qt --all-name

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.francis.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_bindir}/francis
%{_kf6_datadir}/applications/org.kde.francis.desktop
%{_kf6_datadir}/icons/hicolor/scalable/apps/org.kde.francis.svg
%{_metainfodir}/org.kde.francis.metainfo.xml


%changelog
* Tue Jan 07 2025 Steve Cossette <farchord@gmail.com> - 24.12.1-1
- 24.12.1

* Sat Dec 07 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.12.0-1
- 24.12.0

* Fri Nov 29 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.11.90-1
- 24.11.90

* Fri Nov 15 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.11.80-1
- 24.11.80

* Tue Nov 05 2024 Steve Cossette <farchord@gmail.com> - 24.08.3-1
- 24.08.3

* Tue Oct 08 2024 Steve Cossette <farchord@gmail.com> - 24.08.2-1
- 24.08.2

* Wed Sep 25 2024 Alessandro Astone <ales.astone@gmail.com> - 24.08.1-1
- 24.08.1

* Thu Aug 22 2024 Steve Cossette <farchord@gmail.com> - 24.08.0-1
- 24.08.0

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.05.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jul 07 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.2-1
- 24.05.2

* Wed May 22 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 24.05.0-1
- 24.05.0

* Sat Mar 2 2024 Steve Cossette <farchord@gmail.com> - 1.1.0-1
- Initial Release
