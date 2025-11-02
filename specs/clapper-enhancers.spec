%global _clapperenhdir %{_libdir}/clapper-0.0/enhancers

Name:           clapper-enhancers
Version:        0.8.3
Release:        %autorelease
Summary:        Plugins enhancing Clapper library capabilities

License:        LGPL-2.1-or-later
URL:            https://github.com/Rafostar/clapper-enhancers
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(clapper-0.0)
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
# required by yt-dlp enhancer (segfaults in libpeas.so otherwise)
Requires:       libpeas-loader-python%{_isa}
Requires:       python3dist(yt-dlp)

%description
This package contains the following plugins enhancing Clapper capabilities:
* lbry (odysee.com)
* peertube
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
%dir %{_clapperenhdir}/lbry
%{_clapperenhdir}/lbry/clapper-lbry.plugin
%{_clapperenhdir}/lbry/libclapper-lbry.so
%dir %{_clapperenhdir}/peertube
%{_clapperenhdir}/peertube/clapper-peertube.plugin
%{_clapperenhdir}/peertube/libclapper-peertube.so
%dir %{_clapperenhdir}/yt-dlp
%dir %{_clapperenhdir}/yt-dlp/__pycache__
%{_clapperenhdir}/yt-dlp/clapper_yt_dlp.plugin
%pycached %{_clapperenhdir}/yt-dlp/clapper_yt_dlp.py
%pycached %{_clapperenhdir}/yt-dlp/clapper_yt_dlp_dash.py
%pycached %{_clapperenhdir}/yt-dlp/clapper_yt_dlp_direct.py
%pycached %{_clapperenhdir}/yt-dlp/clapper_yt_dlp_hls.py
%pycached %{_clapperenhdir}/yt-dlp/clapper_yt_dlp_overrides.py

%changelog
%autochangelog
