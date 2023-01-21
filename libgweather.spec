%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           libgweather
Version:        40.0
Release:        5%{?dist}
Summary:        A library for weather information

License:        GPLv2+
URL:            https://wiki.gnome.org/Projects/LibGWeather
Source0:        https://download.gnome.org/sources/libgweather/40/%{name}-%{tarball_version}.tar.xz

BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig(geocode-glib-1.0)
BuildRequires:  pkgconfig(gladeui-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  python3-gobject-base
BuildRequires:  vala

%description
libgweather is a library to access weather information from online
services for numerous locations.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1 -n libgweather-%{tarball_version}

%build
%meson -Dgtk_doc=true
%meson_build

%install
%meson_install

%find_lang %{name} --all-name

%files -f %{name}.lang
%doc HACKING.md NEWS README.md
%license COPYING
%{_libdir}/libgweather-3.so.16*
%{_libdir}/girepository-1.0/GWeather-3.0.typelib
%dir %{_libdir}/libgweather
%{_libdir}/libgweather/Locations.bin
%dir %{_datadir}/libgweather
%{_datadir}/libgweather/Locations.xml
%{_datadir}/libgweather/locations.dtd
%{_datadir}/glib-2.0/schemas/org.gnome.GWeather.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.GWeather.gschema.xml

%files devel
%{_includedir}/libgweather-3.0
%{_libdir}/libgweather-3.so
%{_libdir}/pkgconfig/gweather-3.0.pc
%{_datadir}/gir-1.0/GWeather-3.0.gir
%dir %{_datadir}/glade/
%dir %{_datadir}/glade/catalogs/
%{_datadir}/glade/catalogs/libgweather.xml
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/libgweather/
%dir %{_datadir}/vala/
%dir %{_datadir}/vala/vapi/
%{_datadir}/vala/vapi/gweather-3.0.deps
%{_datadir}/vala/vapi/gweather-3.0.vapi

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 40.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 40.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 40.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 40.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Mar 24 2021 Kalev Lember <klember@redhat.com> - 40.0-1
- Update to 40.0

* Wed Feb 17 2021 Kalev Lember <klember@redhat.com> - 40~beta-1
- Update to 40.beta

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 40~alpha.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 19 2021 Kalev Lember <klember@redhat.com> - 40~alpha.1-1
- Update to 40.alpha.1

* Tue Jan 19 2021 Kalev Lember <klember@redhat.com> - 40~alpha-1
- Update to 40.alpha

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.36.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.36.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 20 2020 Bastien Nocera <bnocera@redhat.com> - 3.36.1-1
+ libgweather-3.36.1-1
- Update to 3.36.1
- Work-around broken current conditions weather servers

* Mon Mar 09 2020 Bastien Nocera <bnocera@redhat.com> - 3.36.0-1
+ libgweather-3.36.0-1
- Update to 3.36.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Kalev Lember <klember@redhat.com> - 3.34.0-1
- Update to 3.34.0

* Tue Sep 03 2019 Kalev Lember <klember@redhat.com> - 3.33.92-1
- Update to 3.33.92

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.33.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 08 2019 Kalev Lember <klember@redhat.com> - 3.33.0-1
- Update to 3.33.0

* Wed Mar 20 2019 Kalev Lember <klember@redhat.com> - 3.32.1-1
- Update to 3.32.1

* Mon Mar 11 2019 Kalev Lember <klember@redhat.com> - 3.32.0-1
- Update to 3.32.0

* Fri Feb 22 2019 Kalev Lember <klember@redhat.com> - 3.31.91-1
- Update to 3.31.91

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 09 2018 Debarshi Ray <rishi@fedoraproject.org> - 3.28.2-3
- Fix dangling symbolic link to README.md

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 13 2018 Bastien Nocera <bnocera@redhat.com> - 3.28.2-1
+ libgweather-3.28.2-1
- Fix crasher in gnome-shell (#1577561)

* Thu Mar 22 2018 Kalev Lember <klember@redhat.com> - 3.28.1-1
- Update to 3.28.1

* Fri Mar 16 2018 Kalev Lember <klember@redhat.com> - 3.28.0-2
- Backport a patch to fix memory and D-Bus match rule leaks

* Sun Mar 11 2018 Kalev Lember <klember@redhat.com> - 3.28.0-1
- Update to 3.28.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.27.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Kalev Lember <klember@redhat.com> - 3.27.4-1
- Update to 3.27.4
- Switch to meson build system
- Drop ldconfig scriptlets
- Tighten soname globs

* Sat Jan 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.26.1-2
- Remove obsolete scriptlets

* Fri Dec 01 2017 Kalev Lember <klember@redhat.com> - 3.26.1-1
- Update to 3.26.1

* Mon Sep 11 2017 Kalev Lember <klember@redhat.com> - 3.26.0-1
- Update to 3.26.0

* Thu Sep 07 2017 Kalev Lember <klember@redhat.com> - 3.25.92-1
- Update to 3.25.92

* Fri Aug 25 2017 Bastien Nocera <bnocera@redhat.com> - 3.25.91-1
+ libgweather-3.25.91-1
- Update to 3.25.91

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 12 2017 Kalev Lember <klember@redhat.com> - 3.24.1-1
- Update to 3.24.1

* Wed May 24 2017 Adam Williamson <awilliam@redhat.com> - 3.24.0-3
- Backport some more memory handling fixes

* Thu Apr 27 2017 Florian Müllner <fmuellner@redhat.com> - 3.24.0-2
- Backport memory handling fixes

* Tue Mar 21 2017 Kalev Lember <klember@redhat.com> - 3.24.0-1
- Update to 3.24.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 27 2016 Kalev Lember <klember@redhat.com> - 3.20.4-1
- Update to 3.20.4

* Thu Sep 22 2016 Kalev Lember <klember@redhat.com> - 3.20.3-2
- BR vala instead of obsolete vala-tools subpackage

* Mon Aug 29 2016 Kalev Lember <klember@redhat.com> - 3.20.3-1
- Update to 3.20.3

* Wed Aug 17 2016 Kalev Lember <klember@redhat.com> - 3.20.2-1
- Update to 3.20.2

* Mon May 09 2016 Kalev Lember <klember@redhat.com> - 3.20.1-1
- Update to 3.20.1

* Tue Mar 22 2016 Kalev Lember <klember@redhat.com> - 3.20.0-1
- Update to 3.20.0

* Tue Mar 15 2016 Kalev Lember <klember@redhat.com> - 3.19.92-1
- Update to 3.19.92

* Tue Feb 16 2016 Richard Hughes <rhughes@redhat.com> - 3.19.90-1
- Update to 3.19.90

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 12 2015 Kalev Lember <klember@redhat.com> - 3.18.1-1
- Update to 3.18.1

* Mon Sep 21 2015 Kalev Lember <klember@redhat.com> - 3.18.0-1
- Update to 3.18.0

* Fri Sep 11 2015 Kalev Lember <klember@redhat.com> - 3.17.92-1
- Update to 3.17.92
- Use make_install macro

* Tue Jul 28 2015 Kalev Lember <klember@redhat.com> - 3.17.2-1
- Update to 3.17.2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 01 2015 Kalev Lember <kalevlember@gmail.com> - 3.17.1-1
- Update to 3.17.1

* Tue Apr 14 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.1-1
- Update to 3.16.1

* Mon Mar 23 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.0-1
- Update to 3.16.0

* Tue Mar 17 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.92-1
- Update to 3.15.92

* Tue Mar 03 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.91-1
- Update to 3.15.91

* Mon Feb 16 2015 David King <amigadave@amigadave.com> - 3.15.90-1
- Update to 3.15.90
- Update URL
- Use license macro for COPYING
- Add HACKING, NEWS and README to doc
- Use pkgconfig for BuildRequires

* Tue Jan 20 2015 Richard Hughes <rhughes@redhat.com> - 3.15.1-1
- Update to 3.15.1

* Mon Dec 29 2014 Richard Hughes <rhughes@redhat.com> - 3.14.2-1
- Update to 3.14.2

* Mon Oct 13 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.1-1
- Update to 3.14.1

* Mon Sep 22 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.0-1
- Update to 3.14.0

* Tue Sep 16 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.92-1
- Update to 3.13.92

* Thu Sep 11 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.91-3
- Really apply the patch

* Thu Sep 11 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.91-2
- Adapt to yr.no API changes (#1140476)

* Mon Sep 01 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.91-1
- Update to 3.13.91

* Tue Aug 19 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.90-1
- Update to 3.13.90

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.4-1
- Update to 3.13.4
- Drop gnome-icon-theme deps

* Tue Jun 24 2014 Richard Hughes <rhughes@redhat.com> - 3.13.3-1
- Update to 3.13.3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.2-1
- Update to 3.13.2

* Thu May 01 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.1-1
- Update to 3.13.1

* Wed Apr 16 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.1-1
- Update to 3.12.1

* Tue Mar 25 2014 Richard Hughes <rhughes@redhat.com> - 3.12.0-1
- Update to 3.12.0

* Tue Mar 18 2014 Richard Hughes <rhughes@redhat.com> - 3.11.92-1
- Update to 3.11.92

* Tue Mar 04 2014 Richard Hughes <rhughes@redhat.com> - 3.11.91-1
- Update to 3.11.91

* Tue Feb 18 2014 Richard Hughes <rhughes@redhat.com> - 3.11.90-1
- Update to 3.11.90

* Mon Feb 03 2014 Richard Hughes <rhughes@redhat.com> - 3.11.5-1
- Update to 3.11.5

* Tue Jan 14 2014 Richard Hughes <rhughes@redhat.com> - 3.11.4-1
- Update to 3.11.4

* Wed Jan 08 2014 Richard Hughes <rhughes@redhat.com> - 3.11.3-1
- Update to 3.11.3

* Tue Oct 29 2013 Richard Hughes <rhughes@redhat.com> - 3.10.1-1
- Update to 3.10.1

* Wed Sep 25 2013 Kalev Lember <kalevlember@gmail.com> - 3.10.0-1
- Update to 3.10.0

* Wed Sep 18 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.92-1
- Update to 3.9.92

* Wed Sep 04 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.91-1
- Update to 3.9.91
- Install the glade catalog
- Enable vala support

* Thu Aug 22 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.90-1
- Update to 3.9.90

* Mon Aug 05 2013 Debarshi Ray <rishi@fedoraproject.org> - 3.9.5-1
- Update to 3.9.5

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 21 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.3-2
- Tighten the -devel subpackage deps

* Thu Jun 20 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.3-1
- Update to 3.9.3

* Sun Jun 02 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.2-1
- Update to 3.9.2

* Sat May 04 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.1-1
- Update to 3.9.1
- Remove old gnome-applets-devel obsoletes

* Mon Apr 15 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.1-1
- Update to 3.8.1

* Tue Mar 26 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.0-1
- Update to 3.8.0

* Tue Mar 19 2013 Richard Hughes <rhughes@redhat.com> - 3.7.92-1
- Update to 3.7.92

* Thu Mar  7 2013 Matthias Clasen <mclasen@redhat.com> - 3.7.91-1
- Update to 3.7.91

* Tue Feb 19 2013 Richard Hughes <rhughes@redhat.com> - 3.7.90-1
- Update to 3.7.90

* Wed Feb 06 2013 Kalev Lember <kalevlember@gmail.com> - 3.7.5-1
- Update to 3.7.5

* Wed Jan 16 2013 Richard Hughes <hughsient@gmail.com> - 3.7.4-1
- Update to 3.7.4

* Thu Dec 20 2012 Kalev Lember <kalevlember@gmail.com> - 3.7.3-1
- Update to 3.7.3

* Tue Nov 20 2012 Richard Hughes <hughsient@gmail.com> - 3.7.2-1
- Update to 3.7.2

* Tue Nov 13 2012 Kalev Lember <kalevlember@gmail.com> - 3.6.2-1
- Update to 3.6.2

* Tue Oct 16 2012 Kalev Lember <kalevlember@gmail.com> - 3.6.1-1
- Update to 3.6.1

* Tue Sep 25 2012 Kalev Lember <kalevlember@gmail.com> - 3.6.0-1
- Update to 3.6.0

* Wed Sep 19 2012 Kalev Lember <kalevlember@gmail.com> - 3.5.92-2
- Silence glib-compile-schemas scriplets

* Wed Sep 19 2012 Richard Hughes <hughsient@gmail.com> - 3.5.92-1
- Update to 3.5.92

* Tue Sep 04 2012 Richard Hughes <hughsient@gmail.com> - 3.5.91-1
- Update to 3.5.91

* Tue Aug 21 2012 Richard Hughes <hughsient@gmail.com> - 3.5.90-1
- Update to 3.5.90

* Tue Aug 07 2012 Richard Hughes <hughsient@gmail.com> - 3.5.5-1
- Update to 3.5.5

* Tue Jul 17 2012 Richard Hughes <hughsient@gmail.com> - 3.5.4-1
- Update to 3.5.4

* Tue Jun 26 2012 Matthias Clasen <mclasen@redhat.com> - 3.5.1-1
- Update to 3.5.1

* Thu Jan 12 2012 Matthias Clasen <mclasen@redhat.com> - 3.2.1-2
- Drop gtk-doc dependency

* Wed Nov  2 2011 Matthias Clasen <mclasen@redhat.com> - 3.2.1-1
- Update to 3.2.1

* Mon Sep 26 2011 Ray <rstrode@redhat.com> - 3.2.0-1
- Update to 3.2.0

* Mon Jul 04 2011 Bastien Nocera <bnocera@redhat.com> 3.1.3-1
- Update to 3.1.3

* Mon Apr  4 2011 Christopher Aillon <caillon@redhat.com> - 3.0.0-1
- Update to 3.0.0

* Thu Feb 10 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.6-3
- Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.91.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Feb 03 2011 Bastien Nocera <bnocera@redhat.com> 2.91.6-1
- Update to 2.91.6

* Sun Jan 30 2011 Matthew Barnes <mbarnes@redhat.com> - 2.91.0-1
- Update to 2.91.0

* Thu Sep 30 2010 Matthias Clasen <mclasen@redhat.com> - 2.30.3-1
- Update to 2.30.3

* Tue Mar 30 2010 Matthias Clasen <mclasen@redhat.com> - 2.30.0-1
- Update to 2.30.0

* Tue Mar 09 2010 Bastien Nocera <bnocera@redhat.com> 2.29.92-1
- Update to 2.29.92

* Tue Feb 23 2010 Matthias Clasen <mclasen@redhat.com> 2.29.91-1
- Update to 2.29.91

* Wed Feb 10 2010 Bastien Nocera <bnocera@redhat.com> 2.29.90-1
- Update to 2.29.90

* Tue Jan 12 2010 Matthias Clasen <mclasen@redhat.com> 2.29.5-1
- Update to 2.29.5

* Tue Dec 22 2009 Matthias Clasen <mclasen@redhat.com> 2.29.4-1
- Update to 2.29.4

* Mon Sep 21 2009 Matthias Clasen <mclasen@redhat.com> 2.28.0-1
- Update to 2.28.0

* Wed Sep  9 2009 Matthias Clasen <mclasen@redhat.com> 2.27.92-1
- Update to 2.27.92

* Tue Aug 25 2009 Matthias Clasen <mclasen@redhat.com> 2.27.91-1
- Update to 2.27.91

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 20 2009 Matthias Clasen <mclasen@redhat.com> 2.26.1-5
- Keep locations in gettext catalogs

* Wed Jun 10 2009 Matthias Clasen <mclasen@redhat.com> 2.26.1-3
- Fix multilib parallel-installability (#477672)
- Remove some old optimizations that are now no-ops

* Mon Apr 27 2009 Matthias Clasen <mclasen@redhat.com> 2.26.1-2
- Don't drop schemas translations from po files

* Mon Apr 13 2009 Matthias Clasen <mclasen@redhat.com> 2.26.1-1
- Update to 2.26.1
- See http://download.gnome.org/sources/libgweather/2.26/libgweather-2.26.1.news

* Mon Mar 16 2009 Matthias Clasen <mclasen@redhat.com> 2.26.0-1
- Update to 2.26.0

* Tue Mar  3 2009 Matthias Clasen <mclasen@redhat.com> 2.25.92-1
- Update to 2.25.92

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.25.91-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 18 2009 Matthias Clasen <mclasen@redhat.com> 2.25.91-1
- Update to 2.25.91

* Tue Jan 20 2009 Matthias Clasen <mclasen@redhat.com> 2.25.5-1
- Upate to 2.25.5

* Mon Jan 05 2009 Matthew Barnes <mbarnes@redhat.com> 2.25.4-1
- Update to 2.25.4

* Tue Dec 16 2008 Matthias Clasen <mclasen@redhat.com> 2.25.3-2
- Update to 2.25.3

* Wed Dec  3 2008 Matthias Clasen <mclasen@redhat.com> 2.25.2-2
- Update to 2.25.2

* Wed Oct 22 2008 Matthias Clasen <mclasen@redhat.com> 2.24.1-1
- Update to 2.24.1

* Mon Sep 22 2008 Matthias Clasen <mclasen@redhat.com> 2.24.0-2
- Apply %%lang tags to localized xml files

* Mon Sep 22 2008 Matthias Clasen <mclasen@redhat.com> 2.24.0-1
- Update to 2.24.0

* Mon Sep  8 2008 Matthias Clasen <mclasen@redhat.com> 2.23.92-1
- Update to 2.23.92

* Tue Sep  2 2008 Matthias Clasen <mclasen@redhat.com> 2.23.91-1
- Update to 2.23.91

* Mon Aug  4 2008 Matthias Clasen <mclasen@redhat.com> 2.23.6-1
- Update to 2.23.6

* Fri Jul 25 2008 Matthias Clasen <mclasen@redhat.com> 2.23.5-2
- Fix pending request accounting

* Tue Jul 22 2008 Matthias Clasen <mclasen@redhat.com> 2.23.5-1
- Update to 2.23.5

* Tue Jun 17 2008 Matthias Clasen <mclasen@redhat.com> 2.23.4-1
- Update to 2.23.4

* Wed Jun  4 2008 Matthias Clasen <mclasen@redhat.com> 2.23.3-1
- Update to 2.23.3

* Wed May 14 2008 Matthias Clasen <mclasen@redhat.com> 2.23.2-1
- Update to 2.23.2

* Thu Apr 24 2008 Matthias Clasen <mclasen@redhat.com> 2.23.1-1
- Update to 2.23.1

* Thu Apr 17 2008 Matthias Clasen <mclasen@redhat.com> 2.22.1.1-2
- Leave Cairo in Africa (#442793)

* Mon Apr  7 2008 Matthias Clasen <mclasen@redhat.com> 2.22.1.1-1
- Update to 2.22.1.1

* Tue Mar 11 2008 Matthias Clasen <mclasen@redhat.com> 2.22.0-1
- Update to 2.22.0

* Tue Feb 26 2008 Matthias Clasen <mclasen@redhat.com> 2.21.92-1
- Update to 2.21.92

* Mon Feb 11 2008  Matthias Clasen <mclasen@redhat.com> 2.21.2-6
- Remove obsolete translations

* Sat Feb  9 2008  Matthias Clasen <mclasen@redhat.com> 2.21.2-5
- Rebuild for gcc 4.3

* Wed Jan 16 2008  Matthias Clasen <mclasen@redhat.com> 2.21.2-4
- Add Obsoletes for gnome-applets-devel

* Wed Jan 16 2008  Matthias Clasen <mclasen@redhat.com> 2.21.2-3
- Carry over space-saving hack from gnome-applets

* Tue Jan 15 2008  Matthias Clasen <mclasen@redhat.com> 2.21.2-2
- Incorporate review feedback (#428739)

* Mon Jan 14 2008  Matthias Clasen <mclasen@redhat.com> 2.21.2-1
- Update to 2.21.2

* Thu Jan 10 2008  Matthias Clasen <mclasen@redhat.com> 2.21.1-1
- Initial packaging

