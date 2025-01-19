%global orig_name kirigami-addons

Name:           kf5-kirigami2-addons
Version:        0.11.0
Release:        6%{?dist}
Epoch:          1
License:        BSD-2-Clause AND CC-BY-SA-4.0 AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
Summary:        Convergent visual components ("widgets") for Kirigami-based applications
Url:            https://invent.kde.org/libraries/kirigami-addons
Source:         https://invent.kde.org/libraries/%{orig_name}/-/archive/v%{version}/%{orig_name}-v%{version}.tar.gz

BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf5-rpm-macros
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Kirigami2)

BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickControls2)

Obsoletes: kf5-kirigami2-addons-dateandtime < 1:0.11.0-2
Provides:  kf5-kirigami2-addons-dateandtime = %{epoch}:%{version}-%{release}
Provides:  kf5-kirigami2-addons-dateandtime%{?_isa} = %{epoch}:%{version}-%{release}

Obsoletes: kf5-kirigami2-addons-treeview < 1:0.11.0-2
Provides:  kf5-kirigami2-addons-treeview = %{epoch}:%{version}-%{release}
Provides:  kf5-kirigami2-addons-treeview%{?_isa} = %{epoch}:%{version}-%{release}

%description
A set of "widgets" i.e visual end user components along with a
code to support them. Components are usable by both touch and
desktop experiences providing a native experience on both, and
look native with any QQC2 style (qqc2-desktop-theme, Material
or Plasma).

%prep
%autosetup -n %{orig_name}-v%{version}

%build
%cmake_kf5
%cmake_build

%install
%cmake_install
%find_lang %{orig_name} --all-name

%files -f %{orig_name}.lang
%doc README.md
%license LICENSES/
%dir %{_kf5_qmldir}/org/kde
%{_kf5_qmldir}/org/kde/kirigamiaddons
%{_kf5_libdir}/cmake/KF5KirigamiAddons

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.11.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.11.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.11.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 10 2024 Alessandro Astone <ales.astone@gmail.com> - 1:0.11.0-2
- Remove subpackages

* Fri Aug 18 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:0.11.0-1
- Update to 0.11.0

* Sat Aug 05 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:0.10.0-1
- Update to 0.10.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Apr 19 2023 Marc Deop marcdeop@fedoraproject.org - 1:0.8.0-1
- Update to 0.8.0

* Wed Mar 08 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:0.7.2-1
- Update to 0.7.2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 30 2022 Marc Deop <marcdeop@fedoraproject.org> - 1:0.6-1
- 0.6

* Wed Sep 28 2022 Justin Zobel <justin@1707.io> - 0.4-1
- Update to 0.4

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.05-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 14 2022 Jan Grulich <jgrulich@redhat.com> - 21.05-6
- Rebuild (qt5)

* Tue May 17 2022 Jan Grulich <jgrulich@redhat.com> - 21.05-5
- Rebuild (qt5)

* Fri Mar 11 2022 Jan Grulich <jgrulich@redhat.com> - 21.05-4
- Rebuild (qt5)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 15 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 21.05-1
- initial version of package
