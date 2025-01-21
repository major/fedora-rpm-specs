Summary:        Real-time software synthesizer
Name:           zynaddsubfx
Version:        3.0.6
Release:        9%{?dist}
# Source is a collective work, distributed by
# Automatically converted from old format: GPLv2 and GPLv2+ - review is highly recommended.
License:        GPL-2.0-only AND GPL-2.0-or-later
URL:            http://zynaddsubfx.sourceforge.net
Source0:        http://download.sf.net/sourceforge/zynaddsubfx/zynaddsubfx-%{version}.tar.bz2
# We cannot build this from source since Fedora's texlive is too old
Patch0:         zynaddsubfx-buildflags.patch
# Do not ask for cortex-a9 which conflicts with the armv7a baseline
Patch1:         zynaddsubfx-cortex.patch
Patch2:         %{name}-missing-cstdint.patch

Requires:       hicolor-icon-theme
Requires:       %{name}-common = %{version}-%{release}

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  alsa-lib-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  dssi-devel
BuildRequires:  fftw3-devel
BuildRequires:  fltk-devel
BuildRequires:  fltk-fluid
BuildRequires:  non-ntk-devel
BuildRequires:  ImageMagick
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  lash-devel
BuildRequires:  mxml-devel
BuildRequires:  portaudio-devel
BuildRequires:  zlib-devel
BuildRequires:  liblo-devel
BuildRequires:  libXpm-devel

# Build dumps core on i686
# Bug 2297277
ExcludeArch:	i686

%description
ZynAddSubFX is an open source software synthesizer capable of making a
countless number of instrument sounds. It is microtonal, and the instruments
made by it sounds like those from professional keyboards. The program has
effects like Reverb, Echo, Chorus, Phaser...

This package includes the standalone implementation of the synthesizer.

%package common
Summary:        Common files for ZynAddSubFX synthesizers
BuildArch:      noarch

%description common
ZynAddSubFX is an open source software synthesizer capable of making a
countless number of instrument sounds. It is microtonal, and the instruments
made by it sounds like those from professional keyboards. The program has
effects like Reverb, Echo, Chorus, Phaser...

This package includes the common files needed by the implementations of the
synthesizer.

%package dssi
Summary:        Real-time software synthesizer for DSSI
Requires:       %{name}-common = %{version}-%{release}
Requires:       dssi

%description dssi
ZynAddSubFX is an open source software synthesizer capable of making a
countless number of instrument sounds. It is microtonal, and the instruments
made by it sounds like those from professional keyboards. The program has
effects like Reverb, Echo, Chorus, Phaser...

This package includes the DSSI implementation of the synthesizer.

%package lv2
Summary:        %{name} LV2 plugins
Requires:       %{name}-common = %{version}-%{release}
Requires:       lv2

%description lv2
ZynAddSubFX is an open source software synthesizer capable of making a
countless number of instrument sounds. It is microtonal, and the instruments
made by it sounds like those from professional keyboards. The program has
effects like Reverb, Echo, Chorus, Phaser...

This package includes the LV2 implementation of the synthesizer.

%package vst
Summary:        %{name} VST plugins
Requires:       %{name}-common = %{version}-%{release}

%description vst
ZynAddSubFX is an open source software synthesizer capable of making a
countless number of instrument sounds. It is microtonal, and the instruments
made by it sounds like those from professional keyboards. The program has
effects like Reverb, Echo, Chorus, Phaser...

This package includes the VST implementation of the synthesizer.

%prep
%autosetup -p 1

# Fix encoding
for i in AUTHORS.txt; do
   iconv -f iso8859-1 -t utf8 $i -o tmpfile
   touch -r $i tmpfile
   mv -f tmpfile $i
done


%build
%cmake \
  -DDefaultOutput=jack -DPluginLibDir=%{_libdir} \
  -DBASHCOMP_PKG_PATH=%{_datadir}/bash-completion/completions \
%ifarch %{ix86} x86_64
  -DX86Build=ON \
%endif
  %{nil}

%cmake_build

# build external programs
%make_build -C ExternalPrograms/Controller
%make_build -C ExternalPrograms/Spliter

%install
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
%cmake_install

mkdir -p %{buildroot}%{_datadir}/%{name}

cp -rp instruments/examples instruments/banks %{buildroot}%{_datadir}/%{name}

# install external programs
pushd ExternalPrograms
   install -m 0755 Controller/controller %{buildroot}%{_bindir}/zynaddsubfx-controller
   install -m 0755 Spliter/spliter %{buildroot}%{_bindir}/zynaddsubfx-spliter
popd

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-jack.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-alsa.desktop

# We are including these in the common package below
rm -fr %{buildroot}%{_datadir}/doc/%{name}/
install -d -m 0755 %{buildroot}%{_libdir}/%{name}

%files
%{_bindir}/*
%{_datadir}/applications/%{name}*.desktop
%{_datadir}/pixmaps/zynaddsubfx.svg
%{_datadir}/pixmaps/zynaddsubfx.png
%{_datadir}/bash-completion/completions/%{name}

%files common
%doc AUTHORS.txt
%license COPYING
%{_datadir}/%{name}/

%files dssi
%{_libdir}/dssi/*.so

%files lv2
%{_libdir}/lv2/*

%files vst
%{_libdir}/vst/*.so

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 07 2024 Miroslav Suchý <msuchy@redhat.com> - 3.0.6-8
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jul 11 2024 Guido Aulisi <guido.aulisi@gmail.com> - 3.0.6-6
- Exclude i686 because build system dumps core #2297277

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jul 23 2023 Guido Aulisi <guido.aulisi@gmail.com> - 3.0.6-4
- Fix FTBFS in Fedora rawhide: missing cstdint

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 03 2022 Guido Aulisi <guido.aulisi@gmail.com> - 3.0.6-1
- Update to 3.0.6

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 3.0.5-10
- Rebuilt for removed libstdc++ symbol (#1937698)

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 31 2020 Jeff Law <law@redhat.com> - 3.0.5-8
- Do not ask for cortex-a9 which conflicts with baseline armv7a
- Re-enable LTO

* Mon Aug 10 2020 Guido Aulisi <guido.aulisi@gmail.com> - 3.0.5-7
- Fix FTBFS in Fedora rawhide/f33 (#1865663)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Guido Aulisi <guido.aulisi@gmail.com> - 3.0.5-3
- Rebuilt for new non-ntk

* Wed Aug 28 2019 Guido Aulisi <guido.aulisi@gmail.com> - 3.0.5-2
- Build without non-ntk
- Install bash completion file

* Sun Jul 28 2019 Guido Aulisi <guido.aulisi@gmail.com> - 3.0.5-1
- Update to 3.0.5

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Nov 18 2017 Brendan Jones <brendan.jones.it@gmail.com> - 3.0.2-1
- Update to 3.0.2

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 18 2015 Richard Hughes <rhughes@redhat.com> - 2.4.4-7
- Remove no longer required AppData file

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.4.4-5
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 2.4.4-4
- Add an AppData file for the software center

* Thu Feb 19 2015 Rex Dieter <rdieter@fedoraproject.org> 2.4.4-3
- rebuild (fltk)

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 29 2014 Brendan Jones <brendan.jones.it@gmail.com> 2.4.4-1
- Update to 2.4.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 10 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 2.4.3-3
- Remove vendor tag from desktop file as per https://fedorahosted.org/fesco/ticket/1077

* Sun Oct 28 2012 Brendan Jones <brendan.jones.it@gmail.com> 2.4.3-2
- Mov ebanks/examples

* Thu Oct 25 2012 Brendan Jones <brendan.jones.it@gmail.com> 2.4.3-1
- New upstream release

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar 08 2012 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 2.4.2-1
- 2.4.2

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-5
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jun 26 2011 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 2.4.1-3
- Fix FTBFS RHBZ#715835

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 2.4.1-1
- Version update
- Build the DSSI plugin since it is fixed now
- Put the common files between standalone ad DSSI synths in a common package
- Drop patches that are not necessary anymore
- Fix .desktop file

* Wed Feb 10 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 2.4.0-3
- Fix DSO-linking failure

* Tue Sep 08 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 2.4.0-2
- Bugfix: presets and parameters don't load on ix86 (RHBZ #518755)

* Thu Aug 06 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 2.4.0-1
- Update to 2.4.0
- Update scriptlets according to new guidelines
- Update the .desktop file
- Use Fedora specific flags during compilation
- License is GPLv2+ (just run the program on the command line :))

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Aug 11 2008 Jason L Tibbitts III <tibbs@math.uh.edu> - 2.2.1-19
- Fix license tag.

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.2.1-18
- Autorebuild for GCC 4.3

* Wed Oct 10 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 2.2.1-17
- added tweaked unzombify patch by Lars Luthman (patch3), see:
  http://sourceforge.net/tracker/index.php?func=detail&aid=1498438&group_id=62934&atid=502314

* Tue Oct 09 2007 Anthony Green <green@redhat.com> 2.2.1-16
- Rebuilt for new lash again.

* Mon Oct 08 2007 Anthony Green <green@redhat.com> 2.2.1-15
- Rebuilt for new lash.

* Wed Mar 14 2007 Anthony Green <green@redhat.com> 2.2.1-14
- Rebuild with new ImageMagick for working desktop icons.

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 2.2.1-13
 - rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Tue Sep 19 2006 Anthony Green <green@redhat.com>  2.2.1-12
- Fix release tag.

* Mon Sep 18 2006 Anthony Green <green@redhat.com>  2.2.1-11.1
- Rebuild.

* Wed Aug 30 2006 Anthony Green <green@redhat.com>  2.2.1-11
- Fix ppc problem (in a different way).

* Wed Aug 30 2006 Anthony Green <green@redhat.com>  2.2.1-10
- Fix ppc problem.  Add perl dependency.

* Wed Aug 30 2006 Anthony Green <green@redhat.com>  2.2.1-9
- Only build for x86 and x86-64 for now.  (ppc build problem)

* Wed Aug 30 2006 Anthony Green <green@redhat.com>  2.2.1-8
- Depend on hicolor-icon-theme.

* Sat Aug 26 2006 Anthony Green <green@redhat.com>  2.2.1-7
- Add dist tag to release version.
- Tidy up description.
- Use standard scriptlets in %%post/%%postun.

* Thu Jul 20 2006 Anthony Green <green@redhat.com>  2.2.1-6
- Fix compile options and remove rpath usage (bug in fltk-config).

* Sat Jul 15 2006 Anthony Green <green@redhat.com>  2.2.1-5
- First Fedora Extras build.
- Fix Source0 permissions.
- Add desktop-file-utils requirements.
- Tweak macro usage and .desktop file.
- Convert and install icons.  Add post(un) install scripts.
- Add ImageMagick BuildRequires.

* Mon May  8 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 2.2.1-4
- added lash patch (http://www.student.nada.kth.se/~d00-llu/programming.php)

* Sat May  6 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 2.2.1-3
- add Planet CCRMA categories to desktop file

* Fri Mar 31 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- build on fc5

* Fri Sep 23 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 2.2.1-2
- rebuilt with new version of mxml (2.2.2)
- added specific requires for mxml version

* Tue May  3 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 2.2.1-1
- updated to 2.2.1

* Fri Apr  8 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 2.2.0-1
- updated to 2.2.0

* Mon Feb  7 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 2.1.1-2
- fixed microtuning bug (patch from Paul Nasca)

* Sun Oct  3 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 2.1.1-1
- updated to 2.1.1

* Fri Oct  1 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 2.1.0-1
- updated to 2.1.0

* Fri Aug 27 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 2.0.0-1
- updated to 2.0.0 final
- readded examples directory to the file list
- installed banks and presets
- compiled and installed "controller" and "spliter"

* Wed Aug  4 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 2.0.0-0.pre2.1
- updated to latest prerelease
- added mxml build dependency, updated requirements to fftw3
- no documentation or examples for now

* Sat Nov  8 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.4.3-1
- spec file tweaks

* Mon Sep  1 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.4.3-1
- updated to 1.4.3, added release tag

* Fri Jul 25 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.4.2-1
- updated to 1.4.2

* Thu May  8 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.4.1-1
- updated to 1.4.1 (docs are still 1.4.0)

* Tue May  6 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.4.0-1
- updated to 1.4.0

* Tue Apr  8 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.2.1-2
- rebuilt for newer version of fftw

* Tue Apr  8 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.2.1-1
- udpated to 1.2.1

* Wed Apr  2 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.2.0-2
- rebuild for jack 0.66.3, added explicit requires for it

* Fri Mar 21 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.2.0-1
- updated to 1.2.0

* Thu Mar  6 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.0.9-2
- rebuilt due to changed fltk (from 1.1.0rc3 to 1.1.3)
- commented out deprecated jack_set_buffer_size_callback() call

* Mon Feb 24 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.0.9-1
- updated to 1.0.9

* Fri Feb 14 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.0.8-1
- updated to 1.0.8

* Thu Feb  6 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.0.7-1
- updated to 1.0.7

* Sun Jan 26 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.0.5-1
- Initial build.
