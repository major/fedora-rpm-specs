%global debug_package %{nil}

Name: gtk-doc
Version: 1.35.1
Release: %autorelease
Summary: API documentation generation tool for GTK+ and GNOME

License: GPL-2.0-or-later AND GFDL-1.1-no-invariants-or-later
URL: https://gitlab.gnome.org/GNOME/gtk-doc/
Source0: http://download.gnome.org/sources/%{name}/1.35/%{name}-%{version}.tar.xz

# Resolve FTBFS, unclear if solution is 'proper'
# https://gitlab.gnome.org/GNOME/gtk-doc/-/issues/150
Patch: https://gitlab.gnome.org/GNOME/gtk-doc/-/merge_requests/74.patch

# Update CMake minimum version from 3.2 to 3.12: support CMake 4.0
# https://gitlab.gnome.org/GNOME/gtk-doc/-/merge_requests/101
Patch: https://gitlab.gnome.org/GNOME/gtk-doc/-/merge_requests/101.patch

BuildRequires: dblatex
BuildRequires: docbook-utils
BuildRequires: /usr/bin/xsltproc
BuildRequires: docbook-style-xsl
BuildRequires: gcc
BuildRequires: gettext
BuildRequires: glib2-devel
BuildRequires: meson
BuildRequires: python3-devel
BuildRequires: python3-pygments
%if 0%{?fedora} && 0%{?fedora} <= 43
BuildRequires: python3-parameterized
%endif
BuildRequires: python3-lxml
BuildRequires: yelp-tools

# Following are not automatically installed
Requires: docbook-utils /usr/bin/xsltproc docbook-style-xsl
Requires: python3-pygments
Requires: python3-lxml

# Required for cmake directory
Requires: cmake-filesystem

%description
gtk-doc is a tool for generating API reference documentation.
It is used for generating the documentation for GTK+, GLib
and GNOME.

%prep
%autosetup -p1

# Move this doc file to avoid name collisions
mv doc/README doc/README.docs

%build
%meson
%meson_build

%install
%meson_install

%py_byte_compile %{__python3} %{buildroot}%{_datadir}/gtk-doc/

%if 0%{?fedora} && 0%{?fedora} <= 43
%check
%meson_test
%endif

%files
%license COPYING COPYING-DOCS
%doc AUTHORS README doc/* examples
%{_bindir}/*
%{_datadir}/aclocal/gtk-doc.m4
%{_datadir}/gtk-doc/
%{_datadir}/pkgconfig/gtk-doc.pc
%{_datadir}/help/*/gtk-doc-manual/
%{_libdir}/cmake/GtkDoc/

%changelog
%autochangelog
