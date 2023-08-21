%undefine __cmake_in_source_build

Name:           seadrive-gui
Version:        2.0.28
Release:        1%{?dist}
Summary:        GUI part of Seafile Drive client

# main source:  Apache-2.0
# QtAwesome:    MIT
# FontAwesome:  OFL-1.1
License:        Apache-2.0 AND MIT AND OFL-1.1
URL:            https://seafile.com
Source0:        https://github.com/haiwen/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        seadrive.appdata.xml

ExclusiveArch:  %{qt5_qtwebengine_arches}

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  make

BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5WebEngine)
BuildRequires:  cmake(Qt5WebEngineCore)
BuildRequires:  cmake(Qt5WebEngineWidgets)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(jansson)
BuildRequires:  pkgconfig(libsearpc)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sqlite3)

# 3.x.unidentified with local changes
Provides:       bundled(QtAwesome)
Provides:       bundled(fontawesome-fonts) = 3.2.1
Requires:       hicolor-icon-theme
# Confirmed with upstream that versions are expected to be matching
# even if there's no direct dependency. New seadrive-daemon release
# would be tagged if there are GUI changes relevant for Linux
Requires:       seadrive-daemon = %{version}

%description
Seafile is a next-generation open source cloud storage system, with advanced
support for file syncing, privacy protection and teamwork.

Seafile allows users to create groups with file syncing, wiki, and discussion
to enable easy collaboration around documents within a team.

This package contains the GUI part of Seafile Drive client. The Drive client
enables you to access files on the server without syncing to local disk.


%prep
%autosetup -p1
# ensure that these don't affect the build
rm -rf third_party/{CrawlScopeCommandLine,macfuse.fs,MPMessagePack.framework,WinSparkle-0.5.3}


%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build


%install
%cmake_install
install -D -m 644 -pv %{SOURCE1} %{buildroot}%{_metainfodir}/seadrive.appdata.xml


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/seadrive.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/seadrive.appdata.xml


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/seadrive.desktop
%{_datadir}/icons/hicolor/*/apps/seadrive.png
%{_datadir}/icons/hicolor/scalable/apps/seadrive.svg
%{_datadir}/pixmaps/seadrive.png
%{_metainfodir}/seadrive.appdata.xml

%changelog
* Wed Aug 16 2023 Aleksei Bavshin <alebastr@fedoraproject.org> - 2.0.28-1
- Update to 2.0.28 (#2232277)
- Convert License tag to SPDX

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 22 2022 Aleksei Bavshin <alebastr@fedoraproject.org> - 2.0.22-1
- Update to 2.0.22 (#2099894)

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 08 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 2.0.16-1
- Update to 2.0.16

* Fri Aug 06 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 2.0.15-1
- Update to 2.0.15

* Sat Jul 24 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 2.0.10-3
- Fix build with glib2 >= 2.68

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 25 2020 Aleksei Bavshin <alebastr@fedoraproject.org> - 2.0.10-1
- Update to 2.0.10

* Sun Nov 01 2020 Aleksei Bavshin <alebastr89@gmail.com> - 2.0.7-1
- Initial import (#1895549)
