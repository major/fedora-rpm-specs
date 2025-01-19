Name:           gtkpod
Version:        2.1.5
Release:        31%{?dist}
Summary:        Graphical song management program for Apple's iPod

License:        GPL-2.0-or-later
URL:            http://www.gtkpod.org/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		gtkpod-m4a-copy.patch
Patch1:         includes.patch
Patch2:         gtkpod-snprintf.patch

BuildRequires:  gcc-c++
BuildRequires:  gtk3-devel
BuildRequires:  curl-devel
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  anjuta-devel
BuildRequires:  desktop-file-utils
BuildRequires:  flac-devel
BuildRequires:  flex
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libgpod-devel >= 0.7.0
BuildRequires:  libid3tag-devel
BuildRequires:  libvorbis-devel
BuildRequires:  perl-generators
BuildRequires:  perl(XML::Parser)
BuildRequires:  pkgconfig
BuildRequires:  libmusicbrainz5-devel
BuildRequires:  automake autoconf libtool
BuildRequires:  python3-devel
BuildRequires: make

# some of the scripts in %%{_datadir}/%%{name}/scripts use which
Requires:       which
Requires:       hicolor-icon-theme

%description
gtkpod is a platform independent Graphical User Interface for Apple's
iPod using GTK3. It supports all current iPod models, including
the Mini, Photo, Shuffle, Nano, Video, Classic, Touch, and iPhone.

%package devel
Summary: Development files for the gtkpod
Requires: %{name} = %{version}-%{release}

%description devel
The gtkpod-devel package contains libraries and header files for
developing extensions for gtkpod.

%prep
%{__python3} %{_rpmconfigdir}/redhat/pathfix.py -pni "%{__python2} %{py2_shbang_opts}" .
%setup -q
%patch -P 0 -p1
%patch -P 1 -p0
%patch -P 2 -p0

%build
autoreconf -if
export CPPFLAGS="$CPPFLAGS -fcommon"
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} INSTALL="install -p"

desktop-file-install \
    --delete-original \
    --dir %{buildroot}%{_datadir}/applications \
    --add-category="Audio" \
    --add-category="Video" \
    %{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %{name}

# delete libtool files
find %{buildroot} -name '*.la' -exec rm -f {} \;

%py3_shebang_fix %{buildroot}/usr/share/gtkpod/scripts/*

%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog* README TODO TROUBLESHOOTING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/applications/*.desktop
%{_mandir}/man1/%{name}*
%dir %{_libdir}/gtkpod
%{_libdir}/gtkpod/*.plugin
%{_libdir}/gtkpod/*.so
%{_libdir}/*.so.*
%{_datadir}/glib-2.0/schemas/org.gtkpod.gschema.xml

%files devel
%{_includedir}/gtkpod
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Oct 09 2024 Gwyn Ciesla <gwync@protonmail.com> - 2.1.5-30
- Bump EVR

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Feb 05 2024 Gwyn Ciesla <gwync@protonmail.com> - 2.1.5-28
- Fix FTBFS

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 03 2023 Gwyn Ciesla <gwync@protonmail.com> - 2.1.5-24
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Sep 14 2022 Michel Alexandre Salim <salimma@fedoraproject.org> - 2.1.5-22
- Rebuilt for flac 1.4.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu May 05 2022 Sérgio Basto <sergio@serjux.com> - 2.1.5-20
- Based on NEWS file, libmp4v2 was replaced in version 2.1.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.1.5-15
- Fix FTBFS.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 06 2019 Gwyn Ciesla <gwync@protonmail.com> - 2.1.5-13
- Python 3.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 10 2018 Gwyn Ciesla <limburgher@gmail.com> - 2.1.5-10
- Fix shebang handling.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.5-7
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 25 2016 Jon Ciesla <limburgher@gmail.com> - 2.1.5-2
- Add m4a support, BZ 1298720.

* Mon Jun 29 2015 Jon Ciesla <limburgher@gmail.com> - 2.1.5-1
- Latest upstream, BZ 1236415.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.1.4-4
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Nov 06 2013 Jon Ciesla <limburgher@gmail.com> - 2.1.4-1
- Latest upstream.

* Tue Sep 03 2013 Jon Ciesla <limburgher@gmail.com> - 2.1.3-5
- Desktop fixes.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Petr Pisar <ppisar@redhat.com> - 2.1.3-3
- Perl 5.18 rebuild

* Fri Jul 12 2013 Jon Ciesla <limburgher@gmail.com> - 2.1.3-2
- Patch for anjuta incompatibility, BZ 975605.

* Mon Feb 11 2013 Jon Ciesla <limburgher@gmail.com> - 2.1.3-1
- Latest upstream.
- Anjuta patch upstreamed.
- Drop desktop vendor tag.

* Wed Sep 26 2012 Kalev Lember <kalevlember@gmail.com> - 2.1.2-2
- Rebuilt for libgdl soname bump

* Tue Jul 24 2012 Jon Ciesla <limburgher@gmail.com> - 2.1.2-1
- Latest upstream.
- Patch for anjuta 3.5.4.

* Mon Jul 23 2012 Kalev Lember <kalevlember@gmail.com> - 2.1.1-5
- Rebuilt for libgdl 3.5.4 soname bump

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 23 2012 Kalev Lember <kalevlember@gmail.com> - 2.1.1-3
- Rebuilt for libgdl 3.4.2 soname bump

* Wed Apr 11 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 2.1.1-2
- Rebuild for new libimobiledevice and usbmuxd

* Wed Mar 28 2012 Jon Ciesla <limburgher@gmail.com> - 2.1.1-1
- Latest upstream.
- Dropped gtk patch, fixed.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 2.1.0-2
- Rebuild for new libpng

* Tue Aug 30 2011 Christian Krause <chkr@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0 (GTK3 support)
- Minor spec file cleanup
- Add patch to fix compilation issue with newer GTK3 versions and anjuta
  ( https://bugzilla.redhat.com/show_bug.cgi?id=734605 )

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 1.0.0-2
- recompiling .py files against Python 2.7 (rhbz#623316)

* Wed Aug 11 2010 Todd Zullinger <tmz@pobox.com> - 1.0.0-1
- Update to 1.0.0

* Tue Jun 15 2010 Todd Zullinger <tmz@pobox.com> - 0.99.16-1
- Update to 0.99.16
- Link with libdl

* Sun Feb 14 2010 Todd Zullinger <tmz@pobox.com> - 0.99.14-4
- Link with libm and libvorbis (#564853)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Todd Zullinger <tmz@pobox.com> - 0.99.14-1
- Update to 0.99.14
- Add GFDL to License tag, for documentation
- Update xdg-open patch so it applies without fuzz
- Drop libgnomecanvas-devel BR, it is not used anymore
- Apply upstream patch to fix lame-tag endianess problem (this prevented gapless
  playback from working correctly)

* Sat Jan 17 2009 Todd Zullinger <tmz@pobox.com> - 0.99.12-5
- Apply upstream fix for disappearing tooltips (#428940)

* Mon Dec 01 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.99.12-4
- Rebuild for Python 2.6

* Tue Jun 10 2008 Todd Zullinger <tmz@pobox.com> - 0.99.12-3
- use xdg-open as default player (#449199)
  (patch from Debarshi Ray)
- update %%description to include more complete model list

* Tue Feb 12 2008 Todd Zullinger <tmz@pobox.com> - 0.99.12-2
- rebuild for gcc 4.3

* Tue Dec 11 2007 Todd Zullinger <tmz@pobox.com> - 0.99.12-1
- update to 0.99.12

* Wed Nov 21 2007 Todd Zullinger <tmz@pobox.com> - 0.99.10-2
- rebuild for libgpod-0.6.0
- apply upstream patch to fix smart playlist play time bug
- Requires: which (used in some of the provided scripts)

* Sat Aug 04 2007 Todd Zullinger <tmz@pobox.com> - 0.99.10-1
- update to 0.99.10
- use upstream .desktop file
- add new BRs, update libgpod BR to >= 0.5.2
- add %%post and %%postun to update the icon cache
- update license tag

* Fri Feb 16 2007 Todd Zullinger <tmz@pobox.com> - 0.99.8-3
- preserve timestamps when copying .desktop file to builddir and
  running make install
- use a symlink for the menu icon

* Mon Feb 12 2007 Todd Zullinger <tmz@pobox.com> - 0.99.8-2
- remove redundant gtk2-devel BR
- move .desktop creation to a separate file
- remove livna stuff from .desktop file
- don't use macros for install and mkdir
- remove NEWS file from %%doc as it mostly mirrors the ChangeLog

* Mon Feb 12 2007 Todd Zullinger <tmz@pobox.com> - 0.99.8-1
- initial fedora package, parts stolen from Matthias' FreshRPMS spec
