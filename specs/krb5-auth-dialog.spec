%global tarball_version %%(echo %{version} | tr '~' '.')

%global __provides_exclude_from ^%{_libdir}/krb5-auth-dialog/plugins/.*\\.so$

Name:    krb5-auth-dialog
Version: 44.0~alpha1
Release: 6%{?dist}
Summary: Kerberos 5 authentication dialog

License: GPL-2.0-or-later
URL:     https://gitlab.gnome.org/GNOME/krb5-auth-dialog/
Source0: https://download.gnome.org/sources/%{name}/44/%{name}-%{tarball_version}.tar.xz

# avoid annoying notifications
Patch0: krb5-auth-dialog-autostart.patch
Patch1: Improve-auto-detection.patch

BuildRequires: gcc
BuildRequires: gettext
BuildRequires: intltool
BuildRequires: itstool
BuildRequires: meson
BuildRequires: pam-devel
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(krb5)
BuildRequires: pkgconfig(libadwaita-1)

%description
This package contains a dialog that warns the user when their Kerberos
tickets are about to expire and lets them renew them.

%prep
%autosetup -p1 -n %{name}-%{tarball_version}

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

%files -f %name.lang
%license COPYING
%doc AUTHORS NEWS README.md
%{_bindir}/krb5-auth-dialog*
%{_datadir}/applications/org.gnome.KrbAuthDialog.desktop
%{_datadir}/dbus-1/services/org.gnome.KrbAuthDialog.service
%{_datadir}/glib-2.0/schemas/org.gnome.KrbAuthDialog.gschema.xml
%{_datadir}/icons/hicolor/*/status/*
%{_libdir}/krb5-auth-dialog
%{_mandir}/man1/%{name}.1*
%{_metainfodir}/org.gnome.KrbAuthDialog.metainfo.xml
%{_sysconfdir}/xdg/autostart/krb5-auth-dialog.desktop


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 44.0~alpha1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 44.0~alpha1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 44.0~alpha1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 44.0~alpha1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 44.0~alpha1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Feb 08 2023 David King <amigadave@amigadave.com> - 44.0~alpha1-1
- Update to 44.0.alpha1

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 43.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Oct 28 2022 David King <amigadave@amigadave.com> - 43.0-1
- Update to 43.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 21 2018 Lubomir Rintel <lkundrak@v3.sk> - 3.26.1-4
- Switch to libnm from libnm-glib

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.26.1-2
- Remove obsolete scriptlets

* Fri Dec 01 2017 Kalev Lember <klember@redhat.com> - 3.26.1-1
- Update to 3.26.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jul 25 2016 Kalev Lember <klember@redhat.com> - 3.20.0-1
- Update to 3.20.0
- Use make_install macro

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.15.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.15.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 16 2015 David King <amigadave@amigadave.com> - 3.15.4-1
- Update to 3.15.4
- Use pkgconfig for BuildRequires

* Sat Nov 29 2014 Kalev Lember <kalevlember@gmail.com> - 3.15.1-1
- Update to 3.15.1

* Fri Oct 24 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.0-1
- Update to 3.14.0
- Adjust packaging for the gconf to gsettings port
- Build without scrollkeeper support

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 10 2014 Dan Horák <dan[at]danny.cz> - 3.2.1-8
- there is NetworkManager on s390(x)

* Wed Nov 06 2013 Simo Sorce <simo@redhat.com> - 3.2.1-7
- Fix bz1017292

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-2
- Rebuilt for glibc bug#747377

* Tue Oct 18 2011 Matthias Clasen <mclasen@redhat.com> - 3.2.1-1
- Update to 3.2.1

* Wed Sep 28 2011 Matthias Clasen <mclasen@redhat.com> - 3.2.0-1
- Update to 3.2.0

* Tue Sep  6 2011 Matthias Clasen <mclasen@redhat.com> - 3.1.91-1
- Update to 3.1.91

* Mon Apr 25 2011 Matthias Clasen <mclasen@redhat.com> - 3.0.1-1
- Update to 3.0.1
- Avoid annoying notification at login (#688302)

* Mon Apr  4 2011 Matthias Clasen <mclasen@redhat.com> - 3.0.0-1
- Update to 3.0.0

* Sat Mar 26 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.93-1
- Update to 2.91.93

* Thu Mar 24 2011 Dan Williams <dcbw@redhat.com> - 2.91.91-3
- Rebuild

* Thu Mar 10 2011 Dan Williams <dcbw@redhat.com> - 2.91.91-2
- Update for NetworkManager 0.9

* Tue Mar  8 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.91-1
- Update to 2.91.91

* Mon Feb 14 2011 Christopher Aillon <caillon@redhat.com> - 2.91.6-1
- Update to 2.91.6

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Nov  3 2010 Matthias Clasen <mclasen@redhat.com> 0.16-3
- Rebuild against libnotify 0.7.0

* Thu Sep 09 2010 Parag Nemade <paragn AT fedoraproject.org> 0.16-2
- Merge-review cleanup (#225973)

* Thu Jul  1 2010 Matthias Clasen <mclasen@redhat.com> - 0.16-1
- Update to 0.16

* Tue Apr  6 2010 Matthias Clasen <mclasen@redhat.com> - 0.15-1
- Update to 0.15

* Wed Oct 21 2009 Matěj Cepl <mcepl@redhat.com> - 0.13-1
- New upstream release (fixes #530001)

* Fri Sep 25 2009 Matthias Clasen <mclasen@redhat.com> - 0.12-2
- Fix the preferences dialog

* Sat Aug 29 2009 Matthias Clasen <mclasen@redhat.com> - 0.12-1
- Update to 0.12
- Rebuild against new libnm_glib

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 12 2009 Matěj Cepl <mcepl@redhat.com> - 0.10-1
- Catch up with upstream release again.

* Thu Apr 23 2009 Matthias Clasen <mclasen@redhatcom> - 0.8-4
- Don't show bubbles before the icon is there
- Use the same invisible char as the rest of the world

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jan 14 2009 Colin Walters <walters@verbum.org> - 0.8-2
- BR notify, pointed out by Bojan Smojver <bojan@rexursive.com>

* Tue Jan 13 2009 Colin Walters <walters@verbum.org> - 0.8-1
- New upstream release
- Remove both patches; they are upstreamed
- Add gconf spec goo
- Add new stuff to files list

* Mon Feb 18 2008 Christopher Aillon <caillon@redhat.com> - 0.7-7
- Rebuild to celebrate my birthday (and GCC 4.3)

* Thu Nov  1 2007 Matthias Clasen <mclasen@redhat.com> - 0.7-6
- Fix the Comment field in the desktop file (#344351)

* Mon Oct 22 2007 Christopher Aillon <caillon@redhat.com> - 0.7-5
- Don't start multiple times in KDE (#344991)

* Fri Aug 24 2007 Adam Jackson <ajax@redhat.com> - 0.7-4
- Rebuild for build ID

* Mon Aug 13 2007 Christopher Aillon <caillon@redhat.com> 0.7-3
- Update the license tag

* Thu Mar 15 2007 Karsten Hopp <karsten@redhat.com> 0.7-2
- rebuild with current gtk2 to add png support (#232013)

* Mon Jul 24 2006 Christopher Aillon <caillon@redhat.com> - 0.7-1
- Update to 0.7
- Don't peg the network and CPU when the KDC is unavailable

* Wed Jul 19 2006 John (J5) Palmieri <johnp@redhat.com> - 0.6.cvs20060212-4
- rebuild for dbus 

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.6.cvs20060212-3.1
- rebuild

* Sat Jun 24 2006 Jesse Keating <jkeating@redhat.com> - 0.6.cvs20060212-3
- Add missing BRs perl-XML-Parser, gettext
- Work around no network manager stuff on z900s

* Sun Feb 12 2006 Christopher Aillon <caillon@redhat.com> - 0.6.cvs20060212-1
- Update to latest CVS to get some of Nalin's fixes

* Tue Feb  7 2006 Jesse Keating <jkeating@redhat.com> - 0.6-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Tue Jan 31 2006 Christopher Aillon <caillon@redhat.com> 0.6-1
- Update to 0.6, adding an autostart file

* Fri Dec  9 2005 Jesse Keating <jkeating@redhat.com> - 0.5-2.1
- rebuilt

* Thu Dec  1 2005 John (J5) Palmieri <johnp@redhat.com> - 0.5-2
- rebuild for new dbus

* Tue Nov  8 2005 Christopher Aillon <caillon@redhat.com> 0.5-1
- Update to 0.5

* Tue Nov  1 2005 Christopher Aillon <caillon@redhat.com> 0.4-1
- Update to 0.4

* Mon Oct 31 2005 Christopher Aillon <caillon@redhat.com> 0.3-1
- Update to 0.3, working with newer versions of krb5 and NetworkManager

* Tue Aug 16 2005 David Zeuthen <davidz@redhat.com>
- Rebuilt

* Tue Mar 22 2005 Nalin Dahyabhai <nalin@redhat.com> 0.2-5
- Change Requires: krb5 to krb5-libs, repeat $ -> % fix for build requirements.

* Tue Mar 22 2005 Dan Williams <dcbw@redhat.com> 0.2-4
- Fix $ -> % for Requires: krb5 >= ...

* Mon Mar 21 2005 David Zeuthen <davidz@redhat.com> 0.2-3
- Fix up BuildRequires and Requires (#134704)

* Fri Mar  4 2005 David Zeuthen <davidz@redhat.com> 0.2-2
- Rebuild

* Mon Aug 16 2004 GNOME <jrb@redhat.com> - auth-dialog
- Initial build.

