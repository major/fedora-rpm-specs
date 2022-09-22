Name:           chessx
Version:        1.5.6
Release:        8%{?dist}
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
License:        GPLv2 and GPLv3
URL:            https://sourceforge.net/projects/chessx/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tgz

# https://github.com/Isarhamster/chessx/commit/975db069e4e6834a52cc75fbb402ca3c2c87f200
Patch001:       001-qmake-install-support-for-linux-bsd.patch
# https://github.com/Isarhamster/chessx/commit/c26ab900b525c5bce794734b2852bc445c2753d7
Patch002:       002-add-metainfo-file.patch
# https://github.com/Isarhamster/chessx/pull/61
Patch003:       003-fix-icons-installation.patch
# (downstream patch)
Patch004:       004-wayland-workaround.patch
# https://github.com/Isarhamster/chessx/pull/63
Patch005:       005-use-pkg-config.patch

# Requires Qt >= 5.7 as per INSTALL
%global min_qt_version 5.7.0

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
%license COPYING
%{_bindir}/chessx
%{_datadir}/applications/chessx.desktop
%{_datadir}/icons/hicolor/128x128/apps/chessx.png
%{_datadir}/icons/hicolor/64x64/apps/chessx.png
%{_datadir}/icons/hicolor/32x32/apps/chessx.png
%{_metainfodir}/io.sourceforge.ChessX.metainfo.xml


%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Apr 18 2022 Miro Hrončok <mhroncok@redhat.com> - 1.5.6-7
- Rebuilt for quazip 1.3

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 28 2021 Ondrej Mosnacek <omosnace@redhat.com> - 1.5.6-5
- Unbundle the quazip library

* Mon Jul 26 2021 Ondrej Mosnacek <omosnace@redhat.com> - 1.5.6-4
- Work around Wayland issue

* Wed Jul 07 2021 Ondrej Mosnacek <omosnace@redhat.com> - 1.5.6-3
- Install metadata and icons from upstream

* Sun Jun 13 2021 Ondrej Mosnacek <omosnace@redhat.com> - 1.5.6-2
- Add a desktop file and icon

* Sun Jun 06 2021 Ondrej Mosnacek <omosnace@redhat.com> - 1.5.6-1
- Update to version 1.5.6

* Sun Apr 19 2020 Ondrej Mosnacek <omosnace@redhat.com> - 1.5.0-1
- Initial version
