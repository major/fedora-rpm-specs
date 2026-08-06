Name:       kdominate
%global shortcommit 98240e03
%global gitdate 20260721.014343
Version:    26.11.70~%{gitdate}.%{shortcommit}
Release:    %autorelease
Summary:    KDominate is a tactical game for one or two players
License:    GPL-2.0-or-later AND BSD-3-Clause AND CC0-1.0
URL:        https://invent.kde.org/games/kdominate
Source0:    https://invent.kde.org/games/kdominate/-/archive/%{shortcommit}/%{name}-%{shortcommit}.tar.gz

Requires: hicolor-icon-theme

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros
BuildRequires: systemd-rpm-macros
BuildRequires: extra-cmake-modules
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KDEGames6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Svg)

%description
KDominate is a tactical game for one or two players,
where players place and convert tiles with the goal of
controlling the majority of the board.

%prep
%autosetup -n %{name}-%{shortcommit}

%conf
%cmake_kf6

%build
%cmake_build

%install
%cmake_install
%find_lang %{name} --with-html

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.kdominate.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.kdominate.metainfo.xml

%files -f %{name}.lang
%license LICENSES/*.txt
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/applications/org.kde.kdominate.desktop
%{_kf6_datadir}/config.kcfg/kdominate.kcfg
%{_kf6_datadir}/icons/hicolor/128x128/apps/kdominate.png
%{_kf6_datadir}/icons/hicolor/16x16/apps/kdominate.png
%{_kf6_datadir}/icons/hicolor/22x22/apps/kdominate.png
%{_kf6_datadir}/icons/hicolor/256x256/apps/kdominate.png
%{_kf6_datadir}/icons/hicolor/32x32/apps/kdominate.png
%{_kf6_datadir}/icons/hicolor/48x48/apps/kdominate.png
%{_kf6_datadir}/icons/hicolor/64x64/apps/kdominate.png
%{_kf6_metainfodir}/org.kde.kdominate.metainfo.xml
%{_kf6_datadir}/qlogging-categories6/kdominate.categories

%changelog
%autochangelog
