# Filter provides for plugin .so files
%global __provides_exclude_from ^%{_libdir}/gedit/plugins/

%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           gedit-plugins
Version:        48.1
Release:        %autorelease
Summary:        Plugins for gedit

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://gedit-text-editor.org/
Source0:        https://download.gnome.org/sources/%{name}/48/%{name}-%{tarball_version}.tar.xz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  python3-devel
BuildRequires:  vala
BuildRequires:  yelp-tools
BuildRequires:  (pkgconfig(gedit) >= 48.1 and pkgconfig(gedit) < 49)
BuildRequires:  pkgconfig(libpeas-1.0)

# this is a metapackage dragging in all the plugins
Requires:       gedit-plugin-bookmarks
Requires:       gedit-plugin-bracketcompletion
%if !0%{?rhel}
Requires:       gedit-plugin-charmap
%endif
Requires:       gedit-plugin-codecomment
Requires:       gedit-plugin-colorpicker
Requires:       gedit-plugin-drawspaces
Requires:       gedit-plugin-joinlines
Requires:       gedit-plugin-multiedit
Requires:       gedit-plugin-sessionsaver
Requires:       gedit-plugin-smartspaces
Requires:       gedit-plugin-terminal
Requires:       gedit-plugin-wordcompletion

%description
A collection of plugins for gedit.

%package data
Summary:        Common data required by plugins
Requires:       gedit
Requires:       python3-gobject
%description data
Common files required by all plugins.

%package -n     gedit-plugin-bookmarks
Summary:        gedit bookmarks plugin
Requires:       %{name}-data = %{version}-%{release}
%description -n gedit-plugin-bookmarks
The gedit bookmarks plugin.

%package -n     gedit-plugin-bracketcompletion
Summary:        gedit bracketcompletion plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       libpeas-loader-python3%{?_isa}
%description -n gedit-plugin-bracketcompletion
The gedit bracketcompletion plugin.

%if !0%{?rhel}
%package -n     gedit-plugin-charmap
Summary:        gedit charmap plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       gucharmap-libs
Requires:       libpeas-loader-python3%{?_isa}
%description -n gedit-plugin-charmap
The gedit charmap plugin.
%endif

%package -n     gedit-plugin-codecomment
Summary:        gedit codecomment plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       libpeas-loader-python3%{?_isa}
%description -n gedit-plugin-codecomment
The gedit codecomment plugin.

%package -n     gedit-plugin-colorpicker
Summary:        gedit colorpicker plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       libpeas-loader-python3%{?_isa}
%description -n gedit-plugin-colorpicker
The gedit colorpicker plugin.

%package -n     gedit-plugin-drawspaces
Summary:        gedit drawspaces plugin
Requires:       %{name}-data = %{version}-%{release}
%description -n gedit-plugin-drawspaces
The gedit drawspaces plugin.

%package -n     gedit-plugin-joinlines
Summary:        gedit joinlines plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       libpeas-loader-python3%{?_isa}
%description -n gedit-plugin-joinlines
The gedit joinlines plugin.

%package -n     gedit-plugin-multiedit
Summary:        gedit multiedit plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       libpeas-loader-python3%{?_isa}
%description -n gedit-plugin-multiedit
The gedit multiedit plugin.

%package -n     gedit-plugin-sessionsaver
Summary:        gedit sessionsaver plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       libpeas-loader-python3%{?_isa}
%description -n gedit-plugin-sessionsaver
The gedit sessionsaver plugin.

%package -n     gedit-plugin-smartspaces
Summary:        gedit smartspaces plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       libpeas-loader-python3%{?_isa}
%description -n gedit-plugin-smartspaces
The gedit smartspaces plugin.

%package -n     gedit-plugin-terminal
Summary:        gedit terminal plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       libpeas-loader-python3%{?_isa}
Requires:       vte291
%description -n gedit-plugin-terminal
The gedit terminal plugin.

%package -n     gedit-plugin-wordcompletion
Summary:        gedit wordcompletion plugin
Requires:       %{name}-data = %{version}-%{release}
%description -n gedit-plugin-wordcompletion
The gedit wordcompletion plugin.

%prep
%autosetup -p1 -n %{name}-%{tarball_version}

%build
%meson \
%if 0%{?rhel}
  -Dplugin_charmap=false \
%endif
  %nil
%meson_build

%install
%meson_install

%py_byte_compile %{__python3} %{buildroot}%{_libdir}/gedit/plugins/

%find_lang %{name} --with-gnome
%find_lang gedit --with-gnome

%check
[ -f ${RPM_BUILD_ROOT}%{_libdir}/gedit/plugins/terminal.py ]

# Empty files section for the metapackage to make sure it's created
%files

%files data -f %{name}.lang -f gedit.lang
%license COPYING
%doc README.md NEWS
%dir %{_libdir}/gedit/plugins/
%dir %{_libdir}/gedit/plugins/__pycache__/
%dir %{_datadir}/gedit/plugins/
%{_libdir}/gedit/plugins/gpdefs.*
%{_libdir}/gedit/plugins/__pycache__/gpdefs.*

%files -n gedit-plugin-bookmarks
%{_libdir}/gedit/plugins/bookmarks.plugin
%{_libdir}/gedit/plugins/libbookmarks.so
%{_metainfodir}/gedit-bookmarks.metainfo.xml

%files -n gedit-plugin-bracketcompletion
%{_libdir}/gedit/plugins/bracketcompletion.*
%{_libdir}/gedit/plugins/__pycache__/bracketcompletion.*
%{_metainfodir}/gedit-bracketcompletion.metainfo.xml

%if !0%{?rhel}
%files -n gedit-plugin-charmap
%{_libdir}/gedit/plugins/charmap
%{_libdir}/gedit/plugins/charmap.plugin
%{_metainfodir}/gedit-charmap.metainfo.xml
%endif

%files -n gedit-plugin-codecomment
%{_libdir}/gedit/plugins/codecomment.*
%{_libdir}/gedit/plugins/__pycache__/codecomment.*
%{_metainfodir}/gedit-codecomment.metainfo.xml

%files -n gedit-plugin-colorpicker
%{_libdir}/gedit/plugins/colorpicker.*
%{_libdir}/gedit/plugins/__pycache__/colorpicker.*
%{_metainfodir}/gedit-colorpicker.metainfo.xml

%files -n gedit-plugin-drawspaces
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.drawspaces.gschema.xml
%{_libdir}/gedit/plugins/drawspaces.plugin
%{_libdir}/gedit/plugins/libdrawspaces.so
%{_metainfodir}/gedit-drawspaces.metainfo.xml

%files -n gedit-plugin-joinlines
%{_libdir}/gedit/plugins/joinlines.*
%{_libdir}/gedit/plugins/__pycache__/joinlines.*
%{_metainfodir}/gedit-joinlines.metainfo.xml

%files -n gedit-plugin-multiedit
%{_libdir}/gedit/plugins/multiedit
%{_libdir}/gedit/plugins/multiedit.plugin
%{_metainfodir}/gedit-multiedit.metainfo.xml

%files -n gedit-plugin-sessionsaver
%{_datadir}/gedit/plugins/sessionsaver
%{_libdir}/gedit/plugins/sessionsaver
%{_libdir}/gedit/plugins/sessionsaver.plugin

%files -n gedit-plugin-smartspaces
%{_libdir}/gedit/plugins/libsmartspaces.so
%{_libdir}/gedit/plugins/smartspaces.plugin
%{_metainfodir}/gedit-smartspaces.metainfo.xml

%files -n gedit-plugin-terminal
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.terminal.gschema.xml
%{_libdir}/gedit/plugins/__pycache__/terminal.*
%{_libdir}/gedit/plugins/terminal.*
%{_metainfodir}/gedit-terminal.metainfo.xml

%files -n gedit-plugin-wordcompletion
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.wordcompletion.gschema.xml
%{_libdir}/gedit/plugins/libwordcompletion.so
%{_libdir}/gedit/plugins/wordcompletion.plugin
%{_metainfodir}/gedit-wordcompletion.metainfo.xml

%changelog
%autochangelog
