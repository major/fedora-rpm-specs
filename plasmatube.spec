Name:           plasmatube
Version:        22.06
Release:        1%{?dist}
License:        GPLv3+ and CC0 and CC-BY-SA
Summary:        YouTube video player based on QtMultimedia and youtube-dl
Url:            https://apps.kde.org/plasmatube/
Source:         https://download.kde.org/stable/plasma-mobile/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf5-rpm-macros
BuildRequires:  libappstream-glib

BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Kirigami2)

BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5Svg)

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
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/org.kde.%{name}.appdata.xml

%files -f %{name}.lang
%license LICENSES/*

%{_kf5_bindir}/%{name}

%{_kf5_datadir}/applications/org.kde.%{name}.desktop
%{_kf5_datadir}/icons/hicolor/*/apps/org.kde.%{name}.*

%{_kf5_metainfodir}/org.kde.%{name}.appdata.xml

%changelog
* Thu May 05 2022 Justin Zobel <justin@1707.io> - 22.04-1
- Update to 22.04

* Tue Mar 1 2022 Jusitn Zobel <justin@1707.io> - 22.02-1
- Update to 22.02

* Wed Dec 22 2021 Justin Zobel <justin@1707.io> - 21.12-1
- Initial version of package
