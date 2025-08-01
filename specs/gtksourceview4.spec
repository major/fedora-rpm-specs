%bcond glade %[!(0%{?rhel} >= 10)]

%global glib_version 2.48
%global gtk_version 3.22

Name:           gtksourceview4
Version:        4.8.4
Release:        10%{?dist}
Summary:        Source code editing widget

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://wiki.gnome.org/Projects/GtkSourceView
Source0:        https://download.gnome.org/sources/gtksourceview/4.8/gtksourceview-%{version}.tar.xz
# https://gitlab.gnome.org/GNOME/gtksourceview/-/commit/2538a4daf1aba9c42c3dcfe2ff394874ac157c67
# https://gitlab.gnome.org/GNOME/gtksourceview/-/issues/278
# Fix some regexes to work with pcre2
Patch0:         0001-language-specs-use-N-U-escape-sequences.patch

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
%if %{with glade}
BuildRequires:  pkgconfig(gladeui-2.0)
%endif
BuildRequires:  pkgconfig(glib-2.0) >= %{glib_version}
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= %{gtk_version}
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pango)
BuildRequires:  vala

Requires: glib2%{?_isa} >= %{glib_version}
Requires: gtk3%{?_isa} >= %{gtk_version}

%description
GtkSourceView is a GNOME library that extends GtkTextView, the standard GTK+
widget for multiline text editing. GtkSourceView adds support for syntax
highlighting, undo/redo, file loading and saving, search and replace, a
completion system, printing, displaying line numbers, and other features
typical of a source code editor.

This package contains version 4 of GtkSourceView.

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
%meson -Dgtk_doc=true %{?with_glade:-Dglade_catalog=true} -Dinstall_tests=true
%meson_build

%install
%meson_install

%find_lang gtksourceview-4

%files -f gtksourceview-4.lang
%license COPYING
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/GtkSource-4.typelib
%{_libdir}/libgtksourceview-4.so.0*
%{_datadir}/gtksourceview-4/

%files devel
%{_includedir}/gtksourceview-4/
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libgtksourceview-4.so
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/GtkSource-4.gir
%if %{with glade}
%dir %{_datadir}/glade
%dir %{_datadir}/glade/catalogs
%{_datadir}/glade/catalogs/gtksourceview.xml
%endif
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/*
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/gtksourceview-4.deps
%{_datadir}/vala/vapi/gtksourceview-4.vapi

%files tests
%dir %{_libexecdir}/installed-tests
%{_libexecdir}/installed-tests/gtksourceview-4/
%dir %{_datadir}/installed-tests
%{_datadir}/installed-tests/gtksourceview-4/

%changelog
* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 4.8.4-8
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Oct 31 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 4.8.4-4
- Disable glade catalog in RHEL builds

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov 03 2022 David King <amigadave@amigadave.com> - 4.8.4-1
- Update to 4.8.4

* Tue Jul 26 2022 Adam Williamson <awilliam@redhat.com> - 4.8.3-3
- Backport fix from main branch for regexes with pcre2

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Mar 19 2022 David King <amigadave@amigadave.com> - 4.8.3-1
- Update to 4.8.3

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 08 2021 Kalev Lember <klember@redhat.com> - 4.8.2-1
- Update to 4.8.2

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Kalev Lember <klember@redhat.com> - 4.8.1-1
- Update to 4.8.1

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Sep 12 2020 Kalev Lember <klember@redhat.com> - 4.8.0-1
- Update to 4.8.0

* Mon Aug 17 2020 Kalev Lember <klember@redhat.com> - 4.7.90-1
- Update to 4.7.90

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Kalev Lember <klember@redhat.com> - 4.6.1-1
- Update to 4.6.1

* Sat Mar 07 2020 Kalev Lember <klember@redhat.com> - 4.6.0-1
- Update to 4.6.0

* Mon Feb 17 2020 Kalev Lember <klember@redhat.com> - 4.5.91-1
- Update to 4.5.91

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 10 2019 Kalev Lember <klember@redhat.com> - 4.4.0-1
- Update to 4.4.0

* Wed Sep 04 2019 Kalev Lember <klember@redhat.com> - 4.3.92-1
- Update to 4.3.92

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 29 2019 Phil Wyett <philwyett@kathenas.org> - 4.3.1-1
- Update to 4.3.1
- Convert to meson

* Sat Mar 16 2019 Kalev Lember <klember@redhat.com> - 4.2.0-1
- Update to 4.2.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep 07 2018 Kalev Lember <klember@redhat.com> - 4.0.3-2
- Rebuilt against fixed atk (#1626575)

* Fri Sep 07 2018 Pete Walter <pwalter@fedoraproject.org> - 4.0.3-1
- Initial packaging of GtkSourceView 4
