Name: wmx
Version: 8
Release: 25%{?dist}
Summary: A really simple window manager for X
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
URL: http://www.all-day-breakfast.com/wmx/
Source0: http://www.all-day-breakfast.com/wmx/%{name}-%{version}.tar.gz
Source1: wmx-defaults-3.tar.gz
Source2: background.xpm
Source3: wmx.desktop
Source4: Xclients.wmx.sh
Patch0: wmx-8-cfg.patch
#wmx's 'New' button is hardcoded to start an xterm, better make sure we have it:
Requires: xterm
BuildRequires: make
BuildRequires: gcc-c++ xorg-x11-proto-devel libX11-devel libXpm-devel libXext-devel libXaw-devel libXt-devel libXcomposite-devel freetype-devel libXft-devel

%description
A really simple window manager for X, based on wm2, with a minimal set of
configurable options.

%prep
%setup -q
%setup -q -a 1
%{__install} -p -m 0644 %{SOURCE2} .
%patch -P0 -p1

%build
%configure --x-libraries=%{_libdir} --x-includes=%{_includedir}/X11 LIBS=-lfontconfig
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m 0755 wmx %{buildroot}%{_bindir}/wmx
%{__install} -d -m 0755 %{buildroot}%{_datadir}/%{name}
%{__install} -m 0755 wmx-defaults-3/* %{buildroot}%{_datadir}/%{name}
%{__chmod} 0644 %{buildroot}%{_datadir}/%{name}/startup
%{__install} -D -m 0644 %{SOURCE3} %{buildroot}%{_datadir}/xsessions/wmx.desktop
%{__install} -D -m 0755 %{SOURCE4} %{buildroot}%{_sysconfdir}/X11/xinit/Xclients.d/Xclients.wmx.sh

%files
%doc README* UPDATES TODO.netwm rsharman-patch/
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/xsessions/*
%{_sysconfdir}/X11/xinit/Xclients.d/*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 8-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 8-24
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 29 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Gabriel Somlo <somlo@cmu.edu> 8-10
- add "BuildRequires: gcc-c++" (#1606700)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 8-2
- Rebuilt for GCC 5 C++11 ABI change

* Thu Nov 20 2014 Gabriel Somlo <somlo@cmu.edu> 8-1
- update to 8

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7-14.20120109svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7-13.20120109svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7-12.20120109svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7-11.20120109svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7-10.20120109svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan 09 2012 Gabriel Somlo <somlo@cmu.edu> 7-9.20120109svn
- upgrade to latest svn checkout
- updated defaults
- dropped xnodecor

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 07 2010 Gabriel Somlo <somlo@cmu.edu> 7-7
- explicitly link against libfontconfig (BZ 660741)

* Mon Mar 01 2010 Gabriel Somlo <somlo@cmu.edu> 7-6
- fixed directory ownership (BZ 569408)

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jan 19 2009 Gabriel Somlo <somlo@cmu.edu> 7-3
- applied patch for use of compositing offscreen storage to speed up rendering
- added buildreq for libxcomposite-devel

* Tue Jan 13 2009 Gabriel Somlo <somlo@cmu.edu> 7-2
- re-enabled scroll-wheel-cycles-channels feature

* Sat Jan 10 2009 Gabriel Somlo <somlo@cmu.edu> 7-1
- update to 7

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 6pl1-18
- Autorebuild for GCC 4.3

* Tue Dec 25 2007 Gabriel Somlo <somlo@cmu.edu> 6pl1-17
- changed build config option to use default X cursor fonts

* Sat Nov 17 2007 Gabriel Somlo <somlo@cmu.edu> 6pl1-16
- rebuild

* Tue Nov 13 2007 Gabriel Somlo <somlo@cmu.edu> 6pl1-15
- patch containing latest cvs fixes
- added xnodecor.c from ftp://ftp.42.org/pub/wmx/contrib/xnodecor.c
- updated default menu entries

* Fri Sep 08 2006 Gabriel Somlo <somlo@cmu.edu> 6pl1-14
- rebuilt for FC6MassRebuild

* Thu Jun 08 2006 Gabriel Somlo <somlo@cmu.edu> 6pl1-13
- rebuild

* Thu Jun 08 2006 Gabriel Somlo <somlo@cmu.edu> 6pl1-12
- more X11 buildrequires (thanks tibbs@math.uh.edu and Jarod Wilson)

* Wed Jun 07 2006 Gabriel Somlo <somlo@cmu.edu> 6pl1-11
- fixed modular X11 build-requires

* Mon Jun 05 2006 Gabriel Somlo <somlo@cmu.edu> 6pl1-10
- gave up on conditional build-requires for X based on fedora version

* Sun Jun 04 2006 Gabriel Somlo <somlo@cmu.edu> 6pl1-9
- added patch containing latest cvs fixes
- both monolithic and modular X supported in the same specfile (to be removed when we drop support for fc4)
- added patch by zpetkovic@acm.org for dynamic config string termination bug
- cvs patch screws up ALT key define, subsequent config patch puts it back

* Fri May 19 2006 Gabriel Somlo <somlo@cmu.edu> 6pl1-8
- Don't strip binary during install to preserve debuginfo (bugzilla #192435)

* Thu Feb 16 2006 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net>
- Fixed 64-bit build

* Sat Dec 31 2005 Gabriel Somlo <somlo@cmu.edu> 6pl1-7
- added BuildRequires for X

* Thu Dec 29 2005 Gabriel Somlo <somlo@cmu.edu> 6pl1-6
- more spec file fixes as per I. Vazquez
- default startup script tweaks

* Mon Dec 19 2005 Gabriel Somlo <somlo@cmu.edu> 6pl1-5
- removed example .xsession file
- added /etc/X11/xinit/Xclients.d/Xclients.wmx.sh startup script
- fixed up some of the default menu entries

* Mon Dec 19 2005 Gabriel Somlo <somlo@cmu.edu> 6pl1-4
- spec file fixes as per J. Carlson
- desktop file for xdm login screen

* Fri Dec 16 2005 Gabriel Somlo <somlo@cmu.edu> 6pl1-3
- spec file fixes as per P. Lemenkov and I. Vazquez
- default menu entries now go in /usr/share/wmx/menu
- example wmx .xsession file added to doc
- gave up on using /usr/X11R6/bin -- using bindir instead

* Wed Dec 14 2005 Gabriel Somlo <somlo@cmu.edu> 6pl1-2
- increased bump-distance parameter for easier placement at edge of screen
- 'fix' patch now cleans up dead files from source directory

* Wed Sep 07 2005 Gabriel Somlo <somlo@cmu.edu> 6pl1-1
- upgrade to 6pl1
- added better looking window-tab background.xpm
- fixed license (bsd, not gpl)

* Tue Aug 09 2005 Gabriel Somlo <somlo@cmu.edu> 6pl1-0
- rebuilt for Fedora Core 4

* Sun May 23 2004 Gabriel Somlo <somlo@acns.colostate.edu>
- initial spec and packages.
