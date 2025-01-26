Name:           nazghul
Version:        0.7.1
Release:        39.20120228gitb0a402a%{?dist}
Summary:        A computer role-playing game (CRPG) engine

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://sourceforge.net/projects/nazghul/

# Occasionally upstream names things with an underscore.
%global         version_us %(echo %{version} | sed -e 's/\\./_/g')

# Construct cvs checkout tarball with:
#  ./nazghul-make-snapshot %%{cvsdate}
Source0:        nazghul-20120228gitb0a402a.txz
Source1:        haxima-music-license
# Since xcftools is orphaned, this was converted manually from haxima.xcf.  If
# there is ever an update, upstream will hopefully include this icon in the
# tarball.
Source2:        haxima.png
Patch0:         nazghul-desktop.patch
Patch1:         nazghul-format-security.patch
Patch2:         nazghul-armbuild.patch

# For building from a CVS snapshot
BuildRequires: make
BuildRequires:  automake, autoconf, gcc-c++
BuildRequires:  SDL_image-devel, SDL_mixer-devel, desktop-file-utils
BuildRequires:  libpng-devel

%description
Nazghul is an old-school RPG engine modeled after those made in the
heyday of top-down, 2d tile-based graphics. It is specifically modeled
after Ultima V.


%package -n haxima
Summary:        A full-featured role-playing game for the Nazghul engine
# The music files installed in /usr/share/nazghul/haxima/music have been
# relicensed as CC-BY-SA-2.0.   See the
# haxima-music-license file for details. The rest of the package is GPL-2.0-or-later.
License:        GPL-2.0-or-later AND CC-BY-SA-2.0
Requires:       nazghul = %{version}
Provides:       nazghul-haxima = %{version}-%{release}
Obsoletes:      nazghul-haxima < 0.6.0-8

%description -n haxima
A complete, playable and full-featured role playing game which runs
under the Nazghul CRPG engine.

You must install Nazghul in order to play Haxima.


%prep
%autosetup -p1 -n %{name}

# clean up CVS directories left in the source tarball
find . -depth -type d -name CVS -exec rm -rf {} \;

# Fix line endings
sed -i -e 's/\r//' doc/engine_extension_and_design/my_TODO.2004.05.05.txt

mv doc/* .

cp %SOURCE1 .


%build
export CFLAGS="-std=c++14 $RPM_OPT_FLAGS"
./autogen.sh
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

mv %{buildroot}/%{_bindir}/haxima.sh %{buildroot}/%{_bindir}/haxima

desktop-file-install \
    --dir %{buildroot}/%{_datadir}/applications \
    --add-category X-Fedora                     \
    haxima.desktop

install -D -m 644 %SOURCE2 %{buildroot}/%{_datadir}/pixmaps/haxima.png

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/haxima.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ryan Lerch <rlerch@redhat.com> -->
<!--
BugReportURL: https://sourceforge.net/p/nazghul/support-requests/5/
SentUpstream: 2014-09-24
-->
<application>
  <id type="desktop">haxima.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Top view 2D role playing game</summary>
  <description>
    <p>
      Haxima is a 2D role playing game (RPG) that runs on the Nazghul engine.
      You start out as a defenseless wanderer, you have to equip yourself,
      learn spells, and travel the land completing quests.
    </p>
  </description>
  <url type="homepage">http://myweb.cableone.net/gmcnutt/nazghul.html</url>
  <screenshots>
    <screenshot type="default">https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/haxima/a.png</screenshot>
    <screenshot>https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/haxima/b.png</screenshot>
  </screenshots>
</application>
EOF

%files
%{_bindir}/nazghul
%dir %{_datadir}/nazghul
%doc AUTHORS ChangeLog COPYING NEWS GAME_RULES GHULSCRIPT
%doc MAP_HACKERS_GUIDE engine_extension_and_design world_building


%files -n haxima
%{_bindir}/haxima
%{_datadir}/nazghul/haxima
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/*haxima.desktop
%{_datadir}/pixmaps/haxima.png
%doc USERS_GUIDE haxima-music-license


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-39.20120228gitb0a402a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.7.1-38.20120228gitb0a402a
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-37.20120228gitb0a402a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-36.20120228gitb0a402a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-35.20120228gitb0a402a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-34.20120228gitb0a402a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-33.20120228gitb0a402a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-32.20120228gitb0a402a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-31.20120228gitb0a402a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-30.20120228gitb0a402a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-29.20120228gitb0a402a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 Jeff Law <law@redhat.com> - 0.7.1-28.20120228gitb0a402a
- Force C++14 as this code is not C++17 ready

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-27.20120228gitb0a402a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-26.20120228gitb0a402a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-25.20120228gitb0a402a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-24.20120228gitb0a402a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 17 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.7.1-23.20120228gitb0a402a
- Stop using xcf2png because it's been orphaned.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-22.20120228gitb0a402a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 18 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.7.1-21.20120228gitb0a402a
- Add g++ build dependency.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-20.20120228gitb0a402a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-19.20120228gitb0a402a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-18.20120228gitb0a402a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-17.20120228gitb0a402a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-16.20120228gitb0a402a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 25 2016 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.7.1-15.20120228gitb0a402a
- Remove pointless %%defattr statements.

* Fri Dec 25 2015 Jason L Tibbitts III <tibbs@math.uh.edu>
- Change %%define to %%global.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-14.20120228gitb0a402a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.7.1-13.20120228gitb0a402a
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.7.1-12.20120228gitb0a402a
- Add an AppData file for the software center

* Sat Feb 21 2015 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.7.1-11.20120228gitb0a402a
- Generate a 256x256 icon from the included XCF to fix bug 1157591.

* Sat Feb 21 2015 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.7.1-10.20120228gitb0a402a
- Fix build on ARM.

* Sat Feb 21 2015 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.7.1-9.20120228gitb0a402a
- Fix format-security errors.
- Fix upstream URL.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-8.20120228gitb0a402a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-7.20120228gitb0a402a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-6.20120228gitb0a402a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 29 2013 Jon Ciesla <limburgher@gmail.com> - 0.7.1-5.20120228gitb0a402a
- Drop desktop vendor tag.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-4.20120228gitb0a402a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-3.20120228gitb0a402a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.7.1-2.20120228gitb0a402a
- Upstream switched to git.
- Update to latest snapshot.

* Wed Feb 01 2012 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.7.1-1.20120104cvs
- The package version actually incremented between the previous snapshot and
  this one, so update to reflect that.  There have been no upstream changes
  since October, 2011.

* Wed Jan 04 2012 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.7.0-4.20120104cvs
- Update to current CVS, fixing  many compiler warnings.
- Don't install the INSTALL file.
- Small spec cleanups.

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.7.0-3.20100413cvs
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-2.20100413cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Aug 17 2010 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.7.0-1.20100413cvs
- Update to post-0.7.0 release.
- Remove %%clean section; no longer required in Fedora.
- The music is now freely licensed!  Install the license file properly and
  document the change.

* Tue Sep 29 2009 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.7.0-0.4.20090928cvs
- Pull latest fixes.

* Tue Sep 22 2009 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.7.0-0.3.20090918cvs
- Modernize the spec a bit; nuke BuildRoot:, no more RPM_BUILD_ROOT.

* Fri Sep 18 2009 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.7.0-0.2.20090918cvs
- New CVS snapshot; hopefully fix x86_64 startup crash and music issues.

* Thu Sep 10 2009 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.7.0-0.1.20090910cvs
- Initial attempt to rebase to current CVS.
- Update to use xz for compression of snapshot tarballs.
- Rename "nazghul-haxima" package to "haxima", according to upstream wishes and
  common sense.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-7.20080407cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 14 2009 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.6.0-6.20080407cvs
- Tweak desktop file with proper categories (bug 485358) and fixes for other
  desktop-file-install complaints.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-5.20080407cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Apr 07 2008 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.6.0-4.20080407cvs
- Bump to latest CVS snapshot.

* Thu Mar 13 2008 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.6.0-3.20080312cvs
- Bump to current CVS version at upstream request.
- Add CVS snapshot generation instructions.
- Install the music which "make install" misses.

* Sun Feb 10 2008 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.6.0-2
- Rebuild for gcc 4.3.

* Mon Nov 05 2007 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.6.0-1
- Update to 0.6.0.

* Wed Aug 22 2007 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.5.6-4
- Patch upstream .desktop file for proper use of Version.
- Remove some errant CVS directories.
- Fix an end-of-line encoding.
- Minor spec cleanup.

* Tue Aug 21 2007 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.5.6-3
- License is GPLv2+.
- Bump for rebuild.

* Tue May 29 2007 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.5.6-2
- Bump release.

* Thu Jan 18 2007 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.5.6-0.1.rc1
- Bump to 0.5.6rc1.

* Sat Dec 16 2006 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.5.5-3
- Force a link against libpng since SDL_image only loads it at runtime.

* Fri Dec 15 2006 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.5.5-2
- Add libpng-devel build dependency.

* Fri Dec 15 2006 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.5.5-1
- Update to 0.5.5.

* Thu Aug 31 2006 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.5.4-2
- Rebuild.

* Thu Jun 29 2006 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.5.4-1
- Update to 0.5.4 release.

* Wed Jun 28 2006 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.5.3-6
- Update to CVS snapshot in preparation for the new release.

* Thu Jun  8 2006 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.5.3-5
- Add fix for crash when attacking diagonally in the wilderness.

* Tue Feb 14 2006 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.5.3-4
- More 64bit fixes.
- Package additional documentation.

* Mon Feb 13 2006 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.5.3-3
- Add some 64-bit cleanliness fixes.

* Tue Feb  7 2006 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.5.3-2
- Incorporate some review suggestions
- Patch bug with generation of haxima.sh.

* Sun Feb  5 2006 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.5.3-1
- Update to 0.5.3

* Sat Jan 28 2006 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.5.2-1
- Initial attempt
