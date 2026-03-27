%global debug_package %{nil}

%global major_minor_version %%(echo %%{version} | cut -d "." -f 1-2)

Name: gtk-doc
Version: 1.36.0
Release: %autorelease
Summary: API documentation generation tool for GTK+ and GNOME

License: GPL-2.0-or-later AND GFDL-1.1-no-invariants-or-later
URL: https://gitlab.gnome.org/GNOME/gtk-doc/
Source0: http://download.gnome.org/sources/%{name}/%{major_minor_version}/%{name}-%{version}.tar.xz

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
%if 0%{?fedora} && 0%{?fedora} <= 43
%meson -Dtests=true
%else
%meson -Dtests=false
%endif
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
%doc README.md doc/* examples
%{_bindir}/*
%{_datadir}/aclocal/gtk-doc.m4
%{_datadir}/gtk-doc/
%{_datadir}/pkgconfig/gtk-doc.pc
%{_datadir}/help/*/gtk-doc-manual/
%{_libdir}/cmake/GtkDoc/

%changelog
%autochangelog
