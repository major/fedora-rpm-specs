%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           seahorse
Version:        47.0.1
Release:        2%{?dist}
Summary:        A GNOME application for managing encryption keys

# seahorse is GPLv2+
# libcryptui is LGPLv2+
License:        GPL-2.0-or-later AND LGPL-2.0-or-later AND CC-BY-SA-3.0
URL:            https://wiki.gnome.org/Apps/Seahorse
Source:         https://download.gnome.org/sources/%{name}/47/%{name}-%{tarball_version}.tar.xz

BuildRequires:  pkgconfig(avahi-client)
BuildRequires:  pkgconfig(avahi-glib)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gck-1)
BuildRequires:  pkgconfig(gcr-3)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libsecret-unstable)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(pwquality)
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-style-xsl
BuildRequires:  gettext
BuildRequires:  gpgme-devel >= 1.0
BuildRequires:  gnupg2
BuildRequires:  itstool
BuildRequires:  libSM-devel
BuildRequires:  meson
BuildRequires:  openldap-devel
BuildRequires:  openssh-clients
BuildRequires:  vala
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/xsltproc

# https://bugzilla.redhat.com/show_bug.cgi?id=474419
# https://bugzilla.redhat.com/show_bug.cgi?id=587328
Requires:       pinentry-gui

%description
Seahorse is a graphical interface for managing and using encryption keys.
It also integrates with nautilus, gedit and other places for encryption
operations.  It is a keyring manager.


%prep
%autosetup -p1 -n %{name}-%{tarball_version}

%build
%meson -Dmanpage=true
%meson_build

%install
%meson_install

%find_lang seahorse --with-gnome --all-name

%check
appstream-util validate-relax --nonet $RPM_BUILD_ROOT/%{_metainfodir}/org.gnome.seahorse.Application.appdata.xml
desktop-file-validate ${RPM_BUILD_ROOT}%{_datadir}/applications/org.gnome.seahorse.Application.desktop

%files -f %{name}.lang
%license COPYING*
%doc NEWS README.md
%{_bindir}/seahorse
%{_libexecdir}/seahorse/
%{_datadir}/applications/org.gnome.seahorse.Application.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.seahorse.Application.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.seahorse.Application.svg
%{_datadir}/dbus-1/services/org.gnome.seahorse.Application.service
%{_datadir}/glib-2.0/schemas/org.gnome.seahorse*.gschema.xml
%dir %{_datadir}/gnome-shell/
%dir %{_datadir}/gnome-shell/search-providers/
%{_datadir}/gnome-shell/search-providers/seahorse-search-provider.ini
%{_datadir}/seahorse/
%{_mandir}/man1/seahorse.1*
%{_metainfodir}/org.gnome.seahorse.Application.appdata.xml

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 47.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Sep 28 2024 David King <amigadave@amigadave.com> - 47.0.1-1
- Update to 47.0.1

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 43.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon May 06 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 43.0-6
- Add upstream patches for GCC 14

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 43.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 43.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 14 2023 Florian Weimer <fweimer@redhat.com> - 43.0-3
- Port to C99

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 43.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Oct 27 2022 David King <amigadave@amigadave.com> - 43.0-1
- Update to 43.0

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 42.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 23 2022 David King <amigadave@amigadave.com> - 42.0-1
- Update to 42.0

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 41.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 29 2021 Kalev Lember <klember@redhat.com> - 41.0-1
- Update to 41.0

* Wed Sep 08 2021 Kalev Lember <klember@redhat.com> - 41~beta-1
- Update to 41.beta

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 40.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Apr 13 2021 Kalev Lember <klember@redhat.com> - 40.0-1
- Update to 40.0

* Fri Feb 19 2021 Kalev Lember <klember@redhat.com> - 40~alpha-1
- Update to 40.alpha

* Tue Feb 16 2021 Kalev Lember <klember@redhat.com> - 3.38.1-1
- Update to 3.38.1

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov  9 2020 Kalev Lember <klember@redhat.com> - 3.38.0.1-1
- Update to 3.38.0.1
- Switch to libhandy1

* Mon Aug 24 2020 Kalev Lember <klember@redhat.com> - 3.37.2-1
- Update to 3.37.2

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.37.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Kalev Lember <klember@redhat.com> - 3.37.1-1
- Update to 3.37.1

* Mon Jun 22 2020 Kalev Lember <klember@redhat.com> - 3.36.2-1
- Update to 3.36.2

* Wed Mar 11 2020 Kalev Lember <klember@redhat.com> - 3.36-1
- Update to 3.36

* Tue Feb 18 2020 Kalev Lember <klember@redhat.com> - 3.35.91-1
- Update to 3.35.91

* Mon Feb 03 2020 Kalev Lember <klember@redhat.com> - 3.35.90-1
- Update to 3.35.90

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.35.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 10 2020 Kalev Lember <klember@redhat.com> - 3.35.1-1
- Update to 3.35.1

* Tue Jan 07 2020 Kalev Lember <klember@redhat.com> - 3.34.1-1
- Update to 3.34.1

* Tue Oct 01 2019 Kalev Lember <klember@redhat.com> - 3.34-1
- Update to 3.34

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.32.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 17 2019 Kalev Lember <klember@redhat.com> - 3.32.2-1
- Update to 3.32.2

* Mon May 06 2019 Kalev Lember <klember@redhat.com> - 3.32.1-1
- Update to 3.32.1

* Tue Mar 12 2019 Kalev Lember <klember@redhat.com> - 3.32-1
- Update to 3.32

* Tue Feb 19 2019 Kalev Lember <klember@redhat.com> - 3.31.91-2
- Rebuilt against fixed atk (#1626575)

* Tue Feb 19 2019 Kalev Lember <klember@redhat.com> - 3.31.91-1
- Update to 3.31.91

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 09 2019 Kalev Lember <klember@redhat.com> - 3.31.1-1
- Update to 3.31.1

* Tue Dec 18 2018 Kalev Lember <klember@redhat.com> - 3.30.1.1-1
- Update to 3.30.1.1

* Fri Sep 07 2018 Kalev Lember <klember@redhat.com> - 3.30-1
- Update to 3.30
- Switch to the meson build system

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.20.0-8
- Remove unneeded ldconfig

* Fri Jan 05 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.20.0-7
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 10 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 3.20.0-3
- Rebuild for gpgme 1.18

* Fri Sep 02 2016 Kalev Lember <klember@redhat.com> - 3.20.0-2
- Drop old gnome-keyring-manager obsoletes
- Don't set group tags

* Fri Mar 25 2016 Kalev Lember <klember@redhat.com> - 3.20.0-1
- Update to 3.20.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Kalev Lember <klember@redhat.com> - 3.19.4-1
- Update to 3.19.4

* Mon Sep 28 2015 Kalev Lember <klember@redhat.com> - 3.18.0-2
- Build with gnupg2 support

* Mon Sep 28 2015 Kalev Lember <klember@redhat.com> - 3.18.0-1
- Update to 3.18.0

* Tue Sep 15 2015 Richard Hughes <rhughes@redhat.com> - 3.17.4-1
- Update to 3.17.4

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 12 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.0-1
- Update to 3.16.0

* Tue Mar 17 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.92-1
- Update to 3.15.92

* Thu Feb 26 2015 David King <amigadave@amigadave.com> - 3.15.90-1
- Update to 3.15.90
- Update URL
- Use license macro for COPYING and COPYING.LIB
- Use pkgconfig for BuildRequires
- Update man page glob in files section
- Validate AppData in check

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 3.14.0-4
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Thu Nov 20 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.0-3
- Fix SSH key generation (#1163660)

* Sat Oct 25 2014 Stef Walter <stefw@redhat.com> - 3.14.0-2
- Seahorse is not compatible with gnupg2 for now due to incompatible
  upstream changes.

* Tue Sep 23 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.0-1
- Update to 3.14.0
- Drop last remnants of GConf schema handling

* Sat Sep 20 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.2-7
- Update mime scriptlets

* Wed Aug 27 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.2-6
- Backport a fix for a search provider crash

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 27 2014 Rex Dieter <rdieter@fedoraproject.org> 3.12.2-4
- drop needless scriptlet deps, %%postun: update-mime-database only on removal

* Fri Jun 27 2014 Bastien Nocera <bnocera@redhat.com> 3.12.2-3
- Don't run update-mime-database in post, we don't ship mime XML
  files anymore.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 15 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.2-1
- Update to 3.12.2

* Sun Mar 23 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.0-1
- Update to 3.12.0

* Mon Mar 17 2014 Richard Hughes <rhughes@redhat.com> - 3.11.92-1
- Update to 3.11.92

* Sat Mar 08 2014 Richard Hughes <rhughes@redhat.com> - 3.11.91-1
- Update to 3.11.91

* Mon Jan 13 2014 Richard Hughes <rhughes@redhat.com> - 3.10.2-1
- Update to 3.10.2

* Tue Oct 29 2013 Richard Hughes <rhughes@redhat.com> - 3.10.1-1
- Update to 3.10.1

* Wed Sep 25 2013 Kalev Lember <kalevlember@gmail.com> - 3.10.0-1
- Update to 3.10.0

* Tue Sep 03 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.91-1
- Update to 3.9.91

* Fri Aug 30 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.90-2
- Obsolete retired seahorse-plugins

* Wed Aug 28 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.90-1
- Update to 3.9.90

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat May 04 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.1-1
- Update to 3.9.1

* Tue Apr 16 2013 Richard Hughes <rhughes@redhat.com> - 3.8.1-1
- Update to 3.8.1

* Tue Mar 26 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.0-1
- Update to 3.8.0

* Fri Mar  8 2013 Matthias Clasen <mclasen@redhat.com> 0- 3.7.91-1
- Update to 3.7.91

* Wed Feb 06 2013 Kalev Lember <kalevlember@gmail.com> - 3.7.5-1
- Update to 3.7.5

* Thu Jan 03 2013 Debarshi Ray <rishi@fedoraproject.org> - 3.7.2-1
- Update to 3.7.2

* Fri Nov 09 2012 Kalev Lember <kalevlember@gmail.com> - 3.7.1-1
- Update to 3.7.1

* Tue Oct 16 2012 Kalev Lember <kalevlember@gmail.com> - 3.6.1-1
- Update to 3.6.1

* Wed Sep 26 2012 Matthias Clasen <mclasen@redhat.com> - 3.6.0-1
- Update to 3.6.0

* Wed Sep 19 2012 Richard Hughes <hughsient@gmail.com> - 3.5.92-1
- Update to 3.5.92

* Tue Sep 04 2012 Richard Hughes <hughsient@gmail.com> - 3.5.91-1
- Update to 3.5.91

* Tue Aug 21 2012 Richard Hughes <hughsient@gmail.com> - 3.5.90-1
- Update to 3.5.90

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 17 2012 Richard Hughes <hughsient@gmail.com> - 3.5.4-1
- Update to 3.5.4

* Mon Apr 16 2012 Richard Hughes <hughsient@gmail.com> - 3.4.1-1
- Update to 3.4.1

* Thu Apr 12 2012 Kalev Lember <kalevlember@gmail.com> - 3.4.0-2
- Added self-obsoletes to assist with seahorse-sharing package split

* Mon Mar 26 2012 Debarshi Ray <rishi@fedoraproject.org> - 3.4.0-1
- Update to 3.4.0

* Wed Mar 21 2012 Kalev Lember <kalevlember@gmail.com> - 3.3.92-1
- Update to 3.3.92

* Thu Mar 15 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.91-1
- Update to 3.3.91

* Tue Feb 28 2012 Ray Strode <rstrode@redhat.com> 3.3.5-2
- Drop fedora- vendor prefix

* Tue Feb  7 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.5-1
- Update to 3.3.5

* Tue Jan 17 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.4-1
- Update to 3.3.4

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 21 2011 Matthias Clasen <mclasen@redhat.com> - 3.3.3-1
- Update to 3.3.3

* Wed Nov  2 2011 Matthias Clasen <mclasen@redhat.com> - 3.3.1-1
- Update to 3.3.1

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-2
- Rebuilt for glibc bug#747377

* Wed Oct 19 2011 Matthias Clasen <mclasen@redhat.com> - 3.2.1-1
- Update to 3.2.1

* Tue Sep 27 2011 Ray <rstrode@redhat.com> - 3.2.0-1
- Update to 3.2.0

* Tue Sep 20 2011 Kalev Lember <kalevlember@gmail.com> 3.1.92-1
- Update to 3.1.92

* Wed Sep 07 2011 Kalev Lember <kalevlember@gmail.com> 3.1.91-1
- Update to 3.1.91

* Wed Aug 31 2011 Kalev Lember <kalevlember@gmail.com> 3.1.90-1
- Update to 3.1.90
- Remove and obsolete seahorse-devel
- Switch to gsettings and obsolete the gconf schema

* Mon Jul 25 2011 Matthew Barnes <mbarnes@redhat.com> 3.1.4-1
- Update to 3.1.4

* Mon May  9 2011 Tomas Bzatek <tbzatek@redhat.com> 3.1.1-1
- Update to 3.1.1

* Mon Apr 25 2011 Matthias Clasen <mclasen@redhat.com> 3.0.1-1
- Update to 3.0.1

* Thu Apr  7 2011 Christopher Aillon <caillon@redhat.com> 3.0.0-1
- Update to 3.0.0

* Fri Mar 25 2011 Matthias Clasen <mclasen@redhat.com> 2.91.93-1
- Update to 2.91.93

* Mon Mar 21 2011 Matthias Clasen <mclasen@redhat.com> 2.91.92-1
- Update to 2.91.92

* Tue Mar  8 2011 Matthias Clasen <mclasen@redhat.com> 2.91.91-1
- Update to 2.91.91

* Fri Feb 11 2011 Matthias Clasen <mclasen@redhat.com> 2.91.4-5
- Rebuild against newer gtk

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.91.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb  2 2011 Matthias Clasen <mclasen@redhat.com> 2.91.4-3
- Rebuild against newer gtk

* Sun Jan  9 2011 Matthias Clasen <mclasen@redhat.com> 2.91.4-2
- Rebuild against newer gtk3

* Mon Jan  3 2011 Tomas Bzatek <tbzatek@redhat.com> 2.91.4-1
- Update to 2.91.4

* Fri Dec  3 2010 Matthias Clasen <mclasen@redhat.com> 2.91.2-2
- Rebuild against new gtk

* Tue Nov  9 2010 Tomas Bzatek <tbzatek@redhat.com> 2.91.2-1
- Update to 2.91.2

* Wed Nov  3 2010 Matthias Clasen <mclasen@redhat.com> 2.91.2-0.1.gitc548f3b
- git snapshot
- build against libnotify 0.7.0

* Tue Nov  2 2010 Matthias Clasen <mclasen@redhat.com> 2.91.1.1-1
- Update to 2.91.1.1

* Mon Oct 18 2010 Tomas Bzatek <tbzatek@redhat.com> 2.91.1-1
- Update to 2.91.1

* Wed Sep 29 2010 Tomas Bzatek <tbzatek@redhat.com> 2.32.0-1
- Update to 2.32.0

* Tue Sep 21 2010 Matthias Clasen <mclasen@redhat.com> - 2.31.91-2
- Rebuild against newer gobject-introspection

* Tue Aug 31 2010 Matthias Clasen <mclasen@redhat.com> - 2.31.91-1
- Update to 2.31.91

* Thu Jul 15 2010 Colin Walters <walters@verbum.org> - 2.30.1-3
- Rebuild with new gobject-introspection

* Tue May 04 2010 Rex Dieter <rdieter@fedoraproject.org> 2.30.1-2
- Requires: pinentry-gui (#587328)

* Tue Apr 27 2010 Tomas Bzatek <tbzatek@redhat.com> 2.30.1-1
- Update to 2.30.1

* Mon Apr 19 2010 Rahul Sundaram <sundaram@fedoraproject.org> 2.30.0-2
- Fix description to mention keyring manager
- Resolves rhbz#536945

* Tue Mar 30 2010 Matthias Clasen <mclasen@redhat.com> 2.30.0-1
- Update to 2.30.0

* Mon Feb 22 2010 Tomas Bzatek <tbzatek@redhat.com> 2.29.91-1
- Update to 2.29.91

* Tue Feb  9 2010 Tomas Bzatek <tbzatek@redhat.com> 2.29.90-1
- Update to 2.29.90
- Removed daemon autostart file (upstream)

* Fri Jan  8 2010 Tomas Bzatek <tbzatek@redhat.com> 2.29.4-2
- Fix bad usage of g_strconcat: missing NULL (#553647)

* Thu Jan  7 2010 Tomas Bzatek <tbzatek@redhat.com> 2.29.4-1
- Update to 2.29.4

* Mon Dec 14 2009 Matthias Clasen <mclasen@redhat.com> 2.29.3-2
- Fix a wrong use of gdk_property_get that can lead to crashes

* Mon Nov 30 2009 Tomas Bzatek <tbzatek@redhat.com> 2.29.3-1
- Update to 2.29.3

* Mon Nov  2 2009 Tomas Bzatek <tbzatek@redhat.com> 2.29.1-1
- Update to 2.29.1

* Tue Sep 22 2009 Tomas Bzatek <tbzatek@redhat.com> 2.28.0-1
- Update to 2.28.0

* Mon Sep 14 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.92-1
- Update to 2.27.92

* Wed Aug 26 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.90-2
- Make seahorse respect the button-images setting

* Tue Aug 11 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.90-1
- Update to 2.27.90

* Thu Aug  6 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.5-2
- Bring the password tab back

* Tue Jul 28 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.5-1
- Update to 2.27.5

* Mon Jul 27 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.1-4
- Drop unneeded direct deps

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.27.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun  1 2009 Tomas Bzatek <tbzatek@redhat.com> 2.27.1-2
- Require pinentry-gtk (#474419)

* Mon May  4 2009 Tomas Bzatek <tbzatek@redhat.com> 2.27.1-1
- Update to 2.27.1

* Sun Apr 12 2009 Matthias Clasen <mclasen@redhat.com> 2.26.1-1
- Update to 2.26.1
- See http://download.gnome.org/sources/seahorse/2.26/seahorse-2.26.1.news

* Fri Apr 10 2009 Matthias Clasen <mclasen@redhat.com> 2.26.0-2
- Fix directory ownership

* Mon Mar 16 2009 Tomas Bzatek <tbzatek@redhat.com> 2.26.0-1
- Update to 2.26.0

* Mon Mar  2 2009 Tomas Bzatek <tbzatek@redhat.com> 2.25.92-1
- Update to 2.25.92

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.25.91-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb 14 2009 Matthias Clasen <mclasen@redhat.com> 2.25.91-1
- Update to 2.25.91

* Tue Feb  3 2009 Matthias Clasen <mclasen@redhat.com> 2.25.90-1
- Update to 2.25.90

* Wed Jan  7 2009 Matthias Clasen <mclasen@redhat.com> 2.25.4-1
- Update to 2.25.4

* Mon Dec 22 2008 Tomas Bzatek <tbzatek@redhat.com> 2.25.3-1
- Update to 2.25.3

* Tue Dec  2 2008 Matthias Clasen <mclasen@redhat.com> 2.25.1-3
- Rebuild for pkg-config provides

* Mon Dec  1 2008 Tomas Bzatek <tbzatek@redhat.com> 2.25.1-2
- Mark Seahorse as an official replacement for gnome-keyring-manager

* Thu Nov 13 2008 Matthias Clasen <mclasen@redhat.com> 2.25.1-1
- Update to 2.25.1

* Sun Oct 19 2008 Matthias Clasen <mclasen@redhat.com> 2.24.1-1
- Update to 2.24.1

* Thu Oct  9 2008 Matthias Clasen <mclasen@redhat.com> 2.24.0-3
- Save some space

* Sun Sep 21 2008 Matthias Clasen <mclasen@redhat.com> 2.24.0-2
- Update to 2.24.0

* Sun Sep  7 2008 Matthias Clasen <mclasen@redhat.com> 2.23.92-1
- Update to 2.23.92

* Thu Sep  4 2008 Matthias Clasen <mclasen@redhat.com> 2.23.91-1
- Update to 2.23.91

* Sat Aug 30 2008 Michel Salim <salimma@fedoraproject.org> 2.23.90-2
- Patch configure to detect gpg2 binary

* Sat Aug 23 2008 Matthias Clasen <mclasen@redhat.com> 2.23.90-1
- Update to 2.23.90

* Tue Aug  5 2008 Matthias Clasen <mclasen@redhat.com> 2.23.6-1
- Update to 2.23.6
- Split off a -devel package

* Tue Jul 22 2008 Matthias Clasen <mclasen@redhat.com> 2.23.5-1
- Update to 2.23.5

* Mon Apr  7 2008 Matthias Clasen <mclasen@redhat.com> 2.22.1-1
- Update to 2.22.1

* Mon Mar 10 2008 Matthias Clasen <mclasen@redhat.com> 2.22.0-1
- Update to 2.22.0

* Tue Feb 26 2008 Matthias Clasen <mclasen@redhat.com> 2.21.92-1
- Update to 2.21.92

* Fri Feb 15 2008 Matthias Clasen <mclasen@redhat.com> 2.21.90-2
- Rebuild

* Tue Jan 29 2008 Seth Vidal <skvidal at fedoraproject.org> 2.21.90-1
- 2.21.90
- rebuild for new libsoup


* Mon Jan  7 2008 Seth Vidal <skvidal at fedoraproject.org> 2.21.4-2
- drop in seahorse-agent.sh to xinit - closes bug 427466 but will mean
  that seahorse agent will start if it is installed - even on kde or xfce
  desktops :(

* Thu Jan  3 2008 Seth Vidal <skvidal at fedoraproject.org> 2.21.4-1
- upgrade to 2.21.4


* Sat Dec  1 2007 Matt Domsch <mdomsch at fedoraproject.org> 2.21.3-1
- upgrade to 2.21.3
- enable avahi integration
- rpmlint cleanups: remove rpath, unneeded .so, tag config files

* Wed Aug 22 2007 Seth Vidal <skvidal at fedoraproject.org>
- fix license tag
- rebuild for fun!

* Fri Jul 20 2007 Seth Vidal <skvidal at fedoraproject.org>
- disable gedit plugin in rawhide, for now :(

* Tue Jun 26 2007 Seth Vidal <skvidal at fedoraproject.org>
- update to 1.0.1

* Sun Aug 13 2006 Seth Vidal <skvidal at linux.duke.edu>
- re-enable gedit
- update to 0.8.1

* Tue Mar  7 2006 Seth Vidal <skvidal at linux.duke.edu>
- added openldap-devel buildreq to hopefully close bug # 184124

* Thu Feb 23 2006 Seth Vidal <skvidal at linux.duke.edu>
- Patch from John Thacker for rh bug #182694 


* Mon Jan 16 2006 Seth Vidal <skvidal at linux.duke.edu> - 0.8-2
- added configure patch for it to build
- disable gedit plugins until seahorse gets fixed to work with gedit 2.13+

* Wed Oct 26 2005 Seth Vidal <skvidal@phy.duke.edu> - 0.8-1
- 0.8

* Thu Jul 28 2005 Seth Vidal <skvidal@phy.duke.edu> - 0.7.9-1
- 0.7.9

* Wed May 25 2005 Jeremy Katz <katzj@redhat.com> - 0.7.7-3
- make sure all files are included
- BR nautilus-devel

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 0.7.7-2
- rebuild on all arches

* Thu May  5 2005 Seth Vidal <skvidal@phy.duke.edu> 0.7.7-1
- 0.7.7

* Tue Apr 19 2005 Seth Vidal <skvidal at phy.duke.edu> 0.7.6-4
- something innocuous to test on

* Wed Apr  6 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Fri Feb 25 2005 Phillip Compton <pcompton[AT]proteinmedia.com> 0.7.6-2
- desktop entry fixes.

* Fri Feb 25 2005 Phillip Compton <pcompton[AT]proteinmedia.com> 0.7.6-1
- 0.7.6.

* Sun Nov 09 2003 Phillip Compton <pcompton[AT]proteinmedia.com> 0:0.7.3-0.fdr.5
- BuildReq scrollkeeper.

* Wed Oct 22 2003 Phillip Compton <pcompton[AT]proteinmedia.com> 0:0.7.3-0.fdr.4
- Uncommented .la removal.

* Sun Sep 21 2003 Phillip Compton <pcompton[AT]proteinmedia.com> 0:0.7.3-0.fdr.3
- Grabbed new copy os source from upstream.
- Fixed path on Source0, to allow direct download.
- BuildReq desktop-file-utils.

* Sun Sep 21 2003 Phillip Compton <pcompton[AT]proteinmedia.com> 0:0.7.3-0.fdr.2
- Fixed file permission on source tarball.
- Fixed Group.
- Removed aesthetic comments.
- Brought more in line with current spec template.

* Sun Aug 17 2003 Phillip Compton <pcompton[AT]proteinmedia.com> 0:0.7.3-0.fdr.1
- Fedorification.
- Added path to Source0.
- Added URL.
- buildroot -> RPM_BUILD_ROOT.
- BuildReq libgnomeui-devel, eel2-devel, gpgme03-devel.
- BuildReq gettext.
- post Req GConf2.
- post/postun Req scrollkeeper.
- .la/.a removal.
- cosmetic changes.

* Fri May 02 2003 Matthew Hall <matt@ecsc.co.uk> 0.7.3-1
- 0.7.3 Release

* Wed Apr 23 2003 Matthew Hall <matt@ecsc.co.uk> 0.7.1-3
- Rebuilt against gpgme 0.3.15

* Sat Apr 12 2003 Matthew Hall <matt@ecsc.co.uk> 0.7.1-2
- RedHat 9 Rebuild

* Sun Jan 26 2003 Matthew Hall <matt@ecsc.co.uk>
- New Spec File

