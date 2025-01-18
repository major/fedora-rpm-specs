Name:           deja-dup
Version:        46.1
Release:        4%{?dist}
Summary:        Simple backup tool and frontend for duplicity

License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/World/deja-dup
Source0:        https://gitlab.gnome.org/World/deja-dup/-/archive/%{version}/deja-dup-%{version}.tar.bz2

BuildRequires:  meson
BuildRequires:  gettext desktop-file-utils intltool
BuildRequires:  yelp-tools pango-devel cairo-devel
BuildRequires:  libvala-devel vala
BuildRequires:  libtool glib2-devel libnotify-devel
BuildRequires:  libpeas-devel
BuildRequires:  libsecret-devel
BuildRequires:  gtk4-devel > 4.5
BuildRequires:  itstool
BuildRequires:  libappstream-glib
BuildRequires:  gnome-online-accounts-devel
BuildRequires:  libgpg-error-devel
BuildRequires:  dbus-daemon
BuildRequires:  json-glib-devel libsoup3-devel
BuildRequires:  libhandy1-devel
BuildRequires:  libadwaita-devel
Requires:       duplicity >= 0.6.23
Requires:       python3-gobject-base
Requires:       python3-PyDrive2
Requires:       rclone
Recommends:     gvfs-fuse
Recommends:     restic

%description
Déjà Dup is a simple backup tool. It hides the complexity of doing backups the
'right way' (encrypted, off-site, and regular) and uses duplicity as the
backend.

Features: 
 • Support for local, remote, or consumer cloud backup locations (Google Drive, etc)
 • Securely encrypts and compresses your data
 • Incrementally backs up, letting you restore from any particular backup
 • Schedules regular backups
 • Integrates well into your GNOME desktop

%prep
%autosetup -p1

%build
%meson -Denable_restic=true
%meson_build

%install
%meson_install
rm -f %{buildroot}/%{_libdir}/deja-dup/*.la

desktop-file-validate %{buildroot}/%{_datadir}/applications/org.gnome.DejaDup.desktop
desktop-file-validate %{buildroot}/%{_sysconfdir}/xdg/autostart/org.gnome.DejaDup.Monitor.desktop

appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*.metainfo.xml

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%license LICENSES/
%doc NEWS.md README.md
%{_bindir}/deja-dup
%{_mandir}/man1/deja-dup.1*
%{_datadir}/glib-2.0/schemas/org.gnome.DejaDup.gschema.xml
%{_sysconfdir}/xdg/autostart/org.gnome.DejaDup.Monitor.desktop
%{_libdir}/deja-dup/
%{_libexecdir}/deja-dup/
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/org.gnome.DejaDup*
%{_datadir}/dbus-1/services/org.gnome.DejaDup.service
%{_datadir}/metainfo/org.gnome.DejaDup.metainfo.xml
%{_datadir}/help/*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 46.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Oct 21 2024 Gwyn Ciesla <gwync@protonmail.com> - 46.1-3
- Require rclone

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 46.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 24 2024 Gwyn Ciesla <gwync@protonmail.com> - 46.1-1
- 46.1

* Mon May 20 2024 Gwyn Ciesla <gwync@protonmail.com> - 45.2-5
- Patch for 2281457

* Mon Apr 29 2024 Gwyn Ciesla <gwync@protonmail.com> - 45.2-4
- Patch for 2276705

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 45.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 45.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Dec 22 2023 Gwyn Ciesla <gwync@protonmail.com> - 45.2-1
- 45.2

* Fri Sep 22 2023 Gwyn Ciesla <gwync@protonmail.com> - 45.1-1
- 45.1

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 44.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon May 22 2023 Gwyn Ciesla <gwync@protonmail.com> - 44.2-1
- 44.2

* Wed Apr 26 2023 Gwyn Ciesla <gwync@protonmail.com> - 44.1-2
- Enable restic support.

* Fri Mar 24 2023 Gwyn Ciesla <gwync@protonmail.com> - 44.1-1
- 44.1

* Wed Mar 01 2023 Gwyn Ciesla <gwync@protonmail.com> - 44.0-3
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 44.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 28 2022 Gwyn Ciesla <gwync@protonmail.com> - 44.0-1
- 44.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 43.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 24 2022 Gwyn Ciesla <gwync@protonmail.com> - 43.4-1
- 43.4

* Tue May 17 2022 Gwyn Ciesla <gwync@protonmail.com> - 43.3-1
- 43.3

* Sun Feb 06 2022 Gwyn Ciesla <gwync@protonmail.com> - 43.2-1
- 43.2

* Wed Jan 05 2022 Gwyn Ciesla <gwync@protonmail.com> - 43.1-1
- 43.1

* Tue Jan 04 2022 Gwyn Ciesla <gwync@protonmail.com> - 43.0-1
- 43.0

* Wed Nov 10 2021 Gwyn Ciesla <gwync@protonmail.com> - 42.8-2
- PyDrive->PyDrive2

* Thu Aug 12 2021 Gwyn Ciesla <gwync@protonmail.com> - 42.8-1
- 42.8

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 42.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Mar 26 2021 Kalev Lember <klember@redhat.com> - 42.7-3
- Drop unnecessary requires on dconf

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 42.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 2021 Gwyn Ciesla <gwync@protonmail.com> - 42.7-1
- 42.7

* Mon Nov 23 2020 Gwyn Ciesla <gwync@protonmail.com> - 42.6-1
- 42.6

* Thu Oct 22 2020 Gwyn Ciesla <gwync@protonmail.com> - 42.5-1
- 42.5

* Wed Sep 23 2020 Gwyn Ciesla <gwync@protonmail.com> - 42.4-2
- Explicitly require python3-PyDrive, BZ 1881990.

* Mon Sep 14 2020 Gwyn Ciesla <gwync@protonmail.com> - 42.4-1
- 42.4

* Wed Sep 09 2020 Gwyn Ciesla <gwync@protonmail.com> - 42.3-1
- 42.3

* Tue Aug 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 42.2-1
- 42.2

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 42.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 15 2020 Gwyn Ciesla <gwync@protonmail.com> - 42.1-1
- 42.1

* Wed Jun 24 2020 Gwyn Ciesla <gwync@protonmail.com> - 42.0-1
- 42.0

* Mon Jun 22 2020 Gwyn Ciesla <gwync@protonmail.com> - 41.3-1
- 41.3

* Thu May 28 2020 Gwyn Ciesla <gwync@protonmail.com> - 41.1-1
- 41.1
- nautilus extension dropped upstream.

* Wed May 20 2020 Gwyn Ciesla <gwync@protonmail.com> - 41.0-1
- 41.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 40.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 09 2019 Gwyn Ciesla <gwync@protonmail.com> - 40.6-1
- 40.6

* Mon Nov 25 2019 Gwyn Ciesla <gwync@protonmail.com> - 40.5-1
- 40.5

* Fri Nov 15 2019 Gwyn Ciesla <gwync@protonmail.com> - 40.4-1
- 40.4

* Thu Nov 14 2019 Gwyn Ciesla <gwync@protonmail.com> - 40.3-1
- 40.3

* Wed Oct 23 2019 Gwyn Ciesla <gwync@protonmail.com> - 40.2-1
- 40.2

* Fri Aug 09 2019 Gwyn Ciesla <gwync@protonmail.com> - 40.1-4
- Require Python 3 modules.

* Wed Jul 31 2019 Gwyn Ciesla <gwync@protonmail.com> - 40.1-3
- Upstream patch to fix build with recent vala.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 40.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 16 2019 Gwyn Ciesla <gwync@protonmail.com> - 40.1-1
- 40.1

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 40.0-2
- Rebuild with Meson fix for #1699099

* Mon Apr 15 2019 Gwyn Ciesla <gwync@protonmail.com> - 40.0-1
- 40.0

* Fri Apr 05 2019 Gwyn Ciesla <gwync@protonmail.com> - 39.1-1
- 39.1

* Fri Mar 29 2019 Gwyn Ciesla <gwync@protonmail.com> - 39.0-1
- 39.0

* Mon Feb 25 2019 Gwyn Ciesla <gwync@protonmail.com> - 38.4-1
- 38.4

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 38.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 13 2018 Gwyn Ciesla <limburgher@gmail.com> - 38.1-1
- 38.1

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 38.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 10 2018 Gwyn Ciesla <limburgher@gmail.com> - 38.0-2
- Added weak dep on gvfs-fuse.

* Tue Apr 10 2018 Gwyn Ciesla <limburgher@gmail.com> - 38.0-1
- 38.0

* Mon Apr 09 2018 Michal Schmidt <mschmidt@redhat.com> - 37.1-4
- Remove service's ulimit. It conflicts with WebKit's Gigacage.
- Fixes rhbz#1556743.

* Thu Mar 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 37.1-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 37.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 04 2018 Gwyn Ciesla <limburgher@gmail.com> - 37.1-1
- 37.1

* Mon Nov 20 2017 Gwyn Ciesla <limburgher@gmail.com> - 37.0-1
- 37.0

* Mon Oct 23 2017 Gwyn Ciesla <limburgher@gmail.com> - 36.3-1
- 36.3

* Wed Oct 04 2017 Gwyn Ciesla <limburgher@gmail.com> - 36.2-1
- 36.2

* Fri Sep 15 2017 Gwyn Ciesla <limburgher@gmail.com> - 36.1-1
- 36.1

* Mon Sep 11 2017 Gwyn Ciesla <limburgher@gmail.com> - 36.0-1
- 36.0

* Fri Sep 01 2017 Gwyn Ciesla <limburgher@gmail.com> - 35.6-1
- 35.6

* Wed Aug 23 2017 Gwyn Ciesla <limburgher@gmail.com> - 35.5-1
- 35.5

* Wed Aug 09 2017 Gwyn Ciesla <limburgher@gmail.com> - 35.3-2
- Add weak dep on nautilus.

* Mon Aug 07 2017 Gwyn Ciesla <limburgher@gmail.com> - 35.3-1
- 35.3

* Mon Jul 31 2017 Gwyn Ciesla <limburgher@gmail.com> - 35.2-1
- 35.2

* Fri Jul 28 2017 Gwyn Ciesla <limburgher@gmail.com> - 35.0-1
- 35.0

* Thu Jul 27 2017 Gwyn Ciesla <limburgher@gmail.com> - 34.3-7
- Upstream patch for wrong-tab issue.

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 34.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 21 2017 Kai Engert <kaie@redhat.com> - 34.3-5
- Added upstream patches for building with vala 0.36

* Wed Jun 21 2017 Kai Engert <kaie@redhat.com> - 34.3-4
- Removed apparently unnecessary dependency on scrollkeeper

* Fri Mar 17 2017 Jon Ciesla <limburgher@gmail.com> - 34.3-3
- libbluray rebuild.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 34.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 30 2016 Jon Ciesla <limburgher@gmail.com> - 34.3-1
- Latest upstream, BZ 1400115

* Thu Jun 30 2016 Pete Walter <pwalter@fedoraproject.org> - 34.2-3
- Fix pygobject3 dependencies on RHEL 7

* Sat Apr 23 2016 Kevin Fenzi <kevin@scrye.com> - 34.2-2
- Fix appstream data. Fixes bug #1237364

* Mon Apr 11 2016 Jon Ciesla <limburgher@gmail.com> - 34.2-1
- Latest upstream, BZ 1325550

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 34.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 02 2015 Jon Ciesla <limburgher@gmail.com> - 34.1-1
- Latest upstream, BZ 1287328

* Thu Nov 19 2015 Jon Ciesla <limburgher@gmail.com> - 34.0-3
- Add python-gobject-base Requires, BZ 1283311.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 34.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Apr 11 2015 Jon Ciesla <limburgher@gmail.com> - 34.0-1
- Update to 34.0, BZ 1210918.

* Sat Oct 18 2014 Rahul Sundaram <sundaram@fedoraproject.org> - 32.0-3
- let's try that again

* Fri Oct 17 2014 Rahul Sundaram <sundaram@fedoraproject.org> - 32.0-2
- split up nautilus extension into a subpackage. resolves rhbz#1152449 

* Sun Oct 12 2014 Richard Hughes <richard@hughsie.com> - 32.0-1
- Update to 32.0

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 30.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 30.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 11 2014 Rahul Sundaram <sundaram@fedoraproject.org> - 30.0-1
- update to 30.0
- add a runtime requirement on duplicity >= 0.6.23

* Wed Mar 05 2014 Rahul Sundaram <sundaram@fedoraproject.org> - 29.5-1
- update to 29.5. resolves rhbz#1011780
- respect rpm opt flags. resolves rhbz#1057771
- add requires on dconf. resolves rhbz#1072097
- add upstream patch to make it build with cmake 3.0

* Mon Jan 20 2014 Kai Engert <kaie@redhat.com> - 29.4-1
- Update to 29.4
- Change configure to cmake

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 27.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 20 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 27.3.1-1
- update to 27.3.1-1

* Fri Mar 29 2013 Kalev Lember <kalevlember@gmail.com> - 26.0-1
- Update to 26.0

* Fri Jan 25 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 25.3-1
- upstream release 25.3

* Fri Sep 21 2012 Kalev Lember <kalevlember@gmail.com> - 23.92-1
- Update to 23.92

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun  1 2012 Ville Skyttä <ville.skytta@iki.fi> - 20.2-3
- Own %%{_libexecdir}/deja-dup and %%{_datadir}/deja-dup dirs.

* Wed Mar 21 2012 Tom Callaway <spot@fedoraproject.org> - 20.2-2
- fix BuildRequires

* Wed Mar 21 2012 Richard Hughes <rhughes@redhat.com> - 20.2-1
- Update to 20.2

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct 23 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 20.1-1
- New upstream release
- https://launchpad.net/deja-dup/+announcement/9065
- http://bazaar.launchpad.net/~deja-dup-hackers/deja-dup/20/view/1210/NEWS
- Fixes rhbz#748223
- validate deja-dup-monitor.desktop

* Tue Aug 23 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 19.90-1
- New upstream release
- https://launchpad.net/deja-dup/+announcement/8826
- http://bazaar.launchpad.net/~deja-dup-hackers/deja-dup/20/view/1141/NEWS
- Drop no longer needed build requires on po4a and unique-devel

* Sun Aug 07 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 19.5-1
- New upstream release
- Validate the preferences desktop file. Upstream bug reported by me lp:822312
- Drop BR on libxml2-python since itstool was fixed by me to add that dep

* Sun Aug 07 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 19.4-1
- New upstream release
- https://launchpad.net/deja-dup/+announcement/8715
- Upstream dropped Ubuntu specific icons per my bug report
- Dropped build requires on control-center-devel.  no longer exists
- Added build requires on itstool and libxml2-python
- Changed build requires from gnome-doc-utils to yelp-tools
- Add versioned requires on duplicity as per offlist mail from upstream
- Validate the primary desktop file
- Drop GConf entirely

* Sun Jun 26 2011 Jitesh Shah <jitesh.1337@gmail.com> - 19.3-1
- New upstream release (Mostly bugfixes and a couple of layout changes)
- https://launchpad.net/deja-dup/20/19.3
- http://bazaar.launchpad.net/~deja-dup-team/deja-dup/20/view/head:/NEWS

* Tue Jun 14 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 19.2.2-1
- New upstream release
- https://launchpad.net/deja-dup/20/19.2
- http://bazaar.launchpad.net/~deja-dup-team/deja-dup/20/view/head:/NEWS
- Drop build dependency on unique3-devel. No longer needed

* Mon May 09 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 19.1-1
- New upstream release
- Drop defattr since recent rpm makes it redundant 
- Add control-center-devel as build requires
- Update gsettings scriptlets to match latest guidelines
- Drop obsolete and invalid configuration options

* Sat Apr 16 2011 Chris Smart <csmart@fedoraproject.org> - 18.1.1-1
- Update to latest upstream release, which will "actually work with NetworkManager 0.9"
- http://bazaar.launchpad.net/~deja-dup-team/deja-dup/18/revision/888

* Wed Apr 13 2011 Chris Smart <csmart@fedoraproject.org> - 18.1-1
- Update to latest upstream release, 18.1
- https://launchpad.net/deja-dup/18/18.1

* Sat Apr 09 2011 Chris Smart <csmart@fedoraproject.org> - 18.0-1
- Update to latest upstream release, 18.0
- https://launchpad.net/deja-dup/18/18.0

* Wed Apr 06 2011 Dan Williams <dcbw@redhat.com> - 17.92-3
- Really fix for NM 0.9

* Tue Apr 05 2011 Dan Williams <dcbw@redhat.com> - 17.92-2
- Update for NetworkManager 0.9

* Sun Mar 27 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 17.92-1
- Update to latest upstream release
- http://bazaar.launchpad.net/~deja-dup-team/deja-dup/trunk/revision/863

* Thu Mar 17 2011 Chris Smart <csmart@fedoraproject.org> - 17.91-1
- Update to latest upstream release
- http://bazaar.launchpad.net/~deja-dup-team/deja-dup/trunk/revision/854

* Sat Mar 05 2011 Chris Smart <csmart@fedoraproject.org> - 17.90-1
- Update to latest upstream release
- http://bazaar.launchpad.net/~deja-dup-team/deja-dup/trunk/revision/838

* Tue Feb 15 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 17.6-3
- Rebuild against new GTK

* Fri Feb 11 2011 Matthias Clasen <mclasen@redhat.com> - 17.6-2
- Rebuild against newer gtk

* Fri Feb 11 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 17.6-2
- Update build requirements

* Fri Feb 11 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 17.6-1
- Update to latest upstream release
- http://bazaar.launchpad.net/~deja-dup-team/deja-dup/trunk/revision/827
- Drop no longer needed nautilus extension related patch
- Enable GTK3 and Nautilus support unconditionally

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 17.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb  2 2011 Matthias Clasen <mclasen@redhat.com> - 17.5-1
- Update to 17.5

* Sat Jan 29 2011 Ville Skyttä <ville.skytta@iki.fi> - 17.4-3
- Dir ownership fixes.

* Fri Jan  7 2011 Matthias Clasen <mclasen@redhat.com> - 17.4-2
- Rebuild against new GTK+

* Tue Dec 28 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 17.4-1
- http://bazaar.launchpad.net/~deja-dup-team/deja-dup/trunk/annotate/761/NEWS
- Reorganize the backup location preferences to be more intuitive
- New Chinese (simplified) translation and other translation updates

* Sat Dec 04 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 17.3-1
- https://launchpad.net/deja-dup/+announcement/7341
- http://bazaar.launchpad.net/~deja-dup-team/deja-dup/trunk/revision/753#NEWS
- drop no longer needed libnotify patch

* Fri Dec  3 2010 Matthias Clasen <mclasen@redhat.com> - 17.2-1
- Update to 17.2

* Fri Nov 12 2010 Adam Williamson <awilliam@redhat.com> - 17.1-1
- bump to 17.1
- adjust for use of gsettings
- add notify.patch to fix build against new libnotify

* Sun Jun 06 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 15.3-2
- Drop the dependency on yelp

* Sun Jun 06 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 15.3-1
- Several bug fixes including a potential data loss fix

* Sat May 08 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 15.1-1
- http://bazaar.launchpad.net/~deja-dup-team/deja-dup/trunk/revision/646#NEWS
- Reorganize help documentation to use new mallard format
- Change terminology for 'backup' verb to 'back up'
- Many new and updated translations
 
* Sat May 01 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 14.1-1
- https://launchpad.net/deja-dup/+announcement/5730
- Fix critical bugs preventing backup to external disks and restore single dir

* Sun Apr 18 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 14.0.3-1
- https://launchpad.net/deja-dup/+announcement/5630
- fix restoring to a non-empty directory

* Mon Apr 12 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 14.0.2-1
- https://launchpad.net/deja-dup/+announcement/5544
- drop the clean section

* Thu Apr 01 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 14.0-1
- new upstream release
- http://bazaar.launchpad.net/~deja-dup-team/deja-dup/14/annotate/head:/NEWS
- Gconf schema installation. Fixes rhbz #577004

* Sat Mar 20 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 13.92-1
- new upstream release
- https://launchpad.net/deja-dup/+announcement/5313

* Mon Mar 01 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 13.91-1
- new upstream release
- Fix review issues

* Tue Dec 22 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 13.4-1
- new upstream release
- http://bazaar.launchpad.net/~deja-dup-team/deja-dup/trunk/revision/557#NEWS

* Tue Dec 08 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 13.3-1
- new upstream release

* Mon Nov 23 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 11.1-1
- Initial spec
