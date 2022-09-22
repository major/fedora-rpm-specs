Name:           koules
Version:        1.4
Release:        37%{?dist}
Summary:        Action game with multiplayer, network and sound support

License:        GPLv2
URL:            http://www.ucw.cz/~hubicka/koules/
Source0:        http://www.ucw.cz/~hubicka/koules/packages/%{name}%{version}-src.tar.gz
Source1:        koules.desktop
Source2:        koules.sndsrv.linux

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  SDL2_gfx-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  xmkmf
BuildRequires:  desktop-file-utils

Requires:       %{name}-sound = %{version}
Requires:       %{name}-x11 = %{version}

Obsoletes:	koules-svgalib < 1.4-34

# https://github.com/lkundrak/koules/tree/SDL2
Patch1:         0001-gitignore.patch
Patch2:         0002-Fix-warnings.patch
Patch3:         0003-Remove-relics.patch
Patch4:         0004-Fix-a-buffer-overflow.patch
Patch5:         0005-Spelling-fixes-from-Debian.patch
Patch6:         0006-From-Debian-050_defines.diff.patch
Patch7:         0007-We-do-not-install-manual-pages.patch
Patch8:         0008-Fix-build.patch
Patch9:         0009-Install-to-relative-location-and-look-for-the-sound-.patch
Patch10:        0010-From-Debian-106_shm_check.diff.patch
Patch11:        0011-From-Debian-107_fix_xsynchronize.diff.patch
Patch12:        0012-From-Debian-108_use_right_visual.diff.patch
Patch13:        0013-From-Debian-109_fpe_fix.diff.patch
Patch14:        0014-Set-TABSIZE-globally.patch
Patch15:        0015-io.h-no-longer-needed.patch
Patch16:        0016-DEFAULTINITPORT-is-not-defined-if-building-without-N.patch
Patch17:        0017-Fix-undefined-reference-if-building-with-net-and-wit.patch
Patch18:        0018-Fix-pointer-target-signedness.patch
Patch19:        0019-Fix-banner-placement-with-OS-2.patch
Patch20:        0020-Fix-rocketcolor-signedness.patch
Patch21:        0021-Fix-background-color-calculation.patch
Patch22:        0022-Fix-string-quoting.patch
Patch23:        0023-Fix-socket-types.patch
Patch24:        0024-Silence-warning-about-potentially-uninitialized-stru.patch
Patch25:        0025-Fix-warning-about-ambigious-if-else-s.patch
Patch26:        0026-Avoid-warnings-about-unused-labels.patch
Patch27:        0027-Get-rid-of-unused-variables-if-building-with-both-MO.patch
Patch28:        0028-Dynamically-decide-about-window-size-based-on-inform.patch
Patch29:        0029-Fix-rocketcolor-signedness.patch
Patch30:        0030-Add-SDL-support.patch
Patch31:        0031-Add-koules.sdl.6-manual.patch
Patch32:        0032-Fix-an-off-by-one-error.patch
Patch33:        0033-Drop-an-unused-variable.patch
Patch34:        0034-Make-compiler-bounds-checking-happy.patch
Patch35:        0035-Don-t-do-extern-inline.patch
Patch36:        0036-Remove-redundant-normalize-function.patch
Patch37:        0037-Allow-setting-DESTDIR-for-sdl-and-svga-installs.patch
Patch38:        0038-SDL2-build.patch
Patch39:        0039-SDL2-GFX.patch
Patch40:        0040-SDL2-input.patch
Patch41:        0041-Correct-path-to-the-sound-server.patch
Patch42:        koules-1.4-gcc-10.patch

%description
Koules is a fast action arcade-style game.  It works in fine resolution
with cool 256 color graphics, multiplayer mode up to 5 players, full sound
and, of course, network support.  Koules is an original idea. First version
of Koules was developed from scratch by Jan Hubicka in July 1995.


%package x11
Summary:        X Window system variant of a multiplayer action game
Requires:       xorg-x11-fonts-misc

%description x11
This package contains variant of a classic Linux arcade game with X Window
System support and can act as a network server for multiplayer game.


%package sdl
Summary:        SDL2 variant of a multiplayer action game

%description sdl
This package contains variant of a classic Linux arcade game built with SDL
library that can also act as a network server for multiplayer game.


%package sound
Summary:        Sound files for a classic Linux multiplayer action game

%description sound
This package contains sound files for a classic Linux arcade game. To make
sound functioning in Koules you either need to ensure exclusive access to
sound hardware for the game, or use a /dev/dsp wrapper such as padsp from
pulseaudio-utils package.


%global bindir          BINDIR=%{_bindir}
%global sounddir        SOUNDDIR=%{_datadir}/%{name}/sound
%global mandir          MANDIR=%{_mandir}/man6
%global libexecdir      LIBEXECDIR=%{_libexecdir}/%{name}
%global makedirs        %{bindir} %{sounddir} %{mandir} %{libexecdir}


%prep
%setup -q -c
pushd %{name}%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
popd


%build
# Build SDL variant
cp -a  %{name}%{version} %{name}-%{version}-sdl
make -C %{name}-%{version}-sdl -f Makefile.sdl %{makedirs} \
        %{_smp_mflags} OPTIMIZE="%{optflags}" OPTIMIZE1="%{optflags}"

# Build X11 variant
cp -a  %{name}%{version} %{name}-%{version}-x11
cd %{name}-%{version}-x11
echo '#define HAVEUSLEEP' >>Iconfig
xmkmf -a
make %{makedirs} %{_smp_mflags} CCOPTIONS="%{optflags} -DONLYANSI"


%install
install -d %{buildroot}%{_mandir}/man6
install -d %{buildroot}%{_datadir}/%{name}/sound
install -d %{buildroot}%{_libexecdir}/%{name}

# Install SDL variant
make -C %{name}-%{version}-sdl -f Makefile.sdl install INSTALLSOUND=False \
        %{makedirs} DESTDIR=%{buildroot}

# Install X11 variant and sound
make -C %{name}-%{version}-x11 install %{makedirs} DESTDIR=%{buildroot}
install -d %{buildroot}%{_datadir}/pixmaps
install %{name}%{version}/Icon.xpm %{buildroot}%{_datadir}/pixmaps/%{name}.xpm
desktop-file-install \
        --dir ${RPM_BUILD_ROOT}%{_datadir}/applications \
        %{SOURCE1}

# PulseAudio wrapper for the sound server
mv %{buildroot}%{_libexecdir}/%{name}/koules.sndsrv.linux{,.bin}
cp %{SOURCE2} %{buildroot}%{_libexecdir}/%{name}/koules.sndsrv.linux


%files
%doc %{name}%{version}/ANNOUNCE
%doc %{name}%{version}/BUGS
%doc %{name}%{version}/COPYING
%doc %{name}%{version}/Card
%doc %{name}%{version}/ChangeLog
%doc %{name}%{version}/Koules.FAQ
%doc %{name}%{version}/README
%doc %{name}%{version}/TODO


%files sound
%{_datadir}/%{name}
%{_libexecdir}/%{name}


%files x11
%{_bindir}/xkoules
%attr(644,root,root) %{_mandir}/man6/xkoules.6*
%attr(644,root,root) %{_datadir}/pixmaps/%{name}.xpm
%if (0%{?fedora} && 0%{?fedora} < 19) || ( 0%{?rhel} && 0%{?rhel} < 7)
%{_datadir}/applications/fedora-koules.desktop
%else
%{_datadir}/applications/koules.desktop
%endif


%files sdl
%attr(755,root,root) %{_bindir}/koules.sdl
%attr(644,root,root) %{_mandir}/man6/koules.sdl.6*


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 20 2021 Charles R. Anderson <cra@alum.wpi.edu> - 1.4-34
- Remove svgalib subpackage (rhbz#1814815, rhbz#1923424)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 24 2020 Than Ngo <than@redhat.com> - 1.4-31
- Fixed FTBFS

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 1.4-26
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov  9 2015 Lubomir Rintel <lkundrak@v3.sk> - 1.4-20
- Fix build
- Add SDL2 support

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct 24 2013 Lubomir Rintel <lkundrak@v3.sk> - 1.4-16
- Bulk sad and useless attempt at consistent SPEC file formatting

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar  6 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 1.4-14
- Remove vendor prefix from desktop files in F19+ https://fedorahosted.org/fesco/ticket/1077

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 9 2010 Lubomir Rintel <lkundrak@v3.sk> 1.4-9
- Do not build svgalib flavour on RHEL-6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Apr 13 2009 Lubomir Rintel <lkundrak@v3.sk> 1.4-7
- Debian apparently fixed shm more sanely than me
- Import bunch of Debian fixes

* Sun Apr 12 2009 Lubomir Rintel <lkundrak@v3.sk> 1.4-6
- Wrap the OSS-based sound server in padsp

* Mon Mar 16 2009 Lubomir Rintel <lkundrak@v3.sk> 1.4-5
- Require fonts
- Fix Xshm support

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 1 2008 Lubomir Rintel <lkundrak@v3.sk> 1.4-3
- Own /usr/libexec/koules (#473931)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.4-2
- Autorebuild for GCC 4.3

* Sun Oct 28 2007 Lubomir Kundrak <lkundrak@redhat.com> 1.4-1
- From Red Hat Linux 4.2 back into life
