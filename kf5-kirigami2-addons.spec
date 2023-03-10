%global orig_name kirigami-addons

Name:           kf5-kirigami2-addons
Version:        0.7.2
Release:        1%{?dist}
Epoch:          1
License:        LGPLv3
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
%dir %{_kf5_qmldir}/org/kde/kirigamiaddons
%{_kf5_libdir}/qt5/qml/org/kde/kirigamiaddons/*
%{_kf5_libdir}/cmake/KF5KirigamiAddons/*


%files dateandtime
%{_kf5_qmldir}/org/kde/kirigamiaddons/dateandtime/

%files treeview
%{_kf5_qmldir}/org/kde/kirigamiaddons/treeview/

%changelog
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
