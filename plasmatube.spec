Name:           plasmatube
Version:        23.04.2
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
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Kirigami2)

BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5Svg)

BuildRequires:  pkgconfig(mpv)

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
* Tue Jun 06 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.2-1
- 23.04.2

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

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 01 2022 Justin Zobel <justin@1707.io> - 22.11-1
- Update to 22.11

* Wed Sep 28 2022 Justin Zobel <justin@1707.io> - 22.09-1
- Update to 22.09

* Thu May 05 2022 Justin Zobel <justin@1707.io> - 22.04-1
- Update to 22.04

* Tue Mar 1 2022 Jusitn Zobel <justin@1707.io> - 22.02-1
- Update to 22.02

* Wed Dec 22 2021 Justin Zobel <justin@1707.io> - 21.12-1
- Initial version of package
