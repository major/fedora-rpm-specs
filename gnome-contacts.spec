%global gtk4_version 4.6

%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           gnome-contacts
Version:        43.0
Release:        1%{?dist}
Summary:        Contacts manager for GNOME

License:        GPLv2+
URL:            https://wiki.gnome.org/Apps/Contacts
Source0:        https://download.gnome.org/sources/%{name}/43/%{name}-%{tarball_version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  docbook-dtds
BuildRequires:  docbook-style-xsl
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  pkgconfig(folks)
BuildRequires:  pkgconfig(folks-eds)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(goa-1.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4) >= %{gtk4_version}
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libportal-gtk4)

Requires:       gtk4%{?_isa} >= %{gtk4_version}
Requires:       hicolor-icon-theme

%description
%{name} is a standalone contacts manager for GNOME desktop.

%prep
%autosetup -p1 -n %{name}-%{tarball_version}

%build
export VALAFLAGS="-g"
%meson
%meson_build

%install
%meson_install
%find_lang %{name}

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/org.gnome.Contacts.appdata.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.gnome.Contacts.desktop

%files -f %{name}.lang
%doc NEWS
%license COPYING
%{_bindir}/gnome-contacts
%{_libexecdir}/gnome-contacts/
%{_libexecdir}/gnome-contacts-search-provider
%{_datadir}/applications/org.gnome.Contacts.desktop
%{_datadir}/dbus-1/services/org.gnome.Contacts.service
%{_datadir}/dbus-1/services/org.gnome.Contacts.SearchProvider.service
%{_datadir}/glib-2.0/schemas/org.gnome.Contacts.gschema.xml
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/search-providers
%{_datadir}/gnome-shell/search-providers/org.gnome.Contacts.search-provider.ini
%{_datadir}/icons/hicolor/*/apps/org.gnome.Contacts*.svg
%{_datadir}/metainfo/org.gnome.Contacts.appdata.xml
%{_mandir}/man1/gnome-contacts.1*

%changelog
* Fri Sep 23 2022 Kalev Lember <klember@redhat.com> - 43.0-1
- Update to 43.0

* Wed Sep 14 2022 Kalev Lember <klember@redhat.com> - 43~rc-3
- Backport upstream fix for a crash when editing contacts

* Tue Sep 13 2022 Kalev Lember <klember@redhat.com> - 43~rc-2
- Produce vala debug information

* Tue Sep 06 2022 Kalev Lember <klember@redhat.com> - 43~rc-1
- Update to 43.rc

* Tue Aug 09 2022 Kalev Lember <klember@redhat.com> - 43~beta-1
- Update to 43.beta

* Wed Jul 27 2022 Kalev Lember <klember@redhat.com> - 43~alpha-1
- Update to 43.alpha

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 42.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Kalev Lember <klember@redhat.com> - 42.0-2
- Rebuilt for evolution-data-server soname bump

* Wed Mar 23 2022 David King <amigadave@amigadave.com> - 42.0-1
- Update to 42.0

* Mon Mar 14 2022 David King <amigadave@amigadave.com> - 42~beta-1
- Update to 42.beta

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 42~alpha-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 12 2022 David King <amigadave@amigadave.com> - 42~alpha-1
- Update to 42.alpha

* Wed Sep 29 2021 Kalev Lember <klember@redhat.com> - 41.0-1
- Update to 41.0

* Wed Sep 08 2021 Kalev Lember <klember@redhat.com> - 41~beta-1
- Update to 41.beta

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 40.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 23 2021 Kalev Lember <klember@redhat.com> - 40.0-1
- Update to 40.0
- Drop minimum version requirements on old library versions

* Mon Mar 01 2021 Kalev Lember <klember@redhat.com> - 40~beta-1
- Update to 40.beta

* Fri Feb 19 2021 Kalev Lember <klember@redhat.com> - 40~alpha-1
- Update to 40.alpha

* Tue Feb 16 2021 Kalev Lember <klember@redhat.com> - 3.38.1-4
- Rebuilt for folks soname bump

* Fri Feb 12 2021 Milan Crha <mcrha@redhat.com> - 3.38.1-3
- Rebuilt for evolution-data-server soname version bump

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov  9 2020 Kalev Lember <klember@redhat.com> - 3.38.1-1
- Update to 3.38.1

* Sat Sep 19 2020 Kalev Lember <klember@redhat.com> - 3.38-1
- Update to 3.38

* Mon Aug 24 2020 Kalev Lember <klember@redhat.com> - 3.37.2-1
- Update to 3.37.2

* Mon Aug 17 2020 Kalev Lember <klember@redhat.com> - 3.37.1-1
- Update to 3.37.1

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.36.2-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.36.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 03 2020 Milan Crha <mcrha@redhat.com> - 3.36.2-2
- Rebuilt for evolution-data-server soname version bump

* Mon Jun 22 2020 Kalev Lember <klember@redhat.com> - 3.36.2-1
- Update to 3.36.2

* Sat Apr 25 2020 Kalev Lember <klember@redhat.com> - 3.36.1-1
- Update to 3.36.1

* Tue Apr 14 2020 Kalev Lember <klember@redhat.com> - 3.36-2
- Fix an issue with GNOME Contacts not getting past welcome screen (#1823910)

* Wed Mar 11 2020 Kalev Lember <klember@redhat.com> - 3.36-1
- Update to 3.36

* Mon Feb 03 2020 Kalev Lember <klember@redhat.com> - 3.35.90-1
- Update to 3.35.90

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Kalev Lember <klember@redhat.com> - 3.34.1-2
- Rebuilt for libgnome-desktop soname bump

* Tue Jan 07 2020 Kalev Lember <klember@redhat.com> - 3.34.1-1
- Update to 3.34.1

* Tue Sep 10 2019 Kalev Lember <klember@redhat.com> - 3.34-1
- Update to 3.34

* Wed Sep 04 2019 Kalev Lember <klember@redhat.com> - 3.33.92-1
- Update to 3.33.92

* Tue Aug 20 2019 Kalev Lember <klember@redhat.com> - 3.33.91-1
- Update to 3.33.91

* Sun Jul 28 2019 Kevin Fenzi <kevin@scrye.com> - 3.33.4-1
- Update to 3.33.4.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.33.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 09 2019 Kalev Lember <klember@redhat.com> - 3.33.1-1
- Update to 3.33.1

* Mon May 06 2019 Kalev Lember <klember@redhat.com> - 3.32.1-1
- Update to 3.32.1

* Tue Mar 12 2019 Kalev Lember <klember@redhat.com> - 3.32-1
- Update to 3.32

* Wed Feb 06 2019 Kalev Lember <klember@redhat.com> - 3.31.90-1
- Update to 3.31.90

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 09 2019 Kalev Lember <klember@redhat.com> - 3.31.4-1
- Update to 3.31.4

* Wed Dec 19 2018 Kalev Lember <klember@redhat.com> - 3.30.2-1
- Update to 3.30.2

* Wed Nov 28 2018 Debarshi Ray <rishi@fedoraproject.org> - 3.30.1-3
- Disable Telepathy (RH #1654208)

* Mon Nov 12 2018 Mohan Boddu <mboddu@bhujji.com> - 3.30.1-2
- Rebuilt for evolution-data-server soname bump

* Sat Sep 29 2018 Kalev Lember <klember@redhat.com> - 3.30.1-1
- Update to 3.30.1

* Fri Sep 07 2018 Kalev Lember <klember@redhat.com> - 3.30-1
- Update to 3.30
- Drop old, unneeded BRs

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 08 2018 Kalev Lember <klember@redhat.com> - 3.28.2-1
- Update to 3.28.2

* Fri Apr 13 2018 Kalev Lember <klember@redhat.com> - 3.28.1-1
- Update to 3.28.1

* Mon Mar 12 2018 Kalev Lember <klember@redhat.com> - 3.28.0-1
- Update to 3.28.0

* Mon Mar 05 2018 Kalev Lember <klember@redhat.com> - 3.27.92-1
- Update to 3.27.92
- Switch to the meson build system

* Tue Feb 13 2018 Björn Esser <besser82@fedoraproject.org> - 3.26.1-3
- Rebuild against newer gnome-desktop3 package

* Wed Feb 07 2018 Kalev Lember <klember@redhat.com> - 3.26.1-2
- Rebuilt for evolution-data-server soname bump

* Wed Jan 24 2018 Kalev Lember <klember@redhat.com> - 3.26.1-1
- Update to 3.26.1

* Sat Jan 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.26-2
- Remove obsolete scriptlets

* Mon Sep 11 2017 Kalev Lember <klember@redhat.com> - 3.26-1
- Update to 3.26

* Thu Sep 07 2017 Kalev Lember <klember@redhat.com> - 3.25.92.1-1
- Update to 3.25.92.1

* Mon Jul 31 2017 Kalev Lember <klember@redhat.com> - 3.25.4-1
- Update to 3.25.4

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Oct 25 2016 Milan Crha <mcrha@redhat.com> - 3.22.1-3
- Rebuild for newer evolution-data-server

* Thu Sep 22 2016 Kalev Lember <klember@redhat.com> - 3.22.1-2
- BR vala instead of obsolete vala-tools subpackage

* Wed Sep 21 2016 Kalev Lember <klember@redhat.com> - 3.22.1-1
- Update to 3.22.1
- Drop ancient obsoletes

* Mon Jul 18 2016 Milan Crha <mcrha@redhat.com> - 3.20.0-3
- Rebuild for newer evolution-data-server

* Tue Jun 21 2016 Milan Crha <mcrha@redhat.com> - 3.20.0-2
- Rebuild for newer evolution-data-server

* Tue May 17 2016 Kalev Lember <klember@redhat.com> - 3.20.0-1
- Update to 3.20.0

* Sun Feb 28 2016 David King <amigadave@amigadave.com> - 3.19.91-1
- Update to 3.19.91

* Tue Feb 16 2016 Milan Crha <mcrha@redhat.com> - 3.18.1-4
- Rebuild for newer evolution-data-server

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Kevin Fenzi <kevin@scrye.com> - 3.18.1-2
- Rebuild for new libical

* Thu Nov 12 2015 David King <amigadave@amigadave.com> - 3.18.1-1
- Update to 3.18.1

* Mon Oct 05 2015 David King <amigadave@amigadave.com> - 3.18.0-2
- Fix a crash in the search provider (#1244256)

* Wed Sep 23 2015 Kalev Lember <klember@redhat.com> - 3.18.0-1
- Update to 3.18.0
- Use make_install macro

* Mon Aug 17 2015 Kalev Lember <klember@redhat.com> - 3.16.2-7
- Rebuilt for libcheese soname bump

* Wed Jul 22 2015 Milan Crha <mcrha@redhat.com> - 3.16.2-6
- Rebuild for newer evolution-data-server

* Mon Jun 29 2015 Michael Catanzaro <mcatanzaro@gnome.org> - 3.16.2-5
- Really hopefully fix crashes in the search provider (#1199712)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.16.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Matthias Clasen <mclasen@redhat.com> - 3.16.2-3
- Fix crashes in the search provider (#1199712)

* Tue Apr 28 2015 Milan Crha <mcrha@redhat.com> - 3.16.2-2
- Rebuild for newer evolution-data-server

* Wed Apr 22 2015 David King <amigadave@amigadave.com> - 3.16.2-1
- Update to 3.16.2

* Thu Apr 16 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.1-1
- Update to 3.16.1

* Fri Mar 20 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.0-1
- Update to 3.16.0
- Set minimum required geocode-glib version

* Tue Mar 17 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.92-1
- Update to 3.15.92

* Tue Mar 03 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.91-1
- Update to 3.15.91

* Mon Feb 16 2015 David King <amigadave@amigadave.com> - 3.15.90-1
- Update to 3.15.90
- Use license macro for COPYING

* Tue Jan 20 2015 David King <amigadave@amigadave.com> - 3.15.4-1
- Update to 3.15.4
- Use pkgconfig for BuildRequires
- Update URL
- Build man page
- Validate AppData in check

* Mon Nov 10 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.2-1
- Update to 3.14.2

* Mon Oct 13 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.1-1
- Update to 3.14.1

* Mon Sep 22 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.0-1
- Update to 3.14.0

* Wed Sep 17 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.92-1
- Update to 3.13.92

* Wed Sep 03 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.91-1
- Update to 3.13.91
- Set minimum required gtk3 version

* Mon Aug 18 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.90-1
- Update to 3.13.90

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 31 2014 Milan Crha <mcrha@redhat.com> - 3.13.3-2
- Rebuild against newer evolution-data-server

* Thu Jun 26 2014 Richard Hughes <rhughes@redhat.com> - 3.13.3-1
- Update to 3.13.3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 24 2014 Richard Hughes <rhughes@redhat.com> - 3.12.0-1
- Update to 3.12.0

* Tue Mar 18 2014 Richard Hughes <rhughes@redhat.com> - 3.11.92-1
- Update to 3.11.92

* Wed Mar 05 2014 Richard Hughes <rhughes@redhat.com> - 3.11.91-1
- Update to 3.11.91

* Thu Feb 20 2014 Kalev Lember <kalevlember@gmail.com> - 3.11.90-3
- Rebuilt for cogl soname bump

* Wed Feb 19 2014 Richard Hughes <rhughes@redhat.com> - 3.11.90-2
- Rebuilt for gnome-desktop soname bump

* Mon Feb 17 2014 Richard Hughes <rhughes@redhat.com> - 3.11.90-1
- Update to 3.11.90

* Mon Feb 10 2014 Peter Hutterer <peter.hutterer@redhat.com> - 3.10.1-6
- Rebuild for libevdev soname bump

* Wed Feb 05 2014 Kalev Lember <kalevlember@gmail.com> - 3.10.1-5
- Rebuilt for cogl soname bump

* Mon Feb 03 2014 Milan Crha <mcrha@redhat.com> - 3.10.1-4
- Rebuild against newer evolution-data-server

* Tue Jan 14 2014 Milan Crha <mcrha@redhat.com> - 3.10.1-3
- Rebuild against newer evolution-data-server

* Tue Nov 19 2013 Milan Crha <mcrha@redhat.com> - 3.10.1-2
- Rebuild against newer evolution-data-server

* Mon Oct 28 2013 Richard Hughes <rhughes@redhat.com> - 3.10.1-1
- Update to 3.10.1

* Wed Sep 25 2013 Richard Hughes <rhughes@redhat.com> - 3.10-1
- Update to 3.10

* Wed Sep 18 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.92-1
- Update to 3.9.92
- Include the appdata file

* Tue Sep 03 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.91-1
- Update to 3.9.91

* Thu Aug 22 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.90-1
- Update to 3.9.90

* Mon Aug 19 2013 Adam Williamson <awilliam@redhat.com> - 3.9.5-3
- rebuild for new evolution-data-server

* Fri Aug 09 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.5-2
- Rebuilt for cogl 1.15.4 soname bump

* Mon Aug 05 2013 Debarshi Ray <rishi@fedoraproject.org> - 3.9.5-1
- Update to 3.9.5

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 16 2013 Richard Hughes <rhughes@redhat.com> - 3.9.4-1
- Update to 3.9.4

* Wed Jul 10 2013 Milan Crha <mcrha@redhat.com> - 3.8.2-3
- Rebuild against newer evolution-data-server

* Fri Jun 21 2013 Matthias Clasen <mclasen@redhat.com> - 3.8.2-2
- Don't install ChangeLog

* Tue May 28 2013 Matthias Clasen <mclasen@redhat.com> - 3.8.2-1
- Update to 3.8.2

* Sat May 04 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.1-2
- Rebuild against newer evolution-data-server

* Mon Apr 15 2013 Richard Hughes <rhughes@redhat.com> - 3.8.1-1
- Update to 3.8.1

* Tue Mar 26 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.0-1
- Update to 3.8.0

* Fri Mar  8 2013 Matthias Clasen <mclasen@redhat.com> - 3.7.91-1
- Update to 3.7.91

* Thu Feb 21 2013 Kalev Lember <kalevlember@gmail.com> - 3.7.90-1
- Update to 3.7.90

* Wed Feb 20 2013 Kalev Lember <kalevlember@gmail.com> - 3.7.3-3
- Rebuilt for libgnome-desktop soname bump

* Fri Jan 25 2013 Peter Robinson <pbrobinson@fedoraproject.org> 3.7.3-2
- Rebuild for new cogl

* Fri Dec 21 2012 Kalev Lember <kalevlember@gmail.com> - 3.7.3-1
- Update to 3.7.3

* Tue Nov 20 2012 Milan Crha <mcrha@redhat.com> - 3.6.2-2
- Rebuild against newer evolution-data-server

* Tue Nov 13 2012 Kalev Lember <kalevlember@gmail.com> - 3.6.2-1
- Update to 3.6.2

* Thu Oct 25 2012 Milan Crha <mcrha@redhat.com> - 3.6.1-2
- Rebuild against newer evolution-data-server

* Tue Oct 16 2012 Kalev Lember <kalevlember@gmail.com> - 3.6.1-1
- Update to 3.6.1

* Tue Oct  2 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 3.6.0-2
- Obsolete contacts. RHBZ # 861373
- Cleanup spec, update URL and Source locations

* Tue Sep 25 2012 Richard Hughes <hughsient@gmail.com> - 3.6.0-1
- Update to 3.6.0

* Wed Sep 19 2012 Kalev Lember <kalevlember@gmail.com> - 3.5.92-2
- Rebuilt for new libcheese

* Wed Sep 19 2012 Richard Hughes <hughsient@gmail.com> - 3.5.92-1
- Update to 3.5.92

* Tue Sep 04 2012 Richard Hughes <hughsient@gmail.com> - 3.5.91-1
- Update to 3.5.91

* Tue Aug 28 2012 Matthias Clasen <mclasen@redhat.com> - 3.5.90-2
- Rebuild against new cogl/clutter

* Tue Aug 21 2012 Elad Alfassa <elad@fedoraproject.org> - 3.5.90-1
- New upstream release

* Tue Jul 31 2012 Richard Hughes <hughsient@gmail.com> - 3.5.4.1-1
- Update to 3.5.4.1

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 18 2012 Matthias Clasen <mclasen@redhat.com> - 3.5.3-2
- Rebuild

* Tue Jul 17 2012 Richard Hughes <hughsient@gmail.com> - 3.5.3-1
- Update to 3.5.3

* Mon Jun 25 2012 Richard Hughes <hughsient@gmail.com> - 3.5.2-1
- Update to 3.5.2

* Thu Jun 07 2012 Richard Hughes <hughsient@gmail.com> - 3.5.1-1
- Update to 3.5.1

* Fri May 18 2012 Richard Hughes <hughsient@gmail.com> - 3.4.1-1
- Update to 3.4.1

* Tue Apr 24 2012 Kalev Lember <kalevlember@gmail.com> - 3.4.0-2
- Silence rpm scriptlet output

* Tue Mar 27 2012 Richard Hughes <hughsient@gmail.com> - 3.4.0-1
- Update to 3.4.0

* Wed Mar 21 2012 Kalev Lember <kalevlember@gmail.com> - 3.3.92-1
- Update to 3.3.92

* Tue Mar  6 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.91-1
- Update to 3.3.91

* Sun Feb 26 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.90-1
- Update to 3.3.90

* Tue Feb  7 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.4-1
- Update to 3.3.4

* Tue Jan 17 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.3-1
- Update to 3.3.3

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 20 2011 Matthias Clasen <mclasen@redhat.com> - 3.3.1-1
- Update to 3.3.1

* Thu Nov 24 2011 Tomas Bzatek <tbzatek@redhat.com> - 3.2.2-3
- Rebuilt for new eds

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.2-2
- Rebuilt for glibc bug#747377

* Thu Oct 20 2011 Elad Alfassa <elad@fedoraproject.org> - 3.2.2-1
- Upstream bugfix release 3.2.2
- Fixes RHBZ #743827, #743989

* Tue Oct 18 2011 Elad Alfassa <elad@fedoraproject.org> - 3.2.1-1
- Update to 3.2.1 (Translation updates)

* Tue Sep 27 2011 Elad Alfassa <elad@fedoraproject.org> - 3.2.0.1-1
- New upstream release

* Tue Sep 20 2011 Elad Alfassa <elad@fedoraproject.org> - 0.1.5.2-1
- New upstream release (mainly contact linking support)

* Wed Sep 07 2011 Elad Alfassa <elad@fedoraproject.org> - 0.1.4.1-1
- New upstream release (fix a crash).

* Wed Sep 07 2011 Elad Alfassa <elad@fedoraproject.org> - 0.1.4-1
- New upstream release:
- *Unique application instance support
- *Support browsing for avatar file
- *Support deleting (some) contacts
- *Support linking contacts
- *Support for new fields:
-  * nickname
-  * birthday (readonly)
-  * company/title/etc (readonly)
- * Lots of small UI tweaks

* Tue Aug 30 2011 Elad Alfassa <elad@fedoraproject.org> - 0.1.3-1
- New upstream version

* Mon Aug 22 2011 Brian Pepple <bpepple@fedoraproject.org> - 0.1.2-2
- Rebuld for eds.

* Tue Aug 16 2011 Elad Alfassa <elad@fedoraproject.org> - 0.1.2-0
- New upstream release

* Sun Aug 14 2011 Elad Alfassa <elad@fedoraproject.org> - 0.1.1-2
- Rebuilt to fix broken libfolks dependencies

* Tue Jul 05 2011 Elad Alfassa <elad@fedoraproject.org> - 0.1.1-1
- Update to 0.1.1

* Sun Jun 19 2011 Elad Alfassa <elad@fedoraproject.org> - 0.1.0-3
- Fix unowned directory

* Sun Jun 19 2011 Elad Alfassa <elad@fedoraproject.org> - 0.1.0-2
- Add missing doc files.
- Use package names instead of pkgconfig() in BuildRequires

* Mon Jun 13 2011 Elad Alfassa <elad@fedoraproject.org> - 0.1.0-1
- Initial packaging


