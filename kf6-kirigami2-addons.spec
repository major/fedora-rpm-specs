%global framework kirigami-addons

Name:           kf6-kirigami2-addons
Epoch:          1
Version:        5.246.0
Release:        1%{?dist}
License:        BSD-2-Clause AND CC-BY-SA-4.0 AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND LicenseRef-KDE-Accepted-GPL AND LicenseRef-KDE-Accepted-LGPL AND LicenseRef-KFQF-Accepted-GPL
Summary:        Convergent visual components ("widgets") for Kirigami-based applications
Url:            https://invent.kde.org/libraries/%{framework}
Source:         https://download.kde.org/%{stable_kf6}/%{framework}/%{framework}-%{version}.tar.xz

BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Kirigami2)
BuildRequires:  cmake(KF6Svg)
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  cmake(Qt6)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)

BuildRequires:  pkgconfig(xkbcommon)
Requires: kf6-filesystem

%description
A set of "widgets" i.e visual end user components along with a
code to support them. Components are usable by both touch and
desktop experiences providing a native experience on both, and
look native with any QQC2 style (qqc2-desktop-theme, Material
or Plasma).

%package dateandtime
Summary:        Date and time add-on for the Kirigami framework
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description dateandtime
Date and time Kirigami addons, which complements other
software like Kclock.

%package treeview
Summary:         Tree view add-on for the Kirigami framework
Requires:        %{name}%{?_isa} = %{epoch}:%{version}-%{release}
%description treeview
Tree view Kirigami addon, which is useful for listing files.

%prep
%autosetup -n %{framework}-%{version}

%build
# Manually rename translation files
# This change missed the 0.11.76 release tarball
# REMOVEME when you next update
find ./po -type f -execdir mv {} kirigami-addons6.po \;

%cmake_kf6 -DBUILD_WITH_QT6=ON
%cmake_build

%install
%cmake_install
%find_lang %{orig_name}6 --all-name

%files -f %{orig_name}6.lang
%doc README.md
%license LICENSES/
%dir %{_kf6_qmldir}/org/kde
%dir %{_kf6_qmldir}/org/kde/kirigamiaddons
%{_kf6_libdir}/qt6/qml/org/kde/kirigamiaddons/*
%{_kf6_libdir}/cmake/KF6KirigamiAddons/*


%files dateandtime
%{_kf6_qmldir}/org/kde/kirigamiaddons/dateandtime/

%files treeview
%{_kf6_qmldir}/org/kde/kirigamiaddons/treeview/

%changelog
* Sat Dec 02 2023 Justin Zobel <justin.zobel@gmail.com> - 1:5.246.0-1
- Update to 5.246.0

* Wed Nov 29 2023 Jan Grulich <jgrulich@redhat.com> - 1:0.11.76-4
- Rebuild (qt6)

* Sun Nov 19 2023 Alessandro Astone <ales.astone@gmail.com> - 1:0.11.76-3
- Backport translation files rename to not conflict with qt5 build

* Mon Nov 13 2023 Steve Cossette <farchord@gmail.com> - 0.11.76-2
- Fixed a spec mistake

* Mon Nov 13 2023 Steve Cossette <farchord@gmail.com> - 0.11.76-1
- 0.11.76

* Mon Nov 6 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231102.154105.6d270f9-1
- Initial Release

* Sat Sep 23 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231013.134815.a0375f9-1
- Initial release
