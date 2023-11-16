Name:           merkaartor
Version:        0.18.4
Release:        %autorelease
Summary:        Qt-Based OpenStreetMap editor

# GPL-2.0-or-later: main program
# GPL-3.0-or-later: plugins/background/MCadastreFranceBackground/qadastre
# LGPL-3.0-or-later: 
# - src/ImportExport/fileformat.proto
# - src/ImportExport/osmformat.proto
# LGPL-2.1-only WITH Qt-LGPL-exception-1.1 OR GPL-3.0-only: src/QToolBarDialog
License:        GPL-2.0-or-later AND GPL-3.0-or-later AND LGPL-3.0-or-later AND (LGPL-2.1-only WITH Qt-LGPL-exception-1.1 OR GPL-3.0-only)
URL:            http://www.merkaartor.be
VCS:            https://github.com/openstreetmap/merkaartor
Source0:        %vcs/archive/%{version}/%{name}-%{version}.tar.gz
Patch:          merkaartor-0.18.3-no-git-version.patch
# Fix Qt5.15 build
Patch:          merkaartor_qt5.15.patch
# Upstream patch to port to proj >= 6 API, fixes FTBFS with proj >= 8
# https://github.com/openstreetmap/merkaartor/pull/233
Patch:          merkaartor-0.18.4-proj-remove-legacy-api.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5Designer)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5WebKit)
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(gdal)
BuildRequires:  pkgconfig(proj) >= 6.0.0
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  qtsingleapplication-qt5-devel
Requires:       hicolor-icon-theme

%description
Merkaartor is a small editor for OpenStreetMap available under the
GNU General Public License and developed using the Qt toolkit.

It has some unique features like anti-aliased displaying,
transparent display of map features like roads and curved roads.

%prep
%autosetup -p1 -n %{name}-%{version}
# Use packaged qtsingleapplication instead of bundled version
rm -rfv 3rdparty/qtsingleapplication-2.6_1-opensource
sed -i "s|../3rdparty/qtsingleapplication-2.6_1-opensource/src/qtsingleapplication.pri|%{_libdir}/qt5/mkspecs/features/qtsingleapplication.prf|" src/src.pro

%build
lrelease-qt5 src/src.pro
%{qmake_qt5} Merkaartor.pro \
             PREFIX=%{_prefix} \
             LIBDIR=%{_libdir} \
             RELEASE=1 \
             NODEBUG=1 \
             GEOIMAGE=1 \
             GPSD=1 \
             GDAL=1 \
             ZBAR=0
%{make_build}

%install
%{make_install} INSTALL_ROOT=%{buildroot}
%find_lang %{name} --with-qt

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.%{name}.%{name}.desktop

%files -f %{name}.lang
%license LICENSE
%doc AUTHORS CHANGELOG HACKING.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%exclude %{_datadir}/%{name}/translations
%{_datadir}/applications/org.%{name}.%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_libdir}/%{name}/

%changelog
%autochangelog
