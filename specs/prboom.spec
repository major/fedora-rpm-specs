%define waddir  %{_datadir}/doom

Name:           prboom
Version:        2.5.0
Release:        36%{?dist}
Summary:        Open source port of the DOOM game engine

License:        GPL-2.0-or-later
URL:            http://prboom.sourceforge.net/
Source0:        http://downloads.sourceforge.net/prboom/prboom-2.5.0.tar.gz

Patch0:         pointer-types.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  SDL_mixer-devel SDL_net-devel
BuildRequires:  libGLU-devel
BuildRequires:  autoconf >= 2.69-10

Requires:       freedoom

%description
prboom is an open-source port of Doom, the classic 3D first-person shooter
game.  It totally outclassed any 3D world games that preceded it, with amazing
speed, flexibility, and outstanding gameplay. The specs to the game were
released, and thousands of extra levels were written by fans of the game; even
today new levels are written for Doom faster then any one person could play
them.

%prep
%setup -q

%patch -P 0 -p0

%build
autoreconf -vif
sed -i /HAVE_LIBPNG/d configure
export CPPFLAGS="$CPPFLAGS -fcommon -std=gnu17"
%configure --enable-gl --disable-cpu-opt --program-prefix='' --with-waddir=%{waddir} --disable-i386-asm

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

# Move the binaries out of the crufty /usr/games directory
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mv $RPM_BUILD_ROOT/usr/games/* $RPM_BUILD_ROOT/%{_bindir}

# Remove the doc files that will get picked up in the files
# section below.
rm -rf $RPM_BUILD_ROOT/%{_docdir}

%files
%license COPYING
%{_bindir}/prboom
%{_bindir}/prboom-game-server
%dir %{waddir}
%{waddir}/prboom.wad
%{_mandir}/man5/*
%{_mandir}/man6/*
%doc NEWS AUTHORS README
%doc doc/README.compat doc/README.demos doc/MBF.txt doc/MBFFAQ.txt doc/boom.txt

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 06 2024 Gwyn Ciesla <gwync@protonmail.com> - 2.5.0-34
- Patch for stricter flags

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Mar 04 2023 Gwyn Ciesla <gwync@protonmail.com> - 2.5.0-30
- migrated to SPDX license

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.5.0-23
- Fix FTBFS.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 28 2013 Jaromir Capik <jcapik@redhat.com> - 2.5.0-9
- aarch64 support (#926369)
- Adding BuildConflicts with libpng-devel

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Apr 18 2010 Wart <wart at kobold.org> 2.5.0-4
- configure with --disable-i386-asm to prevent crash on startup (BZ #517600)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Dec 20 2008 Wart <wart at kobold.org> 2.5.0-1
- Update to 2.5.0

* Fri Feb 8 2008 Wart <wart at kobold.org> 2.4.7-3
- Rebuild for gcc 4.3

* Mon Aug 20 2007 Wart <wart at kobold.org> 2.4.7-2
- License tag clarification
- Better download URL

* Tue Nov 19 2006 Wart <wart at kobold.org> 2.4.7-1
- Update to 2.4.7

* Tue Oct 17 2006 Wart <wart at kobold.org> 2.4.6-1
- Update to 2.4.6

* Fri Sep 1 2006 Wart <wart at kobold.org> 2.4.5-2
- Rebuild for Fedora Extras 6

* Sat Aug 12 2006 Wart <wart at kobold.org> 2.4.5-1
- Update to 2.4.5
- Remove gamedir patch as it was accepted upstream.

* Sun Jul 23 2006 Wart <wart at kobold.org> 2.4.4-1
- Update to 2.4.4

* Sun Jul 23 2006 Wart <wart at kobold.org> 2.4.3-2
- Forgot to update the sources file before building.

* Sun Jul 23 2006 Wart <wart at kobold.org> 2.4.3-1
- Update to 2.4.3

* Sun Jul 16 2006 Wart <wart at kobold.org> 2.4.2-1
- Update to 2.4.2

* Sat Apr 22 2006 Wart <wart at kobold.org> 2.4.1-2
- Build both opengl and non-opengl binaries.

* Tue Apr 18 2006 Wart <wart at kobold.org> 2.4.1-1
- Update to 2.4.1

* Sun Mar 19 2006 Wart <wart at kobold.org> 2.3.1-6
- Updated -gamedir patch to add freedoom to the in-game wad menu.

* Sat Mar 18 2006 Wart <wart at kobold.org> 2.3.1-5
- Updated patches to fix segfault on i386 (BZ #185741)

* Tue Mar 14 2006 Wart <wart at kobold.org> 2.3.1-4
- Added patch to fix up some x86_64 issues

* Mon Mar 13 2006 Wart <wart at kobold.org> 2.3.1-3
- Once again, change the default wad dir to datadir/doom (see discussion on
  bz #185211)

* Sun Mar 12 2006 Wart <wart at kobold.org> 2.3.1-2
- Replace datadir/games/doom with datadir/prboom in the files section.

* Sat Mar 11 2006 Wart <wart at kobold.org> 2.3.1-1
- Initial package for Fedora Extras
