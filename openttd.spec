# If we have a prerelease version we can define it here
#%%global prever RC1

Name:           openttd
Version:        13.0
Release:        1%{?prever:.%{prever}}%{?dist}
Summary:        Transport system simulation game

License:        GPLv2+
URL:            https://www.openttd.org
Source0:        https://cdn.openttd.org/openttd-releases/%{version}%{?prever:-%{prever}}/%{name}-%{version}%{?prever:-%{prever}}-source.tar.xz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  fontconfig-devel
BuildRequires:  fluidsynth-devel
BuildRequires:  freetype-devel
BuildRequires:  gcc-c++
BuildRequires:  libicu-devel
BuildRequires:  libpng-devel
BuildRequires:  lzo-devel
BuildRequires:  SDL2-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel

Requires:       hicolor-icon-theme

Recommends:     openttd-opengfx => 0.5.0
Recommends:     fluid-soundfont-gm

%description
OpenTTD is modeled after a popular transportation business simulation game
by Chris Sawyer and enhances the game experience dramatically. Many features
were inspired by TTDPatch while others are original.


%package docs
Summary:        Documentation for OpenTTD
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description docs
Development documentation for OpenTTD. Includes information on how to program
the AI.


%prep
%autosetup -p1 -n %{name}-%{version}%{?prever:-%{prever}}

sed -i "s|/usr/share|%{_datadir}|g" src/music/fluidsynth.cpp

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_BINDIR=bin \
    -DCMAKE_INSTALL_DATADIR=%{_datadir} \
    -DGLOBAL_DIR:PATH=%{_datadir}/%{name}

%cmake_build

%install
%cmake_install

# Remove the installed docs - we will install subset of those
rm -rf $RPM_BUILD_ROOT%{_docdir}

# install documentation
install -dpm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/docs/
cp -a docs/* $RPM_BUILD_ROOT%{_datadir}/%{name}/docs/
# this is installed into the proper path earlier
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/docs/%{name}.6


desktop-file-install --dir=$RPM_BUILD_ROOT%{_datadir}/applications \
        --add-category=StrategyGame \
        $RPM_BUILD_ROOT%{_datadir}/applications/openttd.desktop

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
<!-- Copyright 2014 Ankur Sinha <ankursinha@fedoraproject.org> -->
<!--
EmailAddress: alberth@openttd.org
SentUpstream: 2014-09-25
-->
<application>
  <id type="desktop">openttd.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>A highly detailed transport simulation game</summary>
  <description>
  <p>
      OpenTTD is a transport tycoon simulation game that enhances the
      original Transport Tycoon game developed by Chris Sawyer.
      The game includes road, air, train and naval transport with a large
      selection of industries and passenger services that need to be provided.
    </p>
  <p>
      The game can be played in both single and multiplayer modes where
      you compete with other transport companies to dominate the markets.
  </p>
  </description>
  <url type="homepage">https://www.openttd.org</url>
  <screenshots>
    <screenshot type="default">https://www.openttd.org/screenshots/1.4-02-opengfx-1920x1200.png</screenshot>
    <screenshot>https://www.openttd.org/screenshots/1.9-darkuk-3.png</screenshot>
  </screenshots>
  <updatecontact>info@openttd.org</updatecontact>
</application>
EOF

%files
%license COPYING.md
%doc changelog.txt CONTRIBUTING.md CREDITS.md known-bugs.txt README.md
%{_bindir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man6/%{name}.6*
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.32.xpm
%{_datadir}/pixmaps/%{name}.64.xpm
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%exclude %{_datadir}/%{name}/docs

%files docs
# These are really devel docs, but as we don't have -devel subpackage, we put it here
# Could be useful for people making graphics, AI scripts or translations
%{_datadir}/%{name}/docs/


%changelog
* Mon Feb 06 2023 Felix Kaechele <felix@kaechele.ca> - 13.0-1
- update to 13.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 12.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 31 2022 Pete Walter <pwalter@fedoraproject.org> - 12.2-5
- Rebuild for ICU 72

* Sun Sep 25 2022 Felix Kaechele <felix@kaechele.ca> - 12.2-4
- add weak dependency on fluid-soundfont-gm (rhbz#1588367)

* Mon Aug 01 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 12.2-3
- Rebuilt for ICU 71.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Apr 03 2022 Felix Kaechele <felix@kaechele.ca> - 12.2-1
- update to 12.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 09 2021 Felix Kaechele <felix@kaechele.ca> - 12.1-1
- update to 12.1

* Mon Oct 18 2021 Felix Kaechele <felix@kaechele.ca> - 12.0-1
- update to 12.0

* Sat Sep 25 2021 Felix Kaechele <felix@kaechele.ca> - 12.0-0.2.RC1
- update to 12.0-RC1

* Sun Aug 22 2021 Felix Kaechele <felix@kaechele.ca> - 12.0-0.1.beta2
- update to 12.0-beta2

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Felix Kaechele <felix@kaechele.ca> - 1.11.2-3
- set CMAKE_BUILD_TYPE to Release (rhbz#1963215)

* Thu May 20 2021 Pete Walter <pwalter@fedoraproject.org> - 1.11.2-2
- Rebuild for ICU 69

* Tue May 04 2021 Felix Kaechele <felix@kaechele.ca> - 1.11.2-1
- update to 1.11.2

* Mon Apr 19 2021 Felix Kaechele <felix@kaechele.ca> - 1.11.1-1
- update to 1.11.1

* Thu Apr 01 2021 Felix Kaechele <felix@kaechele.ca> - 1.11.0-1
- update to 1.11.0 final

* Mon Mar 15 2021 Felix Kaechele <felix@kaechele.ca> - 1.11.0-0.2.RC1
- update to 1.11.0-RC1
- replace timidity with fluidsynth to allow for ingame sound control

* Mon Mar 08 2021 Felix Kaechele <felix@kaechele.ca> - 1.11.0-0.1.beta2
- update to 1.11.0-beta2
- switch to cmake build system
- remove BR on ccache, libtimidity, unzip; no longer needed
- update screenshots and indentation in appdata.xml

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild


* Thu Aug 13 2020 Felix Kaechele <heffer@fedoraproject.org> - 1.10.3-1
- update to 1.10.3

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 03 2020 Felix Kaechele <heffer@fedoraproject.org> - 1.10.2-1
- update to 1.10.2

* Fri May 15 2020 Pete Walter <pwalter@fedoraproject.org> - 1.10.1-2
- Rebuild for ICU 67

* Tue Apr 14 2020 Felix Kaechele <heffer@fedoraproject.org> - 1.10.1-1
- update to 1.10.1

* Wed Apr 01 2020 Felix Kaechele <heffer@fedoraproject.org> - 1.10.0-1
- update to 1.10.0

* Wed Feb 26 2020 Felix Kaechele <heffer@fedoraproject.org> - 1.10.0-0.1.RC1
- update to 1.10.0-RC1
- switch to SDL2
- update source URL

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 01 2019 Pete Walter <pwalter@fedoraproject.org> - 1.9.3-2
- Rebuild for ICU 65

* Thu Sep 19 2019 Felix Kaechele <heffer@fedoraproject.org> - 1.9.3-1
- update to 1.9.3

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Felix Kaechele <heffer@fedoraproject.org> - 1.9.2-1
- update to 1.9.2

* Mon Apr 08 2019 Felix Kaechele <heffer@fedoraproject.org> - 1.9.1-1
- update to 1.9.1

* Tue Apr 02 2019 Felix Kaechele <heffer@fedoraproject.org> - 1.9.0-1
- Update to 1.9.0
- Upstream changed source URLs

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Pete Walter <pwalter@fedoraproject.org> - 1.8.0-6
- Rebuild for ICU 63

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 1.8.0-4
- Rebuild for ICU 62

* Thu Jun 07 2018 Felix Kaechele <heffer@fedoraproject.org> - 1.8.0-3
- re-sort BuildRequires
- use autosetup macro
- Switch openttd-opengfx from Requires to Recommends (game works without it as
  free/libre content can be downloaded from within the game)
- add Recommends timidity++ (BZ#1588367)
- add patch to fix compilation with ICU 61

* Mon Apr 30 2018 Pete Walter <pwalter@fedoraproject.org> - 1.8.0-2
- Rebuild for ICU 61.1

* Wed Apr 04 2018 Felix Kaechele <heffer@fedoraproject.org> - 1.8.0-1
- update to 1.8.0

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.7.2-2
- Remove obsolete scriptlets

* Thu Dec 28 2017 Felix Kaechele <heffer@fedoraproject.org> - 1.7.2-1
- update to 1.7.2

* Thu Nov 30 2017 Pete Walter <pwalter@fedoraproject.org> - 1.7.1-4
- Rebuild for ICU 60.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 26 2017 Felix Kaechele <heffer@fedoraproject.org> - 1.7.1-1
- update to 1.7.1

* Mon Apr 10 2017 Felix Kaechele <heffer@fedoraproject.org> - 1.7.0-1
- update to 1.7.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 06 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.6.1-2
- rebuild for libtimidity 0.2.x

* Thu Jun 30 2016 Felix Kaechele <heffer@fedoraproject.org> - 1.6.1-1
- update to 1.6.1
- drop GCC 6 patch

* Mon May 23 2016 Felix Kaechele <heffer@fedoraproject.org> - 1.6.0-1
- update to 1.6.0

* Fri Apr 15 2016 David Tardon <dtardon@redhat.com> - 1.5.3-4
- rebuild for ICU 57.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Feb 02 2016 Jonathan Wakely <jwakely@redhat.com> - 1.5.3-2
- Patched to build with GCC 6

* Sat Jan 02 2016 Felix Kaechele <heffer@fedoraproject.org> - 1.5.3-1
- update to 1.5.3

* Wed Oct 28 2015 David Tardon <dtardon@redhat.com> - 1.5.2-2
- rebuild for ICU 56.1

* Sat Oct 03 2015 Felix Kaechele <heffer@fedoraproject.org> - 1.5.2-1
- update to 1.5.2

* Tue Jul 28 2015 Felix Kaechele <heffer@fedoraproject.org> - 1.5.1-1
- update to 1.5.1

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.5.0-2
- Rebuilt for GCC 5 C++11 ABI change

* Sun Apr 05 2015 Felix Kaechele <heffer@fedoraproject.org> - 1.5.0-1
- update to 1.5.0
- remove compile patch, fixed upstream

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1.4.4-3
- Add an AppData file for the software center

* Mon Jan 26 2015 David Tardon <dtardon@redhat.com> - 1.4.4-2
- rebuild for ICU 54.1

* Tue Oct 21 2014 Felix Kaechele <heffer@fedoraproject.org> - 1.4.4-1
- update to 1.4.4

* Tue Sep 23 2014 Felix Kaechele <heffer@fedoraproject.org> - 1.4.3-1
- update to 1.4.3

* Tue Aug 26 2014 David Tardon <dtardon@redhat.com> - 1.4.2-3
- rebuild for ICU 53.1

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Aug 16 2014 Felix Kaechele <heffer@fedoraproject.org> - 1.4.2-1
- update to 1.4.2

* Sat Jun 21 2014 Felix Kaechele <heffer@fedoraproject.org> - 1.4.1-1
- update to 1.4.1
- change my e-mail in the changelogs

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 04 2014 Felix Kaechele <heffer@fedoraproject.org> - 1.4.0-1
- update to 1.4.0
- bump dependency on openttd-opengfx to 0.5.0

* Thu Feb 13 2014 Felix Kaechele <heffer@fedoraproject.org> - 1.3.3-2
- rebuild for new ICU

* Thu Dec 12 2013 Felix Kaechele <heffer@fedoraproject.org> - 1.3.3-1
- update to 1.3.3
- fixes CVE-2013-6411

* Sat Sep 21 2013 Felix Kaechele <heffer@fedoraproject.org> - 1.3.2-3
- another try at a rebuild to fix BZ#989786

* Fri Aug 02 2013 Felix Kaechele <heffer@fedoraproject.org> - 1.3.2-2
- rebuild for icu

* Sun Jul 28 2013 Felix Kaechele <heffer@fedoraproject.org> - 1.3.2-1
- update to 1.3.2

* Mon Jul 22 2013 David Tardon <dtardon@redhat.com> - 1.3.2-0.2.RC1
- rebuild for ICU ABI break

* Thu Jul 04 2013 Felix Kaechele <heffer@fedoraproject.org> - 1.3.2-0.1.RC1
- update to 1.3.2-RC1

* Wed May 22 2013 Felix Kaechele <heffer@fedoraproject.org> - 1.3.1-0.1.RC1
- update to the 1.3.1-RC1
- fixes compilation with F19+

* Mon Apr 08 2013 Felix Kaechele <heffer@fedoraproject.org> - 1.3.0-1
- update to 1.3.0

* Sat Mar 23 2013 Felix Kaechele <heffer@fedoraproject.org> - 1.3.0-0.1.RC3
- update to 1.3.0-RC3
- fixes compilation on F19+

* Fri Feb 08 2013 Jon Ciesla <limburgher@gmail.com> - 1.2.3-2
- libicu rebuild.

* Sat Dec 15 2012 Felix Kaechele <heffer@fedoraproject.org> - 1.2.3-1
- update to 1.2.3

* Sat Aug 18 2012 Felix Kaechele <heffer@fedoraproject.org> - 1.2.2-1
- fixes CVE-2012-3436
- many other bugfixes

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 26 2012 Felix Kaechele <heffer@fedoraproject.org> - 1.2.1-1
- update to 1.2.1

* Mon Apr 23 2012 Felix Kaechele <heffer@fedoraproject.org> - 1.2.0-2
- rebuild for new icu

* Sun Apr 15 2012 Felix Kaechele <heffer@fedoraproject.org> - 1.2.0-1
- update to stable 1.2.0

* Tue Apr 03 2012 Felix Kaechele <heffer@fedoraproject.org> - 1.2.0-0.1.RC4
- Update to 1.2.0-RC4
- builds in F17 and rawhide again

* Sun Jan 15 2012 Felix Kaechele <heffer@fedoraproject.org> - 1.1.5-1
- update to 1.1.5
- fixes CVE-2012-0049 (bz #782179)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.1.3-2
- Rebuild for new libpng

* Sun Sep 18 2011 Felix Kaechele <heffer@fedoraproject.org> - 1.1.3-1
- update to 1.1.3
- fixes CVE-2011-3341, CVE-2011-3342 and CVE-2011-3343

* Fri Sep 09 2011 Felix Kaechele <heffer@fedoraproject.org> - 1.1.2-2
- rebuild for new icu

* Mon Aug 29 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 1.1.2-1
- update to 1.1.2
- drop definition of buildroot, defattr and clean stage

* Sun Jun 12 2011 Felix Kaechele <heffer@fedoraproject.org> - 1.1.1-1
- update to 1.1.1

* Tue Apr 05 2011 Felix Kaechele <heffer@fedoraproject.org> - 1.1.0-2
- add BR xz-devel

* Tue Apr 05 2011 Felix Kaechele <heffer@fedoraproject.org> - 1.1.0-1
- update to 1.1.0
- cleaned up configure arguments
- enabled GCC's Link Time Optimization (LTO)

* Mon Mar 07 2011 Caolán McNamara <caolanm@redhat.com> - 1.0.5-3
- rebuild for icu 4.6

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Nov 21 2010 Felix Kaechele <heffer@fedoraproject.org> - 1.0.5-1
- 1.0.5
- fixes CVE-2010-4168 Denial of service (server/client) via invalid read
- switched to using the XZ tarball

* Sat Sep 18 2010 Felix Kaechele <heffer@fedoraproject.org> - 1.0.4-1
- new upstream release

* Tue Aug 03 2010 Felix Kaechele <heffer@fedoraproject.org> - 1.0.3-1
- update to final 1.0.3
- fixes various and desync bugs

* Sat Jul 24 2010 Felix Kaechele <heffer@fedoraproject.org> - 1.0.3-0.1.RC1
- update to 1.0.3-RC1
- contains fixes for a remote DoS described in CVE-2010-2534

* Sun Jun 20 2010 Felix Kaechele <heffer@fedoraproject.org> - 1.0.2-1
- update to 1.0.2
- contains bugfixes and translation updates

* Sat May 01 2010 Felix Kaechele <heffer@fedoraproject.org> - 1.0.1-1
- update to 1.0.1
- fixes CVE-2010-0401, CVE-2010-0402, CVE-2010-0406

* Fri Apr 02 2010 Caolán McNamara <caolanm@redhat.com> - 1.0.0-2
- rebuild for icu 4.4

* Thu Apr 01 2010 Felix Kaechele <heffer@fedoraproject.org> - 1.0.0-1
- update to final release

* Thu Mar 18 2010 Felix Kaechele <heffer@fedoraproject.org> - 1.0.0-0.6.RC3
- update to RC3

* Thu Mar 04 2010 Felix Kaechele <heffer@fedoraproject.org> - 1.0.0-0.5.RC2
- 1.0.0-RC2 bugfix release

* Wed Feb 24 2010 Felix Kaechele <heffer@fedoraproject.org> - 1.0.0-0.4.RC1
- update to RC1

* Fri Feb 05 2010 Felix Kaechele <heffer@fedoraproject.org> - 1.0.0-0.3.beta4
- 1.0.0-beta4

* Thu Jan 21 2010 Felix Kaechele <heffer@fedoraproject.org> - 1.0.0-0.2.beta3
- 1.0.0-beta3

* Sat Jan 16 2010 Felix Kaechele <heffer@fedoraproject.org>
- 1.0.0-beta2

* Sat Jan 02 2010 Felix Kaechele <heffer@fedoraproject.org> - 0.7.5-1
- 0.7.5 stable release
- fixes CVE-2009-4007

* Thu Dec 17 2009 Felix Kaechele <heffer@fedoraproject.org> - 0.7.5-0.1.rc1
- bump to 0.7.5-RC1
- omitting 0.7.4 because it has a bug

* Sat Oct 10 2009 Alexey Torkhov <atorkhov@gmail.com> - 0.7.3-1
- New upstream release 0.7.3

* Sun Aug 23 2009 Felix Kaechele <heffer@fedoraproject.org> - 0.7.2-1
- new upstream release 0.7.2

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 12 2009 Felix Kaechele <heffer@fedoraproject.org> - 0.7.1-1
- upstream 0.7.1

* Sun May 31 2009 Felix Kaechele <heffer@fedoraproject.org> - 0.7.1-0.4.rc2
- disable allegro due to performance problems

* Fri May 29 2009 Felix Kaechele <heffer@fedoraproject.org> - 0.7.1-0.3.rc2
- updated icon cache scriptlets

* Thu May 28 2009 Felix Kaechele <heffer@fedoraproject.org> - 0.7.1-0.2.rc2
- 0.7.1-RC2
- build docs from source

* Sat May 16 2009 Felix Kaechele <heffer@fedoraproject.org> - 0.7.1-0.1.rc1
- updated to 0.7.1-RC1

* Sat Apr 11 2009 Felix Kaechele <felix at fetzig dot org> - 0.7.0-1
- upstream 0.7.0
- added docs subpackage

* Sun Mar 29 2009 Felix Kaechele <felix at fetzig dot org> - 0.7.0-0.3.rc2
- 0.7.0-RC2
- dropped Patch0 since this does not reflect the behaviour that is intended
  by upstream. See http://bugs.openttd.org/task/2756

* Sat Mar 21 2009 Felix Kaechele <felix at fetzig dot org> - 0.7.0-0.2.rc1
- updated to RC1
- removed all references to possible trademarks
- added patch to ignore a missing sample.cat

* Mon Mar 09 2009 Alexey Torkhov <atorkhov@gmail.com> - 0.7.0-0.1.beta1
- Doing big cleanup of package:
- Dropping subpackages
- Drop .desktop sources in favour of one bundled
- Drop server menu entry - one can start server from game menu
- Drop suspicious data_patch (what was it needed for?)
- Cleanup macro usage
- Drop version from freetype build dep
- Correcting dirs in configure call: icons paths, disable duplicate shared dir,
  correct doc dir

- And adding few improvements:
- Using VERBOSE when doing make
- Adding libicu to build requires
- Add icons theme require
- Drop installation instructions from docs
- Use ccache (should speedup the local and mock builds)
- Change source url to canonical one

* Sun Jan 11 2009 Felix Kaechele <felix at fetzig dot org> - 0.6.3-3
- even more improvements made

* Sun Jan 11 2009 Felix Kaechele <felix at fetzig dot org> - 0.6.3-2
- incorporated suggestions made by reviewers

* Wed Dec 31 2008 Felix Kaechele <felix at fetzig dot org> - 0.6.3-1
- Initial build based on the SPEC by Peter Hanecak (http://hany.sk/~hany/RPM/)
