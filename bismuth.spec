Name:           bismuth
Version:        3.1.4
Release:        %autorelease
Summary:        KDE Plasma extension that lets you tile your windows automatically

License:        MIT AND BSD-3-Clause AND LGPL-3.0-or-later AND CC-BY-4.0
URL:            https://bismuth-forge.github.io/bismuth
VCS:            https://github.com/Bismuth-Forge/bismuth
Source:         %vcs/archive/v%{version}/%{name}-%{version}.tar.gz

# Due to problem with kconfig_compiler
# https://invent.kde.org/frameworks/kconfig/-/blob/master/src/kconfig_compiler/KConfigHeaderGenerator.cpp#L224
# Temporarily exclude those archictures 
ExcludeArch: ppc64le armv7hl s390x

BuildRequires:  cmake 
BuildRequires:  ninja-build 
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  golang-github-evanw-esbuild

BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5GlobalAccel)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KDecoration2)

BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Feedback)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5Core)

BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtdeclarative-devel 

Requires:   kwin
Requires:   hicolor-icon-theme


%global _description %{expand:
KDE Plasma extension, that lets you tile your windows automatically and manage
them via keyboard, just like in classical tiling window managers.}

%description %_description

%prep
%autosetup

%build
%cmake_kf5 -G Ninja \
           -DUSE_NPM=OFF \
           -DUSE_TSC=OFF \
           -DBUILD_TESTING=false

%cmake_build

%install
%cmake_install

%files
%license LICENSES/MIT.txt
%doc README.md CHANGELOG.md CONTRIBUTING.md

%dir %{_kf5_qmldir}/org/kde/%{name}
%dir %{_kf5_qmldir}/org/kde/%{name}/core

%{_kf5_qmldir}/org/kde/%{name}/core/lib%{name}_core.so
%{_kf5_qmldir}/org/kde/%{name}/core/qmldir

%{_kf5_qtplugindir}/kcms/kcm_%{name}.so
%{_kf5_qtplugindir}/org.kde.kdecoration2/%{name}_kdecoration.so

%{_kf5_datadir}/kpackage/kcms/kcm_%{name}
%{_kf5_datadir}/kservices5/kcm_%{name}.desktop
%{_kf5_datadir}/kwin/scripts/%{name}
%{_kf5_datadir}/icons/hicolor/*/status/*
%{_kf5_datadir}/icons/hicolor/*/categories/*.svg
%{_kf5_datadir}/icons/hicolor/scalable/apps/*.svg
%{_kf5_datadir}/kconf_update/%{name}*
%{_kf5_datadir}/qlogging-categories5/%{name}.categories
%{_kf5_datadir}/config.kcfg/%{name}_config.kcfg


%changelog
%autochangelog
