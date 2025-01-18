Summary: 3D multi-player tank battle game
Name: bzflag
Version: 2.4.26
Release: 7%{?dist}
# Automatically converted from old format: LGPLv2 - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2
URL: http://bzflag.org
Source0: https://download.bzflag.org/bzflag/source/%{version}/bzflag-%{version}.tar.bz2
Source1: bzflag.desktop
Source2: bzflag.sysconfig
Source3: bzflag.service
BuildRequires: libXxf86vm-devel
BuildRequires: libXext-devel
BuildRequires: libSM-devel
BuildRequires: libICE-devel
BuildRequires: libX11-devel
BuildRequires: libGLU-devel
BuildRequires: make
BuildRequires: glew-devel
BuildRequires: gcc-c++
BuildRequires: desktop-file-utils
BuildRequires: SDL2-devel
BuildRequires: ncurses-devel
BuildRequires: libcurl-devel
BuildRequires: c-ares-devel
BuildRequires: zlib-devel
BuildRequires: sed
BuildRequires: systemd
Requires: opengl-games-utils
Requires(pre): shadow-utils

%description
BZFlag is a 3D multi-player tank battle game  that  allows users to play
against each other in a networked environment.  There are five teams: red,
green, blue, purple and rogue (rogue tanks are black).  Destroying a player
on another team  scores a win, while being destroyed or destroying a teammate
scores a loss.  Rogues have no teammates (not even other rogues), so they
cannot shoot teammates and they do not have a team score.
There are two main styles of play: capture-the-flag and free-for-all.

%package maps-sample
Summary: Sample maps for bzflag
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
BuildArch: noarch

%description maps-sample
This package contains sample world maps for bzflag.

%prep
%setup -q -n %{name}-%{version}

%build
# Use PIE because bzflag/bzfs are networked server applications
CFLAGS='-fPIC %{optflags} -fno-strict-aliasing' \
CXXFLAGS='-fPIC %{optflags} -fno-strict-aliasing' \
LDFLAGS='-pie' \
SDL_CFLAGS='-I%{_prefix}/include/SDL -D_GNU_SOURCE=1 -D_REENTRANT' \
%configure --libdir=%{_libdir}/%{name} --with-SDL=2 \
    --prefix=%{_prefix} --exec-prefix=%{_prefix} \
    --with-sdl-prefix=%{_prefix} --with-sdl-exec-prefix=%{_prefix}
%make_build

%install
%make_install
install -D -m 644 package/rpm/bzflag-m.xpm \
    %{buildroot}%{_datadir}/pixmaps/bzflag.xpm
install -D -m 644 misc/art/bzicon-red.svg \
    %{buildroot}%{_datadir}/pixmaps/bzflag.svg
mkdir -p %{buildroot}%{_datadir}/bzflag/maps
install -m 644 misc/maps/*.bzw %{buildroot}%{_datadir}/bzflag/maps
rm -f %{buildroot}%{_libdir}/bzflag/*.la
rm -f %{buildroot}%{_datadir}/bzflag/bzflag.desktop

ln -snf opengl-game-wrapper.sh %{buildroot}%{_bindir}/bzflag-wrapper
sed 's:^Exec=\(.*\)$:Exec=\1-wrapper:g' < %{SOURCE1} > bzflag.desktop

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --dir %{buildroot}%{_datadir}/applications bzflag.desktop

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ravi Srinivasan <ravishankar.srinivasan@gmail.com> -->
<!--
BugReportURL: https://sourceforge.net/p/bzflag/bugs/601/
SentUpstream: 2014-09-24
-->
<application>
  <id type="desktop">bzflag.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>An online multiplayer 3D tank battle game</summary>
  <description>
    <p>
      bzflag is a multiplayer tank battle game with "retro" 3D style graphics.
    </p>
  </description>
  <url type="homepage">http://bzflag.org</url>
  <screenshots>
    <screenshot type="default">http://bzflag.org/resources/screenshots/dantes_inferno_01.jpg</screenshot>
    <screenshot>http://bzflag.org/resources/screenshots/aa_bridge_crossing_01.jpg</screenshot>
    <screenshot>http://bzflag.org/resources/screenshots/pandemonium_01.jpg</screenshot>
  </screenshots>
</application>
EOF

install -Dp -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/bzflag
install -Dp -m 0644 %{SOURCE3} %{buildroot}%{_unitdir}/bzflag.service

%pre
getent group bzflag >/dev/null || groupadd -r bzflag
if getent passwd bzflag >/dev/null; then
    # provide a more meaningful GECOS field than the one introduced in 2.4.6-3
    if [ "x`getent passwd bzflag | cut -d: -f5`" = 'xUseful comment about the purpose of this account' ]; then
        usermod -c 'BZFlag game server' bzflag
    fi
else
    useradd -r -g bzflag -d %{_datadir}/bzflag -s /sbin/nologin \
    -c 'BZFlag game server' bzflag
fi
exit 0

%post
%systemd_post bzflag.service

%preun
%systemd_preun bzflag.service

%postun
%systemd_postun_with_restart bzflag.service

%files
%license COPYING
%doc AUTHORS ChangeLog README README.Linux
%{_bindir}/bzadmin
%{_bindir}/bzflag
%{_bindir}/bzflag-wrapper
%{_bindir}/bzfs
%dir %{_libdir}/bzflag
%{_libdir}/bzflag/*.so
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/bzflag
%exclude %{_datadir}/bzflag/maps/*
%{_datadir}/pixmaps/bzflag.xpm
%{_datadir}/pixmaps/bzflag.svg
%{_mandir}/man*/*
%{_sysconfdir}/sysconfig/bzflag
%{_unitdir}/bzflag.service

%files maps-sample
%{_datadir}/bzflag/maps/*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.26-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 2.4.26-6
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.26-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.26-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Nov 26 2022 Jeff Makey <jeff@makey.net> 2.4.26-1
- version 2.4.26

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 10 2022 Orion Poplawski <orion@nwra.com> - 2.4.22-4
- Rebuild for glew 2.2

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Mar 12 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.4.22-1
- 2.4.22

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.4.18-11
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.18-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.18-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.18-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 03 2019 Gwyn Ciesla <gwync@protonmail.com> - 2.4.18-6
- Switch to SDL2

* Fri Aug 09 2019 Gwyn Ciesla <gwync@protonmail.com> - 2.4.18-5
- Adapt for flatpak.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Jeff Makey <jeff@makey.net> 2.4.18-2
- Provide a more meaningful GECOS field than the one introduced in 2.4.6-3.

* Fri Oct 19 2018 Gwyn Ciesla <limburgher@gmail.com> - 2.4.18-1
- 2.4.18

* Mon Sep 24 2018 Gwyn Ciesla <limburgher@gmail.com> - 2.4.16-1
- 2.4.16

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 02 2018 Gwyn Ciesla <limburgher@gmail.com> - 2.4.14-1
- 2.4.14.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 30 2017 Gwyn Ciesla <limburgher@gmail.com> - 2.4.12-1
- 2.4.12.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Gwyn Ciesla <limburgher@gmail.com> - 2.4.10-1
- 2.4.10.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Jon Ciesla <limburgher@gmail.com> - 2.4.8-1
- 2.4.8.

* Wed Jul 06 2016 Jon Ciesla <limburgher@gmail.com> - 2.4.6-3
- Run server under bzflag user.
- Revert to SDL.

* Tue Jun 28 2016 Jon Ciesla <limburgher@gmail.com> - 2.4.6-2
- Add unit file, BZ 198929.

* Tue Jun 28 2016 Jon Ciesla <limburgher@gmail.com> - 2.4.6-1
- 2.4.6.
- Use SDL2.

* Sat Feb 20 2016 Jeff Makey <jeff@makey.net> 2.4.4-1
- version 2.4.4
- new source URL
- do not run autogen.sh now that upstream uses autoconf 2.69
- remove obsolete build requirements
- remove unused upstream bzflag.desktop file

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Adam Jackson <ajax@redhat.com> - 2.4.2-15
- Rebuild for glew 1.13

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.4.2-13
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 2.4.2-12
- Add an AppData file for the software center

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 11 2014 Richard Hughes <richard@hughsie.com> - 2.4.2-10
- Use the upstream SVG icon rather than the obsolete small XPM icon
- This makes bzflag show up in the software center applications

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Nov 18 2013 Dave Airlie <airlied@redhat.com> - 2.4.2-8
- rebuilt for GLEW 1.10

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Mar 23 2013 Jeff Makey <jeff@makey.net> 2.4.2-6
- run autogen.sh before configure to gain aarch64 support (#925121)
- fix bogus dates in changelog

* Mon Mar 11 2013 Jeff Makey <jeff@makey.net> 2.4.2-5
- desktop file cleanup

* Thu Feb 14 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 2.4.2-4
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- clean up spec to follow current guidelines
- drop obsolete cruft

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 13 2012 Adam Jackson <ajax@redhat.com> - 2.4.2-2
- Rebuild for glew 1.9.0

* Sun Jul 29 2012 Jeff Makey <jeff@makey.net> 2.4.2-1
- version 2.4.2
- remove BUGS and NEWS doc files which are now content free

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-4
- Rebuilt for c++ ABI breakage

* Tue Jan 10 2012 Nils Philippsen <nils@redhat.com> - 2.4.0-3
- rebuild for gcc 4.7

* Wed Aug 17 2011 Jeff Makey <jeff@makey.net> 2.4.0-2
- build require zlib-devel

* Wed Aug 17 2011 Jeff Makey <jeff@makey.net> 2.4.0-1
- version 2.4.0
- build require glew-devel
- remove obsolete --disable-static and --enable-shared configure options
- set plugin directory with --libdir
- use new sample maps source directory
- it is no longer necessary to remove bzfquery man page

* Mon Apr 04 2011 Nils Philippsen <nils@redhat.com> 2.0.16-3
- package sample maps in their own subpackage (#587815)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Apr 09 2010 Nils Philippsen <nils@redhat.com> 2.0.16-1
- version 2.0.16
- drop obsolete gold patch

* Wed Mar 03 2010 Nils Philippsen <nils@redhat.com> 2.0.14-1
- explicitly link libraries (#565122, patch by Jeff Makey, slightly modified)

* Tue Feb 16 2010 Nils Philippsen <nils@redhat.com>
- version 2.0.14
- don't run autoreconf
- remove obsolete lookup patch (see
  http://sourceforge.net/tracker/index.php?func=detail&aid=1197856&group_id=3248&atid=303248)
- remove obsolete gcc patch
- use --disable-static instead of removing *.a files
- remove bzfquery man page
- sanitize source URL, get rid of %%date

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
* - 2.0.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar 02 2009 Nils Philippsen <nils@redhat.com> 2.0.12-5
- fix building with gcc-4.4

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 22 2008 Nils Philippsen <nils@redhat.com> 2.0.12-4
- use autoreconf -i

* Wed Jul 09 2008 Nils Philippsen <nphilipp@redhat.com> 2.0.12-3
- build with SDL, but fix finding resolutions (#426011)

* Tue Jul 08 2008 Nils Philippsen <nphilipp@redhat.com> 2.0.12-2
- build without SDL (#426011)

* Tue Jul 08 2008 Nils Philippsen <nphilipp@redhat.com> 2.0.12-1
- version 2.0.12
- fix source URL
- drop plugin patch
- use %%bcond_with/_without macros

* Fri Feb 22 2008 Nils Philippsen <nphilipp@redhat.com> 2.0.10-6
- update gcc-4.3 patch (plugins, #434347)
- require libcurl-devel from Fedora 9 onward

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.0.10-5
- Autorebuild for GCC 4.3

* Fri Jan 04 2008 Nils Philippsen <nphilipp@redhat.com> 2.0.10-4
- fix headers for C++ with gcc-4.3

* Thu Dec 20 2007 Nils Philippsen <nphilipp@redhat.com> 2.0.10-3
- fix global plugin directory

* Wed Dec 19 2007 Nils Philippsen <nphilipp@redhat.com> 2.0.10-2
- build and package plugins

* Mon Dec 17 2007 Nils Philippsen <nphilipp@redhat.com> 2.0.10-1
- version 2.0.10

* Wed Oct 17 2007 Nils Philippsen <nphilipp@redhat.com> 2.0.8-8
- really use opengl-games-wrapper.sh from Fedora 7 on (#304781)

* Tue Oct 16 2007 Nils Philippsen <nphilipp@redhat.com> 2.0.8-7
- use opengl-games-wrapper.sh from Fedora 7 on (#304781)

* Wed Sep 05 2007 Nils Philippsen <nphilipp@redhat.com> 2.0.8-6
- change license tag from LGPL to LGPLv2

* Fri Jun 22 2007 Nils Philippsen <nphilipp@redhat.com>
- change license tag from GPL to LGPL

* Mon Nov 06 2006 Jindrich Novy <jnovy@redhat.com> 2.0.8-4
- rebuild because of the new curl

* Mon Aug 28 2006 Nils Philippsen <nphilipp@redhat.com> 2.0.8-3
- FC6 mass rebuild

* Tue Jul 11 2006 Nils Philippsen <nphilipp@redhat.com> 2.0.8-2
- rebuild to pick up new c-ares version

* Tue May 16 2006 Nils Philippsen <nphilipp@redhat.com> 2.0.8-1
- version 2.0.8

* Fri May 12 2006 Nils Philippsen <nphilipp@redhat.com> 2.0.6-1
- automatically decide between modular/traditional X depending on %%fedora

* Thu May 11 2006 Nils Philippsen <nphilipp@redhat.com>
- version 2.0.6
- add disttag
- remove upstreamed stringdos patch
- adapt %%files

* Fri Feb 17 2006 Nils Philippsen <nphilipp@redhat.com> 2.0.4-3
- rebuild

* Wed Dec 28 2005 Nils Philippsen <nphilipp@redhat.com> 2.0.4-2
- don't crash on maliciously formed callsign, etc. strings (#176626, patch
  backported from upstream CVS)

* Mon Nov 21 2005 Nils Philippsen <nphilipp@redhat.com> 2.0.4-1
- version 2.0.4
- update lookup patch
- build require c-ares-devel instead of adns-devel
- add newly introduced libs and includes (but exclude headers and static libs,
  courtesy of Matthias Saou)
- use -fPIC, -pie (hopefully) correctly to avoid build problems on x86_64

* Thu Nov 17 2005 Nils Philippsen <nphilipp@redhat.com> 2.0.2-5
- rebuild to pick up new openssl version
- prepare for modular X
- appease ISO C++

* Mon May 09 2005 Nils Philippsen <nphilipp@redhat.com> 2.0.2-4
- build with -fno-strict-aliasing (typo)

* Mon May 09 2005 Nils Philippsen <nphilipp@redhat.com> 2.0.2-3
- build with -fnostrict-aliasing

* Wed Apr 06 2005 Nils Philippsen <nphilipp@redhat.com> 2.0.2-2
- build with adns
- build require libGL-devel and libGLU-devel to hopefully resolve building
  problems
- apply name lookup patch

* Wed Mar 23 2005 Nils Philippsen <nphilipp@redhat.com>
- work around missing dependency in xorg-x11-devel

* Wed Mar 23 2005 Nils Philippsen <nphilipp@redhat.com>
- version 2.0.2

* Tue Mar 15 2005 Nils Philippsen <nphilipp@redhat.com> 2.0.0-4
- buildrequire bc for curl version check

* Fri Mar 04 2005 Nils Philippsen <nphilipp@redhat.com>
- move package over to Extras
- make desktop file a file, don't generate it in %%install
- use an a bit more individual build root
- buildrequire curl-devel

* Mon Feb 21 2005 Nils Philippsen <nphilipp@redhat.com> 2.0.0-3
- fix dates in %%changelog

* Fri Feb 18 2005 Nils Philippsen <nphilipp@redhat.com> 2.0.0-2
- build as PIE

* Fri Feb 18 2005 Nils Philippsen <nphilipp@redhat.com> 2.0.0-1
- correct source URL
- buildrequire ncurses-devel

* Tue Jan 18 2005 Nils Philippsen <nphilipp@redhat.com> 2.0.0-0.1
- version 2.0.0.20050117
- buildrequire xorg-x11-devel, not XFree86-devel

* Tue Aug 10 2004 Alan Cox <alan@redhat.com> 1.10.6-2
- Adopted for FC3 core from Matthias Saou's freshrpms package. Thanks
  to Matthias for doing all the work.

* Tue May 18 2004 Matthias Saou <http://freshrpms.net/> 1.10.6-1
- Update to 1.10.6.
- First rebuild for Fedora Core 2.

* Thu Mar 25 2004 Matthias Saou <http://freshrpms.net/> 1.10.4-2
- Removed explicit XFree86 dependency.

* Mon Feb 16 2004 Matthias Saou <http://freshrpms.net/> 1.10.4-1
- Update to 1.10.4.20040125, update the included docs.
- Removed no longer existing bzfls file and added bzadmin.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 1.7g2-2
- Rebuild for Fedora Core 1.
- Added missing gcc-c++ build dependency.

* Sun Jun 22 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.7g2.
- Major spec changes for the new build method.

* Tue Apr  1 2003 Matthias Saou <http://freshrpms.net/>
- Fix the Xfree86 dependency, doh!
- Clean up the confusing build.
- Add a system menu entry.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.7g0.
- Rebuilt for Red Hat Linux 9.

* Mon Nov  4 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.

* Wed Jun 19 2002 Matthias Saou <http://freshrpms.net/>
- Update to 1.7e6.

* Wed Feb 13 2002 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

