%global __cmake_in_source_build 1
Name:		xmoto
Version:	0.6.2
Release:	5%{?dist}
Summary:	Challenging 2D Motocross Platform Game

License:	GPL-2.0-or-later
URL:		http://xmoto.sourceforge.net/
Source0:	https://github.com/xmoto/xmoto/archive/v%{version}/%{version}.tar.gz
Source1:	xmoto.desktop
Source2:	xmoto.png
Patch0:		xmoto-0.5.0-helpers-text-includes.patch
Patch1:		xmoto-0.5.0-helpers-log-include.patch

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:	desktop-file-utils
BuildRequires:	SDL2_mixer-devel
BuildRequires:	SDL2_ttf-devel
BuildRequires:	curl-devel
BuildRequires:	ode-devel
BuildRequires:	lua-devel
BuildRequires:	libGL-devel
BuildRequires:	libGLU-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	bzip2-devel
BuildRequires:	sqlite-devel
BuildRequires:	SDL2_net-devel
BuildRequires:	libxdg-basedir-devel
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
BuildRequires:	gettext
BuildRequires:  cmake
BuildRequires:  zlib-devel
Requires: dejavu-sans-fonts


%description
X-Moto is a challenging 2D motocross platform game, where physics play an all
important role in the gameplay. You need to control your bike to its limit, if
you want to have a chance finishing the more difficult of the challenges.

First you'll try just to complete the levels, while later you'll compete with
yourself and others, racing against the clock.


%prep
%setup -q
%patch -P0 -p0
%patch -P1 -p0

%build
mkdir build
pushd build
%cmake -DPREFER_SYSTEM_BZip2=ON -DPREFER_SYSTEM_Lua=ON -DPREFER_SYSTEM_ODE=ON -DPREFER_SYSTEM_XDG=ON ..
%make_build
popd

%install
pushd build
%make_install

# Install icon and desktop file
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps

desktop-file-install  --dir $RPM_BUILD_ROOT%{_datadir}/applications --add-category X-Fedora %{SOURCE1}

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
<!-- Copyright 2014 Ryan Lerch <rlerch@redhat.com> -->
<!--
EmailAddress: neckelmann@gmail.com
SentUpstream: 2014-09-25
-->
<application>
  <id type="desktop">xmoto.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>2D motocross platform game</summary>
  <description>
    <p>
      xmoto is a side-scrolling 2D motocross platform game where the objective
      is to collect all the floating items in the level and proceed to the
      checkered finishing ball.
      The motocross bike that the player rides in
      xmoto has a lot of bounce, and the if the player hits their head on any
      solid object the level has to be restarted.
    </p>
    <p>
      There are hundreds of levels available in xmoto, both included in the
      initial install, and downloadable from the internet.
      There is also the
      ability to challenge fastest times with other players from around the world.
      and saved ghost data to visually see the runs of other players through the
      levels.
    </p>
  </description>
  <url type="homepage">http://xmoto.sourceforge.net/</url>
  <screenshots>
    <screenshot type="default">http://wiki.xmoto.tuxfamily.org/images/7/7d/Screenshot0022.png</screenshot>
    <screenshot>http://wiki.xmoto.tuxfamily.org/images/6/65/Xmoto01.png</screenshot>
    <screenshot>http://wiki.xmoto.tuxfamily.org/images/0/04/Screenshot0005.png</screenshot>
  </screenshots>
</application>
EOF
popd

rm $RPM_BUILD_ROOT%{_datadir}/xmoto/Textures/Fonts/DejaVuSans.ttf 
ln -s ../../../fonts/dejavu-sans-fonts/DejaVuSans.ttf $RPM_BUILD_ROOT%{_datadir}/xmoto/Textures/Fonts/DejaVuSans.ttf 

# Locale files
%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%license COPYING
%doc ChangeLog README.md
%{_bindir}/xmoto
%{_datadir}/xmoto
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/xmoto.desktop
%{_datadir}/icons/hicolor/48x48/apps/xmoto.png
%{_mandir}/man6/xmoto.6.gz
%{_datadir}/pixmaps/xmoto.png

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Mar 07 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.6.2-1
- 0.6.2

* Thu Mar 02 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.6.1-11
- migrated to SPDX license

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Jul 24 2022 Robert-André Mauchin <zebob.m@gmail.com> - 0.6.1-9
- Rebuilt for Ode soname bump

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 29 2022 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 0.6.1-7
-  Rebuild for new ode-0.16

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.6.1-1
- 0.6.1

* Mon Mar 16 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.5.11-20
- Fix dejavu symlink

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.11-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.11-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.11-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.11-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.11-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.11-14
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.11-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 22 2017 Jon Ciesla <limburgher@gmail.com> 0.5.11-11
- Fix FTBFS.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec 12 2015 Jon Ciesla <limburgher@gmail.com> 0.5.11-8
- Font display fix using svn trunk tarball, BZ 1290869.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.5.11-6
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.5.11-5
- Add an AppData file for the software center

* Wed Oct 29 2014 Jon Ciesla <limburgher@gmail.com> 0.5.11-4
- Use system ode, rebuild for new ode.

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Jon Ciesla <limburgher@gmail.com> 0.5.11-1
- 0.5.11, BZ1082323, moves back to lua 5.2.

* Fri Mar 28 2014 Jon Ciesla <limburgher@gmail.com> 0.5.10-9
- Move back to 5.1 to fix level problems, BZ 1071558.
- Fix changelog date.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 07 2013 Jon Ciesla <limburgher@gmail.com> 0.5.10-7
- Conrad Meyer <konrad@tylerc.org>'s patch for segfault.

* Sun Feb 10 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 0.5.10-6
- Remove vendor tag from desktop file as per https://fedorahosted.org/fesco/ticket/1077
- Cleanup spec as per recently changed packaging guidelines

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 0.5.10-5
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 0.5.10-4
- rebuild against new libjpeg

* Fri Aug 24 2012 Jon Ciesla <limburgher@gmail.com> 0.5.10-3
- Rebuild for new ode.

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Jon Ciesla <limburgher@gmail.com> 0.5.10-1
- New upstream, BZ 834616.
- libpng patch upstreamed.

* Fri Jan 06 2012 Jon Ciesla <limburgher@gmail.com> 0.5.9-2
- Patched for gcc 4.7.0.

* Wed Dec 07 2011 Jon Ciesla <limburgher@gmail.com> 0.5.9-1
- New upstream.

* Thu Nov 10 2011 Jon Ciesla <limb@jcomserv.net> 0.5.8-2
- Rebuild for libpng 1.5.

* Fri Oct 21 2011 Jon Ciesla <limb@jcomserv.net> 0.5.8-1
- New upstream.

* Mon Apr 11 2011 Jon Ciesla <limb@jcomserv.net> 0.5.7-1
- New upstream.

* Tue Mar 29 2011 Jon Ciesla <limb@jcomserv.net> 0.5.6-1
- New upstream.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 26 2011 Jon Ciesla <limb@jcomserv.net> 0.5.5-1
- New upstream.

* Mon Dec 13 2010 Jon Ciesla <limb@jcomserv.net> 0.5.4-1
- New upstream.

* Tue May 04 2010 Jon Ciesla <limb@jcomserv.net> 0.5.3-1
- New upstream.
- Dropped upstreamed x86-64 patch.

* Mon Dec 07 2009 Jon Ciesla <limb@jcomserv.net> 0.5.2-1.1
- EVR bump for fix CVS tagging snafu.

* Sun Dec 06 2009 Howard Liberty <liberty@live.com> 0.5.2-1
- New upstream.
- Add x86-64 patch so it can be compiled in x86-64 enviroment.

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 14 2009 Jon Ciesla <limb@jcomserv.net> 0.5.1-0
- New upstream.
- Dropped opengldepth patch, applied upstream.

* Mon Feb 23 2009 Jon Ciesla <limb@jcomserv.net> 0.5.0-6
- Patch for includes.

* Mon Feb 02 2009 Jon Ciesla <limb@jcomserv.net> 0.5.0-5
- Fix for ati crash, BZ 481485.

* Tue Jan 20 2009 Jon Ciesla <limb@jcomserv.net> 0.5.0-4
- Font requires change for BZ 480480, dejavu rename.

* Tue Dec 30 2008 Jon Ciesla <limb@jcomserv.net> 0.5.0-3
- Symlink to system font, BZ 477485.
- Dropped extension from icon in .desktop.

* Wed Dec 10 2008 Jon Ciesla <limb@jcomserv.net> 0.5.0-2
- No remaining fuzzy patches, dropping patch fuzz workaround.

* Mon Dec 01 2008 Jon Ciesla <limb@jcomserv.net> 0.5.0-1
- Update to 0.5.0.

* Wed Oct 15 2008 Hans de Goede <hdegoede@redhat.com> 0.4.2-4
- Fix crash caused by using new ode (bz 466738)

* Tue Sep 30 2008 Jon Ciesla <limb@jcomserv.net> 0.4.2-3
- Patch for new ode version.

* Fri Sep 12 2008 Jon Ciesla <limb@jcomserv.net> 0.4.2-2
- Introducted patch fuzz workaround, will fix.

* Tue Mar 18 2008 Jon Ciesla <limb@jcomserv.net> 0.4.2-1
- Update to 0.4.2.
- Dropping xmoto-man patch.

* Wed Feb 13 2008 Jon Ciesla <limb@jcomserv.net> 0.4.1-1
- Update to 0.4.1.
- Dropped subversion BR.

* Mon Feb 11 2008 Jon Ciesla <limb@jcomserv.net> 0.4.0-1
- Update to 0.4.0.
- Dropped unneeded patches.
- Added string patch, hash_map, inline(jwrdegoede) patch.
- BRed subversion.

* Tue Jan 08 2008 Jon Ciesla <limb@jcomserv.net> 0.3.4-2
- Added cstdlib, include extra tokens patches.
- GCC 4.3 rebuild.

* Thu Oct 25 2007 Jon Ciesla <limb@jcomserv.net> 0.3.4-1
- Bumped to 0.3.4.

* Mon Sep 24 2007 Jon Ciesla <limb@jcomserv.net> 0.3.3-2
- Patches from upstream to correct BZ 295981.

* Wed Aug 29 2007 Jon Ciesla <limb@jcomserv.net> 0.3.3-1
- Bumped to upstream.
- Fixed URL.

* Thu Aug 16 2007 Jon Ciesla <limb@jcomserv.net> 0.3.1-2
- License tag correction.

* Mon Jul 09 2007 Jon Ciesla <limb@jcomserv.net> 0.3.1-1
- Bumped to upstream, BZ 247445.

* Wed Jun 20 2007 Jon Ciesla <limb@jcomserv.net> 0.3.0-1
- Bumped to upstream.

* Mon Mar 19 2007 Jon Ciesla <limb@jcomserv.net> 0.2.7-1
- Bumped to upstream, fixed man issues.

* Fri Mar 16 2007 Jon Ciesla <limb@jcomserv.net> 0.2.6-2
- Bumped release, build mistake.

* Fri Mar 16 2007 Jon Ciesla <limb@jcomserv.net> 0.2.6-1
- New upstream release.
- Removed Application from .desktop.
- Spec cleanup.
- Fixed man path with patch.
- Removed X-Fedora.

* Wed Feb 28 2007 Jon Ciesla <limb@jcomserv.net> 0.2.4-1
- New upstream release
- xmoto-edit now seperate from base xmoto

* Mon Nov 13 2006 Hugo Cisneiros <hugo@devin.com.br> 0.2.2-2
- Added again the debuginfo package (it's working)

* Sun Nov 12 2006 Hugo Cisneiros <hugo@devin.com.br> 0.2.2-1
- New upstream release

* Mon Nov  6 2006 Jindrich Novy <jnovy@redhat.com> 0.2.0-2
- Rebuild against the new curl

* Wed Sep 13 2006 Hugo Cisneiros <hugo@devin.com.br> 0.2.0-1
- New upstream release

* Wed Sep 13 2006 Hugo Cisneiros <hugo@devin.com.br> 0.1.16-2
- Rebuilt for FC6

* Wed Jul  5 2006 Hugo Cisneiros <hugo@devin.com.br> 0.1.16-1
- Initial RPM release
