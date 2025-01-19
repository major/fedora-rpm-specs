Name:          marknote
Version:       1.3.0
Release:       2%{?dist}
License:       BSD-3-Clause AND CC-BY-SA-4.0 AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND GPL-3.0-or-later AND LGPL-2.0-only AND LGPL-2.1-or-later AND LGPL-3.0-only
Summary:       A simple markdown note management app for KDE
URL:           https://apps.kde.org/%{name}/

Source0:       https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz

BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Widgets)

BuildRequires: cmake(KF6Kirigami)
BuildRequires: cmake(KF6KirigamiAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6ColorScheme)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6BreezeIcons)

BuildRequires: cmake(KPim6Mime)

BuildRequires: cmake(md4c)

Requires:      hicolor-icon-theme
Requires:      qt6qml(org.kde.iconthemes)
Requires:      qt6qml(org.kde.kirigamiaddons.components)
Requires:      qt6qml(org.kde.kitemmodels)
Requires:      qt6qml(org.kde.sonnet)

%description
Marknote lets you create rich text notes and easily organize them
into notebooks. You can personalize your notebooks by choosing an
icon and accent color for each one, making it easy to distinguish
between them and keep your notes at your fingertips.


%prep
%autosetup -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{name} --with-man --with-qt --all-name

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.marknote.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_bindir}/marknote
%{_kf6_datadir}/applications/org.kde.marknote.desktop
%{_kf6_datadir}/icons/hicolor/scalable/apps/org.kde.marknote.svg
%{_kf6_metainfodir}/org.kde.%{name}.metainfo.xml
%{_kf6_datadir}/qlogging-categories6/marknote.categories

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Aug 26 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 1.3.0-1
- 1.3.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Apr 01 2024 Steve Cossette <farchord@gmail.com> - 1.1.1-1
- 1.1.1

* Sat Mar 30 2024 Steve Cossette <farchord@gmail.com> - 1.0.0-1
- Initial Release
