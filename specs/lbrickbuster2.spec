# we ship lbreakout2 under a different name because of trademark concerns
%define realname lbreakout2

Name:           lbrickbuster2
Version:        2.6.5
Release:        24%{?dist}
Summary:        Brickbuster arcade game
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://lgames.sourceforge.net/
Source0:        http://downloads.sourceforge.net/lgames/%{realname}-%{version}.tar.gz
# replacement art changing the logos from lbreakout2 to lbrickbuster2
Source1:        %{name}-art.tar.gz
Patch0:         lbrickbuster2-rebrand-images.patch  
Patch1:         lbrickbuster2-default-fullscreen.patch
Patch2:         lbrickbuster2-fix-fortify-source.patch
BuildRequires:  gcc make
BuildRequires:  SDL_mixer-devel libpng-devel ImageMagick desktop-file-utils
BuildRequires:  gettext
Requires:       hicolor-icon-theme
# obsolete non rebranded freshrpms version
Obsoletes:      lbreakout2 <= %{version}-%{release}
Provides:       lbreakout2 = %{version}-%{release}

%description
The successor to LBrickBuster offers you a new challenge in more than 50 levels
with loads of new bonuses (goldshower, joker, explosive balls, bonus magnet
...), maluses (chaos, darkness, weak balls, malus magnet ...) and special
bricks (growing bricks, explosive bricks, regenerative bricks ...). If you
are still hungry for more after that you can create your own levelsets with
the integrated level editor.


%prep
%autosetup -p1 -a 1 -n %{realname}-%{version}
# fully automated rebrand to lbrickbuster
for i in `find -type f -not -name "*.png" -not -name "*.wav"`; do
  touch -r $i $i.stamp
  sed -i -e 's/Breakout/Brickbuster/g' -e 's/breakout/brickbuster/g' $i
  touch -r $i.stamp $i
  rm $i.stamp
done
# and rename some files to match
mv client/lbreakout.h client/lbrickbuster.h
mv client/levels/LBreakout1 client/levels/LBrickbuster1
mv client/levels/LBreakout2 client/levels/LBrickbuster2
# install replacement art and remove themes overrides
mv fr_top.png menuback.png client/gfx/AbsoluteB
mv client/gfx/AbsoluteB/fr_*.png client/gfx/AbsoluteB/menuback.png client/gfx
rm client/gfx/Oz/fr_*.png client/gfx/Moiree/fr_*.png
mv lbreakout32.gif lbrickbuster32.gif
mv lbreakout48.gif lbrickbuster48.gif
mv lbreakout2.desktop.in lbrickbuster2.desktop.in
# rebranding done, other fixes / cleanups below
sed -i 's|/usr/doc/%{name}|%{_defaultdocdir}/%{name}|g' po/*.po client/help.c
iconv -f ISO_8859-1 -t utf-8 ChangeLog > ChangeLog.tmp
touch -r ChangeLog ChangeLog.tmp
mv ChangeLog.tmp ChangeLog


%build
%configure --localstatedir=%{_var}/games --with-docdir=%{_defaultdocdir}
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
install -p -m 644 AUTHORS ChangeLog README TODO \
  $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}
%find_lang %{name}

# Install desktop entry, fix icon location
rm $RPM_BUILD_ROOT%{_datadir}/icons/lbrickbuster48.gif
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
sed -i 's|/usr/share/icons/lbrickbuster48.gif|%{name}|' \
    $RPM_BUILD_ROOT%{_datadir}/applications/lbrickbuster2.desktop
desktop-file-install \
    --delete-original \
    --add-category=ArcadeGame --add-category=BlocksGame \
    --dir $RPM_BUILD_ROOT%{_datadir}/applications/ \
    $RPM_BUILD_ROOT%{_datadir}/applications/lbrickbuster2.desktop
convert lbrickbuster32.gif \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
touch -r lbrickbuster32.gif \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
convert lbrickbuster48.gif \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
touch -r lbrickbuster48.gif \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

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
<!-- Copyright 2014 Edgar Muniz Berlinck <edgar.vv@gmail.com> -->
<!--
EmailAddress: wolfgang@rohdewald.de
SentUpstream: 2014-09-24
-->
<application>
  <id type="desktop">lbrickbuster2.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Free version of Breakout</summary>
  <description>
    <p>
      Break all the tiles and don't let your ball fall.
      Simple and fun.
    </p>
  </description>
  <url type="homepage">http://lgames.sourceforge.net/index.php?project=LBreakout2</url>
  <screenshots>
    <screenshot type="default">http://lgames.sourceforge.net/LBreakout2/ss2.jpg</screenshot>
  </screenshots>
</application>
EOF


%files -f %{name}.lang
%doc %{_defaultdocdir}/%{name}
%license COPYING
%attr(2755, root, games) %{_bindir}/%{name}
%{_bindir}/%{name}server
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/appdata/*%{name}.appdata.xml
%{_datadir}/applications/*%{name}.desktop
%verify(not md5 size mtime) %config(noreplace) %attr(664, games, games) %{_var}/games/%{name}.hscr


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.6.5-23
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Thomas Huth <thuth@redhat.com> - 2.6.5-20
- Fix crash due to bad buffersize caught by -D_FORTIFY_SOURCE=3
- Resolves: rhbz#2249220

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.6.5-7
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.6.5-5
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Apr 03 2016 Hans de Goede <hdegoede@redhat.com> - 2.6.5-1
- New upstream release 2.6.5 (rhbz#1315462)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 2.6.4-8
- Add an AppData file for the software center

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 24 2013 Jon Ciesla <limburgher@gmail.com> - 2.6.4-4
- Drop desktop vendor tag.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul  5 2012 Hans de Goede <hdegoede@redhat.com> - 2.6.4-1
- New upstream release 2.6.4

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Hans de Goede <hdegoede@redhat.com> - 2.6.3-1
- New upstream release 2.6.3
- This fixes building with libpng-1.5 (amongst other things)

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 2.6-0.13.beta7
- Rebuild for new libpng

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-0.12.beta7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-0.11.beta7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-0.10.beta7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 28 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 2.6-0.9.beta7
- Rebrand to lbrickbuster2 to avoid potential trademark issues
- Cleanup specfile
- Submit for Fedora inclusion

* Tue Aug 28 2006 Matthias Saou <http://freshrpms.net/> 2.6-0.8.beta
- Update to 2.6beta-7.

* Mon May 29 2006 Matthias Saou <http://freshrpms.net/> 2.6-0.7.beta
- Update to 2.6beta-6.

* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 2.6-0.6.beta
- Release bump to drop the disttag number in FC5 build.

* Wed Nov 30 2005 Matthias Saou <http://freshrpms.net/> 2.6-0.5.beta
- Update to 2.6beta-5.

* Mon Nov 14 2005 Matthias Saou <http://freshrpms.net/> 2.6-0.4.beta
- Update to 2.6beta-4.
- No longer override datadir to datadir/games/ to get the locales installed.
- Include translations.

* Fri Oct 21 2005 Matthias Saou <http://freshrpms.net/> 2.6-0.3.beta
- Update to 2.6beta-3.

* Thu Oct 20 2005 Matthias Saou <http://freshrpms.net/> 2.6-0.2.beta
- Update to 2.6beta-2 (use ugly temp "-2" instead of complex macros).
- Missing common/gettext.h, doesn't build, reported upstream, so beta-3 out.

* Tue May 17 2005 Matthias Saou <http://freshrpms.net/> 2.6-0.1.beta
- Update to 2.6beta.

* Fri Jan 14 2005 Matthias Saou <http://freshrpms.net/> 2.5.2-1
- Update to 2.5.2.

* Sun Sep 26 2004 Matthias Saou <http://freshrpms.net/> 2.5.1-1
- Update to 2.5.1.

* Mon Aug  9 2004 Matthias Saou <http://freshrpms.net/> 2.5-1
- Update to 2.5 final.

* Mon Jun 21 2004 Matthias Saou <http://freshrpms.net/> 2.5-0.beta8.1
- Update to 2.5beta-8.

* Mon Jun 14 2004 Matthias Saou <http://freshrpms.net/> 2.5-0.beta6.1
- Update to 2.5beta-6.

* Tue May 18 2004 Matthias Saou <http://freshrpms.net/> 2.5-0.beta5.1
- Update to 2.5beta-5.
- Change the gif pixmap to png.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 2.5-0.beta3.1
- Update to 2.5beta-3.
- Added missing zlib and libpng dependencies.
- Rebuild for Fedora Core 1.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Sun Mar  9 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.4.1.

* Fri Jan  3 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.4.

* Sat Oct 26 2002 Matthias Saou <http://freshrpms.net/>
- Fixed the menu entry, thanks to Erwin J. Prinz.

* Sat Sep 28 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.
- New menu entry with icon.

* Mon Sep 23 2002 Matthias Saou <http://freshrpms.net/>
- Update to 2.3.5.

* Tue Sep 10 2002 Matthias Saou <http://freshrpms.net/>
- Update to 2.3.3.

* Tue Sep 10 2002 Matthias Saou <http://freshrpms.net/>
- Update to 2.3.3.

* Mon Aug 19 2002 Matthias Saou <http://freshrpms.net/>
- Update to 2.3.2.

* Wed Aug 14 2002 Matthias Saou <http://freshrpms.net/>
- Update to 2.3.1.

* Thu May  2 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt against Red Hat Linux 7.3.
- Added the %%{?_smp_mflags} expansion.

* Sun Feb 24 2002 Matthias Saou <http://freshrpms.net/>
- Update to 2.2.2.

* Tue Feb  5 2002 Matthias Saou <http://freshrpms.net/>
- Update to 2.2.1.

* Mon Jan 28 2002 Matthias Saou <http://freshrpms.net/>
- Update to 2.2.

* Sun Jan  6 2002 Matthias Saou <http://freshrpms.net/>
- Update to 2.1.2.

* Tue Jan  1 2002 Matthias Saou <http://freshrpms.net/>
- Update to 2.1.1.

* Sat Dec  8 2001 Matthias Saou <http://freshrpms.net/>
- Update to 2.0.1.

* Thu Nov 29 2001 Matthias Saou <http://freshrpms.net/>
- Update to 2.0-pre2.

* Thu Nov 22 2001 Matthias Saou <http://freshrpms.net/>
- Update to 2.0beta2.

* Tue Apr 10 2001 Matthias Saou <http://freshrpms.net/>
- Update to 010315.

* Mon Nov 27 2000 Matthias Saou <http://freshrpms.net/>
- Initial RPM release for RedHat 7.0

