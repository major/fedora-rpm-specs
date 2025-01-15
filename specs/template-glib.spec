Name:           template-glib
Version:        3.36.3
Release:        1%{?dist}
Summary:        A templating library for GLib

License:        LGPL-2.1-or-later
URL:            https://gitlab.gnome.org/GNOME/template-glib/
Source0:        https://download.gnome.org/sources/%{name}/3.36/%{name}-%{version}.tar.xz

BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)


%description
Template-GLib is a templating library for GLib. It includes a simple template
format along with integration into GObject-Introspection for properties and
methods. It separates the parsing of templates and the expansion of templates 
for faster expansion. You can also define scope, custom functions, and more 
with the embedded expression language.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup


%build
%meson -Dgtk_doc=true
%meson_build


%install
%meson_install
%find_lang template-glib


%files -f template-glib.lang
%license COPYING
%doc AUTHORS NEWS README.md
%{_libdir}/libtemplate_glib-1.0.so.0*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Template-1.0.typelib

%files devel
%doc CONTRIBUTING.md examples
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Template-1.0.gir
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/template-glib
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/template-glib-1.0.*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/template-glib-1.0.pc


%changelog
* Mon Jan 13 2025 nmontero <nmontero@redhat.com> - 3.36.3-1
- Update to 3.36.3

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.36.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Mar 04 2024 David King <amigadave@amigadave.com> - 3.36.2-1
- Update to 3.36.2

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.36.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.36.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Mar 04 2023 David King <amigadave@amigadave.com> - 3.36.1-1
- Update to 3.36.1

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.36.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Sep 19 2022 Kalev Lember <klember@redhat.com> - 3.36.0-1
- Update to 3.36.0

* Thu Jul 28 2022 Kalev Lember <klember@redhat.com> - 3.35.0-1
- Update to 3.35.0
- Tighten soname deps

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Mar 19 2022 David King <amigadave@amigadave.com> - 3.34.1-1
- Update to 3.34.1

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 10 2019 Kalev Lember <klember@redhat.com> - 3.34.0-1
- Update to 3.34.0

* Thu Sep 05 2019 Kalev Lember <klember@redhat.com> - 3.33.92-1
- Update to 3.33.92

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.32.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 13 2019 Kalev Lember <klember@redhat.com> - 3.32.0-1
- Update to 3.32.0

* Tue Feb 19 2019 Kalev Lember <klember@redhat.com> - 3.31.91-1
- Update to 3.31.91

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.30.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep 07 2018 Kalev Lember <klember@redhat.com> - 3.30.0-2
- Rebuilt against fixed atk (#1626575)

* Thu Sep 06 2018 Kalev Lember <klember@redhat.com> - 3.30.0-1
- Update to 3.30.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 14 2018 Kalev Lember <klember@redhat.com> - 3.28.0-1
- Update to 3.28.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.27.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Kalev Lember <klember@redhat.com> - 3.27.90-1
- Update to 3.27.90
- Drop ldconfig scriptlets

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.27.2-2
- Switch to %%ldconfig_scriptlets

* Tue Dec 19 2017 Kalev Lember <klember@redhat.com> - 3.27.2-1
- Update to 3.27.2

* Tue Oct  3 2017 Yanko Kaneti <yaneti@declera.com> - 3.26.1-1
- Update to 3.26.1

* Tue Sep 12 2017 Yanko Kaneti <yaneti@declera.com> - 3.26.0-1
- Update to 3.26.0

* Tue Sep  5 2017 Yanko Kaneti <yaneti@declera.com> - 3.25.92-1
- Update to 3.25.92

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.25.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.25.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 19 2017 Yanko Kaneti <yaneti@declera.com> - 3.25.3-1
- Update to 3.25.3

* Fri Jun  9 2017 Yanko Kaneti <yaneti@declera.com> - 3.25.2-2
- Address package review issues (#1460189) - -2
- Initial spec
