%global  mpd_user            mpd
%global  mpd_group           %{mpd_user}

%global  mpd_homedir         %{_localstatedir}/lib/mpd
%global  mpd_logdir          %{_localstatedir}/log/mpd
%global  mpd_musicdir        %{mpd_homedir}/music
%global  mpd_playlistsdir    %{mpd_homedir}/playlists
%global  mpd_rundir          %{_rundir}/mpd

%global  mpd_configfile      %{_sysconfdir}/mpd.conf
%global  mpd_dbfile          %{mpd_homedir}/mpd.db
%global  mpd_logfile         %{mpd_logdir}/mpd.log
%global  mpd_statefile       %{mpd_homedir}/mpdstate

Name:           mpd
Epoch:          1
Version:        0.24.12
Release:        5%{?dist}
Summary:        Music player daemon

License:        GPL-2.0-only AND BSD-2-Clause AND ISC AND LGPL-2.1-only AND LGPL-2.1-or-later AND BSD-2-Clause-Views
URL:            https://www.musicpd.org/
Source0:        %{url}/download/mpd/0.24/mpd-%{version}.tar.xz
Source1:        %{url}/download/mpd/0.24/mpd-%{version}.tar.xz.sig
# http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x236E8A58C6DB4512
Source2:        gpgkey.asc
Source3:        mpd.logrotate
Source4:        mpd.tmpfiles.d
Source5:        mpd.sysusers
# Use Fedora specific patches for runtime log paths and settings
Patch0:         mpd-0.24.8-mpdconf.patch

BuildRequires:  firewalld-filesystem
BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  hicolor-icon-theme
BuildRequires:  lame-devel
BuildRequires:  libmpcdec-devel
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(adplug)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(ao)
BuildRequires:  pkgconfig(audiofile)
BuildRequires:  pkgconfig(avahi-core)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(faad2)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(fluidsynth)
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(id3tag)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libchromaprint)
BuildRequires:  pkgconfig(libcdio)
BuildRequires:  pkgconfig(libcdio_paranoia)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  pkgconfig(libgme)
BuildRequires:  pkgconfig(libmikmod)
BuildRequires:  pkgconfig(libmms)
BuildRequires:  pkgconfig(libmodplug)
BuildRequires:  pkgconfig(libmpdclient)
BuildRequires:  pkgconfig(libmpg123)
BuildRequires:  pkgconfig(libnfs)
BuildRequires:  pkgconfig(libopenmpt)
BuildRequires:  pkgconfig(libpcre2-posix)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libsidplayfp)
BuildRequires:  pkgconfig(libupnp)
BuildRequires:  pkgconfig(liburing)
BuildRequires:  pkgconfig(mad)
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(shout)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(soxr)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(twolame)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(wavpack)
BuildRequires:  pkgconfig(wildmidi)
BuildRequires:  pkgconfig(zziplib)
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros

# Not packaged
# https://sourceforge.net/projects/sidplay2/
#BuildRequires:  libsidplay2-devel
# https://packages.debian.org/sid/libsidutils-dev
#BuildRequires:   libsidutils-devel
# https://packages.debian.org/sid/libresid-builder-dev
#BuildRequires:  libresid-builder-devel
# https://github.com/toots/shine
#BuildRequires:  libshine-devel
# https://github.com/ratchov/sndio
#BuildRequires:  libsndio-devel

# Documentation
BuildRequires:  doxygen
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  texinfo

Requires: hicolor-icon-theme
Requires: logrotate

%description
A daemon for playing music of various formats. Music is played through the
server's audio device. The daemon stores info about all available music, and
this info can be easily searched and retrieved. Player control, info
retrieval, and playlist management can all be managed remotely.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1



%build
%meson -Ddocumentation=enabled \
       -Dhtml_manual=false \
       -Dmanpages=true \
       -Ddoxygen=true \
       -Dtest=true \
       -Dpipe=true \
       -Dsystemd=enabled \
       -Dpcre=enabled \
       -Dsndio=disabled \
       -Dshine=disabled \
       -Dtremor=disabled \
       -Dipv6=enabled \
       -Dsystemd_system_unit_dir=%{_unitdir} \
       -Dsystemd_user_unit_dir=%{_userunitdir} \
       -Dsolaris_output=disabled
%meson_build
pushd doc
sphinx-build -b texinfo . texinfo
pushd texinfo
makeinfo --docbook musicplayerdaemon.texi
popd
popd

%install
%meson_install

install -pDm0644 doc/texinfo/musicplayerdaemon.xml \
  %{buildroot}%{_datadir}/help/en/mpd/musicplayerdaemon.xml
install -p -D -m 0644 %{SOURCE3} \
    %{buildroot}%{_sysconfdir}/logrotate.d/mpd
install -p -D -m 0644 %{SOURCE4} \
    %{buildroot}%{_tmpfilesdir}/mpd.conf
install -p -D -m 0644 %{SOURCE5} \
    %{buildroot}%{_sysusersdir}/mpd.conf
mkdir -p %{buildroot}/run
install -d -m 0755 %{buildroot}/%{mpd_rundir}

mkdir -p %{buildroot}%{mpd_homedir}
mkdir -p %{buildroot}%{mpd_logdir}
mkdir -p %{buildroot}%{mpd_musicdir}
mkdir -p %{buildroot}%{mpd_playlistsdir}
touch %{buildroot}%{mpd_dbfile}
touch %{buildroot}%{mpd_logfile}
touch %{buildroot}%{mpd_statefile}

install -D -p -m644 doc/mpdconf.example %{buildroot}%{mpd_configfile}

# Packaged in license directory
rm %{buildroot}%{_docdir}/mpd/COPYING

%check
%meson_test

%post
%systemd_post mpd.service
%systemd_user_post mpd.service

%preun
%systemd_preun mpd.service
%systemd_user_preun mpd.service

%postun
%systemd_postun_with_restart mpd.service
%systemd_user_postun_with_restart mpd.service
%systemd_user_postun_with_reload mpd.service
%systemd_user_postun mpd.service


%files
%license COPYING
%license LICENSES/BSD-2-Clause.txt
%license LICENSES/GPL-2.0-or-later.txt
%license LICENSES/ISC.txt
%license LICENSES/LGPL-2.1-only.txt
%doc README.md
%doc AUTHORS
%doc NEWS
%{_bindir}/mpd
%{_mandir}/man1/mpd.1*
%{_mandir}/man5/mpd.conf.5*
%dir  %{_datadir}/help/en
%lang(en) %{_datadir}/help/en/mpd
%{_unitdir}/mpd.service
%{_unitdir}/mpd.socket
%{_userunitdir}/mpd.service
%{_userunitdir}/mpd.socket
%{_sysusersdir}/mpd.conf
%config(noreplace) %{mpd_configfile}
%config(noreplace) %{_sysconfdir}/logrotate.d/mpd
%{_tmpfilesdir}/mpd.conf
%{_iconsdir}/hicolor/scalable/apps/mpd.svg

%defattr(-,%{mpd_user},%{mpd_group})
%dir %{mpd_homedir}
%dir %{mpd_logdir}
%dir %{mpd_musicdir}
%dir %{mpd_playlistsdir}
%ghost %dir %{mpd_rundir}
%ghost %{mpd_dbfile}
%ghost %{mpd_logfile}
%ghost %{mpd_statefile}

%changelog
* Sat Jun 27 2026 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1:0.24.12-5
- Rebuild for new fmt again

* Fri Jun 26 2026 Gwyn Ciesla <gwync@protonmail.com> - 1:0.24.12-4
- libupnp rebuild

* Thu Jun 25 2026 František Zatloukal <fzatlouk@redhat.com> - 1:0.24.12-3
- Rebuilt for fmt/spdlog

* Mon Jun 08 2026 František Zatloukal <fzatlouk@redhat.com> - 1:0.24.12-2
- Rebuilt for icu 78.3

* Wed May 20 2026 Benson Muite <fed500@fedoraproject.org> 1:0.24.12-1
- Package for Fedora main repositories

* Fri May 30 2025 Leigh Scott <leigh123linux@gmail.com> - 1:0.24.4-2
- Rebuild for new flac .so version

* Tue May 20 2025 Leigh Scott <leigh123linux@gmail.com> - 1:0.24.4-1
- Update to 0.24.4

* Thu Apr 10 2025 Leigh Scott <leigh123linux@gmail.com> - 1:0.24.3-1
- Update to 0.24.3

* Wed Mar 26 2025 Leigh Scott <leigh123linux@gmail.com> - 1:0.24.2-1
- Update to 0.24.2

* Sat Mar 22 2025 Leigh Scott <leigh123linux@gmail.com> - 1:0.24.1-1
- Update to 0.24.1

* Sat Mar 15 2025 Leigh Scott <leigh123linux@gmail.com> - 1:0.24-2
- Rebuild for new libnfs

* Wed Mar 12 2025 Leigh Scott <leigh123linux@gmail.com> - 1:0.24-1
- Update to 0.24

* Fri Feb 21 2025 Leigh Scott <leigh123linux@gmail.com> - 1:0.23.17-3
- Patch for new libnfs

* Thu Feb 13 2025 Leigh Scott <leigh123linux@gmail.com> - 1:0.23.17-2
- Rebuild for firewalld change

* Thu Jan 30 2025 Leigh Scott <leigh123linux@gmail.com> - 1:0.23.17-1
- Update to 0.23.17

* Tue Jan 28 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1:0.23.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Dec 03 2024 Leigh Scott <leigh123linux@gmail.com> - 1:0.23.16-1
- Update to 0.23.16

* Tue Oct 08 2024 Nicolas Chauvet <kwizart@gmail.com> - 1:0.23.15-6
- Rebuilt

* Fri Aug 02 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1:0.23.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jul 20 2024 Leigh Scott <leigh123linux@gmail.com> - 1:0.23.15-4
- Rebuild for new fmt version

* Sun Feb 04 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1:0.23.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 13 2024 Leigh Scott <leigh123linux@gmail.com> - 1:0.23.15-2
- Install html docs

* Wed Dec 20 2023 Leigh Scott <leigh123linux@gmail.com> - 1:0.23.15-1
- Update to 0.23.15

* Wed Nov 08 2023 Leigh Scott <leigh123linux@gmail.com> - 1:0.23.14-2
- Rebuild for new faad2 version

* Sun Oct 08 2023 Leigh Scott <leigh123linux@gmail.com> - 1:0.23.14-1
- Update to 0.23.14

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1:0.23.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jul 02 2023 Leigh Scott <leigh123linux@gmail.com> - 1:0.23.13-2
- rebuilt

* Mon May 22 2023 Leigh Scott <leigh123linux@gmail.com> - 1:0.23.13-1
- Update to 0.23.13

* Sat Mar 25 2023 Leigh Scott <leigh123linux@gmail.com> - 1:0.23.12-3
- Use systemd sysusers config to create user and group

* Tue Feb 28 2023 Leigh Scott <leigh123linux@gmail.com> - 1:0.23.12-2
- Rebuild for new ffmpeg

* Tue Jan 17 2023 Leigh Scott <leigh123linux@gmail.com> - 1:0.23.12-1
- Update to 0.23.12

* Mon Nov 28 2022 Leigh Scott <leigh123linux@gmail.com> - 1:0.23.11-1
- Update to 0.23.11

* Fri Oct 14 2022 Leigh Scott <leigh123linux@gmail.com> - 1:0.23.10-1
- Update to 0.23.10

* Fri Aug 19 2022 Leigh Scott <leigh123linux@gmail.com> - 1:0.23.9-1
- Update to 0.23.9

* Fri Jul 22 2022 Leigh Scott <leigh123linux@gmail.com> - 1:0.23.8-2
- Rebuild for new ffmpeg

* Sat Jul 09 2022 Leigh Scott <leigh123linux@gmail.com> - 1:0.23.8-1
- Update to 0.23.8

* Tue May 10 2022 Leigh Scott <leigh123linux@gmail.com> - 1:0.23.7-1
- Update to 0.23.7

* Mon Mar 14 2022 Leigh Scott <leigh123linux@gmail.com> - 1:0.23.6-1
- Update to 0.23.6

* Sat Feb 05 2022 Leigh Scott <leigh123linux@gmail.com> - 1:0.23.5-2
- Rebuilt for ffmpeg

* Thu Dec 09 2021 Leigh Scott <leigh123linux@gmail.com> - 1:0.23.5-1
- Update to 0.23.5

* Tue Nov 16 2021 Leigh Scott <leigh123linux@gmail.com> - 1:0.23.4-1
- Update to 0.23.4

* Tue Nov 09 2021 Leigh Scott <leigh123linux@gmail.com> - 1:0.23.3-2
- Rebuilt for new ffmpeg snapshot

* Sun Oct 31 2021 Leigh Scott <leigh123linux@gmail.com> - 1:0.23.3-1
- Update to 0.23.3

* Fri Oct 22 2021 Leigh Scott <leigh123linux@gmail.com> - 1:0.23.2-1
- Update to 0.23.2

* Tue Oct 19 2021 Leigh Scott <leigh123linux@gmail.com> - 1:0.23.1-1
- Update to 0.23.1

* Mon Oct 18 2021 Leigh Scott <leigh123linux@gmail.com> - 1:0.23-2
- Fix pipewire samplerate

* Thu Oct 14 2021 Leigh Scott <leigh123linux@gmail.com> - 1:0.23-1
- Update to 0.23

* Fri Aug 27 2021 Leigh Scott <leigh123linux@gmail.com> - 1:0.22.11-1
- Update to 0.22.11

* Sat Aug 07 2021 Leigh Scott <leigh123linux@gmail.com> - 1:0.22.10-1
- Update to 0.22.10

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:0.22.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 23 2021 Leigh Scott <leigh123linux@gmail.com> - 1:0.22.9-1
- Update to 0.22.9

* Tue Jun 08 2021 Leigh Scott <leigh123linux@gmail.com> - 1:0.22.8-2
- Drop fluidsynth support due to poor fedora maintenance (.so bumps to stable releases)

* Sun May 23 2021 Leigh Scott <leigh123linux@gmail.com> - 1:0.22.8-1
- Update to 0.22.8

* Fri May 21 2021 Leigh Scott <leigh123linux@gmail.com> - 1:0.22.7-1
- Update to 0.22.7

* Tue May 11 2021 Leigh Scott <leigh123linux@gmail.com> - 1:0.22.6-2
- rebuilt

* Wed Feb 17 2021 Leigh Scott <leigh123linux@gmail.com> - 1:0.22.6-1
- Update to 0.22.6

* Mon Feb 15 2021 Leigh Scott <leigh123linux@gmail.com> - 1:0.22.5-1
- Update to 0.22.5

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:0.22.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 21 2021 Leigh Scott <leigh123linux@gmail.com> - 1:0.22.4-1
- Update to 0.22.4

* Wed Jan  6 2021 Leigh Scott <leigh123linux@gmail.com> - 1:0.22.3-3
- Disable adplug support

* Thu Dec 31 2020 Leigh Scott <leigh123linux@gmail.com> - 1:0.22.3-2
- Rebuilt for new ffmpeg snapshot

* Fri Nov  6 2020 Leigh Scott <leigh123linux@gmail.com> - 1:0.22.3-1
- Update to 0.22.3

* Wed Oct 28 2020 Leigh Scott <leigh123linux@gmail.com> - 1:0.22.2-1
- Update to 0.22.2

* Sat Oct 17 2020 Leigh Scott <leigh123linux@gmail.com> - 1:0.22.1-1
- Update to 0.22.1

* Sun Oct 11 2020 Leigh Scott <leigh123linux@gmail.com> - 1:0.22-1
- Update to 0.22

* Wed Sep 23 2020 Leigh Scott <leigh123linux@gmail.com> - 1:0.21.26-1
- Update to 0.21.26

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:0.21.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 18 2020 Leigh Scott <leigh123linux@gmail.com> - 1:0.21.25-2
- Rebuilt

* Wed Jul 08 2020 Leigh Scott <leigh123linux@gmail.com> - 1:0.21.25-1
- Update to 0.21.25

* Thu Jun 11 2020 Leigh Scott <leigh123linux@gmail.com> - 1:0.21.24-1
- Update to 0.21.24

* Fri Apr 24 2020 Leigh Scott <leigh123linux@gmail.com> - 1:0.21.23-1
- Update to 0.21.23

* Fri Apr 10 2020 Leigh Scott <leigh123linux@gmail.com> - 1:0.21.22-2
- Rebuild for new libcdio version

* Sat Apr 04 2020 leigh123linux <leigh123linux@googlemail.com> - 1:0.21.22-1
- Update to 0.21.22

* Thu Mar 19 2020 Leigh Scott <leigh123linux@gmail.com> - 1:0.21.21-1
- Update to 0.21.21

* Sat Feb 22 2020 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1:0.21.20-2
- Rebuild for ffmpeg-4.3 git

* Thu Feb 20 2020 Leigh Scott <leigh123linux@gmail.com> - 1:0.21.20-1
- Update to 0.21.20

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:0.21.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Leigh Scott <leigh123linux@gmail.com> - 1:0.21.19-1
- Update to 0.21.19

* Wed Dec 25 2019 Leigh Scott <leigh123linux@gmail.com> - 1:0.21.18-1
- Update to 0.21.18

* Tue Dec 17 2019 Leigh Scott <leigh123linux@gmail.com> - 1:0.21.17-1
- Update to 0.21.17

* Sun Dec 01 2019 Leigh Scott <leigh123linux@googlemail.com> - 1:0.21.16-2
- Rebuilt for new libicu

* Wed Oct 16 2019 Leigh Scott <leigh123linux@googlemail.com> - 1:0.21.16-1
- Update to 0.21.16

* Thu Sep 26 2019 Leigh Scott <leigh123linux@googlemail.com> - 1:0.21.15-1
- Update to 0.21.15

* Wed Sep 11 2019 Leigh Scott <leigh123linux@googlemail.com> - 1:0.21.14-3
- Rebuild for new libnfs version

* Sat Aug 31 2019 Leigh Scott <leigh123linux@gmail.com> - 1:0.21.14-2
- Rebuild for libsidplayfp-2.0.0 (rfbz #5374)

* Thu Aug 22 2019 Leigh Scott <leigh123linux@googlemail.com> - 1:0.21.14-1
- Update to 0.21.14

* Mon Aug 12 2019 Leigh Scott <leigh123linux@gmail.com> - 1:0.21.13-1
- Update to 0.21.13

* Tue Aug 06 2019 Leigh Scott <leigh123linux@gmail.com> - 1:0.21.12-2
- Rebuild for new ffmpeg version

* Sat Aug 03 2019 Leigh Scott <leigh123linux@gmail.com> - 1:0.21.12-1
- Update to 0.21.12

* Thu Jul 04 2019 Leigh Scott <leigh123linux@googlemail.com> - 1:0.21.11-1
- Update to 0.21.11
- Clean up

* Sat Jun 08 2019 Leigh Scott <leigh123linux@googlemail.com> - 1:0.21.10-1
- Update to 0.21.10

* Wed May 22 2019 Leigh Scott <leigh123linux@googlemail.com> - 1:0.21.9-1
- Update to 0.21.9

* Wed Apr 24 2019 Leigh Scott <leigh123linux@googlemail.com> - 1:0.21.8-1
- Update to 0.21.8

* Wed Apr 03 2019 Leigh Scott <leigh123linux@googlemail.com> - 1:0.21.7-1
- Update to 0.21.7
- Add upstream commit to fix gcc-9 build issue

* Mon Mar 18 2019 Leigh Scott <leigh123linux@googlemail.com> - 1:0.21.6-1
- Update to 0.21.6

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:0.21.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Feb 25 2019 Leigh Scott <leigh123linux@googlemail.com> - 1:0.21.5-2
- Add BuildRequires firewalld-filesystem

* Sat Feb 23 2019 Leigh Scott <leigh123linux@googlemail.com> - 1:0.21.5-1
- Update to 0.21.5
- Force python3-sphinx for docs

* Wed Jan 16 2019 Leigh Scott <leigh123linux@googlemail.com> - 1:0.21.4-2
- Add firewalld sub-package

* Mon Jan 14 2019 Leigh Scott <leigh123linux@googlemail.com> - 1:0.21.4-1
- Update to 0.21.4
- Add changes for meson build

* Thu Oct 25 2018 Leigh Scott <leigh123linux@googlemail.com> - 1:0.20.22-1
- Update to 0.20.22
- Switch buildroot macro

* Wed Oct 17 2018 Leigh Scott <leigh123linux@googlemail.com> - 1:0.20.21-1
- Update to 0.20.21
- Remove Group tag

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:0.20.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1:0.20.19-2
- Update to add BRs for plugins
- rpmfusionbz: 4961

* Sun Apr 29 2018 Sérgio Basto <sergio@serjux.com> - 1:0.20.19-1
- Update 0.20.19

* Thu Mar 08 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1:0.20.16-3
- Rebuilt for new ffmpeg snapshot

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1:0.20.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Feb 06 2018 Leigh Scott <leigh123linux@googlemail.com> - 1:0.20.16-1
- Update to 0.20.16

* Sun Jan 28 2018 Nicolas Chauvet <kwizart@gmail.com> - 1:0.20.15-1
- Update to 0.20.15

* Sun Jan 28 2018 Nicolas Chauvet <kwizart@gmail.com> - 1:0.20.10-5
- Rebuilt for libcdio

* Thu Jan 18 2018 Leigh Scott <leigh123linux@googlemail.com> - 1:0.20.10-4
- Rebuilt for ffmpeg-3.5 git

* Mon Oct 16 2017 Leigh Scott <leigh123linux@googlemail.com> - 1:0.20.10-3
- Rebuild for ffmpeg update

* Sat Oct 07 2017 Leigh Scott <leigh123linux@googlemail.com> - 1:0.20.10-2
- Enable sidplay (rfbz #2305)

* Sat Oct 07 2017 Leigh Scott <leigh123linux@googlemail.com> - 1:0.20.10-1
- Update to 0.20.10
- Remove NoNewPrivileges (rfbz #4549)

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1:0.20.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 22 2017 Nicolas Chauvet <kwizart@gmail.com> - 1:0.20.8-1
- Update to 0.20.8

* Sat Apr 29 2017 Leigh Scott <leigh123linux@googlemail.com> - 1:0.20.6-2
- Rebuild for ffmpeg update

* Mon Apr 10 2017 Leigh Scott <leigh123linux@googlemail.com> - 1:0.20.6-1
- Update to latest upstream version
- Add systemd user service (rfbz #3768)
