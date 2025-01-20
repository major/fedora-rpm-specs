Name:		qmmp
Version:	2.2.2
Release:	2%{?dist}
Summary:	Qt-based multimedia player

License:	GPL-2.0-or-later AND CC-BY-SA-4.0
URL:		http://qmmp.ylsoftware.com/
Source:		http://qmmp.ylsoftware.com/files/%{name}-%{version}.tar.bz2

BuildRequires:	alsa-lib-devel
BuildRequires:	cmake
BuildRequires:	desktop-file-utils
BuildRequires:	enca-devel
BuildRequires:	ffmpeg-free-devel
BuildRequires:	flac-devel
BuildRequires:	game-music-emu-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	libarchive-devel
BuildRequires:	libbs2b-devel
BuildRequires:	libcddb-devel
BuildRequires:	libcdio-paranoia-devel
BuildRequires:	libcurl-devel
BuildRequires:	libmad-devel
BuildRequires:	libmms-devel
BuildRequires:	libmpcdec-devel
BuildRequires:	libogg-devel
BuildRequires:	libprojectM-devel
BuildRequires:	librcd-devel
BuildRequires:	libshout-devel
BuildRequires:	libsidplayfp-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libxmp-devel
BuildRequires:	mpg123-devel
BuildRequires:	openssl-devel
BuildRequires:	opusfile-devel
BuildRequires:	pipewire-devel
BuildRequires:	qt6-qtmultimedia-devel
BuildRequires:	qt6-qttools-devel
BuildRequires:	soxr-devel
BuildRequires:	taglib-devel >= 1.10
BuildRequires:	wavpack-devel
BuildRequires:	wildmidi-devel

# /usr/share/solid/actions owner
%if 0%{?fedora} >= 40 || 0%{?rhel} >= 10
Requires:	kde-filesystem
%elif %{undefined flatpak}
Requires:	kf5-filesystem
%endif

Recommends:	qmmp-plugin-pack
# some external tools listed in
# https://sourceforge.net/p/qmmp-dev/code/HEAD/tree/trunk/qmmp/src/plugins/General/converter/presets.conf
Recommends:	vorbis-tools
Recommends:	lame
Recommends:	opus-tools
Recommends:	wavpack
Recommends:	flac

# Do not check .so files in an application-specific library directory
%global __provides_exclude_from ^%{_libdir}/%{name}/.*\\.so$

%package devel
Summary:	Development files for qmmp
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description
This program is an audio-player, written with help of Qt library.
The user interface is similar to winamp or xmms.
Main opportunities:

	* Winamp and xmms skins support
	* plugins support
	* MPEG1 layer 2/3 support
	* Ogg Vorbis support
	* native FLAC support
	* WavePack support
	* ModPlug support
	* PCM WAVE support
	* CD Audio support
	* CUE sheet support
	* ALSA sound output
	* JACK sound output
	* OSS sound output
	* PipeWire output
	* Last.fm/Libre.fm scrobbler
	* D-Bus support
	* Spectrum Analyzer
	* projectM visualization
	* sample rate conversion
	* bs2b dsp effect
	* streaming support
	* removable device detection
	* MPRIS support
	* global hotkey support
	* lyrics support

%description devel
QMMP is Qt-based audio player. This package contains its development files.

%prep
%setup -q


%build
%cmake \
	-D USE_AAC:BOOL=FALSE \
	-D USE_MPLAYER:BOOL=FALSE \
	-D USE_LIBRCD:BOOL=TRUE \
	-D QMMP_DEFAULT_OUTPUT=pipewire \
	-D CMAKE_INSTALL_PREFIX=%{_prefix} \
	-D LIB_DIR=%{_lib} \
	-D PLUGIN_DIR=%{_lib}/%{name}
%cmake_build

%install
%cmake_install
# filter out unsupported formats from MimeType
sed -i -e "s#audio/aac;##" \
       -e "s#audio/x-aac;##" \
    %{buildroot}/%{_datadir}/applications/%{name}.desktop
sed -i -e "s#audio/aac;##" \
       -e "s#audio/x-aac;##" \
    %{buildroot}/%{_datadir}/applications/%{name}-enqueue.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}-dir.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}-enqueue.desktop
# the validator makes assumptions not mandated by the standard
# https://specifications.freedesktop.org/desktop-entry-spec/desktop-entry-spec-latest.html
# as of today, 2020-07-31
#desktop-file-validate %%{buildroot}/%%{_datadir}/solid/actions/%%{name}-opencda.desktop

%files
%doc AUTHORS ChangeLog ChangeLog.rus README README.RUS
%license COPYING COPYING.CC-by-sa_V4
%{_bindir}/qmmp
%{_libdir}/qmmp
%{_libdir}/libqmmp*.so.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-dir.desktop
%{_datadir}/applications/%{name}-enqueue.desktop
%{_datadir}/solid/actions/%{name}-opencda.desktop
%{_datadir}/icons/hicolor/
%{_datadir}/%{name}/
%{_metainfodir}/%{name}.appdata.xml

%files devel
%{_includedir}/*
%{_libdir}/pkgconfig/qmmp*
%{_libdir}/libqmmp*.so

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Nov 11 2024 Karel Volný <kvolny@redhat.com> 2.2.2-1
- new version 2.2.2 (rhbz#2325053)
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Tue Oct 15 2024 Karel Volný <kvolny@redhat.com> 2.2.1-1
- new version 2.2.1 (rhbz#2316649)
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Mon Sep 23 2024 Fabio Valentini <decathorpe@gmail.com> - 2.1.9-2
- Rebuild for ffmpeg 7

* Tue Aug 13 2024 Karel Volný <kvolny@redhat.com> 2.1.9-1
- new version 2.1.9 (rhbz#2304136)
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 05 2024 Karel Volný <kvolny@redhat.com> 2.1.8-1
- new version 2.1.8 (rhbz#2280887)
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Tue May 21 2024 Jan Grulich <jgrulich@redhat.com> - 2.1.7-2
- Rebuild (qt6)

* Thu Apr 18 2024 Karel Volný <kvolny@redhat.com> 2.1.7-1
- new version 2.1.7 (rhbz#2275632)
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Thu Apr 04 2024 Jan Grulich <jgrulich@redhat.com> - 2.1.6-2
- Rebuild (qt6)

* Mon Mar 11 2024 Karel Volný <kvolny@redhat.com> 2.1.6-1
- new version 2.1.6 (rhbz#2268701)
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Aug 31 2023 Karel Volný <kvolny@redhat.com> 2.1.5-1
- new version 2.1.5 (rhbz#2235874)
- enabled MMS support (rhbz#2235608)
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri May 26 2023 Karel Volný <kvolny@redhat.com> 2.1.4-1
- new version 2.1.4 (rhbz#2210109)
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Thu Mar 30 2023 Karel Volný <kvolny@redhat.com> 2.1.3-1
- new version 2.1.3 (rhbz#2182859)
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Fri Mar 17 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 2.1.2-5
- Enable musepack input plugin

* Sun Mar 12 2023 Neal Gompa <ngompa@fedoraproject.org> - 2.1.2-4
- Rebuild for ffmpeg 6.0

* Mon Feb 27 2023 Karel Volný <kvolny@redhat.com> 2.1.2-3
- enable ffmpeg plugin using ffmpeg-free

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep 15 2022 Karel Volný <kvolny@redhat.com> 2.1.2-1
- new version 2.1.2 (rhbz#2126914)
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Wed Sep 14 2022 Michel Alexandre Salim <salimma@fedoraproject.org> - 2.1.1-3
- Rebuilt for flac 1.4.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Karel Volný <kvolny@redhat.com> 2.1.1-1
- new version 2.1.1 (#2095831)
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Wed May 18 2022 Karel Volný <kvolny@redhat.com> 2.1.0-1
- new version 2.1.0 (#2087200)
- replaces libmodplug with libxmp
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Thu Apr 07 2022 Karel Volný <kvolny@redhat.com> 2.0.4-1
- new version 2.0.4
- uses Qt6
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Thu Apr 07 2022 Carl George <carl@george.computer> - 1.5.1-4
- Filter all plugins from provides
- Resolves: rhbz#2072796

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 17 2021 Karel Volný <kvolny@redhat.com> 1.5.1-1
- new version 1.5.1
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Wed May 26 2021 Karel Volný <kvolny@redhat.com> 1.5.0-1
- new version 1.5.0 (#1963431)
- see the upstream changelog at http://qmmp.ylsoftware.com/
- use PipeWire instead of PulseAudio (https://fedoraproject.org/wiki/Changes/DefaultPipeWire)
- adds librcd support

* Tue May 11 2021 Karel Volný <kvolny@redhat.com> 1.4.6-1
- new version 1.4.6 (#1958613)
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Thu Apr 29 2021 Karel Volný <kvolny@redhat.com> 1.4.5-1
- new version 1.4.5 (#1954785)
- see the upstream changelog at http://qmmp.ylsoftware.com/
- fixes GCC 11 issue, patch removed

* Sun Feb 21 2021 Karel Volný <kvolny@redhat.com> 1.4.4-1
- new version 1.4.4 (#1908503)
- see the upstream changelog at http://qmmp.ylsoftware.com/
- fixes rhbz#1910933

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 15 2020 Jeff Law <law@redhat.com> 1.4.2-2
- Fix missing #include for gcc-11

* Mon Sep 21 2020 Karel Volný <kvolny@redhat.com> 1.4.2-1
- new version 1.4.2 (#1880775)
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Fri Jul 31 2020 Karel Volný <kvolny@redhat.com> 1.4.1-1
- new version 1.4.1 (#1828957)
- see the upstream changelog at http://qmmp.ylsoftware.com/
- adapted to F33 System-Wide Change: CMake to do out-of-source builds
- install desktop file for opening audio CDs as Solid action

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 31 2020 Adrian Reber <adrian@lisas.de> - 1.3.7-2
- Rebuilt for libcdio-2.1.0

* Sun Mar 29 2020 Karel Volný <kvolny@redhat.com> 1.3.7-1
- new version 1.3.7 (#1817683)
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 15 2020 Karel Volný <kvolny@redhat.com> 1.3.6-1
- new version 1.3.6 (#1791042)
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Sat Dec 28 2019 Karel Volný <kvolny@redhat.com> 1.3.5-1
- new version 1.3.5 (#1785870)
- see the upstream changelog at http://qmmp.ylsoftware.com/
- fixes crash when reading encrypted archive (#1694388)

* Wed Aug 28 2019 Karel Volný <kvolny@redhat.com> 1.3.4-1
- new version 1.3.4
- see the upstream changelog at http://qmmp.ylsoftware.com/
- also fixes rhbz#1684881

* Fri Aug 09 2019 Karel Volný <kvolny@redhat.com> 1.3.3-2
- use mpg123, previously included in qmmp-plugin-pack (both mad and mpg123 in libmpeg)

* Wed Aug 07 2019 Karel Volný <kvolny@redhat.com> 1.3.3-1
- new version 1.3.3 (#1674198)
- see the upstream changelog at http://qmmp.ylsoftware.com/
- adds appdata
- dropped qmmp-plugins-freeworld conflict
- cleaned up desktop file handling
- define unversioned plugin dir
# ^ I will NOT support parallel installs
- drop old musepack support (see bug #1014468; upstream commit r8015)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 30 2018 Karel Volný <kvolny@redhat.com> 1.2.4-1
- new version 1.2.4
- see the upstream changelog at http://qmmp.ylsoftware.com/
- fixes restoring window position in multiscreen setup (#1591487)

* Wed Jul 25 2018 Karel Volný <kvolny@redhat.com> 1.2.3-1
- new version 1.2.3 (#1606937)
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 01 2018 Karel Volný <kvolny@redhat.com> 1.2.2-1
- new version 1.2.2 (#1584930)
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Fri Apr 20 2018 Karel Volný <kvolny@redhat.com> 1.2.1-1
- new version 1.2.1 (#1569776)
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Thu Apr 19 2018 Karel Volný <kvolny@redhat.com> 1.2.0-2
- added dependencies for archive and icecast plugins

* Tue Apr 17 2018 Karel Volný <kvolny@redhat.com> 1.2.0-1
- new version 1.2.0
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Adrian Reber <adrian@lisas.de> - 1.1.12-2
- Rebuilt for libcdio-2.0.0

* Tue Nov 14 2017 Karel Volný <kvolny@redhat.com> 1.1.12-1
- new version 1.1.12 (#1505139)
- see the upstream changelog at http://qmmp.ylsoftware.com/
- filter out newly added mimetypes not supported in this package

* Mon Aug 07 2017 Karel Volný <kvolny@redhat.com> 1.1.10-1
- new version 1.1.10
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 08 2017 Karel Volný <kvolny@redhat.com> 1.1.9-1
- new version 1.1.9 (#1458495)
- see the upstream changelog at http://qmmp.ylsoftware.com/
- added weak dependencies for SRC plugin (#1450271)

* Thu Mar 23 2017 Karel Volný <kvolny@redhat.com> 1.1.8-1
- new version 1.1.8 (#1435226)
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Mon Feb 06 2017 Karel Volný <kvolny@redhat.com> 1.1.7-1
- new version 1.1.7 (#1419294)
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Wed Nov 23 2016 Karel Volný <kvolny@redhat.com> 1.1.6-1
- new version 1.1.6 (#1412601)
- see the upstream changelog at http://qmmp.ylsoftware.com/
- enabled MAD plugin (#1400109)

* Wed Nov 23 2016 Karel Volný <kvolny@redhat.com> 1.1.5-1
- new version 1.1.5 (#1393366)
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Mon Nov 14 2016 Adrian Reber <adrian@lisas.de> 1.1.4-2
- rebuild for new libcdio-0.94

* Tue Oct 04 2016 Karel Volný <kvolny@redhat.com> 1.1.4-1
- new version 1.1.4 (#1370807)
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Fri Aug 26 2016 Hans de Goede <hdegoede@redhat.com> 1.1.2-2
- Rebuild for new wildmidi

* Mon Jul 25 2016 Karel Volný <kvolny@redhat.com> 1.1.2-1
- new version 1.1.2 (update bug missing - Anitya issue #316)
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Mon Jul 11 2016 Karel Volný <kvolny@redhat.com> 1.1.1-1
- new version 1.1.1 (#1352736)
- see the upstream changelog at http://qmmp.ylsoftware.com/
- removed libsamplerate dependency; moved to plugin pack in 1.1.0

* Thu Jun 23 2016 Karel Volný <kvolny@redhat.com> 1.1.0-1
- new version 1.1.0 (#1348548)
- see the upstream changelog at http://qmmp.ylsoftware.com/
- adds soxr (SoX Resampler) effect plugin
- adds qt5-qtmultimedia output plugin

* Fri Jun 03 2016 Karel Volný <kvolny@redhat.com> 1.0.10-1
- new version 1.0.10 (#1341421)
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Mon May 02 2016 Karel Volný <kvolny@redhat.com> 1.0.9-1
- new version 1.0.9 (#1332176)
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Mon Apr 04 2016 Karel Volný <kvolny@redhat.com> 1.0.7-1
- new version 1.0.7 (#1323535)
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Tue Mar 22 2016 Karel Volný <kvolny@redhat.com> 1.0.6-3
- rebuilt for libprojectM update

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Karel Volný <kvolny@redhat.com> 1.0.6-1
- new version 1.0.6 (#1302491)
- see the upstream changelog at http://qmmp.ylsoftware.com/
 - fixed gme plugin build
 - added feature to change default output plugin
   (removed workaround in specfile)
- updated provides filtering
- fix desktop files - filter out mimetypes that are not supported by this build
- added license info for the "glare" skin

* Mon Jan 04 2016 Karel Volný <kvolny@redhat.com> 1.0.5-1
- new version 1.0.5 (#1295137)
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Fri Dec 25 2015 Karel Volný <kvolny@redhat.com> 1.0.4-1
- new version 1.0.4
- see the upstream changelog at http://qmmp.ylsoftware.com/
- change default output to PulseAudio instead of ALSA

* Tue Nov 24 2015 Karel Volný <kvolny@redhat.com> 1.0.2-1
- new version 1.0.2
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Thu Oct 22 2015 Karel Volný <kvolny@redhat.com> 1.0.1-1
- new version 1.0.1
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Wed Oct 07 2015 Karel Volný <kvolny@redhat.com> 1.0.0-1
- new version 1.0.0
- see the upstream changelog at http://qmmp.ylsoftware.com/
- uses Qt5

* Tue Sep 08 2015 Karel Volný <kvolny@redhat.com> 0.9.1-1
- new version
- see the upstream changelog at http://qmmp.ylsoftware.com/
- adds QSUI from plugin pack
- removed qmmp_cue.desktop, no longer handled separately
- run update-desktop-database in %%post* scriptlets (bug #1242974)

* Tue Aug 25 2015 Karel Volný <kvolny@redhat.com> 0.8.8-1
- new version
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Fri Jul 10 2015 Hans de Goede <hdegoede@redhat.com> 0.8.5-2
- Rebuilt for libsidplayfp soname bump
- Misc. specfile cleanups

* Wed Jun 24 2015 Karel Volný <kvolny@redhat.com> 0.8.5-1
- new version
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 04 2015 Karel Volný <kvolny@redhat.com> 0.8.4-1
- new version
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.8.3-2
- Rebuilt for GCC 5 C++11 ABI change

* Tue Feb 03 2015 Karel Volný <kvolny@redhat.com> 0.8.3-1
- new version
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Tue Nov 11 2014 Adrian Reber <adrian@lisas.de> 0.8.1-3
- rebuild for new libcdio-0.93

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Aug 14 2014 Karel Volný <kvolny@redhat.com> 0.8.1-1
- new version
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Mon Jul 14 2014 Karel Volný <kvolny@redhat.com> 0.8.0-1
- new version
- see the upstream changelog at http://qmmp.ylsoftware.com/
- added SID support via libsidplay
- cleanup of BuildRequires

* Mon Jun 09 2014 Karel Volný <kvolny@redhat.com> 0.7.7-1
- new version
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 17 2014 Karel Volný <kvolny@redhat.com> 0.7.4-1
- new version
- see the upstream changelog at http://qmmp.ylsoftware.com/
- should fix bug #1049267

* Tue Aug 27 2013 Karel Volný <kvolny@redhat.com> 0.7.2-1
- new version
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 20 2013 Karel Volný <kvolny@redhat.com> 0.7.1-1
- new version
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Thu Apr 18 2013 Karel Volný <kvolny@redhat.com> 0.7.0-1
- new version
- see the upstream changelog at http://qmmp.ylsoftware.com/
- project URLs changed
- add Opus support
- use UDisks2 instead of UDisks

* Tue Apr 02 2013 Karel Volný <kvolny@redhat.com> 0.6.8-1
- new version
- see the upstream changelog at http://qmmp.ylsoftware.com/index_en.php

* Fri Feb 22 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.6.6-2
- Remove --vendor from desktop-file-install for F19 https://fedorahosted.org/fesco/ticket/1077

* Tue Jan 29 2013 Karel Volný <kvolny@redhat.com> 0.6.6-1
- new version
- see the upstream changelog at http://qmmp.ylsoftware.com/index_en.php

* Mon Jan 07 2013 Adrian Reber <adrian@lisas.de> 0.6.5-2
- rebuild for new libcdio-0.90

* Tue Dec 11 2012 Karel Volný <kvolny@redhat.com> 0.6.5-1
- new version
- see the upstream changelog at http://qmmp.ylsoftware.com/index_en.php

* Tue Nov 06 2012 Karel Volný <kvolny@redhat.com> 0.6.4-1
- new version
- see the upstream changelog at http://qmmp.ylsoftware.com/index_en.php

* Thu Aug 16 2012 Karel Volný <kvolny@redhat.com> 0.6.3-1
- new version
- see the upstream changelog at http://qmmp.ylsoftware.com/index_en.php

* Tue Jul 31 2012 Karel Volný <kvolny@redhat.com> 0.6.2-2
- move the unversioned libraries symlinks to -devel subpackage

* Mon Jul 30 2012 Karel Volný <kvolny@redhat.com> 0.6.2-1
- new version
- see the upstream changelog at http://qmmp.ylsoftware.com/index_en.php

* Fri Jul 27 2012 Karel Volný <kvolny@redhat.com> 0.6.1-1
- new version
- see the upstream changelog at http://qmmp.ylsoftware.com/index_en.php

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 3 2012 Karel Volný <kvolny@redhat.com> 0.6.0-1
- new version
- see the upstream changelog at http://qmmp.ylsoftware.com/index_en.php
- new qmmp_dir.desktop file
- provide new pkgconfig files in -devel

* Mon Jun 18 2012 Karel Volný <kvolny@redhat.com> 0.5.6-1
- new version
- see the upstream changelog at http://qmmp.ylsoftware.com/index_en.php

* Thu Jun 7 2012 Karel Volný <kvolny@redhat.com> 0.5.5-1
- new version
- see the upstream changelog at http://qmmp.ylsoftware.com/index_en.php

* Thu Mar 1 2012 Karel Volný <kvolny@redhat.com> 0.5.4-1
- new version
- see the upstream changelog at http://qmmp.ylsoftware.com/index_en.php
- removed cmake include patch (accepted upstream)

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-2
- Rebuilt for c++ ABI breakage

* Mon Jan 23 2012 Karel Volný <kvolny@redhat.com> 0.5.3-1
- new version
- see upstream changelog at http://qmmp.ylsoftware.com/index_en.php
- patch missing cmake include (qmmp-0.5.3-CheckCXXSourceCompiles.patch)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 20 2011 Adrian Reber <adrian@lisas.de> 0.5.2-2
- rebuild for new libcdio

* Tue Sep 06 2011 Karel Volný <kvolny@redhat.com> 0.5.2-1
- new version
- see upstream changelog at http://qmmp.ylsoftware.com/index_en.php

* Fri Jun 24 2011 Karel Volný <kvolny@redhat.com> 0.5.1-1
- new version
- lots of improvements, see http://qmmp.ylsoftware.com/index_en.php
- added MIDI support via wildmidi and game music support via game-music-emu

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Karel Volný <kvolny@redhat.com> 0.4.3-1
- new version
- adds dvd autodetection
- lot of fixes

* Mon Sep 13 2010 Karel Volný <kvolny@redhat.com> 0.4.2-1
- new version
- adds Japanese and Spanish translations
- lot of fixes

* Wed Jun 30 2010 Karel Volný <kvolny@redhat.com> 0.4.1-1
- new version
- adds Dutch translation
- lot of fixes

* Thu Jun 10 2010 Karel Volný <kvolny@redhat.com> 0.4.0-1
- new version
- core rewrites, lots of new plugins
- BuildRequires enca-devel, libcddb-devel

* Tue Jun  1 2010 Ville Skyttä <ville.skytta@iki.fi> - 0.3.4-2
- Rebuild.

* Mon Apr 19 2010 Karel Volný <kvolny@redhat.com> 0.3.4-1
- new version
- fixes desktop file (yum warning issue), some other fixes

* Fri Apr 09 2010 Karel Volný <kvolny@redhat.com> 0.3.3-1
- new version
- adds Hungarian translation, some fixes

* Fri Jan 22 2010 Adrian Reber <adrian@lisas.de> 0.3.2-3
- rebuild for new libcdio

* Thu Jan 21 2010 Karel Volný <kvolny@redhat.com> 0.3.2-2
- rebuild for new libprojectM

* Wed Jan 13 2010 Karel Volný <kvolny@redhat.com> 0.3.2-1
- new version
- projectM 2.0 compatible (WRT bug #551855)

* Wed Nov 25 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.3.1-2
- rebuild for Qt 4.6.0 RC1 in F13 (was built against Beta 1 with unstable ABI)

* Wed Nov 04 2009 Karel Volný <kvolny@redhat.com> 0.3.1-1
- new version

* Wed Sep 02 2009 Karel Volný <kvolny@redhat.com> 0.3.0-3
- add libbs2b support, as it got added to Fedora (see bug #519138)

* Thu Aug 27 2009 Tomas Mraz <tmraz@redhat.com> - 0.3.0-2
- rebuilt with new openssl

* Tue Aug 25 2009 Karel Volný <kvolny@redhat.com> - 0.3.0-1
- new version
- updated %%description to match upstream
- new plugins = new BuildRequires, new .desktop files
- AAC support disabled due to patent restrictions
- mplayer plugin disabled due to mplayer missing from Fedora

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 05 2009 Karel Volny <kvolny@redhat.com> 0.2.3-3
- do not own /usr/include in -devel subpackage (fixes bug #484098)

* Sat Jan 17 2009 Tomas Mraz <tmraz@redhat.com> 0.2.3-2
- rebuild with new openssl

* Fri Dec 05 2008 Karel Volny <kvolny@redhat.com> 0.2.3-1
- new version
- added %%{?_smp_mflags} to make, as parallel build was fixed

* Tue Sep 02 2008 Karel Volny <kvolny@redhat.com> 0.2.2-1
- new version

* Wed Jul 30 2008 Karel Volny <kvolny@redhat.com> 0.2.0-1
- new version
- updated %%description to match upstream
- added BuildRequires: libsndfile-devel wavpack-devel pulseaudio-libs-devel
- added BuildRequires: libmodplug-devel libcurl-devel openssl-devel
- xpm icon is not used anymore (several pngs available)
- created devel subpackage

* Mon May 19 2008 Karel Volny <kvolny@redhat.com> 0.1.6-2
- fixed %%description not to include patent-encumbered formats (bug #447141)

* Tue May 13 2008 Karel Volny <kvolny@redhat.com> 0.1.6-1
- new version

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.1.5-2
- Autorebuild for GCC 4.3

* Mon Dec 10 2007 Karel Volny <kvolny@redhat.com> 0.1.5-1
- new version
- simplified setting of library destination
- removed install-permissions patch, fixed upstream

* Wed Nov 21 2007 Karel Volny <kvolny@redhat.com> 0.1.4-5
- included Hans de Goede's patch for file permissions

* Mon Nov 19 2007 Karel Volny <kvolny@redhat.com> 0.1.4-4
- additional spec improvements as suggested in comment #10 to bug #280751

* Wed Sep 12 2007 Karel Volny <kvolny@redhat.com> 0.1.4-3
- additional spec improvements as suggested in comment #4 to bug #280751

* Tue Sep 11 2007 Karel Volny <kvolny@redhat.com> 0.1.4-2
- spec cleanup as suggested in comment #2 to bug #280751

* Mon Sep 10 2007 Karel Volny <kvolny@redhat.com> 0.1.4-1
- version bump
- install vendor-supplied .desktop file

* Thu Sep 6 2007 Karel Volny <kvolny@redhat.com> 0.1.3.1-2
- patched for multilib Fedora setup
- added .desktop entry and icon
- fixed spec to meet Fedora policies and rpm requirements
- removed ffmpeg and mad plugins to meet Fedora no-mp3 policy

* Wed Aug 1 2007 Eugene Pivnev <ti DOT eugene AT gmail DOT com> 1.1.9-1
- Initial release for Fedora 7
