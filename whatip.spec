%global app_id  org.gabmus.whatip

Name:           whatip
Version:        1.1
Release:        %autorelease
Summary:        Info on your IP address
License:        GPL-3.0-or-newer
URL:            https://gitlab.gnome.org/GabMus/whatip
Source0:        %{url}/-/archive/%{version}/whatip-%{version}.tar.bz2

BuildRequires:  meson
BuildRequires:  blueprint-compiler
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  python3-devel
Requires:       gtk4
Requires:       libadwaita
Requires:       iproute
Requires:       iputils
Requires:       python3-gobject
Requires:       python3-netaddr
Requires:       python3-requests
Requires:       hicolor-icon-theme

BuildArch:      noarch

# blueprint-compiler does not work on s390x:
# https://gitlab.gnome.org/jwestman/blueprint-compiler/-/issues/96
ExcludeArch:    s390x

%description
What IP displays information on your local network, IP addresses and open ports.

%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

desktop-file-validate %{buildroot}%{_datadir}/applications/%{app_id}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{app_id}.appdata.xml

%find_lang %{name}


%files -f %{name}.lang
%license LICENSE
%doc README.md
%{_bindir}/whatip
%{python3_sitelib}/%{name}/
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/dbus-1/services/%{app_id}.service
%{_datadir}/glib-2.0/schemas/%{app_id}.gschema.xml
%{_datadir}/icons/hicolor/*/*/%{app_id}*
%{_metainfodir}/%{app_id}.appdata.xml
%{_datadir}/%{name}/


%changelog
%autochangelog
