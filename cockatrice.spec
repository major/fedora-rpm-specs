%global		gittag0			2023-09-14-Release-2.9.0

%define			lang_subpkg() \
%package		langpack-%{1}\
Summary:		%{2} language data for %{name}\
BuildArch:	noarch\
Requires:		%{name} = %{version}-%{release}\
Supplements:	(%{name} = %{version}-%{release} and langpacks-%{1})\
\
%description	langpack-%{1}\
%{2} language data for %{name}.\
\
%files			langpack-%{1}\
%{_datadir}/%{name}/translations/%{name}_%{1}.qm\
%{_datadir}/oracle/translations/oracle_%{1}.qm

Name:		cockatrice
Version:	2.9.0
Release:	%autorelease
Summary:	A cross-platform virtual tabletop software for multi-player card games

# * Public Domain (cockatrice/resources/countries/*.svg)
# * GPLv2+ (most of the code)
# * BSD (cockatrice/src/qt-json/, common/sfmt/, 
# * GPLv2 (oracle/src/zip/)
# * CPL or LGPLv2 (servatrice/src/smtp/)
# # Webclient code (not included?)
# * ASL 2.0 (webclient/js/protobuf.js, webclient/js/long.js,
# webclient/js/bytebuffer.js)
# * MIT (webclient/js/jquery-*.js)
License:	GPLv2 and Public Domain
URL:		https://%{name}.github.io
Source0:	https://github.com/%{name}/%{name}/archive/%{gittag0}.tar.gz
Source1:	cockatrice.appdata.xml
Patch0:		cockatrice-ea9e966330-fix-desktop-entry-files.patch
# Support MacOS 12 & 13. Support Protobuf 23. Deprecate MacOS 11. (#4884)
# https://github.com/Cockatrice/Cockatrice/commit/ee674cb0cfa42875eef1a0a80597840816ad86ea
# Backported to the 2.9.0 release
Patch1:         cockatrice-ee674cb0cf-protobuf-23.patch

BuildRequires:	gcc-c++
BuildRequires:	cmake >= 3.1
BuildRequires:	protobuf-devel
BuildRequires:	qt5-qttools-devel
BuildRequires:	qt5-qtsvg-devel
BuildRequires:	qt5-qtmultimedia-devel
BuildRequires:	zlib-devel
BuildRequires:	sqlite-devel
BuildRequires:	qt5-qtwebsockets-devel
BuildRequires:	libappstream-glib
BuildRequires:	desktop-file-utils
Requires:		wget
Requires:		hicolor-icon-theme
Requires:		%{name}-utils = %{version}-%{release}

%description
Cockatrice is an open-source multi-platform supported program for playing
tabletop card games over a network. The program's server design prevents any
kind of client modifications to gain an unfair advantage in a game.
The client also has a built in single-player mode where you can create decks
without being connected to a server.


%package server
Summary:	Standalone server for Cockatrice
Provides:	servatrice = %{version}-%{release}
Requires:	%{name}-utils = %{version}-%{release}

%description server
Cockatrice is an open-source multi-platform supported program for playing
tabletop card games over a network. The program's server design prevents any
kind of client modifications to gain an unfair advantage in a game.
The client also has a built in single-player mode where you can create decks
without being connected to a server.

This is the standalone server, "servatrice".


%package utils
Summary:	Utilities common to both cockatrice and servatrice

%description utils
Cockatrice is an open-source multi-platform supported program for playing
tabletop card games over a network. The program's server design prevents any
kind of client modifications to gain an unfair advantage in a game.
The client also has a built in single-player mode where you can create decks
without being connected to a server.

This package provides utilities required by both cockatrice and servatrice.


%prep
%setup -q -n Cockatrice-%{gittag0}
%patch -P 0
%patch -P 1 -p1
find . -iname "*.h" -exec chmod a-x "{}" \;
find . -iname "*.cpp" -exec chmod a-x "{}" \;
# The API for Protobuf v4 (23.x) requires at least C++14. When compiled as
# C++17, abseil-cpp (a transitive dependency via the generated bindings)
# requires API users to compile with at least C++17.
sed -r -i 's/(CMAKE_CXX_STANDARD )11\b/\117/' CMakeLists.txt


%build
%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DBUILD_SHARED_LIBS=OFF \
	-DWITH_SERVER=ON

%cmake_build


%check
appstream-util validate-relax --nonet %{SOURCE1}
desktop-file-validate cockatrice/%{name}.desktop
desktop-file-validate servatrice/servatrice.desktop
desktop-file-validate oracle/oracle.desktop


%install
%cmake_install

install -m644 -D %{SOURCE1} %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
rm %{buildroot}%{_datadir}/%{name}/translations/%{name}_en@pirate.qm
rm %{buildroot}%{_datadir}/oracle/translations/oracle_en@pirate.qm


%files
%doc README.md
%license LICENSE
%{_bindir}/{cockatrice,oracle}
%{_datadir}/applications/{cockatrice,oracle}.desktop
%{_datadir}/appdata/*
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/{48x48,scalable}/apps/*
%{_datadir}/oracle
%exclude %{_datadir}/%{name}/translations/%{name}_*.qm
%exclude %{_datadir}/oracle/translations/oracle_*.qm

%lang_subpkg cs Czech
%lang_subpkg de German
%lang_subpkg en_US English
%lang_subpkg es Spanish
%lang_subpkg et Estonian
%lang_subpkg fr French
%lang_subpkg it Italian
%lang_subpkg ja Japanese
%lang_subpkg ko Korean
%lang_subpkg nb Norwegian
%lang_subpkg nl Dutch
%lang_subpkg pl Polish
%lang_subpkg pt Portuguese
%lang_subpkg pt_BR Brazil
%lang_subpkg ru Russian
%lang_subpkg sr Serbian
%lang_subpkg sv Swedish
%lang_subpkg zh-Hans "Chinese (Simplified)"

%files utils
%license LICENSE
%{_bindir}/dbconverter

%files server
%license LICENSE
%{_bindir}/servatrice
%{_datadir}/servatrice
%{_datadir}/applications/servatrice.desktop

%changelog
%autochangelog
