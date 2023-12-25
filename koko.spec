Name:           koko
Version:        24.01.85
Release:        1%{?dist}
License:        GPLv2+ and GPLv3 and LGPLv2 and LGPLv2+ and CC0 and BSD
Summary:        An Image gallery application
Url:            https://apps.kde.org/koko/
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Source1:        https://download.geonames.org/export/dump/cities1000.zip
Source2:        https://download.geonames.org/export/dump/admin1CodesASCII.txt
Source3:        https://download.geonames.org/export/dump/admin2Codes.txt

BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros
BuildRequires: libappstream-glib

BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Sql)
BuildRequires: cmake(Qt6Positioning)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: qt6-qtbase-private-devel

BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Declarative)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6GuiAddons)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6FileMetaData)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6Kirigami)
BuildRequires: cmake(KQuickImageEditor)

BuildRequires: pkgconfig(exiv2)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-atom)

# QML module dependencies
Requires:      kf6-kcoreaddons%{?_isa}
Requires:      kf6-kdeclarative%{?_isa}
Requires:      kf6-kirigami%{?_isa}
Requires:      kf6-kirigami-addons%{?_isa}
Requires:      kf6-purpose%{?_isa}
Requires:      kquickimageeditor-qt6%{?_isa}
Requires:      qt6-qtmultimedia%{?_isa}

Obsoletes:     %{name}-devel < 24.01.80

%description
%{summary}.

%prep
%autosetup
# Copying these to src dir as per https://invent.kde.org/graphics/koko/-/blob/master/README.md Packaging section.
cp %{_topdir}/SOURCES/cities1000.zip src/
cp %{_topdir}/SOURCES/admin1CodesASCII.txt src/
cp %{_topdir}/SOURCES/admin2Codes.txt src/

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml

%files -f %{name}.lang
%{_kf6_bindir}/%{name}

%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/icons/hicolor/*/apps/org.kde.%{name}.*
%{_kf6_datadir}/knotifications6/*
%{_kf6_datadir}/%{name}

%{_kf6_libdir}/libkokocommon.so.0.0.1
# internal library, no public API, no need for devel package
%exclude %{_kf6_libdir}/libkokocommon.so

%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml

%{_kf6_qmldir}/org/kde/%{name}/

%changelog
* Sat Dec 23 2023 ales.astone@gmail.com - 24.01.85-1
- 24.01.85

* Wed Dec 06 2023 Yaakov Selkowitz <yselkowitz@fedoraproject.org> - 24.01.80-1
- 24.01.80

* Thu Oct 12 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.2-1
- 23.08.2

* Sat Sep 16 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.1-1
- 23.08.1

* Sat Aug 26 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.0-1
- 23.08.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

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

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 01 2022 Justin Zobel <justin@1707.io> - 22.11-1
- Update to 22.11

* Wed Sep 28 2022 Justin Zobel <justin@1707.io> - 22.09-1
- Update to 22.09

* Thu Aug 25 2022 Justin Zobel <justin@1707.io> - 22.06-1
- Update to 22.06

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 03 2022 Justin Zobel <justin@1707.io> - 22.04-1
- Update to 22.04

* Sat Feb 26 2022 Justin Zobel <justin@1707.io> - 22.02
- Verison bump to 22.02

* Wed Dec 22 2021 Justin Zobel <justin@1707.io> - 21.12-1
- Initial version of package
