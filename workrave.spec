%global	gnome_flashback	1
%global	mate		1
%global	xfce		1

Name: workrave
Version: 1.10.50
Release: 3%{?dist}
Summary: Program that assists in the recovery and prevention of RSI
# Based on older packages by Dag Wieers <dag@wieers.com> and Steve Ratcliffe
License: GPLv3+
URL: http://www.workrave.org/
%global tag %(echo %{version} | sed -e 's/\\./_/g')
Source0: https://github.com/rcaelers/workrave/archive/v%{tag}/%{name}-v%{tag}.tar.gz
# Support GNOME Shell 43, backport of https://github.com/rcaelers/workrave/pull/430
Patch0:  578180d0982dd8f0dbe72574ae4758e6903691bb.patch

Obsoletes: %{name}-gtk2 < 1.10.37-1
Provides: %{name}-gtk2 = %{?epoch:%{epoch}:}%{version}-%{release}

BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: libX11-devel
BuildRequires: libXScrnSaver-devel
BuildRequires: pkgconfig(ice)
BuildRequires: pkgconfig(sm)
BuildRequires: pkgconfig(glib-2.0) >= 2.28.0
BuildRequires: pkgconfig(gio-2.0) >= 2.26.0
BuildRequires: pkgconfig(gtk+-3.0) >= 3.0.0
BuildRequires: pkgconfig(sigc++-2.0) >= 2.2.4.2
BuildRequires: pkgconfig(glibmm-2.4) >= 2.28.0
BuildRequires: pkgconfig(gtkmm-3.0) >= 3.0.0
BuildRequires: gobject-introspection-devel >= 0.6.7
BuildRequires: pkgconfig(indicator3-0.4) >= 0.3.19
BuildRequires: pkgconfig(dbusmenu-glib-0.4) >= 0.1.1
BuildRequires: pkgconfig(dbusmenu-gtk3-0.4) >= 0.3.95
BuildRequires: boost-devel
BuildRequires: python3
BuildRequires: python3-devel
BuildRequires: python3-cheetah
BuildRequires: python3-jinja2
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(libpulse) >= 0.9.15
BuildRequires: pkgconfig(libpulse-mainloop-glib) >= 0.9.15
BuildRequires: gettext
BuildRequires: intltool
BuildRequires: autoconf, automake, libtool, autoconf-archive
BuildRequires: desktop-file-utils
%if 0%{?gnome_flashback}
BuildRequires: pkgconfig(libgnome-panel)
%endif
%if 0%{?xfce} || 0%{?mate}
BuildRequires: pkgconfig(gtk+-3.0)
%endif
%if 0%{?xfce}
BuildRequires: pkgconfig(libxfce4panel-2.0) >= 4.12
%endif
%if 0%{?mate}
BuildRequires: pkgconfig(libmatepanelapplet-4.0)
%endif

Requires: dbus
%if 0%{?fedora}
Recommends: gstreamer1-plugins-base
Recommends: gstreamer1-plugins-good
%endif
Obsoletes: %{name}-devel < %{version}-%{release}

%global _description Workrave is a program that assists in the recovery and prevention of\
Repetitive Strain Injury (RSI). The program frequently alerts you to\
take micro-pauses, rest breaks and restricts you to your daily limit.

%description
%{_description}

%package gnome-flashback
Requires: %{name} = %{version}-%{release}
Summary: Workrave applet for GNOME Flashback

%description gnome-flashback
%{_description}

This package provides an applet for the GNOME Flashback panel.

%package mate
Requires: %{name} = %{version}-%{release}
Summary: Workrave applet for MATE

%description mate
%{_description}

This package provides an applet for the MATE panel.

%package xfce
Requires: %{name} = %{version}-%{release}
Summary: Workrave applet for Xfce

%description xfce
%{_description}

This package provides an applet for the Xfce panel.


%prep
%setup -q -n workrave-%{tag}
%patch0 -p1
touch ChangeLog
# https://bugzilla.redhat.com/show_bug.cgi?id=304121
sed -i -e '/^DISTRIBUTION_HOME/s/\/$//' frontend/gtkmm/src/Makefile.*


# upstream is python2
2to3 --write --nobackups libs/dbus/bin/dbusgen.py
%{__python3} %{_rpmconfigdir}/redhat/pathfix.py -pni %{__python3} libs/dbus/bin/dbusgen.py
sed -i 's/AC_CHECK_PROG(PYTHON, python, python)/AC_CHECK_PROG(PYTHON, python3, python3)/' configure.ac

%build
if [ ! -x configure ]; then
  ### Needed for snapshot releases.
  NOCONFIGURE=1 ./autogen.sh
fi

# gnome3 is flashback panel applet, not gnome-shell
%configure \
%if 0%{?gnome_flashback}
  --enable-gnome3 \
%else
  --disable-gnome3 \
%endif
%if 0%{?mate}
  --enable-mate \
%else
  --disable-mate \
%endif
%if 0%{?xfce}
  --enable-xfce \
%else
  --disable-xfce \
%endif
  --disable-static --disable-xml

make V=1 %{_smp_mflags}

%install
make install DESTDIR=%{buildroot}

find %{buildroot} -name '*.la' -delete
# workrave does not provide a public API
rm -f %{buildroot}%{_datadir}/gir-1.0/*.gir
rm -f %{buildroot}%{_libdir}/*.so

%find_lang %{name}

desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  --delete-original \
  %{buildroot}%{_datadir}/applications/%{name}.desktop


%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README.md
%{_bindir}/workrave
%{_datadir}/workrave/
%{_datadir}/sounds/workrave/
%{_datadir}/icons/hicolor/16x16/apps/workrave.png
%{_datadir}/icons/hicolor/24x24/apps/workrave.png
%{_datadir}/icons/hicolor/32x32/apps/workrave.png
%{_datadir}/icons/hicolor/48x48/apps/workrave.png
%{_datadir}/icons/hicolor/64x64/apps/workrave.png
%{_datadir}/icons/hicolor/96x96/apps/workrave.png
%{_datadir}/icons/hicolor/128x128/apps/workrave.png
%{_datadir}/icons/hicolor/scalable/workrave-sheep.svg
%{_datadir}/icons/hicolor/scalable/apps/workrave.svg
%{_datadir}/metainfo/workrave.appdata.xml
%{_datadir}/applications/workrave.desktop
%{_datadir}/dbus-1/services/org.workrave.Workrave.service
%{_datadir}/glib-2.0/schemas/org.workrave.*.xml
# support library for gtk3 applets
%{_libdir}/girepository-1.0/Workrave-1.0.typelib
%{_libdir}/libworkrave-private-1.0.so.*
# gnome-shell extension
%dir %{_datadir}/gnome-shell/
%dir %{_datadir}/gnome-shell/extensions/
%{_datadir}/gnome-shell/extensions/workrave@workrave.org/
# cinnamon applet
%dir %{_datadir}/cinnamon/
%dir %{_datadir}/cinnamon/applets/
%{_datadir}/cinnamon/applets/workrave@workrave.org/
# indicator applet
%dir %{_libdir}/indicators3/
%dir %{_libdir}/indicators3/7/
%{_libdir}/indicators3/7/libworkrave.so

%if 0%{?gnome_flashback}
%files gnome-flashback
%{_libdir}/gnome-panel/modules/libworkrave-applet.so
%endif

%if 0%{?xfce}
%files xfce
%{_libdir}/xfce4/panel/plugins/libworkrave-plugin.so
%{_datadir}/xfce4/panel/plugins/workrave-xfce-applet.desktop
%endif

%if 0%{?mate}
%files mate
%{_libdir}/mate-applets/workrave-applet
%{_datadir}/dbus-1/services/org.mate.panel.applet.WorkraveAppletFactory.service
%{_datadir}/mate-panel/applets/org.workrave.WorkraveApplet.mate-panel-applet
%{_datadir}/mate-panel/ui/workrave-menu.xml
%endif

%changelog
* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.50-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.50-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 04 2022 Yaakov Selkowitz <yselkowi@redhat.com> - 1.10.50-1
- Update to 1.10.50
- Enable GNOME Flashback applet
- Support GNOME Shell 42 (#2132504) and 43 (#2132507)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.49-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.49-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan 09 2022 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.10.49-1
- Update to 1.10.49
- Fixes rhbz#1986369 and rhbz#2035023

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.45-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 06 2021 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.10.45-1
- Update to 1.10.45
- Drop upstreamed patch

* Mon Feb 08 2021 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.10.44-3
- Build against xfce-4.16

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.44-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 02 2020 Lukas Zapletal <lzap+rpm@redhat.com> - 1.10.44-1
- new version

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Mar 27 2020 Lukas Zapletal <lzap+rpm@redhat.com> - 1.10.37-1
- new version

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.20-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.20-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 12 2019 Lukas Zapletal <lzap+rpm@redhat.com> - 1.10.20-5
- Updated X11 and python3 deps

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 14 2017 Yaakov Selkowitz <yselkowi@redhat.com> - 1.10.20-1
- new version (#1508256)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Sep 16 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 1.10.16-1
- new version (#1376625)

* Thu May 12 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 1.10.15-1
- new version (#1321458)

* Fri Feb 26 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 1.10.10-1
- new version
- Add Cinnamon, Indicator, MATE, Xfce applets
- Cleanup spec

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.10-8
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 1.10-6
- Rebuilt for gobject-introspection 1.41.4

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May  3 2013 Tomáš Mráz <tmraz@redhat.com> - 1.10-3
- do not build the panel applet

* Mon Mar 25 2013 Peter Robinson <pbrobinson@fedoraproject.org> 1.10-2
- Add missing distag

* Tue Feb 19 2013 Tomáš Mráz <tmraz@redhat.com> - 1.10-1
- new upstream release

* Fri Feb  8 2013 Tomáš Mráz <tmraz@redhat.com> - 1.9.911-0.2.20130107git6f9bc5d
- drop --vendor from desktop-file-install call

* Tue Jan  8 2013 Tom Callaway <spot@fedoraproject.org> - 1.9.911-0.1.20130107git6f9bc5d
- update to 1.9.911 checkout from github
- build for gnome3

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.4-5
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov  7 2011 Tomas Mraz <tmraz@redhat.com> - 1.9.4-3
- rebuilt with new libpng

* Tue Jun 28 2011 Tomas Mraz <tmraz@redhat.com> - 1.9.4-2
- no longer needs gnet2

* Wed Apr 06 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 1.9.4-1
- New upstream bug fix release. Closes rhbz#693958
- https://github.com/rcaelers/workrave/blob/b491d9b5054b5571d5b4ff0f6c9137133735129d/NEWS
- Drop buildroot definition and clean section 

* Thu Feb 10 2011 Tomas Mraz <tmraz@redhat.com> - 1.9.3-4
- due to changes in gnome applet API we have to build without
  gnome support

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Feb  3 2011 Tomas Mraz <tmraz@redhat.com> - 1.9.3-2
- rebuilt with new gnome-panel

* Fri Dec 17 2010 Tomas Mraz <tmraz@redhat.com> - 1.9.3-1
- new upstream release with bug fixes and usability improvements

* Wed Nov  3 2010 Tomas Mraz <tmraz@redhat.com> - 1.9.2-1
- new upstream release hopefully fixing at least some of the aborts

* Mon Apr 26 2010 Tomas Mraz <tmraz@redhat.com> - 1.9.1-4
- better guard for BadWindow errors in input monitor (#566156)

* Wed Mar 17 2010 Tomas Mraz <tmraz@redhat.com> - 1.9.1-3
- fix FTBFS (#564917)

* Thu Jan 28 2010 Tomas Mraz <tmraz@redhat.com> - 1.9.1-2
- do not build against gdome2 - not too useful optional feature

* Tue Dec  8 2009 Tomas Mraz <tmraz@redhat.com> - 1.9.1-1
- new upstream version

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Feb 27 2009 Tomas Mraz <tmraz@redhat.com> - 1.9.0-3
- fix build with new gcc 4.4 and glibc

* Fri Sep 26 2008 Tomas Mraz <tmraz@redhat.com> - 1.9.0-1
- new upstream version

* Fri Apr  4 2008 Tomas Mraz <tmraz@redhat.com> - 1.8.5-4
- fix locking/unlocking with gnome-screensaver (#207058)
- make it build with current libsigc++

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.8.5-3
- Autorebuild for GCC 4.3

* Tue Feb 19 2008 Tomas Mraz <tmraz@redhat.com> - 1.8.5-2
- make it build on gcc-4.3

* Mon Jan  7 2008 Tomas Mraz <tmraz@redhat.com> - 1.8.5-1
- upgrade to latest upstream version

* Wed Aug 22 2007 Tomas Mraz <tmraz@redhat.com> - 1.8.4-4
- applet counters don't start properly
- license tag fix

* Wed Apr 18 2007 Tomas Mraz <tmraz@redhat.com> - 1.8.4-3
- fixed applet crash (#236543)

* Mon Mar 26 2007 Tomas Mraz <tmraz@redhat.com> - 1.8.4-2
- new upstream version
- add datadir/pixmaps/workrave to files (#233815)

* Thu Sep  7 2006 Tomas Mraz <tmraz@redhat.com> - 1.8.3-2
- rebuilt for FC6

* Wed May 31 2006 Tomas Mraz <tmraz@redhat.com> - 1.8.3-1
- New upstream version

* Wed Feb 15 2006 Tomas Mraz <tmraz@redhat.com> - 1.8.2-2
- Rebuilt with updated gcc

* Thu Feb  2 2006 Tomas Mraz <tmraz@redhat.com> - 1.8.2-1
- Updated version, dropped obsolete patch
- Added missing buildrequires for modular X
- Fixed compilation on gcc-4.1

* Sat Oct 22 2005 Tomas Mraz <tmraz@redhat.com> - 1.8.1-4
- Added a desktop file
- Added find_lang
- Fixed wrong install extension for message translations

* Thu Oct 20 2005 Tomas Mraz <tmraz@redhat.com> - 1.8.1-3
- Removed Prefix:, added BuildRequires gnome-panel-devel
- Group: Applications/Productivity

* Thu Sep 22 2005 Tomas Mraz <tmraz@redhat.com> - 1.8.1-2
- Initial package, reused spec from package by Steve Ratcliffe
