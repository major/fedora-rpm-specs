%global kf5_min_version 5.88.0

Name:           kalk
Version:        23.04.1
Release:        1%{?dist}
License:        GPLv3+
Summary:        %{name} is a convergent calculator for Plasma.
Url:            https://apps.kde.org/%{name}/
Source:         https://download.kde.org/stable/plasma-mobile/%{version}/%{name}-%{version}.tar.xz

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros

BuildRequires: bison
BuildRequires: flex
BuildRequires: mpfr-devel

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

BuildRequires: cmake(KF5Config) >= %{kf5_min_version} 
BuildRequires: cmake(KF5I18n) >= %{kf5_min_version}
BuildRequires: cmake(KF5CoreAddons) >= %{kf5_min_version}
BuildRequires: cmake(KF5UnitConversion) >= %{kf5_min_version}
BuildRequires: cmake(KF5Kirigami2) >= %{kf5_min_version}

BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Feedback)
BuildRequires: cmake(Qt5Quick)
BuildRequires: cmake(Qt5QuickControls2)

%description
%{summary}.

%prep
%autosetup

%build
%cmake_kf5
%cmake_build

%install
%cmake_install
%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/org.kde.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/org.kde.%{name}.appdata.xml

%files -f %{name}.lang
%{_kf5_bindir}/%{name}

%{_kf5_datadir}/applications/org.kde.%{name}.desktop
%{_kf5_datadir}/icons/hicolor/scalable/apps/org.kde.%{name}.svg

%{_kf5_metainfodir}/org.kde.%{name}.appdata.xml

%license LICENSES/*

%changelog
* Sat May 13 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.1-1
- 23.04.1

* Thu Apr 20 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.0-1
- 23.04.0

* Fri Mar 31 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.90-1
- 23.03.90

* Mon Mar 20 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.80-1
- 23.03.80

* Mon Jan 30 2023 Justin Zobel <justin@1707.io> - 23.01.0-1
- Update to 23.01.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 01 2022 Justin Zobel <justin@1707.io> - 22.11-1
- Update to 22.11

* Wed Sep 28 2022 Justin Zobel <justin@1707.io> - 22.09-1
- Update to 22.09

* Thu Aug 25 2022 Justin Zobel <justin@1707.io> - 22.06-1
- Update to 22.06

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jan 16 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 21.12-1
- Initial package
