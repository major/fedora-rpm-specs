%global rdnn    com.raggesilver.BlackBox

%global commit      bb1ce17d374bb339eca2c0200744012feef44c53
%global shortcommit %{sub %{commit} 1 7}

Name:           blackbox-terminal
Version:        0.15.0~^2.%{shortcommit}
Release:        %autorelease
Summary:        Elegant and customizable terminal for GNOME
# Entire source code is GPL-3.0-or-later except src/utils/Terminal.vala which
# is GPL-3.0-or-later AND (MIT OR Apache-2.0) AND MPL-2.0.
License:        GPL-3.0-or-later AND (MIT OR Apache-2.0) AND MPL-2.0
URL:            https://gitlab.gnome.org/raggesilver/blackbox
Source:         %{url}/-/archive/%{commit}/blackbox-%{shortcommit}.tar.gz
# https://gitlab.gnome.org/raggesilver/blackbox/-/merge_requests/122
Patch:          0001-Rename-executable-to-blackbox-terminal.patch
# https://gitlab.gnome.org/raggesilver/blackbox/-/merge_requests/126
Patch:          0002-Remove-duplicate-icons.patch

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  vala
BuildRequires:  gettext
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(pqmarble)
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
%autosetup -p 1 -n blackbox-%{commit}


%build
%meson -Dblackbox_is_flatpak=%{?flatpak:true}%{!?flatpak:false}
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
%if %{defined flatpak}
%{_bindir}/terminal-toolbox
%endif
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
