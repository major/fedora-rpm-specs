Name:           chessx
Version:        1.5.8
Release:        %autorelease
Summary:        Chess Database and PGN viewer

# Various parts of code are annotated with different licenses:
# - GNU General Public License (dep/scid/code/src/*)
# - GNU General Public License v2.0 or later (src/*)
# - GNU General Public License, Version 2 (COPYING and License.txt)
# - GNU General Public License, Version 3 (src/gui/messagedialog.cpp)
# - GNU Lesser General Public License, Version 2.1 (src/gui/qled.*)
# - Expat License (dep/scid/code/src/bytebuf.h)
# - BSD 3-clause "New" or "Revised" License (src/database/downloadmanager.*)
# - LGPL (v2.1 or v3) (src/gui/textedit.*)
# In the License field below only the minimal effective license set is
# documented.
License:        GPL-2.0-only AND GPL-3.0-only
URL:            https://sourceforge.net/projects/chessx/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tgz

# (downstream patch)
Patch001:       0001-Work-around-Qt-Wayland-integration-issue.patch
# https://github.com/Isarhamster/chessx/pull/61
Patch002:       0002-Fix-install-path-of-icons-on-Linux.patch
# https://github.com/Isarhamster/chessx/pull/63
Patch003:       0003-Allow-linking-against-system-libraries-via-pkg-confi.patch

# Requires Qt >= 5.14.1 as per INSTALL.md
%global min_qt_version 5.14.1

BuildRequires:  gcc-c++
BuildRequires:  qt5-qtbase-devel >= %{min_qt_version}
BuildRequires:  qt5-linguist >= %{min_qt_version}
BuildRequires:  pkgconfig(Qt5Svg) >= %{min_qt_version}
BuildRequires:  pkgconfig(Qt5Multimedia) >= %{min_qt_version}
BuildRequires:  pkgconfig(quazip1-qt5)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

# Bundles part of scid 1.0 (https://sourceforge.net/projects/scid/)
Provides:       bundled(scid) = 1.0

%description
ChessX is a free and open source chess database application for Linux, Mac OS X
and Windows.


%prep
%autosetup -p1 -n %{name}-%{version}

# Ensure bundled quazip code is not used
rm -rf src/quazip

# Remove executable bit from regular files (the tarball is buggy)
chmod -R -x+X .


%build
%qmake_qt5 -r CONFIG+=link_pkgconfig
%make_build


%install
%make_install INSTALL_ROOT=%{buildroot}


%check
# Make sure the .metainfo.xml file passes validation
appstream-util validate-relax --nonet \
    %{buildroot}%{_metainfodir}/io.sourceforge.ChessX.metainfo.xml


%files
%license COPYING.md
%doc README.md ChangeLog.md
%{_bindir}/chessx
%{_datadir}/applications/chessx.desktop
%{_datadir}/icons/hicolor/256x256/apps/chessx.png
%{_datadir}/icons/hicolor/64x64/apps/chessx.png
%{_datadir}/icons/hicolor/32x32/apps/chessx.png
%{_metainfodir}/io.sourceforge.ChessX.metainfo.xml


%changelog
%autochangelog
