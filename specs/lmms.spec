
%ifarch %ix86
%bcond_with  wine
%else
%bcond_with  wine
%endif

Name:           lmms
Version:        1.2.2
Release:        17%{?dist}
Summary:        Linux MultiMedia Studio
URL:            https://lmms.io/

# - lmms itself is GPLv2+
# - third party code used by plugins:
#   - drumsynth files: GPLv2+ or MIT
#   - for ladspa-effects (note that we only include cmt and swh in the
#     binary rpm (see below):
#     - caps: GPLv2
#     - cmt: GPLv2(+?)
#     - swh: GPLv2+
#     - tap: GPLv2+
#     - calf: GPLv2+ and LGPLv2+
#   - Portsmf (midi_import plugin): MIT
#   - Blip_Buffer and Gb_Snd_Emu (papu plugin): LGPLv2.1+
#   - reSID (sid plugin): GPLv2+
#   - basename.c (vst_base): Copyright only
#   - embedded zynaddsubfx plugin: GPLv2+
#     - fltk (zynaddsubfx): LGPLv2+, with exceptions (but we use
#       system's fltk)
License:        GPLv2+ and GPLv2 and (GPLv2+ or MIT) and GPLv3+ and MIT and LGPLv2+ and (LGPLv2+ with exceptions) and Copyright only

# original tarfile can be found here:
# https://github.com/LMMS/lmms/releases/download/v%%{version}/lmms_%%{version}.tar.xz
Source0:        lmms_%{version}.stripped.tar.xz

# we strip all .ogg / .wav / .mmp(z) files from the tarfile,
# until their license situation becomes clearer.
Source1:        README.fedora

# see #1575262
Source2:        lmms.metainfo.xml

# Fix for finding libwine
Patch0:         lmms-1.2.2_winelib.patch

# Pass LIB_SUFFIX
Patch1:         lmms-1.2.2_lib_suffix.patch

# Fix building against Carla 2.4.3, see #6395
Patch2:         lmms-1.2.2_carla_2.4.3.patch

# according to upstream we should at least support oss, alsa, and
# jack. output via pulseaudio has high latency, but we enable it
# nevertheless as it is standard on fedora now. portaudio support is
# beta (and causes crashes), sdl is rarely used (?).
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libsndfile-devel
BuildRequires:  fftw3-devel
BuildRequires:  fluidsynth-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libogg-devel
BuildRequires:  ladspa-devel
BuildRequires:  stk-devel
BuildRequires:  qt5-qt3d-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  xcb-util-devel
BuildRequires:  xcb-util-keysyms-devel
BuildRequires:  fltk-devel
BuildRequires:  fltk-fluid
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  bash-completion
BuildRequires:  Carla-devel
BuildRequires:  libappstream-glib
# require packages owning directories we use
Requires:  shared-mime-info
Requires:  hicolor-icon-theme

%if %{with wine}
BuildRequires:  wine-devel 
%endif

Requires:       ladspa-caps-plugins
Requires:       ladspa-tap-plugins
# this has been retired:
#Requires: ladspa-swh-plugins
Requires:       ladspa-calf-plugins
# the version included in lmms contains patches sent to, but not yet
# applied by cmt's upstream.
#Requires: ladspa-cmt-plugins

# the -vst subpackage can only be built on ix86, but is also usable
# (and thus should be installed) on x86_64.
#ifarch #ix86 x86_64
%if %{with wine}
Requires:       %{name}-vst = %{version}-%{release}
%endif

%global __provides_exclude_from ^%{_libdir}/lmms/.*$
%global __requires_exclude ^libvstbase\\.so.*$|^libZynAddSubFxCore\\.so.*$|^libcarlabase\\.so.*$|^libcarla_native-plugin\\.so.*$


%description
LMMS aims to be a free alternative to popular (but commercial and
closed- source) programs like FruityLoops/FL Studio, Cubase and Logic
allowing you to produce music with your computer. This includes
creation of loops, synthesizing and mixing sounds, arranging samples,
having fun with your MIDI-keyboard and much more...

LMMS combines the features of a tracker-/sequencer-program and those
of powerful synthesizers, samplers, effects etc. in a modern,
user-friendly and easy to use graphical user-interface.

Features

 * Song-Editor for arranging the song
 * creating beats and basslines using the Beat-/Bassline-Editor
 * easy-to-use piano-roll for editing patterns and melodies
 * instrument- and effect-plugins
 * support for hosting VST(i)- and LADSPA-plugins (instruments/effects)
 * automation-editor
 * MIDI-support


%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}


%description devel
The %{name}-devel package contains header files for
developing addons for %{name}.


%prep
%autosetup -p1 -n %{name}

# remove spurious x-bits
find . -type f -exec chmod 0644 {} \;

cp -a %{SOURCE1} README.fedora


%build
%cmake \
       -DWANT_SDL:BOOL=OFF \
       -DWANT_PORTAUDIO:BOOL=OFF \
       -DWANT_CAPS:BOOL=OFF \
       -DWANT_TAP:BOOL=OFF \
       -DWANT_CALF:BOOL=OFF \
       -DWINE_CXX_FLAGS:STRING="-fno-lto" \
       -DWANT_QT5:BOOL=ON \
%ifarch %ix86 x86_64
       -DWANT_VST:BOOL=ON \
%else
       -DWANT_VST:BOOL=OFF \
%endif
%ifarch x86_64
       -DWANT_VST_NOWINE:BOOL=ON \
       -DREMOTE_VST_PLUGIN_FILEPATH="../../lib/lmms/RemoteVstPlugin" \
%endif
       -DCMAKE_INSTALL_LIBDIR=%{_lib} \
       -Wno-dev

%cmake_build


%install
%cmake_install

# remove unneeded file
rm -f %{buildroot}%{_libdir}/libqx11embedcontainer.a

desktop-file-install --vendor '' \
        --add-category=Midi \
        --add-category=Sequencer \
        --add-category=X-Jack \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/%{name}.desktop

install -D -m 0644 -p %{SOURCE2} %{buildroot}%{_metainfodir}/%{name}.metainfo.xml
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml


%files
%doc README.md README.fedora
%doc doc/AUTHORS doc/CONTRIBUTORS
%license LICENSE.txt
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.{png,svg}
%{_datadir}/icons/hicolor/*/mimetypes/application-x-%{name}-project.{png,svg}
%{_metainfodir}/%{name}.metainfo.xml
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/%{name}
%{_mandir}/man*/%{name}*


%files devel
%{_includedir}/%{name}


%if %{with wine}

%package vst
Summary:        VST hosting plugin for %{name}

%description vst
This package contains the necessary files to host VST plugins.

%files vst
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/RemoteVstPlugin*

%endif


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild
- Disable wine vst due to libwine.so.1 being removed in wine version 8.3
  see https://bugs.winehq.org/show_bug.cgi?id=54635 and https://github.com/LMMS/lmms/issues/6672
  (copied from https://build.opensuse.org/package/view_file/openSUSE:Backports:SLE-15-SP6/lmms/)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 14 2022 Jan Grulich <jgrulich@redhat.com> - 1.2.2-11
- Rebuild (qt5)

* Tue May 24 2022 Thomas Moschny <thomas.moschny@gmx.de> - 1.2.2-10
- Add patch to fix building with Carla 2.4.3.

* Tue May 17 2022 Jan Grulich <jgrulich@redhat.com> - 1.2.2-9
- Rebuild (qt5)

* Tue Mar 08 2022 Jan Grulich <jgrulich@redhat.com> - 1.2.2-8
- Rebuild (qt5)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Thomas Moschny <thomas.moschny@gmx.de> - 1.2.2-5
- Rebuild against newer fluidsynth.

* Sun May 23 2021 Thomas Moschny <thomas.moschny@gmx.de> - 1.2.2-4
- Switch to Qt5.
- Fix search path for RemoteZynAddSubFx plugin.
- Update patch for wine 6.8.

* Mon May 10 2021 Thomas Moschny <thomas.moschny@gmx.de> - 1.2.2-3
- Install appdata file (#1575262).

* Mon May 10 2021 Thomas Moschny <thomas.moschny@gmx.de> - 1.2.2-2
- Filter unwanted requirements.
- VST fixes.
- Enable Carla plugins.

* Sat May  8 2021 Thomas Moschny <thomas.moschny@gmx.de> - 1.2.2-1
- Update to 1.2.2.
- Remove obsolete patches.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Oct 03 2020 Thomas Moschny <thomas.moschny@gmx.de> - 1.1.3-20
- Rebuilt for newer stk.

* Wed Aug  5 2020 Thomas Moschny <thomas.moschny@gmx.de> - 1.1.3-19
- Use %%cmake macros.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-18
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 17 2020 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.1.3-16
- Rebuild against fluidsynth2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May  1 2019 Thomas Moschny <thomas.moschny@gmx.de> - 1.1.3-13
- Use bundled swh ladspa plugins (#1703804).

* Fri Feb 15 2019 Thomas Moschny <thomas.moschny@gmx.de> - 1.1.3-12
- Remove obsolete patch, fix FTBFS (#1675328).

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov  5 2018 Thomas Moschny <thomas.moschny@gmx.de> - 1.1.3-10
- Add patch for FTBFS with wine 3 (#1604715).

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 18 2018 Thomas Moschny <thomas.moschny@gmx.de> - 1.1.3-8
- Add patch fixing linkage of the Vestige module (#1388466).
- Add BR on gcc and g++.

* Tue Feb 13 2018 Thomas Moschny <thomas.moschny@gmx.de> - 1.1.3-7
- Add patch for building with gcc8.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 30 2015 Thomas Moschny <thomas.moschny@gmx.de> - 1.1.3-1
- Update to 1.1.3.
- Update upstream URL.
- Rebase patches.
- Add dependency on fltk-fluid.
- Mark license with %%license.

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.3-6
- Rebuilt for GCC 5 C++11 ABI change

* Thu Feb 19 2015 Rex Dieter <rdieter@fedoraproject.org> 1.0.3-5
- lmms-1.0.3-no_werror.patch

* Thu Feb 19 2015 Rex Dieter <rdieter@fedoraproject.org> 1.0.3-4
- rebuild (fltk)

* Mon Sep 08 2014 Rex Dieter <rdieter@fedoraproject.org> 1.0.3-3
- update mime scriptlet

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Aug 10 2014 Thomas Moschny <thomas.moschny@gmx.de> - 1.0.3-1
- Update to 1.0.3.
- Rebase patches, drop obsolete patches.
- Filter internal provides.
- Spec file cleanups.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Jul 28 2013 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.15-1
- Update to 0.4.15.
- Modernize spec file.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec 18 2012 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.13-4
- Rebuilt for new STK.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.13-2
- Rebuilt for c++ ABI breakage

* Wed Feb  8 2012 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.13-1
- Update to 0.4.13.

* Sat Jan 14 2012 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.12-1
- Update to 0.4.12.
- Add patch for gcc47 compatibility.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Jun 11 2011 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.11-1
- Update to 0.4.11.

* Sat May 28 2011 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.10-3
- Rebuild for new fltk.

* Thu Feb 10 2011 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.10-2
- The remote_vst_plugin has been renamed to RemoteVstPlugin, fix
  libexecdir patch and specfile.

* Wed Feb  9 2011 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.10-1
- Update to 0.4.10, rebase patches.
- Add patch for bz 672918.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan  7 2011 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.9-2
- Add patch to use system's fltk.
- Add BR to fltk-devel.

* Sat Dec 18 2010 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.9-1
- Update to 0.4.9, rebase patches.

* Sat Sep  4 2010 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.8-1
- Update to 0.4.8, rebase patches.
- Remove comments about minixml, no longer bundled.

* Wed Aug 18 2010 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.7-1
- Update to 0.4.7.
- Remove obsolete patch, rebase other patches.
- Specfile fixes.

* Tue Feb 16 2010 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.6-4
- Rebuilt for stk update.

* Wed Feb 10 2010 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.6-3
- Add patch to fix DSO issue.

* Fri Jan 15 2010 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.6-2
- Let cmake create rpaths where needed. This should fix bz 555852
  (zynaddsubfx gui not showing up). In order to make that work
  properly, drop the libdir patch, and set CMAKE_INSTALL_LIBDIR
  instead. Thanks to Rex Dieter for helping with that issue.

* Wed Dec 30 2009 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.6-1
- Update to 0.4.6.
- Rebase patches.
- Minor specfile fixes.

* Wed Sep 23 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.4.5-2
- Update desktop file according to F-12 FedoraStudio feature

* Fri Sep  4 2009 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.5-1
- Udate to 0.4.5.
- Rebase patches, and drop fltk patches not needed anymore.
- Add a dependency on the Calf LADSPA plugins.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 17 2009 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.4-1
- Update to 0.4.4.
- Need to borrow patches for embedded fltk from the fltk package.
- Update detailed license information in the spec file.
- Update patches.

* Mon Mar  9 2009 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.3-1
- Update to 0.4.3.
- Remove lmms-0.4.2-gcc44.patch (fixed upstream).
- Add README.fedora.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 18 2009 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.2-4
- Re-add drumsynth files and adjust License tag.

* Thu Feb 12 2009 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.2-3
- Add patch for gcc44 issues.

* Wed Feb 11 2009 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.2-2
- Strip files with unclear licensing from the tarfile.
- Regenerate patches.
- Add BR on libsamplerate-devel.

* Thu Jan 22 2009 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.2-1
- Update to 0.4.2.

* Sun Nov  2 2008 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.0-1
- Updated to 0.4.0 final.
- Removed patches already applied upstream, adjusted the remaining.

* Fri Oct 24 2008 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.0-0.2.rc3
- Add patch to fix libdir on ppc64.

* Tue Oct 21 2008 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.0-0.1.rc3
- Update to 0.4.0rc3.
- Don't build remote_vst_plugin.exe on x86_64, but do build all other
  parts of the VST host there.

* Fri Sep 26 2008 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.0-0.1.rc2
- Update to 0.4.0rc2.
- Use oss, jack, alsa and pulseaudio backends and disable other
  backends.
- Depend on the system packages for all but one of the ladspa plugins
  instead of building our own versions.

* Thu Sep 18 2008 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.0-0.1.rc1
- Update to 0.4.0rc1. Upstream uses cmake and qt4 now.
- Updated license tag.
- Drop festival dependency, and add fftw and fluidsynth.
- Remove patches no longer necessary.
- VST now also builds on x86_64.

* Wed Sep 17 2008 Thomas Moschny <thomas.moschny@gmx.de> - 0.3.2-3
- Add stk-devel BR.
- Use libdir patch from upstream bug tracker.
- Use xdg-open instead of x-www-browser.

* Wed Jun 25 2008 Thomas Moschny <thomas.moschny@gmx.de> - 0.3.2-2
- Update license tag.
- Add patch to fix plugin dir on 64bit archs.
- Add ladspa-caps-plugins dependency.
- Suggestions from the review:
  * Simplify configure step.
  * Fix sf.net download link.
  * Add patch to let configure find the qt translations.
  * Link icon to _datadir/pixmaps.

* Mon Apr 21 2008 Thomas Moschny <thomas.moschny@gmx.de> - 0.3.2-1
- New package.
