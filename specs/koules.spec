Name:           koules
Version:        1.4
Release:        47%{?dist}
Summary:        Action game with multiplayer, network and sound support

License:        GPL-2.0-or-later AND BSD-4-Clause-UC AND HPND-Netrek
URL:            http://www.ucw.cz/~hubicka/koules/
Source0:        http://www.ucw.cz/~hubicka/koules/packages/%{name}%{version}-src.tar.gz
Source1:        koules.desktop
Source2:        koules.sndsrv.linux

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  SDL2_gfx-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  imake
BuildRequires:  desktop-file-utils

Requires:       %{name}-sound%{?_isa} = %{version}-%{release}
Requires:       %{name}-x11%{?_isa}   = %{version}-%{release}

Obsoletes:      koules-svgalib < 1.4-34

# https://github.com/lkundrak/koules/tree/SDL2
Patch1:         0001-gitignore.patch
Patch2:         0002-Fix-warnings.patch
Patch3:         0003-Remove-relics.patch
Patch4:         0004-Fix-a-buffer-overflow.patch
Patch5:         0005-From-Debian-100_spelling.diff.patch
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
Patch43:        0043-Fix-accel-type-mismatch.patch
Patch44:        0044-Fix-lastlevel-joystick-format-overflows.patch
Patch45:        0045-Fix-unused-results.patch
Patch46:        0046-Makefiles-use-cc-variable.patch
Patch48:        0048-From-Debian-110_manpage_hyphens.diff.patch
Patch49:        0049-From-Debian-111_font_unsigned_char.diff.patch
Patch50:        0050-From-Debian-112_unsigned_control.diff.patch
Patch51:        0051-From-Debian-113_spelling_fixes.diff.patch
Patch52:        0052-From-Debian-double-declaration.patch

%description
Koules is a fast action arcade-style game.  It works in fine resolution
with cool 256 color graphics, multiplayer mode up to 5 players, full sound
and, of course, network support.  Koules is an original idea. First version
of Koules was developed from scratch by Jan Hubicka in July 1995.


%package x11
Summary:        X Window system variant of a multiplayer action game
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       xorg-x11-fonts-misc

%description x11
This package contains variant of a classic Linux arcade game with X Window
System support and can act as a network server for multiplayer game.


%package sdl
Summary:        SDL2 variant of a multiplayer action game
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description sdl
This package contains variant of a classic Linux arcade game built with SDL
library that can also act as a network server for multiplayer game.


%package sound
Summary:        Sound files for a classic Linux multiplayer action game
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pulseaudio-utils

%description sound
This package contains sound files for a classic Linux arcade game.


%global bindir          BINDIR=%{_bindir}
%global sounddir        SOUNDDIR=%{_datadir}/%{name}/sound
%global mandir          MANDIR=%{_mandir}/man6
%global libexecdir      LIBEXECDIR=%{_libexecdir}/%{name}
%global makedirs        %{bindir} %{sounddir} %{mandir} %{libexecdir}


%prep
%autosetup -c -N
pushd %{name}%{version}
%autopatch -p1
popd


%build
# Build SDL variant
cp -a  %{name}%{version} %{name}-%{version}-sdl
%make_build -C %{name}-%{version}-sdl -f Makefile.sdl %{makedirs} \
        OPTIMIZE="%{optflags}" OPTIMIZE1="%{optflags}"

# Build X11 variant
cp -a  %{name}%{version} %{name}-%{version}-x11
pushd %{name}-%{version}-x11
echo '#define HAVEUSLEEP' >>Iconfig
xmkmf -a
%make_build %{makedirs} CCOPTIONS="%{optflags} -DONLYANSI"
popd

%install
install -d %{buildroot}%{_mandir}/man6
install -d %{buildroot}%{_datadir}/%{name}/sound
install -d %{buildroot}%{_libexecdir}/%{name}

# Install SDL variant
%make_install -C %{name}-%{version}-sdl -f Makefile.sdl INSTALLSOUND=False \
        %{makedirs}

# Install X11 variant and sound
%make_install -C %{name}-%{version}-x11 %{makedirs}
install -d %{buildroot}%{_datadir}/pixmaps
install %{name}%{version}/Icon.xpm %{buildroot}%{_datadir}/pixmaps/%{name}.xpm
desktop-file-install \
        --dir ${RPM_BUILD_ROOT}%{_datadir}/applications \
        %{SOURCE1}

# PulseAudio wrapper for the sound server
mv %{buildroot}%{_libexecdir}/%{name}/koules.sndsrv.linux{,.bin}
cp %{SOURCE2} %{buildroot}%{_libexecdir}/%{name}/koules.sndsrv.linux


%files
%license %{name}%{version}/COPYING
%doc %{name}%{version}/ANNOUNCE
%doc %{name}%{version}/BUGS
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
%{_datadir}/applications/koules.desktop


%files sdl
%attr(755,root,root) %{_bindir}/koules.sdl
%attr(644,root,root) %{_mandir}/man6/koules.sdl.6*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Aug 01 2024 Charles R. Anderson <cra@alum.wpi.edu> - 1.4-46
- Fix License tag NTP --> HPND-Netrek

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Apr 21 2024 Charles R. Anderson <cra@alum.wpi.edu> - 1.4-44
- BuildRequires: imake rather than xmkmf
- Simplify description for sound subpackage

* Sun Apr 21 2024 Charles R. Anderson <cra@alum.wpi.edu> - 1.4-43
- Pull more patches from Debian

* Sun Apr 21 2024 Charles R. Anderson <cra@alum.wpi.edu> - 1.4-42
- Convert License tag to SPDX format and add missing licenses
- Tag COPYING as license file
- Use autosetup, autopatch, make_build, make_install macros
- Requires: pulseaudio-utils for padsp
- Subpackages Requires: main package
- Fix type mismatch, format overflow, and unused results warnings

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

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
