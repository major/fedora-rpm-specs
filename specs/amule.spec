%global forgeurl    https://github.com/amule-org/amule
%global commit      3cfd01faabed0757ba7b506e50f033c9cfd560e7

Name:           amule
Version:        3.0.1
Summary:        File sharing client compatible with eDonkey
License:        GPL-2.0-or-later AND GPL-3.0-or-later WITH Bison-exception-2.2

%forgemeta

Release:        %autorelease
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  wxGTK-devel >= 3.2.0
BuildRequires:  desktop-file-utils
BuildRequires:  boost-devel
BuildRequires:  pkgconfig(libpng)
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(libcryptopp)
BuildRequires:  pkgconfig(libupnp)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(ayatana-appindicator3-0.1)
BuildRequires:  cmake
BuildRequires:  libmaxminddb-devel
BuildRequires:  picojson-static
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  gettext
BuildRequires:  python3

Requires:       hicolor-icon-theme

%description
aMule is an easy to use multi-platform client for ED2K Peer-to-Peer
Network. It is a fork of xMule, which was based on eMule for
Windows. aMule currently supports (but is not limited to) the
following platforms: Linux, *BSD and MacOS X.

%package nogui
Summary:        Components of aMule which don't require a GUI (for servers)
License:        GPL-2.0-or-later AND GPL-3.0-or-later WITH Bison-exception-2.2 AND Apache-2.0 AND MIT
# Browser-side ESM modules for the amuleapi frontend have no directly usable
# Fedora system web assets; retaining these upstream copies avoids a much
# larger offline npm build dependency set. Versions and licenses are explicit.
Provides:       bundled(nodejs-htm) = 3.1.1
Provides:       bundled(nodejs-preact) = 10.29.2
%description nogui
This package contains the aMule components which don't require a GUI.
It is useful for servers which don't have Xorg.

%prep
%forgesetup

# Fedora provides picojson as a header-only system library. Ensure the
# compiler cannot select the bundled copy and use the system header instead.
sed -i 's/#include "picojson\.h"/#include <picojson.h>/' \
    src/libwebcommon/Jwt.cpp \
    src/webapi/Api.cpp
rm -f src/libwebcommon/picojson.h

%build
%cmake \
    -DBUILD_MONOLITHIC=YES \
    -DBUILD_DAEMON=YES \
    -DBUILD_WEBSERVER=NO \
    -DBUILD_AMULEAPI=YES \
    -DBUILD_AMULECMD=YES \
    -DBUILD_ALCC=YES \
    -DBUILD_BFD=NO \
    -DBUILD_VERSION_CHECK=NO \
    -DBUILD_ED2K=YES \
    -DENABLE_NLS=YES \
    -DENABLE_IP2COUNTRY=YES

%cmake_build

%install
%cmake_install
%find_lang %{name}

# CMake installs the project license alongside the regular documentation.
# Keep the canonical RPM %%license copy and avoid packaging it again as %%doc.
rm -f %{buildroot}%{_docdir}/%{name}/LICENSE.md

%check
desktop-file-validate \
    %{buildroot}%{_datadir}/applications/org.amule.aMule.desktop

appstream-util validate-relax --nonet \
    %{buildroot}%{_metainfodir}/org.amule.aMule.metainfo.xml

%files -f %{name}.lang
%license LICENSE.md
%doc %{_docdir}/%{name}
%{_bindir}/amule
%{_datadir}/applications/org.amule.aMule.desktop
%{_datadir}/metainfo/org.amule.aMule.metainfo.xml
%{_datadir}/pixmaps/org.amule.aMule.png
%{_datadir}/icons/hicolor/128x128/apps/org.amule.aMule.png
%{_datadir}/icons/hicolor/256x256/apps/org.amule.aMule.png
%{_mandir}/man1/amule.1.*
%dir %{_datadir}/amule
%{_datadir}/amule/skins

%files nogui
%license LICENSE.md
%dir %{_datadir}/amule
%{_bindir}/alcc
%{_bindir}/amulecmd
%{_bindir}/amuled
%{_bindir}/ed2k
%{_bindir}/amuleapi
%dir %{_datadir}/amule/amuleapi-static
%{_datadir}/amule/amuleapi-static/css
%{_datadir}/amule/amuleapi-static/i18n
%{_datadir}/amule/amuleapi-static/img
%{_datadir}/amule/amuleapi-static/index.html
%dir %{_datadir}/amule/amuleapi-static/js
%{_datadir}/amule/amuleapi-static/js/*.js
%dir %{_datadir}/amule/amuleapi-static/js/vendor
%{_datadir}/amule/amuleapi-static/js/vendor/*.js
%license %{_datadir}/amule/amuleapi-static/js/vendor/htm.LICENSE
%license %{_datadir}/amule/amuleapi-static/js/vendor/preact.LICENSE
%{_datadir}/amule/amuleapi-static/js/views

%{_mandir}/man1/alcc.1.*
%{_mandir}/man1/amulecmd.1.*
%{_mandir}/man1/amuled.1.*
%{_mandir}/man1/ed2k.1.*
%{_mandir}/man1/amuleapi.1.*

%changelog
%autochangelog
