%if 0%{?fedora}
%bcond_without modular_x
%bcond_without modular_xss
%else
%bcond_with modular_x
%bcond_with modular_xss
%endif

%global xssconfigdir %{_datadir}/xscreensaver/config
%global xssexthacksconfdir %{_datadir}/xscreensaver/hacks.conf.d
%global xssbindir %{_libexecdir}/xscreensaver

%bcond_with matrixview
%global patchext %{nil}%{!?with_matrixview:.p}

Summary: Really Slick Screensavers
Name: rss-glx
Version: 0.9.1%{patchext}
Release: 63%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL: http://rss-glx.sourceforge.net/
# We ship a tarball with one questionable hack patched out.
# The original URL is the following without %%patchext:
# Source0: http://downloads.sourceforge.net/sourceforge/rss-glx/rss-glx_%{version}.tar.bz2
Source0: rss-glx_%{version}.tar.bz2
Source1: README.fedora
# The following two strip matrixview from the package and build a new tarball
Source2: rss-glx-rm-matrixview.sh
Source3: rss-glx-0.9.1-0.9.1.p.diff
Source4: rss-glx-matrixview.conf
Source5: rss-glx.conf
# https://sourceforge.net/tracker/?func=detail&aid=2839037&group_id=67131&atid=517003
Patch0: rss-glx-0.9.0.p-optflags.patch
Patch10: rss-glx-0.9.1.p-6-autoreconf.patch.bz2
Patch11: rss-glx-0.9.1.p-linker.patch
Patch12: rss-glx-0.9.1.p-pixelcity.patch
Patch13: rss-glx-gcc11.patch
# Modified version from openSUSE: https://build.opensuse.org/package/view_file/X11:Utilities/rss-glx/rss-glx-ImageMagick7.patch?expand=1
Patch14: rss-glx-ImageMagick7.patch
# Autotools regeneration doesn't work
Patch15: rss-glx-ImageMagick7-configure.patch

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires: libGL-devel
BuildRequires: libGLU-devel
BuildRequires: glew-devel
BuildRequires: quesoglc-devel
BuildRequires: ImageMagick-devel >= 6.4
%if %{with modular_x}
BuildRequires: libICE-devel
BuildRequires: libSM-devel
BuildRequires: libX11-devel
BuildRequires: libXt-devel
%else
BuildRequires: xorg-x11-devel
%endif
BuildRequires: bzip2-devel
BuildRequires: freealut-devel
BuildRequires: gawk
BuildRequires: sed

%if 0%{?fedora} >= 33
Obsoletes:     %{name}-gnome-screensaver < 0.9.1.p-43
%endif

%description
A port of the Really Slick Screensavers to GLX. Provides several visually
impressive and graphically intensive screensavers.

Note that this package contains only the display hacks themselves; you will
need to install the appropriate subpackage for your desktop environment in
order to use them as screensavers.

%package xscreensaver
Summary: Really Slick Screensavers
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
%if %{with modular_xss}
Requires(post): xscreensaver-base >= 1:5.03-3
Requires(postun): xscreensaver-base >= 1:5.03-3
%else
Requires: xscreensaver-base < 1:5.03-3
%endif
Requires: xscreensaver-gl-base

%description xscreensaver
A port of the Really Slick Screensavers to GLX. Provides several visually
impressive and graphically intensive screensavers.

This package contains files needed to use the hacks with xscreensaver.

%prep
cat << EOF

Build settings:
%if %{with modular_x}
- with modular X
%else
- with monolithic X
%endif
%if %{with matrixview}
- with matrixview hack
%else
- without matrixview hack
%endif
%if %{with modular_xss}
- with modular xscreensaver support
%else
- without modular xscreensaver support
%endif
EOF

%autosetup -p1 -n rss-glx_%{version}

%build
%configure \
    --with-configdir=%{xssconfigdir} \
    --program-prefix=rss-glx-
%make_build

%install
install -m 0644 "%SOURCE1" "%SOURCE2" "%SOURCE3" .
make DESTDIR=%{buildroot} install
rm -f %{buildroot}%{_libdir}/lib*.{,l}a
rm %{buildroot}%{_bindir}/rss-glx-rss-glx_install.pl

mkdir -p %{buildroot}%{xssbindir}
mkdir -p %{buildroot}%{xssexthacksconfdir}
%if %{with matrixview}
install -m 0644 "%SOURCE4" %{buildroot}%{xssexthacksconfdir}/rss-glx.conf
%else
install -m 0644 "%SOURCE5" %{buildroot}%{xssexthacksconfdir}/rss-glx.conf
%endif

cd %buildroot/%{_bindir}/
for file in rss-glx*; do
    ln -snf "%{_bindir}/${file}" "%{buildroot}%{xssbindir}/${file}"
done

cd %buildroot/%{xssconfigdir}/
for file in *.xml; do
    mv -f ${file} rss-glx-${file}
done

%if %{with modular_xss}
%post xscreensaver
if [ -x %{_sbindir}/update-xscreensaver-hacks ]; then
    %{_sbindir}/update-xscreensaver-hacks
fi

%postun xscreensaver
if [ -x %{_sbindir}/update-xscreensaver-hacks ]; then
    %{_sbindir}/update-xscreensaver-hacks || :
fi
%endif

%files
%doc ChangeLog COPYING INSTALL
%doc README.fedora rss-glx-rm-matrixview.sh rss-glx-0.9.1-0.9.1.p.diff
%{_bindir}/*
%{_mandir}/*/*

%files xscreensaver
# xscreensaver-base provides %{xssexthacksconfdir}
%config(noreplace) %{xssexthacksconfdir}/rss-glx.conf
%{xssconfigdir}/*.xml
%dir %{xssbindir}
%{xssbindir}/*

%changelog
* Fri Jan 17 2025 josef radinger <cheese@nosuchhost.net> - 0.9.1.p-63
- rebuild for broken dependency on libMagickWand

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.1.p-62
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1.p-61
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1.p-60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1.p-59
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1.p-58
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1.p-57
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 05 2023 Neal Gompa <ngompa@fedoraproject.org> - 0.9.1.p-56
- Rebuild for ImageMagick 7

* Mon Dec 05 2022 Neal Gompa <ngompa@fedoraproject.org> - 0.9.1.p-55
- Patch pregenerated configure script since regeneration fails

* Sun Dec 04 2022 Neal Gompa <ngompa@fedoraproject.org> - 0.9.1.p-54
- Add patch for ImageMagick 7 compatibility

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1.p-53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 10 2022 Orion Poplawski <orion@nwra.com> - 0.9.1.p-52
- Rebuild for glew 2.2

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1.p-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Oct 17 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.1.p-50
- Rebuild against new ImageMagick

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1.p-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1.p-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 15 2020 Jeff Law <law@redhat.com> - 0.9.1.p-47
- Fix missing include of cstddef for gcc-11

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1.p-46
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1.p-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 07 2020 josef radinger <cheese@nosuchhost.net> - 0.9.1.p-44
- obsolete rss-glx-gnome-screensaver
- further cleanup

* Sat Jun 06 2020 josef radinger <cheese@nosuchhost.net> - 0.9.1.p-43
- we no longer have gnome-screensaver
- and we have no kde-packages for long times, too
- specfile-cleanup


* Sat May 16 2020 josef radinger <cheese@nosuchhost.net> - 0.9.1.p-42
- fix pixelcity rss-glx-0.9.1.p-pixelcity.patch

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1.p-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1.p-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1.p-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 31 2018 josef radinger <cheese@nosuchhost.net> - 0.9.1.p-38
- fix rss-glx-0.9.1.p-linker.patch (reorder and patch Makefile.in instead of Makefile.am)

* Tue Aug 28 2018 Michael Cronenworth <mike@cchtml.com> - 0.9.1.p-37
- Rebuild for new ImageMagick 6.9.10

* Thu Aug 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 0.9.1.p-36
- Rebuilt for glew 2.1.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1.p-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.1.p-34
- Escape macros in %%changelog

* Tue Sep 05 2017 Adam Williamson <awilliam@redhat.com> - 0.9.1.p-33
- Rebuild for ImageMagick 6 reversion, drop ImageMagick 7 patch

* Mon Aug 28 2017 Michael Cronenworth <mike@cchtml.com> - 0.9.1.p-32
- Rebuilt for ImageMagick

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1.p-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1.p-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1.p-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Orion Poplawski <orion@cora.nwra.com> - 0.9.1.p-28
- Rebuild for glew 2.0.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1.p-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 19 2016 Nils Philippsen <nils@redhat.com>
- use %%global instead of %%define

* Thu Jan 14 2016 Adam Jackson <ajax@redhat.com> - 0.9.1.p-26
- Rebuild for glew 1.13

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1.p-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 28 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.1.p-24
- F-22+: Obsoletes -kde subpackage

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1.p-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1.p-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 02 2014 josef radinger <cheese@nosuchhost.net> - 0.9.1.p-20
- fix date in changelog 

* Tue Apr 01 2014 josef radinger <cheese@nosuchhost.net> - 0.9.1.p-19
- rename xml-files (#744862)

* Mon Nov 18 2013 Dave Airlie <airlied@redhat.com> - 0.9.1.p-18
- rebuilt for GLEW 1.10

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1.p-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Mar 30 2013 Kevin Fenzi <kevin@scrye.com> - 0.9.1.p-16
- Rebuild for broken deps in rawhide

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1.p-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 13 2012 Adam Jackson <ajax@redhat.com> - 0.9.1.p-14
- Rebuild for glew 1.9.0

* Wed Aug 01 2012 Adam Jackson <ajax@redhat.com> - 0.9.1.p-13
- -Rebuild for new glew

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1.p-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 13 2012 Tom Callawau <spot@fedoraproject.org> - 0.9.1.p-11
- rebuild for new ImageMagick

* Tue Jan 10 2012 Nils Philippsen <nils@redhat.com> - 0.9.1.p-10
- rebuild for gcc 4.7

* Mon Jul 04 2011 Nils Philippsen <nils@redhat.com> - 0.9.1.p-9
- rebuild against new ImageMagick

* Mon Jun 20 2011 ajax@redhat.com - 0.9.1.p-8
- Rebuild for new glew soname

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1.p-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Oct 11 2010 Nils Philippsen <nils@redhat.com> 0.9.1.p-6
- fix silent skyrocket desktop filename (#617531)

* Wed Sep 29 2010 jkeating - 0.9.1.p-5
- Rebuilt for gcc bug 634757

* Wed Sep 15 2010 Nils Philippsen <nils@redhat.com> 0.9.1.p-4
- rebuild for new ImageMagick

* Sun Apr 11 2010 Caolán McNamara <caolanm@redhat.com> 0.9.1.p-3
- Resolves: rhbz#564845 Fix ImplicitDSOLinking

* Tue Jan 26 2010 Nils Philippsen <nils@redhat.com> 0.9.1.p-2
- add autoreconf patch, the optflags patch isn't worth much without it
  (#558561)

* Mon Jan 18 2010 Nils Philippsen <nils@redhat.com> 0.9.1.p-1
- version 0.9.1.p
- remove autofoo patch
- add BR: quesoglc-devel for new pixelcity hack
- bump BR: ImageMagick-devel >= 6.4

* Tue Sep 01 2009 Nils Philippsen <nils@redhat.com> 0.9.0.p-3
- don't ship prefixed rss-glx-rss-glx_install.pl

* Tue Aug 18 2009 Nils Philippsen <nils@redhat.com>
- explain autofoo patch

* Mon Aug 17 2009 Nils Philippsen <nils@redhat.com> 0.9.0.p-2
- don't rebuild autofoo files

* Mon Aug 17 2009 Nils Philippsen <nils@redhat.com> 0.9.0.p-1
- version 0.9.0.p
- build with GLEW
- don't distribute README
- replace flags by optflags patch
- remove obsolete gcc-4.3 patch
- remove symlinked source files workaround (#189928)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2.p-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2.p-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 22 2008 Nils Philippsen <nils@redhat.com> 0.8.2.p-1
- use autoreconf to avoid using non-matching ltmain.sh

* Wed Dec 17 2008 Nils Philippsen <nils@redhat.com>
- correct KDE desktop files so that they work with KDE 4.1
- remove encoding lines from desktop files as they're deprecated

* Tue Dec 16 2008 Nils Philippsen <nils@redhat.com>
- version 0.8.2.p
- remove obsolete freealut patch
- update flags, gcc43 patches

* Thu May 29 2008 Nils Philippsen <nphilipp@redhat.com> 0.8.1.p-20
- use %%bcond, %%with macros for consistency
- don't use quotes around %%fedora macro to make it work with Fedora 10
- use correct binary names for KDE (#448844)

* Wed Apr 02 2008 Rex Dieter <rdieter@fedoraproject.org> 0.8.1.p-19
- -kde: drop Requires: kdebase (kdeartwork dep is enough)
- fix %%kdessconfigdir for kde4

* Thu Jan 31 2008 Adel Gadllah <adel.gadllah@gmail.com> 0.8.1.p-18
- Fix build with gcc43

* Mon Nov 05 2007 Nils Philippsen <nphilipp@redhat.com> 0.8.1.p-17
- make screensavers show up in screensaver preferences again (#365991)

* Tue Oct 30 2007 Nils Philippsen <nphilipp@redhat.com> 0.8.1.p-16
- don't show screensaver hacks in main menu (#357451)

* Fri Oct 19 2007 Nils Philippsen <nphilipp@redhat.com> 0.8.1.p-15
- let -xscreensaver require xscreensaver-gl-base (#336331)

* Tue Oct 02 2007 Nils Philippsen <nphilipp@redhat.com> 0.8.1.p-14
- prefix xscreensaver symlinks with "rss-glx-" as well (#318611)

* Tue Oct 02 2007 Nils Philippsen <nphilipp@redhat.com> 0.8.1.p-13
- prefix binaries with "rss-glx-" (#250180)

* Mon Oct 01 2007 Nils Philippsen <nphilipp@redhat.com> 0.8.1.p-12
- don't ship README.xscreensaver (#200881)

* Sat Sep 15 2007 Nils Philippsen <nphilipp@redhat.com> 0.8.1.p-11
- enable modular xscreensaver support for Fedora 7 and later (#200881)
- include %%post/%%postun scripts only with modular xscreensaver support

* Fri Sep 14 2007 Nils Philippsen <nphilipp@redhat.com> 0.8.1.p-10
- replace requirement on %%{_bindir}/kxsconfig by kdeartwork-kxe (Fedora >= 7,
  RHEL >= 6), kdeartwork-extras (<= Fedora 6, RHEL 5) 
- license is GPLv2
- run %%{_sbindir}/update-xscreensaver-hacks in %%post, %%postun, require
  xscreensaver-base >= 5.03-3 for that
- don't reference upstream URL for source tarball as we ship a modified one

* Mon Sep 03 2007 Nils Philippsen <nphilipp@redhat.com>
- implement revamped modular xscreensaver configuration (#200881)
- require post/preun xscreensaver-base min/max EVR
- don't let %%preun fail

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 0.8.1.p-9
- Buildrequire gawk.

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 0.8.1.p-8
- Rebuild for selinux ppc32 issue.

* Thu Jun 14 2007 Nils Philippsen <nphilipp@redhat.com> 0.8.1.p-7
- build xscreensaver hack description files (#200881)
- require %%{_bindir}/kxsconfig (#219106)

* Mon Aug 28 2006 Nils Philippsen <nphilipp@redhat.com> 0.8.1.p-6
- FC6 mass rebuild

* Tue Aug 01 2006 Nils Philippsen <nphilipp@redhat.com> 0.8.1.p-5
- don't install world-writable documentation files (#200843)

* Mon Jul 24 2006 Nils Philippsen <nphilipp@redhat.com> 0.8.1.p-4
- require libtool for building

* Mon Jun 12 2006 Nils Philippsen <nphilipp@redhat.com> 0.8.1.p-3
- move gnome-screensaver desktop files to match new location in FC6 (#194862)

* Fri Jun 02 2006 Nils Philippsen <nphilipp@redhat.com> 0.8.1.p-2
- replace symlinked source files with copies to work around #189928
- honour RPM optflags

* Mon May 29 2006 Nils Philippsen <nphilipp@redhat.com> 0.8.1.p-1
- bump release

* Fri May 26 2006 Nils Philippsen <nphilipp@redhat.com> 0.8.1.p-0.6
- symlink hacks to /usr/libexec/xscreensaver
- own directories not included in filesystem

* Wed May 24 2006 Nils Philippsen <nphilipp@redhat.com> 0.8.1.p-0.5
- include %%{patchext} in version
- fix excessively long line in %%description
- make -kde require -xscreensaver
- fix "Actions", add "X-KDE-Category" and "X-KDE-Type" to KDE desktop files

* Tue May 23 2006 Nils Philippsen <nphilipp@redhat.com> 0.8.1.p-0.4
- remove executable bit from doc files, change README.fedora accordingly
- use %%buildroot consistently
- don't ship rss-glx_install.pl
- make %%description more understandable (Jason Tibbitts)

* Mon May 22 2006 Nils Philippsen <nphilipp@redhat.com> 0.8.1.p-0.3
- include README.fedora, rss-glx-rm-matrixview.sh, rss-glx-0.8.1-0.8.1.p.diff
  to be able to generate patched from upstream tarball
- versionize %%changelog
- don't obsolete rss_glx
- don't distribute zero-length AUTHORS and NEWS files

* Mon Apr 03 2006 Nils Philippsen <nphilipp@redhat.com> 0.8.1.p-0.2
- add libXt-devel to modular X build requirements (#90133)

* Tue Mar 28 2006 Nils Philippsen <nphilipp@redhat.com>
- use freealut when needed

* Fri Mar 10 2006 Nils Philippsen <nphilipp@redhat.com>
- add build requirements for non-modular X, default determined by Fedora
  version
- patch tarball to remove matrixview
- don't build gnome-screensaver subpackage before FC5

* Thu Mar 09 2006 Nils Philippsen <nphilipp@redhat.com> 0.8.1
- version 0.8.1
- include gnome-screensaver support
- new build requirements for FC5

* Wed Jul 07 2004 Nils Philippsen <nphilipp@redhat.com>
- rebuild for FC2

* Wed Sep 10 2003 Nils Philippsen <nphilipp@redhat.com>
- version 0.7.6
- manage new matrixview and spirographx hacks in XScreensaver.ad

* Fri Jul 04 2003 Nils Philippsen <nphilipp@redhat.com>
- version 0.7.4
- fix temp file issue in scripts
- buildrequire OpenAL-devel
- move stuff out of /usr/X11R6
- patch inline asm to work with new gcc versions
- remove hacks from XScreensaver.ad in %%preun
