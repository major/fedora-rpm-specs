Name:           alligator 
Version:        23.04.3
Release:        1%{?dist}
License:        GPLv2 or GPLv3
Summary:        Kirigami-based RSS reader
Url:            https://invent.kde.org/plasma-mobile/alligator
Source:         https://download.kde.org/stable/plasma-mobile/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  appstream

BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5Sql)

BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KirigamiAddons)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5Syndication)

Requires:       hicolor-icon-theme
# QML module dependencies
Requires:       kf5-kirigami2%{?_isa}
Requires:       kf5-kirigami2-addons%{?_isa}
Requires:       qt5-qtquickcontrols2%{?_isa}

%description
Alligator is a convergent RSS/Atom feed reader.

%prep
%autosetup -n alligator-%{version}

%build
%cmake_kf5
%cmake_build

%install
%cmake_install
%find_lang %{name}
chmod -x %{buildroot}%{_datadir}/applications/org.kde.%{name}.desktop


%check
appstreamcli validate --no-net %{buildroot}%{_datadir}/metainfo/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.%{name}.desktop

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf5_bindir}/%{name}
%{_kf5_datadir}/applications/org.kde.%{name}.desktop
%{_kf5_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf5_datadir}/icons/hicolor/scalable/apps/%{name}.svg


%changelog
* Sat Jul 08 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.3-1
- 23.04.3

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

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 01 2022 Justin Zobel <justin@1707.io> - 22.11-1
- Update to 22.11

* Wed Sep 28 2022 Justin Zobel <justin@1707.io> - 22.09-1
- Update to 22.09

* Thu Aug 25 2022 Justin Zobel <justin@1707.io> - 22.06-1
- Update to 22.06

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 10 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 22.02-1
- Plasma mobile version 22.02

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan 16 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 21.12-1
- 21.12

* Sun Sep 12 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 21.08-2
- Source1 removed

* Sun Sep 12 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 21.08-1
- 21.08

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 16 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 21.06-1
- 21.06

* Sat May 22 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 21.05-2
- License section fixed

* Sun May 16 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 21.05-1
- initial version of package

