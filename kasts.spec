%global kf5_min_version 5.88.0

Name:           kasts
Version:        22.11
Release:        1%{?dist}
License:        GPLv2 and GPLv2+ and GPLv3+ and BSD and LGPLv3+
Summary:        A mobile podcast application
Url:            https://apps.kde.org/%{name}
Source:         https://download.kde.org/stable/plasma-mobile/22.09/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  taglib-devel

BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5Keychain)


BuildRequires:  kf5-rpm-macros          >= %{kf5_min_version}
BuildRequires:  cmake(KF5CoreAddons)    >= %{kf5_min_version}
BuildRequires:  cmake(KF5Syndication)   >= %{kf5_min_version}
BuildRequires:  cmake(KF5Config)        >= %{kf5_min_version}
BuildRequires:  cmake(KF5I18n)          >= %{kf5_min_version}
BuildRequires:  cmake(KF5ThreadWeaver)  >= %{kf5_min_version}

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
%license LICENSES/*
%{_kf5_bindir}/%{name}
%{_kf5_datadir}/applications/org.kde.%{name}.desktop
%{_kf5_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_kf5_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf5_libdir}/libKastsSolidExtras.so
%{_kf5_qmldir}/org/kde/%{name}/solidextras/qmldir
%{_kf5_qmldir}/org/kde/%{name}/solidextras/libkasts-solidextrasqmlplugin.so


%changelog
* Thu Dec 01 2022 Justin Zobel <justin@1707.io> - 22.11-1
- Update to 22.11

* Wed Sep 28 2022 Justin Zobel <justin@1707.io> - 22.09.2-1
- Update to 22.09.2

* Thu Aug 25 2022 Justin Zobel <justin@1707.io> - 22.06-1
- Update to 22.06

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Apr 19 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 22.02-1
- Update to 22.02

* Sun Jan 16 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 21.12-1
- Initial package
