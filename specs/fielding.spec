%global gitcommit 1912c8055d9f607916e0c6fc568e2c0ee0336493
%global gitdate 20231028.022709
%global shortcommit %(c=%{gitcommit}; echo ${c:0:7})

Name:          fielding
Version:       0.1~%{gitdate}.%{shortcommit}
Release:       6%{?dist}
Summary:       A simple REST API testing tool

# The following files contribute to the licenses of the binary RPMs:
#
# CC0-1.0:
#   - README.md
#   - org.kde.fielding.desktop
#   - org.kde.fielding.json
#   - org.kde.fielding.metainfo.xml
# GPL-3.0-or-later:
#   - po/
#   - src/ui/
# LGPL-2.0-or-later:
#   - logo.png
#   - src/fieldingconfig.{kcfg,kcfgc}
# LGPL-2.1-or-later:
#   - src/app.{cpp,h}
#   - src/controller.{cpp,h}
#   - src/main.cpp
#
# The basis for considering the translations (po/) GPL-3.0-or-later is that
# their header comments say they are “distributed under the same license as
# the fielding package,” and the <project_license> tag in
# org.kde.fielding.metainfo.xml suggests that upstream considers this to be
# GPL-3.0-or-later.
#
# The following files do not contribute to the licenses of the binary RPMs,
# e.g. because they belong to the build system.
#
# CC0-1.0:
#   - .gitlab-ci.yml
#   - .kde-ci.yml
#   - Messages.sh
#   - src/Messages.sh
# BSD-2-Clause:
#   - CMakeLists.txt
#   - src/CMakeLists.txt
#
# The Messages.sh files (and perhaps the CI YAML files?) would normally be
# considered code, for which the CC0-1.0 license is not-allowed. However,
# they fall under the following exception:
#
#   Upstream application of CC0-1.0 to trivial, noncreative, unoriginal, and
#   nonexpressive material as part of an effort to achieve conformance to the
#   REUSE specification (https://reuse.software/) (for example, CI/CD
#   configuration files) is permitted regardless of whether such material
#   would normally be classified as "content".
License:       CC0-1.0 AND GPL-3.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:           https://apps.kde.org/en-gb/%{name}/

Source:       https://invent.kde.org/utilities/%{name}/-/archive/%{shortcommit}/%{name}-%{shortcommit}.tar.gz

BuildRequires: kf6-rpm-macros
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: cmake(Qt6Core)
BuildRequires: qt6-qtbase-private-devel
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: pkgconfig(xkbcommon)

BuildRequires: cmake(KF6Kirigami2)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6DBusAddons)

Requires: hicolor-icon-theme

%description
%{summary}.

%prep
%autosetup -n %{name}-%{shortcommit} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
# No translations for this package yet.

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.kde.fielding.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.fielding.metainfo.xml

%files
%license LICENSES/*
%doc README.md
%{_bindir}/fielding
%{_datadir}/applications/org.kde.fielding.desktop
%{_kf6_metainfodir}/org.kde.fielding.metainfo.xml
%{_datadir}/icons/hicolor/scalable/apps/org.kde.fielding.svg

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1~20231028.022709.1912c80-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Oct 14 2024 Jan Grulich <jgrulich@redhat.com> - 0.1~20231028.022709.1912c80-5
- Rebuild (qt6)

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1~20231028.022709.1912c80-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 04 2024 Jan Grulich <jgrulich@redhat.com> - 0.1~20231028.022709.1912c80-3
- Rebuild (qt6)

* Thu Apr 04 2024 Jan Grulich <jgrulich@redhat.com> - 0.1~20231028.022709.1912c80-2
- Rebuild (qt6)

* Thu Oct 12 2023 Steve Cossette <farchord@gmail.com> - 0.1~20231028.022709.1912c80-1
- v0.1
