%global orig_name kirigami-addons

Name:           kf5-kirigami2-addons
Version:        21.05
Release:        7%{?dist}
License:        LGPLv3
Summary:        Convergent visual components ("widgets") for Kirigami-based applications
Url:            https://invent.kde.org/libraries/kirigami-addons
Source:         https://invent.kde.org/libraries/%{orig_name}/-/archive/release/%{version}/%{orig_name}-release-%{version}.tar.gz


BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros

BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Quick) 
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Kirigami2)


%description
A set of "widgets" i.e visual end user components along with a
code to support them. Components are usable by both touch and
desktop experiences providing a native experience on both, and
look native with any QQC2 style (qqc2-desktop-theme, Material
or Plasma).

%package dateandtime
Summary:        Date and time add-on for the Kirigami framework
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description dateandtime
Date and time Kirigami addons, which complements other
software like Kclock.

%package treeview
Summary:         Tree view add-on for the Kirigami framework
Requires:        %{name}%{?_isa} = %{version}-%{release}
%description treeview
Tree view Kirigami addon, which is useful for listing files.

%prep
%autosetup -n %{orig_name}-release-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSES/
%dir %{_kf5_qmldir}/org/kde
%dir %{_kf5_qmldir}/org/kde/kirigamiaddons


%files dateandtime
%{_kf5_qmldir}/org/kde/kirigamiaddons/dateandtime/

%files treeview
%{_kf5_qmldir}/org/kde/kirigamiaddons/treeview/

%changelog
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