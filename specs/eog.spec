%global gtk3_version 3.24.15
%global glib2_version 2.73.2
%global gnome_desktop_version 2.91.2
%global libexif_version 0.6.14
%global libhandy_version 1.5.0

%global tarball_version %%(echo %%{version} | tr '~' '.')
%global major_version %%(echo %%{tarball_version} | cut -d "." -f 1)

Name:    eog
Version: 50.0
Release: %autorelease
Summary: Eye of GNOME image viewer

License: GPL-2.0-or-later AND CC-BY-SA-3.0 AND CC0-1.0
URL:     https://wiki.gnome.org/Apps/EyeOfGnome
Source0: https://download.gnome.org/sources/%{name}/%{major_version}/%{name}-%{tarball_version}.tar.xz

Patch0:  eog-lower-requires-libpeas-version.patch

BuildRequires: pkgconfig(exempi-2.0)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires: pkgconfig(gnome-desktop-3.0) >= %{gnome_desktop_version}
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(gsettings-desktop-schemas)
BuildRequires: pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires: pkgconfig(lcms2)
BuildRequires: pkgconfig(libexif) >= %{libexif_version}
BuildRequires: pkgconfig(libhandy-1) >= %{libhandy_version}
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(libpeas-1.0) >= 0.7.4
BuildRequires: pkgconfig(libpeas-gtk-1.0) >= 0.7.4
%if 0%{?flatpak}
BuildRequires: pkgconfig(libportal-gtk3)
%endif
BuildRequires: pkgconfig(librsvg-2.0)
BuildRequires: pkgconfig(shared-mime-info)
BuildRequires: pkgconfig(x11)
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: gi-docgen
BuildRequires: itstool
BuildRequires: meson
BuildRequires: zlib-devel
BuildRequires: /usr/bin/appstream-util

Requires:      gsettings-desktop-schemas
Requires:      glib2%{?_isa} >= %{glib2_version}
Requires:      gtk3%{?_isa} >= %{gtk3_version}
Requires:      libhandy%{?_isa} >= %{libhandy_version}

# Contains some files from the Independent JPEG Group's implementation of the
# libjpeg library. They are the parts that are used by the jpegtran tool, which
# are unfortunately not provided as part of libjpeg's API. They neither parse
# files (or Exif data) nor allocate memory by themselves. They only work on
# the data and functions provided by libjpeg.
Provides:      bundled(libjpeg)

%description
The Eye of GNOME image viewer (eog) is the official image viewer for the
GNOME desktop. It can view single image files in a variety of formats, as
well as large image collections.

eog is extensible through a plugin system.

%package devel
Summary: Support for developing plugins for the eog image viewer
Requires: %{name}%{?_isa} = %{version}-%{release}
# Because web fonts from upstream are not bundled in the gi-docgen package,
# packages containing documentation generated with gi-docgen should depend on
# this metapackage to ensure the proper system fonts are present.
Recommends: gi-docgen-fonts

%description devel
The Eye of GNOME image viewer (eog) is the official image viewer for the
GNOME desktop. This package allows you to develop plugins that add new
functionality to eog.

%if !0%{?rhel}
%package  tests
Summary:  Tests for the %{name} package
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: python3-behave
Requires: python3-dogtail

%description tests
The %{name}-tests package contains tests that can be used to verify
the functionality of the installed %{name} package.
%endif

%prep
# check for human errors
if [ `echo "%{version}" | grep -cE "\.alpha|\.beta|\.rc"` = "1" ]; then echo "Error: Use tilde in Version field in front of alpha/beta/rc; checked '%{version}'" 1>&2; exit 1; fi

%autosetup -p1 -n %{name}-%{tarball_version}

%build
%meson \
       -Dgtk_doc=true \
    %if 0%{?rhel}
       -Dinstalled_tests=false \
    %else
       -Dinstalled_tests=true \
    %endif
    %if ! 0%{?flatpak}
       -Dlibportal=false
    %endif
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

%check
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/org.gnome.eog.metainfo.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.gnome.eog.desktop

%files -f %{name}.lang
%doc AUTHORS NEWS README.md
%license COPYING
%{_bindir}/eog
%{_datadir}/eog
%{_datadir}/applications/org.gnome.eog.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_libdir}/eog
%{_datadir}/GConf/gsettings/eog.convert
%{_datadir}/glib-2.0/schemas/org.gnome.eog.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.eog.gschema.xml
%{_metainfodir}/org.gnome.eog.metainfo.xml

%files devel
%{_includedir}/eog-3.0
%{_libdir}/pkgconfig/eog.pc
%{_datadir}/gtk-doc/

%if !0%{?rhel}
%files tests
%dir %{_libexecdir}/eog
%{_libexecdir}/eog/installed-tests/
%{_datadir}/installed-tests/
%endif

%changelog
%autochangelog
