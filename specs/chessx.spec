# Fedora 40+ ships with KDE 6, so the Qt6 build is preferred
%if 0%{?fedora} >= 40
%bcond_without qt6
%else
%bcond_with    qt6
%endif

Name:           chessx
Version:        1.6.6
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
Patch002:       https://github.com/Isarhamster/chessx/pull/61.patch#/0002-Fix-install-path-of-icons-on-Linux.patch
Patch003:       https://github.com/Isarhamster/chessx/pull/63.patch#/0003-Allow-linking-against-system-libraries-via-pkg-confi.patch

BuildRequires:  gcc-c++
%if %{with qt6}
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6Multimedia)
BuildRequires:  pkgconfig(quazip1-qt6)
BuildRequires:  qt6-linguist
%else
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(quazip1-qt5)
BuildRequires:  qt5-linguist
%endif
BuildRequires:  pkgconfig(zlib)
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

# Bundles part of scid 1.0 (https://sourceforge.net/projects/scid/)
Provides:       bundled(scid) = 1.0

%description
ChessX is a free and open source chess database application for Linux, Mac OS X
and Windows.


%prep
%autosetup -p1 -n %{name}-master

# Fix up lupdate path
sed -i 's| lupdate | $$[QT_INSTALL_BINS]/lupdate |' chessx.pro

# Ensure bundled quazip code is not used
rm -rf src/quazip

# Remove executable bit from regular files (the tarball is buggy)
chmod -R -x+X .


%build
%if %{with qt6}
%qmake_qt6 \
%else
%qmake_qt5 \
%endif
    -r CONFIG+=link_pkgconfig PREFIX=%{_prefix}
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
