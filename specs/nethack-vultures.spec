Name:           nethack-vultures
Version:        2.1.2
Release:        41%{?dist}
Summary:        NetHack - Vulture's Eye and Vulture's Claw

License:        NGPL
URL:            http://www.darkarts.co.za/vulture-for-nethack
# This location is no longer valid
Source0:        http://downloads.usrsrc.org/vultures/%{version}/vultures-%{version}-full.tar.bz2
Source1:        %{name}.logrotate
Patch0:         %{name}-1.11.0-optflags.patch
Patch1:         %{name}-2.1.2-config.patch
Patch2:         %{name}-1.10.1-clawguide.patch
Patch3:         %{name}-2.1.2-tabfullscreen.patch
Patch4:         %{name}-2.1.2-logging.patch
Patch5:         %{name}-libpng.patch
Patch6:         format-fix.patch
Patch7:         parser-fix.patch
Patch8:         make-bison.patch
Patch9:         nethack-vultures-c99.patch
Patch10:	objtype.patch
Patch11:	doorfix.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  SDL-devel
BuildRequires:  SDL_mixer-devel >= 1.2.6
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_ttf-devel
BuildRequires:  SDL-static
BuildRequires:  libpng-devel
BuildRequires:  ncurses-devel
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  desktop-file-utils
BuildRequires:  groff
BuildRequires:  util-linux

# Automate finding font paths
%global fonts font(bitstreamveraserif)
BuildRequires:  fontconfig %{fonts}
Requires:       %{fonts}

Requires:       /usr/bin/bzip2
Requires:       logrotate
Requires(pre):  shadow-utils
Requires(pre):  coreutils
Obsoletes:      nethack-falconseye <= 1.9.4-6.a

%description
Vulture's Eye is a mouse-driven interface for NetHack that enhances
the visuals, audio and accessibility of the game, yet retains all the
original gameplay and game features.  Vulture's Eye is based on
Falcon's Eye, but is greatly extended.  Also included is Vulture's
Claw, which is based on the Slash'Em core.


%prep
%setup -q -n vultures-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -F1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p0 -b .libpng
%patch -P6 -p0 -b .format-fix
%patch -P7 -p0 -b .parser-fix
%patch -P8 -p0 -b .make-bison
%patch -P9 -p1
%patch 10 -p0
%patch 11 -p0
sed -i -e 's|/usr/games/lib/nethackdir|%{_prefix}/games/vultureseye|g' \
    nethack/doc/{nethack,recover}.6 nethack/include/config.h
sed -i -e 's|/var/lib/games/nethack|%{_var}/games/vultureseye|g' \
    nethack/include/unixconf.h
sed -i -e 's|/usr/games/lib/nethackdir|%{_prefix}/games/vulturesclaw|g' \
    slashem/doc/{nethack,recover}.6 slashem/include/config.h
sed -i -e 's|/var/lib/games/nethack|%{_var}/games/vulturesclaw|' \
    slashem/include/unixconf.h


%build
# Note: no %{?_smp_mflags} in any of these: various parallel build issues.
for i in nethack slashem ; do
    make $i/Makefile
    make -C $i
    make -C $i/util recover dlb dgn_comp lev_comp YACC="bison -y"
    make -C $i/dat spec_levs quest_levs
done


%install
rm -rf $RPM_BUILD_ROOT

make -C nethack install CHGRP=: CHOWN=: \
    GAMEDIR=$RPM_BUILD_ROOT%{_prefix}/games/vultureseye \
    VARDIR=$RPM_BUILD_ROOT%{_var}/games/vultureseye \
    SHELLDIR=$RPM_BUILD_ROOT%{_bindir}
make -C slashem install CHGRP=: CHOWN=: \
    GAMEDIR=$RPM_BUILD_ROOT%{_prefix}/games/vulturesclaw \
    VARDIR=$RPM_BUILD_ROOT%{_var}/games/vulturesclaw \
    SHELLDIR=$RPM_BUILD_ROOT%{_bindir}

install -dm 755 $RPM_BUILD_ROOT%{_mandir}/man6
install -pm 644 nethack/doc/nethack.6 \
    $RPM_BUILD_ROOT%{_mandir}/man6/vultureseye.6
install -pm 644 nethack/doc/recover.6 \
    $RPM_BUILD_ROOT%{_mandir}/man6/vultureseye-recover.6
install -pm 644 slashem/doc/nethack.6 \
    $RPM_BUILD_ROOT%{_mandir}/man6/vulturesclaw.6
install -pm 644 slashem/doc/recover.6 \
    $RPM_BUILD_ROOT%{_mandir}/man6/vulturesclaw-recover.6

install -dm 755 $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
for i in vultureseye vulturesclaw ; do
    desktop-file-install \
        --dir=$RPM_BUILD_ROOT%{_datadir}/applications \
        --mode=644 \
        --add-category=RolePlaying \
        --remove-category=Application \
        --remove-category=3DGame \
        --remove-category=PuzzleGame \
        dist/unix/desktop/$i.desktop
    mv $RPM_BUILD_ROOT%{_prefix}/games/$i/*.png \
        $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/$i.png
    mv $RPM_BUILD_ROOT%{_prefix}/games/$i/recover \
        $RPM_BUILD_ROOT%{_bindir}/$i-recover
done

ln -sf $(fc-match -f "%{file}" "bitstream:vera:serif") \
    $RPM_BUILD_ROOT%{_prefix}/games/vulturesclaw/fonts
ln -sf $(fc-match -f "%{file}" "bitstream:vera:serif") \
    $RPM_BUILD_ROOT%{_prefix}/games/vultureseye/fonts

rm -r $RPM_BUILD_ROOT%{_prefix}/games/vultures*/manual

# Save quite a bit of space
/usr/bin/hardlink -cv $RPM_BUILD_ROOT%{_prefix}/games/vultures*

chmod -s $RPM_BUILD_ROOT%{_prefix}/games/vultures*/vultures* # for stripping

# Clean up
sed -i -e "s|$RPM_BUILD_ROOT||" $RPM_BUILD_ROOT%{_bindir}/vultures{eye,claw}
rm $RPM_BUILD_ROOT%{_prefix}/games/vultures*/*.ico

install -Dpm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/%{name}
install -dm 775 $RPM_BUILD_ROOT%{_var}/log/vultures/



%pre
/usr/sbin/groupadd vultures 2> /dev/null || :
# Get dir symlinks that were there once out of the way
for dir in graphics sound music ; do
    [ -L %{_prefix}/games/vulturesclaw/$dir ] && \
        rm -f %{_prefix}/games/vulturesclaw/$dir || :
done

%files
%doc nethack/README nethack/dat/license nethack/dat/history nethack/dat/*help
%doc slashem/readme.txt slashem/history.txt slashem/slamfaq.txt
%doc vultures/gamedata/manual/
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%{_bindir}/vultures*
%dir %{_prefix}/games/vultureseye/
%{_prefix}/games/vultureseye/config/
%{_prefix}/games/vultureseye/defaults.nh
%{_prefix}/games/vultureseye/graphics/
%{_prefix}/games/vultureseye/license
%{_prefix}/games/vultureseye/music/
%{_prefix}/games/vultureseye/nhdat
%{_prefix}/games/vultureseye/sound/
%{_prefix}/games/vultureseye/fonts/
%{_prefix}/games/vultureseye/tiles/
%attr(2755,root,vultures) %{_prefix}/games/vultureseye/vultureseye
%dir %{_prefix}/games/vulturesclaw/
%{_prefix}/games/vulturesclaw/config/
%{_prefix}/games/vulturesclaw/defaults.nh
%{_prefix}/games/vulturesclaw/graphics/
%{_prefix}/games/vulturesclaw/Guidebook.txt
%{_prefix}/games/vulturesclaw/license
%{_prefix}/games/vulturesclaw/music/
%{_prefix}/games/vulturesclaw/nh*share
%{_prefix}/games/vulturesclaw/sound/
%{_prefix}/games/vulturesclaw/fonts/
%{_prefix}/games/vulturesclaw/tiles/
%attr(2755,root,vultures) %{_prefix}/games/vulturesclaw/vulturesclaw
%{_datadir}/applications/*vultures*.desktop
%{_datadir}/icons/hicolor/48x48/apps/vultures*.png
%{_mandir}/man6/vultures*.6*
%defattr(664,root,vultures,775)
%dir %{_var}/games/vultureseye/
%config(noreplace) %{_var}/games/vultureseye/record
%config(noreplace) %{_var}/games/vultureseye/perm
%config(noreplace) %{_var}/games/vultureseye/logfile
%dir %{_var}/games/vultureseye/save/
%dir %{_var}/games/vulturesclaw/
%config(noreplace) %{_var}/games/vulturesclaw/record
%config(noreplace) %{_var}/games/vulturesclaw/perm
%config(noreplace) %{_var}/games/vulturesclaw/logfile
%dir %{_var}/games/vulturesclaw/save/
%dir %{_var}/log/vultures/


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Bruno Wolff III <bruno@wolff.to> - 2.1.2-39
- Fix some mismatched types

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Apr 24 2023 Florian Weimer <fweimer@redhat.com> - 2.1.2-35
- Port to C99 (#2189107)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 09 2021 Bruno Wolff III <bruno@wolff.to> - 2.1.2-30
- Fix bison step of build process

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 22 2020 Bruno Wolff III <bruno@wolff.to> - 2.1.2-27
- Automate font path finding at build time

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 2019 Bruno Wolff III <bruno@wolff.to> - 2.1.2-24
- hardlink in util-linux has a different path than it did in hardlink

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.2-20
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jul 12 2015 Bruno Wolff III <bruno@wolff.to> - 2.1.2-15
- Lots of format string warnings addressed

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 10 2014 Bruno Wolff III <bruno@wolff.to> - 2.1.2-12
- Don't use messages as format strings

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 12 2013 Jon Ciesla <limburgher@gmail.com> - 2.1.2-9
- Drop desktop vendor tag.

* Sun Nov  4 2012 Bruno Wolff III <bruno@wolff.to> - 2.1.2-8
- Silence logrotate warning bz 768355

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 28 2012 Bruno Wolff III <bruno@wolff.to> - 2.1.2-6
- Update for libpng 1.5
- Abide by font guidelines (bz 477431)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 2.1.2-4
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 23 2009 Ville Skyttä <ville.skytta at iki.fi> - 2.1.2-1
- Update to 2.1.2 (#502292).
- Patch to log in %%{_var}/log/vultures.
- Bring icon cache update scriptlets up to date with current guidelines.
- Simplify and improve space savings by using hardlink.
- Build with bison instead of byacc; bison is needed anyway.
- Drop default patch fuzz, apply it selectively.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 08 2009 Jon Ciesla <limb@jcomserv.net> - 2.1.0-15
- Fix Requires(pre), BZ 475919.

* Mon Aug 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.1.0-14
- fix license tag

* Sun Aug 3 2008 Karen Pease <meme@daughtersoftiresias.org> - 2.1.0-13
- Adding default patch fuzz

* Tue Mar 11 2008 Karen Pease <meme@daughtersoftiresias.org> - 2.1.0-12
- Added SDL-static requirement.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.1.0-11
- Autorebuild for GCC 4.3

* Tue Aug 14 2007 Hans de Goede <j.w.r.degoede@hhs.nl> - 2.1.0-10
- Fixup .desktop file categories

* Sat Mar 10 2007 Hans de Goede <j.w.r.degoede@hhs.nl> - 2.1.0-9
- Make the binaries run with their own gid instead of gid games, to minimize
  results of a possible privelidge escalation (bz 187382)
- Fix the crashes on fs<->window toggle on a 16bpp X-server
- Fixup .desktop file categories

* Tue Oct 10 2006 Karen Pease <meme@daughtersoftiresias.org> - 2.1.0-8
- Add in pre-tag to eliminate the old graphics directory symlink that was confusing rpm.

* Fri Sep 15 2006 Karen Pease <meme@daughtersoftiresias.org> - 2.1.0-7
- Rebuild

* Tue Aug 29 2006 Karen Pease <meme@daughtersoftiresias.org> - 2.1.0-6
- Attempting to stop graphics duplication.

* Thu Aug 24 2006 Karen Pease <meme@daughtersoftiresias.org> - 2.1.0-5
- Attempting to stop graphics duplication.

* Wed Aug 16 2006 Karen Pease <meme@daughtersoftiresias.org> - 2.1.0-4
- Attempting to stop graphics duplication.

* Sun Aug 13 2006 Karen Pease <meme@daughtersoftiresias.org> - 2.1.0-3
- Attempting to stop graphics duplication.

* Mon Jun 26 2006 Karen Pease <meme@daughtersoftiresias.org> - 2.1.0-2
- Dealt with the gametiles.bin eye bug not present in claw.

* Thu Jun 08 2006 Karen Pease <meme@daughtersoftiresias.org> - 2.1.0-1
- Upgraded patches 2.1.1

* Wed Jun 07 2006 Karen Pease <meme@daughtersoftiresias.org> - 2.1.0-0
- Upgraded to 2.1.0

* Fri Apr 14 2006 Karen Pease <meme@daughtersoftiresias.org> - 2.0.0-5
- Upped the release tag to keep up with FC-3

* Sun Apr 09 2006 Karen Pease <meme@daughtersoftiresias.org> - 2.0.0-3
- Packaged extra fonts

* Sun Apr 09 2006 Karen Pease <meme@daughtersoftiresias.org> - 2.0.0-2
- Upped the release to try and make the plague server use the right source tarball.

* Sat Apr 08 2006 Karen Pease <meme@daughtersoftiresias.org> - 2.0.0-1
- Upgraded to 2.0.0

* Wed Mar 01 2006 Karen Pease <meme@daughtersoftiresias.org> - 1.11.2-5
- Rebuilt for FC5

* Thu Feb 02 2006 Frank Arnold <frank@scirocco-5v-turbo.de> - 1.11.2-4
- Got a working plague build by working around util-linux bug #176441.

* Sun Jan 08 2006 Karen Pease <meme@daughtersoftiresias.org> - 1.11.2-3
- To fix a strange error on the plague server, added a req for util-linux.

* Sun Jan 08 2006 Karen Pease <meme@daughtersoftiresias.org> - 1.11.2-2
- Upped revision to try to get package to build on the server.

* Fri Jan 06 2006 Karen Pease <meme@daughtersoftiresias.org> - 1.11.2-1
- Upgraded the tarball to the latest version.

* Fri Dec 23 2005 Karen Pease <meme@daughtersoftiresias.org> - 1.11.1-3
- Modified the specfile to duplicate the slash'em contents into the vultures dirs before rm'ing, to fix a missing-file crash

* Wed Dec 21 2005 Karen Pease <meme@daughtersoftiresias.org> - 1.11.1-2
- Upped revision to try to get package to build on the server.

* Tue Dec 20 2005 Karen Pease <meme@daughtersoftiresias.org> - 1.11.1-1
- Upgraded source package; fixes some keyboard bugs and problems for 64bit/big endian machines concerning transparency.

* Thu Dec 15 2005 Karen Pease <meme@daughtersoftiresias.org> - 1.11.0-8
- Forgot to relocate moved docs for postbuild.

* Thu Dec 15 2005 Karen Pease <meme@daughtersoftiresias.org> - 1.11.0-7
- Apparently we're using libpng-devel now also (nobody told me)

* Thu Dec 15 2005 Karen Pease <meme@daughtersoftiresias.org> - 1.11.0-6
- SDL image devel required for build to complete properly.

* Thu Dec 15 2005 Karen Pease <meme@daughtersoftiresias.org> - 1.11.0-6
- SDL image devel required for build to complete properly.

* Thu Dec 15 2005 Karen Pease <meme@daughtersoftiresias.org> - 1.11.0-5
- That patch was fixed, but.. the folly of not checking all patches  :P

* Thu Dec 15 2005 Karen Pease <meme@daughtersoftiresias.org> - 1.11.0-4
- Once again with the patch - ah, the folly of doing diffs by hand.  Last error.

* Thu Dec 15 2005 Karen Pease <meme@daughtersoftiresias.org> - 1.11.0-3
- Didn't quite get that patch right.

* Thu Dec 15 2005 Karen Pease <meme@daughtersoftiresias.org> - 1.11.0-2
- Forgot to update the patches previously; done.

* Thu Dec 15 2005 Karen Pease <meme@daughtersoftiresias.org> - 1.11.0-1
- Upgraded the tarball to the latest release
- Upped the version
- Removed a patch that's now part of the source

* Mon Nov 21 2005 Karen Pease <meme@daughtersoftiresias.org> - 1.10.1-1
- Made it so I don't have to manually tinker with revisions between dists
- Using a 1.x release
- Removed excess tarball

* Mon Nov 21 2005 Karen Pease <meme@daughtersoftiresias.org> - 1.10.1-0.5
- Upped revision in order to make tag

* Mon Nov 21 2005 Karen Pease <meme@daughtersoftiresias.org> - 1.10.1-0.3
- Applied patch 3 (log2stderr)

* Wed Nov 16 2005 Karen Pease <meme@daughtersoftiresias.org> - 1.10.1-0.2
- Upped revision
- Removed timidity++ dep
- Fixed manual installation
- Put stderr patch back in.

* Tue Nov 15 2005 Karen Pease <meme@daughtersoftiresias.org> - 1.10.1-0.1
- Took over maintainership of package
- Handled TODOs

* Tue Nov 15 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.10.1-0.1
- 1.10.1, log crash fix applied upstream.

* Mon Nov  7 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.10.0-0.1
- First build, based on my, Karen Pease's and Luke Macken's related work.
