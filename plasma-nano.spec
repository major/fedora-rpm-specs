
%global kf5_min_version 5.88.0
%global orig_name org.kde.plasma.nano

Name:    plasma-nano
Version: 5.26.0
Release: 1%{?dist}
License: MIT and GPLv2+ and LGPLv2+
URL:     https://invent.kde.org/plasma/plasma-nano
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source:  https://download.kde.org/%{stable}/plasma/%{version}/%{name}-%{version}.tar.xz

Summary: A minimalist Plasma shell for developing custom experiences on embedded devices.


BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  libappstream-glib
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros          >= %{kf5_min_version}
BuildRequires:  hicolor-icon-theme
BuildRequires:  desktop-file-utils


BuildRequires:  cmake(KF5I18n)              >= %{kf5_min_version}
BuildRequires:  cmake(KF5KIO)               >= %{kf5_min_version}
BuildRequires:  cmake(KF5Notifications)     >= %{kf5_min_version}
BuildRequires:  cmake(KF5Plasma)            >= %{kf5_min_version}
BuildRequires:  cmake(KF5Service)           >= %{kf5_min_version}
BuildRequires:  cmake(KF5Wayland)           >= %{kf5_min_version}
BuildRequires:  cmake(KWinDBusInterface)    >= %{kf5_min_version}
BuildRequires:  cmake(KF5WindowSystem)      >= %{kf5_min_version}
BuildRequires:  cmake(KF5Package)           >= %{kf5_min_version}
BuildRequires:  cmake(KF5CoreAddons)        >= %{kf5_min_version}
BuildRequires:  cmake(Qt5Qml)


Requires: kf5-plasma
Requires: kf5-kwayland
Requires: kf5-kwindowsystem
Requires: kf5-kservice
Requires: kf5-kcoreaddons
Requires: kf5-kpackage
Requires: qt5-qtdeclarative


%description
%{Summary}

%prep
%autosetup -n %{name}-%{version}

%build
%cmake_kf5
%cmake_build

%install
%cmake_install
sed -i 's,<icon type="stock">plasma</icon>, ,g' %{buildroot}%{_kf5_metainfodir}/%{orig_name}.desktoptoolbox.appdata.xml
%find_lang plasma_shell_%{orig_name} --all-name

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/%{orig_name}.desktoptoolbox.appdata.xml


%files -f plasma_shell_%{orig_name}.lang
%license LICENSES/*.txt
%doc README.md

%{_kf5_metainfodir}/%{orig_name}.desktoptoolbox.appdata.xml
%{_kf5_qmldir}/org/kde/plasma/private/nanoshell
%{_kf5_datadir}/kservices5/plasma-applet-%{orig_name}.desktop
%{_kf5_datadir}/kservices5/plasma-package-%{orig_name}.desktoptoolbox.desktop
%{_kf5_datadir}/plasma/packages/%{orig_name}.desktoptoolbox
%{_kf5_datadir}/plasma/shells/%{orig_name}


%changelog
* Thu Oct 06 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.26.0-1
- 5.26.0

* Sat Sep 17 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.25.90-1
- 5.25.90

* Wed Sep 07 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.25.5-1
- 5.25.5

* Wed Aug 31 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 5.25.4-1
- 5.25.4

* Sat Apr 16 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 5.24.4-1
- 5.24.4

* Mon Jan 17 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 5.23.5-1
- Initial version of package

