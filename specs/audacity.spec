# Compile options:
# invoke with: rpmbuild --with ffmpeg --with local_ffmpeg audacity.spec to use local ffmpeg
%bcond_without  ffmpeg
%bcond_with     local_ffmpeg

#global commit0 53a5c930a4b5b053ab06a8b975458fc51cf41f6c
#global shortcommit0 #(c=#{commit0}; echo ${c:0:7})

# Ignore these libraries because they are internal-only and should never be exposed in the RPM database
%global __requires_exclude ^lib-.*.so
%global __provides_exclude ^lib-.*.so

Name: audacity

Version: 3.7.1
Release: 2%{?dist}
Summary: Multitrack audio editor
License: GPL-2.0-or-later AND GPL-3.0-only AND CC-BY-3.0
URL:     https://www.audacityteam.org/

Source0: https://github.com/audacity/audacity/releases/download/Audacity-%{version}/%{name}-sources-%{version}.tar.gz
Source1: https://github.com/audacity/audacity/releases/download/Audacity-%{version}/%{name}-manual-%{version}.tar.gz

# Use the X11 backend in GTK to make the waveform viewer work properly (RHBZ: 2024019)
Patch0: gdk_x11_backend.patch

Patch2: fix_data_path.patch

BuildRequires: cmake
BuildRequires: gettext-devel

%if 0%{?rhel} == 7
BuildRequires: devtoolset-7-toolchain, devtoolset-7-libatomic-devel
%endif
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: chrpath

BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils
BuildRequires: expat-devel
BuildRequires: flac-devel
BuildRequires: git
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: ladspa-devel
BuildRequires: lame-devel
BuildRequires: libid3tag-devel
BuildRequires: libmpg123-devel
BuildRequires: taglib-devel
%if 0%{?rhel} && 0%{?rhel} == 8
#note: epel-8 currently doesn't have twolame-devel.
%else
BuildRequires: twolame-devel
%endif
BuildRequires: libogg-devel
BuildRequires: libsndfile-devel
BuildRequires: libvorbis-devel
BuildRequires: libuuid-devel
BuildRequires: portaudio-devel >= 19-16
BuildRequires: portmidi-devel
BuildRequires: soundtouch-devel
BuildRequires: soxr-devel
BuildRequires: sqlite-devel >= 3.32
BuildRequires: vamp-plugin-sdk-devel >= 2.0
BuildRequires: wavpack-devel
BuildRequires: zip
BuildRequires: zlib-devel
BuildRequires: python3
BuildRequires: rapidjson-devel
BuildRequireS: opusfile-devel
BuildRequires: libjpeg-turbo-devel turbojpeg
# We need /usr/bin/wx-config so that configure can detect the wx-config version:
#if 0#{?rhel} || 0#{?fedora} < 28
#BuildRequires: wxGTK3-devel
#endif
# But we will actually use the --toolkit=gtk2 version using --with-wx-version
#BuildRequires: compat-wxGTK3-gtk2-devel
BuildRequires: wxGTK-devel
%if 0%{?rhel} >= 8 || 0%{?fedora}
BuildRequires: libappstream-glib
%endif

%if %{with ffmpeg}
%if ! %{with local_ffmpeg}
BuildRequires: ffmpeg-free-devel
%endif
%endif

# LV2 interface and the plugins used
BuildRequires: lv2-devel >= 1.16
BuildRequires: lilv-devel >= 0.24.6
BuildRequires: serd-devel >= 0.30.2
BuildRequires: sord-devel >= 0.16.4
BuildRequires: sratom-devel >= 0.6.4
BuildRequires: suil-devel  >= 0.10.6

# For new symbols in portaudio
Requires:      portaudio%{?_isa} >= 19-16

# We force the GDK backend to be X11 in the launcher, so we need to ensure we have Xwayland available
%if !0%{?flatpak}
Requires:      xorg-x11-server-Xwayland
%endif

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86} s390x

%description
Audacity is a cross-platform multitrack audio editor. It allows you to
record sounds directly or to import files in various formats. It features
a few simple effects, all of the editing features you should need, and
unlimited undo. The GUI was built with wxWidgets and the audio I/O
supports PulseAudio, OSS and ALSA under Linux.

%package manual
Summary: Manual for Audacity - Offline Install
BuildArch: noarch
# -manual suits either audacity or audacity-freeworld; both create the path:
%if 0%{?fedora} || 0%{?rhel} >= 9
Requires: (audacity or audacity-freeworld)
%else
Requires: /usr/bin/audacity
%endif

%description manual
Audacity Manual can be installed locally if preferred, or accessed on-line
if internet connection is available.
For the most up to date manual content, use the on-line manual.


%prep
%setup -q -n %{name}-sources-%{version}

#%%patch -P 0 -p0
%patch -P 2 -p1

# fix building translations with gettext-0.22 (#2225711), fixed in 3.4
sed -i -e 's|%hs|%s|g' locale/*.po

%build
export CFLAGS="$CFLAGS -std=gnu17"
%if 0%{?rhel} == 7
export WX_CONFIG=wx-config-3.0
%endif

%if 0%{?rhel} == 7
. /opt/rh/devtoolset-7/enable
%endif

%cmake \
    -DwxWidgets_CONFIG_EXECUTABLE="$(which wx-config-3.2)" \
    -DAUDACITY_BUILD_LEVEL:STRING=2 \
    -Daudacity_conan_enabled=Off \
    -Daudacity_has_networking=Off \
    -Daudacity_has_crashreports=Off \
    -Daudacity_has_updates_check=Off \
    -Daudacity_has_sentry_reporting=Off \
    -Daudacity_has_vst3=Off \
    -Daudacity_lib_preference=system \
    -Daudacity_obey_system_dependencies=On \
    -Daudacity_use_wxwidgets=system \
    -Daudacity_use_uuid=system \
    -Daudacity_use_sqlite=system \
    -Daudacity_use_libsndfile=system \
    -Daudacity_use_soxr=system \
    -Daudacity_use_lame=system \
%if 0%{?rhel} == 8
    -Daudacity_use_twolame=off \
%else
    -Daudacity_use_twolame=system \
%endif
    -Daudacity_use_libflac=system \
    -Daudacity_use_ladspa=on \
    -Daudacity_use_libvorbis=system \
    -Daudacity_use_libid3tag=system \
    -Daudacity_use_expat=system \
    -Daudacity_use_soundtouch=system \
    -Daudacity_use_vamp=system \
    -Daudacity_use_lv2=system \
    -Daudacity_use_portaudio=system \
    -Daudacity_use_midi=system \
    -Daudacity_use_libogg=system \
%if %{with ffmpeg}
%if ! %{with local_ffmpeg}
    -Daudacity_use_ffmpeg=loaded \
%endif
%else
    -Daudacity_use_ffmpeg=off \
%endif
    -Daudacity_use_portsmf=local \
    -Daudacity_use_sbsms=local \
    -Daudacity_use_wavpack=system \

%cmake_build


%install
%cmake_install

rm -Rf %{buildroot}%{_datadir}/%{name}/include
rm -Rf %{buildroot}%{_bindir}/../%{name}

# Remove the RPATH from all the private libraries provided with Audacity and
# make them all executable so that debug symbol extraction happens.
# CMake could do this on its own using the install target for the library,
# but the Audacity build system manually copies around the libraries so it
# doesn't use the install target. This is very involved to fix in the code,
# so this work around is easier and more maintainable than patching the build
# system.
pushd %{buildroot}%{_libdir}/%{name}
for libFile in *;
do
    if [[ ! -d $libFile ]];
    then
        chrpath --delete $libFile
        chmod 755 $libFile
    fi
done
popd

pushd %{buildroot}%{_libdir}/%{name}/modules
for libFile in *;
do
    if [[ ! -d $libFile ]];
    then
        chrpath --delete $libFile
        chmod 755 $libFile
    fi
done
popd


%if 0%{?rhel} >= 8 || 0%{?fedora}
if appstream-util --help | grep -q replace-screenshots ; then
# Update the screenshot shown in the software center
#
# NOTE: It would be *awesome* if this file was pushed upstream.
#
# See http://people.freedesktop.org/~hughsient/appdata/#screenshots for more details.
#
appstream-util replace-screenshots %{buildroot}%{_metainfodir}/audacity.appdata.xml \
  https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/audacity/a.png
fi
%endif

# audacity manual must be extracted to correct location
pushd %{buildroot}%{_datadir}/%{name}
gzip -dc %{SOURCE1} | tar -xvvf -
#unzip %{SOURCE1}
#mv %{name}-manual-%{version}/* .
mv help/manual/* .
#rmdir %{name}-manual-%{version}
rmdir -p help/manual
popd

%{find_lang} %{name}

desktop-file-install --dir %{buildroot}{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/audacity.desktop

mkdir %{buildroot}%{_datadir}/doc/%{name}/nyquist
cp -pr lib-src/libnyquist/nyquist/license.txt %{buildroot}%{_datadir}/doc/%{name}/nyquist
cp -pr lib-src/libnyquist/nyquist/Readme.txt %{buildroot}%{_datadir}/doc/%{name}/nyquist
rm %{buildroot}%{_datadir}/doc/%{name}/LICENSE.txt

%files -f %{name}.lang
%{_bindir}/%{name}
%{_libdir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/EffectsMenuDefaults.xml
%{_datadir}/%{name}/nyquist/
%{_datadir}/%{name}/plug-ins/
%exclude %{_datadir}/%{name}/favicon.ico
%exclude %{_datadir}/%{name}/index.html
%exclude %{_datadir}/%{name}/quick_help.html
%exclude %{_datadir}/%{name}/man/
%exclude %{_datadir}/%{name}/m/
%{_mandir}/man*/*
%{_metainfodir}/%{name}.appdata.xml
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/icons/hicolor/*/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/mime/packages/*
%{_datadir}/doc/%{name}
%license LICENSE.txt

%files manual
%{_datadir}/%{name}/favicon.ico
%{_datadir}/%{name}/index.html
%{_datadir}/%{name}/quick_help.html
%{_datadir}/%{name}/man/
%{_datadir}/%{name}/m/

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jan 07 2025 Yaakov Selkowitz <yselkowi@redhat.com> - 3.7.1-1
- 3.7.1

* Wed Sep 25 2024 Dominik Mierzejewski <dominik@greysector.net> - 3.5.1-4
- Rebuilt for FFmpeg 7

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri May 03 2024 Robert-André Mauchin <zebob.m@gmail.com> - 3.5.1-2
- Add patch for FFMPEG 7 compatibility

* Wed Apr 24 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.5.1-1
- 3.5.1

* Mon Apr 22 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.5.0-1
- 3.5.0

* Tue Jan 30 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.4.2-1
- 3.4.2

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 01 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 3.3.3-1
- Update to 3.3.3

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Mar 30 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 3.1.3-9
- Added patch to fix GCC 13 build error (Fixes RHBZ: 2171444)

* Sun Mar 05 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.1.3-8
- migrated to SPDX license

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep 15 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.3-6
- Patch to lv2 header patch change due to meson build change
- Rebuild for new FLAC

* Fri Jul 22 2022 Scott Talbert <swt@techie.net> - 3.1.3-5
- Rebuild for wxGTK 3.2.0

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 10 2022 Scott Talbert <swt@techie.net> - 3.1.3-3
- Rebuild for wxGTK 3.1.7

* Tue Apr 12 2022 Scott Talbert <swt@techie.net> - 3.1.3-2
- Rebuild for wxGTK 3.1.6

* Sun Apr 10 2022 Ian McInerney <ian.s.mcinerney@ieee.org> - 3.1.3-1
- Update to upstream release 3.1.3
- Remove conditionals for Fedora 33 (it is now EOL)
- Unbundle sqlite and use the system version (rhbz: #1973455)
- Force X11 backend in GTK to fix cursor scroll (rhbz: #2024019)
- Fix builds when using wxWidgets 3.1.6 (rhbz: #2072823)

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 18 2021 Ian McInerney <ian.s.mcinerney@ieee.org> - 3.0.2-4
- Disable rpath checking until upstream fixes the rpath issues

* Thu Jun 17 2021 Ian McInerney <ian.s.mcinerney@ieee.org> - 3.0.2-4
- Fix detection of Jack development package (fixes rhbz #1972963)
- Add packages needed for the LV2 interface to use the system libraries
- Temporarily disable the rpath checks until upstream fixes it
- Fix CVE-2020-1867 (fixes rhbz #1904016)

* Wed May 05 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.0.2-3
- wxGTK rebuild.

* Mon Apr 19 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.0.2-2
- Fix ffmpeg typo.

* Mon Apr 19 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.0.2-1
- 3.0.2

* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 3.0.0-2
- Rebuilt for removed libstdc++ symbol (#1937698)

* Wed Mar 17 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.0.0-1
- 3.0.0

* Thu Feb 11 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.4.2-4
- Use system for lv2 and midi.

* Tue Feb 09 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.4.2-3
- Specify system ogg.

* Tue Feb 09 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.4.2-2
- Python2 -> 3

* Sat Jan 2 2021 Brandon Nielsen <nielsenb@jetfuse.net> - 2.4.2-1
- Cleanup unsupported Fedora version conditionals
- Update to 2.4.2 / cmake
- Make manual own its own folder
- Get rid of realname definition
- Reviewed, tested, committed, and built by Gwyn Ciesla, gwync@protonmail.com

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 15 2020 Ian McInerney <Ian.S.McInerney@ieee.org> - 2.3.3-6
- Fix incorrect appdata.xml type tag (bug #1810509)

* Sun May 3 2020 Ian McInerney <Ian.S.McInerney@ieee.org> - 2.3.3-5
- Fix installation location of manual package (bug #1830445)
- Add GDK_BACKEND=x11 to audacity.desktop exec line (bug #1798987)

* Mon Apr 6 2020 Ian McInerney <Ian.S.McInerney@ieee.org> - 2.3.3-4
- Fix changelog date from last entry

* Wed Apr 1 2020 Ian McInerney <Ian.S.McInerney@ieee.org> - 2.3.3-3
- Use legacy -fcommon support with GCC10.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 23 2019 David Timms <iinet.net.au@dtimms> - 2.3.3-1
- Update to Audacity 2.3.3.
- Modify wxWidgets build require to wxGTK3 (gtk3 version).
- Modify libdir patch for 2.3.3.
- Fix -manual file archive dropping the leading help/ in path.
- Disable twolame for EPEL-8 as the -devel package isn't available.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun  4 2019 David Timms <iinet.net.au@dtimms> - 2.3.2-1
- Update to Audacity 2.3.2 release.
- Rebase audacity-2.3.2-libdir.patch.
- Fix -manual placing files in extra help/manual path.

* Fri Apr 19 2019 David Timms <iinet.net.au@dtimms> - 2.3.1-1
- Update to Audacity 2.3.1 release.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct  1 2018 David Timms <iinet.net.au@dtimms> - 2.3.0-1
- Update to Audacity 2.3.0 release.

* Thu Sep 20 2018 David Timms <iinet.net.au@dtimms> - 2.2.2-3
- retry below change as my git foo didn't manage to delete the empty lines.

* Fri Sep  7 2018 David Timms <iinet.net.au@dtimms> - 2.2.2-2
- fix empty lines within configure command causing non x86 build fails.

* Thu Sep  6 2018 David Timms <iinet.net.au@dtimms> - 2.2.2-1
- Update to 2.2.2
- further improvements from Sérgio Basto <sergio@serjux.com>
- Add conditionals to enable or disable ffmpeg
- Also add conditionals to be possible build with local ffmpeg (not in use)
- Use autoconf before ./configure
- Re-add libmp3lame-default.patch and libdir.patch
- Add to configure --disable-dynamic-loading
- General review of spec
- Re-add desktop.in.patch
- Add to configure --with-lv2 --with-midi --with-portmidi with some commentaries
- Temporary fix to portaudio became permanent (--with-portaudio=local)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.3-8
- Remove obsolete scriptlets

* Wed Oct 04 2017 Scott Talbert <swt@techie.net> - 2.1.3-7
- Update to build against merged compat-wxGTK3-gtk2-devel package

* Sat Sep 30 2017 Jerry James <loganjerry@gmail.com> - 2.1.3-6
- Rebuild for soundtouch 2.0.0

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Mar 25 2017 David Timms <iinet.net.au@dtimms> - 2.1.3-2
- include mp3 import support via libmad, which is now available in Fedora.

* Tue Mar 21 2017 David Timms <iinet.net.au@dtimms> - 2.1.3-1
- 2.1.3 release.
- modify -manual extract path to match earlier builds.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-0.8.20161109git53a5c93
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov  9 2016 David Timms <iinet.net.au@dtimms> - 2.1.3-0.7.20161109git53a5c93
- 2.1.3 Alpha git snapshot 2016-11-09.

* Tue Nov  8 2016 David Timms <iinet.net.au@dtimms> - 2.1.3-0.6.20161025gitff9763f
- add requires wxGTK3-gtk2 tookit version.
- trick configure into detecting and using wxWidgets gtk2.

* Tue Oct 25 2016 David Timms <iinet.net.au@dtimms> - 2.1.3-0.5.20161025gitff9763f
- 2.1.3 Alpha git snapshot 2016-10-25.

* Sun Sep  4 2016 David Timms <iinet.net.au@dtimms> - 2.1.3-0.4.20160904git2fb18e8
- 2.1.3 Alpha git snapshot 2016-09-04.

* Wed Aug 24 2016 David Timms <iinet.net.au@dtimms> - 2.1.3-0.3.20160824git781de82
- 2.1.3 Alpha git snapshot for testing.

* Sun Aug  7 2016 David Timms <iinet.net.au@dtimms> - 2.1.3-0.2.20160807git8392a57
- 2.1.3 Alpha git snapshot for testing.

* Sun Jun  5 2016 David Timms <iinet.net.au@dtimms> - 2.1.3-0.1.20160605gitd41f865
- 2.1.3 Alpha git snapshot for testing.
- remove already applied gcc6 patch.

* Tue Mar 29 2016 Orion Poplawski <orion@cora.nwra.com> - 2.1.2-4
- Add patch to fix gcc6 build issues (bug #1307335)

* Thu Mar 03 2016 David Timms <iinet.net.au@dtimms> - 2.1.2-3
- Rebuild for new soundtouch required to fix symbol lookup error.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 23 2016 David Timms <iinet.net.au@dtimms> - 2.1.2-1
- 2.1.2 final release.

* Fri Jan  1 2016 David Timms <iinet.net.au@dtimms> - 2.1.2-0.8.rc2
- 2.1.2 Release Candidate 2 for testing.

* Sun Nov 15 2015 David Timms <iinet.net.au@dtimms> - 2.1.2-0.7.rc1
- 2.1.2 Release Candidate 1 for testing.

* Thu Nov 12 2015 David Timms <iinet.net.au@dtimms> - 2.1.2-0.6.20151112gitecdb1d8
- 2.1.2 Alpha git snapshot.
- Test build of git master which requires wxGTK3.

* Sun Jul 19 2015 David Timms <iinet.net.au@dtimms> - 2.1.1-1
- Release of Audacity 2.1.1.

* Wed Jul 08 2015 David Timms <iinet.net.au@dtimms> - 2.1.1-0.4.rc2
- Update to 2.1.1rc3 for testing.

* Sat Jul 04 2015 David Timms <iinet.net.au@dtimms> - 2.1.1-0.2.rc1
- Update to 2.1.1rc1 for testing.

* Wed Jun 24 2015 David Timms <iinet.net.au@dtimms> - 2.1.1-0.1.dea351a
- Update to 2.1.1 pre-release git snapshot to prepare for release.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 06 2015 David Timms <iinet.net.au@dtimms> - 2.1.0-3
- Conditionalize AppData out of EPEL <=7 release.

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.1.0-2
- Rebuilt for GCC 5 C++11 ABI change

* Tue Mar 31 2015 David Timms <iinet.net.au@dtimms> - 2.1.0-1
- Update to 2.1.0 final release.

* Mon Mar 30 2015 Richard Hughes <rhughes@redhat.com> - 2.1.0-0.2.rc2
- Use better AppData screenshots

* Thu Mar 05 2015 David Timms <iinet.net.au@dtimms> - 2.1.0-0.1.rc2
- Update to release candidate 2 for testing.

* Mon Sep 29 2014 Richard Hughes <richard@hughsie.com> - 2.0.6-1
- Update to new upstream release

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Aug 09 2014 Rex Dieter <rdieter@fedoraproject.org> 2.0.5-4
- update mime scriptlet, drop (old) umask

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 17 2014 Darryl L. Pierce <dpierce@redhat.com> - 2.0.5-1
- Removed bundled expat.h from sources.
- Resolves: BZ#1076795

* Tue Feb 25 2014 Darryl L. Pierce <dpierce@redhat.com> - 2.0.5-1
- Rebased on Audacity 2.0.5.

* Sun Sep 22 2013 David Timms <iinet.net.au@dtimms> - 2.0.4-2
- Add upstream patch to avoid segfault when starting Effects|Equalization

* Sat Sep 14 2013 David Timms <iinet.net.au@dtimms> - 2.0.4-1
- update to upstream release 2.0.4
- rebase audacity-2.0.1-libmp3lame-default

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 28 2013 Tom Callaway <spot@fedoraproject.org> - 2.0.3-2
- include the readme/license for the nyquist/xlisp bits

* Sat May  4 2013 Hans de Goede <hdegoede@redhat.com> - 2.0.3-1
- New upstream release 2.0.3 (rhbz#951001)
- This release adds aarch64 support (rhbz#925052)
- Use system portaudio
- Add icon-cache update scriptlets

* Sun Feb 10 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 2.0.2-3
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- clean up spec to follow current guidelines

* Tue Sep 04 2012 Dan Horák <dan[at]danny.cz> - 2.0.2-2
- fix build on non-x86 arches

* Mon Aug 27 2012 David Timms <iinet.net.au@dtimms> - 2.0.2-1
- update to 2.0.2 final
- update to manual-2.0.2
- adjust manual extract path to suit changes to manual.zip

* Thu Jul 19 2012 David Timms <iinet.net.au@dtimms> - 2.0.1-1
- update to 2.0.1 final
- rebase libmp3lame-default.patch
- rebase desktop.in.patch

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 14 2012 David Timms <iinet.net.au@dtimms> - 2.0.0-1
- update to 2.0.0 final

* Sun Mar 11 2012 David Timms <iinet.net.au@dtimms> - 2.0.0-0.9.rc9
- update to 2.0.0 release candidate 9
- drop upstreamed glib2 include patch

* Tue Mar  6 2012 David Timms <iinet.net.au@dtimms> - 2.0.0-0.8.rc8
- update to 2.0.0 release candidate 8 for testing only

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-0.4.rc3
- Rebuilt for c++ ABI breakage

* Wed Feb 22 2012 David Timms <iinet.net.au@dtimms> - 2.0.0-0.3.rc3
- update to 2.0.0 release candidate 3

* Sat Feb 18 2012 David Timms <iinet.net.au@dtimms> - 2.0.0-0.2.rc1.20120218svn11513
- update to release candidate from svn snapshot
- update to use online manual for 2.0 series

* Sun Feb  5 2012 David Timms <iinet.net.au@dtimms> - 2.0.0-0.1.alpha20120205svn11456
- update to 2.0.0 alpha svn snapshot
- delete accepted ffmpeg-0.8.y patch

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.14-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 13 2011 David Timms <iinet.net.au@dtimms> - 1.3.14-0.5
- fix Source1 help reference (again).

* Tue Dec 13 2011 David Timms <iinet.net.au@dtimms> - 1.3.14-0.4
- update to 1.3.14 beta release

* Thu Dec  8 2011 David Timms <iinet.net.au@dtimms> - 1.3.14-0.3.alpha20111101svn11296
- add ffmpeg-0.8 patch from Leland Lucius
- add test patch to workaround gtypes-include problem

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.3.14-0.2.alpha20111101svn11296
- Rebuild for new libpng

* Tue Nov  1 2011 David Timms <iinet.net.au@dtimms> - 1.3.14-0.1.alpha20111101svn11296
- update to 1.3.14 alpha svn snapshot

* Wed May  4 2011 David Timms <iinet.net.au@dtimms> - 1.3.13-0.4.beta
- add Requires on audacity folder path to pick up either audacity* package

* Sat Apr 30 2011 David Timms <iinet.net.au@dtimms> - 1.3.13-0.4.beta
- fix files and dir ownership including -manual files in the main package

* Tue Apr 26 2011 David Timms <iinet.net.au@dtimms> - 1.3.13-0.3.beta
- add audacity manual help file Source and subpackage

* Sun Apr 24 2011 David Timms <iinet.net.au@dtimms> - 1.3.13-0.2.beta
- upgrade to 1.3.13-beta
- drop patches included in upstream release
- convert desktop file to a patch against new upstream .desktop file.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.12-0.7.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec  7 2010 Manuel F Martinez <manpaz@bashlinux.com> - 1.3.12-0.6.beta
- Create gcc45 patch to fix issues with configure in portmixer

* Wed Jul 14 2010 Dan Horák <dan@danny.cz> - 1.3.12-0.5.beta
- rebuilt against wxGTK-2.8.11-2

* Mon Jun 28 2010 David Timms <iinet.net.au@dtimms> - 1.3.12-0.4.beta
- mods to ease diffs between builds for fedora and full

* Mon Jun 28 2010 David Timms <iinet.net.au@dtimms> - 1.3.12-0.3.beta
- really package new icons found in icons/hicolor

* Mon Jun 28 2010 David Timms <iinet.net.au@dtimms> - 1.3.12-0.2.beta
- mod tartopdir to use package version macro

* Mon Jun 28 2010 David Timms <iinet.net.au@dtimms> - 1.3.12-0.1.beta
- upgrade to 1.3.12-beta
- package new icons found in icons/hicolor

* Thu Jan 21 2010 Michael Schwendt <mschwendt@fedoraproject.org> - 1.3.11-0.1.beta
- Upgrade to 1.3.11-beta.

* Thu Jan 21 2010 Michael Schwendt <mschwendt@fedoraproject.org> - 1.3.10-0.4.beta
- Add audio/x-flac to .desktop file (#557335).
- Create fresh .desktop file patch. Enable startup notification.

* Sat Jan  9 2010 Michael Schwendt <mschwendt@fedoraproject.org> - 1.3.10-0.3.beta
- Merge improved resample patch from Richard Ash.

* Mon Dec 28 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 1.3.10-0.2.beta
- Patch resampling call to not set end_of_input flag for all sample buffers.

* Fri Dec  4 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 1.3.10-0.1.beta
- Upgrade to 1.3.10-beta.

* Fri Dec  4 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 1.3.9-0.5.beta
- Prevent race-condition segfault with Sound Activated Recording (#544125).

* Wed Sep 23 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.3.9-0.4.beta
- Update desktop file according to F-12 FedoraStudio feature

* Mon Sep 14 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 1.3.9-0.3.beta
- add patch to fix LabelTrack popup

* Sat Sep 12 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 1.3.9-0.2.beta
- add wxGTK work-around patches to fix LabelTrack crash
  (shall fix #520917 and similar race-conditions)

* Thu Sep  3 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 1.3.9-0.1.beta
- upgrade to 1.3.9-beta
- upstream's changes in the device prefs code make the audiodevdefaults
  patch unnecessary afaic see

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.8-0.3.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 20 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 1.3.8-0.2.beta
- glib2 2.21.1's gio in Rawhide F-12 introduces a GSocket that
  conflicts with wxGTK's GSocket class (gsocket.h): as a work-around,
  include less glib headers

* Mon Jul 20 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 1.3.8-0.1.beta
- upgrade to 1.3.8-beta
- BR taglib-devel
- patches merged/obsoleted upstream:
  audacity-1.3.7-portaudio-non-mmap-alsa.patch
  audacity-1.3.7-repeat.patch
  audacity-1.3.6-flac-import.patch

* Wed May 13 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 1.3.7-0.7.beta
- retag up-to-date files and copy to F-10/F-11

* Mon Mar  2 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 1.3.7-0.6.beta
- revise default device names patch, so it doesn't save the defaults

* Sun Mar  1 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 1.3.7-0.5.beta
- show default device names in Audio I/O preferences

* Sat Feb 28 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.3.7-0.4.beta
- remove no longer needed default hostapi hunk of the non-mmap-alsa patch

* Sat Feb 28 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 1.3.7-0.3.beta
- F-10/F-9 only: patch to build with older Vamp API 1.3
- upgrade to 1.3.7-beta pkg from test branch in Fedora cvs

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5-0.13.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb  2 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 1.3.5-0.12.beta
- buildrequire >= 2.0 of Vamp SDK (because we adjust the include paths
  and to avoid that the unpatched local copy is used if system version
  is too old)

* Fri Jan  2 2009 David Timms <iinet.net.au@dtimms> - 1.3.5-0.11.beta
- add PortAudio non mmap alsa patch (Kevin Kofler) bz 445644
  allows record and playback through pulseaudio

* Wed Dec 17 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 1.3.5-0.10.beta
- patch include paths for changes in new vamp-plugin-sdk-devel

* Wed Dec 17 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 1.3.5-0.9.beta
- rebuild in Rawhide for new SONAME in vamp-plugin-sdk
- BR wxGTK-devel for rename of wxGTK2-devel

* Tue Nov  4 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 1.3.5-0.8.beta
- insert a guard in ImportFLAC next to the import assertion

* Tue Nov  4 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 1.3.5-0.7.beta
- BR vamp-plugin-sdk-devel
- no longer build with included Vamp API, also drop Vamp multilib patch

* Thu Aug 28 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 1.3.5-0.6.beta
- rediff some patches for Fedora fuzz=0 pedantry

* Sun Jun  8 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 1.3.5-0.5.beta
- fix bad fr.po that makes Fichier>Open dialog too wide

* Thu May 15 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 1.3.5-0.4.beta
- desktop-file: drop deprecated Encoding, drop Icon file extension

* Thu May 15 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 1.3.5-0.3.beta
- merge 1.3.5-beta from test branch

* Fri May  9 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 1.3.5-0.2.beta
- update to 1.3.5-beta
- expat2 patch merged upstream
- scriptlets: run update-desktop-database without path
- drop scriptlet dependencies

* Mon May  5 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 1.3.5-0.1.rc3.20080505cvs
- update to 1.3.5-rc3 cvs snapshot
- ExportMP3.cpp libdir patch obsolete

* Sat May  3 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 1.3.4-0.7.20080123cvs
- check ownership of temporary files directory (#436260) (CVE-2007-6061)

* Sat Apr 12 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 1.3.4-0.6.20080123cvs
- set a default location for libmp3lame.so.0 again

* Fri Mar 21 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 1.3.4-0.5.20080123cvs
- package the old 1.3.2-beta and a post 1.3.4-beta snapshot in the
  same package -- users may stick to the older one, but please help
  with evaluating the newer one
- merge packaging changes from my 1.3.3/1.3.4 test packages:
- build newer release with wxGTK 2.8.x
- BR soundtouch-devel  and  --with-soundtouch=system
- drop obsolete patches: resample, mp3 export, destdir, FLAC, fr

* Fri Mar 21 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 1.3.2-20
- make soundtouch and allegro build with RPM optflags

* Sun Feb 10 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 1.3.2-19
- rawhide: patch for JACK 0.109.0 API changes (jack_port_lock/unlock removal).
- rebuilt for GCC 4.3 as requested by Fedora Release Engineering
- subst _libdir in ladspa plugin loader

* Thu Jan  3 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 1.3.2-18
- Patch for GCC 4.3.0 C++.

* Fri Nov 16 2007 Michael Schwendt <mschwendt@fedoraproject.org> - 1.3.2-17
- rebuilt for FLAC 1.1.4 -> 1.2.x upgrade, which broke FLAC import

* Tue Aug 28 2007 Michael Schwendt <mschwendt@fedoraproject.org> - 1.3.2-16
- rebuilt for new expat (#195888)

* Tue Aug 21 2007 Michael Schwendt <mschwendt@fedoraproject.org> - 1.3.2-15
- rebuild per request on fedora-devel-list
- clarify licence (GPLv2)

* Mon Mar  5 2007 Michael Schwendt <mschwendt@fedoraproject.org>
- add umask 022 to scriptlets

* Sat Feb 24 2007 Michael Schwendt <mschwendt@fedoraproject.org> - 1.3.2-14
- patch for FLAC 1.1.4 API compatibility

* Sat Feb 24 2007 Michael Schwendt <mschwendt@fedoraproject.org> - 1.3.2-13
- patch ExportMP3.cpp (MPEG-2 Layer III bitrates resulted in
  broken/empty files)
- convert locale related perl substitutions into patches (safer)
- configure with portaudio/portmixer defaults
- drop category Application from desktop file
- fix the libmp3lame.so.0 subst
- subst _libdir in libmp3lame search
- use sed instead of perl

* Fri Feb 23 2007 Gerard Milmeister <gemi@bluewin.ch> - 1.3.2-12
- build with wxGTK 2.6 compatibility package

* Sun Feb 18 2007 Gerard Milmeister <gemi@bluewin.ch> - 1.3.2-11.20070106cvs
- added patch for compiling with libsamplerate

* Thu Feb 15 2007 Gerard Milmeister <gemi@bluewin.ch> - 1.3.2-9.20070106cvs
- disable flac for now

* Thu Feb 15 2007 Gerard Milmeister <gemi@bluewin.ch> - 1.3.2-8.20070106cvs
- compile with jack

* Mon Feb  5 2007 Gerard Milmeister <gemi@bluewin.ch> - 1.3.2-7.20070106cvs
- compile with libsamplerate

* Mon Jan 22 2007 Gerard Milmeister <gemi@bluewin.ch> - 1.3.2-6.20070106cvs
- convert french locale to iso-8859-1

* Sat Jan  6 2007 Gerard Milmeister <gemi@bluewin.ch> - 1.3.2-5.20070106cvs
- corrected cvs date

* Sat Jan  6 2007 Gerard Milmeister <gemi@bluewin.ch> - 1.3.2-3.cvs20060106
- update to cvs

* Fri Jan  5 2007 Gerard Milmeister <gemi@bluewin.ch> - 1.3.2-2
- remove -msse flag for ppc

* Fri Jan  5 2007 Gerard Milmeister <gemi@bluewin.ch> - 1.3.2-1
- new version 1.3.2

* Tue Jan  2 2007 Gerard Milmeister <gemi@bluewin.ch> - 1.2.6-1
- new version 1.2.6

* Sat Nov 11 2006 Gerard Milmeister <gemi@bluewin.ch> - 1.2.5-3
- correct mime types in .desktop file
- msse flag only on intel

* Fri Nov  3 2006 Gerard Milmeister <gemi@bluewin.ch> - 1.2.5-2
- remove -msse flag for ppc

* Fri Nov  3 2006 Gerard Milmeister <gemi@bluewin.ch> - 1.2.5-1
- new version 1.2.5

* Mon Aug 28 2006 Gerard Milmeister <gemi@bluewin.ch> - 1.2.4-0.2.b
- Rebuild for FE6

* Fri Mar 17 2006 Michael Schwendt <mschwendt@fedoraproject.org> - 1.2.4-0.1.b
- Update to 1.2.4b (stable release).
- Follow upstream recommendation and use the GTK+ 1.x wxGTK.
  This is because of various issues with fonts/layout/behaviour.
- Build with compat-wxGTK-devel.
- Modify build section to find wx-2.4-config instead of wx-config.

* Fri May 20 2005 David Woodhouse <dwmw2@infradead.org> - 1.2.3-5
- Bump release number again due to spurious build system failure and
  the fact that the build system seems to be ignoring repeated build
  requests for the previous version.

* Fri May 20 2005 David Woodhouse <dwmw2@infradead.org> - 1.2.3-4
- Add more possible MIME types for ogg which may be seen even though
  they're not standard.

* Thu Apr  7 2005 Gerard Milmeister <gemi@bluewin.ch> - 1.2.3-3
- Build gtk2 version by default

* Thu Apr  7 2005 Michael Schwendt <mschwendt@fedoraproject.org>
- rebuilt

* Tue Apr  5 2005 Gerard Milmeister <gemi@bluewin.ch> - 1.2.3-2
- Rebuild to pick a new FLAC dependencies

* Sat Nov 20 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:1.2.3-1
- New Version 1.2.3

* Sat Oct 30 2004 Michael Schwendt <mschwendt@fedoraproject.org> - 0:1.2.2-0.fdr.1
- Update to 1.2.2, patch aboutdialog to be readable with wxGTK.

* Mon May 10 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:1.2.1-0.fdr.1
- New Version 1.2.1

* Sun Apr 11 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:1.2.0-0.fdr.2
- Fix for Language.cpp restored

* Tue Mar  2 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:1.2.0-0.fdr.1
- New Version 1.2.0

* Mon Nov 24 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:1.2.0-0.fdr.4.pre3
- Added icon
- Separated mp3 plugin

* Sun Nov 23 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:1.2.0-0.fdr.2.pre3
- Changes to specfile

* Sun Nov  2 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:1.2.0-0.fdr.1.pre3
- New upstream version 1.2.0-pre3

* Sat Oct 25 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:1.2.0-pre2.fdr.1
- First Fedora release

