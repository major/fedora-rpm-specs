Name:           ularn
Version:        1.5p4
Release:        48%{?dist}
Summary:        Simple roguelike game

License:        GPL-1.0-or-later
URL:            http://www.ularn.org
Source0:        http://downloads.sourceforge.net/ularn/Ularn-1.5ishPL4.tar.gz
Source1:        config.sh.in
Source2:        ularn.desktop
Source3:        ularn.png
Patch0:         ularn-build.patch
Patch1:         ularn-euid.patch
Patch2:         ularn-datadir.patch
Patch3:         ularn-drop-setgid.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  ncurses-devel
BuildRequires:  desktop-file-utils
Requires:       ncompress

%description
A text-based roguelike game based on the original Larn.  Travel through
dungeons collecting weapons, killing monsters, in order to find and sell the
Eye of Larn to save your sick daughter.

%prep
%setup -q -n Ularn

# The configure script for this package is interactive.  However, it
# produces a config.sh script that can be customized if necessary.
# a pre-built config.sh script is used to avoid running an interactive
# configure script, but still must be customized slightly.
sed -e 's#@bindir@#%{_bindir}#' \
        -e 's#@datadir@#%{_datadir}#' \
        -e 's#@var@#%{_var}#' < %{SOURCE1} > config.sh
chmod +x config.h.SH
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

%build
# This package requires C89 compatibility mode (bug 2155503).
%global build_type_safety_c 0

# Keep track of where we are.  Some of the configuration scripts change
# the current working directory.
builddir=`pwd`
. ./config.h.SH
${builddir}/Makefile.u.SH
cd ${builddir}
mv Makefile.u Makefile
CC="gcc $RPM_OPT_FLAGS -fcommon -std=gnu17" make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_var}/games
touch $RPM_BUILD_ROOT/%{_var}/games/Ularn-scoreboard

desktop-file-install \
        --dir ${RPM_BUILD_ROOT}%{_datadir}/applications         \
        %{SOURCE2}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/32x32/apps/
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/32x32/apps/

# Note that the game is setgid games, and the score file is group writable.
%files
%attr(2755,root,games) %{_bindir}/Ularn
%{_datadir}/%{name}
%config(noreplace) %attr (0664,root,games) %{_var}/games/Ularn-scoreboard
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%doc README README.spoilers CHANGES.text Ularnopts
%license GPL

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5p4-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5p4-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5p4-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Aug 31 2023 Florian Weimer <fweimer@redhat.com> - 1.5p4-45
- Set build_type_safety_c to 0 (#2155503)

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5p4-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Mar 05 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.5p4-43
- migrated to SPDX license

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5p4-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 21 2022 Florian Weimer <fweimer@redhat.com> - 1.5p4-41
- Build in C89 mode (#2155503)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5p4-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5p4-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5p4-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5p4-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5p4-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 10 2020 Gwyn Ciesla <gwync@protonmail.com> 1.5p4-35
- Fix FTBFS.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5p4-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5p4-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar  7 2019 Tim Landscheidt <tim@tim-landscheidt.de> - 1.5p4-32
- Remove obsolete requirements for %%post/%%postun scriptlets

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5p4-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5p4-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5p4-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.5p4-28
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5p4-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5p4-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5p4-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5p4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5p4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5p4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5p4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5p4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 11 2013 Jon Ciesla <limburgher@gmail.com> - 1.5p4-19
- Drop desktop vendor tag.

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5p4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5p4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5p4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5p4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Mar 01 2009 Caolán McNamara <caolanm@redhat.com> - 1.5p4-14
- . config.h.SH -> . ./config.h.SH for new bash

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5p4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 18 2008 Wart <wart at kobold.org> 1.5p4-12
- Add coreutils requirement for rpm post scripts (BZ #475915)

* Fri Feb 8 2008 Wart <wart at kobold.org> 1.5p4-11
- Rebuild for gcc 4.3

* Tue Aug 21 2007 Wart <wart at kobold.org> 1.5p4-10
- License tag clarification

* Sat Aug 11 2007 Wart <wart at kobold.org> 1.5p4-9
- Use correct .desktop file version

* Sat Mar 3 2007 Wart <wart at kobold.org> 1.5p4-8
- Update .desktop file categories
- Use new upstream file location at Sourceforge

* Mon Aug 28 2006 Wart <wart at kobold.org> 1.5p4-7
- Fixed BR: ncurses -> ncurses-devel

* Mon Aug 28 2006 Wart <wart at kobold.org> 1.5p4-6
- Rebuild for Fedora Extras

* Sat Apr 15 2006 Wart <wart at kobold.org> 1.5p4-5
- Update setgid patch to prevent closing the scoreboard file after writing
  it.  This file might get written multiple times during the game.

* Fri Mar 17 2006 Wart <wart at kobold.org> 1.5p4-4
- Updated setgid patch to prevent someone from regaining setgid
  privileges.
- Own /usr/share/ularn directory

* Thu Mar 16 2006 Wart <wart at kobold.org> 1.5p4-3
- Added a patch to use the effective uid in determining the players name,
  or more precisely, don't use the id of the controlling terminal's user.
- Added a patch to look for game files in /usr/share/ularn and move the
  scoreboard to /var/games.
- Added a patch to drop setgid privileges after opening the scoreboard file
  for writing.

* Mon Mar 13 2006 Wart <wart at kobold.org> 1.5p4-2
- Added icon for .desktop file.
- Change default permissions so that only critical files are owned by 'games'
- Add missing scoreboard file.

* Sat Feb 25 2006 Wart <wart at kobold.org> 1.5p4-1
- Initial spec file.
