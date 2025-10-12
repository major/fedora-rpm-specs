# Filter provides for plugin .so files
%global __provides_exclude_from ^%{_libdir}/gedit/plugins/

%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           gedit-plugins
Version:        48.2
Release:        %autorelease
Summary:        Plugins for gedit

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://gedit-text-editor.org/
Source:         https://gitlab.gnome.org/World/gedit/%{name}/-/archive/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  yelp-tools
BuildRequires:  (pkgconfig(gedit) >= 48.2 and pkgconfig(gedit) < 49)
BuildRequires:  pkgconfig(libpeas-1.0)

# this is a metapackage dragging in all the plugins
Requires:       gedit-plugin-bookmarks
Requires:       gedit-plugin-drawspaces
Requires:       gedit-plugin-smartspaces
Requires:       gedit-plugin-wordcompletion

%description
A collection of plugins for gedit.

%package data
Summary:        Common data required by plugins
Requires:       gedit
%description data
Common files required by all plugins.

%package -n     gedit-plugin-bookmarks
Summary:        gedit bookmarks plugin
Requires:       %{name}-data = %{version}-%{release}
%description -n gedit-plugin-bookmarks
The gedit bookmarks plugin.

%package -n     gedit-plugin-drawspaces
Summary:        gedit drawspaces plugin
Requires:       %{name}-data = %{version}-%{release}
%description -n gedit-plugin-drawspaces
The gedit drawspaces plugin.

%package -n     gedit-plugin-smartspaces
Summary:        gedit smartspaces plugin
Requires:       %{name}-data = %{version}-%{release}
%description -n gedit-plugin-smartspaces
The gedit smartspaces plugin.

%package -n     gedit-plugin-wordcompletion
Summary:        gedit wordcompletion plugin
Requires:       %{name}-data = %{version}-%{release}
%description -n gedit-plugin-wordcompletion
The gedit wordcompletion plugin.

%prep
%autosetup -p1 -n %{name}-%{tarball_version}

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome
%find_lang gedit --with-gnome

# Empty files section for the metapackage to make sure it's created
%files

%files data -f %{name}.lang -f gedit.lang
%license COPYING
%doc README.md NEWS
%dir %{_libdir}/gedit/plugins/

%files -n gedit-plugin-bookmarks
%{_libdir}/gedit/plugins/bookmarks.plugin
%{_libdir}/gedit/plugins/libbookmarks.so
%{_metainfodir}/gedit-bookmarks.metainfo.xml

%files -n gedit-plugin-drawspaces
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.drawspaces.gschema.xml
%{_libdir}/gedit/plugins/drawspaces.plugin
%{_libdir}/gedit/plugins/libdrawspaces.so
%{_metainfodir}/gedit-drawspaces.metainfo.xml

%files -n gedit-plugin-smartspaces
%{_libdir}/gedit/plugins/libsmartspaces.so
%{_libdir}/gedit/plugins/smartspaces.plugin
%{_metainfodir}/gedit-smartspaces.metainfo.xml

%files -n gedit-plugin-wordcompletion
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.wordcompletion.gschema.xml
%{_libdir}/gedit/plugins/libwordcompletion.so
%{_libdir}/gedit/plugins/wordcompletion.plugin
%{_metainfodir}/gedit-wordcompletion.metainfo.xml

%changelog
%autochangelog
