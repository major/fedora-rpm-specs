Name: dustrac
Summary: Traditional top-down car racing game

# GPL-3.0-or-later:
# - The game proper.
#
# GPL-2.0-or-later:
# - src/game/MiniCore/ - "MiniCore" game engine
#
# LGPL-3.0-or-later:
# - src/game/MiniCore/src/Core/mcvector2d.hh
# - src/game/MiniCore/src/Core/mcvector3d.hh
#
# MIT:
# - src/contrib/Argengine - CLI argument parsing library
# - src/contrib/SimpleLogger - logging library
License: GPL-3.0-or-later AND GPL-2.0-or-later AND LGPL-3.0-or-later AND MIT

Version: 2.1.1
Release: 4%{?dist}

URL: https://juzzlin.github.io/DustRacing2D/
Source0: https://github.com/juzzlin/DustRacing2D/archive/%{version}/DustRacing2D-%{version}.tar.gz
Source6: %{name}-game.6

# Unbundle glew and glm libraries
Patch0: 0000-unbundle-libs.patch

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: hardlink
BuildRequires: libappstream-glib
BuildRequires: pkgconfig

BuildRequires: cmake(OpenAL)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(Qt5OpenGL)
BuildRequires: cmake(Qt5Sql)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5Xml)
BuildRequires: glew-devel
BuildRequires: glm-devel
BuildRequires: pkgconfig(glu)
BuildRequires: pkgconfig(vorbisfile)

%global fontlist font(liberationsans)
BuildRequires: fontconfig
BuildRequires: %{fontlist}

# Version info based on src/contrib/*/CHANGELOG
Provides: bundled(Argengine) = 0.0.1
Provides: bundled(SimpleLogger) = 1.4.0

Requires: %{name}-data = %{version}-%{release}

%description
Dust Racing 2D is a tile-based 2D racing game written with Qt (in C++)
and OpenGL. Dust Racing 2D comes with a Qt-based level editor for level
creation. A separate engine, MiniCore, is used for physics modeling.


%package data
Summary: Data files for Dust Racing 2D
License: CC-BY-SA-3.0
BuildArch: noarch

Requires: hicolor-icon-theme
Requires: %{fontlist}

%description data
This package provides the data files (graphics, sounds, et cetera)
required to play Rust Racing 2D.


%prep
%autosetup -p1 -n DustRacing2D-%{version}

# Remove bundled libs that we want to unbundle
rm -rf src/game/MiniCore/src/Graphics/contrib/


%build
%cmake \
	-DReleaseBuild=1 \
	-DSystemFonts=1 \
	-DDATA_PATH=%{_datadir}/%{name} \
	-DDOC_PATH=%{_docdir}/%{name} \
	-DBUILD_SHARED_LIBS:BOOL=OFF
%cmake_build


%install
%cmake_install

# The game ships some duplicated assets
hardlink --verbose %{buildroot}%{_datadir}/%{name}/

install -m 755 -d %{buildroot}%{_mandir}/man6/
install -m 644 -p %{SOURCE6} %{buildroot}%{_mandir}/man6/%{name}-game.6


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-game.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-editor.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml


%files
%{_bindir}/%{name}-game
%{_bindir}/%{name}-editor
%{_datadir}/applications/%{name}-game.desktop
%{_datadir}/applications/%{name}-editor.desktop
%{_datadir}/metainfo/%{name}.appdata.xml
%{_mandir}/man6/%{name}-game.6*

%files data
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/AUTHORS
%doc %{_docdir}/%{name}/CHANGELOG
%doc %{_docdir}/%{name}/README.md
%license %{_docdir}/%{name}/COPYING
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/%{name}-game.png
%{_datadir}/icons/hicolor/*/apps/%{name}-editor.png


%changelog
* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Sep 12 2025 Artur Frenszek-Iwicki <fedora@svgames.pl> - 2.1.1-3
- De-duplicate files after installing
- Add a man page for the game binary

* Mon Sep 08 2025 Artur Frenszek-Iwicki <fedora@svgames.pl> - 2.1.1-2
- Fix license tag and add Provides for bundled libraries
- Unbundle GLEW and GLM libraries

* Tue Sep 02 2025 Artur Frenszek-Iwicki <fedora@svgames.pl> - 2.1.1-1
- Initial packaging
