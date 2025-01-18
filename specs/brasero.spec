%define basever %(echo %{version} | sed "s/\.[0-9]*$//")

%bcond cdrdao %[!(0%{?rhel} >= 9)]
%bcond cdrkit %[!(0%{?rhel} >= 9)]
%bcond dvdrwtools %[!(0%{?rhel} >= 9)]
%bcond nautilus %[!(0%{?fedora} >= 37 || 0%{?rhel} >= 10)]
%bcond plparser %[!(0%{?rhel} >= 10)]

Name:      brasero
Version:   3.12.3
Release:   12%{?dist}
Summary:   Gnome CD/DVD burning application


# see https://bugzilla.gnome.org/show_bug.cgi?id=683503
# SVG files are GPL-2.0-only
# data/icons/hicolor_actions_scalable_transform-crop-and-resize.svg is CC-BY-SA-2.0
# libbrasero-media is GPL-2.0-or-later WITH GStreamer-exception-2008                                                                                                                         
License:   GPL-3.0-or-later AND LGPL-2.0-or-later AND GPL-2.0-only AND CC-BY-SA-2.0 AND GPL-2.0-or-later WITH GStreamer-exception-2008
URL:       https://wiki.gnome.org/Apps/Brasero
Source0:   https://download.gnome.org/sources/%{name}/%{basever}/%{name}-%{version}.tar.xz
# https://gitlab.gnome.org/GNOME/brasero/-/merge_requests/30
Patch0:    0001-Fix-gcc-14.x-build-failure.patch

BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0) >= 0.11.92
BuildRequires:  pkgconfig(gtk+-3.0) >= 2.99.0
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libburn-1) >= 0.4.0
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libisofs-1) >= 0.6.4
BuildRequires:  pkgconfig(libnotify) >= 0.7.0
%if %{with nautilus}
BuildRequires:  pkgconfig(libnautilus-extension) >= 2.22.2
%endif
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6.0
BuildRequires:  pkgconfig(sm)
%if %{with plparser}
BuildRequires:  pkgconfig(totem-plparser) >= 2.29.1
%endif
BuildRequires:  pkgconfig(tracker-sparql-3.0)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  yelp-tools

%{?with_dvdrwtools:Requires:  dvd+rw-tools}
%{?with_cdrkit:Requires:  wodim}
%{?with_cdrkit:Requires:  genisoimage}
Requires:  %{name}-libs%{?_isa} = %{version}-%{release}
%ifnarch s390x
%{?with_cdrdao:Requires:  cdrdao}
%endif
%{?with_cdrkit:Recommends: icedax}

%if %{without nautilus}
Obsoletes: %{name}-nautilus < %{version}-%{release}
%endif

%description
Simple and easy to use CD/DVD burning application for the Gnome
desktop.


%package   libs
Summary:   Libraries for %{name}

%description libs
The %{name}-libs package contains the runtime shared libraries for
%{name}.


%if %{with nautilus}
%package   nautilus
Summary:   Nautilus extension for %{name}
Requires:  %{name}%{?_isa} = %{version}-%{release}

%description nautilus
The %{name}-nautilus package contains the brasero nautilus extension.
%endif


%package   devel
Summary:   Headers for developing programs that will use %{name}
Requires:  %{name}-libs%{?_isa} = %{version}-%{release}


%description devel
This package contains the static libraries and header files needed for
developing brasero applications.


%prep
%autosetup -p1


%build
%configure \
        %{!?with_nautilus:--disable-nautilus} \
        --enable-libburnia \
        --enable-search \
        %{!?with_plparser:--disable-playlist} \
        --enable-preview \
        --enable-inotify \
        %{!?with_cdrdao:--disable-cdrdao} \
        %{!?with_cdrkit:--disable-cdrkit} \
        %{!?with_dvdrwtools:--disable-growisofs} \
        --disable-caches \
        --disable-static
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
%make_build


%install
%make_install
find %{buildroot} -type f -name "*.la" -delete
%find_lang %{name}

# Update the screenshot shown in the software center
#
# NOTE: It would be *awesome* if this file was pushed upstream.
#
# See http://people.freedesktop.org/~hughsient/appdata/#screenshots for more details.
#
appstream-util replace-screenshots $RPM_BUILD_ROOT%{_datadir}/metainfo/brasero.appdata.xml \
  https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/brasero/a.png \
  https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/brasero/b.png \
  https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/brasero/c.png 


%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%ldconfig_scriptlets libs


%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README
%{_mandir}/man1/%{name}.*
%{_bindir}/*
%{_libdir}/brasero3
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/help/*
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/mime/packages/*
%{_datadir}/GConf/gsettings/brasero.convert
%{_datadir}/glib-2.0/schemas/org.gnome.brasero.gschema.xml

%files libs
%{_libdir}/*.so.*
%{_libdir}/girepository-1.0/*.typelib

%if %{with nautilus}
%files nautilus
%{_libdir}/nautilus/extensions-3.0/*.so
%{_datadir}/applications/brasero-nautilus.desktop
%endif

%files devel
%doc %{_datadir}/gtk-doc/html/libbrasero-media
%doc %{_datadir}/gtk-doc/html/libbrasero-burn
%doc ChangeLog
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/brasero3
%{_datadir}/gir-1.0/*.gir


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Aug 09 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 3.12.3-11
- Disable playlist support on RHEL 10+

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jun 06 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 3.12.3-9
- Fix build with GCC 14

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Aug 15 2022 Kalev Lember <klember@redhat.com> - 3.12.3-4
- Obsolete brasero-nautilus subpackage

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Sep 20 2021 David King <amigadave@amigadave.com> - 3.12.3-1
- Update to 3.12.3

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 17 2021 Jiri Kucera <jkucera@redhat.com> - 3.12.2-16
- Drop dependencies on cdrdao, cdrkit, and dvd+rw-tools for el9+

* Mon Mar 15 2021 Kalev Lember <klember@redhat.com> - 3.12.2-15
- Switch to Tracker 3

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 21 2021 Adam Jackson <ajax@redhat.com> - 3.12.2-13
- Relax Requires: icedax to Recommends

* Thu Jan 07 2021 David King <amigadave@amigadave.com> - 3.12.2-12
- Use pkgconfig for BuildRequires
- Depend on tracker only on Fedora

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul  9 2018 Peter Robinson <pbrobinson@fedoraproject.org> 3.12.2-6
- Update requires

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.12.2-4
- Switch to %%ldconfig_scriptlets

* Sat Jan 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.12.2-3
- Remove obsolete scriptlets

* Thu Aug 10 2017 Kalev Lember <klember@redhat.com> - 3.12.2-2
- Rebuilt for libtotem-plparser soname bump

* Mon Jul 31 2017 Kalev Lember <klember@redhat.com> - 3.12.2-1
- Update to 3.12.2
- Use desktop-file-validate instead of desktop-file-install
- Update download URLs

* Mon Jul 31 2017 Kalev Lember <klember@redhat.com> - 3.12.1-7
- Rebuilt for libtotem-plparser soname bump

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 17 2015 Richard Shaw <hobbes1069@gmail.com> - 3.12.1-3
- Add patch to fix libdvdcss version detection, fixes BZ#1193628.
- Use %%license tag.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 28 2015 Matthias Clasen <mclasen@redhat.com> - 3.12.1-1
- Update to 3.12.1

* Mon Mar 30 2015 Richard Hughes <rhughes@redhat.com> - 3.12.0-2
- Use better AppData screenshots

* Thu Nov 13 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.0-1
- Update to 3.12.0

* Tue Sep 16 2014 Kalev Lember <kalevlember@gmail.com> - 3.11.4-2
- Drop last GConf2 remnants (#1142397)

* Thu Sep 11 2014 Kalev Lember <kalevlember@gmail.com> - 3.11.4-1
- Update to 3.11.4

* Thu Aug 21 2014 Kalev Lember <kalevlember@gmail.com> - 3.11.3-11
- Backport a patch to fix crashes with gtk+ 3.13.x

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.11.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Aug 12 2014 Rex Dieter <rdieter@fedoraproject.org> - 3.11.3-9
- update scriptlets
- tighten subpkg dep
- %%check: validate appdata

* Sat Aug  2 2014 Peter Robinson <pbrobinson@fedoraproject.org> 3.11.3-8
- Base package should depend on -libs

* Mon Jul 28 2014 Kalev Lember <kalevlember@gmail.com> - 3.11.3-7
- Rebuilt once more for tracker

* Mon Jul 28 2014 Peter Robinson <pbrobinson@fedoraproject.org> 3.11.3-6
- rebuild (tracker)

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 3.11.3-5
- Rebuilt for gobject-introspection 1.41.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.11.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 19 2014 Kalev Lember <kalevlember@gmail.com> - 3.11.3-3
- Support tracker 1.0 API

* Fri Dec 27 2013 Adam Williamson <awilliam@redhat.com> - 3.11.3-2
- rebuild for new tracker

* Tue Dec 17 2013 Richard Hughes <rhughes@redhat.com> - 3.11.3-1
- Update to 3.11.3

* Mon Dec 09 2013 Richard Hughes <rhughes@redhat.com> - 3.11.0-1
- Update to 3.11.0

* Sat Nov 30 2013 Kalev Lember <kalevlember@gmail.com> - 3.10.0-1
- Update to 3.10.0

* Thu Sep 19 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.0-4
- Rebuilt for totem-pl-parser soname bump

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul  2 2013 Matthias Clasen <mclasen@redhat.com> - 3.8.0-2
- Cosmetic spec file cleanups

* Tue Mar 26 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.0-1
- Update to 3.8.0

* Wed Mar  6 2013 Matthias Clasen <mclasen@redhat.com> - 3.7.91-1
- Update to 3.7.91

* Sun Jan 27 2013 Kalev Lember <kalevlember@gmail.com> - 3.6.1-2
- Build with tracker 0.16 API

* Mon Nov 12 2012 Tomas Bzatek <tbzatek@redhat.com> - 3.6.1-1
- Update to 3.6.1

* Wed Oct 10 2012 Tomas Bzatek <tbzatek@redhat.com> - 3.6.0-2
- Fix BD media disc copy

* Tue Sep 25 2012 Richard Hughes <hughsient@gmail.com> - 3.6.0-1
- Update to 3.6.0

* Wed Sep 19 2012 Richard Hughes <hughsient@gmail.com> - 3.5.92-1
- Update to 3.5.92

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 17 2012 Kalev Lember <kalevlember@gmail.com> - 3.4.1-1
- Update to 3.4.1

* Tue Mar 27 2012 Richard Hughes <hughsient@gmail.com> - 3.4.0-1
- Update to 3.4.0

* Wed Mar 21 2012 Kalev Lember <kalevlember@gmail.com> - 3.3.92-1
- Update to 3.3.92

* Tue Mar  6 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.91-2
- Rebuild against new tracker

* Tue Mar  6 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.91-1
- Update to 3.3.91

* Tue Feb 28 2012 Matthias Clasen <mclasen@redhat.com> - 3.2.0-3
- Rebuild against new tracker

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Sep 27 2011 Ray <rstrode@redhat.com> - 3.2.0-1
- Update to 3.2.0

* Fri May  6 2011 Christopher Aillon <caillon@redhat.com> - 3.0.0-1
- Update scriptlets per packaging guidelines

* Mon Apr  4 2011 Matthias Clasen <mclasen@redhat.com> - 3.0.0-1
- Update to 3.0.0

* Fri Mar 25 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.93-1
- Update to 2.91.93

* Tue Mar  8 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.91-1
- Update to 2.91.91

* Tue Feb 22 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.90-1
- Update to 2.91.90

* Thu Feb 10 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.6-4
- Rebuild against newer gtk

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.91.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Feb 06 2011 Bastien Nocera <bnocera@redhat.com> 2.91.6-2
- Fix GTK+ name in pkg-config file

* Wed Feb  2 2011 Christopher Aillon <caillon@redhat.com> - 2.91.6-1
- Update to 2.91.6

* Thu Jan 13 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.5-2
- Move girs to -devel

* Mon Jan 10 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.5-1
- Update to 2.91.5

* Fri Jan  7 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.4.2-1
- Update to 2.91.4.2

* Fri Dec  3 2010 Matthias Clasen <mclasen@redhat.com> - 2.91.3-1
- Update to 2.91.3

* Thu Nov 11 2010 Matthias Clasen <mclasen@redhat.com> - 2.91.2-1
- Update to 2.91.2

* Wed Nov  3 2010 Matthias Clasen <mclasen@redhat.com> - 2.91.2-0.2.gitcede364
- Rebuild against libnotify 0.7.0

* Mon Nov  1 2010 Matthias Clasen <mclasen@redhat.com> - 2.91.2-0.1.gitcede364
- Git snapshot that builds against gtk3

* Wed Oct  6 2010 Matthias Clasen <mclasen@redhat.com> - 2.91.0-1
- Update to 2.91.0

* Tue Sep 28 2010 Matthias Clasen <mclasen@redhat.com> - 2.32.0-1
- Update to 2.32.0

* Wed Sep 22 2010 Matthias Clasen <mclasen@redhat.com> - 2.31.92-1
- Update to 2.31.92

* Tue Aug 31 2010 Matthias Clasen <mclasen@redhat.com> - 2.31.91-1
- Update to 2.31.91

* Thu Aug 19 2010 Matthias Clasen <mclasen@redhat.com> - 2.31.90-1
- Update to 2.31.90

* Thu Jul 15 2010 Colin Walters <walters@verbum.org> - 2.31.5-2
- Rebuild with new gobject-introspection

* Tue Jul 13 2010 Matthias Clasen <mclasen@redhat.com> - 2.31.5-1
- Update to 2.31.5

* Wed Jun 30 2010 Matthias Clasen <mclasen@redhat.com> - 2.31.4-1
- Update to 2.31.4

* Tue Jun  8 2010 Matthias Clasen <mclasen@redhat.com> - 2.31.3-1
- Update to 2.31.3

* Thu May 27 2010 Matthias Clasen <mclasen@redhat.com> - 2.31.2-1
- Update to 2.31.2

* Tue Apr 27 2010 Matthias Clasen <mclasen@redhat.com> - 2.30.1-1
- Update to 2.30.1
- Spec file cleanups

* Mon Mar 29 2010 Matthias Clasen <mclasen@redhat.com> - 2.30.0-1
- Update to 2.30.0

* Thu Mar 11 2010 Matthias Clasen <mclasen@redhat.com> - 2.29.92-1
- Update to 2.29.92

* Wed Mar  3 2010 Matthias Clasen <mclasen@redhat.com> - 2.29.91-2
- Fix a nautilus cd-burner crash

* Mon Feb 22 2010 Matthias Clasen <mclasen@redhat.com> - 2.29.91-1
- Update to 2.29.91

* Wed Feb 10 2010 Bastien Nocera <bnocera@redhat.com> 2.29.90-1
- Update to 2.29.90

* Tue Jan 26 2010 Bastien Nocera <bnocera@redhat.com> 2.29.4-2
- Add patch for new totem-pl-parser API
- Fix introspection building

* Tue Dec 22 2009 Matthias Clasen <mclasen@redhat.com> 2.29.4-1
- Update to 2.29.4

* Wed Dec  2 2009 Bastien Nocera <bnocera@redhat.com> 2.29.3-2
- Make libbeagle dep more automatic

* Tue Dec 01 2009 Bastien Nocera <bnocera@redhat.com> 2.29.3-1
- Update to 2.29.3

* Thu Nov 12 2009 Matthias Clasen <mclasen@redhat.com> 2.28.2-3
- Obsolete nautilus-cd-burner-devel and -libs as well

* Mon Oct 26 2009 Matthias Clasen <mclasen@redhat.com> 2.28.2-2
- Avoid a stray underline in a button label

* Tue Oct 20 2009 Matthias Clasen <mclasen@redhat.com> 2.28.2-1
- Update to 2.28.2

* Wed Oct 07 2009 Bastien Nocera <bnocera@redhat.com> 2.28.1-2
- Fix command-line parsing (#527484)

* Mon Oct  5 2009 Matthias Clasen <mclasen@redhat.com> - 2.28.1-1
- Update to 2.28.1, fixes a number of crashes and other serious bugs:
 - Fix a crash when we try to download a missing gstreamer plugin through PK
 - Don't fail if a drive cannot be checksumed after a burn
 - Fix a data corruption when libisofs was used for a dummy session
 - Fix #596625: brasero crashed with SIGSEGV in brasero_track_data_cfg_add
 - Fix progress reporting
 ...

* Fri Oct  2 2009 Matthias Clasen <mclasen@redhat.com> - 2.28.0-2
- Fix ejecting after burning

* Tue Sep 22 2009 Matthias Clasen <mclasen@redhat.com> - 2.28.0-1
- Update to 2.28.0

* Fri Sep 11 2009 Karsten Hopp <karsten@redhat.com> 2.27.92-2
- fix requirements on s390, s390x where we don't have cdrdao

* Mon Sep  7 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.92-1
- Update to 2.27.92

* Tue Aug 25 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.91-1
- Update to 2.27.91

* Mon Aug 10 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.90-1
- Update to 2.27.90

* Mon Aug  3 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.5-2
- Fix a nautilus segfault when burning  

* Tue Jul 28 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.5-1
- Update to 2.27.5

* Sun Jul 26 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.4-3
- Move ChangeLog to -devel to save some space

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.27.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 14 2009 Matthias Clasen <mclasen@redhat.com> 2.27.4-1
- Update to 2.27.4

* Tue Jun 16 2009 Matthias Clasen <mclasen@redhat.com> 2.27.3-1
- Update to 2.27.3

* Wed May 27 2009 Bastien Nocera <bnocera@redhat.com> 2.27.2-1
- Update to 2.27.2

* Tue May 26 2009 Bastien Nocera <bnocera@redhat.com> 2.27.1-2
- Add missing unique-devel BR

* Mon May 18 2009 Bastien Nocera <bnocera@redhat.com> 2.27.1-1
- Update to 2.27.1

* Fri May  1 2009 Bill Nottingham <notting@redhat.com> - 2.26.1-3
- require main package in brasero-nautilus (#498632)

* Fri Apr 17 2009 Denis Leroy <denis@poolshark.org> - 2.26.1-2
- Obsoletes nautilus-cd-burner

* Tue Apr 14 2009 Matthias Clasen <mclasen@redhat.com> - 2.26.1-1
- Update to 2.26.1
- See http://download.gnome.org/sources/brasero/2.26/brasero-2.26.1.news

* Mon Apr 13 2009 Denis Leroy <denis@poolshark.org> - 2.26.0-2
- Removed duplicate desktop source

* Sun Mar 29 2009 Matthias Clasen <mclasen@redhat.com> - 2.26.0-1
- Update to 2.26.0

* Mon Mar 02 2009 - Bastien Nocera <bnocera@redhat.com> - 2.25.91.2-3
- Fix icon and Bugzilla component

* Mon Mar 02 2009 - Bastien Nocera <bnocera@redhat.com> - 2.25.91.2-2
- Fix regressions in burn:/// and blank media handling

* Tue Feb 24 2009 Denis Leroy <denis@poolshark.org> - 2.25.91.2-1
- Update to upstream 2.25.91.2
- Dvdcss patch upstreamed
- Split nautilus extension into subpackage (#485918)

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.25.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb  7 2009 Denis Leroy <denis@poolshark.org> - 2.25.90-2
- Added patch to fix dynamic load of libdvdcss (#484413)

* Tue Feb  3 2009 Denis Leroy <denis@poolshark.org> - 2.25.90-1
- Update to upstream 2.25.90
- Split media library into separate RPM (#483754)
- Added patch to validate desktop files

* Tue Jan 20 2009 Denis Leroy <denis@poolshark.org> - 0.9.1-1
- Update to upstream 0.9.1
- Added development package

* Tue Dec 16 2008 Denis Leroy <denis@poolshark.org> - 0.8.3-1
- Update to upstream 0.8.4
- Enabled nautilus extension

* Mon Sep 15 2008 Denis Leroy <denis@poolshark.org> - 0.8.2-1
- Update to upstream 0.8.2

* Wed Aug 27 2008 Denis Leroy <denis@poolshark.org> - 0.8.1-1
- Update to upstream 0.8.1
- Desktop patch upstreamed

* Sun Jul  6 2008 Denis Leroy <denis@poolshark.org> - 0.7.91-1
- Update to unstable 0.7.91
- open flags patch upstreamed

* Wed Jun 11 2008 Denis Leroy <denis@poolshark.org> - 0.7.90-1
- Update to unstable 0.7.90
- Added patch to validate desktop file
- BRs updated

* Fri May 16 2008 Denis Leroy <denis@poolshark.org> - 0.7.1-4
- Rebuild for new totem-pl-parser

* Sat Feb 23 2008 Denis Leroy <denis@poolshark.org> - 0.7.1-3
- Fixed desktop mime field

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.7.1-2
- Autorebuild for GCC 4.3

* Tue Jan 29 2008 Denis Leroy <denis@poolshark.org> - 0.7.1-1
- Update to 0.7.1 upstream, bugfix release

* Sun Dec 30 2007 Denis Leroy <denis@poolshark.org> - 0.7.0-1
- Update to upstream 0.7.0, updated BRs
- Forward-ported open() permission patch

* Mon Dec 10 2007 Denis Leroy <denis@poolshark.org> - 0.6.1-4
- Changed totem-devel req to totem-pl-parser-devel

* Sun Dec  9 2007 Denis Leroy <denis@poolshark.org> - 0.6.1-3
- Rebuild with new libbeagle

* Fri Nov  9 2007 Denis Leroy <denis@poolshark.org> - 0.6.1-2
- Rebuild to pick up new totem version (#361361)

* Sat Aug 25 2007 Denis Leroy <denis@poolshark.org> - 0.6.1-1
- Update to upstream version 0.6.1
- Filter UI patch is now upstream

* Fri Aug 17 2007 Denis Leroy <denis@poolshark.org> - 0.6.0-2
- Updated License tag
- Fixed open() O_CREAT problem

* Fri Aug 10 2007 Denis Leroy <denis@poolshark.org> - 0.6.0-1
- Update to 0.6.0
- Removed libburn support until it compiles against libisofs 0.2.8
- Fixed project URL
- Added patch to port to new Gtk+ tooltip interface
- Added patch to fix filter dialog crash

* Sun Jun  3 2007 Denis Leroy <denis@poolshark.org> - 0.5.2-4
- Removed beagle support for ppc64

* Tue May 22 2007 Denis Leroy <denis@poolshark.org> - 0.5.2-3
- Added umask 022 to scriptlets (#230781)

* Mon May 21 2007 Denis Leroy <denis@poolshark.org> - 0.5.2-2
- Rebuild to pick up new totem library

* Mon Feb 26 2007 Denis Leroy <denis@poolshark.org> - 0.5.2-1
- Update to 0.5.2
- Removed libisofs patch, now upstream

* Wed Jan 17 2007 Denis Leroy <denis@poolshark.org> - 0.5.1-2
- Added patch to support libisofs.so.4 and libburn.so.6

* Thu Nov 16 2006 Denis Leroy <denis@poolshark.org> - 0.5.1-1
- Update to 0.5.1

* Sun Oct 29 2006 Denis Leroy <denis@poolshark.org> - 0.5.0-1
- Update to 0.5.0
- Updated icon paths
- Added gconf schemas sections

* Tue Oct  3 2006 Denis Leroy <denis@poolshark.org> - 0.4.4-3
- fixed homepage URL

* Tue Sep 26 2006 Denis Leroy <denis@poolshark.org> - 0.4.4-2
- BRs cleanup

* Fri Sep 22 2006 Denis Leroy <denis@poolshark.org> - 0.4.4-1
- First version
foo
