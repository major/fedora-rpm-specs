Name:           koko
Version:        22.06
Release:        1%{?dist}
License:        GPLv2+ and GPLv3 and LGPLv2 and LGPLv2+ and CC0 and BSD
Summary:        An Image gallery application
Url:            https://apps.kde.org/koko/
Source:         https://download.kde.org/stable/plasma-mobile/%{version}/koko-%{version}.tar.xz
Source1:        http://download.geonames.org/export/dump/cities1000.zip
Source2:        http://download.geonames.org/export/dump/admin1CodesASCII.txt
Source3:        http://download.geonames.org/export/dump/admin2Codes.txt

BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf5-rpm-macros
BuildRequires: kquickimageeditor-devel
BuildRequires: libgexiv2-devel
BuildRequires: xcb-util-devel

BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5Declarative)
BuildRequires: cmake(KF5FileMetaData)
BuildRequires: cmake(KF5GuiAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5Kirigami2)
BuildRequires: cmake(KF5Notifications)

BuildRequires: cmake(Qt5Positioning)
BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(Qt5QuickControls2)
BuildRequires: cmake(Qt5Svg)
BuildRequires: cmake(Qt5X11Extras)

%description
%{summary}.

%prep
%autosetup
# Copying these to src dir as per https://invent.kde.org/graphics/koko/-/blob/master/README.md Packaging section.
cp %{_topdir}/SOURCES/cities1000.zip src/
cp %{_topdir}/SOURCES/admin1CodesASCII.txt src/
cp %{_topdir}/SOURCES/admin2Codes.txt src/

%build
%cmake_kf5
%cmake_build

%install
%cmake_install
%find_lang %{name}
desktop-file-install --dir=%{buildroot}%{_kf5_datadir}/applications/ %{buildroot}/%{_kf5_datadir}/applications/org.kde.%{name}.desktop

%files -f %{name}.lang
%{_kf5_bindir}/%{name}

%{_kf5_datadir}/applications/org.kde.%{name}.desktop
%{_kf5_datadir}/icons/hicolor/*/apps/%{name}.*
%{_kf5_datadir}/knotifications5/*
%{_kf5_datadir}/%{name}

%{_kf5_libdir}/libkokocommon.so.0.0.1
# Confirmed with upstream that unversioned so belongs in main package.
%{_kf5_libdir}/qt5/qml/org/kde/%{name}/libkokoqmlplugin.so

%{_kf5_metainfodir}/org.kde.%{name}.appdata.xml

%{_kf5_qmldir}/org/kde/%{name}/*

%package devel
Summary: Development files for koko
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}.

%files devel
%{_kf5_libdir}/libkokocommon.so

%changelog
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
