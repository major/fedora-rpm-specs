%global framework purpose

Name:    kf6-purpose
Summary: Framework for providing abstractions to get the developer's purposes fulfilled
Version: 6.11.0
Release: 1%{?dist}

License: CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:     https://invent.kde.org/frameworks/%{framework}

Source0: http://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz

# upstream patches

BuildRequires: extra-cmake-modules >= %{version}
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: intltool
BuildRequires: cmake
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Kirigami2)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KAccounts6)
BuildRequires: pkgconfig(Qt6Network)
BuildRequires: pkgconfig(Qt6Qml)

BuildRequires: accounts-qml-module-qt6
Requires:      accounts-qml-module-qt6
BuildRequires: cmake(KF6Declarative)
Requires:      kf6-kdeclarative
BuildRequires: cmake(KF6Prison)
Requires:      kf6-prison


Requires: hicolor-icon-theme
Requires: kf6-bluez-qt >= %{version}

%description
Purpose offers the possibility to create integrate services and actions on
any application without having to implement them specifically. Purpose will
offer them mechanisms to list the different alternatives to execute given the
requested action type and will facilitate components so that all the plugins
can receive all the information they need.

%package  devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: cmake(KF6CoreAddons)
%description devel
%{summary}.

%prep
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name} --all-name

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6Purpose.so.6
%{_kf6_libdir}/libKF6Purpose.so.%{version}
%{_kf6_libdir}/libKF6PurposeWidgets.so.6
%{_kf6_libdir}/libKF6PurposeWidgets.so.%{version}
%{_kf6_libexecdir}/purposeprocess
%{_kf6_datadir}/kf6/purpose/
%{_kf6_datadir}/accounts/services/kde/*.service
%{_kf6_plugindir}/purpose/
%dir %{_kf6_plugindir}/kfileitemaction/
%{_kf6_plugindir}/kfileitemaction/sharefileitemaction.so
%{_kf6_qmldir}/org/kde/purpose/
%{_datadir}/icons/hicolor/*/apps/*-purpose6.*

%files devel
%{_kf6_libdir}/libKF6Purpose.so
%{_kf6_libdir}/libKF6PurposeWidgets.so
%{_kf6_includedir}/Purpose/
%{_kf6_includedir}/PurposeWidgets/
%{_kf6_libdir}/cmake/KF6Purpose/

%changelog
* Fri Feb 07 2025 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.11.0-1
- 6.11.0

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jan 03 2025 Steve Cossette <farchord@gmail.com> - 6.10.0-1
- 6.10.0

* Sat Dec 14 2024 Steve Cossette <farchord@gmail.com> - 6.9.0-1
- 6.9.0

* Sat Nov 02 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.8.0-1
- 6.8.0

* Fri Oct 04 2024 Steve Cossette <farchord@gmail.com> - 6.7.0-1
- 6.7.0

* Mon Sep 16 2024 Steve Cossette <farchord@gmail.com> - 6.6.0-1
- 6.6.0

* Sat Aug 10 2024 Steve Cossette <farchord@gmail.com> - 6.5.0-1
- 6.5.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jul 06 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.4.0-1
- 6.4.0

* Sat Jun 01 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.3.0-1
- 6.3.0

* Sat May 04 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.2.0-1
- 6.2.0

* Wed Apr 10 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.1.0-1
- 6.1.0

* Thu Feb 29 2024 Marie Loise Nolden <loise@kde.org> - 6.0.0-2
- add kf6-prison and kf6-kdeclarative runtime Requires

* Wed Feb 21 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.0.0-1
- 6.0.0

* Wed Jan 31 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.249.0-1
- 5.249.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.248.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.248.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 10 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.248.0-1
- 5.248.0

* Tue Dec 26 2023 Alessandro Astone <ales.astone@gmail.com> - 5.247.0-2
- Enable KAccounts integration

* Wed Dec 20 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.247.0-1
- 5.247.0

* Thu Dec 07 2023 Nicolas Fella <nicolas.fella@gmx.de> - 5.246.0-2
- Add missing bluez-qt QML module dependency

* Sat Dec 02 2023 Justin Zobel <justin.zobel@gmail.com> - 5.246.0-1
- Update to 5.246.0

* Thu Nov 09 2023 Steve Cossette <farchord@gmail.com> - 5.245.0-1
- 5.245.0

* Sat Sep 23 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231011.004242.c0f1138-1
- Initial release
