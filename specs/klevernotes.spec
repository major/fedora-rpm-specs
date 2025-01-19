Name:          klevernotes
Version:       1.1.0
Release:       3%{?dist}
License:       BSD-3-Clause AND CC-BY-SA-4.0 AND CC0-1.0 AND FSFAP AND GPL-2.0-or-later AND GPL-3.0-only AND GPL-3.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only
Summary:       A convergent markdown note taking application
URL:           https://apps.kde.org/klevernotes/

Source0:       https://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.xz

Patch0:        no-ksandbox.patch

# handled by qt6-srpm-macros, which defines %%qt6_qtwebengine_arches
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}

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
BuildRequires: cmake(Qt6WebEngineQuick)

BuildRequires: cmake(KF6Kirigami)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6KIO)

Requires: hicolor-icon-theme
Requires: qt6qml(org.kde.kirigami)
Requires: qt6qml(org.kde.kirigamiaddons.formcard)
Requires: qt6qml(org.kde.kitemmodels)
Requires: qt6qml(QtWebChannel)
Requires: qt6qml(QtWebEngine)

%description
KleverNotes is a note taking and management application
for your mobile and desktop devices. It uses markdown
and allow you to preview your content. Different Markdown
flavors are supported thanks to its custom Markdown parser
based Marked.js, which make the integration of "plugins"
and new features even easier.


%prep
%autosetup -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{name} --with-man --with-qt --all-name

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.klevernotes.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%files -f %{name}.lang
%doc README.md
%license LICENSES/*
%{_kf6_bindir}/klevernotes
%{_kf6_datadir}/applications/org.kde.klevernotes.desktop
%{_kf6_datadir}/icons/hicolor/scalable/apps/org.kde.klevernotes.svg
%{_kf6_metainfodir}/org.kde.klevernotes.metainfo.xml

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Nov 26 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 1.1.0-2
- Do not exit sandbox for additional tools

* Mon Nov 25 2024 Steve Cossette <farchord@gmail.com> - 1.1.0-1
- Initial Release
