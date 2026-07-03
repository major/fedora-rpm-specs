%global rdnn    com.raggesilver.BlackBox

Name:           blackbox-terminal
Version:        0.15.2
Release:        %autorelease
Summary:        Elegant and customizable terminal for GNOME
License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/raggesilver/blackbox
Source:         %{url}/-/archive/v%{version}/blackbox-v%{version}.tar.gz

# https://gitlab.gnome.org/raggesilver/blackbox/-/work_items/424
# https://gitlab.gnome.org/raggesilver/blackbox/-/commit/7182d6da8ddbd925db001b30ed6b3b00927dd7f5
Patch:          0001-Implement-last-known-cwd.patch

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


%package nautilus
Summary:        Black Box extension for Nautilus
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       nautilus-python%{?_isa}


%description nautilus
This package provides a Nautilus extension that adds the 'Open in Black Box'
option to the right-click context menu in Nautilus.


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


%files nautilus
%{_datadir}/nautilus-python/extensions/open-blackbox.py


%changelog
%autochangelog
