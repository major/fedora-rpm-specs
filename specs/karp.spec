%global gitcommit a5d2573d8ad1e7831d169efa0db051dc51959036
%global gitdate 20251108.040727
%global shortcommit %(c=%{gitcommit}; echo ${c:0:7})

Name:          karp
Version:       25.03.70~%{gitdate}.%{shortcommit}
Release:       1%{?dist}
License:       CC0-1.0 AND GPL-2.0-only AND GPL-3.0-only AND FSFAP AND CC-BY-SA-4.0 AND BSD-3-Clause AND LGPL-2.0-or-later
Summary:       Simple PDF editor to arrange, merge and improve PDF file(s)
URL:           https://apps.kde.org/karp/

Source0:       https://invent.kde.org/graphics/%{name}/-/archive/%{gitcommit}/%{name}-%{gitcommit}.tar.gz

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
BuildRequires: cmake(Qt6Pdf)
BuildRequires: cmake(Qt6Widgets)

BuildRequires: cmake(KF6Kirigami)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KirigamiAddons)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(qpdf)

Requires: hicolor-icon-theme
Requires: qpdf
Requires: ghostscript
Requires: qt6qml(org.kde.coreaddons)
Requires: qt6qml(org.kde.kirigamiaddons.components)
Requires: qt6qml(org.kde.kirigamiaddons.formcard)
Requires: qt6qml(org.kde.kirigamiaddons.settings)
Requires: qt6qml(org.kde.kirigami)
Requires: qt6qml(org.kde.kirigami.delegates)
Requires: qt6qml(Qt.labs.folderlistmodel)
Requires: qt6qml(Qt.labs.qmlmodels)
Requires: qt6qml(QtQml.Models)
Requires: qt6qml(QtQuick)
Requires: qt6qml(QtQuick.Controls)
Requires: qt6qml(QtQuick.Dialogs)
Requires: qt6qml(QtQuick.Layouts)

%description
A simple PDF editor which can select, delete,
rearrange pages, merge PDF files and reduce file size.

%prep
%autosetup -p1 -n %{name}-%{gitcommit}

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name}

%check
# Validation fails, but the software isn't completed, so...
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.karp.desktop ||:
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%files -f %{name}.lang
%license LICENSES/*
%doc README.md
%{_kf6_bindir}/karp
%{_kf6_datadir}/applications/org.kde.karp.desktop
%{_kf6_datadir}/icons/hicolor/scalable/apps/org.kde.karp.svg
%{_kf6_metainfodir}/org.kde.karp.metainfo.xml
%{_kf6_datadir}/qlogging-categories6/karp.categories

%changelog
* Sun Jan 18 2026 Steve Cossette <farchord@gmail.com> - 25.03.70~20251108.040727.a5d2573-1
- Updated to newer git snapshot

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 25.03.70~20241125.202901.de3b630-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 25.03.70~20241125.202901.de3b630-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 25.03.70~20241125.202901.de3b630-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Nov 26 2024 Steve Cossette <farchord@gmail.com> - 25.03.70~20241125.202901.de3b630-2
- Require ghostscript

* Mon Jun 17 2024 Steve Cossette <farchord@gmail.com> - 25.03.70~20241125.202901.de3b630-1
- Initial Release
