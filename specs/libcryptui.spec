Name:    libcryptui
Version: 3.12.2
Release: %autorelease
Summary: Interface components for OpenPGP

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
URL:     http://projects.gnome.org/seahorse/
Source0: http://download.gnome.org/sources/libcryptui/3.12/%{name}-%{version}.tar.xz
Patch0:  libcryptui-3.12.2-gpg22.patch
Patch1:  libcryptui-3.12.2-use-gcr.patch
Patch2:  libcryptui-gpg_version_fix.patch

BuildRequires: autoconf automake
BuildRequires: gnupg1
BuildRequires: gobject-introspection-devel
BuildRequires: gpgme-devel
BuildRequires: gtk-doc
BuildRequires: intltool
BuildRequires: libtool
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(gcr-3)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libnotify)
BuildRequires: pkgconfig(sm)
BuildRequires: make

%description
libcryptui is a library used for prompting for PGP keys.

%package devel
Summary: Header files required to develop with libcryptui
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The libcryptui-devel package contains the header files and developer
documentation for the libcryptui library.

%prep
%autosetup -p1
autoreconf --force --install

%build
%configure
%make_build

%install
%make_install
%find_lang cryptui --with-gnome --all-name

find ${RPM_BUILD_ROOT} -type f -name "*.a" -delete
find ${RPM_BUILD_ROOT} -type f -name "*.la" -delete

%files -f cryptui.lang
%license COPYING-LIBCRYPTUI
%doc AUTHORS NEWS README
%{_bindir}/*
%{_mandir}/man1/*.1*
%{_datadir}/cryptui
%{_libdir}/libcryptui.so.*
%{_datadir}/dbus-1/services/*
%{_datadir}/pixmaps/cryptui
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/*
%{_datadir}/GConf/gsettings/org.gnome.seahorse.recipients.convert
%{_datadir}/glib-2.0/schemas/org.gnome.seahorse.recipients.gschema.xml

%files devel
%{_libdir}/libcryptui.so
%{_libdir}/pkgconfig/*
%{_includedir}/libcryptui
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/libcryptui
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/*

%changelog
%autochangelog
