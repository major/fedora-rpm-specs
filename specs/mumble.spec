# Test suite only works on x86_64
# https://github.com/mumble-voip/mumble/issues/3845
%ifarch x86_64
%bcond_without tests
%endif

%global build_number 287

Name:           mumble
Version:        1.4.%{build_number}
Release:        7%{?dist}
Summary:        Low-latency and high-quality voice-chat program
# primary license: BSD-3-Clause
# themes/Mumble: Unlicense and WTFPL
# 3rdparty/arc4random: ISC
# 3rdparty/celt-0.7.0-src: BSD-3-Clause and GPL-2.0-or-later
# 3rdparty/qqbonjour: BSD-3-Clause
# 3rdparty/smallft: BSD-3-Clause
License:        BSD-3-Clause AND Unlicense AND WTFPL AND ISC AND GPL-2.0-or-later
URL:            https://www.mumble.info
Source:         https://github.com/mumble-voip/mumble/releases/download/v%{version}/mumble-%{version}.tar.gz
Source1:        murmur.service
Source2:        mumble-server.sysusers

# patches from the upstream master branch
# https://github.com/mumble-voip/mumble/commit/f4cea62ed95e4967d8591f25e903f5e8fc2e2a30
Patch:          0001-BUILD-crypto-Migrate-to-OpenSSL-3.0-compatible-API.patch
# https://github.com/mumble-voip/mumble/commit/f8d47db318f302f5a7d343f15c9936c7030c49c4
Patch:          0002-FIX-crypto-Sharing-EVP-context-between-threads-crushes-Mumble.patch

# downstream-only patches
# https://docs.fedoraproject.org/en-US/packaging-guidelines/CryptoPolicies/
Patch:          0003-CHANGE-server-Default-to-system-crypto-policy.patch
Patch:          0004-FIX-client-Avoid-loading-unversioned-libraries.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++

# Referencing build requirements:
#
# - Find instances of find_pkg and find_library in the mumble source code.
# - Ensure that the instance applies based on the conditionals.
# - Check if anything provides cmake(<name>).  If found use that.
# - Check the modules from cmake-data (/usr/share/cmake/Modules/) to see if any
#   locate it by a file path.  If found use exact package name.
# - Check if anything provides pkgconfig(<name>).  If found, use that.
#
# docs/dev/build-instructions/cmake_options.md
#
# That should cover most scenarios.  If you are working on this spec file and
# find another scenario, please add it to this list.

# cmake/os.cmake
BuildRequires:  pkgconfig(openssl)
BuildRequires:  cmake(Qt5)

# cmake/qt-utils.cmake
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  python3

# src/CMakeLists.txt
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(protobuf)

# src/mumble/CMakeLists.txt
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(PocoXML)
BuildRequires:  cmake(PocoZip)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  boost-devel
BuildRequires:  libXext-devel
BuildRequires:  libXi-devel
BuildRequires:  glibc-devel
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(speex)
BuildRequires:  pkgconfig(speexdsp)
BuildRequires:  pkgconfig(rnnoise)
BuildRequires:  pkgconfig(speech-dispatcher)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  pkgconfig(avahi-compat-libdns_sd)
BuildRequires:  alsa-lib-devel
BuildRequires:  pipewire-jack-audio-connection-kit-devel
BuildRequires:  pipewire-devel
BuildRequires:  portaudio-devel
BuildRequires:  pulseaudio-libs-devel

%if %{with tests}
# src/tests/CMakeLists.txt
BuildRequires:  cmake(Qt5Test)
%endif

# multiple files in 3rdparty/celt-0.7.0-src
BuildRequires:  libogg-devel

# appstream-util in %%check
BuildRequires:  libappstream-glib
# desktop-file-validate in %%check
BuildRequires:  desktop-file-utils

# There are multiple available audio backends which are opened at runtime.
# They aren't linked against, but they are opened by the library name.
# https://github.com/mumble-voip/mumble/issues/3794
%if 0%{?__isa_bits} == 32
%global libsymbolsuffix %{nil}
%else
%global libsymbolsuffix ()(%{__isa_bits}bit)
%endif
# src/mumble/JackAudio.cpp
Recommends:     libjack.so.0%{libsymbolsuffix}
# to prefer the pipewire implementation of libjack
Suggests:       pipewire-jack-audio-connection-kit
# src/mumble/PAAudio.cpp
Recommends:     libportaudio.so.2%{libsymbolsuffix}
# src/mumble/PipeWire.cpp
Recommends:     libpipewire-0.3.so.0%{libsymbolsuffix}
# src/mumble/PulseAudio.cpp
Recommends:     libpulse.so.0%{libsymbolsuffix}

# modified version of OpenBSD's arc4random
Provides:       bundled(arc4random)
# old version of celt for compatibility
Provides:       bundled(celt) = 0.7.0
# modified version of Qt Quarterly example code
Provides:       bundled(qqbonjour)
# modified version of vorbis's smallft
Provides:       bundled(smallft)

ExcludeArch:    %{ix86}

%global _privatelibs libcelt0[.]so.*
%global __provides_exclude ^(%{_privatelibs})$
%global __requires_exclude ^(%{_privatelibs})$


%description
Mumble is an Open Source, low-latency and high-quality voice-chat program
written on top of Qt and Opus.


%package server
Summary:        Mumble voice chat server

# Renamed from murmur to mumble-server, per upstream preference.  Obsoletes
# added in F37, can be removed in F39.
# https://github.com/mumble-voip/mumble/issues/5436#issuecomment-1084917505
Provides:       murmur = %{version}-%{release}
Obsoletes:      murmur < 1.3.4-10

# src/murmur/CMakeLists.txt
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  libcap-devel
BuildRequires:  pkgconfig(avahi-compat-libdns_sd)
BuildRequires:  cmake(Qt5DBus)

BuildRequires:  systemd-rpm-macros

# To be able to announce the presence of the server via Bonjour.
Recommends:     avahi

%{?systemd_requires}
%{?sysusers_requires_compat}


%description server
mumble-server (also called murmur) is part of the VoIP suite Mumble primarily
aimed at gamers.


%package plugins
Summary:        Plugins for VoIP program Mumble
Requires:       %{name} = %{version}-%{release}


%description plugins
Mumble-plugins is part of VoIP suite Mumble primarily intended for gamers. This
plugin allows game linking so the voice of players will come from the direction
of their characters.


%package overlay
Summary:        Start games with the mumble overlay
Requires:       %{name} = %{version}-%{release}


%description overlay
Mumble-overlay is part of the Mumble VoIP suite aimed at gamers. If supported,
starting your game with this script will enable an ingame Mumble overlay.


%prep
%autosetup -p 1 -n mumble-%{version}.src

pushd 3rdparty

# remove bundled libraries that we have system copies of
rm -r jack opus pipewire portaudio pulseaudio rnnoise* speex*

# remove bundled libraries for windows
rm -r GL minhook xinputcheck*

# remove bundled libraries for mac
rm -r mach-override*

popd

# use system headers for audio backends
sed \
    -e 's|"${3RDPARTY_DIR}/jack"|"%{_includedir}/jack"|' \
    -e 's|"${3RDPARTY_DIR}/portaudio"|"%{_includedir}"|' \
    -e 's|"${3RDPARTY_DIR}/pipewire"|"%{_includedir}/pipewire-0.3" "%{_includedir}/spa-0.2"|' \
    -e 's|"${3RDPARTY_DIR}/pulseaudio"|"%{_includedir}/pulse"|' \
    -i src/mumble/CMakeLists.txt


%build
%cmake \
    -DBUILD_NUMBER=%{build_number} \
    %{?with_tests:-Dtests=ON} \
    -Dupdate=OFF \
    -Dbundled-opus=OFF \
    -Dbundled-speex=OFF \
    -Dbundled-rnnoise=OFF \
    -Dice=OFF \
    -Doverlay-xcompile=OFF \
    -DCMAKE_BUILD_TYPE=Release

%cmake_build


%install
%cmake_install

# translations
install -d -m 0755 %{buildroot}%{_datadir}/mumble/translations
install -p -m 0644 %{_vpath_builddir}/src/mumble/*.qm %{buildroot}%{_datadir}/mumble/translations

install -D -p -m 0664 scripts/murmur.ini %{buildroot}%{_sysconfdir}/murmur.ini
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/murmur.service
install -D -p -m 0644 %{SOURCE2} %{buildroot}%{_sysusersdir}/mumble-server.conf
install -D -p -m 0755 scripts/mumble-server-user-wrapper %{buildroot}%{_bindir}/mumble-server-user-wrapper

# dir for mumble-server.sqlite
mkdir -p %{buildroot}%{_localstatedir}/lib/mumble-server/

# compatibility symlinks
mkdir -p %{buildroot}%{_sbindir}
ln -s %{_bindir}/mumble-server %{buildroot}%{_sbindir}/murmurd


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/info.mumble.Mumble.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/info.mumble.Mumble.desktop

%if %{with tests}
%ctest
%endif


# added in F37, can be removed in F39
%posttrans server
# relocation of config file
if [ -f %{_sysconfdir}/murmur/murmur.ini.rpmsave ]; then
    mv -vf %{_sysconfdir}/murmur.ini %{_sysconfdir}/murmur.ini.rpmnew
    mv -vf %{_sysconfdir}/murmur/murmur.ini.rpmsave %{_sysconfdir}/murmur.ini
fi
rmdir --ignore-fail-on-non-empty %{_sysconfdir}/murmur


%pre server
%sysusers_create_compat %{SOURCE2}


%post server
%systemd_post murmur.service


%preun server
%systemd_preun murmur.service


%postun server
%systemd_postun_with_restart murmur.service


%files
%license LICENSE
%doc README.md CHANGES
%{_bindir}/mumble
%{_mandir}/man1/mumble.1*
%{_datadir}/icons/hicolor/256x256/apps/mumble.png
%{_datadir}/icons/hicolor/scalable/apps/mumble.svg
%{_datadir}/applications/info.mumble.Mumble.desktop
%{_metainfodir}/info.mumble.Mumble.appdata.xml
%{_datadir}/mumble/
%dir %{_libdir}/mumble/
%{_libdir}/mumble/libcelt0.so
%{_libdir}/mumble/libcelt0.so.0.7.0


%files server
%license LICENSE
%doc README.md CHANGES
%{_bindir}/mumble-server
%{_bindir}/mumble-server-user-wrapper
%{_mandir}/man1/mumble-server.1*
%{_mandir}/man1/mumble-server-user-wrapper.1*
%{_sbindir}/murmurd
%{_unitdir}/murmur.service
%{_sysusersdir}/mumble-server.conf
%config(noreplace) %attr(664,mumble-server,mumble-server) %{_sysconfdir}/murmur.ini
%dir %attr(-,mumble-server,mumble-server) %{_localstatedir}/lib/mumble-server/


%files plugins
%{_libdir}/mumble/plugins/


%files overlay
%{_bindir}/mumble-overlay
%{_mandir}/man1/mumble-overlay.1*
%{_libdir}/mumble/libmumbleoverlay.so
%{_libdir}/mumble/libmumbleoverlay.so.%{version}


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.287-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.287-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Apr 22 2024 Carl George <carlwgeorge@fedoraproject.org> - 1.4.287-5
- Rebuilt for poco 1.13.3 rhbz#2274227 rhbz#2276278

* Wed Mar 06 2024 Carl George <carlwgeorge@fedoraproject.org> - 1.4.287-4
- Rebuilt for poco 1.13.2 rhbz#2264958

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.287-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.287-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Oct 07 2023 Carl George <carlwgeorge@fedoraproject.org> - 1.4.287-1
- Update to version 1.4.287, resolves rhbz#2126913
- Switch to SPDX license notation
- Move mumble-server user creation from %%posttrans to %%pre

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.274-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jan 24 2023 Carl George <carl@george.computer> - 1.4.274-5
- Rebuild for poco 1.12.4, resolves rhbz#2163844

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.274-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Dec 11 2022 spike <spike@fedoraproject.org> - 1.4.274-3
- Fix non-existent source when calling sysusers_create_compat macro

* Tue Oct 25 2022 Carl George <carl@george.computer> - 1.4.274-2
- Rebuilt for poco 1.12.3

* Mon Aug 22 2022 Carl George <carl@george.computer> - 1.4.274-1
- Latest upstream, resolves rhbz#2120162

* Sat Aug 20 2022 Carl George <carl@george.computer> - 1.4.230-2
- Rename murmur config in %%posttrans instead of %%pre
- Drop symlinks for other possible config paths

* Tue Aug 09 2022 Carl George <carl@george.computer> - 1.4.230-1
- Latest upstream, resolves rhbz#2036444
- Move murmur config file from /etc/murmur/murmur.ini to /etc/murmur.ini
- Rename mumur to mumble-server
- Create mumble-server user with sysusers
- Run test suite on x86_64
- Drop i686 build

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Nov 18 2021 Carl George <carl@george.computer> - 1.3.4-7
- Fix openssl build requirement
- Resolves: rhbz#2021964

* Tue Oct 26 2021 Adrian Reber <adrian@lisas.de> - 1.3.4-6
- Rebuilt for protobuf 3.18.1

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.3.4-5
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 09 2021 Carl George <carl@george.computer> - 1.3.4-3
- Disable PCH to fix epel8 build rhbz#1791391

* Wed Mar 17 2021 Carl George <carl@george.computer> - 1.3.4-2
- Enable RNNoise noise suppression
- Fixes: rhbz#1921721

* Sun Mar 14 2021 Carl George <carl@george.computer> - 1.3.4-1
- Latest upstream

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.3.3-4
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 08:32:14 CET 2021 Adrian Reber <adrian@lisas.de> - 1.3.3-2
- Rebuilt for protobuf 3.14

* Mon Dec 21 2020 Carl George <carl@george.computer> - 1.3.3-1
- Latest upstream rhbz#1885088
- Update license to reflect bundled libraries
- Add virtual provides for bundled libraries
- Remove celt071 dependency rhbz#1904471
- Remove obsolete for mumble-protocol
- Remove non-root ownership of murmurd
- Remove weblist perl and php scripts from %%doc

* Fri Sep 25 2020 Adrian Reber <adrian@lisas.de> - 1.3.2-2
- Rebuilt(2) for protobuf 3.13

* Fri Sep 25 2020 Carl George <carl@george.computer> - 1.3.2-1
- Latest upstream
- Add upstream patch for push-to-talk dbus calls

* Thu Sep 24 2020 Adrian Reber <adrian@lisas.de> - 1.3.0-7
- Rebuilt for protobuf 3.13

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 14 2020 Adrian Reber <adrian@lisas.de> - 1.3.0-4
- Rebuilt for protobuf 3.12

* Wed Jun 03 2020 Rex Dieter <rdieter@fedoraproject.org> - 1.3.0-3
- mumble: drop qt5-qtbase-sqlite dep (#1832458)

* Fri Apr 24 2020 Rex Dieter <rdieter@fedoraproject.org> - 1.3.0-2
- fix Qt5 deps

* Fri Mar 20 2020 Nils Philippsen <nils@tiptoe.de> - 1.3.0-1
- version 1.3.0
- update build deps, patches and drop obsolete ones
- build with Qt 5

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.19-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.19-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 17 2019 Rex Dieter <rdieter@fedoraproject.org> - 1.2.19-14
- mumble-1.2.19-13: Unable to find matching CELT codecs with other clients (#1711435)
- support no_bundled_celt macro

* Thu May 16 2019 Rex Dieter <rdieter@fedoraproject.org> - 1.2.19-13
- pull in more upstream fixes (ssl ciphers, opengl link flags)
- CONFIG+=no-oss

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.19-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 21 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.19-11
- Rebuild for protobuf 3.6

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.19-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 23 2018 Filipe Rosset <rosset.filipe@gmail.com> - 1.2.19-9
- drop deprecated libXevie-devel usage to fix FTBFS on rawhide

* Wed Mar 21 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.2.19-8
- fix FTBFS (#1555858)
- pull in upstream appdata (#1501525)
- use %%make_build %%{?systemd_requires}
- build in c++-11 mode (fixes FTBFS on s390x wrt protobuf)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.19-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.19-6
- Remove obsolete scriptlets

* Wed Nov 29 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.2.19-5
- Rebuild for protobuf 3.5

* Mon Nov 13 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.19-4
- Rebuild for protobuf 3.4

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 18 2017 Filipe Rosset <rosset.filipe@gmail.com> - 1.2.19-1
- Rebuilt for new upstream release 1.2.19, fixes rhbz#1417330
- Added a patch to fix rhbz#1454438 until upstream fixes it
- Fixes rhbz#1462279 regarding desktop file

* Tue Jun 13 2017 Orion Poplawski <orion@cora.nwra.com> - 1.2.18-4
- Rebuild for protobuf 3.3.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 26 2017 Orion Poplawski <orion@cora.nwra.com> - 1.2.18-2
- Rebuild for protobuf 3.2.0

* Thu Dec 15 2016 Filipe Rosset <rosset.filipe@gmail.com> - 1.2.18-1
- Rebuilt for new upstream release 1.2.18, fixes rhbz #1293181

* Sat Nov 19 2016 Orion Poplawski <orion@cora.nwra.com> - 1.2.11-4
- Rebuild for protobuf 3.1.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 7 2015 John Popplewell <johnhatestrash@gmail.com> - 1.2.11-2
- Removed perl dependency and all deprecated d-bus rpc support

* Sun Dec 6 2015 John Popplewell <johnhatestrash@gmail.com> - 1.2.11-1
- Update to 1.2.11
- Added mumble-FixNoBindAtBoot.patch mumble-murmur_exit_on_no_bind.patch

* Wed Nov 25 2015 John Popplewell <johnhatestrash@gmail.com> - 1.2.10-4
- Hardened murmur.service
- Added patch to disable murmur.ini d-bus rpc - remove on 1.3.0

* Wed Nov 25 2015 John Popplewell <johnhatestrash@gmail.com> - 1.2.10-3
- Added ppc support
- Marked LICENSE with license tag
- Added patch to modify murmur.ini with PROFILE=SYSTEM sslCipher= setting

* Tue Nov 24 2015 John Popplewell <johnhatestrash@gmail.com> - 1.2.10-2
- Removed protocol subpkg, added Obsoletes mumble-protocol < 1.2.10-2
- Made recommended review changes (qmake_qt4, added parallel make, qt4-devel in favor of qt-devel)

* Tue Nov 24 2015 John Popplewell <johnhatestrash@gmail.com> - 1.2.10-1
- Update to 1.2.10
- Drop ice

* Tue Jan 13 2015 Carlos O'Donell <codonell@redhat.com> - 1.2.6-5
- Rebuilt against new ice-devel.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 1.2.6-2
- Rebuild for boost 1.55.0

* Sat May 17 2014 Christian Krause <chkr@fedoraproject.org> - 1.2.6-1
- Update 1.2.6
- Update fixes CVE-2014-3755 (BZ 1098231) and CVE-2014-3756 (BZ 1098233)

* Fri Apr 25 2014 Christian Krause <chkr@fedoraproject.org> - 1.2.5-1
- Update 1.2.5 (BZ 1062209)
- Update fixes CVE-2014-0044 (BZ 1061857) and CVE-2014-0045 (BZ 1061858)
- Add patch to fix an compile error with g++ 4.9.0
- Remove upstreamed patch for CVE-2012-0863

* Tue Aug 27 2013 Christian Krause <chkr@fedoraproject.org> - 1.2.4-1
- Update 1.2.4 (BZ 976001)
- New systemd-rpm macros (BZ 850218)
- Cleanup

* Mon Aug 19 2013 Peter Robinson <pbrobinson@fedoraproject.org> 1.2.3-16
- Fix FTBFS due to speechd
- Drop alsa-oss support

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 1.2.3-14
- Rebuild for boost 1.54.0

* Wed Apr 03 2013 Christian Krause <chkr@fedoraproject.org> - 1.2.3-13
- Rebuild against new ice package
- Updated Ice version in patch0

* Sun Mar 17 2013 Christian Krause <chkr@fedoraproject.org> - 1.2.3-12
- Rebuild against new protobuf package

* Wed Feb 06 2013 Christian Krause <chkr@fedoraproject.org> - 1.2.3-11
- Rebuild against new ice package
- Updated Ice version in patch0
- Use new systemd-rpm macros (BZ 850218)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May 31 2012 Christian Krause <chkr@fedoraproject.org> - 1.2.3-9
- Fix startup issues of murmurd (BZ 711711, BZ 770469, BZ 771423)
- Fix migration to systemd
  http://fedoraproject.org/wiki/Packaging:ScriptletSnippets#Systemd
- Fix directory ownership of %%{_libdir}/mumble and %%{_datadir}/mumble*
  (BZ 744886)
- Add upstream patch for CVE-2012-0863 (BZ 791058)
- Fix broken logrotate config file (BZ 730129)
- Add dependency for qt4-sqlite (BZ 660221)
- Remove /sbin/ldconfig from %%post(un) since mumble does not
  contain any libraries in %%{_libdir}
- Some minor cleanup

* Wed Apr 18 2012 Jon Ciesla <limburgher@gmail.com> - 1.2.3-8
- Migrate to systemd, BZ 790040.

* Fri Mar 16 2012 Tom Callaway <spot@fedoraproject.org> - 1.2.3-7
- rebuild against fixed ice

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 10 2011 Andreas Osowski <th0br0@mkdir.name> - 1.2.3-5
- Updated Ice version in patch0
- Added new patch to build against celt071 includes thanks to Florent Le Coz

* Thu Nov 10 2011 Andreas Osowski <th0br0@mkdir.name> - 1.2.3-4
- rebuilt for protobuf update

* Mon Sep 12 2011 Andreas Osowski <th0br0@mkdir.name> - 1.2.3-3
- Rebuild for newer protobuf

* Tue May 17 2011 Andreas Osowski <th0br0@mkdir.name> - 1.2.3-2
- Added celt071 functionality
- Fixed the qmake args

* Wed Mar 30 2011 Andreas Osowski <th0br0@mkdir.name> - 1.2.3-1
- Update to 1.2.3
- Fixes vulnerability #610845
- Added patch to make it compile with Ice 3.4.0
- Added tmpfile.d config file for murmur

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 25 2010 Andreas Osowski <th0br0@mkdir.name> - 1.2.2-10
- Actually removed the requirement for redhat-lsb

* Tue Aug 03 2010 Andreas Osowski <th0br0@mkdir.name> - 1.2.2-9
- Removed redhat-lsb from Requires for murmur
- Updated initscript for murmur

* Sun May 16 2010 Andreas Osowski <th0br0@mkdir.name> - 1.2.2-8
- Rebuild for protobuf ABI change
- Added redhat-lsb to the Requires for murmur

* Sun May  2 2010 Andreas Osowski <th0br0@mkdir.name> - 1.2.2-7
- Fixed murmur's init script

* Sun Apr 18 2010 Andreas Osowski <th0br0@mkdir.name> - 1.2.2-6
- Fix for missing dbus-qt-devel on >F12

* Sun Apr 18 2010 Andreas Osowski <th0br0@mkdir.name> - 1.2.2-5
- Merged Mary Ellen Foster's changelog entry

* Tue Mar 30 2010 Andreas Osowski <th0br0@mkdir.name> - 1.2.2-4
- Marked the files in /etc as config entries

* Tue Mar 23 2010 Andreas Osowski <th0br0@mkdir.name> - 1.2.2-3
- Added desktop file for mumble11x

* Mon Feb 22 2010 Julian Golderer <j.golderer@novij.at> - 1.2.2-2
- Added mumble11x
- Added svg icons
- Added language files

* Sun Feb 21 2010 Andreas Osowski <th0br0@mkdir.name> - 1.2.2-1
- Update to 1.2.2
