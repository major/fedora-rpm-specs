%global po_package %{name}-3.0

Name:           gnome-applets
Version:        3.44.0
Release:        2%{?dist}
Summary:        Small applications for the GNOME Flashback panel

License:        GPLv2+
URL:            https://wiki.gnome.org/Projects/GnomeApplets
Source0:        https://download.gnome.org/sources/%{name}/3.44/%{name}-%{version}.tar.xz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  intltool
BuildRequires:  libSM-devel
BuildRequires:  libtool
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  yelp-tools

BuildRequires:  pkgconfig(adwaita-icon-theme) >= 3.14.0
BuildRequires:  pkgconfig(dbus-1) >= 1.1.2
BuildRequires:  pkgconfig(dbus-glib-1) >= 0.74
BuildRequires:  pkgconfig(glib-2.0) >= 2.44.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20.0
BuildRequires:  pkgconfig(gucharmap-2.90) >= 2.33.0
BuildRequires:  pkgconfig(gweather4) >= 3.91
BuildRequires:  pkgconfig(libgnome-panel) >= 3.41.1
BuildRequires:  pkgconfig(libgtop-2.0) >= 2.11.92
BuildRequires:  pkgconfig(libnotify) >= 0.7
BuildRequires:  pkgconfig(libwnck-3.0) >= 3.14.1
BuildRequires:  pkgconfig(libxml-2.0) >= 2.5.0
BuildRequires:  pkgconfig(polkit-gobject-1) >= 0.97
BuildRequires:  pkgconfig(tracker-sparql-3.0)
BuildRequires:  pkgconfig(upower-glib) >= 0.9.4
BuildRequires:  pkgconfig(x11)
%ifnarch s390 s390x sparc64
BuildRequires:  kernel-tools-devel
%endif

Requires:       gnome-panel >= 3.41.1
Requires:       hicolor-icon-theme

%description
Gnome Applets component is part of the GnomeFlashback project. It currently
provides the following applets:

- Accessibility applet (accessx-status)
- Battery status (battstat)
- A symbol table (charpick)
- A system monitor for cpu, memory and network usage information (cpufreq)
- A drive mount applet (drivemount)
- Geyes, a funny applet that shows a pair of eyes which follow the cursor
  (geyes)
- A weather applet (gweather)
- A command execution and macro plugin (mini-commander)
- A sound applet (deprecated and replaced by libsound-applet in GnomeFlashback
  (mixer)
- A model lights plugin for modems (modemlights)
- A multi load plugin (multiload)
- A notes applets (stickynotes)
- A trash applet (trashapplet)
- A window picker applet that shows open applications as icons. This saves a lot
  of screen space and is very useful if many applications are open.
  (windowpicker)


%prep
%autosetup -p1
autoreconf -fiv


%build
%configure                      \
    --disable-scrollkeeper      \
    --disable-static            \
    --enable-gtk-doc            \
    --enable-mini-commander     \
    --enable-suid=no            \
    --with-cpufreq-lib=cpupower \
    --without-hal               \
    %{nil}
%make_build


%install
%make_install
%find_lang %{po_package} --all-name

# Clean up unpackaged files
find %{buildroot}%{_libdir}/gnome-panel/ -name '*.la' -delete

# drop non-XKB support files
rm -rf %{buildroot}%{_datadir}/xmodmap


%files -f %{po_package}.lang
%license COPYING
%doc README AUTHORS NEWS
%{_datadir}/%{name}/
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_libdir}/gnome-panel/modules/org.gnome.%{name}.so
%{_datadir}/glib-2.0/schemas/*.enums.xml
%ifnarch s390 s390x
%{_bindir}/cpufreq-selector
%{_datadir}/dbus-1/system-services/org.gnome.CPUFreqSelector.service
%{_datadir}/polkit-1/actions/org.gnome.cpufreqselector.policy
%config %{_sysconfdir}/dbus-1/system.d/org.gnome.CPUFreqSelector.conf
%endif

# Don't make it as separate noarch package since it builds differently on 's390x'
# arch and we got build error here
%{_datadir}/help/


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.44.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Mar 19 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 3.44.0-1
- chore(update): 3.44.0

* Sat Mar 12 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 3.43.1-1
- chore(update): 3.43.1

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.42.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Oct 23 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 3.42.0-1
- chore(update): 3.42.0

* Fri Oct 01 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 3.41.1-1
- build(update): 3.41.1

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.40.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Mar 26 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 3.40.0-1
- build(update): 3.40.0

* Thu Mar 18 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 3.38.0-4
- build: BR tracker-sparql-3.0
  build: Apply upstream patch 3725b0e3 commit
  style: Trim trailing whitespaces

* Thu Mar 18 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 3.38.0-3
- build: apply upstream patch with port to Tracker 3

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 15 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 3.38.0-1
- build(update): 3.38.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.36.4-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.36.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 24 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 3.36.4-1
- Update to 3.36.4
- Disable LTO

* Tue Apr 07 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 3.36.2-1
- Update to 3.36.2

* Fri Mar 27 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 3.36.1-2
- Backport upstream patch for memory leak fix | gnome-panel#21

* Thu Mar 26 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 3.36.1-1
- Update to 3.36.1

* Wed Mar 25 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 3.34.0-6
- Remove noarch doc package due to build error

* Sun Feb 23 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 3.34.0-5
- Spec file improvements
- Drop obsolete macroses
- Enable LTO

* Thu Dec 26 2019 Yaakov Selkowitz <yselkowi@redhat.com> - 1:3.34.0-1
- new version

* Sun May 05 2019 Yaakov Selkowitz <yselkowi@redhat.com> - 1:3.32.0-1
- new version

* Mon Nov 12 2018 Yaakov Selkowitz <yselkowi@redhat.com> - 1:3.30.0-1
- new version

* Mon Mar 26 2018 Yaakov Selkowitz <yselkowi@redhat.com> - 1:3.28.0-1
- new version

* Mon Nov 13 2017 Yaakov Selkowitz <yselkowi@redhat.com> - 1:3.26.0-1
- new version

* Tue Mar 28 2017 Yaakov Selkowitz <yselkowi@redhat.com> - 1:3.24.0-1
- new version

* Sun Mar 26 2017 Yaakov Selkowitz <yselkowi@redhat.com> - 1:3.22.0-1
- new version

* Mon Sep 12 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 1:3.20.0-2
- Update cpupower patch for kernel 4.7

* Mon Apr 18 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 1:3.20.0-1
- Version bump for GNOME Flashback 3.20.

* Thu Apr 14 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 1:3.18.2-1
- new version

* Tue Oct 13 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 1:3.18.1-1
- Update to 3.18.1.

* Fri Oct 02 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 1:3.18.0-1
- Version bump for GNOME Flashback 3.18.0.

* Wed Jul 15 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 1:3.17.2-1
- Unstable version bump

* Wed Jul 15 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 1:3.16.1-2
- Enable battstat applet

* Thu Apr 30 2015 Mike DePaulo <mikedep333@gmail.com> - 1:3.16.1-1
- Version bump for GNOME Flashback 3.16.1.
- Drop gnome-applets-cpupower.patch because we can call
  --with-cpufreq-lib=cpupower now instead.

* Mon Feb 09 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 1:3.14.0-1
- Version bump for GNOME Flashback 3.14.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.5.92-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Sep 22 2012 Kalev Lember <kalevlember@gmail.com> - 1:3.5.92-3
- Remove gweather gconf schema handling

* Sat Sep 22 2012 Kalev Lember <kalevlember@gmail.com> - 1:3.5.92-2
- Update the icon cache scriptlets
- Fix the build; add glib-compile-schemas scriptlets
- Clean out some old cruft from the spec file

* Thu Sep 20 2012 Richard Hughes <hughsient@gmail.com> - 1:3.5.92-1
- Update to 3.5.92

* Tue Sep 04 2012 Richard Hughes <hughsient@gmail.com> - 1:3.5.91-1
- Update to 3.5.91

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun May 06 2012 Kalev Lember <kalevlember@gmail.com> - 1:3.5.1-1
- Update to 3.5.1

* Mon Apr 16 2012 Richard Hughes <hughsient@gmail.com> - 1:3.4.1-1
- Update to 3.4.1

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov  2 2011 Matthias Clasen <mclasen@redhat.com> = 1:3.3.1-1
- Update to 3.3.1

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.2.1-2
- Rebuilt for glibc bug#747377

* Wed Oct 19 2011 Matthias Clasen <mclasen@redhat.com> - 1:3.2.1-1
- Update to 3.2.1

* Wed Sep 28 2011 Ray <rstrode@redhat.com> - 1:3.2.0-1
- Update to 3.2.0

* Wed Sep 28 2011 Ray <rstrode@redhat.com> - 1:3.2.0-1
- Update to 3.2.0

* Tue Sep 20 2011 Matthias Clasen <mclasen@redhat.com> - 3.1.92-1
- Update to 3.1.92

* Thu Sep 08 2011 Dan Horák <dan[at]danny.cz> - 3.1.91-2
- kernel-tools-devel isn't built on s390(x) and sparc64

* Wed Sep 07 2011 Kalev Lember <kalevlember@gmail.com> - 3.1.91-1
- Update to 3.1.91

* Wed Aug 31 2011 Matthias Clasen <mclasen@redhat.com> - 3.1.90-1
- Update to 3.1.90

* Thu Aug 18 2011 Matthias Clasen <mclasen@redhat.com> - 3.1.5-1
- Update to 3.1.5

* Tue Jul 26 2011 Matthias Clasen <mclasen@redhat.com> - 3.1.4-1
- Update to 3.1.4

* Mon Jul 04 2011 Bastien Nocera <bnocera@redhat.com> 3.1.3-1
- Update to 3.1.3

* Tue Jun 14 2011 Tomas Bzatek <tbzatek@redhat.com> - 1:3.1.2-1
- Update to 3.1.2

* Mon May  9 2011 Tomas Bzatek <tbzatek@redhat.com> - 1:3.1.1-2
- Fix package Requires

* Mon May  9 2011 Tomas Bzatek <tbzatek@redhat.com> - 1:3.1.1-1
- Update to 3.1.1
- Restored basic functionality

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.32.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Nov  3 2010 Matthias Clasen <mclasen@redhat.com> - 1:2.32.0-3
- Rebuild against libnotify 0.7.0

* Mon Oct 11 2010 Matthias Clasen <mclasen@redhat.com> - 1:2.32.0-2
- Rebuild without gucharmap support

* Thu Sep 30 2010 Matthias Clasen <mclasen@redhat.com> - 1:2.32.0-1
- Update to 2.32.0

* Tue Aug 31 2010 Matthias Clasen <mclasen@redhat.com> - 1:2.31.91-1
- Update to 2.31.91

* Thu Aug 19 2010 Matthias Clasen <mclasen@redhat.com> - 1:2.31.90.1-1
- Update to 2.31.90.1

* Tue Aug  3 2010 Matthias Clasen <mclasen@redhat.com> - 1:2.31.6-1
- Update to 2.31.6

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 1:2.31.5-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Mon Jul 12 2010 Matthias Clasen <mclasen@redhat.com> - 1:2.31.5-1
- 2.31.5

* Wed Jun 16 2010 Matthias Clasen <mclasen@redhat.com> - 1:2.30.0-3
- Kill the scrollkeeper runtime dep

* Thu Jun  3 2010 Matthias Clasen <mclasen@redhat.com> - 1:2.30.0-2
- Fix BRs

* Sun Mar 28 2010 Matthias Clasen <mclasen@redhat.com> - 1:2.30.0-1
- Update to 2.30.0

* Sun Feb 14 2010 Matthias Clasen <mclasen@redhat.com> - 1:2.29.5-2
- Add missing libs

* Sun Jan 17 2010 Matthias Clasen <mclasen@redhat.com> - 1:2.29.5-1
- Update to 2.29.5

* Tue Oct 27 2009 Matthias Clasen <mclasen@redhat.com> - 1:2.28.0-2
- Fix a help file seriesid clash between accessx-status and invest-applet

* Mon Sep 21 2009 Matthias Clasen <mclasen@redhat.com> - 1:2.28.0-1
- Update to 2.28.0

* Tue Sep  8 2009 Matthias Clasen <mclasen@redhat.com> - 1:2.27.92-1
- Update to 2.27.92

* Tue Aug 25 2009 Matthias Clasen <mclasen@redhat.com> - 1:2.27.91-1
- 2.27.91

* Wed Jul 29 2009 Matthias Clasen <mclasen@redhat.com> - 1:2.27.4-1
- Update to 2.27.4

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.27.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Matthias Clasen <mclasen@redhat.com> - 1:2.27.3-5
- Rebuild against new libgnomekbd

* Mon Jul 13 2009 Matthias Clasen <mclasen@redhat.com> - 1:2.27.3-4
- Fix PolicyKit 1 patch

* Tue Jun 30 2009 Matthias Clasen <mclasen@redhat.com> - 1:2.27.3-3
- Rebuild against new libxklavier

* Wed Jun 17 2009 Matthias Clasen <mclasen@redhat.com> - 1:2.27.3-2
- Drop sticky notes, now that we have gnotes

* Wed Jun 17 2009 Matthias Clasen <mclasen@redhat.com> - 1:2.27.3-1
- Update to 2.27.3

* Sat Jun 13 2009 Matthias Clasen <mclasen@redhat.com> - 1:2.27.2-3
- Drop unneeded direct dependencies

* Wed Jun 10 2009 Matthias Clasen <mclasen@redhat.com> - 1:2.27.2-2
- Port to PolicyKit 1

* Sun May 31 2009 Matthias Clasen <mclasen@redhat.com> - 1:2.27.2-1
- Update to 2.27.2
- http://download.gnome.org/sources/gnome-applets/2.27/gnome-applets-2.27.2.news

* Mon Apr 27 2009 Matthias Clasen <mclasen@redhat.com> - 1:2.26.1-3
- Don't drop schemas translations from po files

* Wed Apr 15 2009 Matthias Clasen <mclasen@redhat.com> - 1:2.26.1-2
- Make gweather network status tracking work

* Mon Apr 13 2009 Matthias Clasen <mclasen@redhat.com> - 1:2.26.1-1
- Update to 2.26.1

* Sun Mar 29 2009 Matthias Clasen <mclasen@redhat.com> - 1:2.25.92-4
- Make cpufreq applet work (#492741)

* Sat Mar 21 2009 Matthias Clasen <mclasen@redhat.com> - 1:2.25.92-3
- Make the invest applet work

* Tue Mar 17 2009 Matthias Clasen <mclasen@redhat.com> - 1:2.25.92-2
- Support https in minicommander (#490387)

* Mon Mar  2 2009 Matthias Clasen <mclasen@redhat.com> - 1:2.25.92-1
- Update to 2.25.92

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.25.91-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 19 2009 Matthias Clasen <mclasen@redhat.com> - 1:2.25.91-2
- Update to 2.25.91

* Fri Feb  6 2009 Matthias Clasen <mclasen@redhat.com> - 1:2.25.90-3
- Keep the dead mixer applet from haunting the add to panel dialog

* Tue Feb  3 2009 Matthias Clasen <mclasen@redhat.com> - 1:2.25.90-1
- Update to 2.25.90

* Wed Jan 21 2009 Matthias Clasen <mclasen@redhat.com> - 1:2.25.4-2
- Fix trash applet not starting up

* Tue Jan 20 2009 Matthias Clasen <mclasen@redhat.com> - 1:2.25.4-1
- Update to 2.25.4

* Sun Jan 11 2009 Matthias Clasen <mclasen@redhat.com> - 1:2.25.3-3
- Fix the nullappletification of the mixer applet

* Tue Jan  6 2009 Matthias Clasen <mclasen@redhat.com> - 1:2.25.3-2
- Update to 2.25.3

* Sat Dec 20 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.25.2-4
- Update to 2.25.2

* Fri Dec 19 2008 - Bastien Nocera <bnocera@redhat.com> - 1:2.25.1-8
- Fix battstat nullification

* Fri Dec 19 2008 - Bastien Nocera <bnocera@redhat.com> - 1:2.25.1-7
- Remove the mixer applet

* Fri Dec 19 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.25.1-5
- Fix the build

* Thu Dec 18 2008 Jon McCann <jmccann@redhat.com> - 1:2.25.1-5
- Rebuild for gnome-desktop

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1:2.25.1-4
- Rebuild for Python 2.6

* Sat Nov 22 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.25.1-4
- Improve description

* Fri Nov 21 2008 Ray Strode <rstrode@redhat.com> - 1:2.25.1-3
- Install modemlights schema (bug 417031)

* Thu Nov 13 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.25.1-2
- Rebuild

* Wed Nov 12 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.25.1-1
- Update to 2.25.1

* Tue Oct 21 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.24.1-1
- Update to 2.24.1

* Fri Oct 10 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.24.0.1-5
- Fix some missing translations

* Fri Oct 10 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.24.0.1-4
- Save space

* Fri Sep 26 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.24.0.1-3
- Small improvement to the drivemount applet

* Wed Sep 24 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.24.0.1-2
- Update to 2.24.0.1

* Sun Sep 21 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.24.0-2
- Update to 2.24.0

* Tue Sep 16 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.23.92-2
- Plug a leak in the trash applet

* Tue Sep  9 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.23.92-1
- Update to 2.23.92

* Thu Sep  4 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.23.91-1
- Update to 2.23.91

* Fri Aug 29 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.23.90-2
- Plug a memory leak in the keyboard applet

* Fri Aug 22 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.23.90-1
- Update to 2.23.90

* Fri Aug  8 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.23.4-2
- Undecorate the mixer popup

* Mon Aug  4 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.23.4-1
- Update to 2.23.4

* Wed Jul 23 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1:2.23.3-3
- fix license tag

* Wed Jun 18 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.23.3-1
- Update to 2.23.3

* Wed Jun  4 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.23.2-2
- Rebuild

* Tue May 13 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.23.2-1
- Update to 2.23.2
- Drop upstreamed patches

* Tue May  6 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.22.1-3
- Drop gnome-netstatus dependency (#445059)

* Wed Apr 23 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.22.1-2
- Reduce the trash icon size (#438620)

* Mon Apr  7 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.22.1-1
- Update to 2.22.1

* Fri Apr  4 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.22.0-2
- Fix a bug in the keyboard accessibility applet

* Mon Mar 10 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.22.0-1
- Update to 2.22.0

* Tue Feb 26 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.21.92-1
- Update to 2.21.92

* Tue Feb 12 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.21.91-1
- Update to 2.21.91

* Thu Jan 31 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.21.4-5
- Rebuild against new libxklavier

* Fri Jan 25 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.21.4-4
- Port trash applet to gvfs
- Remove gnome-vfs dependency in gweather

* Mon Jan 21 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.21.4-3
- Fix the invest applet on vertical panels

* Sun Jan 20 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.21.4-2
- Make the weather applet find locations.xml again

* Wed Jan 16 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.21.4-1
- Update to 2.21.4

* Sun Dec  9 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.21.2-2
- Silence the %%post script

* Wed Dec  5 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.21.2-1
- Update to 2.21.2
- Drop the battstat applet

* Mon Oct 29 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.20.0-10
- Fix a number of problems in the weather applet

* Tue Oct 23 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.20.0-9
- Rebuild against new dbus-glib

* Sun Oct 21 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.20.0-8
- Update weather info when going online

* Fri Oct 12 2007 - Bastien Nocera <bnocera@redhat.com> - 1:2.20.0-7
- Update out-of-sync patch to handle mute properly (#320451)

* Thu Sep 27 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.20.0-6
- Fix a memory leak in the mixer preferences

* Tue Sep 25 2007 - Bastien Nocera <bnocera@redhat.com> - 1.2.20.0-5
- Fix possible crasher in the mixer messages when we receive an
  unhandled message (#302881)

* Sat Sep 22 2007 David Woodhouse <dwmw2@infradead.org> - 1.2.20.0-4
- Build modemlights applet again (#301601)

* Sat Sep 22 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.20.0-3
- Make the gweather.pc file less useless

* Thu Sep 20 2007 - Bastien Nocera <bnocera@redhat.com> - 1:2.20.0-2
- Add patch to avoid the volume scale getting out-of sync with the
  real hardware volume

* Sun Sep 16 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.20.0-1
- Update to 2.20.0

* Tue Sep  4 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.19.91-1
- Update to 2.19.91

* Thu Aug 23 2007 Adam Jackson <ajax@redhat.com> - 1:2.19.1-8
- Rebuild for build ID

* Sun Aug 12 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.19.1-7
- Fix Requires

* Sun Aug 12 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.19.1-6
- Stop the mixer applet from polling the volume

* Sun Aug  5 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.19.1-5
- Use %%find_lang for help files, too
- Update the license field

* Sun Aug  5 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.19.1-4
- gswitchit.schemas does not exist anymore

* Thu Aug  2 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.19.1-3
- Waste less space in Locations.xml

* Wed Aug  1 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.19.1-2
- Fix scriptlets

* Wed Aug  1 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.19.1-1
- Update to 2.19.1

* Tue Jul 31 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.19.0-2
- Rebuild

* Mon Jul 30 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.19.0-1
- Update to 2.19.0
- Drop modemlights, since it doesn't build anymore

* Sat Jul  7 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.18.0-13
- Another directory ownership fix

* Fri Jul  6 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.18.0-12
- Fix a directory ownership issue

* Sun Jun 17 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.18.0-11
- Fix #237058

* Tue Jun  5 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.18.0-10
- Rebuild again

* Mon Jun  4 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.18.0-9
- Rebuild against new libwnck

* Mon May 21 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.18.0-8
- Split off a -devel package

* Tue Apr 10 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.18.0-7
- Fix a leak in the keyboard indicator applet

* Sat Mar 31 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.18.0-6
- Fix the bug-buddy support of the accessx status applet

* Sat Mar 31 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.18.0-5
- Add bug-buddy support to the keyboard indicator applet

* Fri Mar 30 2007 Ray Strode <rstrode@redhat.com> - 1:2.18.0-4
- make gweather applet preferences find feature work slightly
  better (bug 209488)

* Wed Mar 28 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.18.0-3
- Remove non-XKB support files to save space

* Wed Mar 21 2007 Ray Strode <rstrode@redhat.com> - 1:2.18.0-2
- rerun intltoolize to get latest version

* Tue Mar 13 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.18.0-1
- Update to 2.18.0
- Drop upstreamed patch

* Tue Feb 27 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.17.90-1
- Update to 2.17.90

* Wed Jan 10 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.17.1-1
- Update to 2.17.1

* Wed Jan 10 2007 Ray Strode <rstrode@redhat.com> - 1:2.16.2-6
- fix null applet error on login for new users (bug 222104)

* Tue Dec 12 2006 Ray Strode <rstrode@redhat.com> - 1:2.16.2-5
- fix mixer applet error on login for new users (bug 217919)

* Sat Dec  9 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.16.2-4
- Small spec file cleanups

* Thu Dec  7 2006 Jeremy Katz <katzj@redhat.com> - 1:2.16.2-3
- rebuild for python 2.5

* Tue Dec  5 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.16.2-2
- Fix the trashapplet opening a window on the wrong screen (#218447)

* Tue Dec  5 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.16.2-1
- Update to 2.16.2
- Drop obsolete patches

* Thu Nov 16 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.16.1-5
- Fix muted icon in mixer again

* Mon Nov  6 2006 Ray Strode <rstrode@redhat.com> - 1:2.16.1-4
- s/verion/version/ in dbus glib build requires

* Fri Nov  3 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.16.1-3
- Silence %%pre

* Mon Oct 23 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.16.1-2
- Make the cpufreq applet pick up preference changes (#209168)

* Sat Oct 21 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.16.1-1
- Update to 2.16.1
- Drop upstreamed patches

* Wed Oct 18 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.16.0.1-11
- Fix scripts according to packaging guidelines

* Tue Oct 17 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.16.0.1-10
- Fix up requirements (#202549)

* Sat Oct 14 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.16.0.1-9
- Fix muting in the mixer applet (#208660)

* Sun Oct 01 2006 Jesse Keating <jkeating@redhat.com> - 1:2.16.0.1-7
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Thu Sep 21 2006 Ray Strode <rstrode@redhat.com> - 1:2.16.0.1-6
- Don't ask for password when changing CPU frequency

* Mon Sep 18 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.16.0.1-5
- Fix a segfault in the keyboard indicator applet

* Fri Sep 15 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.16.0.1-4
- Fix some icon size issues in the trash applet

* Sun Sep 10 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.16.0.1-3
- Make stickynotes not wake up 10 times per second (#205909)

* Fri Sep  8 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.16.0.1-2
- Fix the resizing behaviour of the mixer applet

* Mon Sep  4 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.16.0.1-1.fc6
- Update to 2.16.0.1

* Mon Sep  4 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.16.0-1.fc6
- Update to 2.16.0

* Fri Sep  1 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.15.90-6.fc6
- Make the battstat applet poll less often (204858)

* Mon Aug 28 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.15.90-5.fc6
- Make cpufreq-selector use the config-utils pam policy

* Sun Aug 27 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.15.90-4.fc6
- Fix some redraw issues in the keyboard capplet

* Sun Aug 27 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.15.90-3.fc6
- More keyboard drawing improvements

* Thu Aug 24 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.15.90-2.fc6
- Various improvements for the keyboard applet

* Tue Aug 22 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.15.90-1.fc6
- Update to 2.15.90
- Drop upstreamed patches
- Add a %%preun script
- Require pkgconfig

* Fri Aug 18 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.15.3-2.fc6
- Make the invest applet work

* Sun Aug 13 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.15.3-1.fc6
- Update to 2.15.3

* Tue Aug  8 2006 Ray Strode <rstrode@redhat.com> - 1:2.15.2-4.fc6
- destroy about dialog on close (bug 197975)

* Sat Aug  5 2006 Caolan McNamara <caolanm@redhat.com> - 1:2.15.2-3.fc6
- rebuild against new gucharmap

* Fri Aug  4 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.15.2-2.fc6
- Fix the multiload schema

* Thu Aug  3 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.15.2-1.fc6
- Update to 2.15.2

* Wed Aug  2 2006 Ray Strode <rstrode@redhat.com> - 1:2.15.1.1-7
- don't require a display to build invest applet (bug 200970).
  Problem discovered by Nalin Dahyabhai <nalin@redhat.com>

* Sat Jul 29 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.15.1.1-6
- Require gnome-python2-libegg for invest applet (#200640)

* Wed Jul 19 2006 John (J5) Palmieri <johnp@redhat.com> - 1:2.15.1.1-5
- Add BR for dbus-glib-devel

* Wed Jul 19 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.15.1.1-4
- Rebuild against dbus

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1:2.15.1.1-3.1
- rebuild

* Fri Jul  7 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.15.1.1-3
- Try to make the invest applet actually work

* Thu Jun 22 2006 Jeremy Katz <katzj@redhat.com> - 1:2.15.1.1-2
- fix invest applet location

* Mon Jun 19 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.1.1-1
- Update to 2.15.1.1

* Thu Jun 15 2006 Matthias Clasen <mclasen@redhat.com> - 2.14.2-5
- Rebuild against new libxklavier

* Thu Jun  8 2006 Matthias Clasen <mclasen@redhat.com> - 2.14.2-4
- Explicitly list the applets to be included

* Tue Jun  6 2006 Matthias Clasen <mclasen@redhat.com> - 2.14.2-3
- Rebuild

* Sun May 28 2006 Matthias Clasen <mclasen@redhat.com> - 2.14.2-2
- Update to 2.14.2

* Mon Apr 10 2006 Matthias Clasen <mclasen@redhat.com> - 2.14.1-2
- Update to 2.14.1
- Update patches

* Tue Mar 28 2006 Ray Strode <rstrode@redhat.com> - 2.14.0-3
- apply patch

 * Tue Mar 28 2006 Ray Strode <rstrode@redhat.com> - 2.14.0-2
- export symbols in gswitchit applet so applet plugins
  work (bug 187168)

* Sun Mar 12 2006 Ray Strode <rstrode@redhat.com> - 2.14.0-1
- update to 2.14.0

* Thu Mar  9 2006 Ray Strode <rstrode@redhat.com> - 2.13.90-8
- s/divemount/drivemount/

* Thu Mar  9 2006 Ray Strode <rstrode@redhat.com> - 2.13.90-7
- remove some bad trailing spaces introduced in 2.13.90-6

* Wed Mar  8 2006 Ray Strode <rstrode@redhat.com> - 2.13.90-6
- improve package installation time by running gconftool-2 only
  once in %%post

* Wed Mar  8 2006 Matthias Clasen <mclasen@redhat.com> - 2.13.90-5
- Fix a crash in the mixer applet (#184285, #182957)

* Tue Mar 7 2006 Ray Strode <rstrode@redhat.com> - 2.13.90-4
- ref some objects given to us by gstreamer

* Wed Mar 1 2006 Ray Strode <rstrode@redhat.com> - 2.13.90-3
- More stock ticker fun (bug 179528)

* Tue Feb 28 2006 Karsten Hopp <karsten@redhat.de> 2.13.90-2
- BuildRequires: which

* Sun Feb 26 2006 Matthias Clasen <mclasen@redhat.com> - 2.13.90-1
- Update to 2.13.90

* Thu Feb 23 2006 Matthias Clasen <mclasen@redhat.com> - 2.13.4-4
- Make the stock ticker work with gcc 4.1 (#179528)

* Sat Feb 18 2006 Matthias Clasen <mclasen@redhat.com> - 2.13.4-3
- Remove a warning from the stock ticker applet

* Wed Feb 15 2006 Matthias Clasen <mclasen@redhat.com> - 2.13.4-2
- Build with --enable-mini-commander

* Sun Feb 12 2006 Matthias Clasen <mclasen@redhat.com> - 2.13.4-1
- Update to 2.13.4

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1:2.13.3-4.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1:2.13.3-4.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Feb 01 2006 Matthias Clasen <mclasen@redhat.com> 2.13.3-4
- Fix an overflow in the weather applet

* Tue Jan 31 2006 Matthias Clasen <mclasen@redhat.com> 2.13.3-3
- Update gstreamer requires

* Tue Jan 31 2006 Matthias Clasen <mclasen@redhat.com> 2.13.3-1
- Update to 2.13.3

* Wed Jan 18 2006 Matthias Clasen <mclasen@redhat.com> 2.13.2-2
- BuildRequire gnome-doc-utils

* Tue Jan 17 2006 Matthias Clasen <mclasen@redhat.com> 2.13.2-1
- Update to 2.13.2

* Fri Jan 05 2006 John (J5) Palmieri <johnp@redhat.com> 2.13.1-4
- GStreamer has been split into gstreamer08 and gstreamer (0.10) packages
  we need gstreamer08 for now

* Wed Jan 04 2006 Matthias Clasen <mclasen@redhat.com> 2.13.1-3
- Rebuild against new libgtop

* Fri Dec 16 2005 Matthias Clasen <mclasen@redhat.com> 2.13.1-2
- Rebuild against new libgtop

* Thu Dec 15 2005 Matthias Clasen <mclasen@redhat.com> 2.13.1-1
- Update to 2.13.1
- Update file lists

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com> 2.12.2-1.1
- rebuilt

* Fri Dec  2 2005 Matthias Clasen <mclasen@redhat.com> 2.12.2-1
- Update to 2.12.2

* Thu Dec 01 2005 John (J5) Palmieri <johnp@redhat.com> - 1:2.12.1-4
- rebuild for new dbus

* Mon Nov 14 2005 Ray Strode <rstrode@redhat.com> - 1:2.12.1-3
- build correct command string for cpufreq-selection. Fix
  spotted by Ingo Schaefer <ingo@ingo-shaefer.de> (Bug 164147).

* Thu Oct 20 2005 Ray Strode <rstrode@redhat.com> - 1:2.12.1-2
- require libgtop2 >= 2.12.0, bug 171285

* Thu Oct  6 2005 Matthias Clasen <mclasen@redhat.com> - 1:2.12.1-1
- Update to 2.12.1

* Thu Sep  8 2005 Matthias Clasen <mclasen@redhat.com> - 1:2.12.0-1
- Update to 2.12.0, drop upstreamed patches

* Wed Aug 17 2005 Jeremy Katz <katzj@redhat.com> - 1:2.11.91-5
- fun with auto* to really get the build working

* Wed Aug 17 2005 Jeremy Katz <katzj@redhat.com> - 1:2.11.91-4
- patch from upstream cvs to fix build with new pango (bgo #313368)

* Tue Aug 16 2005 Warren Togami <wtogami@redhat.com> - 1:2.11.91-3
- rebuild for new cairo

* Thu Aug 11 2005 Ray Strode <rstrode@redhat.com> 1:2.11.91-2
- disable scrollkeeper database updates
- add omf files to package list
- require gnome-utils for gucharmap/charpick integration

* Wed Aug 10 2005 Ray Strode <rstrode@redhat.com> 1:2.11.91-1
- New upstream version

* Fri Aug  5 2005 Matthias Clasen <mclasen@redhat.com> 1:2.11.2-2
- New upstream version

* Tue Jul 12 2005 Matthias Clasen <mclasen@redhat.com> 1:2.11.1-2
- Rebuilt

* Fri Jul  8 2005 Matthias Clasen <mclasen@redhat.com> 1:2.11.1-1
- Update to 2.11.1

* Fri Jul  1 2005 Mark McLoughlin <markmc@redhat.com> 1:2.10.1-10
- Backport from HEAD patch to remove lame warning dialog when the
  mixer applet can't find a mixer device

* Fri May 27 2005 Bill Nottingham <notting@redhat.com> 1:2.10.1-9
- remove setuid bit from cpufreq-selector, usermode-ify it

* Thu May 19 2005 Ray Strode <rstrode@redhat.com> 1:2.10.1-8
- Install modemlights gconf schema (bug 157764).

* Fri May 13 2005 Ray Strode <rstrode@redhat.com> 1:2.10.1-7
- Don't disable battstat on some platforms (bug 157683).

* Wed Apr 27 2005 Jeremy Katz <katzj@redhat.com> - 1:2.10.1-6
- silence %%post

* Tue Apr 26 2005 Ray Strode <rstrode@redhat.com> 1:2.10.1-5
- Add back old patch to change ppp connect/disconnect commands
  (bug 147675)

* Wed Apr 20 2005 Ray Strode <rstrode@redhat.com> 1:2.10.1-4
- Use builtin copy of apmlib instead of adding an external dependency
  (bug 155125)

* Thu Apr 14 2005 Ray Strode <rstrode@redhat.com> 1:2.10.1-3
- Apply patch from Jan de Groot <jan@jgc.homeip.net> to
  silence scrollkeeper noise (bug 152236)

* Thu Apr 14 2005 Ray Strode <rstrode@redhat.com> 1:2.10.1-2
- Add Obsoletes: gnome-cpufreq-applet (bug 154853)

* Thu Apr  7 2005 Ray Strode <rstrode@redhat.com> 1:2.10.1-1
- update to 2.10.1
- actually build the old modemlights that were added in 2.10.0-4

* Tue Apr  5 2005 Ray Strode <rstrode@redhat.com> 1:2.10.0-5
- Don't use %%postun -p optimization now that we do more than
  just /sbin/ldconfig in %%postun (bug 152236)

* Mon Apr  4 2005 Ray Strode <rstrode@redhat.com> 1:2.10.0-4
- use old modemlights applet that doesn't depend on gnome-system-tools

* Mon Mar 28 2005 Christopher Aillon <caillon@redhat.com>  2.10.0-3
- rebuilt

* Fri Mar 25 2005 Christopher Aillon <caillon@redhat.com> 2.10.0-2
- Update the GTK+ theme icon cache on (un)install

* Wed Mar 16 2005 Matthias Clasen <mclasen@redhat.com> - 2.10.0-1
- Rebuild against new libwnck
- Update to 2.10.0
- Drop upstreamed patch

* Wed Mar  2 2005 Mark McLoughlin <markmc@redhat.com> 1:2.9.6-2
- Stop libgswitchit using -Werror
- Rebuild with gcc4

* Wed Feb  9 2005 Matthias Clasen <mclasen@redhat.com> - 2.9.6-1
- Update to 2.9.6

* Wed Feb  9 2005 Mark McLoughlin <markmc@redhat.com> 2.9.5-4
- Add patch for mixer crash - #147282.
  Thanks Neil Paris for tracking down.

* Fri Feb  4 2005 Mark McLoughlin <markmc@redhat.com> - 2.9.5-2
- Fix schemas list (#146880, #147011)

* Mon Jan 31 2005 Matthias Clasen <mclasen@redhat.com> - 2.9.5-1
- Update to 2.9.5

* Sun Jan 30 2005 Florian La Roche <laroche@redhat.com>
- rebuild against new libs

* Thu Oct  7 2004 Mark McLoughlin <markmc@redhat.com> - 2.8.0-5
- Add patch to fix crash with gweather preferences (#134572)

* Thu Oct  7 2004 Mark McLoughlin <markmc@redhat.com> - 2.8.0-4
- Fix mixer icons bugs - #134224 and #134773

* Wed Sep 29 2004 Mark McLoughlin <markmc@redhat.com> 2.8.0-3
- Add new icons from upstream

* Tue Sep 21 2004 Mark McLoughlin <markmc@redhat.com> 2.8.0-2
- Remove the wireless applet and add patch to use the netstatus
  applet for backwards compat. bug #131652.

* Tue Sep 21 2004 Mark McLoughlin <markmc@redhat.com> 2.8.0-1
- Update to 2.8.0

* Wed Sep  1 2004 Mark McLoughlin <markmc@redhat.com> 2.7.3-2
- Rebuild

* Mon Aug 30 2004 Mark McLoughlin <markmc@redhat.com> 2.7.3-1
- Update to 2.7.3

* Fri Aug 27 2004 Mark McLoughlin <markmc@redhat.com> 2.7.2-2
- Run mc-install-default-macros in %%post
- Fixed small-volume patch from Nathan Fredrickson <nathan@silverorange.com>

* Wed Aug 18 2004 Mark McLoughlin <markmc@redhat.com> 2.7.2-1
- Update to 2.7.2

* Wed Aug 11 2004 Mark McLoughlin <markmc@redhat.com> 2.7.1-2
- Remove reference to cdplayer.schemas which has been removed (bug #129490)

* Thu Aug  5 2004 Mark McLoughlin <markmc@redhat.com> 2.7.1-1
- Update to 2.7.1
- Remove battstat-arg patch - upstream now

* Wed Jul 21 2004 Mark McLoughlin <markmc@redhat.com> 1:2.6.2.1-2
- rebuild

* Wed Jul 21 2004 Mark McLoughlin <markmc@redhat.com> 1:2.6.2.1-1
- Update to 2.6.2.1
- Re-do the way we decide whether to build the battstat applet.
  Should fix 122379
- Remove some patches that have gone upstream

* Tue Jun 22 2004 Mark McLoughlin <markmc@redhat.com> 1:2.6.0-8
- Fix typo with apmd requires

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt
- Remove ifarch'd buildrequires on apmd

* Thu May 05 2004 Nils Philippsen <nphilipp@redhat.com> 1:2.6.0-5
- fix #120354 (mixer applet forgets channel settings)

* Thu Apr 29 2004 Karsten Hopp <karsten@redhat.de> 1:2.6.0-4
- fix error during update on s390(x) due to missing battery applet

* Mon Apr 19 2004 Mark McLoughlin <markmc@redhat.com> 1:2.6.0-3
- Build battstat on ppc too

* Wed Apr 14 2004 Alex Larsson <alexl@redhat.com> 1:2.6.0-2
- Add gswitchit.schemas to SCHEMAS

* Wed Mar 31 2004 Mark McLoughlin <markmc@redhat.com> 2.6.0-1
- Update to 2.6.0

* Tue Mar 16 2004 Jeremy Katz <katzj@redhat.com> 1:2.5.7-4
- rebuild for new gstreamer

* Thu Mar 11 2004 Mark McLoughlin <markmc@redhat.com> 2.5.7-3
- Update Requires/BuildRequires to include gstreamer-plugins

* Thu Mar 11 2004 Mark McLoughlin <markmc@redhat.com> 2.5.7-2
- Rebuild

* Wed Mar 10 2004 Mark McLoughlin <markmc@redhat.com> 2.5.7-1
- Update to 2.5.7
- Add gnome-panel-devel BuildRequires

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Feb 26 2004 Alexander Larsson <alexl@redhat.com> 1:2.5.6-1
- update to 2..5.6

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jan 27 2004 Alexander Larsson <alexl@redhat.com> 1:2.5.4-1
- update to 2.5.4

* Fri Oct  3 2003 Alexander Larsson <alexl@redhat.com> 1:2.4.1-1
- 2.4.1

* Wed Aug 27 2003 Alexander Larsson <alexl@redhat.com> 1:2.3.7-1
- Add missing schemas to post (fixes #102710)
- Update to 2.3.7
- Add ifnarch apmd buildreq

* Mon Aug 18 2003 Alexander Larsson <alexl@redhat.com> 1:2.3.6-1
- update for gnome 2.3

* Mon Jul 28 2003 Havoc Pennington <hp@redhat.com> 1:2.2.2-3
- require the newer libgtop2 so it rebuilds vs. correct soname

* Fri Jul 18 2003  <timp@redhat.com> 1:2.2.2-2
- rebuild against new libgtop

* Mon Jul  7 2003 Havoc Pennington <hp@redhat.com> 1:2.2.2-1
- 2.2.2

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Feb 24 2003 Havoc Pennington <hp@redhat.com> 1:2.2.0-8
- change the volume applet size fix patch to work

* Mon Feb 24 2003 Elliot Lee <sopwith@redhat.com>
- debuginfo rebuild

* Sat Feb 22 2003 Havoc Pennington <hp@redhat.com> 1:2.2.0-6
- clamp size of volume applet to 24

* Thu Feb 20 2003 Havoc Pennington <hp@redhat.com> 1:2.2.0-5
- rebuild with datadir/wireless-applet and datadir/gen_util,
  someone got overzealous deleting unpackaged files instead
  of packaging them. #82279

* Fri Feb 14 2003 Jonathan Blandford <jrb@redhat.com> 1:2.2.0-4
- rebuild to get new gnome-panel

* Fri Feb 14 2003 Havoc Pennington <hp@redhat.com> 1:2.2.0-3
- nuke buildreq Xft

* Mon Feb 10 2003 Bill Nottingham <notting@redhat.com> 1:2.2.0-2
- fix path in modemlights patch

* Wed Feb  5 2003 Havoc Pennington <hp@redhat.com> 1:2.2.0-1
- 2.2.0

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Mon Dec 23 2002 Jeremy Katz <katzj@redhat.com> 1:2.1.3-1
- update to 2.1.3

* Tue Dec  3 2002 Havoc Pennington <hp@redhat.com>
- require newer panel, libgtop2
- require newer libgnomeui, libbonoboui

* Mon Dec  2 2002 Tim Powers <timp@redhat.com> 1:2.1.1-2
- remove unpackaged files from the buildroot

* Mon Dec  2 2002 Tim Powers <timp@redhat.com> 1:2.1.1-1
- update to 2.1.1
- add x86_64 to no_apm_archs

* Tue Aug 27 2002 Owen Taylor <otaylor@redhat.com>
- Register the cd player per-device (#72645).

* Fri Aug 23 2002 Owen Taylor <otaylor@redhat.com>
- Keep the CD device closed except when actually accessing it
  (bugzilla.gnome.org 91512)
- Register CD player so we can start only one CD player
  for display from magicdev. (#39208)

* Tue Aug 13 2002 Havoc Pennington <hp@redhat.com>
- add ppc ppc64 to no_apm_arches #67564

* Wed Jul 31 2002 Nalin Dahyabhai <nalin@redhat.com>
- include applets in libexecdir

* Mon Jul 29 2002 Havoc Pennington <hp@redhat.com>
- 2.0.1, and build with new gail
- 69971 (use correct ppp on/off commands)
- remove scrollkeeper dtd-compliance patch,
  fixed upstream apparently (patch doesn't apply anymore)

* Wed Jun 26 2002 Owen Taylor <otaylor@redhat.com>
- Fix %%find_lang

* Sun Jun 16 2002 Havoc Pennington <hp@redhat.com>
- rebuild with new libs
- remove temporary hack for too-old libgnomeui
- add /etc/sound stuff to file list

* Thu Jun 13 2002 Nalin Dahyabhai <nalin@redhat.com>
- rebuild in different environment

* Thu Jun 13 2002 Nalin Dahyabhai <nalin@redhat.com>
- fix a scrollkeeper validation bug

* Wed Jun 12 2002 Havoc Pennington <hp@redhat.com>
- remove panel-menu.schemas from the list of schemas.
- 2.0.0

* Fri Jun 07 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Wed Jun  5 2002 Havoc Pennington <hp@redhat.com>
- 1.105.0

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue May 21 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Tue May 21 2002 Havoc Pennington <hp@redhat.com>
- 1.103.0

* Fri May  3 2002 Havoc Pennington <hp@redhat.com>
- 1.100.0

* Fri Apr 19 2002 Havoc Pennington <hp@redhat.com>
- GNOME 2 version

* Mon Apr 15 2002 Havoc Pennington <hp@redhat.com>
- merge translations

* Thu Apr 11 2002 Havoc Pennington <hp@redhat.com>
- default battstat applet to vertical mode

* Thu Mar 21 2002 Havoc Pennington <hp@redhat.com>
- add patch to adapt to yahoo web site changes, #61561

* Tue Mar  5 2002 Havoc Pennington <hp@redhat.com>
- remove requires libghttp4

* Mon Mar  4 2002 Havoc Pennington <hp@redhat.com>
- no apm on sparc, #60538
- obsolete battstat_applet for Ximian compat, #51427
- use ifup/ifdown ppp0 instead of pppon/pppoff for default
  ppp command in modemlights, #54199

* Tue Feb 12 2002 Havoc Pennington <hp@redhat.com>
- 1.4.0.5, cross fingers
- add gconf-devel buildreq, though this is dubious as hell
  (pulled in by gtik using gnome-vfs, but if gtik actually
   accessed gconf it would fail due to gnorba conflict)
- patch totally busted charpick Makefile.am cflags override

* Thu Jan 24 2002 Havoc Pennington <hp@redhat.com>
- automake14

* Thu Aug 30 2001 Alex Larsson <alexl@redhat.com>
- Removed annoying broken battery full dialog #52861
- Also fix mixer applet for USB sound #52603

* Mon Aug 27 2001 Havoc Pennington <hp@redhat.com>
- Add po files from sources.redhat.com

* Wed Aug 15 2001 Alexander Larsson <alexl@redhat.com>
- Own /usr/share/gnome/gkb and /usr/share/gnome/help/*

* Wed Jul 18 2001 Havoc Pennington <hp@redhat.com>
- add some build requires
- remove ifarch build requires, replace with check in setup

* Wed Jul 11 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- sanitize specfile to RH style
- do not require apmd for s390 s390x

* Mon Jul  9 2001 Jonathan Blandford <jrb@redhat.com>
- new version

* Sun Jul 08 2001 Havoc Pennington <hp@redhat.com>
- remove extra .desktop file for battstat

* Sat Jul 07 2001 Havoc Pennington <hp@redhat.com>
- add battstat applet
- rearrange .desktop files for applets

* Tue Jun 12 2001 Than Ngo <than@redhat.com>
- fix isdn stuff to build against kernel-2.4.x
- use %%{_tmppath}

* Mon Jun 11 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- allow newer gettext versions

* Thu Mar 15 2001 Havoc Pennington <hp@redhat.com>
- translations

* Mon Feb 12 2001 Akira TAGOH <tagoh@redhat.com>
- Updated Japanese translation (ja.po, .desktop).
  Note: Please remove Source[23]: when release the next upstream version.

* Fri Jan 19 2001 Havoc Pennington <hp@redhat.com>
- 1.2.4

* Fri Aug 11 2000 Jonathan Blandford <jrb@redhat.com>
- Update Epoch

* Wed Jul 19 2000 Jonathan Blandford <jrb@redhat.com>
- Change slashapp to gnome-news app.

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Mon Jun 19 2000 Owen Taylor <otaylor@redhat.com
- %%defattr fixes
- Remove Docdir:

* Thu Jun 15 2000 Havoc Pennington <hp@redhat.com>
- 1.2.1
- use %%makeinstall
