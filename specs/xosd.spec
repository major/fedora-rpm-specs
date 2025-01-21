Name:           xosd
Version:        2.2.14
Release:        45%{?dist}
Summary:        On-screen display library for X
# COPYING:      GPL-2.0 text
# man/osd_cat.1:        GPL-1.0-or-later
# man/xosd-config.1:    MIT-open-group
# src/libxosd/xosd.c:   GPL-2.0-or-later
## Disabled at configure time, unused
# src/bmp_plugin/bmp_osd.c:     GPL-2.0-or-later
# src/bmp_plugin/dlg_colour.c:  GPL-2.0-or-later
# src/bmp_plugin/dlg_config.c:  GPL-2.0-or-later
# src/bmp_plugin/dlg_config_old.c:  GPL-2.0-or-later
# src/bmp_plugin/dlg_font.c:    GPL-2.0-or-later
# src/xmms_plugin/dlg_colour.c: GPL-2.0-or-later
# src/xmms_plugin/dlg_config.c: GPL-2.0-or-later
# src/xmms_plugin/dlg_config_old.c: GPL-2.0-or-later
# src/xmms_plugin/dlg_font.c:   GPL-2.0-or-later
# src/xmms_plugin/xmms_osd.c:   GPL-2.0-or-later
## Not in any binary package
# aclocal.m4:   FSFULLR AND GPL-2.0-or-later WITH Autoconf-exception-generic
#               AND GPL-2.0-or-later
# config.guess: GPL-2.0-or-later WITH Autoconf-exception-generic
# config.sub:   GPL-2.0-or-later WITH Autoconf-exception-generic
# configure:    FSFUL AND GPL-2.0-or-later WITH Autoconf-exception-generic
# depcomp:      GPL-2.0-or-later WITH Autoconf-exception-generic
# INSTALL:      FSFUL
# install-sh:   HPND-sell-variant
# ltconfig:     GPL-2.0-or-later WITH Autoconf-exception-generic
# ltmain.sh:    GPL-2.0-or-later WITH Autoconf-exception-generic
# macros/Makefile.in:   FSFULLR
# Makefile.in:  FSFULLR
# man/Makefile.in:      FSFULLR
# missing:      GPL-2.0-or-later WITH Autoconf-exception-generic
# pixmaps/Makefile.in:  FSFULLR
# script/Makefile.in:   FSFULLR
# src/bmp_plugin/Makefile.in:   FSFULLR
# src/libxosd/Makefile.in:  FSFULLR
# src/Makefile.in:          FSFULLR
# src/xmms_plugin/Makefile.in:  FSFULLR
License:        GPL-2.0-or-later AND GPL-1.0-or-later
URL:            https://sourceforge.net/projects/libxosd/
Source:         https://downloads.sourceforge.net/libxosd/%{name}-%{version}.tar.gz
Patch0:         %{name}-aclocal18.patch
Patch1:         %{name}-2.2.14-Do-not-install-some-manual-pages-twice.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  gcc
# glibc-common for iconv
BuildRequires:  glibc-common
BuildRequires:  libtool
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXinerama-devel
BuildRequires:  make
BuildRequires:  perl-interpreter
# As of 2.2.14, the default font *must* be found, even if not used (#183971)
Requires:       xorg-x11-fonts-misc
# XMMS is dead, gdk-pixbuf-0 is dead. Dropping xmms plug-in.
Obsoletes:      xmms-%{name} < 2.2.14-15
Obsoletes:      %{name}-xmms <= 2.2.12

%description
XOSD displays text on your screen, sounds simple right? The difference
is it is unmanaged and shaped, so it appears transparent. This gives
the effect of an On Screen Display, like your TV/VCR etc.

%package        devel
Summary:        Development files for the XOSD on-screen display library
License:        GPL-2.0-or-later AND MIT-open-group
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libX11-devel
Requires:       libXext-devel
Requires:       libXinerama-devel

%description    devel
Header files and documentation for developing applications that use the XOSD
on-screen display.

%prep
%setup -q
%patch -P0 -p0
%patch -P1 -p1
# XMMS is dead, gdk-pixbuf-0 is dead. Dropping xmms plug-in.
sed -i -e '/AM_PATH_GTK/,+1 d' -e '/AM_PATH_XMMS/,+1 d' \
    -e '/AM_PATH_GDK_PIXBUF/,+1 d' configure.ac
# Update config.sub to support aarch64, bug #926836
autoreconf -i -f
for f in ChangeLog man/xosd_{create,destroy,display,is_onscreen,set_bar_length}.3 ; do
    iconv -f iso-8859-1 -t utf-8 "$f" > "${f}.utf8"
    touch -r "$f" "${f}.utf8"
    mv "${f}.utf8" "$f"
done

%build
%configure --disable-dependency-tracking --disable-static \
    --disable-gtktest --disable-gdk_pixbuftest \
    --disable-new-plugin --disable-old-plugin \
    --disable-beep_media_player_plugin\
    --enable-xinerama
%{make_build}
perl -pi -e "s|$RPM_OPT_FLAGS\\s*|| ; s|\\s*-Wall||" script/xosd-config

%install
%{make_install}
rm -f $RPM_BUILD_ROOT{%{_libdir},%{xmms_plugdir}}/*.la
# Pixmaps are needed only by unsupported XMMS plug-in.
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}

%files
%license COPYING
%doc AUTHORS ChangeLog README TODO
%{_bindir}/osd_cat
%{_libdir}/libxosd.so.2
%{_libdir}/libxosd.so.2.*
%{_mandir}/man1/osd_cat.1*

%files devel
%{_bindir}/xosd-config
%{_includedir}/xosd.h
%{_libdir}/libxosd.so
%{_datadir}/aclocal/libxosd.m4
%{_mandir}/man1/xosd-config.1*
%{_mandir}/man3/xosd*.3*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.14-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.14-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.14-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.14-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.14-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep 08 2022 Petr Pisar <ppisar@redhat.com> - 2.2.14-40
- License corrected to "GPL-2.0-or-later AND GPL-1.0-or-later AND MIT-open-group

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.14-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.14-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.14-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Peter Hutterer <peter.hutterer@redhat.com> 2.2.14-36
- Require xorg-x11-fonts-misc instead of -base. -base hasn't existed for
  over a decade.

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.14-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.14-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 09 2020 Petr Pisar <ppisar@redhat.com> - 2.2.14-33
- Modernize a spec file

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.14-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.14-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.14-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.14-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 23 2018 Petr Pisar <ppisar@redhat.com> - 2.2.14-28
- Modernize a spec file

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.14-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.14-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.14-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.14-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.14-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.14-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.14-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.14-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.14-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 27 2013 Petr Pisar <ppisar@redhat.com> - 2.2.14-18
- Update config.sub to support aarch64 (bug #926836)

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.14-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.14-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Petr Pisar <ppisar@redhat.com> - 2.2.14-15
- Disable XMMS plug-in because gdk-pixpuf-0 has been removed
- Remove build-optional static library
- Clean spec file up 
- Do not package XMMS plug-in pixmaps
- Remove patch changing default offset to keep closer with upstream
- Update upstream URLs

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.14-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.14-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.14-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 10 2008 Kevin Fenzi <kevin@tummy.com> - 2.2.14-11
- Rebuild for gcc43

* Sun Aug 26 2007 Kevin Fenzi <kevin@tummy.com> - 2.2.14-10
- Update License tag

* Tue Feb 27 2007 Kevin Fenzi <kevin@tummy.com> - 2.2.14-9
- Remove bmp subpackage, as bmp is no longer shipped. 

* Sun Aug 27 2006 Kevin Fenzi <kevin@tummy.com> - 2.2.14-8
- Rebuild for fc6

* Fri Jun 16 2006 Kevin Fenzi <kevin@tummy.com> - 2.2.14-7
- Rebuild against new libgdk_pixbuf

* Wed Apr 12 2006 Ville Skyttä <ville.skytta at iki.fi> - 2.2.14-6
- Revert to upstream default font, require xorg-x11-fonts-base (#183971).

* Sun Mar 12 2006 Ville Skyttä <ville.skytta at iki.fi> - 2.2.14-5
- Convert docs to UTF-8.

* Thu Nov 17 2005 Ville Skyttä <ville.skytta at iki.fi> - 2.2.14-4
- Adapt to modular X packaging.
- Don't ship static libraries by default.
- Specfile cleanups.

* Thu May 19 2005 Ville Skyttä <ville.skytta at iki.fi> - 2.2.14-3
- Rebuild.

* Thu Mar 17 2005 Ville Skyttä <ville.skytta at iki.fi> - 2.2.14-2
- Add Beep Media Player plugin subpackage.
- Improve default font and plugin OSD placement.

* Mon Nov 29 2004 Ville Skyttä <ville.skytta at iki.fi> - 2.2.14-1
- Update to 2.2.14 (from Debian).
- Drop pre-FC1 gdk-pixbuf compatibility kludges.

* Wed Nov 10 2004 Matthias Saou <http://freshrpms.net/> 2.2.12-2
- Bump release to provide Extras upgrade path.
- Remove zero epochs.

* Tue Sep 14 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:2.2.12-0.fdr.1
- Update to 2.2.12.
- Disable dependency tracking to speed up the build.
- Include TODO in docs.

* Sun Sep 12 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:2.2.11-0.fdr.1
- Update to 2.2.11 (from Debian).
- While at it, borrow patches from Debian's 2.2.11-2.

* Sat Aug 28 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:2.2.10-0.fdr.1
- Update to 2.2.10.
- Patch to eliminate aclocal >= 1.8 warnings from libxosd.m4.

* Mon Jul  5 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:2.2.8-0.fdr.1
- Update to 2.2.8.

* Tue May 25 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:2.2.7-0.fdr.1
- Update to 2.2.7.

* Wed May 19 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:2.2.5-0.fdr.2
- Clean up "xosd-config --cflags".

* Sat Sep 27 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:2.2.5-0.fdr.1
- Update to 2.2.5.

* Mon Jun 30 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:2.2.2-0.fdr.1
- Update to 2.2.2.

* Sat Apr 19 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:2.2.1-0.fdr.1
- Update to 2.2.1.
- Disable gdk-pixbuf test, XOSD says it requires >= 0.22.0, but 0.18.0
  seems to work just fine.

* Sun Apr 13 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:2.2.0-0.fdr.1
- Update to 2.2.0.
- Rename XMMS plugin package to xmms-xosd, and obsolete xosd-xmms.

* Mon Apr  7 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:2.1.3-0.fdr.3
- Require XFree86-devel in -devel (xosd-config --libs).

* Sat Apr  5 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:2.1.3-0.fdr.2
- Add epoch to devel and xmms Requires (#30 comment 4).
- Don't include *.la in xmms package.
- Save .spec in UTF-8.

* Sat Mar 22 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:2.1.3-0.fdr.1
- Update to 2.1.3 and current Fedora guidelines.
- Don't include %%{_libdir}/*.la.

* Wed Feb 26 2003 Ville Skyttä <ville.skytta at iki.fi> - 2.1.2-1.fedora.1
- Update to 2.1.2.
- Use %%post(un) -p /sbin/ldconfig.

* Sat Feb  8 2003 Ville Skyttä <ville.skytta at iki.fi> - 2.1.0-1.fedora.1
- First Fedora release, based on Matthias Saou's work.

* Wed Feb  5 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 2.1.0.
- Spec file updates to reflect upstream changes.

* Wed Jan  8 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 2.0.1.

* Mon Oct 21 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.1.1.

* Sun Sep 29 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.0.4.
- Rebuilt for Red Hat Linux 8.0.

* Fri Aug 30 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.0.3.

* Wed Aug 28 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.0.2.
- Fixed %%defattr for xmms plugin sub-package.

* Mon Jul 22 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.0.0.
- Spec file cleanup (near rewrite), added devel and xmms sub-packages.

* Wed Aug  1 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.7.0 and spec file cleanup.
- Changed the plugin path.
- Added ldconfig execution since I also changed the lib filename.

* Sat Feb  3 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Initial RPM release.

