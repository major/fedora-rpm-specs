%global glib_version 2.72
%global gtk_version 4.13.9

%global api_ver 5

Name:           gtksourceview5
Version:        5.15.0
Release:        1%{?dist}
Summary:        Source code editing widget

License:        LGPL-2.1-or-later
URL:            https://wiki.gnome.org/Projects/GtkSourceView
Source0:        https://download.gnome.org/sources/gtksourceview/5.15/gtksourceview-%{version}.tar.xz

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
BuildRequires:  pkgconfig(sysprof-capture-4)
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
%meson -Ddocumentation=true -Dsysprof=true -Dinstall-tests=true
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
* Mon Feb 03 2025 nmontero <nmontero@redhat.com> - 5.15.0-1
- Update to 5.15.0

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.14.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Nov 25 2024 nmontero <nmontero@redhat.com> - 5.14.2-1
- Update to 5.14.2

* Sat Oct 05 2024 David King <amigadave@amigadave.com> - 5.14.1-1
- Update to 5.14.1

* Mon Sep 16 2024 nmontero <nmontero@redhat.com> - 5.14.0-1
- Update to 5.14.0

* Mon Aug 05 2024 nmontero <nmontero@redhat.com> - 5.13.1-1
- Update to 5.13.1

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 01 2024 Nieves Montero <nmontero@redhat.com> - 5.13.0-1
- Update to 5.13.0

* Fri May 31 2024 Nieves Montero <nmontero@redhat.com> - 5.12.1-1
- Update to 5.12.1

* Sat Mar 16 2024 David King <amigadave@amigadave.com> - 5.12.0-1
- Update to 5.12.0

* Mon Mar 04 2024 David King <amigadave@amigadave.com> - 5.11.2-1
- Update to 5.11.2

* Wed Feb 14 2024 David King <amigadave@amigadave.com> - 5.11.1-1
- Update to 5.11.1

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 David King <amigadave@amigadave.com> - 5.11.0-1
- Update to 5.11.0

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Sep 19 2023 Kalev Lember <klember@redhat.com> - 5.10.0-1
- Update to 5.10.0

* Tue Sep 05 2023 Kalev Lember <klember@redhat.com> - 5.9.0-1
- Update to 5.9.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Mar 18 2023 David King <amigadave@amigadave.com> - 5.8.0-1
- Update to 5.8.0

* Sat Mar 04 2023 David King <amigadave@amigadave.com> - 5.7.2-1
- Update to 5.7.2

* Thu Feb 16 2023 David King <amigadave@amigadave.com> - 5.7.1-1
- Update to 5.7.1

* Mon Feb 06 2023 David King <amigadave@amigadave.com> - 5.7.0-1
- Update to 5.7.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Sep 27 2022 Kalev Lember <klember@redhat.com> - 5.6.1-2
- Rebuild to fix sysprof-capture symbols leaking into libraries consuming it

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
