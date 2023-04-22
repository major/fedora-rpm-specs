Name:           krecorder 
Version:        23.04.0
Release:        1%{?dist}
License:        GPLv3+
Summary:        Convergent KDE audio recording application
Url:            https://invent.kde.org/plasma-mobile/krecorder
Source0:        https://download.kde.org/stable/plasma-mobile/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  appstream

BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5Svg)

BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5KirigamiAddons)
BuildRequires:  cmake(KF5WindowSystem)

Requires:       kf5-kirigami2
Requires:       gstreamer1-plugins-good
Requires:       hicolor-icon-theme
Requires:       kf5-kirigami2-addons

%description
Audio recorder for Plasma Mobile and other platforms

%prep
%autosetup -n %{name}-%{version}

%build
%cmake_kf5
%cmake_build

%install
%cmake_install
chmod -x %{buildroot}%{_datadir}/applications/org.kde.%{name}.desktop
sed -i 's/GPL-3+/GPL-3.0-or-later/g' %{buildroot}%{_datadir}/metainfo/org.kde.%{name}.appdata.xml
sed -i 's/Multimedia/AudioVideo;Audio/g' %{buildroot}%{_datadir}/applications/org.kde.%{name}.desktop
%find_lang %{name}

%check
appstreamcli validate --no-net %{buildroot}%{_datadir}/metainfo/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.%{name}.desktop


%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf5_bindir}/%{name}
%{_kf5_datadir}/applications/org.kde.%{name}.desktop
%{_kf5_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf5_datadir}/icons/hicolor/scalable/apps/org.kde.%{name}.svg

%changelog
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

* Wed Oct 12 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 22.09-2
- Adding Missing Runtime requries (kf5-kirigami2-addons) fix #2134145

* Wed Sep 28 2022 Justin Zobel <justin@1707.io> - 22.09-1
- Update to 22.09

* Thu Aug 25 2022 Justin Zobel <justin@1707.io> - 22.06-1
- Update to 22.06

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 10 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 22.02-1
- Plasma mobile version 22.02

* Sat Feb 05 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.12-1
- 21.12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 16 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 21.06-1
- 21.06

* Sat May 15 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 21.05-2
- update appdata license and desktop file category 

* Thu May 06 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 21.05-1
- initial package
