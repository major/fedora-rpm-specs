Name:           hedgewars
Version:        1.0.2
Release:        9%{?dist}
Summary:        Funny turn-based artillery game, featuring fighting Hedgehogs!
License:        GPL-1.0-or-later
URL:            http://www.hedgewars.org/

Source0:        http://www.hedgewars.org/download/releases/%{name}-src-%{version}.tar.bz2
# SystemD service file for hedgewars-server
Source100:      hedgewars.service
# Environment file for systemd
Source101:      hedgewars.sysconfig
# FirewallD config
Source102:      hedgewars.xml

# Prevent use of rpath
Patch0:         rpath-fix.patch

# Tweak CFLAGS for clang
Patch1:         hedgewars-clang.patch

# Install hwengine.desktop
Patch2:        hedgewars-1.0.0-install-hwengine.patch

Patch3:        0a8921bf167481045830095c731eb3c67af913e4.patch

# fix pas2c for ghc-9.4
# https://github.com/hedgewars/hw/pull/75
Patch4:        https://patch-diff.githubusercontent.com/raw/hedgewars/hw/pull/75.patch
Patch5:        hedgewars-mtl-2.3.patch

BuildRequires:  cmake gcc-c++ fpc desktop-file-utils
BuildRequires:  libatomic
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  SDL2_mixer-devel SDL2_net-devel SDL2_image-devel SDL2_ttf-devel
BuildRequires:  openssl-devel libpng-devel physfs-devel glew-devel
BuildRequires:  dejavu-sans-fonts wqy-zenhei-fonts clang
Requires:       dejavu-sans-fonts wqy-zenhei-fonts hicolor-icon-theme
Requires:       hedgewars-data = %{version}-%{release}

ExclusiveArch:  %{fpc_arches}
ExcludeArch: ppc64le

%description
Hedgewars is a turn based strategy game but the real buzz is from watching the
devastation caused by those pesky hedgehogs with those fantastic weapons.

Each player controls a team of several hedgehogs. During the course of the
game, players take turns with one of their hedgehogs. They then use whatever
tools and weapons are available to attack and kill the opponents' hedgehogs,
thereby winning the game. Hedgehogs may move around the terrain in a variety
of ways, normally by walking and jumping but also by using particular tools
such as the "Rope" or "Parachute", to move to otherwise inaccessible areas.

%package server
Summary:        Standalone server for hedgewars
Requires:       %{name}%{?_isa} = %{version}-%{release}
BuildRequires:  ghc-SHA-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-entropy-devel
BuildRequires:  ghc-hslogger-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-regex-tdfa-devel
BuildRequires:  ghc-sandi-devel
BuildRequires:  ghc-utf8-string-devel
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-zlib-devel
BuildRequires:  compat-lua-devel
BuildRequires:  systemd
%{?systemd_requires}

%description server
A standalone server that can be used for LAN play or a private internet server.

%package data
BuildArch:      noarch
Summary:        Game data for %{name}

%description data
Game data for %{name}.


%prep
%autosetup -p1 -n %{name}-src-%{version}

# Make sure that we don't use bundled libraries
rm -r misc/liblua

# Fix these to files as pas2c choked on the UTF-8 files.
for file in hedgewars/uSound.pas hedgewars/uStats.pas; do
    iconv -f utf-8 -t ascii//TRANSLIT $file -o $file.tmp;
    mv $file.tmp $file;
done


%build
# We follow upstream and build with clang, some of the rpm macros need to know this:
# 1. This sets _lto_cflags for clang rather then gcc
# 2. This fixes armv7hl build in combination with .package.note generation
%define toolchain clang

# https://bugzilla.redhat.com/show_bug.cgi?id=1878396
%define _legacy_common_support 1

# -DMINIMAL_FLAGS=1 uses distro complie flags as much as possible

# -DNOVIDEOREC=1 disables video recording which for now needs
# things Fedora can't provide.

# -DGHFLAGS=-dynamic uses dynamic linking for Haskell, but this isn't
# available on arm.

# -DFONTS_DIRS="`find %{_datadir}/fonts -type d -printf '%p;'`"
# makes sure the system fonts are used. This avoids problems with physfs access
# and having to symlink font files.

export CFLAGS="%{build_cflags} -DGL_GLEXT_PROTOTYPES"
export CXXFLAGS="%{build_cxxflags} -DGL_GLEXT_PROTOTYPES"
%ifarch %{arm}
%cmake -DMINIMAL_FLAGS=1 -DNOVIDEOREC=1 -DBUILD_ENGINE_C=1 -DFONTS_DIRS="`find %{_datadir}/fonts -type d -printf '%p;'`"
%else
%cmake -DMINIMAL_FLAGS=1 -DNOVIDEOREC=1 -DBUILD_ENGINE_C=1 -DGHFLAGS=-dynamic -DFONTS_DIRS="`find %{_datadir}/fonts -type d -printf '%p;'`"
%endif

%cmake_build


%install
%cmake_install

# below is the desktop file and icon stuff.
desktop-file-validate %{buildroot}/%{_datadir}/applications/hedgewars.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/hwengine.desktop
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 misc/hedgewars_ico.png \
  %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/hedgewars.png
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/512x512/apps
install -p -m 644 misc/hedgewars.png \
  %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/%{name}.png

# Install systemd and firewalld files for hedgewars-server
mkdir -p %{buildroot}%{_unitdir} %{buildroot}%{_sysconfdir}/sysconfig \
         %{buildroot}%{_prefix}/lib/firewalld/services
install -pm 0644 %{SOURCE100} %{buildroot}%{_unitdir}/
install -pm 0644 %{SOURCE101} %{buildroot}%{_sysconfdir}/sysconfig/%{name}
install -pm 0644 %{SOURCE102} %{buildroot}%{_prefix}/lib/firewalld/services/

# wipe out fonts to unbreak flatpak build
find %{buildroot} -type f -name '*.ttc' | xargs rm -f

%ldconfig_scriptlets

%post server
%systemd_post %{name}.service
%{?firewalld_reload}

%preun server
%systemd_preun %{name}.service

%postun server
%systemd_postun_with_restart %{name}.service


%files
%doc README README.md
%license COPYING
%{_bindir}/%{name}
%{_bindir}/hwengine
%attr(644, -, -) %{_datadir}/appdata/*
%{_datadir}/applications/hedgewars.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/pixmaps/hedgewars.xpm
%{_datadir}/applications/hwengine.desktop
%{_libdir}/libphyslayer.so.1.0
%{_libdir}/libphyslayer.so

%files server
%{_bindir}/%{name}-server
%{_prefix}/lib/firewalld/services/%{name}.xml
%{_sysconfdir}/sysconfig/%{name}
%{_unitdir}/%{name}.service

%files data
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/Data
# Exclude the Fonts directory as there should not be any fonts included
# Note we want the build to fail if any fonts are included in the package
# %%exclude won't trigger a build failure if excluded files are installed.
# So the problem won't show up until runtime.
# Also of note is that unpackaged directories also don't seem to cause
# a build failure. However we don't care in this case.
%{_datadir}/%{name}/Data/Graphics
%{_datadir}/%{name}/Data/Maps
%{_datadir}/%{name}/Data/Missions
%{_datadir}/%{name}/Data/Names
%{_datadir}/%{name}/Data/Sounds
%{_datadir}/%{name}/Data/Forts
%{_datadir}/%{name}/Data/Locale
%{_datadir}/%{name}/Data/misc
%{_datadir}/%{name}/Data/Music
%{_datadir}/%{name}/Data/Scripts
%{_datadir}/%{name}/Data/Themes


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Aug 05 2023 Hans de Goede <hdegoede@redhat.com> - 1.0.2-5
- Fix FTBFS (rhbz#2225917)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 03 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.0.2-3
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 15 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.0.2-1
- 1.0.2

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 14 2022 Jan Grulich <jgrulich@redhat.com> - 1.0.0-26
- Rebuild (qt5)

* Tue May 17 2022 Jan Grulich <jgrulich@redhat.com> - 1.0.0-25
- Rebuild (qt5)

* Fri Apr 01 2022 Hans de Goede <hdegoede@redhat.com> - 1.0.0-24
- Fix F37 FTBFS caused by cmake argument mess (rhbz#2057738)

* Fri Apr 01 2022 Hans de Goede <hdegoede@redhat.com> - 1.0.0-23
- %%define toolchain clang, this fixes LTO and fixes the new .package.note
  support in F36 breaking the build on armv7hl, fixing FTBFS 2045702

* Tue Mar 08 2022 Jan Grulich <jgrulich@redhat.com> - 1.0.0-22
- Rebuild (qt5)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan 08 2022 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-20
- Rebuilt for https://fedoraproject.org/wiki/Changes/LIBFFI34

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 28 2021 Nikolay Nikolov <nickysn@gmail.com> - 1.0.0-18
- rebuilt

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.0-17
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 27 2020 Rex Dieter <rdieter@fedoraproject.org> - 1.0.0-15
- drop hardcoded Qt5 runtime dependency

* Mon Nov 23 07:52:31 CET 2020 Jan Grulich <jgrulich@redhat.com> - 1.0.0-14
- rebuild (qt5)

* Fri Sep 11 2020 Jan Grulich <jgrulich@redhat.com> - 1.0.0-13
- rebuild (qt5)

* Tue Aug 04 2020 Hans de Goede <hdegoede@redhat.com> - 1.0.0-12
- Fix FTBFS (rhbz#1863847)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-11
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Nikolay Nikolov <nickysn@gmail.com> - 1.0.0-9
- Applied patch to fix build with Haskell network version 3
- Support CMAKE out-of-source builds

* Mon Apr 13 2020 Bruno Wolff III <bruno@wolff.to> - 1.0.0-8
- Search for fonts from the top

* Mon Apr 13 2020 Bruno Wolff III <bruno@wolff.to> - 1.0.0-7
- Handle change in where dejavu fonts are located

* Mon Apr 13 2020 Bruno Wolff III <bruno@wolff.to> - 1.0.0-6
- Don't try to install DejaVuSans-Bold

* Mon Apr 06 2020 Rex Dieter <rdieter@fedoraproject.org> - 1.0.0-5
- rebuild (qt5)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 09 2019 Jan Grulich <jgrulich@redhat.com> - 1.0.0-3
- rebuild (qt5)

* Sun Oct 13 2019 Richard Shaw <hobbes1069@gmail.com> - 1.0.0-2
- Rebuilt for Qt 5.12.5.

* Fri Oct 11 2019 Richard Shaw <hobbes1069@gmail.com> - 1.0.0-1
- Update to 1.0.0.

* Wed Sep 25 2019 Jan Grulich <jgrulich@redhat.com> - 0.9.25-9
- rebuild (qt5)

* Thu Sep 12 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.9.25-8
- Tweak for flatpak.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.25-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 17 2019 Jan Grulich <jgrulich@redhat.com> - 0.9.25-6
- rebuild (qt5)

* Thu Jun 06 2019 Bruno Wolff III <bruno@wolff.to> - 0.9.25-5
- Rebuild for qt5 update

* Mon Mar 04 2019 Rex Dieter <rdieter@fedoraproject.org> - 0.9.25-4
- rebuild (qt5)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 27 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.9.25-2
- rebuild (Qt5)

* Wed Dec 12 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.9.25-1
- 0.9.25.
- Building with clang due to upstream change.

* Tue Dec 11 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.9.24.1-4
- rebuild (Qt5)

* Tue Sep 04 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.9.24.1-3
- use module Qt5 build dependencies, track private api usage (#1625239)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.24.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 23 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.9.24.1-1
- 0.9.24.1

* Wed Apr 18 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.9.24-1
- 0.9.24

* Tue Mar 06 2018 Richard Shaw <hobbes1069@gmail.com> - 0.9.23-5
- Move game data to noarch subpackage.

* Thu Feb 22 2018 Richard Shaw <hobbes1069@gmail.com> - 0.9.23-4
- Add systemd and firewalld configuration for hedgewars-server.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.23-2
- Remove obsolete scriptlets

* Fri Nov 24 2017 Richard Shaw <hobbes1069@gmail.com> - 0.9.23-1
- Update to latest upstream release.
- Remove upstreamed or unneeded patches.
- Add new build requirements: ghc-sandi-devel, ghc-regex-tdfa-devel,
  ghc-containers-devel.
- Remove ghc-dataenc-devel from build requirements
  (no longer used, conflicts with sandi)
- Change of build requirements: SDL->SDL2
- Add libphyslayer.so.1.0 to %%files

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.22-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.22-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar 10 2017 Jens Petersen <petersen@redhat.com> - 0.9.22-6
- skip cmake check for Haskell mask failing under ghc8

* Wed Mar 01 2017 Richard Shaw <hobbes1069@gmail.com> - 0.9.22-5
- Rebuild for updated ghc.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jul 17 2016 Richard Shaw <hobbes1069@gmail.com> - 0.9.22-3
- Rebuild for broken dependencies in Rawhide.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec  2 2015 Hans de Goede <hdegoede@redhat.com> - 0.9.22-1
- New upstream release 0.9.22 (rhbz#1276889)

* Fri Sep 18 2015 Richard Hughes <rhughes@redhat.com> - 0.9.21.1-7
- Fix AppData file so that the application gets included

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.21.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.21.1-5
- Rebuilt for GCC 5 C++11 ABI change

* Tue Apr 07 2015 Bruno Wolff III <bruno@wolff.to> - 0.9.21.1-4
- Fix rpath issue
- Fix appdata issues

* Mon Feb 16 2015 Bruno Wolff III <bruno@wolff.to> - 0.9.21.1-3
- Use ghc-bytestring-show

* Mon Feb 09 2015 Bruno Wolff III <bruno@wolff.to> - 0.9.21.1-2
- Rebuild for ghc update

* Fri Jan 09 2015 Bruno Wolff III <bruno@wolff.to> - 0.9.21.1-1
- New upstream release with some distro patches
- Reenable arm
- Use upstream desktop and appdata files

* Mon Jan 05 2015 Bruno Wolff III <bruno@wolff.to> - 0.9.21-3
- Fix problem accessing font files

* Sun Jan 04 2015 Bruno Wolff III <bruno@wolff.to> - 0.9.21-2
- Fix for lua problem

* Fri Jan 02 2015 Bruno Wolff III <bruno@wolff.to> - 0.9.21-1
- Latest upstream release

* Fri Dec 12 2014 Richard Hughes <richard@hughsie.com> - 0.9.18-14
- Fix the AppData file to actually validate.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.18-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.18-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Oct 13 2013 Hans de Goede <hdegoede@redhat.com> - 0.9.18-11
- Improve Summary (rhbz#971887)
- Add an appdata file

* Fri Aug 09 2013 Hans de Goede <hdegoede@redhat.com> - 0.9.18-10
- Don't pass -dynamic to ghc on arm, fixing FTBFS (rhbz#992471)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.18-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 23 2013 Bruno Wolff III <bruno@wolff.to> - 0.9.18-8
- Rebuild for ghc updates

* Wed May 15 2013 Tom Callaway <spot@fedoraproject.org> - 0.9.18-7
- rebuild for new lua

* Sat Mar 23 2013 Bruno Wolff III <bruno@wolff.to> - 0.9.18-6
- Rebuild for ghc-dataenc soname bump

* Sun Feb 24 2013 Bruno Wolff III <bruno@wolff.to> - 0.9.18-5
- Remove vendor prefix from desktop file

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec 21 2012 Bruno Wolff III <bruno@wolff.to> - 0.9.18-3
- Allow screenshots to use png images

* Sun Nov 18 2012 Hans de Goede <hdegoede@redhat.com> - 0.9.18-2
- Rebuild for ghc updates affecting the server

* Thu Nov  1 2012 Hans de Goede <hdegoede@redhat.com> - 0.9.18-1
- Update to latest upstream release: 0.9.18
- 0.9.18 release announcement: http://www.hedgewars.org/node/4090

* Sat Aug 11 2012 Bruno Wolff III <bruno@wolff.to> - 0.9.17-8
- Rebuild for libffi soname bump

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.17-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 24 2012 Bruno Wolff III <bruno@wolff.to> - 0.9.17-6
- Rebuild for some library updates

* Sat May 12 2012 Bruno Wolff III <bruno@wolff.to> - 0.9.17-5
- Add a 512x512 icon

* Sat Mar 24 2012 Jens Petersen <petersen@redhat.com> - 0.9.17-4
- rebuild against new ghc

* Fri Jan 06 2012 Bruno Wolff III <bruno@wolff.to> - 0.9.17-3
- Rebuild for new ghc-utf8-string

* Thu Jan 05 2012 Bruno Wolff III <bruno@wolff.to> - 0.9.17-2
- Rebuild for new ghc-dataenc

* Sun Jan 01 2012 Bruno Wolff III <bruno@wolff.to> - 0.9.17-1
- Update to upstream 0.9.17
- Changelog at http://code.google.com/p/hedgewars/source/browse/ChangeLog.txt
- 0.9.16 release announcement: http://www.hedgewars.org/node/3291
- 0.9.17 release announcement: http://www.hedgewars.org/node/3405
- Use modified Debian patch to work around Text.Show.ByteString not being available
- hedgewars-server now needs ghc-deepseq

* Fri Oct 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.9.15-10.2
- rebuild with new gmp without compat lib

* Tue Oct 11 2011 Peter Schiffer <pschiffe@redhat.com> - 0.9.15-10.1
- rebuild with new gmp

* Sun Aug 28 2011 Bruno Wolff III <bruno@wolff.to> - 0.9.15-10
- Rebuild for hslogger update

* Wed Aug 17 2011 Jens Petersen <petersen@redhat.com> - 0.9.15-9
- rebuild for bumped ghc-dataenc

* Fri Jun 17 2011 Bruno Wolff III <bruno@wolff.to> - 0.9.15-8
- Rebuild for various ghc library updates

* Thu Mar 10 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 0.9.15-7
- Enable build on sparcv9

* Tue Feb 15 2011 Jens Petersen <petersen@redhat.com> - 0.9.15-6
- rebuild for latest updates for haskell-platform-2011.1 and ghc-dataenc

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Feb 03 2011 Dan Horák <dan[at]danny.cz> 0.9.15-4
- add s390(x) to ExcludeArch - no fpc or ghc there

* Tue Feb 01 2011 Bruno Wolff III <bruno@wolff.to> 0.9.15-3
- Rebuild for ghc-hslogger 1.1.3

* Thu Jan 27 2011 Bruno Wolff III <bruno@wolff.to> 0.9.15-2
- Rebuild for qt soname bump

* Wed Jan 19 2011 Bruno Wolff III <bruno@wolff.to> 0.9.15-1
- Upstream release 0.9.15
- Announcement at http://www.hedgewars.org/node/2672
- Changelog at http://code.google.com/p/hedgewars/source/browse/ChangeLog.txt
- Fixes FTBFS due to depreciating Maybe for Data.Maybe

* Sun Jan 16 2011 Bruno Wolff III <bruno@wolff.to> 0.9.14.1-3
- Rebuild again for ghc7.

* Sun Dec 05 2010 Bruno Wolff III <bruno@wolff.to> 0.9.14.1-2
- Rebuild for ghc-HUnit soname bump.

* Sat Nov 27 2010 Bruno Wolff III <bruno@wolff.to> 0.9.14.1-1
- Rebuild for ghc7.
- Get upstream release 0.9.14.1 (0.9.14 was a preview release.)
- Release announcement at: http://www.hedgewars.org/node/2573

* Sun Nov 07 2010 Bruno Wolff III <bruno@wolff.to> 0.9.13-5
- Rebuild for soname bump in libHSffi-ghc6.

* Mon Oct 04 2010 Bruno Wolff III <bruno@wolff.to> 0.9.13-4
- Rebuild for soname bump in libHSdataenc.

* Mon Oct 04 2010 Bruno Wolff III <bruno@wolff.to> 0.9.13-3
- Fix up the requires syntax to do what I mean.

* Sun Oct 03 2010 Bruno Wolff III <bruno@wolff.to> 0.9.13-2
- The server needs to match the version of the game.

* Sun Oct 03 2010 Bruno Wolff III <bruno@wolff.to> 0.9.13-1
- Update to 0.9.13 - Change summary at: http://www.hedgewars.org/node/2037
- Server logging enable now that ghc-hslogger is available.

* Sun Jun 13 2010 Bruno Wolff III <bruno@wolff.to> 0.9.12-4
- In F14 ghc-utf8-string-devel needs to be build required.

* Sun May 23 2010 Bruno Wolff III <bruno@wolff.to> 0.9.12-3
- Fix FTBFS bug 595168 due to invalid -Nu option for fpc.
- Add a dedicated server sub package (with logging disabled)

* Tue Dec  1 2009 Hans de Goede <hdegoede@redhat.com> 0.9.12-2
- Use RPM_OPT_FLAGS when building c++ code and pass -g to fpc (#542000)

* Mon Nov 23 2009 Hans de Goede <hdegoede@redhat.com> 0.9.12-1
- New upstream release 0.9.12
- Remove included google-droid font, use the font from the
  google-droid-sans-fonts package instead

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 0.9.11-3
- rebuilt with new openssl

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon May 25 2009 Hans de Goede <hdegoede@redhat.com> 0.9.11-1
- New upstream release 0.9.11

* Wed Apr 15 2009 Hans de Goede <hdegoede@redhat.com> 0.9.10-1
- New upstream release 0.9.10

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 20 2009 Hans de Goede <hdegoede@redhat.com> 0.9.9-1
- New upstream release 0.9.9
- Fix dejavu font Requires (again) (rh 480458)

* Fri Jan 16 2009 Tomas Mraz <tmraz@redhat.com> 0.9.8-2
- rebuild with new openssl

* Sat Jan 10 2009 Hans de Goede <hdegoede@redhat.com> 0.9.8-1
- New upstream release 0.9.8

* Sat Dec 27 2008 Hans de Goede <hdegoede@redhat.com> 0.9.7-3
- Fix dejavu font Requires

* Fri Dec 26 2008 Hans de Goede <hdegoede@redhat.com> 0.9.7-2
- Replace private dejavu copy with symlink to system version (rh 477396)

* Tue Nov  4 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9.7-1
- New upstream release 0.9.7

* Wed Jul 30 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9.6-1
- New upstream release 0.9.6

* Wed Jul  9 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9.5-1
- New upstream release 0.9.5

* Thu Jun 26 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9.4-1
- New upstream release 0.9.4

* Thu May  1 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9.3-1
- New upstream release 0.9.3

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.2-2
- Autorebuild for GCC 4.3

* Tue Jan 22 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9.2-1
- New upstream release 0.9.2

* Sat Jan 12 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9.0-5
- Fix compilation with gcc 4.3

* Mon Sep 10 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9.0-4
- Remove ExcludeArch ppc64, freepascal is available on ppc64 now (bz 284401)

* Mon Sep 10 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9.0-3
- ExcludeArch ppc64, as freepascal (fpc) isn't available on ppc64 (bz 284401)

* Sun Sep  9 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9.0-2
- Install data files into /usr/share/hedgewars instead of into
  /usr/share/hedgewars/hedgewars
- Minor desktop file cleanup

* Sun Aug 26 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9.0-1
- Initial Fedora package
