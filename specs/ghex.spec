%global tarball_version %%(echo %{version} | tr '~' '.')

%global __provides_exclude_from ^%{_libdir}/gtkhex-4.0/.*\\.so$

Name:           ghex
Version:        48.0
Release:        %autorelease
Summary:        Binary editor for GNOME

# Source code is under GPLv2+, help is under GFDL and icon is under CC-BY-SA.
License:        GPL-2.0-or-later AND GFDL-1.1-no-invariants-or-later AND CC-BY-SA-4.0
URL:            https://gitlab.gnome.org/GNOME/ghex
Source0:        https://download.gnome.org/sources/ghex/48/ghex-%{tarball_version}.tar.xz

BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  /usr/bin/g-ir-scanner

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
GHex can load raw data from binary files and display them for editing in the
traditional hex editor view. The display is split in two columns, with
hexadecimal values in one column and the ASCII representation in the other.
A useful tool for working with raw data.


%package        libs
Summary:        GtkHex library

%description    libs
The %{name}-libs package contains the shared GtkHex library.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n %{name}-%{tarball_version}


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{name} --with-gnome


%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.GHex.desktop
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/org.gnome.GHex.metainfo.xml


%files -f %{name}.lang
%license COPYING COPYING-DOCS
%doc NEWS README.md
%{_bindir}/ghex
%{_datadir}/applications/org.gnome.GHex.desktop
%{_datadir}/dbus-1/services/org.gnome.GHex.service
%{_datadir}/glib-2.0/schemas/org.gnome.GHex.gschema.xml
%{_datadir}/icons/hicolor/*/apps/*
%{_metainfodir}/org.gnome.GHex.metainfo.xml

%files libs
%license COPYING
%{_libdir}/libgtkhex-4.so.1*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Hex-4.typelib
%{_libdir}/gtkhex-4.0/

%files devel
%{_includedir}/gtkhex-4/
%{_libdir}/libgtkhex-4.so
%{_libdir}/pkgconfig/gtkhex-4.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Hex-4.gir


%changelog
%autochangelog