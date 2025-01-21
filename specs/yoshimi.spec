%global _vpath_srcdir src

Name:		yoshimi
Version:	2.3.0
Release:	6%{?dist}
Summary:	Rewrite of ZynAddSubFx aiming for better JACK support

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://sourceforge.net/projects/%{name}
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
Patch0:		%{name}-cflags.patch

BuildRequires:  gcc-c++
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	cmake 
BuildRequires:	zlib-devel 
BuildRequires:	fontconfig-devel
BuildRequires:	fltk-devel 
BuildRequires:	fltk-fluid 
BuildRequires:	fftw3-devel
BuildRequires:	mxml-devel 
BuildRequires:	alsa-lib-devel 
BuildRequires:	libsndfile-devel
BuildRequires:	desktop-file-utils 
BuildRequires:	boost-devel
BuildRequires:	mesa-libGL-devel
BuildRequires:	cairo-devel
BuildRequires:  lv2-devel
BuildRequires:  readline-devel

%description

Yoshimi is a rewrite of ZynAddSubFx to improve its compatibility with
the Jack Audio Connection Kit.

ZynAddSubFX is an open source software synthesizer capable of making a
countless number of instrument sounds. It is microtonal, and the instruments
made by it sound like those from professional keyboards. The program has
effects like Reverb, Echo, Chorus, Phaser...

%prep
%setup -q
%patch 0 -p1

%build
export CFLAGS="%{optflags}"
%cmake -DCMAKE_CXX_FLAGS="${RPM_OPT_FLAGS} -fPIC" -DFLTK_INCLUDE_DIR=%{_includedir}/Fl
%cmake_build


%install
%cmake_install

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -m 644 desktop/%{name}.png %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/

# Fix directory permissions without affecting patch files
chmod 755 %{buildroot}%{_datadir}/%{name}/banks
chmod 755 %{buildroot}%{_datadir}/%{name}/banks/*
chmod 755 %{buildroot}%{_datadir}/%{name}/presets
chmod 755 %{buildroot}%{_datadir}/%{name}/presets/*

#rm %{buildroot}%{_datadir}/doc/%{name}/yoshimi-user-manual-2.0.pdf

%files
%doc Changelog COPYING README.txt doc/* 
%{_bindir}/%{name}
%{_datadir}/%{name}/banks/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.png
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}/presets/
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/icons/hicolor/scalable/apps/%{name}_alt.svg
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/metainfo/%{name}.metainfo.xml
%{_datadir}/%{name}/examples/
%{_libdir}/lv2/%{name}.lv2/
%{_mandir}/man1/yoshimi.1*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.3.0-5
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed May 31 2023 Adam Huffman <bloch@verdurin.com> - 2.3.0-1
- Update to upstream feature release 2.3.0

* Mon Feb 13 2023 Adam Huffman <bloch@verdurin.com> - 2.2.3-1
- Update to latest bugfix release 2.2.3

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jul 25 2022 Adam Huffman <bloch@verdurin.com> - 2.2.1-1
- Update to upstream feature and bugfix release 2.2.1

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun May 22 2022 Adam Huffman <bloch@verdurin.com> - 2.2.0-1
- Update to latest feature release

* Sun Feb 13 2022 Adam Huffman <bloch@verdurin.com> - 2.1.2.2-1
- Update to latest upstream bugfix release 

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 22 2021 Adam Huffman <bloch@verdurin.com> - 2.0.2-1
- Update to upstream bugfix release 2.0.2

* Sun Apr 18 2021 Adam Huffman <bloch@verdurin.com> - 2.0.1-1
- Update to upstream bugfix release 2.0.1

* Mon Mar 01 2021 Adam Huffman <bloch@verdurin.com> - 2.0-1
- New upstream major release 2.0

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 06 2021 Adam Huffman <bloch@verdurin.com> - 1.7.4-1
- Update to upstream maintenance release 1.7.4

* Sun Nov 22 2020 Adam Huffman <bloch@verdurin.com> - 1.7.3-1
- Update to upstream release 1.7.3

* Wed Aug 19 2020 Adam Huffman <bloch@verdurin.com> - 1.7.2-1
- Update to upstream release 1.7.2

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 20 2020 Adam Huffman <bloch@verdurin.com> - 1.7.1-1
- Update to upstream release 1.7.1

* Fri Feb 07 2020 Adam Huffman <bloch@verdurin.com> - 1.7.0.1-1
- Update to upstream bugfix release 1.7.0.1

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 24 2020 Adam Huffman <bloch@verdurin.com> - 1.7.0-1
- Update to upstream release 1.7.0

* Sun Oct 20 2019 Adam Huffman <bloch@verdurin.com> - 1.6.0.2-1
- Update to upstream bugfix release 1.6.0.2

* Tue Oct 15 2019 Adam Huffman <bloch@verdurin.com> - 1.6.0.1-1
- Update to upstream bugfix release 1.6.0.1

* Thu Sep 05 2019 Adam Huffman <bloch@verdurin.com> - 1.6.0-1
- Update to upstream release 1.6.0

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.5.10-3
- Rebuild for readline 8.0

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 06 2019 Adam Huffman <bloch@verdurin.com> - 1.5.10-1
- Update to upstream release 1.5.10

* Wed Sep 26 2018 Adam Huffman <bloch@verdurin.com> - 1.5.9-1
- Update to upstream release 1.5.9

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 10 2018 Adam Huffman <bloch@verdurin.com> - 1.5.8.2-1
- Update to upstream bugfix release 1.5.8.2

* Mon Jun 04 2018 Adam Huffman <bloch@verdurin.com> - 1.5.8.1-1
- Update to upstream release 1.5.8.1

* Thu Mar 22 2018 Adam Huffman <bloch@verdurin.com> - 1.5.7-1
- Update to upstream bugfix release 1.5.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.5.4.1-2
- Remove obsolete scriptlets

* Fri Oct 20 2017 Adam Huffman <bloch@verdurin.com> - 1.5.4.1-1
- Update to upstream bugfix release 1.5.4.1

* Fri Sep 29 2017 Adam Huffman <bloch@verdurin.com> - 1.5.4-1
- Update to upstream release 1.5.4

* Fri Sep 22 2017 Adam Huffman <bloch@verdurin.com> - 1.5.3-1
- Update to upstream release 1.5.3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 25 2017 Adam Huffman <bloch@verdurin.com> - 1.5.2.1-1
- Update to upstream minor release 1.5.2.1

* Wed May 24 2017 Adam Huffman <bloch@verdurin.com> - 1.5.2-1
- Update to new upstream release 1.5.2

* Thu Apr 13 2017 Adam Huffman <bloch@verdurin.com> - 1.5.1.1-1
- Update to upstream bugfix release 1.5.1.1

* Mon Apr 03 2017 Adam Huffman <bloch@verdurin.com> - 1.5.1-1
- Update to upstream release 1.5.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 1.5.0-3
- Rebuilt for Boost 1.63

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.5.0-2
- Rebuild for readline 7.x

* Thu Dec 22 2016 Adam Huffman <bloch@verdurin.com> - 1.5.0-1
- Update to upstream release 1.5.0 with MIDI Learn features

* Mon Sep 05 2016 Adam Huffman <bloch@verdurin.com> - 1.4.1-1
- Update to upstream release 1.4.1 (last update was to 1.4.0.1)

* Sat Jun 18 2016 Adam Huffman <bloch@verdurin.com> - 1.4.0.1-1
- Update to upstream bug-fix release 1.4.1

* Sun Mar 06 2016 Adam Huffman <bloch@verdurin.com> - 1.3.9-1
- Update to upstream release 1.3.9

* Sat Feb 13 2016 Adam Huffman <bloch@verdurin.com> - 1.3.8.2-2
- Patch for GCC6 build fixes

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 23 2016 Adam Huffman <bloch@verdurin.com> - 1.3.8.2-1
- Update to upstream bug-fix release 1.3.8.2

* Tue Jan 19 2016 Adam Huffman <bloch@verdurin.com> - 1.3.8.1-1
- Update to upstream release 1.3.8.1
- Include new manpage

* Wed Dec 02 2015 Adam Huffman <bloch@verdurin.com> - 1.3.7.1-1
- Update to upstream bugfix release 1.3.7.1
- Remove upstreamed patch for lv2 libdir

* Sat Nov 21 2015 Adam Huffman <bloch@verdurin.com> - 1.3.7-1
- Update to upstream release 1.3.7
- Add readline BR
- Add patch for lv2 libdir on x86_64

* Sat Oct 10 2015 Adam Huffman <bloch@verdurin.com> - 1.3.6-1
- Update to upstream release 1.3.6

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 1.3.5.2-5
- Rebuilt for Boost 1.59

* Wed Aug 5 2015 Adam Huffman <bloch@verdurin.com> - 1.3.5.2-4
- Ensure all documentation files are included

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.3.5.2-2
- rebuild for Boost 1.58

* Sun Jul 19 2015 Adam Huffman >bloch@verdurin.com> - 1.3.5.2-1
- Update to upstream release 1.3.5.2

* Wed Jul 01 2015 Adam Huffman <bloch@verdurin.com> - 1.3.5.1-1
- Update to upstream release 1.3.5.1

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.3.4-2
- Rebuilt for GCC 5 C++11 ABI change

* Sun Apr 05 2015 Adam Huffman <bloch@verdurin.com> - 1.3.4-1
- Update to upstream release 1.3.4

* Sat Mar 07 2015 Adam Huffman <bloch@verdurin.com> - 1.3.3-2
- Include new SVG icon

* Fri Mar 06 2015 Adam Huffman <bloch@verdurin.com> - 1.3.3-1
- Update to upstream release 1.3.3

* Thu Feb 19 2015 Adam Huffman <bloch@verdurin.com> - 1.3.2-3
- patch to fix format security warnings

* Thu Feb 19 2015 Rex Dieter <rdieter@fedoraproject.org> 1.3.2-2
- rebuild (fltk)

* Sat Feb 07 2015 Adam Huffman <bloch@verdurin.com> - 1.3.2-1
- Update to 1.3.2

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 1.3.1-2
- Rebuild for boost 1.57.0

* Sat Dec 27 2014 Adam Huffman <bloch@verdurin.com> - 1.3.1-1
- Update to 1.3.1
- Add BR for lv2
- Add examples and lv2 directories

* Sun Oct 05 2014 Adam Huffman <bloch@verdurin.com> - 1.2.4-1
- Update to 1.2.4
- Notes file now replaced by Changelog

* Tue Sep 02 2014 Brendan Jones <brendan.jones.it@gmail.com> 1.2.3-2
- Correct notes

* Tue Sep 02 2014 Brendan Jones <brendan.jones.it@gmail.com> 1.2.3-1
- Update to 1.2.3

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jul 20 2014 Adam Huffman <bloch@verdurin.com> - 1.2.2-1
- Update to upstream 1.2.2
- Add appdata and new icon

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 30 2014 Adam Huffman <bloch@verdurin.com> - 1.2.1-1
- Update to 1.2.1
- Remove format-security patch, now that fix is in upstream
- Include README

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 1.2.0-3
- Rebuild for boost 1.55.0

* Mon May 19 2014 Peter Robinson <pbrobinson@fedoraproject.org> 1.2.0-2
- Re-add cflags patch to fix FTBFS

* Wed Mar 19 2014 Brendan Jones <brendan.jones.it@gmail.com> 1.2.0-1
- Update to 1.2.0

* Thu Aug  1 2013 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.0-4
- Use distro optflags rather than random project flags to fix FTBFS on ARM
- Modernise spec

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 1.1.0-3
- Rebuild for boost 1.54.0

* Thu May  9 2013 Adam Huffman <bloch@verdurin.com> - 1.1.0-2
- add cairo BR

* Thu May  9 2013 Adam Huffman <bloch@verdurin.com> - 1.1.0-1
- First build of new upstream release 1.1.0

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 29 2012 Adam Huffman <bloch@verdurin.com> - 1.0.0-3
- add BR for mesa-libGL-devel, needed by FLTK

* Mon Oct 29 2012 Adam Huffman <bloch@verdurin.com> - 1.0.0-2
- correct fix for FLTK header detection by cmake
- add pixmaps to files

* Mon Oct 29 2012 Adam Huffman <bloch@verdurin.com> - 1.0.0-1
- update to upstream 1.0.0 release
- fix FLTK detection, from Brendan Jones

* Sun Apr 15 2012 Adam Huffman <verdurin@fedoraproject.org> - 0.060.12-4
- add missing posttrans scriptlet

* Mon Feb 20 2012 Adam Huffman <verdurin@fedoraproject.org> - 0.060.12-3
- re-add downstream desktop file
- remove extra .bankdir file

* Sun Feb 19 2012 Adam Huffman <verdurin@fedoraproject.org> - 0.060.12-2
- use upstream desktop and icon files
- fix missing parameters in upstream desktop file
- actually remove FLTK patch

* Sun Jan  8 2012 Adam Huffman <verdurin@fedoraproject.org> - 0.060.12-1
- update to new upstream release 0.060.12
- remove FLTK 1.3 patch

* Mon Aug 29 2011 Adam Huffman <bloch@verdurin.com> - 0.060.10-2
- add patch from Brendan Jones to fix compilation with FLTK 1.3

* Sun Apr 17 2011 Adam Huffman <bloch@verdurin.com> - 0.060.10-1
- new upstream release with further licensing clarification

* Mon Apr 11 2011 Adam Huffman <bloch@verdurin.com> - 0.060.9-1
- new upstream release with licence clarification

* Sun Apr 10 2011 Adam Huffman <bloch@verdurin.com> - 0.060.8-2
- add COPYING and notes to docs

* Sat Apr  9 2011 Adam Huffman <bloch@verdurin.com> - 0.060.8-1
- new upstream release 0.060.8
- add boost-devel BR
- consistent use of macros
- fix directory permissions for banks/presets

* Sun Jun 20 2010 Adam Huffman <bloch@verdurin.com> - 0.058-1
- desktop file and icon added

* Sun May 16 2010 Adam Huffman <bloch@verdurin.com> - 0.056-1
- new upstream release, fixing PAD synth patch problems

* Sun Mar 28 2010 Adam Huffman <bloch@verdurin.com> - 0.055.6-1
- new upstream bugfilx release

* Sat Mar 13 2010 Adam Huffman <bloch@verdurin.com> - 0.055.3-1
- initial version

