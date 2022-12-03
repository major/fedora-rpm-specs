%global kf5_min_version 5.86.0

Name:           audiotube
Version:        22.11
Release:        1%{?dist}
License:        GPLv2+
Summary:        AudioTube can search YouTube Music, list albums and artists, play automatically generated playlists, albums and allows to put your own playlist together.
Url:            https://apps.kde.org/audiotube/
Source:         https://download.kde.org/stable/plasma-mobile/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

BuildRequires:  gcc-c++
BuildRequires:  extra-cmake-modules >= %{kf5_min_version}
BuildRequires:  kf5-rpm-macros      >= %{kf5_min_version}

BuildRequires: pybind11-devel
BuildRequires: python3-devel
BuildRequires: yt-dlp
BuildRequires: python3-ytmusicapi

BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(Qt5QuickControls2)
BuildRequires: cmake(Qt5Svg)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5QmlModels)
BuildRequires: cmake(Qt5Quick)
BuildRequires: cmake(Qt5QuickControls2)
BuildRequires: cmake(Qt5Widgets)

BuildRequires: cmake(KF5CoreAddons) >= %{kf5_min_version}
BuildRequires: cmake(KF5Crash) >= %{kf5_min_version}
BuildRequires: cmake(KF5I18n) >= %{kf5_min_version}
BuildRequires: cmake(KF5Kirigami2) >= %{kf5_min_version}


Requires:   hicolor-icon-theme
Requires:   yt-dlp
Requires:   python3-ytmusicapi
Requires:   kf5-kirigami2

%description
%{summary}.

%prep
%autosetup -p1

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
%{_kf5_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf5_datadir}/icons/hicolor/scalable/apps/org.kde.%{name}.svg


%changelog
* Thu Dec 01 2022 Justin Zobel <justin@1707.io> - 22.11-1
- Update to 22.11

* Wed Sep 28 2022 Justin Zobel <justin@1707.io> - 22.09-1
- Update to 22.09

* Thu Aug 25 2022 Justin Zobel <justin@1707.io> - 22.06-1
- Update to 22.06

* Sun Jul 31 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 22.04-4
- kf5-kirigami requirement added. Fix BZ#2112614

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.04-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 22.04-2
- Rebuilt for Python 3.11

* Wed May 04 2022 Justin Zobel <justin@1707.io> - 22.04-1
- Update to 22.04

* Thu Feb 10 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 22.02-1
- Plasma mobile version 22.02

* Sun Jan 16 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 21.12-1
- Initial version of package
