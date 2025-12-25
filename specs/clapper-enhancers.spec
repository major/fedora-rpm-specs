%global _clapperenhdir %{_libdir}/clapper-0.0/enhancers

Name:           clapper-enhancers
Version:        0.10.0
Release:        %autorelease
Summary:        Plugins enhancing Clapper library capabilities

License:        LGPL-2.1-or-later
URL:            https://github.com/Rafostar/clapper-enhancers
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(clapper-0.0) >= 0.9.0
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-tag-1.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libpeas-2)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  python3-devel
Requires:       clapper%{_isa} >= 0.9.0
# required by yt-dlp enhancer (segfaults in libpeas.so otherwise)
Requires:       libpeas-loader-python%{_isa}
Requires:       python3dist(yt-dlp)

%description
This package contains the following plugins enhancing Clapper capabilities:

* control-hub
* lbry (odysee.com)
* media-scanner
* mpris
* parser-m3u
* peertube
* recall
* utils
* yt-dlp

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%py_byte_compile %{python3} %{buildroot}%{_clapperenhdir}/yt-dlp

%files
%license LICENSE
%dir %{_clapperenhdir}
%dir %{_clapperenhdir}/control-hub
%{_clapperenhdir}/control-hub/clapper-control-hub.gschema.xml
%{_clapperenhdir}/control-hub/clapper-control-hub.plugin
%{_clapperenhdir}/control-hub/gschemas.compiled
%{_clapperenhdir}/control-hub/libclapper-control-hub.so
%dir %{_clapperenhdir}/lbry
%{_clapperenhdir}/lbry/clapper-lbry.plugin
%{_clapperenhdir}/lbry/libclapper-lbry.so
%dir %{_clapperenhdir}/media-scanner
%{_clapperenhdir}/media-scanner/clapper-media-scanner.plugin
%{_clapperenhdir}/media-scanner/libclapper-media-scanner.so
%dir %{_clapperenhdir}/mpris
%{_clapperenhdir}/mpris/clapper-mpris.plugin
%{_clapperenhdir}/mpris/libclapper-mpris.so
%dir %{_clapperenhdir}/parser-m3u
%{_clapperenhdir}/parser-m3u/clapper-parser-m3u.plugin
%{_clapperenhdir}/parser-m3u/libclapper-parser-m3u.so
%dir %{_clapperenhdir}/peertube
%{_clapperenhdir}/peertube/clapper-peertube.plugin
%{_clapperenhdir}/peertube/libclapper-peertube.so
%dir %{_clapperenhdir}/recall
%{_clapperenhdir}/recall/clapper-recall.gschema.xml
%{_clapperenhdir}/recall/clapper-recall.plugin
%{_clapperenhdir}/recall/gschemas.compiled
%{_clapperenhdir}/recall/libclapper-recall.so
%dir %{_clapperenhdir}/yt-dlp
%dir %{_clapperenhdir}/yt-dlp/__pycache__
%{_clapperenhdir}/yt-dlp/clapper_yt_dlp.plugin
%pycached %{_clapperenhdir}/yt-dlp/clapper_yt_dlp.py
%pycached %{_clapperenhdir}/yt-dlp/clapper_yt_dlp_dash.py
%pycached %{_clapperenhdir}/yt-dlp/clapper_yt_dlp_debug.py
%pycached %{_clapperenhdir}/yt-dlp/clapper_yt_dlp_direct.py
%pycached %{_clapperenhdir}/yt-dlp/clapper_yt_dlp_hls.py
%pycached %{_clapperenhdir}/yt-dlp/clapper_yt_dlp_overrides.py
%pycached %{_clapperenhdir}/yt-dlp/clapper_yt_dlp_playlist.py
%pycached %{_clapperenhdir}/yt-dlp/clapper_yt_dlp_utils.py

%changelog
%autochangelog
