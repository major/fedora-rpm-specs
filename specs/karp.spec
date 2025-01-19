%global gitcommit de3b6305b0cc6021563b25e9c168c51621653626
%global gitdate 20241125.202901
%global shortcommit %(c=%{gitcommit}; echo ${c:0:7})

Name:          karp
Version:       25.03.70~%{gitdate}.%{shortcommit}
Release:       3%{?dist}
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

Requires: hicolor-icon-theme
Requires: kf6-kirigami-addons
Requires: qpdf
Requires: ghostscript

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

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 25.03.70~20241125.202901.de3b630-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Nov 26 2024 Steve Cossette <farchord@gmail.com> - 25.03.70~20241125.202901.de3b630-2
- Require ghostscript

* Mon Jun 17 2024 Steve Cossette <farchord@gmail.com> - 25.03.70~20241125.202901.de3b630-1
- Initial Release
