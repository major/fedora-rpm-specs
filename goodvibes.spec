Name:           goodvibes
Version:        0.7.6
Release:        %autorelease
Summary:        Lightweight Radio Player

License:        GPL-3.0-or-later
URL:            https://goodvibes.readthedocs.io/en/stable/index.html
Source0:        https://gitlab.com/%{name}/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(amtk-5)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(keybinder-3.0)
BuildRequires:  pkgconfig(libsoup-2.4)
Requires:       dconf
Requires:       gstreamer1-plugins-ugly-free
Requires:       hicolor-icon-theme

%description
Goodvibes is an Internet radio player for GNU/Linux. It aims to be light,
simple, straightforward.

%prep
%autosetup -n %{name}-v%{version}

%build
export CFLAGS="%build_cflags -fPIE"
%meson -Dc_args="%build_cflags -fPIE"
%meson_build

%install
%meson_install
%find_lang %{name}

%check
appstream-util validate-relax --nonet \
        %{buildroot}%{_metainfodir}/*.appdata.xml
desktop-file-validate \
        %{buildroot}/%{_datadir}/applications/*.desktop
%meson_test

%files -f %{name}.lang
%license COPYING
%doc HACKING.md NEWS README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-client
%{_datadir}/applications/io.gitlab.Goodvibes.desktop
%{_datadir}/dbus-1/services/io.gitlab.Goodvibes.service
%{_datadir}/glib-2.0/schemas/io.gitlab.Goodvibes.enums.xml
%{_datadir}/glib-2.0/schemas/io.gitlab.Goodvibes.gschema.xml
%{_datadir}/icons/hicolor/*/apps/io.gitlab.Goodvibes.png
%{_datadir}/icons/hicolor/symbolic/apps/io.gitlab.Goodvibes-symbolic.svg
%{_mandir}/man1/%{name}-client.1.*
%{_mandir}/man1/%{name}.1.*
%{_metainfodir}/io.gitlab.Goodvibes.appdata.xml

%changelog
%autochangelog
