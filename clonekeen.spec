Name:           clonekeen
Version:        0.8.4
Release:        27%{?dist}
Summary:        "Commander Keen: Invasion of the Vorticons" clone
License:        GPLv3+
URL:            http://clonekeen.sourceforge.net/
# We make a clean tarball by removing bin/data/sound*
# from http://clonekeen.sourceforge.net/files/%%{name}-src-84.tar.gz
Source0:        %{name}-src-84-clean.tar.gz
# This are the .dat files and the extra (GPL) levels from 
# http://downloads.sourceforge.net/%%{name}/CKBeta83_Bin_W32.zip
# The pristine upstream .zip's aren't used because the included sounds.ck?
# files are property of id Software
Source1:        %{name}-0.8.4-data.tar.gz
Source2:        extract.c
Source3:        clonekeen-extract-sounds.c
Source4:        %{name}.sh
Source5:        %{name}.autodlrc
Source6:        %{name}.desktop
Source7:        %{name}.png
Patch0:         %{name}-0.8.4-noSDLmain.patch
Patch1:         %{name}-0.8.4-fcommon-fix.patch
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  SDL_mixer-devel dynamite-devel desktop-file-utils
BuildRequires: make
Requires:       hicolor-icon-theme autodownloader

%description
CloneKeen is an almost complete clone of the old classic DOS game,
"Commander Keen: Invasion of the Vorticons" by by id Software:
http://www.idsoftware.com/
CloneKeen requires the original id Software gamedata files to work.

If you posess the original DOS games. You can play all three episodes of the
game. If you don't, you can can still play the shareware episode one. Which can
be freely downloaded from Apogee, but cannot be distributed as a part of
Fedora. When you start CloneKeen for the first time it will offer to download
the shareware datafiles for you.


%prep
%autosetup -p1 -a 1 -n keen
find -name "*.o" -delete
sed -i 's|gcc -O2|gcc %{optflags} -std=gnu89|g' src/Makefile
cp -a %{SOURCE2} %{SOURCE3} .
sed -i 's/\r//g' README src/changelog.txt


%build
CFLAGS="$CFLAGS -std=gnu89"
make %{?_smp_mflags} -C src -f Makefile
gcc -o %{name}-extract $CFLAGS extract.c -ldynamite
gcc -o %{name}-extract-sounds $CFLAGS %{name}-extract-sounds.c


%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/data
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/gfx

install -m 755 src/keen $RPM_BUILD_ROOT%{_libexecdir}/%{name}
install -m 755 %{name}-extract $RPM_BUILD_ROOT%{_libexecdir}
install -m 755 %{name}-extract-sounds $RPM_BUILD_ROOT%{_libexecdir}
install -p -m 755 %{SOURCE4} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -p -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 644 bin/*.dat  $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 644 bin/*.ini  $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 644 bin/gfx/*  $RPM_BUILD_ROOT%{_datadir}/%{name}/gfx
install -p -m 644 bin/data/* $RPM_BUILD_ROOT%{_datadir}/%{name}/data
install -p -m 644 bin/*.ck1  $RPM_BUILD_ROOT%{_datadir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE6}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/24x24/apps
install -p -m 644 %{SOURCE7} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/24x24/apps

%files
%doc README src/changelog.txt
%{_bindir}/%{name}
%{_libexecdir}/%{name}*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/24x24/apps/%{name}.png

%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Feb 02 2023 Timm Bäder <tbaeder@redhat.com> - 0.8.4-26
- Build in C89 mode
- rhbz#2161553
- https://fedoraproject.org/wiki/Toolchain/PortingToModernC

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Feb 28 2020 Hans de Goede <hdegoede@redhat.com> - 0.8.4-19
- Fix FTBFS (rhbz#1799233)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.4-13
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.8.4-7
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 0.8.4-3
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- clean up spec to follow current guidelines

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Sep  7 2012 Tom Callaway <spot@fedoraproject.org> - 0.8.4-1
- update to 0.8.4

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Sep  7 2008 Hans de Goede <hdegoede@redhat.com> 0.8.3-5
- Fix patch build failure

* Thu Apr  3 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.8.3-4
- Fix missing prototype compiler warnings

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.8.3-3
- Autorebuild for GCC 4.3

* Tue Nov  6 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.8.3-2
- Give proper attribution to id Software

* Thu Oct 25 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.8.3-1
- Initial Fedora package
