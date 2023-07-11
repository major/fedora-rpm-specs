%global kf5_min_version 5.87.0

Name:     skanpage
Version:  23.04.3
Release:  1%{?dist}
Summary:  Utility to scan images and multi-page documents
# For a breakdown of the licensing, see PACKAGE-LICENSING
License:  GPLv3 and GPLv2 and CC0-1.0 and BSD

URL:      https://invent.kde.org/utilities/%{name}
Source0:  https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules >= %{kf5_min_version}
BuildRequires:  gcc-c++
BuildRequires:  kf5-rpm-macros      >= %{kf5_min_version}


BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5Widgets)


BuildRequires:  cmake(KF5Config)     >= %{kf5_min_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{kf5_min_version}
BuildRequires:  cmake(KF5Crash)      >= %{kf5_min_version}
BuildRequires:  cmake(KF5I18n)       >= %{kf5_min_version}
BuildRequires:  cmake(KF5Kirigami2)  >= %{kf5_min_version}
BuildRequires:  cmake(KF5Plasma)     >= %{kf5_min_version}
BuildRequires:  cmake(KF5Purpose)    >= %{kf5_min_version}
BuildRequires:  cmake(KF5Sane)       >= %{kf5_min_version}
BuildRequires:  cmake(KSaneCore)

Requires: qt5-qtquickcontrols2
Requires: kf5-kirigami2              >= %{kf5_min_version}

Recommends: sane-backends-drivers-scanners


%description
Skanpage is a multi-page scanning application built 
using the libksane library and a QML interface. 
It supports saving to image and PDF files.

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
%doc README.md
%{_bindir}/%{name}
%{_kf5_datadir}/applications/org.kde.%{name}.desktop
%{_kf5_metainfodir}/org.kde.%{name}.appdata.xml

%{_kf5_datadir}/qlogging-categories5/%{name}.categories
%{_kf5_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_kf5_datadir}/icons/hicolor/48x48/apps/%{name}.png

%changelog
* Sat Jul 08 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.3-1
- 23.04.3

* Tue Jun 06 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.2-1
- 23.04.2

* Sat May 13 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.1-1
- 23.04.1

* Fri Apr 14 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.0-1
- 23.04.0

* Fri Mar 31 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.90-1
- 23.03.90

* Mon Mar 20 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.80-1
- 23.03.80

* Thu Mar 02 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 22.12.3-1
- 22.12.3

* Tue Jan 31 2023 Marc Deop <marcdeop@fedoraproject.org> - 22.12.2-1
- 22.12.2

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 03 2023 Justin Zobel <justin@1707.io> - 22.12.1-1
- Update to 22.12.1

* Sun Dec 25 2022 Justin Zobel <justin@1707.io> - 22.12.0-1
- Update to 22.12.0

* Thu Jul 28 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 22.04.3-3
- sane-backends-drivers-scanners recommendation for additional scanner added.

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Than Ngo <than@redhat.com> - 22.04.3-1
- 22.04.3

* Sun May 15 2022 Justin Zobel <justin@1707.io> - 22.04.1-1
- Update to 22.04.1

* Sun Feb 27 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 1.0-1
- Initial package for skapage 1.0
