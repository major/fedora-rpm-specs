%undefine __cmake_in_source_build

# trim changelog included in binary rpms
%global _changelog_trimtime %(date +%s -d "1 year ago")

Summary: Graphical user interface for Maxima
Name:    wxMaxima
Version: 24.02.1
Release: 4%{?dist}

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     https://wxmaxima-developers.github.io/wxmaxima/
Source0: https://github.com/wxMaxima-developers/wxmaxima/archive/Version-%{version}.tar.gz

## upstream patches
# none at this time

# match archs maxima uses
ExclusiveArch: %{arm} %{ix86} x86_64 aarch64 ppc sparcv9

BuildRequires: dos2unix
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: doxygen
BuildRequires: gettext
BuildRequires: GraphicsMagick
BuildRequires: libappstream-glib
BuildRequires: libxml2-devel
BuildRequires: wxGTK-devel

Provides: wxmaxima = %{version}-%{release}

Requires: jsmath-fonts
Requires: maxima >= 5.30

%description
A Graphical user interface for the computer algebra system
Maxima using wxWidgets.


%prep
%autosetup -n wxmaxima-Version-%{version} -p1

dos2unix data/io.github.wxmaxima_developers.wxMaxima.desktop
desktop-file-validate data/io.github.wxmaxima_developers.wxMaxima.desktop


%build
%cmake
%cmake_build


%install
%cmake_install

# app icon
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/{scalable,48x48,64x64,128x128}/apps/
cp -alf \
  %{buildroot}%{_datadir}/pixmaps/io.github.wxmaxima_developers.wxMaxima.svg \
  %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
cp -alf \
  %{buildroot}%{_datadir}/pixmaps/io.github.wxmaxima_developers.wxMaxima.png \
  %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/
gm convert -resize 64x64 \
  %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/io.github.wxmaxima_developers.wxMaxima.png \
  %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/io.github.wxmaxima_developers.wxMaxima.png
gm convert -resize 48x48 \
  %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/io.github.wxmaxima_developers.wxMaxima.png \
  %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/io.github.wxmaxima_developers.wxMaxima.png

# mime icons
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/mimetypes/
cp -alf  %{buildroot}%{_datadir}/pixmaps/text-x-wx*.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/mimetypes/

%find_lang wxMaxima
%find_lang wxmaxima --with-man

# Unpackaged files
rm -fv %{buildroot}%{_datadir}/wxmaxima/{COPYING,README,README.md}
rm -rfv %{buildroot}%{_datadir}/pixmaps/
rm -rfv %{buildroot}%{_datadir}/menu


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/io.github.wxmaxima_developers.wxMaxima.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/io.github.wxmaxima_developers.wxMaxima.desktop


%files -f wxMaxima.lang -f wxmaxima.lang
%doc AUTHORS.md ChangeLog NEWS.md README.md
%license COPYING
%{_bindir}/wxmaxima
%{_datadir}/wxMaxima/
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/applications/io.github.wxmaxima_developers.wxMaxima.desktop
%{_metainfodir}/io.github.wxmaxima_developers.wxMaxima.appdata.xml
%{_datadir}/bash-completion/completions/wxmaxima
%{_datadir}/mime/packages/x-wxmathml.xml
%{_datadir}/mime/packages/x-wxmaxima-batch.xml
%{_docdir}/wxmaxima/
%{_mandir}/man1/wxmaxima.1*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 24.02.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 24.02.1-3
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.02.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Feb 16 2024 José Matos <jamatos@fedoraproject.org> - 24.02.1-1
- Update to 24.02.1
- Use Markdow versions instead of simple text that are not updated anymore

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20.12.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20.12.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20.12.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 04 2022 Scott Talbert <swt@techie.net> - 20.12.1-8
- Rebuild with wxWidgets 3.2

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20.12.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20.12.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.12.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.12.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan  3 2021 José Matos <jamatos@fedoraproject.org> - 20.12.1-3
- update to 20.12.2
- patch for gcc11 is already on this release

* Tue Sep 15 2020 Jeff Law <law@redhat.com> - 20.07.0-3
- Add missing include of cstddef for gcc-11

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.07.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 José Matos <jamatos@fedoraproject.org> - 20.07.0-1
- update to 20.07.0

* Fri Jun  5 2020 José Matos <jamatos@fedoraproject.org> - 20.06.2-1
- update to 20.06.2

* Thu Jun  4 2020 José Matos <jamatos@fedoraproject.org> - 20.06.1-1
- update to 20.06.1

* Thu Jun  4 2020 José Matos <jamatos@fedoraproject.org> - 20.06.0-1
- update to 20.06.0

* Tue Jun  2 2020 José Matos <jamatos@fedoraproject.org> - 20.04.0-2
- use upstream patch to avoid crash when exporting to latex

* Mon Jun  1 2020 José Matos <jamatos@fedoraproject.org> - 20.04.0-1
- update to 20.04.0
- add the man pages in German

* Tue Mar 24 2020 José Matos <jamatos@fedoraproject.org> - 20.03.1-1
- update to 20.03.1

* Mon Feb 24 2020 José Matos <jamatos@fedoraproject.org> - 20.02.2-1
- update to 20.02.2

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.07.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19.07.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 11 2019 José Matos <jamatos@fedoraproject.org> - 19.07.0-1
- update to 19.07.0

* Fri Jun  7 2019 José Matos <jamatos@fedoraproject.org> - 19.05.7-1
- update to 19.05.7

* Sat May 11 2019 José Matos <jamatos@fedoraproject.org> - 19.05.3-1
- update to 19.05.3
- remove upstreamed patch

* Sat May  4 2019 José Matos <jamatos@fedoraproject.org> - 19.05.0-1
- update to 19.05.0
- drop upstream patches
- add patch to fix compilation (added to upstream after the release)

* Wed May  1 2019 José Matos <jamatos@fedoraproject.org> - 19.04.3-2
- Try fix to show disappearing text after the first page
  (https://github.com/wxMaxima-developers/wxmaxima/issues/1113)

* Sun Apr 28 2019 José Matos <jamatos@fedoraproject.org> - 19.04.3-1
- 19.04.3
- add upstream patch to fix bad xml appdata file

* Sat Apr 13 2019 José Matos <jamatos@fedoraproject.org> - 19.04.1-1
- 19.04.1

* Sun Mar 10 2019 José Matos <jamatos@fedoraproject.org> - 19.03.1-1
- 19.03.1
- drop patches applied upstream

* Wed Mar  6 2019 José Matos <jamatos@fedoraproject.org> - 19.03.0-1
- 19.03.0
- apply two upstream patches to fix reported bugs (#1591430 and bodhi)

* Wed Feb 27 2019 José Matos <jamatos@fedoraproject.org> - 19.02.2-1
- 19.02.2

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 29 2018 José Matos <jamatos@fedoraproject.org> - 18.12.0-1
- 18.12.0

* Mon Nov 26 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.11.4-1
- 18.11.4

* Fri Nov 09 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.10.2-1
- 18.10.2

* Fri Nov 09 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.10.1-1
- 18.10.1

* Wed Sep 26 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.10.0-1
- 18.10.0
- update URL, drop Group

* Mon Sep 24 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.02.0-1
- 18.02.0
- drop references to now-absent texinfo content
- .spec cosmetics, use %%autosetup %%make_build %%_metainfodir

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 17.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 17.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 17.10.1-2
- Remove obsolete scriptlets

* Tue Dec 19 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.10.1-1
- 17.10.1

* Sat Oct 21 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.10.0-1
- 17.10.0

* Fri Sep 22 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.05.1-1
- 17.05.1, cmake buildsys

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16.04.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16.04.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16.04.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 07 2016 Rex Dieter <rdieter@fedoraproject.org> 16.04.2-1
- 16.04.2, update archs to match maxima

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 15.08.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Sep 14 2015 Rex Dieter <rdieter@fedoraproject.org> 15.08.2-1
- 15.08.2 (#1259888)
- wxMaxima: Does not support aarch64 (#926734)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15.04.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 16 2015 Rex Dieter <rdieter@fedoraproject.org> 15.04.0-3
- uninstallation refers to files that do not exist (#1222229)

* Sat May 16 2015 Rex Dieter <rdieter@fedoraproject.org> 15.04.0-2
- invalid MIME type and no default file association (#1222224)

* Fri May 01 2015 Rex Dieter <rdieter@fedoraproject.org> 15.04.0-1
- 15.04.0

* Tue Mar 03 2015 Rex Dieter <rdieter@fedoraproject.org> 14.09.0-3
- rebuild for gcc5 (#1198392)

* Thu Oct 16 2014 Karsten Hopp <karsten@redhat.com> 14.09.0-2
- enable build on ppc64*

* Sat Oct 11 2014 Rex Dieter <rdieter@fedoraproject.org> 14.09-1
- 14.09

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.04.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.04.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Sep 27 2013 Rex Dieter <rdieter@fedoraproject.org> 13.04.2-1
- 13.04.2

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.09.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.09.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Oct 27 2012 Rex Dieter <rdieter@fedoraproject.org> 12.09.0-1
- 12.09.0

* Sat Aug 04 2012 Rex Dieter <rdieter@fedoraproject.org> 12.04.0-1
- 12.04.0

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.01.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Mar  4 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 12.01.0-1
- 12.01.0

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.08.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug 22 2011 Rex Dieter <rdieter@fedoraproject.org> 11.08.0-1
- 11.08.0

* Thu Feb 10 2011 Rex Dieter <rdieter@fedoraproject.org> 0.8.7-1
- wxMaxima-0.8.7

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Oct 26 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.8.6-1
- wxMaxima-0.8.6

* Wed Jul 14 2010 Dan Horák <dan@danny.cz> - 0.8.5-2
- rebuilt against wxGTK-2.8.11-2

* Mon May 10 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.8.5-1
- wxMaxima-0.8.5

* Sun Mar 21 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.8.4-2
- Requires: jsmath-fonts (f12+)

* Tue Dec 22 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.8.4-1
- wxMaxima-0.8.4

* Fri Nov 13 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.8.3a-1.1
- Requires: maxima >= 5.19 (#521722)

* Sun Oct 25 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.8.3a-1
- wxMaxima-0.8.3a (#530915)

* Sat Jul 18 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.8.2-3
- Requires: maxima >= 5.18

* Sat Jul 18 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.8.2-2
- output window of wxMaxima is not visible in RtL locales (#455863)

* Mon Jun 29 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.8.2-1
- wxMaxima-0.8.2

* Sat Apr 18 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.8.1-1
- wxMaxima-0.8.1

* Fri Feb 27 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.7.6-3
- ExclusiveArch: s/i386/%%ix86/

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Nov 05 2008 Rex Dieter <rdieter@fedoraproject.org> 0.7.6-1
- wxMaxima-0.7.6

* Thu Oct 02 2008 Dennis Gilmore <dennis@ausil.us> 0.7.5-2
- build sparcv9

* Tue Jun 10 2008 Rex Dieter <rdieter@fedoraproject.org> 0.7.5-1
- wxMaxima-0.7.5
- exclude ppc, f9+ (#448734)

* Mon Feb 11 2008 Rex Dieter <rdieter@fedoraproject.org> 0.7.4-3
- respin (gcc43)

* Tue Dec 11 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.7.4-2
- fix app icon handling/packaging

* Fri Dec 07 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.7.4-1
- wxMaxima-0.7.4

* Fri Nov 23 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.7.3a-1
- wxMaxima-0.7.3a

* Fri Oct 19 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.7.3-4.1
- inline plotting of wxMaxima doesn't work in f7 (#339161)

* Fri Sep 14 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.7.3-4
- wxmaxima.desktop: Categories=Development,Math

* Sat Aug 11 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.7.3-3
- License: GPLv2+
- revert to classic icon scriptlets
- respin (BuildID)

* Mon Jun 04 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.7.2-2
- +ExcludeArch, deployable only where maxima exists

* Mon Apr 09 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.7.2-1
- wxMaxima-0.7.2

* Mon Apr 09 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.7.1-3
- wxMaxima-0.7.1-old_gnuplot.patch (#235155)

* Fri Feb 23 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.7.1-2
- wxMaxima-0.7.1
- drop upstreamed patches

* Mon Dec 18 2006 Rex Dieter <rdieter[AT]fedoraproject.org> 0.7.0a-5
- use xdg-utils in scriptlets

* Wed Nov 22 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.7.0a-4
- --remove-category=Science;Utility (#215748)

* Mon Oct 09 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.7.0a-3
- (re)fix typo in %%description

* Mon Oct 09 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.7.0a-2
- patch for proper maxima= entry in ~/.wxMaxima (#209992)

* Mon Sep 25 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.7.0a-1
- 0.7.0a
- Requires: maxima >= 5.10

* Thu Sep 07 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.7.0-3
- fix %%description typo

* Tue Sep 05 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.7.0-2
- update %%description, %%summary
- rename icon -> wxmaxima.png
- omit extraneous COPYING, README
- .desktop: remove X-Red-Hat* categories

* Thu Aug 31 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.7.0-1
- 0.7.0

* Mon Aug 28 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.6.5-1
- use dfi --add-categories="Math;Science;Education"
- follow fdo icon spec
- ./configure --enable-dnd --enable-printing
- Requires: maxima
- 0.6.5

* Wed Dec 15 2004 Andrej Vodopivec <andrejv@users.sourceforge.net>
- Added french translation files.

* Wed Aug 25 2004 Andrej Vodopivec <andrejv@users.sourceforge.net>
- Initial spec file.
