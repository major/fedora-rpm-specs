%global tarball_version %%(echo %{version} | tr '~' '.')

%global __provides_exclude_from ^%{_libdir}/eog/plugins/.*\\.so$

Name:           eog-plugins
Version:        44.1
Release:        %autorelease
Summary:        A collection of plugins for the eog image viewer

License:        GPL-2.0-or-later AND CC0-1.0
URL:            https://wiki.gnome.org/Apps/EyeOfGnome/Plugins
Source0:        https://download.gnome.org/sources/%{name}/44/%{name}-%{tarball_version}.tar.xz

Patch0:         eog-plugins-disable-postasa-plugin-by-default.patch

BuildRequires:  gcc
BuildRequires:  pkgconfig(champlain-gtk-0.12)
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(eog)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libpeas-1.0)
BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  python3-devel

Requires:       eog-plugin-exif-display%{?_isa} = %{version}-%{release}
Requires:       eog-plugin-export-to-folder%{?_isa} = %{version}-%{release}
Requires:       eog-plugin-fit-to-width%{?_isa} = %{version}-%{release}
Requires:       eog-plugin-fullscreenbg%{?_isa} = %{version}-%{release}
Requires:       eog-plugin-light-theme%{?_isa} = %{version}-%{release}
Requires:       eog-plugin-map%{?_isa} = %{version}-%{release}
Requires:       eog-plugin-maximize-windows%{?_isa} = %{version}-%{release}
Requires:       eog-plugin-pythonconsole%{?_isa} = %{version}-%{release}
Requires:       eog-plugin-send-by-mail%{?_isa} = %{version}-%{release}
Requires:       eog-plugin-slideshowshuffle%{?_isa} = %{version}-%{release}

Obsoletes:      eog-plugin-postasa < %{version}-%{release}

%description
It's a collection of plugins for use with the Eye of GNOME Image Viewer.
The included plugins provide a map view for where the picture was taken,
display of Exif information, Zoom to fit, etc.

%package        data
Summary:        Common data required by plugins
BuildArch:      noarch
Requires:       eog
# Plugin removed in 42.alpha. No suitable replacement.
# https://gitlab.gnome.org/GNOME/eog-plugins/-/merge_requests/5
Obsoletes:      eog-plugin-hide-titlebar < 42~alpha-1

%description    data
Common files required by all plugins.

%package -n     eog-plugin-exif-display
Summary:        eog exif-display plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       eog%{?_isa}

%description -n eog-plugin-exif-display
The eog exif-display plugin.

%package -n     eog-plugin-export-to-folder
Summary:        eog export-to-folder plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       eog%{?_isa}
Requires:       libpeas-loader-python3%{?_isa}

%description -n eog-plugin-export-to-folder
The eog export-to-folder plugin.

%package -n     eog-plugin-fit-to-width
Summary:        eog fit-to-width plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       eog%{?_isa}

%description -n eog-plugin-fit-to-width
The eog fit-to-width plugin.

%package -n     eog-plugin-fullscreenbg
Summary:        eog fullscreenbg plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       eog%{?_isa}
Requires:       libpeas-loader-python3%{?_isa}

%description -n eog-plugin-fullscreenbg
The eog fullscreenbg plugin.

%package -n     eog-plugin-light-theme
Summary:        eog light-theme plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       eog%{?_isa}

%description -n eog-plugin-light-theme
The eog light-theme plugin.

%package -n     eog-plugin-map
Summary:        eog map plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       eog%{?_isa}

%description -n eog-plugin-map
The eog map plugin.

%package -n     eog-plugin-maximize-windows
Summary:        eog maximize-windows plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       eog%{?_isa}
Requires:       libpeas-loader-python3%{?_isa}

%description -n eog-plugin-maximize-windows
The eog maximize-windows plugin.

%package -n     eog-plugin-pythonconsole
Summary:        eog pythonconsole plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       eog%{?_isa}
Requires:       libpeas-loader-python3%{?_isa}

%description -n eog-plugin-pythonconsole
The eog pythonconsole plugin.

%package -n     eog-plugin-send-by-mail
Summary:        eog send-by-mail plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       eog%{?_isa}

%description -n eog-plugin-send-by-mail
The eog send-by-mail plugin.

%package -n     eog-plugin-slideshowshuffle
Summary:        eog slideshowshuffle plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       eog%{?_isa}
Requires:       libpeas-loader-python3%{?_isa}

%description -n eog-plugin-slideshowshuffle
The eog slideshowshuffle plugin.

%prep
%autosetup -p1 -n %{name}-%{tarball_version}

%build
%meson
%meson_build

%install
%meson_install

%py_byte_compile %{__python3} %{buildroot}%{_libdir}/eog/plugins/

%find_lang %{name}

%files

%files data -f eog-plugins.lang
%license COPYING
%doc NEWS

%files -n eog-plugin-exif-display
%{_libdir}/eog/plugins/exif-display.plugin
%{_libdir}/eog/plugins/libexif-display.so
%{_metainfodir}/eog-exif-display.appdata.xml
%{_datadir}/glib-2.0/schemas/org.gnome.eog.plugins.exif-display.gschema.xml

%files -n eog-plugin-export-to-folder
%dir %{_libdir}/eog/plugins/__pycache__/
%{_libdir}/eog/plugins/__pycache__/export-to-folder.*.pyc
%{_libdir}/eog/plugins/export-to-folder.plugin
%{_libdir}/eog/plugins/export-to-folder.py
%{_metainfodir}/eog-export-to-folder.appdata.xml
%{_datadir}/eog/plugins/export-to-folder/
%{_datadir}/glib-2.0/schemas/org.gnome.eog.plugins.export-to-folder.gschema.xml

%files -n eog-plugin-fit-to-width
%{_libdir}/eog/plugins/fit-to-width.plugin
%{_libdir}/eog/plugins/libfit-to-width.so
%{_metainfodir}/eog-fit-to-width.appdata.xml

%files -n eog-plugin-fullscreenbg
%dir %{_libdir}/eog/plugins/__pycache__/
%{_libdir}/eog/plugins/__pycache__/fullscreenbg.*.pyc
%{_libdir}/eog/plugins/fullscreenbg.plugin
%{_libdir}/eog/plugins/fullscreenbg.py
%{_metainfodir}/eog-fullscreenbg.appdata.xml
%{_datadir}/eog/plugins/fullscreenbg/
%{_datadir}/glib-2.0/schemas/org.gnome.eog.plugins.fullscreenbg.gschema.xml

%files -n eog-plugin-light-theme
%{_libdir}/eog/plugins/liblight-theme.so
%{_libdir}/eog/plugins/light-theme.plugin
%{_metainfodir}/eog-light-theme.appdata.xml

%files -n eog-plugin-map
%{_libdir}/eog/plugins/libmap.so
%{_libdir}/eog/plugins/map.plugin
%{_metainfodir}/eog-map.appdata.xml

%files -n eog-plugin-maximize-windows
%dir %{_libdir}/eog/plugins/__pycache__/
%{_libdir}/eog/plugins/__pycache__/maximize-windows.*.pyc
%{_libdir}/eog/plugins/maximize-windows.py
%{_libdir}/eog/plugins/maximize-windows.plugin
%{_metainfodir}/eog-maximize-windows.appdata.xml

%files -n eog-plugin-pythonconsole
%{_libdir}/eog/plugins/pythonconsole.plugin
%{_libdir}/eog/plugins/pythonconsole/
%{_metainfodir}/eog-pythonconsole.appdata.xml
%{_datadir}/eog/plugins/pythonconsole/
%{_datadir}/glib-2.0/schemas/org.gnome.eog.plugins.pythonconsole.gschema.xml

%files -n eog-plugin-send-by-mail
%{_libdir}/eog/plugins/send-by-mail.plugin
%{_libdir}/eog/plugins/libsend-by-mail.so
%{_metainfodir}/eog-send-by-mail.appdata.xml

%files -n eog-plugin-slideshowshuffle
%dir %{_libdir}/eog/plugins/__pycache__/
%{_libdir}/eog/plugins/__pycache__/slideshowshuffle.*.pyc
%{_libdir}/eog/plugins/slideshowshuffle.plugin
%{_libdir}/eog/plugins/slideshowshuffle.py
%{_metainfodir}/eog-slideshowshuffle.appdata.xml

%changelog
%autochangelog
