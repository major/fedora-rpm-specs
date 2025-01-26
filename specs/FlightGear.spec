# added temporarily due to errors in libqt5core
%define _lto_cflags %{nil}

Name:           FlightGear
Summary:        The FlightGear Flight Simulator
Version:        2020.3.19
Release:        8%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
Source0:        https://sourceforge.net/projects/flightgear/files/release-2020.3/flightgear-%{version}.tar.bz2
Patch1:         0001-check-to-be-sure-that-n-is-not-being-set-as-format-t.patch
Patch2:         0002-use-system-iaxclient-instead-of-bundled-one.patch
Patch3:         0003-desktop-use-fgfs-wrapper.patch
Patch4:         0004-fgviewer-fix-crash-on-exit.patch
Patch5:         0005-fgviewer-disconnect-the-viewer-from-the-renderer.patch
Patch6:         0006-fgviewer-use-correct-renderer-declaration.patch
Patch7:         0007-fgviewer-prevent-an-assert-on-uninitialized-locale.patch
Patch8:         0008-NasalSGPath-move-checkIORules-to-SGPath-NasalIORules.patch

URL:            http://www.flightgear.org/
BuildRequires:  openal-soft-devel, SimGear-devel >= %{version}
BuildRequires:  libpng-devel, freeglut-devel, libXi-devel, libXmu-devel
BuildRequires:  OpenSceneGraph-devel >= 3.2.0, boost-devel >= 1.44.0
BuildRequires:  fltk-fluid, fltk-devel, dbus-devel, sqlite-devel, glew-devel
BuildRequires:  cmake, desktop-file-utils, iaxclient-devel, libevent-devel
BuildRequires:  bzip2-devel, systemd-devel, qt5-qtbase-devel, libcurl-devel
BuildRequires:  qt5-qtdeclarative-devel, qt5-qtsvg-devel, qt5-linguist, xz-devel
BuildRequires:  FlightGear-data >= %{version}
Requires:       FlightGear-data >= %{version}, opengl-games-utils
Requires:       hicolor-icon-theme

%description
The Flight Gear project is working to create a sophisticated flight
simulator framework for the development and pursuit of interesting
flight simulator ideas. We are developing a solid basic sim that can be
expanded and improved upon by anyone interested in contributing

%prep
%autosetup -p1 -n flightgear-%{version}
rm -rf 3rdparty/iaxclient

# make rpmlint happy
find -name \*.h -o -name \*.cpp -o -name \*.cxx -o -name \*.hxx \
        -o -name \*.hpp |xargs chmod -x
for f in docs-mini/README.xmlparticles Thanks
do
        iconv -f iso-8859-1 -t utf-8 -o ${f}.utf8 ${f}
        mv -f ${f}.utf8 ${f}
done
sed -i 's/\r//' docs-mini/AptNavFAQ.FlightGear.html
# remove some unneeded files for the doc section
for ext in Cygwin IRIX Joystick Linux MSVC MSVC8 MacOS SimGear Unix \
        Win32-X autoconf mingw plib src xmlsyntax 
do
        rm -f docs-mini/README.${ext}
done

%build
export CXXFLAGS="-fPIC $RPM_OPT_FLAGS"
%cmake \
    -DBUILD_SHARED_LIBS:BOOL=OFF \
    -DCMAKE_BUILD_TYPE=Release \
    -DSYSTEM_SQLITE=ON \
    -DFG_DATA_DIR:PATH=%{_datadir}/flightgear \
    -DCMAKE_INSTALL_DOCDIR:PATH=%{_docdir}/%{name}

%cmake_build

%install
%cmake_install
ln -s opengl-game-wrapper.sh $RPM_BUILD_ROOT%{_bindir}/fgfs-wrapper

%files
%doc AUTHORS NEWS README Thanks docs-mini/*
%license COPYING
%{_bindir}/*
%{_mandir}/*/*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/bash-completion/completions/*
%{_datadir}/zsh/site-functions/*
%{_datadir}/metainfo/*.metainfo.xml

%changelog
* Thu Jan 23 2025 Fabrice Bellet <fabrice@bellet.info> - 2020.3.19-8
- NasalSGPath: move checkIORules() to SGPath::NasalIORulesChecker()

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2020.3.19-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 2020.3.19-6
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2020.3.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2020.3.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2020.3.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2020.3.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Oct 21 2023 Fabrice Bellet <fabrice@bellet.info> - 2020.3.19-1
- new upstream release

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2020.3.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Mar 21 2023 Fabrice Bellet <fabrice@bellet.info> - 2020.3.18-1
- new upstream release

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2020.3.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Nov 26 2022 Fabrice Bellet <fabrice@bellet.info> - 2020.3.17-1
- new upstream release

* Thu Oct 20 2022 Fabrice Bellet <fabrice@bellet.info> - 2020.3.16-1
- new upstream release
- Fix crash on METAR without cloud coverage set

* Mon Oct 03 2022 Fabrice Bellet <fabrice@bellet.info> - 2020.3.14-1
- new upstream release

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2020.3.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Mar 31 2022 Fabrice Bellet <fabrice@bellet.info> - 2020.3.13-1
- new upstream release

* Thu Feb 10 2022 Orion Poplawski <orion@nwra.com> - 2020.3.12-2
- Rebuild for glew 2.2

* Fri Feb 04 2022 Fabrice Bellet <fabrice@bellet.info> - 2020.3.12-1
- new upstream release

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2020.3.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 15 2021 Sandro Mani <manisandro@gmail.com> - 2020.3.11-2
- Rebuild (OpenSceneGraph)

* Wed Sep 01 2021 Fabrice Bellet <fabrice@bellet.info> - 2020.3.11-1
- new upstream release

* Mon Jul 26 2021 Fabrice Bellet <fabrice@bellet.info> - 2020.3.10-1
- new upstream release

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Fabrice Bellet <fabrice@bellet.info> - 2020.3.9-1
- new upstream release

* Tue Mar 30 2021 Fabrice Bellet <fabrice@bellet.info> - 2020.3.8-1
- new upstream release

* Mon Mar 22 2021 Fabrice Bellet <fabrice@bellet.info> - 2020.3.7-1
- new upstream release

* Mon Jan 25 2021 Fabrice Bellet <fabrice@bellet.info> - 2020.3.6-1
- new upstream release

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 04 2021 Fabrice Bellet <fabrice@bellet.info> - 2020.3.5-1
- new upstream release

* Wed Dec 02 2020 Fabrice Bellet <fabrice@bellet.info> - 2020.3.4-1
- new upstream release
- reenable arch s390x
- disable compositor
- add BR FlightGear-data for translation strings

* Mon Nov 30 2020 Fabrice Bellet <fabrice@bellet.info> - 2020.3.3-1
- new upstream release
- temporary exclude arch s390x

* Mon Nov 09 2020 Fabrice Bellet <fabrice@bellet.info> - 2020.3.2-1
- new upstream release
- use upstream appdata file

* Sat Oct 31 2020 Fabrice Bellet <fabrice@bellet.info> - 2020.3.1-1
- new upstream release
- enable compositor

* Sat Oct 31 2020 Fabrice Bellet <fabrice@bellet.info> - 2020.1.3-5
- temprorarily disabling LTO build due to errors in libqt5core

* Tue Oct 06 2020 Jeff Law <law@redhat.com> - 2020.1.3-4
- Force -fPIC into CXXFLAGS for QT

* Mon Jul 27 2020 Fabrice Bellet <fabrice@bellet.info> - 2020.1.3-3
- use latest cmake macros

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2020.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Fabrice Bellet <fabrice@bellet.info> - 2020.1.3-1
- new upstream release
- cmake: revert automatic translations detection

* Sat May 23 2020 Fabrice Bellet <fabrice@bellet.info> - 2020.1.2-1
- new upstream release

* Tue May 12 2020 Fabrice Bellet <fabrice@bellet.info> - 2020.1.1-1
- new upstream release

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 20 2019 Fabrice Bellet <fabrice@bellet.info> - 2019.1.1-5
- update appstream file

* Sat Oct 05 2019 Fabrice Bellet <fabrice@bellet.info> - 2019.1.1-4
- newer freeglut doesn't require a dedicated patch

* Tue Oct 1 2019 Gwyn Ciesla <gwync@protonmail.com> - 2019.1.1-3
- Rebuilt for new freeglut

* Mon Sep 30 2019 Fabrice Bellet <fabrice@bellet.info> - 2019.1.1-2
- build fix for gcc-10

* Mon Jul 29 2019 Fabrice Bellet <fabrice@bellet.info> - 2019.1.1-1
- new upstream release

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fabrice Bellet <fabrice@bellet.info> - 2018.3.2-1
- new upstream release

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 07 2018 Fabrice Bellet <fabrice@bellet.info> - 2018.3.1-1
- new upstream release

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2018.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 05 2018 Fabrice Bellet <fabrice@bellet.info> - 2018.2.2-1
- new upstream release

* Wed May 23 2018 Tom Callaway <spot@fedoraproject.org> - 2018.2.1-1
- upate to 2018.2.1

* Sun Apr 08 2018 Fabrice Bellet <fabrice@bellet.info> - 2018.1-1
- new upstream release
- make fgqmlui a static library
- fgviewer: fix crash on exit
- fgviewer: connect the viewer to the renderer

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2017.3.1-6
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2017.3.1-4
- Remove obsolete scriptlets

* Thu Dec 14 2017 Fabrice Bellet <fabrice@bellet.info> - 2017.3.1-3
- drop the local desktop file since upstream provides one

* Mon Sep 25 2017 Fabrice Bellet <fabrice@bellet.info> - 2017.3.1-2
- bump and rebuild

* Thu Sep 21 2017 Fabrice Bellet <fabrice@bellet.info> - 2017.3.1-1
- new upstream release

* Thu Sep 21 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 2017.2.1-5
- Rebuild for OSG-3.4.1.

* Thu Sep 07 2017 Fabrice Bellet <fabrice@bellet.info> - 2017.2.1-4
- fix for CVE-2017-13709

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2017.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2017.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 22 2017 Tom Callaway <spot@fedoraproject.org> - 2017.2.1-1
- update to 2017.2.1

* Mon May 15 2017 Fabrice Bellet <fabrice@bellet.info> - 2017.1.3-2
- fix for CVE-2017-8921

* Wed Apr 05 2017 Fabrice Bellet <fabrice@bellet.info> - 2017.1.3-1
- new upstream release

* Fri Mar 03 2017 Fabrice Bellet <fabrice@bellet.info> - 2017.1.2-1
- new upstream release

* Thu Feb 23 2017 Fabrice Bellet <fabrice@bellet.info> - 2017.1.1-1
- new upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2016.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 28 2017 Jonathan Wakely <jwakely@redhat.com> - 2016.4.4-2
- Rebuilt for Boost 1.63

* Fri Jan 06 2017 Fabrice Bellet <fabrice@bellet.info> - 2016.4.4-1
- new upstream release

* Wed Dec 14 2016 Fabrice Bellet <fabrice@bellet.info> - 2016.4.3-2
- Security fix: don't allow the route manager to overwrite any file

* Tue Dec 06 2016 Fabrice Bellet <fabrice@bellet.info> - 2016.4.3-1
- new upstream release

* Fri Nov 25 2016 Fabrice Bellet <fabrice@bellet.info> - 2016.4.2-1
- new upstream release

* Mon Nov 21 2016 Fabrice Bellet <fabrice@bellet.info> - 2016.4.1-1
- new upstream release

* Wed Sep 14 2016 Fabrice Bellet <fabrice@bellet.info> - 2016.3.1-2
- new upstream release

* Thu May 19 2016 Fabrice Bellet <fabrice@bellet.info> - 2016.2.1-2
- add missing BR libcurl-devel

* Thu May 19 2016 Fabrice Bellet <fabrice@bellet.info> - 2016.2.1-1
- new upstream release

* Mon May  9 2016 Tom Callaway <spot@fedoraproject.org> - 2016.1.2-1
- update to 2016.1.2

* Fri Feb 19 2016 Fabrice Bellet <fabrice@bellet.info> - 2016.1.1-1
- new upstream release

* Sun Feb 14 2016 Fabrice Bellet <fabrice@bellet.info> - 3.7.0-5.gitf4fa687
- rebuild for updated simgear

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-4.gitf4fa687
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Jonathan Wakely <jwakely@redhat.com> - 3.7.0-3.gitf4fa687
- Rebuilt for Boost 1.60

* Fri Sep 11 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.7.0-2.gitf4fa687
- Rebuild for OSG-3.4.0.

* Thu Sep 10 2015 Tom Callaway <spot@fedoraproject.org> - 3.7.0-1.gitf4fa687
- update to 3.7.0 + fixes from git

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 3.4.0-7
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Apr 19 2015 Fabrice Bellet <fabrice@bellet.info> - 3.4.0-4
- Stop using property listener for fgValidatePath
- Normalize the allowed paths as well (fix Windows breakage)

* Fri Apr 17 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.4.0-3
- Rebuild for Gcc-5.0.1 (FTBFS, RHBZ#1212707).
- Modernize spec.
- Add %%license.

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 3.4.0-2
- Add an AppData file for the software center

* Wed Mar 11 2015 Fabrice Bellet <fabrice@bellet.info> - 3.4.0-1
- new upstream release
- enable Qt Launcher

* Thu Feb 19 2015 Rex Dieter <rdieter@fedoraproject.org> 3.2.0-3
- rebuild (fltk)

* Mon Jan 26 2015 Petr Machata <pmachata@redhat.com> - 3.2.0-2
- Rebuild for boost 1.57.0

* Fri Oct 17 2014 Fabrice Bellet <fabrice@bellet.info> - 3.2.0-1
- new upstream release

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 10 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.0.0-7
- Rebuilt for OSG-3.2.1.

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 3.0.0-5
- Rebuild for boost 1.55.0

* Thu Mar 20 2014 Fabrice Bellet <fabrice@bellet.info> - 3.0.0-4
- fix the package owning the data directory

* Sun Mar 16 2014 Ville Skyttä <ville.skytta@iki.fi> - 3.0.0-3
- Use system iaxclient instead of bundled one

* Thu Feb 27 2014 Fabrice Bellet <fabrice@bellet.info> - 3.0.0-2
- forgot to update the sources file

* Fri Feb 21 2014 Fabrice Bellet <fabrice@bellet.info> - 3.0.0-1
- new upstream release

* Sun Sep 22 2013 Fabrice Bellet <fabrice@bellet.info> - 2.12.0-1
- new upstream release

* Thu Aug 15 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.10.0-8
- Rebuilt for OSG-3.2.0.

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 2.10.0-6
- Rebuild for boost 1.54.0

* Sun May 19 2013 Fabrice Bellet <fabrice@bellet.info> - 2.10.0-5
- fix another uncontrolled format string vulnerability (#958312)

* Wed Mar 13 2013 Fabrice Bellet <fabrice@bellet.info> - 2.10.0-4
- libpthread link patch is no longer needed (rh#918003)

* Tue Mar 12 2013 Jon Ciesla <limburgher@gmail.com> - 2.10.0-3
- Drop desktop vendor tag.

* Wed Mar 06 2013 Fabrice Bellet <fabrice@bellet.info> - 2.10.0-2
- add libpthread to the linker where needed

* Mon Feb 18 2013 Fabrice Bellet <fabrice@bellet.info> - 2.10.0-1
- new upstream release

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 2.8.0-3
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 2.8.0-2
- rebuild against new libjpeg

* Tue Sep 11 2012 Fabrice Bellet <fabrice@bellet.info> 2.8.0-1
- new upstream release

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 29 2012 Tom Callaway <spot@fedoraproject.org> 2.6.0-2
- check that printf format strings are never %%n (CVE-2012-2090)
- use snprintf with a max size of 256 to prevent rotor name overflow (CVE-2012-2091)

* Tue Feb 28 2012 Fabrice Bellet <fabrice@bellet.info> 2.6.0-1
- new upstream release

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-4
- Rebuilt for c++ ABI breakage

* Sat Jan 21 2012 Fabrice Bellet <fabrice@bellet.info> 2.4.0-3
- Fix gcc 4.7.0 compile issues in rawhide

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 05 2011 Fabrice Bellet <fabrice@bellet.info> 2.4.0-1
- new upstream release

* Tue Jun 14 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.0.0-6
- Rebuild against OSG-2.8.5.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 18 2010 Fabrice Bellet <fabrice@bellet.info> 2.0.0-4
- Fix a crasher in FGATC::NotifyTransmissionFinished (bz#608523)
  Upstream bug report and suggested workaround :
  http://code.google.com/p/flightgear-bugs/issues/detail?id=133

* Fri Jul 02 2010 Fabrice Bellet <fabrice@bellet.info> 2.0.0-3
- Rebuild with newer OSG

* Wed Jun 02 2010 Fabrice Bellet <fabrice@bellet.info> 2.0.0-2
- Fix a crasher when the requested visual cannot be created

* Fri Feb 26 2010 Fabrice Bellet <fabrice@bellet.info> 2.0.0-1
- New upstream release

* Sun Aug 16 2009 Fabrice Bellet <fabrice@bellet.info> 1.9.1-6
- Switch to openal-soft

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon May 11 2009 Fabrice Bellet <fabrice@bellet.info> 1.9.1-4
- Rebuilt to fix bz#498584

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 15 2009 Fabrice Bellet <fabrice@bellet.info> 1.9.1-2
- rebuild for newer OSG
- gcc44 compilation fix

* Tue Feb 03 2009 Fabrice Bellet <fabrice@bellet.info> 1.9.1-1
- new upstream release

* Tue Jan 06 2009 Fabrice Bellet <fabrice@bellet.info> 1.9.0-1
- new upstream release

* Sun Oct  5 2008 Fabrice Bellet <fabrice@bellet.info> 1.0.0-4
- fixed category of the menu entry (rh#465698)

* Tue May 13 2008 Fabrice Bellet <fabrice@bellet.info> 1.0.0-3
- rebuild with newer plib

* Sun Feb 10 2008 Fabrice Bellet <fabrice@bellet.info> 1.0.0-2
- rebuild with gcc43

* Mon Jan  7 2008 Fabrice Bellet <fabrice@bellet.info> 1.0.0-1
- new upstream release

* Tue Oct  2 2007 Fabrice Bellet <fabrice@bellet.info> 0.9.11-0.4.pre1
- use opengl-games-utils wrapper to show error dialog when DRI is missing

* Sun Sep 23 2007 Fabrice Bellet <fabrice@bellet.info> 0.9.11-0.3.pre1
- update icon cache handling to current guidelines/drafts
- update License tag

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 0.9.11-0.2.pre1
- Rebuild for selinux ppc32 issue.

* Wed Jun 27 2007 Fabrice Bellet <fabrice@bellet.info> 0.9.11-0.1.pre1
- new upstream (pre-)release

* Wed Apr 18 2007 Fabrice Bellet <fabrice@bellet.info> 0.9.10-6
- desktop-database update
- add icons from Josh Babcock

* Mon Apr 16 2007 Fabrice Bellet <fabrice@bellet.info> 0.9.10-5
- doc files cleanup
- remove -fPIC from CXXFLAGS
- add a desktop file (but no dedicated icon is available)
- spec file cleanup

* Sun Apr 08 2007 Fabrice Bellet <fabrice@bellet.info> 0.9.10-4
- disable parallel build, as it is currently broken. A typo in
  _smp_mflags macro in previous builds prevented the problem from
  showing up
- fixed duplicate BuildRequires

* Sat Apr 07 2007 Fabrice Bellet <fabrice@bellet.info> 0.9.10-3
- use sed instead of dos2unix to correct end-of-line encoding
- configure should not call automake (BZ#234826)

* Sun Apr 01 2007 Fabrice Bellet <fabrice@bellet.info> 0.9.10-2
- rebuild against new SimGear

* Tue Mar 20 2007 Fabrice Bellet <fabrice@bellet.info> 0.9.10-1
- initial packaging
