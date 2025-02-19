Name:    glaxnimate
Summary: A simple vector graphics animation program
Version: 0.5.80
Release: 1%{?dist}

License: GPL-2.0-or-later AND LGPL-3.0-or-later AND MIT AND BSD-2-Clause AND CC0-1.0 AND CC-BY-SA-4.0 AND GPL-3.0-or-later
URL:     https://glaxnimate.mattbas.org/
Source0: https://download.kde.org/unstable/%{name}/%{version}/%{name}-%{version}.tar.xz

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: kf6-rpm-macros
BuildRequires: extra-cmake-modules
BuildRequires: cmake
BuildRequires: gcc-c++

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Xml)
BuildRequires: cmake(Qt6UiTools)
BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Svg)

BuildRequires: cmake(KF6BreezeIcons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6Completion)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6Crash)

BuildRequires: ffmpeg-free-devel
BuildRequires: libarchive-devel

BuildRequires: doxygen
BuildRequires: python3-devel
BuildRequires: potrace-devel

Requires:      hicolor-icon-theme

%description
Glaxnimate is a powerful and user-friendly desktop application for
vector animation and motion design. It focuses on Lottie and SVG
and provides an intuitive interface that makes it easy to create
stunning animations.

%prep
%autosetup -p1

%build
%cmake_kf6 -DQT_MAJOR_VERSION=6
%cmake_build

%install
%cmake_install
%find_lang %{name} --all-name --with-html

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.glaxnimate.metainfo.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.glaxnimate.desktop

%files -f %{name}.lang
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/applications/org.kde.glaxnimate.desktop
%{_kf6_datadir}/config.kcfg/glaxnimate_settings.kcfg
%{_kf6_datadir}/glaxnimate/
%{_kf6_datadir}/icons/hicolor/512x512/apps/glaxnimate.png
%{_kf6_datadir}/icons/hicolor/512x512/apps/org.kde.glaxnimate.png
%{_kf6_datadir}/icons/hicolor/scalable/apps/glaxnimate.svg
%{_kf6_datadir}/icons/hicolor/scalable/apps/org.kde.glaxnimate.svg
%{_kf6_metainfodir}/org.kde.glaxnimate.metainfo.xml

%changelog
* Sun Feb 16 2025 Steve Cossette <farchord@gmail.com> - 0.5.80-1
- Initial Release
