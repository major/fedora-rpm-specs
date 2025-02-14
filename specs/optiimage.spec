Name:          optiimage
Version:       1.0.0
Release:       1%{?dist}
License:       LGPL-2.1-only AND LGPL-2.1-or-later AND GPL-3.0-only AND CC0-1.0 AND GPL-2.0-only AND LGPL-2.0-or-later AND GPL-3.0-or-later AND BSD-2-Clause AND LGPL-3.0-only AND FSFAP
Summary:       A useful image compressor that supports many file types
URL:           https://apps.kde.org/%{name}/

Source0:       https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz

BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
Requires: hicolor-icon-theme

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Widgets)

BuildRequires: cmake(KF6Kirigami)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(QCoro6Core)
BuildRequires: cmake(QCoro6Qml)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6KirigamiAddons)
BuildRequires: reuse
BuildRequires: qt6-qtbase-private-devel
BuildRequires: python3-devel

# QML Imports
Requires: qt6qml(org.kde.kirigami)
Requires: qt6qml(org.kde.kirigamiaddons.components)

# Runtime requirements
Requires: libwebp-tools
Requires: jpegoptim
Requires: python3-scour
Requires: oxipng

%description
Optimize your images with OptiImage, a useful image compressor that supports
PNG, JPEG, WebP and SVG file types.
It supports both lossless and lossy compression modes with an option to whether
keep or not metadata of images. It additionally has a safe mode, where a new
image is created instead of overwritting the old one.

%prep
%autosetup -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.optiimage.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_bindir}/optiimage
%{_datadir}/applications/org.kde.optiimage.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.kde.optiimage.svg
%{_metainfodir}/org.kde.optiimage.metainfo.xml

%changelog
* Mon Dec 02 2024 Steve Cossette <farchord@gmail.com> - 1.0.0-1
- Initial Release
