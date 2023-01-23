Name:           scribus
Version:        1.5.8
Release:        8%{?dist}
Summary:        Desktop Publishing application written in Qt
# swatches bring in the fun licenses
License:        GPLv2+ and OGL and CC0 and CC-BY and CC-BY-SA and Public Domain and ASL 2.0 and LGPLv2+ 
URL:            http://www.scribus.net/

# svn export svn://scribus.net/trunk/Scribus scribus-%%{version}
# tar --exclude-vcs -cJf scribus-%%{version}.tar.xz scribus-%%{version}
## The following script removes non free contents
# ./make-free-archive %%{version}
Source0:        %{name}-%{version}-free.tar.xz
#Source0:        http://downloads.sourceforge.net/%%{name}/%%{name}-%%{version}.tar.xz
#Source1:        http://downloads.sourceforge.net/%%{name}/%%{name}-%%{version}.tar.xz.asc

Patch0:         scribus-1.5.8-poppler-22.08.0.patch

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  cups-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  ghostscript
BuildRequires:  hyphen-devel
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(GraphicsMagick)
BuildRequires:  pkgconfig(GraphicsMagick++)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(hunspell)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libcdr-0.1)
BuildRequires:  pkgconfig(libfreehand-0.1)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libmspub-0.1)
BuildRequires:  pkgconfig(libpagemaker-0.0)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libpodofo)
BuildRequires:  pkgconfig(libqxp-0.0)
BuildRequires:  pkgconfig(librevenge-0.0)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libvisio-0.1)
BuildRequires:  pkgconfig(libwpd-0.10)
BuildRequires:  pkgconfig(libwpg-0.3)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libzmf-0.0)
BuildRequires:  pkgconfig(openscenegraph)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(poppler)
BuildRequires:  pkgconfig(poppler-cpp)
BuildRequires:  pkgconfig(poppler-data)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(Qt5) > 5.14
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5UiTools)
BuildRequires:  pkgconfig(Qt5WebKit)
BuildRequires:  pkgconfig(tk)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3dist(pillow)
BuildRequires:  python3-qt5-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3-tkinter


%filter_provides_in %{_libdir}/%{name}/plugins
%filter_setup


%description
Scribus is an desktop open source page layout program with
the aim of producing commercial grade output in PDF and
Postscript, primarily, though not exclusively for Linux.

While the goals of the program are for ease of use and simple easy to
understand tools, Scribus offers support for professional publishing
features, such as CMYK color, easy PDF creation, Encapsulated Postscript
import/export and creation of color separations.


%prep
%autosetup -p1

# fix permissions
chmod a-x scribus/pageitem_latexframe.h

# drop shebang lines from python scripts
%py3_shebang_fix %{name}/plugins/scriptplugin/{samples,scripts}/*.py

%build
%cmake  \
        -DCMAKE_CXX_STANDARD=17 \
        -DWANT_CPP17=ON \
        -DWANT_CCACHE=YES \
        -DWANT_DISTROBUILD=YES \
        -DWANT_GRAPHICSMAGICK=1 \
        -DWANT_HUNSPELL=1 \
%if "%{_lib}" == "lib64"
        -DWANT_LIB64=YES \
%endif
        -DWANT_NORPATH=1 \
        -DWITH_BOOST=1 \
        -DWITH_PODOFO=1
%cmake_build

%install
%cmake_install

find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet \
        %{buildroot}%{_metainfodir}/%{name}.appdata.xml


%files
%license COPYING
%doc AUTHORS ChangeLog COPYING README LINKS TRANSLATION
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_metainfodir}/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
%{_datadir}/icons/hicolor/512x512/apps/%{name}.png
%{_datadir}/icons/hicolor/1024x1024/apps/%{name}.png
%{_datadir}/%{name}/
%{_mandir}/man1/*
%{_mandir}/pl/man1/*
%{_mandir}/de/man1/*


%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 31 2022 Pete Walter <pwalter@fedoraproject.org> - 1.5.8-7
- Rebuild for ICU 72

* Mon Aug 08 2022 Marek Kasik <mkasik@redhat.com> - 1.5.8-6
- Rebuild for poppler-22.08.0
- Backport necessary changes from upstream

* Mon Aug 01 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.5.8-5
- Rebuilt for ICU 71.1

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.5.8-3
- Rebuilt for Python 3.11

* Tue May 03 2022 Sandro Mani <manisandro@gmail.com> - 1.5.8-2
- Rebuild (podofo)

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.8-1
- Update to 1.5.8

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 18 2022 Marek Kasik <mkasik@redhat.com> - 1.5.7-8
- Rebuild for poppler-22.01.0
- Switch to C++17 because it is needed by poppler now

* Mon Nov 15 2021 Sandro Mani <manisandro@gmail.com> - 1.5.7-7
- Rebuild (OpenSceneGraph)

* Tue Sep 21 2021 Parag Nemade <pnemade@fedoraproject.org> - 1.5.7-6
- Fix undefined symbol: hb_subset_input_set_name_legacy (rhbz#2006220)

* Thu Aug 05 2021 Marek Kasik <mkasik@redhat.com> - 1.5.7-5
- Rebuild for poppler-21.08.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.5.7-3
- Rebuilt for Python 3.10

* Thu May 20 2021 Pete Walter <pwalter@fedoraproject.org> - 1.5.7-2
- Rebuild for ICU 69

* Wed May 12 2021 Luya Tshimbalanga <luya@fedoraproject.org> - 1.5.7-1
- Update to 1.5.7
- Drop patch for podofo 0.9.7 fixed upstream

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 19 2021 Marek Kasik <mkasik@redhat.com> - 1.5.6.1-5
- Rebuild for poppler-21.01.0 with correct target

* Tue Jan 19 2021 Marek Kasik <mkasik@redhat.com> - 1.5.6.1-4
- Rebuild for poppler-21.01.0

* Sun Jan 10 16:35:55 CET 2021 Sandro Mani <manisandro@gmail.com> - 1.5.6.1-3
- Rebuild (podofo)

* Sat Jan  9 22:58:15 CET 2021 Sandro Mani <manisandro@gmail.com> - 1.5.6.1-2
- Rebuild (podofo)

* Tue Dec 01 2020 Luya Tshimbalanga <luya@fedoraproject.org> - 1.5.6.1-1
- Update to 1.5.6.1
- Use c++17

* Tue Nov 03 2020 Luya Tshimbalanga <luya@fedoraproject.org> - 1.5.6-0.14
- Further implement pkgconfig for build requirement
- Use python3dist macro for some build requirement

* Mon Oct 05 2020 Than Ngo <than@redhat.com> - 1.5.6-0.13
- add BR on python3-setuptools explicitly

* Fri Aug 21 2020 Jeff law <law@redhat.com> - 1.5.6-0.12
- Fix static ctor initialization issue by removing the unused static
  data member
  Re-enable LTO

* Fri Aug 21 2020 Dan Horák <dan[at]danny.cz> - 1.5.6-0.11
- build with LTO disabled (#1866207)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.6-0.10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 2020 Dan Horák <dan[at]danny.cz> - 1.5.6-0.9
- Update for https://fedoraproject.org/wiki/Changes/CMake_to_do_out-of-source_builds
- Rebuild for poppler-0.90.0

* Wed Jun 03 2020 Charalampos Stratakis <cstratak@redhat.com> - 1.5.6-0.8
- Remove dependency on the retired qt5-devel metapackage (#1840633)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5.6-0.7
- Rebuilt for Python 3.9

* Thu Apr 02 2020 Björn Esser <besser82@fedoraproject.org> - 1.5.6-0.6
- Fix string quoting for rpm >= 4.16

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.6-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Marek Kasik <mkasik@redhat.com> - 1.5.6-0.4
- Rebuild for poppler-0.84.0

* Tue Nov 05 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 1.5.6-0.3
- Update to 1.5.6 pre-release (svn 23333)

* Fri Nov 01 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 1.5.6-0.2
- Update to 1.5.6 pre-release (svn r23311)
- Improve make-free-archives script
- Revamp spec file for adherence to Fedora Packaging Guideline
- Drop source high quality icon 
- Drop obsolete patches

* Wed Oct 30 2019 François Cami <fcami@fedoraproject.org> - 1.5.6-0.1
- Ship 1.5.6 pre-release (svn r23306) to switch to Python3

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 13 2018 Caolán McNamara <caolanm@redhat.com> - 1.4.6-15
- rebuild for hunspell-1.7.0

* Mon Sep 17 2018 Michael J Gruber <mjg@fedoraproject.org> - 1.4.6-14
- fix EPS import (bz #1628943)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Sandro Mani <manisandro@gmail.com> - 1.4.6-12
- Rebuild (podofo)

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.4.6-11
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.4.6-7
- Rebuild due to bug in RPM (RHBZ #1468476)

* Fri Apr 07 2017 Yaakov Selkowitz <yselkowi@redhat.com> - 1.4.6-6
- Fix detection of latest hunspell for spell-checking support (#1425305)

* Mon Feb 06 2017 Kalev Lember <klember@redhat.com> - 1.4.6-5
- Rebuilt for Boost 1.63

* Thu Feb 02 2017 Sandro Mani <manisandro@gmail.com> - 1.4.6-4
- Rebuild (podofo)

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 1.4.6-3
- Rebuilt for Boost 1.63

* Fri Sep 23 2016 Jon Ciesla <limburgher@gmail.com> - 1.4.6-2
- podofo rebuild.

* Tue May 24 2016 Jon Ciesla <limburgher@gmail.com> - 1.4.6-1
- 1.4.6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 1.4.5-8
- Rebuilt for Boost 1.60

* Tue Jan 12 2016 Tom Callaway <spot@fedoraproject.org> - 1.4.5-7
- fix license tag, remove found non-free swatches (bz 1297262)

* Fri Sep 18 2015 Richard Hughes <rhughes@redhat.com> - 1.4.5-6
- Use a bigger resolution application icon

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 1.4.5-5
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.4.5-3
- rebuild for Boost 1.58

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May  7 2015 Tom Callaway <spot@fedoraproject.org> 1.4.5-1
- update to 1.4.5
- drop non-free and questionable hyphen dic files (bz 1219415)
- fix necessary LPPL attributions

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1.4.4-7
- Add an AppData file for the software center

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 1.4.4-6
- Rebuild for boost 1.57.0

* Thu Aug 28 2014 Dan Horák <dan[at]danny.cz> - 1.4.4-5
- switch to Debian patch for the qreal vs double conflict on ARM (fixes #1076885)

* Wed Aug 20 2014 Kevin Fenzi <kevin@scrye.com> - 1.4.4-4
- Rebuild for rpm bug 1131892

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Aug 09 2014 Rex Dieter <rdieter@fedoraproject.org> 1.4.4-2
- optimize/update scriptlets

* Fri Jun  6 2014 Tom Callaway <spot@fedoraproject.org> - 1.4.4-1
- update to 1.4.4, drop non-free dot files

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 1.4.3-3
- Rebuild for boost 1.55.0

* Thu Sep 19 2013 Dan Horák <dan[at]danny.cz> - 1.4.3-2
- fix the double patch (#1009979)

* Mon Aug 19 2013 Dan Horák <dan[at]danny.cz> - 1.4.3-1
- update to 1.4.3 (#990030)
- update for unversioned docdir

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 1.4.2-6
- Rebuild for boost 1.54.0

* Mon Feb 25 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 1.4.2-5
- Remove --vendor from desktop-file-install for F19+ https://fedorahosted.org/fesco/ticket/1077

* Wed Jan 30 2013 Dan Horák <dan[at]danny.cz> - 1.4.2-4
- update for Pillow (#896301)

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 1.4.2-3
- rebuild due to "jpeg8-ABI" feature drop

* Fri Jan 18 2013 Dan Horák <dan[at]danny.cz> - 1.4.2-2
- use hunspell to be consistent with the rest of the system

* Tue Jan 15 2013 Dan Horák <dan[at]danny.cz> - 1.4.2-1
- update to 1.4.2
- remove non-free content from source archive (#887221)
- drop doc and devel sub-packages
- switch to lcms2

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 1.4.1-4
- rebuild against new libjpeg

* Thu Aug  9 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 1.4.1-3
- Add patch to fix FTBFS on ARM

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun May 06 2012 Dan Horák <dan[at]danny.cz> - 1.4.1-1
- update to 1.4.1

* Wed Mar 07 2012 Dan Horák <dan[at]danny.cz> - 1.4.0-5
- fix crash at export as image (rhbz#800765)

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-4
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jan 03 2012 Dan Horák <dan[at]danny.cz> - 1.4.0-2
- the swatches/profiles patches were submitted to upstream bugtracker

* Mon Jan 02 2012 Dan Horák <dan[at]danny.cz> - 1.4.0-1.1
- install profiles and swatches to datadir
- use versioned docdir

* Mon Jan 02 2012 Dan Horák <dan[at]danny.cz> - 1.4.0-1
- update to 1.4.0

* Fri Jun 24 2011 Dan Horák <dan@danny.cz> - 1.3.9-6
- fix build with cups 1.5 (#716107)

* Wed May 04 2011 Dan Horák <dan@danny.cz> - 1.3.9-5
- rebuilt against podofo 0.9.1

* Thu Apr 14 2011 Dan Horák <dan@danny.cz> - 1.3.9-4
- rebuilt against podofo 0.9.0

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Dan Horák <dan[AT]danny.cz> - 1.3.9-2
- run update-desktop-database in scriptlets too (#664318)

* Tue Nov 30 2010 Dan Horák <dan[AT]danny.cz> - 1.3.9-1
- update to 1.3.9
- filter unwanted Provides

* Wed Nov 03 2010 Dan Horák <dan@danny.cz> - 1.3.8-3
- rebuilt against podofo 0.8.4

* Fri Oct 22 2010 Dan Horák <dan@danny.cz> - 1.3.8-2
- rebuilt against podofo 0.8.3

* Mon Aug 16 2010 Dan Horák <dan[AT]danny.cz> - 1.3.8-1
- update to 1.3.8

* Tue Jul 27 2010 David Malcolm <dmalcolm@redhat.com> - 1.3.7-5
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Jun 15 2010 Dan Horák <dan[AT]danny.cz> - 1.3.7-4
- fix crash when selecting frame (#604124)

* Tue Jun 15 2010 Dan Horák <dan[AT]danny.cz> - 1.3.7-3
- show icons in shapes menu (#603921)

* Tue Jun 08 2010 Dan Horák <dan[AT]danny.cz> - 1.3.7-2
- rebuilt with podofo 0.8.1

* Tue Jun  1 2010 Dan Horák <dan[AT]danny.cz> - 1.3.7-1
- update to final 1.3.7

* Thu Apr 29 2010 Dan Horák <dan[AT]danny.cz> - 1.3.6-4
- fix build with podofo 0.8.0

* Thu Apr 29 2010 Dan Horák <dan[AT]danny.cz> - 1.3.6-3
- rebuilt for podofo 0.8.0

* Wed Mar 31 2010 Dan Horák <dan[AT]danny.cz> - 1.3.6-2
- added 2 patches for rawhide

* Mon Mar 29 2010 Dan Horák <dan[AT]danny.cz> - 1.3.6-1
- update to final 1.3.6

* Wed Nov 25 2009 Dan Horák <dan[AT]danny.cz> - 1.3.5.1-5
- fixed a crash when closing a hyphenator object (#537677)

* Thu Aug 27 2009 Tomas Mraz <tmraz@redhat.com> - 1.3.5.1-4
- rebuilt with new openssl

* Tue Aug 25 2009 Dan Horák <dan[AT]danny.cz> - 1.3.5.1-3
- drop shebang line from python scripts
- don't package precompiled python scripts

* Thu Aug 20 2009 Dan Horák <dan[AT]danny.cz> - 1.3.5.1-1
- update to final 1.3.5.1
- drop the upstreamed "install-headers" patch
- always install doc subpackage (#446148)
- full changelog: http://www.scribus.net/?q=node/193

* Wed Jul 29 2009 Dan Horák <dan[AT]danny.cz> - 1.3.5-0.17.rc3
- don't use parallel build on s390x

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5-0.16.rc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 21 2009 Dan Horák <dan[AT]danny.cz> - 1.3.5-0.15.rc3
- update to 1.3.5-rc3
- use system hyphen library (#506074)
- fix update path for the doc subpackage (#512498)
- preserve directories when installing headers (#511800)

* Thu Jun  4 2009 Dan Horák <dan[AT]danny.cz> - 1.3.5-0.14.rc2
- update to 1.3.5-rc2

* Mon May 18 2009 Dan Horák <dan[AT]danny.cz> - 1.3.5-0.13.beta
- rebuilt with podofo enabled

* Wed Apr 22 2009 Dan Horák <dan[AT]danny.cz> - 1.3.5-0.12.beta
- update to 1.3.5.beta
- make docs subpackage noarch
- drop outdated Obsoletes/Provides

* Sun Mar 29 2009 Dan Horák <dan[AT]danny.cz> - 1.3.5-0.11.20090329svn13359
- update to revision 13359
- add aspell-devel and boost-devel as BR
- update release tag to conform to the pre-release versioning guideline

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5-0.10.12516svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 17 2009 Tomas Mraz <tmraz@redhat.com> - 1.3.4-0.9.12516svn
- rebuild with new openssl

* Thu Dec 04 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.3.5-0.8.12516svn
- Rebuild for Python 2.6

* Tue Dec  2 2008 Dan Horák <dan[AT]danny.cz> - 1.3.5-0.7.12516svn
- fix directory ownership in doc subpackage (#474041)

* Sun Nov 30 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.3.5-0.6.12516svn
- Rebuild for Python 2.6

* Mon Oct 13 2008 Dan Horák <dan[AT]danny.cz> 1.3.5-0.5.12516svn
- install global desktop file instead of KDE-only one (#461124)
- little cleanup

* Fri Sep 05 2008 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 1.3.5-0.4.12516svn
- new svn snapshot

* Sun Jul 27 2008 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 1.3.5-0.3.12419svn
- new svn snapshot

* Mon Jul 21 2008 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 1.3.5-0.2.12404svn
- svn snapshot

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.3.4-5
- Autorebuild for GCC 4.3

* Mon Feb 11 2008 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de> - 1.3.4-4
- Rebuilt for gcc43

* Fri Dec 28 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 1.3.4-3
- fix inclusion of python scripts as proposed by Todd Zullinger (#312091)
- fix desktop file

* Thu Aug 23 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 1.3.4-2
- rebuild for buildid
- new license tag

* Sat Jun 02 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.3.4
- version upgrade

* Mon Dec 04 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.3.3.6-1
- version upgrade

* Sat Nov 11 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.3.3.5-1
- version upgrade

* Wed Oct 04 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.3.3.4-1
- version upgrade

* Fri Sep 15 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.3.3.3-1
- version upgrade (#205962)

* Sun Jun 18 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.3.3.2-2
- bump

* Tue May 30 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.3.3.2-1
- version upgrade

* Sat Apr 22 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.3.3.1-1
- version upgrade

* Tue Mar 28 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.3.3-1
- version upgrade
- add BR gnutls-devel

* Sat Mar 18 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.3.2-1
- upgrade to beta version

* Thu Feb 16 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.2.4.1-4
- Rebuild for Fedora Extras 5

* Wed Feb 08 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.2.4.1-3
- add missing requires python-imaging

* Sat Jan 21 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.2.4.1-2
- rebuild (#178494)

* Wed Jan 18 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.2.4.1-1
- version upgrade

* Thu Jul 7 2005 Tom "spot" Callaway <tcallawa@redhat.com> 1.2.2.1-2
- use dist tag for sanity between branches

* Tue Jul 5 2005 P Linnell <mrdocs AT scribus.info> - 1.2.2.1-1
- 1.2.2.1 released to fix crash on open with certain 1.2.1 docs

* Sun Jul 3 2005 P Linnell <mrdocs AT scribus.info> - 1.2.2-0.fc4
- 1.2.2 final

* Tue Jun 28 2005 P Linnell <mrdocs AT scribus.info>- 1.2.2cvs-0
- test build for 1.2.2cvs
- Add freetype2 explicit build requirement
- Add obsoletes. See PACKAGING in the source tarball
- Change the description per PACKAGING
- Bump required python. 2.2 is no longer supported.


* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 1.2.1-5
- rebuild on all arches

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Sun Feb 06 2005 Phillip Compton <pcompton[AT]proteinmedia.com> - 1.2.1-3
- Bumped BR on qt-devel to 3.3.

* Thu Feb  3 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.2.1-2
- Fix x86_64 build and summary.

* Sun Jan 09 2005 Phillip Compton <pcompton[AT]proteinmedia.com> - 1.2.1-1
- 1.2.1.

* Sat Dec 04 2004 Phillip Compton <pcompton[AT]proteinmedia.com> - 1.2.1-0.1.cvs20041118
- cvs snapshot.

* Wed Nov 11 2004 Phillip Compton <pcompton[AT]proteinmedia.com> - 1.2-0.fdr.3
- Redirect output in post/postun, to avoid failure.

* Wed Nov 10 2004 Phillip Compton <pcompton[AT]proteinmedia.com> - 1.2-0.fdr.2
- Mime-type corrections for FC3.
- Dropped redundent BR XFree86-devel.

* Thu Aug 26 2004 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:1.2-0.fdr.1
- 1.2.
- Dropping old obsoletes/provides (don't know of anyone using them).

* Thu Aug 19 2004 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:1.2-0.fdr.0.RC1
- 1.2RC1.

* Sat Aug 07 2004 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:1.1.7-0.fdr.4
- mime info/icon for .sla files.

* Fri Jul 10 2004 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:1.1.7-0.fdr.3
- BuildReq openssl-devel (#1727).

* Thu Jun 10 2004 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:1.1.7-0.fdr.2
- Source0 allows direct download (#1727).
- Req tkinter (#1727).

* Sun Jun 06 2004 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:1.1.7-0.fdr.1
- Updated to 1.1.7.
- Re-added _smp_mflags.

* Mon May 24 2004 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:1.1.6-0.fdr.3
- Add Application Category to desktop entry.

* Sun Apr 11 2004 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:1.1.6-0.fdr.2
- Bump ghostscript Req to 7.07.
- URL scribus.net.

* Tue Apr 06 2004 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:1.1.6-0.fdr.1
- Updated to 1.1.6.
- Using upstream desktop entry.

* Sat Feb 14 2004 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:1.1.5-0.fdr.1
- Updated to 1.1.5.

* Sun Dec 21 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:1.1.4-0.fdr.1
- Updated to 1.1.4.

* Thu Dec 04 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:1.1.3-0.fdr.2
- Dropped LDFLAGS="-lm"
- Added --with-pythondir=%%{_prefix}
- Req ghostscript.

* Sun Nov 30 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:1.1.3-0.fdr.1
- Updated to 1.1.3.
- Removed _smp_mflags.

* Tue Nov 18 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:1.1.2-0.fdr.2
- Req python.
- Provides scribus-scripting.

* Sun Nov 09 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:1.1.2-0.fdr.1
- Updated to 1.1.2.
- Obsoletes scribus-scripting.

* Sat Oct 11 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:1.1.1-0.fdr.2
- BuildReq littlecms-devel -> lcms-devel.

* Thu Oct 09 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:1.1.1-0.fdr.1
- Updated to 1.1.1.
- BuildReq littlecms-devel.
- BuildReq libart_lgpl-devel.

* Wed Sep 10 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:1.0.1-0.fdr.1
- Updated to 1.0.1.
- Split off devel package for headers.
- No longer Obsoletes scribus-i18n-en

* Thu Jul 24 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:1.0-0.fdr.3
- desktop entry terminal=0 -> false.

* Tue Jul 15 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:1.0-0.fdr.2
- Added Obsoletes scribus-i18n-en.

* Tue Jul 15 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:1.0-0.fdr.1
- Updated to 1.0.

* Tue Jul 01 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:1.0-0.fdr.0.1.rc1
- Updated to 1.0RC1.

* Fri Jun 20 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.9.11.1-0.fdr.1
- Updated to 0.9.11.1.
- Added obsoletes scribus-svg.

* Sun May 25 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.9.10-0.fdr.3
- Using make DESTDIR= workaround for plugin issue.
- Removed post/postun ldconfig.
- Removed devel subpackage.

* Mon May 19 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.9.10-0.fdr.2
- Explicitly set file permission on icon.
- Created devel package.
- Removed .la files.
- Added ChangeLog to Documentation.

* Sun May 18 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.9.10-0.fdr.1
- Updated to 0.9.10.
- buildroot -> RPM_BUILD_ROOT.

* Sat Apr 26 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.9.9-0.fdr.3
- Added BuildRequires for cups-devel.

* Thu Apr 24 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.9.9-0.fdr.2
- Added BuildRequires for libtiff-devel.
- Added line to help package find tiff.

* Sun Apr 20 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.9.9-0.fdr.1
- Updated to 0.9.9.
- Added line for QT.

* Thu Apr 10 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.9.8-0.fdr.3.rh90
- Added missing BuildRequires.
- Corrected Group.

* Tue Apr 01 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.9.8-0.fdr.2
- Added desktop-file-utils to BuildRequires.
- Changed category to X-Fedora-Extra.
- Added Epoch:0.

* Thu Mar 27 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0.9.8-0.fdr.1
- Initial RPM release.
