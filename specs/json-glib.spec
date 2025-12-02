%define glib2_version 2.72.0

Name:           json-glib
Version:        1.10.8
Release:        %autorelease
Summary:        Library for JavaScript Object Notation format

License:        LGPL-2.1-or-later
URL:            https://wiki.gnome.org/Projects/JsonGlib
Source0:        https://download.gnome.org/sources/%{name}/1.10/%{name}-%{version}.tar.xz

BuildRequires:  docbook-style-xsl
BuildRequires:  gettext
BuildRequires:  gi-docgen
BuildRequires:  pkgconfig(gio-2.0) >= %{glib2_version}
BuildRequires:  gobject-introspection-devel
BuildRequires:  meson
BuildRequires:  /usr/bin/rst2man
BuildRequires:  /usr/bin/rst2html5
BuildRequires:  python3-docutils

Requires:       glib2%{?_isa} >= %{glib2_version}

%description
%{name} is a library providing serialization and deserialization support
for the JavaScript Object Notation (JSON) format.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{_isa} = %{version}-%{release}
# Because web fonts from upstream are not bundled in the gi-docgen package,
# packages containing documentation generated with gi-docgen should depend on
# this metapackage to ensure the proper system fonts are present.
Recommends:     gi-docgen-fonts

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package tests
Summary: Tests for the json-glib package
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tests
The json-glib-tests package contains tests that can be used to verify
the functionality of the installed json-glib package.


%prep
%setup -q -n %{name}-%{version}


%build
%meson -Ddocumentation=enabled -Dman=true
%meson_build


%install
%meson_install

%find_lang json-glib-1.0


%files -f json-glib-1.0.lang
%doc NEWS README.md
%license LICENSES/LGPL-2.1-or-later.txt
%{_libdir}/libjson-glib-1.0.so.0*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Json-1.0.typelib

%files devel
%{_includedir}/json-glib-1.0/
%{_libdir}/libjson-glib-1.0.so
%{_libdir}/pkgconfig/json-glib-1.0.pc
%{_datadir}/doc/json-glib-1.0/
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Json-1.0.gir
%{_bindir}/json-glib-format
%{_bindir}/json-glib-validate
%{_mandir}/man1/json-glib-format.1*
%{_mandir}/man1/json-glib-validate.1*

%files tests
%{_libexecdir}/installed-tests/
%{_datadir}/installed-tests/


%changelog
%autochangelog
