%global rdnn    com.raggesilver.BlackBox

Name:           blackbox-terminal
Version:        0.15.1
Release:        %autorelease
Summary:        Elegant and customizable terminal for GNOME
License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/raggesilver/blackbox
Source:         %{url}/-/archive/v%{version}/blackbox-v%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  vala
BuildRequires:  gettext
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(vte-2.91-gtk4)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(graphene-gobject-1.0)
# for desktop-file-validate command
BuildRequires:  desktop-file-utils
# for appstream-util command
BuildRequires:  libappstream-glib

Requires:       hicolor-icon-theme


%description
Black Box is an elegant and customizable terminal for GNOME.


%prep
%autosetup -p 1 -n blackbox-v%{version}


%build
%meson
%meson_build


%install
%meson_install
%find_lang blackbox


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{rdnn}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{rdnn}.metainfo.xml


%files -f blackbox.lang
%license COPYING
%doc README.md CHANGELOG.md
%{_bindir}/blackbox-terminal
%{_datadir}/applications/%{rdnn}.desktop
%{_datadir}/blackbox
%{_datadir}/glib-2.0/schemas/%{rdnn}.gschema.xml
%{_datadir}/icons/hicolor/scalable/actions/%{rdnn}-fullscreen-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/%{rdnn}-show-headerbar-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/external-link-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/settings-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/%{rdnn}.svg
%{_metainfodir}/%{rdnn}.metainfo.xml


%changelog
%autochangelog
