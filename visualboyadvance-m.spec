%undefine _hardened_build

%global shortname vbam
#Upstream git tag/commit:
%global upstreamtag 2.1.7
#Sanitized RC name (for fedora)
#global rctagfedora git78cd223
#RC Version that appears in app
#global rcversion Beta3-07032017

Name:           visualboyadvance-m
Version:        %{upstreamtag}
Release:        1%{?rctagfedora:.%{rctagfedora}}%{?dist}.2
Summary:        High compatibility Gameboy Advance Emulator combining VBA builds

License:        GPLv2
Url:            http://www.vba-m.com
Source0:        https://github.com/%{name}/%{name}/archive/v%{upstreamtag}.tar.gz#/%{name}-%{version}%{?rctagfedora:-%{rctagfedora}}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cairo-devel
BuildRequires:  cmake
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  nasm
BuildRequires:  openal-soft-devel
BuildRequires:  SDL2-devel
BuildRequires:  SFML-devel
BuildRequires:  wxGTK-devel
BuildRequires:  zlib-devel
BuildRequires:  zip

BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme
BuildRequires:  libappstream-glib

Requires:  hicolor-icon-theme

# 32bit package serves very little purpose:
ExcludeArch: %{ix86}

#Using info from here: http://vba-m.com/about.html and debian files
%description
VisualBoyAdvance-M is a Nintendo Game Boy Emulator with high compatibility with
commercial games. It emulates the Nintendo Game Boy Advance hand held console,
in addition to the original Game Boy hand held systems and its Super and Color
variants. VBA-M is a continued development of the now inactive VisualBoy
Advance project, with many improvements from various developments of VBA.

%package        sdl
Summary:        SDL version (no GUI) for VBA-M, a high compatibility Gameboy Advance Emulator

%description    sdl
This package provides the no-GUI, SDL only version of VisualBoyAdvance-M.
VisualBoyAdvance-M is a Nintendo Game Boy Emulator with high compatibility with
commercial games. It emulates the Nintendo Game Boy Advance hand held console,
in addition to the original Game Boy hand held systems and its Super and Color
variants. VBA-M is a continued development of the now inactive VisualBoy
Advance project, with many improvements from various developments of VBA.

%prep
%autosetup -p1 -n %{name}-%{upstreamtag}
sed -i 's/ -mtune=generic//g' CMakeLists.txt
#Some odd permission issues:
chmod -x src/wx/rpi.h

%build
%cmake \
    -DCMAKE_SKIP_RPATH=ON \
    -DVERSION="%{version}%{?rcversion: %{rcversion}}" \
    -DVERSION_RELEASE=TRUE \
    -DENABLE_SDL=ON \
    -DENABLE_WX=ON \
    -DENABLE_FFMPEG=OFF \
    -DENABLE_LINK=ON
%cmake_build

%install
%cmake_install
%find_lang wx%{shortname}

%check
desktop-file-validate \
    %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet \
  %{buildroot}/%{_datadir}/metainfo/%{name}.metainfo.xml

%files -f wx%{shortname}.lang
%license doc/gpl.txt doc/License.txt
%doc doc/ips.htm
%{_mandir}/man6/%{name}.*
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}.metainfo.xml
%{_datadir}/%{shortname}
%{_datadir}/icons/hicolor/*/apps/%{name}.*

%files sdl
%doc doc/ReadMe.SDL.txt
%license doc/gpl.txt doc/License.txt
%config(noreplace) %{_sysconfdir}/%{shortname}.cfg
%{_mandir}/man6/%{shortname}.*
%{_bindir}/%{shortname}

%changelog
* Sun Nov 05 2023 Sérgio Basto <sergio@serjux.com> - 2.1.7-1.2
- Rebuild for SFML-2.6.1

* Wed Sep 13 2023 Jeremy Newton <alexjnewt AT hotmail DOT com> - 2.1.7-1
- Update to 2.1.7

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 14 2023 Jeremy Newton <alexjnewt AT hotmail DOT com> - 2.1.6-1
- Update to 2.1.6

* Mon Jan 30 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 2.1.5-1
- Update to 2.1.5

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-4.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Nov 27 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.4-4.5
- Rebuild due to wxGLCanvas ABI change

* Thu Aug 04 2022 Scott Talbert <swt@techie.net> - 2.1.4-4.4
- Rebuild with wxWidgets 3.2

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-4.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-4.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Jeremy Newton <alexjnewt AT hotmail DOT com> - 2.1.4-4
- Cherry-pick build fix for SDL

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar 11 2020 Jeremy Newton <alexjnewt AT hotmail DOT com> - 2.1.4-3
- Fix RHBZ#1776006

* Fri Mar 6 2020 Jeremy Newton <alexjnewt AT hotmail DOT com> - 2.1.4-2
- Fix non x86 arches (backported a patch from upstream)

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

 * Wed Dec 11 2019 Jeremy Newton <alexjnewt AT hotmail DOT com> - 2.1.4-1
- Update to v2.1.4

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

 * Tue Apr 23 2019 Jeremy Newton <alexjnewt AT hotmail DOT com> - 2.1.3-1
- Update to v2.1.3

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

 * Sat Sep 15 2018 Jeremy Newton <alexjnewt AT hotmail DOT com> - 2.1.0-2
- Actually use 2.1.0 sources
- Add performance patch for xserver

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

 * Sun Jul 01 2018 Jeremy Newton <alexjnewt AT hotmail DOT com> - 2.1.0-1
- Update to v2.1.0

* Thu Mar 15 2018 Jeremy Newton <alexjnewt AT hotmail DOT com> - 2.0.2-1
- Update to v2.0.2
- Cleanup old rpmfusion provides

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.1-1.1
- Remove obsolete scriptlets

* Mon Dec 11 2017 Jeremy Newton <alexjnewt AT hotmail DOT com> - 2.0.1-1
- Update to v2.0.1
- Cleanup

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.18.git78cd223
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.17.git78cd223
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 16 2017 Jeremy Newton <alexjnewt AT hotmail DOT com> - 2.0.0-0.16.git78cd223
- Update to new git snapshot

* Sun Mar 05 2017 Jeremy Newton <alexjnewt AT hotmail DOT com> - 2.0.0-0.15.git7b85964
- Update to new git snapshot

* Sun Mar 05 2017 Jeremy Newton <alexjnewt AT hotmail DOT com> - 2.0.0-0.14.waylandplus
- Update to new version
- Add patch for SDL issues
- Fix incorrect bug tracker link

* Mon Feb 20 2017 Jeremy Newton <alexjnewt AT hotmail DOT com> - 2.0.0-0.13.git6a7d494
- Update to git snapshot, fixes many issues
- Drop wayland and openal fixes (better fixes have been upstreamed)
- Better workaround patch for sound syncing issue

* Wed Feb 15 2017 Jeremy Newton <alexjnewt AT hotmail DOT com> - 2.0.0-0.12.Beta3
- Rebuilt for SFML 2.4

* Sat Feb 11 2017 Jeremy Newton <alexjnewt AT hotmail DOT com> - 2.0.0-0.11.Beta3
- Added missing obsoletes for vbam-common (from rpmfusion)
- Tweaking openal patch

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.10.Beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 30 2017 Jeremy Newton <alexjnewt AT hotmail DOT com> - 2.0.0-0.9.Beta3
- Fix dynamic loading of openal library if openal-soft-devel is not installed

* Sun Jan 29 2017 Jeremy Newton <alexjnewt AT hotmail DOT com> - 2.0.0-0.8.Beta3
- Add patch to fix wayland drawing
- Remove launcher to force xwayland

* Thu Jan 19 2017 Jeremy Newton <alexjnewt AT hotmail DOT com> - 2.0.0-0.7.Beta3
- Force X11/xwayland, rendering issues exist on Wayland
- Enable cairo to fix wx segfaults on xwayland

* Thu Jan 19 2017 Dan Horák <dan[at]danny.cz> - 2.0.0-0.6.Beta3
- Don't override distro-wide -mtune option

* Wed Jan 18 2017 Jeremy Newton <alexjnewt AT hotmail DOT com> - 2.0.0-0.5.Beta3
- Added fix for armv7hl and pcc

* Fri Dec 30 2016 Jeremy Newton <alexjnewt AT hotmail DOT com> - 2.0.0-0.4.Beta3
- Added missing desktop scriptlet for f24
- Added missing build requires
- Missing hicolor-icon-theme require
- Use sysconfdir macro in spec

* Wed Dec 21 2016 Jeremy Newton <alexjnewt AT hotmail DOT com> - 2.0.0-0.3.Beta3
- Update to beta 3
- Dropping GTK, upstream no longer supports this
- Change packagename visualboyadvance-m to reflect upstream
- Various tweaks

* Sat Dec 10 2016 Jeremy Newton <alexjnewt AT hotmail DOT com> - 2.0.0-0.2.beta2
- Added patch to fix audio syncing issues
- Added fixes for linux data files

* Fri Dec  9 2016 Jeremy Newton <alexjnewt AT hotmail DOT com> - 2.0.0-0.1.beta2
- Update to 2.0.0 beta 2
- Re-enable wx GUI
- Rename common subpackage to data
- Added appdata
- Build Require cleanup

* Thu Jul  7 2016 Hans de Goede <j.w.r.degoede@gmail.com> - 1.8.0.1229-3
- Fix building with gcc6 / fix FTBFS

* Mon Jan 12 2015 Jeremy Newton <alexjnewt AT hotmail DOT com> - 1.8.0.1229-2
- Fix typo in desktop file

* Sat Apr 5 2014 Jeremy Newton <alexjnewt AT hotmail DOT com> - 1.8.0.1229-1
- Update to latest "release" version

* Mon Nov 18 2013 Jeremy Newton <alexjnewt AT hotmail DOT com> - 1.8.0.1228-3
- Update patch for SFML, thanks to Hans de Goede

* Sun Nov 17 2013 Jeremy Newton <alexjnewt AT hotmail DOT com> - 1.8.0.1228-2
- Added patch for SFML

* Sun Nov 17 2013 Jeremy Newton <alexjnewt AT hotmail DOT com> - 1.8.0.1228-1
- Updated to new snapshot version

* Fri Mar 1 2013 Jeremy Newton <alexjnewt AT hotmail DOT com> - 1.8.0.1159-1
- Updated to new upstream version
- Fixed some spec date typos

* Mon Dec 10 2012 Jeremy Newton <alexjnewt AT hotmail DOT com> - 1.8.0.1149-1
- Updated to new upstream version
- FFMpeg dep removed due to only needed by wx and now disabled by default

* Thu Jul 5 2012 Jeremy Newton <alexjnewt AT hotmail DOT com> - 1.8.0.1097-1
- Updated to new upstream version
- Disabling WX because its not supported
- Removed extra sources as they are now included
- Removed FFMPEG fix
- Moved ips.htm doc file into common to avoid duplicates
- Various cleanup

* Wed Mar 28 2012 Jeremy Newton <alexjnewt AT hotmail DOT com> - 1.8.0.1054-6
- Added man pages

* Tue Feb 14 2012 Jeremy Newton <alexjnewt AT hotmail DOT com> - 1.8.0.1054-5
- Added Zip as a dependancy

* Tue Feb 14 2012 Jeremy Newton <alexjnewt AT hotmail DOT com> - 1.8.0.1054-4
- Changed building commands to avoid failed builds

* Sun Jan 29 2012 Jeremy Newton <alexjnewt AT hotmail DOT com> - 1.8.0.1054-3
- Added missing Build Requirement: openal-soft-devel
- Removed redundant license files

* Thu Jan 26 2012 Jeremy Newton <alexjnewt AT hotmail DOT com> - 1.8.0.1054-2
- Added DCMAKE_SKIP_RPATH=ON to cmake (fixes rpath error)
- Added more relevant package summaries
- Fixed up the descriptions a bit
- Enabled Linking Support
- Various tweaks

* Thu Jan 26 2012 Jeremy Newton <alexjnewt AT hotmail DOT com> - 1.8.0.1054-1
- Updated to new upstream version
- Added new WX subpackage for new GUI
- Adding WX requires gui common subpackage to avoid conflicts
- Added DVERSION cmake tag for aesthetic reasons

* Sun Jan 22 2012 Jeremy Newton <alexjnewt AT hotmail DOT com> - 1.8.0.1001-4
- Added vbam-common package to avoid conflicts with common files
- Added ImageMagick build dep, as cmake checks for it
- Building now uses cmake macro
- Turned off building shared libs
- Removed unnecessary lines
- Fixed debuginfo-without-sources issue

* Sun Jan 22 2012 Jeremy Newton <alexjnewt AT hotmail DOT com> - 1.8.0.1001-3
- Fixed SPM summary
- Cleaned up SPEC for easier reading

* Sun Jan 8 2012 Jeremy Newton <alexjnewt AT hotmail DOT com> - 1.8.0.1001-2
- Fixed up spec file
- Split into two packages: sdl, gtk

* Sun Dec 18 2011 Jeremy Newton <alexjnewt AT hotmail DOT com> - 1.8.0.1001-1
- Initial package SPEC created

