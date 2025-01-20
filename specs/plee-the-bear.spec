Name:           plee-the-bear
Version:        0.7.1
Release:        21%{?dist}
Summary:        2D platform game
# Code and artwork respectively
# Automatically converted from old format: GPLv3 and CC-BY-SA - review is highly recommended.
License:        GPL-3.0-only AND LicenseRef-Callaway-CC-BY-SA
URL:            https://github.com/j-jorge/plee-the-bear/
Source0:        https://github.com/j-jorge/plee-the-bear/archive/%{version}.tar.gz
Patch3:         ptb-docbook2man.patch
BuildRequires:  gcc-c++
BuildRequires:  bear-factory-devel
BuildRequires:  docbook-utils
BuildRequires:  boost-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libclaw-devel >= 1.7.0
BuildRequires:  SDL2_mixer-devel SDL2-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  gettext
BuildRequires:  cmake
BuildRequires:  chrpath
# Build is totally broken on ppc64
ExcludeArch:    %{power64}

%description
Plee the Bear is a 2D platform game in the spirit of 1990s console games.


%prep
%setup -q -n %{name}-%{version}
%autopatch -p1

%build
# plee the bear uses some private libs which it builds as unversioned .so files
# we put them in a private-libdir, and use a wrapper to set LD_LIBRARY_PATH
%cmake \
        -DCMAKE_BUILD_TYPE=release \
        -DPTB_LIBRARY_PATH=%{_libdir} \
        -DPTB_INSTALL_CUSTOM_LIBRARY_DIR=%{_lib} \
        -DPTB_LIBRARY_OUTPUT_PATH=%{_libdir} \
        -DPTB_DATA_DEBUG_DIRECTORY=%{_datadir}/%{name} \
        -DBEAR_ENGINE_LIBRARY_DIRECTORY=%{_libdir} \
        -DBEAR_ENGINE_INSTALL_LIBRARY_DIR=%{_lib} \
        -DBEAR_ROOT_DIRECTORY=%{_includedir}/bear-factory
%cmake_build

%install
%cmake_install

# Translations
%find_lang %{name}

# Move binary to libexec, install wrapper to set LD_LIBRARY_PATH
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}
mv $RPM_BUILD_ROOT%{_bindir}/%{name} $RPM_BUILD_ROOT%{_libexecdir}
cat > $RPM_BUILD_ROOT%{_bindir}/%{name} <<EOF
#!/bin/sh
# export LD_LIBRARY_PATH=%{_libdir}/%{name}
exec %{_libexecdir}/%{name} "$@"
EOF
chmod +x $RPM_BUILD_ROOT%{_bindir}/%{name}

# conflicts with bear
rm -rf $RPM_BUILD_ROOT%{_datadir}/bear-factory/item-description
rm -rf $RPM_BUILD_ROOT%{_datadir}/bear-factory/images
rm `find $RPM_BUILD_ROOT%{_datadir}/%{name} -name "*.sh"`
rm -rf $RPM_BUILD_ROOT%{_datadir}/pixmaps

# Menu entries
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

# Nuke the rpaths.
for i in $RPM_BUILD_ROOT%{_libdir}/*.so \
         $RPM_BUILD_ROOT%{_libexecdir}/%{name}; do
         chrpath --delete $i
done

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
BugReportURL: https://github.com/j-jorge/plee-the-bear/issues/2
SentUpstream: 2014-09-25
-->
<application>
  <id type="desktop">plee-the-bear.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Rescue your kidnapped son in this side scrolling platform game</summary>
  <description>
    <p>
      Plee the bear is a side scrolling platform game where you have to rescue your kidnapped son.
      Progress through the levels and dodge all the obstacles to try to rescue your son.
    </p>
  </description>
  <url type="homepage">http://www.stuff-o-matic.com/plee-the-bear/</url>
  <screenshots>
    <screenshot type="default">http://www.stuff-o-matic.com/plee-the-bear/assets/screenshots/large/2.png</screenshot>
  </screenshots>
</application>
EOF

%ldconfig_scriptlets

%files -f %{name}.lang
%license LICENSE license/GPL license/CCPL
%doc README.md
%{_bindir}/%{name}
%{_libdir}/lib*.so
%{_libexecdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/bear-factory/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/ptb.png
%{_mandir}/man6/%{name}.6*


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.7.1-20
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 11 2022 Hans de Goede <hdegoede@redhat.com> - 0.7.1-14
- Drop . from %%cmake invocation to fix FTBFS (rhbz#2113597)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-11
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 10 2020 Hans de Goede <hdegoede@redhat.com> - 0.7.1-9
- Fix FTBFS, straight-forward cmake macro fix (rhbz#1865235)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 15 2018 Scott Talbert <swt@techie.net> - 0.7.1-3
- Remove unneeded BR on wxGTK-devel; update bear-devel BR to bear-factory-devel

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Tom Callaway <spot@fedoraproject.org> - 0.7.1-1
- update to 0.7.1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.0-18
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 16 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.7.0-13
- set -DBEAR_ENGINE_LIBRARY_DIRECTORY=%%{_libdir} to global %%libdir
- set -DBEAR_ENGINE_INSTALL_LIBRARY_DIR=%%{_lib} to global %%lib
- set -DPTB_LIBRARY_PATH=%%{_libdir} to global %%libdir
- set -DPTB_INSTALL_CUSTOM_LIBRARY_DIR=%%{_lib} global %%lib
- set -DPTB_LIBRARY_OUTPUT_PATH=%%{_libdir} to global %%libdir
- add BR docbook-utils

* Fri Dec 23 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.7.0-12
- add ptb-CMakeLists.patch
- add ptb-sequencer-gcc6.patch
- add ptb-docbook2man.patch

* Thu Dec 22 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.7.0-11
- unbundle bear
- add BR bear-devel
- set -DBEAR_ENGINE_LIBRARY_DIRECTORY=%%{_libdir}/bear
- set -DBEAR_ENGINE_INSTALL_LIBRARY_DIR=%%{_lib}/bear
- set -DBEAR_ROOT_DIRECTORY=%%{_includedir}/bear
- delete add_subdirectory( bear ) in CMakeLists.txt
- correct CMAKE_MODULE_PATH in CMakeLists.txt
- correct BEAR_ROOT_DIRECTORY in CMakeLists.txt
- correct PTB_LIBRARY_PATH in plee-the-bear/launcher/src/CMakeLists.txt
- porting issue https://gcc.gnu.org/gcc-6/porting_to.html in 
  plee-the-bear/lib/src/ptb/item/mini-game/code/sequencer.cpp
- convert docbook2man filename taken from .sgml file to lowercase
- spec file cleanup

* Tue Dec 13 2016 Tom Callaway <spot@fedoraproject.org> - 0.7.0-10
- rebuild for new libclaw
- remove bear-factory specific files, only package plee-the-bear stuff

* Mon Nov 14 2016 Tom Callaway <spot@fedoraproject.org> - 0.7.0-9
- actually fix library handling

* Thu Nov 10 2016 Tom Callaway <spot@fedoraproject.org> - 0.7.0-8
- excludearch power64 due to build failures

* Wed Nov  9 2016 Tom Callaway <spot@fedoraproject.org> - 0.7.0-7
- fix library handling (bz1392141)

* Wed May 18 2016 Jonathan Wakely <jwakely@redhat.com> - 0.7.0-6
- Bump revision due to stuck koji task

* Tue May 17 2016 Jonathan Wakely <jwakely@redhat.com> - 0.7.0-5
- Rebuilt for linker errors in boost (#1331983)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 0.7.0-3
- Rebuilt for Boost 1.60

* Wed Dec  2 2015 Hans de Goede <hdegoede@redhat.com> - 0.7.0-2
- Fix crash on exit
- Remove the editor binaries, we really only want the game
- Put the private libs which are unversioned .so files in a private-libdir
- Drop the -devel subpackage the cmake files are for the private libs
  which have no use outside of plee-the-bear

* Mon Nov 30 2015 Tom Callaway <spot@fedoraproject.org> - 0.7.0-1
- drop -fpermissive patch
- update description
- update to 0.7.0
- drop boost patch (not needed anymore)
- make devel subpackage for cmake files

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.6.0-23
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-22
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.6.0-21
- rebuild for Boost 1.58

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.6.0-19
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.6.0-18
- Add an AppData file for the software center

* Mon Jan 26 2015 Petr Machata <pmachata@redhat.com> - 0.6.0-17
- Rebuild for boost 1.57.0

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 0.6.0-14
- Rebuild for boost 1.55.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 pmachata@redhat.com - 0.6.0-12
- Rebuild for boost 1.54.0

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.6.0-11
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.6.0-10
- Rebuild for Boost-1.53.0

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 0.6.0-9
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 0.6.0-8
- rebuild against new libjpeg

* Tue Aug 21 2012 Tom Callaway <spot@fedoraproject.org> - 0.6.0-7
- fix compile with current boost (thanks to Konstantinos Margaritis)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-5
- Rebuilt for c++ ABI breakage

* Sun Feb  5 2012 Tom Callaway <spot@fedoraproject.org> - 0.6.0-4
- rebuild against fixed libclaw

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.6.0-2
- Rebuild for new libpng

* Thu Aug 25 2011 Tom Callaway <spot@fedoraproject.org> - 0.6.0-1
- update to 0.6.0

* Mon Apr 18 2011 Tom Callaway <spot@fedoraproject.org> - 0.5.1-1
- update to 0.5.1

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Feb 06 2011 Thomas Spura <tomspur@fedoraproject.org> - 0.4.1-9
- rebuild for new boost

* Wed Sep 29 2010 jkeating - 0.4.1-8
- Rebuilt for gcc bug 634757

* Sat Sep 18 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 0.4.1-7
- fix incorrect return type

* Wed Jul 14 2010 Dan Horák <dan@danny.cz> - 0.4.1-6
- rebuilt against wxGTK-2.8.11-2

* Wed Feb 17 2010 Lubomir Rintel <lkundrak@v3.sk> - 0.4.1-5
- Fix build

* Fri Jan 22 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0.4.1-4
- Rebuild for Boost soname bump

* Sun Nov 29 2009 Lubomir Rintel <lkundrak@v3.sk> - 0.4.1-3
- Fix libdir for 64-bit archs

* Fri Sep 18 2009 Lubomir Rintel <lkundrak@v3.sk> - 0.4.1-2
- Incorporate suggestions from review (#524283#c2, Simon Wesp)
- Fix license tag
- Preserve timestamps
- Regenerate icon cache

* Fri Sep 18 2009 Lubomir Rintel <lkundrak@v3.sk> - 0.4.1-1
- Initial packaging
