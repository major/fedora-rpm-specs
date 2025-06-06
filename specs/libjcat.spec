%global glib2_version 2.45.8
%global json_glib_version 1.1.1

Summary:   Library for reading Jcat files
Name:      libjcat
Version:   0.2.3
Release:   %autorelease
License:   LGPL-2.1-or-later
URL:       https://github.com/hughsie/%{name}
Source0:   https://github.com/hughsie/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires: gtk-doc
BuildRequires: meson
BuildRequires: gobject-introspection-devel
BuildRequires: glib2-devel >= %{glib2_version}
BuildRequires: json-glib-devel >= %{json_glib_version}
BuildRequires: gnutls-devel
BuildRequires: gnutls-utils
BuildRequires: gpgme-devel
BuildRequires: vala

Requires: glib2%{?_isa} >= %{glib2_version}

%description
This library allows reading and writing gzip-compressed JSON catalog files,
which can be used to store GPG, PKCS-7 and SHA-256 checksums for each file.

This provides equivalent functionality to the catalog files supported in
Microsoft Windows.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for development with %{name}.

%package tests
Summary: Files for installed tests

%description tests
Executable and data files for installed tests.

%prep
%autosetup -p0

%build

%meson \
    -Dgtkdoc=true \
    -Dtests=true

%meson_build

%install
%meson_install

%check
%meson_test

%files
%doc README.md
%license LICENSE
%{_bindir}/jcat-tool
%{_datadir}/man/man1/*.1*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/*.typelib
%{_libdir}/libjcat.so.1*

%files devel
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/*.gir
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/libjcat
%{_includedir}/libjcat-1
%{_libdir}/libjcat.so
%{_libdir}/pkgconfig/jcat.pc
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/jcat.deps
%{_datadir}/vala/vapi/jcat.vapi

%files tests
%doc README.md
%{_libexecdir}/installed-tests/libjcat/*
%{_datadir}/installed-tests/libjcat/*
%dir %{_datadir}/installed-tests/libjcat

%changelog
%autochangelog
