%global rdnn_name org.gnome.Decibels
%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           decibels
Version:        48.0~alpha
Release:        %autorelease
Summary:        Audio player for the GNOME desktop

# one source file is GPLv2+ the rest are GPLv3
License:        GPL-2.0-or-later and GPL-3.0-only
URL:            https://www.gnome.org
Source0:        https://download.gnome.org/sources/%{name}/48/%{name}-%{tarball_version}.tar.xz

BuildRequires:  meson
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(blueprint-compiler)
BuildRequires:  pkgconfig(gjs-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  (npm(typescript) >= 5.7.3 with npm(typescript) < 5.8)
Requires:       hicolor-icon-theme
# Lacking typelib dependency generator, so use package names instead
Requires:       gtk4
Requires:       libadwaita
Requires:       gstreamer1-plugins-bad-free-libs
# Bundled gi-typescript-defs
Provides:       bundled(gi-typescript-definitions)

# Codecs to make it work
Recommends:     gstreamer1-plugins-good
Recommends:     gstreamer1-plugins-bad-free
Recommends:     gstreamer1-plugins-ugly-free

BuildArch:      noarch

%description
%{summary}.


%prep
%autosetup -n %{name}-%{tarball_version}


%conf
%meson


%build
%meson_build


%install
%meson_install

%find_lang %{rdnn_name}


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{rdnn_name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{rdnn_name}.metainfo.xml


%files -f %{rdnn_name}.lang
%license LICENCE
%doc README*
%{_bindir}/%{rdnn_name}
%{_datadir}/%{rdnn_name}/
%{_datadir}/applications/%{rdnn_name}.desktop
%{_datadir}/icons/hicolor/*/*/%{rdnn_name}*
%{_datadir}/dbus-1/services/%{rdnn_name}.service
%{_metainfodir}/%{rdnn_name}.metainfo.xml


%changelog
%autochangelog
