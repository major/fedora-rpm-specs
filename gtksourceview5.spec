%global glib_version 2.72
%global gtk_version 4.6

%global api_ver 5

Name:           gtksourceview5
Version:        5.6.1
Release:        1%{?dist}
Summary:        Source code editing widget

License:        LGPLv2+
URL:            https://wiki.gnome.org/Projects/GtkSourceView
Source0:        https://download.gnome.org/sources/gtksourceview/%{api_ver}.4/gtksourceview-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gi-docgen
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(gio-2.0) >= %{glib_version}
BuildRequires:  pkgconfig(glib-2.0) >= %{glib_version}
BuildRequires:  pkgconfig(gobject-2.0) >= %{glib_version}
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4) >= %{gtk_version}
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pangoft2)
BuildRequires:  vala

Requires: glib2%{?_isa} >= %{glib_version}
Requires: gtk4%{?_isa} >= %{gtk_version}
Requires: hicolor-icon-theme

%description
GtkSourceView is a GNOME library that extends GtkTextView, the standard GTK+
widget for multiline text editing. GtkSourceView adds support for syntax
highlighting, undo/redo, file loading and saving, search and replace, a
completion system, printing, displaying line numbers, and other features
typical of a source code editor.

This package contains version %{api_ver} of GtkSourceView.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        tests
Summary:        Tests for the %{name} package
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    tests
The %{name}-tests package contains tests that can be used to verify
the functionality of the installed %{name} package.

%prep
%autosetup -n gtksourceview-%{version} -p1

%build
%meson -Dgtk_doc=true -Dsysprof=true -Dinstall_tests=true
%meson_build

%install
%meson_install

%find_lang gtksourceview-%{api_ver}

%files -f gtksourceview-%{api_ver}.lang
%license COPYING
%doc NEWS README.md
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/GtkSource-%{api_ver}.typelib
%{_libdir}/libgtksourceview-%{api_ver}.so.0*
%{_datadir}/gtksourceview-%{api_ver}/
%{_datadir}/icons/hicolor/scalable/actions/*

%files devel
%{_includedir}/gtksourceview-%{api_ver}/
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libgtksourceview-%{api_ver}.so
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/GtkSource-%{api_ver}.gir
%{_datadir}/doc/gtksourceview5
%{_datadir}/vala

%files tests
%{_bindir}/gtksourceview%{api_ver}-widget
%{_libexecdir}/installed-tests
%{_datadir}/installed-tests

%changelog
* Thu Sep 22 2022 Kalev Lember <klember@redhat.com> - 5.6.1-1
- Update to 5.6.1

* Mon Sep 19 2022 Kalev Lember <klember@redhat.com> - 5.6.0-1
- Update to 5.6.0

* Mon Aug 08 2022 Kalev Lember <klember@redhat.com> - 5.5.1-1
- Update to 5.5.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 15 2022 Kalev Lember <klember@redhat.com> - 5.5.0-1
- Update to 5.5.0

* Tue Jun 14 2022 David King <amigadave@amigadave.com> - 5.4.2-1
- Update to 5.4.2 (#2096086)

* Tue May 10 2022 Adam Williamson <awilliam@redhat.com> - 5.4.1-2
- Backport fix for dark theme Markdown highlighting

* Fri Apr 22 2022 David King <amigadave@amigadave.com> - 5.4.1-1
- Update to 5.4.1 (#2077674)

* Fri Mar 25 2022 David King <amigadave@amigadave.com> - 5.4.0-1
- Update to 5.4.0 (#2065873)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 11 2022 Neal Gompa <ngompa@fedoraproject.org> - 5.3.2-2
- Remove usage of undefined macros

* Sun Jan 09 2022 David King <amigadave@amigadave.com> - 5.3.2-1
- Update to 5.3.2

* Sat Jan 08 2022 David King <amigadave@amigadave.com> - 5.3.1-1
- Update to 5.3.1

* Mon Oct 25 2021 Amanda Graven <amanda@amandag.net> - 5.2.0-1
- Initial packaging of GtkSourceView 5
