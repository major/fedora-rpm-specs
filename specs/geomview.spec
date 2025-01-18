
# trim changelog included in binary rpms
%global _changelog_trimtime %(date +%s -d "1 year ago")

Name:    geomview
Summary: Interactive 3D viewing program
Version: 1.9.5
Release: 29%{?dist}

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
Url:     http://www.geomview.org/
Source0: http://downloads.sourceforge.net/geomview/geomview-%{version}.tar.xz

# app.desktop
Source1: geomview.desktop
# mime
Source10: application_x-geomview.xml
#icons
Source20: hi16-app-geomview.png
Source21: hi22-app-geomview.png
Source22: hi32-app-geomview.png
Source23: hi48-app-geomview.png
Source24: hi64-app-geomview.png
Source25: hi128-app-geomview.png
Source26: hisc-app-geomview.svgz

BuildRequires: desktop-file-utils
BuildRequires: byacc flex
BuildRequires: gawk
BuildRequires: gcc-c++
# Until we have a generic BR: motif-devel -- Rex
%if 0%{?fedora} > 17
BuildRequires: motif-devel
%else
BuildRequires: openmotif-devel
%endif
BuildRequires: libGL-devel libGLU-devel
BuildRequires: libXmu-devel
BuildRequires: tcl-devel tk-devel

#BuildRequires: /usr/bin/makeinfo 
BuildRequires: texinfo

#BuildRequires: /usr/bin/texi2html
BuildRequires: texi2html
BuildRequires: make

Requires: xdg-utils

%if (0%{?rhel} && 0%{?rhel} <= 7) || (0%{?fedora} && 0%{?fedora} <= 27)
Requires(post): /sbin/install-info
Requires(preun): /sbin/install-info
%endif

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description
Geomview is an interactive 3D viewing program for Unix. It lets you view and
manipulate 3D objects: you use the mouse to rotate, translate, zoom in and out,
etc. It can be used as a standalone viewer for static objects or as a display
engine for other programs which produce dynamically changing geometry. It can
display objects described in a variety of file formats. It comes with a wide
selection of example objects, and you can create your own objects too.

%package libs
Summary: %{name} runtime libraries
Requires: %{name} = %{version}-%{release}
%description libs
%{summary}.

%package devel
Summary: Development files for %{name} 
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
%{summary}.


%prep
%setup -q 

# rpath hack
sed -i -e 's|"/lib /usr/lib|"/%{_lib} %{_libdir}|' configure


%build
%configure \
  --enable-shared \
  --disable-static \
  --with-htmlbrowser=xdg-open \
  --with-pdfviewer=xdg-open \

%make_build


%install
%make_install

# .desktop entry
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE1}

# mime
install -p -m644 -D %{SOURCE10} %{buildroot}%{_datadir}/mime/packages/x-geomview.xml

# app icons
install -p -m644 -D %{SOURCE20} %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/geomview.png
install -p -m644 -D %{SOURCE21} %{buildroot}%{_datadir}/icons/hicolor/22x22/apps/geomview.png
install -p -m644 -D %{SOURCE22} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/geomview.png
install -p -m644 -D %{SOURCE23} %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/geomview.png
install -p -m644 -D %{SOURCE24} %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/geomview.png
install -p -m644 -D %{SOURCE25} %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/geomview.png
install -p -m644 -D %{SOURCE26} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/geomview.svgz

# Unpackaged files
rm -fv %{buildroot}%{_infodir}/dir
rm -fv %{buildroot}%{_libdir}/lib*.la


%if (0%{?rhel} && 0%{?rhel} <= 7) || (0%{?fedora} && 0%{?fedora} <= 27)
%post
/sbin/install-info --info-dir=%{_infodir} %{_infodir}/%{name}.gz ||:

%preun
if [ $1 -eq 0 ] ;then
  /sbin/install-info --delete --info-dir=%{_infodir} %{_infodir}/%{name}.gz ||:
fi
%endif

%files
%doc AUTHORS ChangeLog NEWS README
%license COPYING
%{_bindir}/*
%{_docdir}/geomview/
%{_datadir}/applications/*.desktop
%{_datadir}/geomview/
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/mime/packages/*.xml
%{_infodir}/figs/
%{_infodir}/geomview*
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_mandir}/man5/*
%{_libexecdir}/geomview/

%ldconfig_scriptlets libs

%files libs
%{_libdir}/libgeomview-%{version}.so

%files devel
%{_libdir}/libgeomview.so
%{_includedir}/geomview/


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 1.9.5-28
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.9.5-13
- new install-info scriptlets
- use %%license %%make_build %%make_install %%ldconfig_scriptlets

* Tue Feb 20 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.9.5-12
- BR: gcc-c++

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.9.5-11
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.9.5-9
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.9.5-3
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 03 2014 Rex Dieter <rdieter@fedoraproject.org> 1.9.5-1
- geomview-1.9.5

* Thu Jul 03 2014 Rex Dieter <rdieter@fedoraproject.org> - 1.9.4-20
- optimize mimeinfo scriptlets
- cleanup .spec
- build against motif

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Mar 22 2011 Rex Dieter <rdieter@fedoraproject.org> 1.9.4-14
- broken or deprecated mime type (#587570) 

* Mon Feb 14 2011 Rex Dieter <rdieter@fedoraproject.org> 1.9.4-13
- fix -libs subpkg 
- drop old baggage

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 27 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.9.4-11
- drop kde3/mimelnk bits where kde4 is used (F-9+, RHEL6+)
- make -libs unconditional
- optimize scriptlets
- nuke rpaths

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Apr 03 2008 Rex Dieter <rdieter@fedoraproject.org> 1.9.4-8
- -libs: scriptlets

* Tue Apr 03 2008 Rex Dieter <rdieter@fedoraproject.org> 1.9.4-7
- -libs subpkg, fixes multiarch conflicts (#341241) (f9+)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.9.4-6
- Autorebuild for GCC 4.3

* Mon Nov 12 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.9.4-5
- fix x-oogl.desktop (to not include Patterns=*). doh.

* Tue Oct 09 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.9.4-4
- more icons (#190218)

* Fri Sep 14 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.9.4-3
- use model/vrml,object/x-oogl(register) mimetypes

* Mon Aug 27 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.9.4-2
- BR: gawk

* Mon Aug 27 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.9.4-1
- geomview-1.9.4

* Sat Aug 11 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.9.3-3
- License: LGPLv2+

* Mon Jul 16 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.9.3-2
- geomview.desktop: Categories=-Education (#241441)

* Thu Jun 21 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.9.3-1
- geomview-1.9.3

* Sat Jun 16 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.9.2-1
- geomview-1.9.2

* Wed Jun 06 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.9.1-1
- geomview-1.9.1
- omit orrery/maniview, can now be packaged separately.

* Thu Oct 26 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.8.2-0.25.rc9
- re-instate dfi --vendor=fedora (thanks Ville!) 

* Thu Oct 26 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.8.2-0.24.rc9
- fixup desktop-file-install usage
- fixup geomview.desktop Categories

* Thu Oct 26 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.8.2-0.22.rc9
- rename (man/man1/)sweep.1 -> geomview-sweep.1 to avoid
  Conflicts: lam (bug #212435)

* Sun Oct 01 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.8.2-0.21.rc9
- 1.8.2rc9

* Thu Sep 07 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.8.2-0.20.rc8
- fc6: BR: openmotif-devel -> lesstif-devel

* Tue Aug 29 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.8.2-0.19.rc8
- fc6 respin

* Wed Aug 09 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.8.2-0.18.rc8
- rename (man/man1/)animate.1 -> geomview-animate.1 to avoid 
  Conflicts: ImageMagick (bug #202039)

* Tue Aug 08 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.8.2-0.17.rc8
- 1.8.2-rc8
- -devel pkg

* Mon Jul 31 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.8.2-0.14.rc7
- BR: tcl-devel tk-devel

* Mon Jul 31 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.8.2-0.13.rc7
- 1.8.2-rc7

* Thu Jul 26 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.8.2-0.12.rc6
- 1.8.2-rc6

* Tue Jul 24 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.8.2-0.11.rc4
- 1.8.2-rc4

* Fri Jul 21 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.8.2-0.10.rc3
- patch to fix ppc build

* Thu Jul 20 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.8.2-0.8.rc3
- 1.8.2-rc3
- --without-maniview (for now, doesn't build)
- drop -maniview, -orrery subpkgs

* Sat Jun 24 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.8.2-0.7.cvs20060623
- omit zero-length files

* Fri Jun 23 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.8.2-0.6.cvs20060623
- geomview-cvs20060623, (hopefully) will yield a usable, x86_64 build (#182625)
- --disable-seekpipe

* Tue Jun 20 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.8.2-0.5.cvs20040221
- BR: automake libtool

* Fri May 12 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.8.2-0.3.cvs20040221
- updated (transparent) icon (rh bug #190218)
- drop deprecated BR: libGL.so.1,libGLU.so.1 bits
- ExcludeArch: x86_64 (#182625)
- .desktop: MimeType: application/x-geomview

* Wed Mar 1 2006 Rex Dieter <rexdieter[AT]users.sf.net>
- fc5: gcc/glibc respin

* Tue Jan 03 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.8.2-0.2.cvs20040221
- rework Obsoletes/Provides: geomview-plugins

* Mon Jan 02 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.8.2-0.1.cvs20040221
- cvs20040421
- --with-xforms unconditional, Obsoletes/Provides: geomview-plugins

* Mon Dec 19 2005 Rex Dieter <rexdieter[AT]usres.sf.net> 1.8.1-12
- follow/use icon spec

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Mon Sep 20 2004 Rex Dieter <rexdieter at sf.net> 0:1.8.1-10
- update Source URL
- fix un-owned /usr/share/geomview/modules
- Requires(post,preun): /sbin-install-info
- -orrery: Requires: tk
- License: LGPL, %%doc COPYING
- comment out the Obsoleting of subpkgs with using --without.  I think
  the logic there is wrong.
- relax subpkgs to Requires: %%{name} = %%epoch:%%version

* Tue Sep 14 2004 Rex Dieter <rexdieter at sf.net> 0:1.8.1-0.fdr.9
- fix build for fc3
- remove unused gcc_ver cruft
- remove unused (by default) lesstif bits

* Mon Jul 19 2004 Rex Dieter <rexdieter at sf.net> 0:1.8.1-0.fdr.8
- .desktop Categories += Education;Math;

* Mon Jul 19 2004 Rex Dieter <rexdieter at sf.net> 0:1.8.1-0.fdr.7
- BR: libGL.so.1 libGLU.so.1

* Mon Jul 19 2004 Rex Dieter <rexdieter at sf.net> 0:1.8.1-0.fdr.6
- fix file list (possible dups)

* Mon Jul 19 2004 Rex Dieter <rexdieter at sf.net> 0:1.8.1-0.fdr.5
- BR: libtool flex
- BR: XFree86-devel (for lib{GL/GLU})

* Thu Jun 03 2004 Rex Dieter <rexdieter at sf.net> 0:1.8.1-0.fdr.4
- .desktop: Categories += Graphics

* Tue Mar 16 2004 Rex Dieter <rexdieter at sf.net> 0:1.8.1-0.fdr.3
- use patch from geomview sf site to allow gcc3.
- use desktop-file-install

* Wed Sep 24 2003 Rex Dieter <rexdieter at sf.net> 0:1.8.1-0.fdr.2
- cleanup for formal submission to fedora.

* Fri Aug 08 2003 Rex Dieter <rexdieter at sf.net> 0:1.8.1-0.fdr.1
- Build against openmotif.

* Mon May 12 2003 Rex Dieter <rexdieter at users.sf.net> 0:1.8.1-0.fdr.0
- fedora'ize
- rh73: link xforms static (for now, so rh80+ users could use if they
  want/need plugins/maniview subpkgs).
- rh80+: use g++296, no xforms.
- Obsoletes: subpkgs not built.

* Fri Jun 21 2002 Rex Dieter <rexdieter at users.sf.net> 1.8.1-8
- Obsoletes/Provides: pluginname=version-release for extra plugins
  (so to gracefully handle upgrade from Mark's orrery rpm)

* Fri Jun 21 2002 Rex Dieter <rexdieter at users.sf.net> 1.8.1-7
- use macros for all subpkgs
- include orrery-0.9.3.
- remove %%_smp_mflags (makefile is not smp safe)

* Thu Jun 20 2002 Rex Dieter <rexdieter at users.sf.net> 1.8.1-6
- include maniview-2.0.0.
- include geomview info/man pages.

* Thu Feb 27 2002 Rex Dieter <rexdieter at users.sf.net> 1.8.1-5
- rebuild to link xforms dynamic

* Wed Feb 20 2002 Rex Dieter <rexdieter at users.sf.net> 1.8.1-4
- conditionally use xforms (no by default)
- make subpkg require %%name-%%version-%%release
- tweak to work with new lesstif

* Tue Dec 11 2001 Rex Dieter <rexdieter at users.sf.net> 1.8.1-3
- really use the app-icon this time.
- use Prefix to at least pretend relocatability

* Wed Nov 7 2001 Rex Dieter <rexdieter at users.sf.net> 1.8.1-2
- make -plugins subpkg for plugins that use xforms.

* Fri Oct 5 2001 Rex Dieter <rexdieter at users.sf.net > 1.8.1-1
- cleanup specfile
- make icon/desktop files
- include option to link xforms-static (untested)

* Fri Sep 28 2001 Rex Dieter <rexdieter at users.sf.net> 1.8.1-0
- first try.
- TODO: make subpkgs manual(html), modules, modules-xforms

