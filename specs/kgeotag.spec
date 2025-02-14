Name:          kgeotag
Version:       1.7.0
Release:       1%{?dist}
License:       CC-BY-SA-4.0 AND CC0-1.0 AND ODbL-1.0 AND BSD-3-Clause AND GPL-3.0-only
Summary:       Photo geotagging program for KDE Plasma
URL:           https://apps.kde.org/%{name}/

Source0:       https://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.xz

# handled by qt6-srpm-macros, which defines %%qt6_qtwebengine_arches
# Because of Marble
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}

BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Network)

BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KExiv2Qt6)
BuildRequires: cmake(Marble)

%description
A Free/Libre Open Source photo geotagging program
built using Qt/C++ and uses the KDE frameworks.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%cmake_kf6 -DQT_MAJOR_VERSION=6
%cmake_build

%install
%cmake_install
%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.kgeotag.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%files -f %{name}.lang
%license LICENSES/*
%doc README.md
%{_kf6_bindir}/kgeotag
%{_kf6_datadir}/applications/org.kde.kgeotag.desktop
%{_docdir}/HTML/en/kgeotag/
%{_kf6_datadir}/icons/hicolor/128x128/apps/kgeotag.png
%{_kf6_datadir}/icons/hicolor/16x16/apps/kgeotag.png
%{_kf6_datadir}/icons/hicolor/22x22/apps/kgeotag.png
%{_kf6_datadir}/icons/hicolor/32x32/apps/kgeotag.png
%{_kf6_datadir}/icons/hicolor/48x48/apps/kgeotag.png
%{_kf6_datadir}/icons/hicolor/64x64/apps/kgeotag.png
%{_kf6_datadir}/kgeotag/
%{_kf6_metainfodir}/org.kde.kgeotag.appdata.xml

%changelog
* Sun Dec 08 2024 Steve Cossette <farchord@gmail.com> - 1.7.0-1
- Initial Release
