Name:           enigma
Version:        1.21
Release:        24.20160222git0027b3b8e694%{?dist}
Summary:        Game where you control a marble with the mouse

License:        GPLv2+
URL:            http://www.nongnu.org/enigma/
# Using a git snapshot for the C++11 fixes.
# git clone https://github.com/Enigma-Game/Enigma.git
# cd Enigma
# git checkout 0027b3b8e694c8db75b5f8f825dada449ac2a6d1
# git archive --prefix=enigma-git0027b3b8e694/ 0027b3b8e694c8db75b5f8f825dada449ac2a6d1 | xz -9 > enigma-git0027b3b8e694.tar.xz
Source0:        enigma-git0027b3b8e694.tar.xz
#Source0:        http://downloads.sourceforge.net/enigma-game/enigma-%{version}.tar.gz
Patch1:         0001-Clean-up-.desktop-file-categories.patch
Patch2:         0002-build-use-system-zipios.patch
Patch3:         0003-prevent-ImageMagick-inserting-timestamps-to-PNGs.patch
Patch4:         0004-src-lev-Proxy.cc-fix-check-for-basic_ifstream-s-read.patch

Requires:       %{name}-data = %{version}-%{release}

# automate finding font paths at build time
%global fonts font(dejavusans)
Requires:       %{fonts}
BuildRequires:  fontconfig %{fonts}

BuildRequires:  gcc-c++
BuildRequires:  SDL-devel
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  SDL_ttf-devel
BuildRequires:  gettext
BuildRequires:  libpng-devel
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  zlib-devel
BuildRequires:  xerces-c-devel
BuildRequires:  curl-devel
BuildRequires:  ImageMagick
BuildRequires:  git
BuildRequires:  autoconf automake
BuildRequires:  zipios++-devel
BuildRequires:  pkgconfig(libenet)
BuildRequires:  texi2html
BuildRequires: make

%description
Enigma is a tribute to and a re-implementation of one of the most
original and intriguing computer games of the 1990's: Oxyd.  Your
objective is easily explained: find and uncover all pairs of identical
Oxyd stones in each landscape.  Sounds simple?  It would be, if it
weren't for hidden traps, vast mazes, insurmountable obstacles and
innumerable puzzles blocking your direct way to the Oxyd stones...

%package data
Summary:        Data for Enigma game
License:        GPLv2+
BuildArch:      noarch

%description data
Data files (levels, graphics, sound, music) and documentation for Enigma.

%prep
%autosetup -S git_am -n enigma-git0027b3b8e694
rm -r lib-src/zipios++ lib-src/enet/*

%build
aclocal -I m4 && autoheader && automake --add-missing --foreign --copy && autoconf
%configure --enable-optimize --with-system-enet
make %{?_smp_mflags}

%install
%make_install

# Use system fonts instead of bundling our own
ln -f -s $(fc-match -f "%{file}" "dejavusans:condensed") \
        $RPM_BUILD_ROOT%{_datadir}/%{name}/fonts/DejaVuSansCondensed.ttf
ln -f -s $(fc-match -f "%{file}" "dejavusans") \

desktop-file-install \
  --remove-key Version \
  --dir ${RPM_BUILD_ROOT}%{_datadir}/applications            \
  $RPM_BUILD_ROOT%{_datadir}/applications/enigma.desktop

appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/appdata/enigma.appdata.xml

%find_lang %{name}

%files
%{_bindir}/enigma
%{_mandir}/man?/enigma.*
%{_datadir}/icons/hicolor/48x48/apps/enigma.png
%{_datadir}/pixmaps/enigma.png
%{_datadir}/applications/enigma.desktop
%{_datadir}/appdata/enigma.appdata.xml

%files data -f %{name}.lang
%{_pkgdocdir}
%{_datadir}/enigma

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-24.20160222git0027b3b8e694
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-23.20160222git0027b3b8e694
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-22.20160222git0027b3b8e694
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-21.20160222git0027b3b8e694
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-20.20160222git0027b3b8e694
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-19.20160222git0027b3b8e694
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 14 2020 Bruno Wolff III <bruno@wolff.to> - 1.21-18.20160222git0027b3b8e694
- Automate finding font paths at build time

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-17.20160222git0027b3b8e694
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-16.20160222git0027b3b8e694
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-15.20160222git0027b3b8e694
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-14.20160222git0027b3b8e694
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-13.20160222git0027b3b8e694
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.21-12.20160222git0027b3b8e694
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-11.20160222git0027b3b8e694
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-10.20160222git0027b3b8e694
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.21-9.20160222git0027b3b8e694
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-8.20160222git0027b3b8e694
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Feb 22 2016 Michal Schmidt <mschmidt@redhat.com> 1.21-7.20160222git0027b3b8e694
- Update to current git snapshot.
- Fix FTBFS.
- BuildRequires: texi2html
- Drop Group tag.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 03 2015 Kalev Lember <kalevlember@gmail.com> - 1.21-4
- Rebuilt for GCC 5 C++11 ABI change

* Tue Jan 06 2015 Michal Schmidt <mschmidt@redhat.com> - 1.21-3
- Avoid inserting timestamps into converted PNGs in doc.
- Split data files into enigma-data.noarch.

* Tue Jan 06 2015 Michal Schmidt <mschmidt@redhat.com> - 1.21-2
- Build against system enet library.

* Mon Jan 05 2015 Michal Schmidt <mschmidt@redhat.com> - 1.21-1
- Upstream release 1.21.
- Use autosetup git_am.
- Ship appstream file.
- Don't shuffle doc files via __doc/.
- Don't BuildRequire tetex.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 18 2014 Michal Schmidt <mschmidt@redhat.com> - 1.20-1
- Update to 1.20 release.
- Remove bundled zipios++ (#1077702, based on patch from Ville Skyttä)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 04 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 1.01-23
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- replace file requires with package requires for dejavu sans fonts
- use make_install macro
- drop obsolete version requirements for build dependencies
- update gtk icon cache scriplets to follow current guidelines
- drop defattr

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jul 30 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 1.01-21
- Add dist tag as required by package guidelines

* Fri Jul 27 2012 Michal Schmidt <mschmidt@redhat.com> - 1.01-20
- Fix FTBFS. Patches provided by Tom Lane (#843643).
- Remove legacy spec file items.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-18
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.01-16
- Rebuild for new libpng

* Thu Mar 10 2011 Kalev Lember <kalev@smartlink.ee> - 1.01-15
- Added a patch to fix build with GCC 4.6

* Thu Mar 10 2011 Kalev Lember <kalev@smartlink.ee> - 1.01-14
- Rebuilt with xerces-c 3.1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Feb 09 2010 Caolán McNamara <caolanm@redhat.com> - 1.01-12
- Rebuild for libxerces-c

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar 02 2009 Caolán McNamara <caolanm@redhat.com> - 1.01-10
- fix up consts

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-9.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 04 2009 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 1.01-8
- add enigma-gcc-4.4-ftbfs.patch from debian

* Mon Dec 29 2008 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 1.01-7
- use file-based deps for fons
- use DejaVuSans instead of vera_sans

* Wed Dec 24 2008 Wart <wart@kobold.org> - 1.01-6.3
- Replace bundled font with a symlink to an identical system font (BZ #477381)

* Mon Feb 11 2008 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 1.01-6.2
- rebuild for new libxerces-c

* Sat Feb 09 2008 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 1.01-6
- update gcc43 patch to one from opensuse

* Sat Feb 09 2008 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 1.01-5
- rebuilt

* Fri Jan 04 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 1.01-4.1
- add enigma-gcc-4.3-ftbfs.patch from debian package

* Wed Sep 12 2007 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 1.01-3.1
- use the newly 64bit-clean upstream tarball

* Tue Aug 21 2007 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 1.01-2.1
- Remove version key from desktop file

* Fri Aug 03 2007 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info>
- Update License field due to the "Licensing guidelines changes"

* Tue Jun 5 2007 Wart <wart@kobold.org> - 1.01-2
- Clean up desktop categories

* Sat May 26 2007 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 1.01-1
- Update to 1.01

* Thu Dec 14 2006 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 1.0-1
- Update to 1.0
- drop enigma-gcc41.patch
- formating changes
- use make install DESTDIR
- new download URL

* Mon Aug 28 2006 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 0.92-4
- Rebuild for Fedora Extras 6

* Mon Feb 13 2006 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 0.92-3
- Rebuild for Fedora Extras 5

* Mon Jan 23 2006 Adrian Reber <adrian@lisas.de> - 0.92-2
- Added patch to build with gcc 4.1

* Sat May 07 2005 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 0.92-1
- Update to 0.92
- Use disttag

* Sat May 07 2005 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 0.91-5
- rebuilt

* Sat May 07 2005 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 0.91-3
- BR libpng-devel

* Thu May 05 2005 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 0.91-2
- rebuilt

* Thu May 05 2005 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 0.91-1
- Update to 0.91
- Add BR gettext, SDL_ttf-devel
- Use find_lang
- gtk-update-icon-cache in post and postun
- Remove GCC patches

* Thu Apr 14 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.81-5
- Fix build for GCC4.

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Thu Nov 11 2004 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.81-3
- Fix a number of C++ issues for FC3/GCC 3.4.

* Fri Jun 11 2004 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 0:0.81-0.fdr.2
- Build-Require zlib-devel, tetex
- Don't install INSTALL

* Wed Dec 24 2003 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 0:0.81-0.fdr.1
- Initial RPM release based on spec-file in source
  package by Daniel Heck <dheck[AT]gmx.de>
