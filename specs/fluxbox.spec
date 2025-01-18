Name:           fluxbox
Version:        1.3.7
Release:        27%{?dist}

Summary:        Window Manager based on Blackbox

License:        MIT
URL:            http://fluxbox.org

Source0:        http://sourceforge.net/projects/%{name}/files/%{name}/%{version}/%{name}-%{version}.tar.bz2
Source3:        fluxbox-xsessions.desktop
Source5:        fluxbox-applications.desktop

Patch0:         fluxbox-startfluxbox-pulseaudio.patch
Patch1:         %{name}-gcc11.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  imlib2-devel
BuildRequires:  zlib-devel
BuildRequires:  libICE-devel
BuildRequires:  libSM-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXft-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXpm-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXrender-devel
BuildRequires:  fontconfig-devel
BuildRequires:  fribidi-devel
BuildRequires:  libtool
BuildRequires:  desktop-file-utils
BuildRequires: make
Requires:       artwiz-aleczapka-fonts
%if ( 0%{?fedora} >= 31) || (0%{?rhel} >= 8)
Requires:       python3-pyxdg
%else
Requires:       pyxdg
%endif

# provide clean upgrade path from old fluxconf tool (#662836)
Provides: fluxconf = 0.9.9-9
Obsoletes: fluxconf < 0.9.9-9

%description
Fluxbox is yet another window-manager for X.  It's based on the Blackbox 0.61.1
code. Fluxbox looks like blackbox and handles styles, colors, window placement
and similar thing exactly like blackbox (100% theme/style compatibility).  So
what's the difference between fluxbox and blackbox then?  The answer is: LOTS!

Have a look at the homepage for more info ;)

%package pulseaudio
Summary:        Enable pulseaudio support
Requires:       %{name} = %{version}-%{release}
Requires:       alsa-plugins-pulseaudio
Requires:       pulseaudio pulseaudio-module-x11 pulseaudio-utils
%if 0%{?fedora} > 9 || 0%{?rhel} > 5
BuildArch:      noarch
%endif

%description pulseaudio
Enable pulseaudio support.

%package vim-syntax
Summary:        Fluxbox syntax scripts for vim
Requires:       %{name} = %{version}-%{release}
Requires:       vim-filesystem
%if 0%{?fedora} > 9 || 0%{?rhel} > 5
BuildArch:      noarch
%endif

%description vim-syntax
Enable vim syntax highlighting support for fluxbox configuration files (menu,
keys, apps).

%prep
%autosetup -p0

%build
%configure \
  --enable-xft \
  --enable-xinerama \
  --enable-imlib2 \
  --enable-nls \
  --x-includes=%{_includedir} \
  --x-libraries=%{_libdir} \

%make_build LIBTOOL=/usr/bin/libtool

%install
%make_install

# this is for desktop integration
mkdir -p %{buildroot}%{_datadir}/xsessions/
mkdir -p %{buildroot}%{_datadir}/applications/
install -m 0644 -p %{SOURCE3} %{buildroot}%{_datadir}/xsessions/fluxbox.desktop
install -m 0644 -p %{SOURCE5} %{buildroot}%{_datadir}/applications/fluxbox.desktop

desktop-file-validate %{buildroot}%{_datadir}/xsessions/fluxbox.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/fluxbox.desktop

# fix 388971
mkdir -p %{buildroot}%{_sysconfdir}
touch -r ChangeLog %{buildroot}%{_sysconfdir}/fluxbox-pulseaudio

# vim syntax files
mkdir -p %{buildroot}%{_datadir}/vim/vimfiles/syntax/
install -m 0644 -p 3rd/vim/vim/syntax/fluxapps.vim %{buildroot}%{_datadir}/vim/vimfiles/syntax/fluxapps.vim
install -m 0644 -p 3rd/vim/vim/syntax/fluxkeys.vim %{buildroot}%{_datadir}/vim/vimfiles/syntax/fluxkeys.vim
install -m 0644 -p 3rd/vim/vim/syntax/fluxmenu.vim %{buildroot}%{_datadir}/vim/vimfiles/syntax/fluxmenu.vim

%files
%doc AUTHORS ChangeLog INSTALL NEWS README TODO
%license COPYING
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_datadir}/%{name}
%{_datadir}/xsessions/fluxbox.desktop
%{_datadir}/applications/fluxbox.desktop

%files pulseaudio
%{_sysconfdir}/fluxbox-pulseaudio

%files vim-syntax
%{_datadir}/vim/vimfiles/syntax/flux*.vim

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Leigh Scott <leigh123linux@gmail.com> - 1.3.7-22
- Rebuild fo new imlib2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 04 2020 Jeff Law <law@redhat.com> - 1.3.7-16
- Fix ordered comparison between pointer and integer 0 for gcc-11

* Mon Nov 23 2020 Ding-Yi Chen <dchen@redhat.com> - 1.3.7-15
- Remove S macro, as it does not seem to work with Fedora 33

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-14
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Ding-Yi Chen <dchen@redhat.com> - 1.3.7-11
- Removed fluxbox-xdg-menu-svn13.py as the upstream is dead.
- Upstream URL updated.

* Tue Oct 08 2019 Ding-Yi Chen <dchen@redhat.com> - 1.3.7-10
- Fix RHBZ 1738904 fluxbox depends on Python 2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 2019 Filipe Rosset <rosset.filipe@gmail.com> - 1.3.7-8
- Rebuilt to fix FTBFS + spec cleanup and modernization fixes rhbz#1674889

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 1.3.7-6
- Rebuild with fixed binutils

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 27 2017 Ding-Yi Chen <dchen@redhat.com> - 1.3.7-1
- Fixes Segfault in many places
- Improved TypeAhead system is not limited to matches on beginning
- Correct handling of 'maximized' statement in the apps file

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.3.6-2
- Rebuilt for GCC 5 C++11 ABI change

* Tue Jan 06 2015 Andreas Bierfert <andreas.bierfert@lowlatency.de>
- 1.3.6-1
- version upgrade (rhbz#1179194)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 18 2013 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 1.3.5-1
- version upgrade

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 31 2012 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 1.3.3-1
- version upgrade

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-4
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 07 2011 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 1.3.2-1
- split desktop files and remove nodisplay from xsessions

* Mon Oct 31 2011 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 1.3.2-1
- version upgrade (rhbz#750045)
- fixes crash on exit (rhbz#711166)
- remove obsoleted gcc46 patch
- ship desktop file in applications as well (rhbz#748048)

* Mon Feb 28 2011 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 1.3.1-1
- version upgrade (including suggestions from #681170)
- rework patches
- update menu gen script
- enabled new bidirectional support (now requires fribidi)
- vim-syntax subpackage with vim syntax files

* Sat Feb 19 2011 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 1.3.0-1
- version upgrade
- rework desktop file

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 14 2010 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 1.1.1-7
- obsolete fluxconf (#662836)

* Wed Dec 08 2010 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 1.1.1-6
- add -lfontconfig (#660981)

* Mon Aug 10 2009 Ville Skyttä <ville.skytta@iki.fi> - 1.1.1-5
- Convert specfile to UTF-8.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 08 2009 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 1.1.1-3
- make -pulseaudio package noarch

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Sep 18 2008 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 1.1.1-1
- version upgrade

* Sat Sep 06 2008 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 1.1.0.1-1
- version upgrade

* Wed Sep 03 2008 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 1.1.0-1
- version upgrade

* Thu Mar 27 2008 Christopher Aillon <caillon@redhat.com> - 1.0.0-5
- Fix the build against GCC 4.3

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.0-4
- Autorebuild for GCC 4.3

* Mon Feb 11 2008 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de> - 1.0.0-3
- Rebuilt for gcc43

* Thu Jan 03 2008 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.0.0-2
- add subpage -pulseaudio to fix #388971: fluxbox fails to start pulseaudio
  at login

* Mon Oct 08 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.0.0-1
- version upgrade

* Wed Aug 22 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 1.0.0-0.3.rc3
- rebuild for buildid

* Sun Jun 03 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.0.0-0.2.rc3
- fix #242187

* Tue Mar 20 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.0.0-0.1.rc3
- version upgrade
- fix #236509
- fix #229307

* Sat Oct 21 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.9.15.1-3
- fix #209347,#196106, and #187740

* Wed Sep 13 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.9.15.1-2
- FE6 rebuild

* Wed Apr 05 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.9.15.1-1
- version upgrade

* Mon Apr 03 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.9.15-2
- fix #187734

* Sun Mar 19 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.9.15-1
- version upgrade

* Thu Mar 02 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.9.14-3
- fix Requires
- patch startfluxbox to generate user menu
- fix gdm detection

* Thu Mar 02 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.9.14-2
- fix build on gcc41

* Thu Nov 10 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- enable nls and imlib2
- require artwizaleczepka instead of providing it...
- add menu script from Rudolf Kastl

* Thu Sep 15 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.9.14-1
- version upgrade

* Tue Sep 06 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.9.13-4
- remove X11R6 path stuff #167601

* Thu Jun 16 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.9.13-3.fc4
- fix #160614

* Wed Jun 08 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.9.13-2.fc4
- fix generate menu bug and revisit switches

* Tue May 31 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- upgrade to 0.9.13

* Wed Apr 13 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.9.9-4
- Fix build for GCC 4.

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Sat Nov 13 2004 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.9.9-2
- Fix build for GCC 3.4.

* Mon Apr 26 2004 Arnaud Abélard
- rebuilt against Fluxbox-0.9.9

* Fri Jan 16 2004 Arnaud Abélard
- now using artwiz-aleczapka as the artwiz-fonts

* Fri Jan 16 2004 Arnaud Abélard
- fixed a bug with the artwiz fonts

* Thu Jan 15 2004 Arnaud Abélard
- rebuilt against Fluxbox-0.9.8

* Sun Jan 11 2004 Arnaud Abélard
- Added Artwiz nice fonts

* Sat Jan 10 2004 Arnaud Abélard
- rebuild against Fluxbox-0.9.7

* Sat Jan 11 2003 Che
- rebuild without debug

* Mon Dec 09 2002 Che
- new version 0.1.14

* Tue Nov 19 2002 Che
- new version 0.1.13

* Wed Oct 30 2002 Che
- fixed gdm entry

* Wed Oct 23 2002 Che
- added a gdm entry :)

* Tue Oct 22 2002 Che
- initial rpm release

