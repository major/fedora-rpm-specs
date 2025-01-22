%global gitcommit 2b92073a0742cd87c5bbfc69b161e09064f71604
%global gitdate 20240615.212920
%global shortcommit %(c=%{gitcommit}; echo ${c:0:7})

Name:          plasma-camera
Version:       1.0^%{gitdate}.%{shortcommit}
Release:       2%{?dist}
License:       BSD-3-Clause AND GPL-2.0-or-later AND CC0-1.0 AND GPL-3.0-or-later
Summary:       Camera application for Plasma Mobile
URL:           https://apps.kde.org/plasma-camera/

Source0:       https://invent.kde.org/plasma-mobile/%{name}/-/archive/%{gitcommit}/%{name}-%{gitcommit}.tar.gz

BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6Widgets)

BuildRequires: cmake(KF6Kirigami)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Config)

%description
%{summary}.
It supports different resolutions, different white balance modes and
switching between different camera devices.


%prep
%autosetup -p1 -n %{name}-%{gitcommit}


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{name} --with-man --with-qt --all-name

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.plasma.camera.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%files -f %{name}.lang
%license LICENSES/*
%{_bindir}/plasma-camera
%{_kf6_datadir}/applications/org.kde.plasma.camera.desktop
%{_metainfodir}/org.kde.plasma.camera.appdata.xml

%changelog
* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0^20240615.212920.2b92073-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jun 17 2024 Steve Cossette <farchord@gmail.com> - 1.0^2b92073.20240615.212920
- Initial Release
