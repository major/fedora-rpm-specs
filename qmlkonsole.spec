Name:           qmlkonsole
Version:        23.08.0
Release:        1%{?dist}
License:        GPLv2+
Summary:        Terminal app for Plasma Mobile
Url:            https://invent.kde.org/plasma-mobile/qmlkonsole
Source:         https://download.kde.org/stable/plasma-mobile/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  appstream
BuildRequires:  abseil-cpp-devel

BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5KirigamiAddons)
BuildRequires:  cmake(KF5WindowSystem)

Requires:       kf5-kirigami2
Requires:       kf5-kirigami2-addons
Requires:       qmltermwidget
Recommends:     dejavu-fonts-all

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
appstreamcli validate --no-net %{buildroot}%{_datadir}/metainfo/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.%{name}.desktop

%files -f %{name}.lang
%license LICENSES/GPL-2.0-or-later.txt
%{_kf5_bindir}/%{name}
%{_kf5_datadir}/applications/org.kde.%{name}.desktop
%{_kf5_datadir}/icons/hicolor/scalable/apps/org.kde.%{name}.svg
%{_kf5_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf5_datadir}/config.kcfg/terminalsettings.kcfg

%changelog
* Sat Sep 07 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.0-1
- 23.08.0

* Wed Aug 30 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 23.04.3-3
- Rebuilt for abseil-cpp 20230802.0

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 08 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.3-1
- 23.04.3

* Tue Jun 06 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.2-1
- 23.04.2

* Sat May 13 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.1-1
- 23.04.1

* Thu Apr 20 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.0-1
- 23.04.0

* Mon Mar 27 2023 Rich Mattes <richmattes@gmail.com> - 23.01.0-2
- Rebuild for abseil-cpp-20230125.1

* Mon Jan 30 2023 Justin Zobel <justin@1707.io> - 23.01.0-1
- Update to 23.01.0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 01 2022 Justin Zobel <justin@1707.io> - 22.11-1
- Update to 22.11

* Wed Sep 28 2022 Justin Zobel <justin@1707.io> - 22.09-1
- Update to 22.09

* Thu Aug 25 2022 Justin Zobel <justin@1707.io> - 22.06-1
- Update to 22.06

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 10 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 22.02-1
- Plasma mobile version 22.02

* Sun Jan 23 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 21.12-1
- 21.12

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Sep 13 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 21.08-1
- 21.08

* Tue Jun 08 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 21.06-1
- initial version of package
