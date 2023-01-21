%define tag 206f6b6

Name:    olpc-kbdshim
Summary: OLPC XO keyboard support daemon
Version: 29
Release: 23%{?dist}
License: GPLv2+
URL: http://dev.laptop.org/git/users/pgf/olpc-kbdshim/tree/README
# Source0: the source tarball is created by "make tarball" from within
# a clone of this git tree: git://dev.laptop.org/users/pgf/olpc-kbdshim
Source0: %{name}-%{version}-git%{tag}.tar.gz

BuildRequires: make
BuildRequires: gcc
BuildRequires: kernel-headers, pkgconfig, glib2-devel
BuildRequires: dbus-glib-devel, systemd-devel
ExclusiveArch: %{ix86} %{arm}

Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
The olpc-kbdshim-udev daemon monitors the keyboard and touchpad,
enabling the XO "grab" keys and touchpad rotation (to match
screen rotation), and reporting user (in)activity.  It can also
bind the XO screen rotate, brightness, and volume keys to
appropriate commands (which are provided).

%prep
%setup -q

%build
export OPT_FLAGS="$RPM_OPT_FLAGS"
make

%install
mkdir -p %{buildroot}%{_bindir}

install -p -m 755 olpc-kbdshim-udev %{buildroot}%{_bindir}/olpc-kbdshim-udev
install -p -m 755 olpc-rotate %{buildroot}%{_bindir}/olpc-rotate
install -p -m 755 olpc-brightness %{buildroot}%{_bindir}/olpc-brightness
install -p -m 755 olpc-volume %{buildroot}%{_bindir}/olpc-volume
install -d %{buildroot}/%{_unitdir}
install -p -m 644 olpc-kbdshim.service %{buildroot}%{_unitdir}/olpc-kbdshim.service


%post
%systemd_post olpc-kbdshim.service

%preun
%systemd_preun olpc-kbdshim.service

%postun
%systemd_postun_with_restart olpc-kbdshim.service


%files
%license COPYING
%doc README
%{_bindir}/olpc-kbdshim-udev
%{_bindir}/olpc-rotate
%{_bindir}/olpc-brightness
%{_bindir}/olpc-volume
%{_unitdir}/olpc-kbdshim.service


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 29-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 29-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 29-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 29-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 29-19
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 29-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 29-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 29-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 29-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 29-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 29-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 29-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 29-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 29-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 29-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 29-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 29-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 29-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 29-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 11 2014 Peter Robinson <pbrobinson@fedoraproject.org> 29-4
- Update systemd scripts to latest distro specs

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 29-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 22 2012 Paul Fox <pgf@laptop.org>
- 29-1
- don't pass input events while the screen is blanked

* Thu Sep  6 2012 Paul Fox <pgf@laptop.org>
- 28-1
- better support for touchscreens (but swipe support is removed)
- create separate keyboard and mouse uinput devices
- prevent duplicate logging under systemd
- use more udev properties to select among the input devices

* Tue Sep  4 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 27-1
- v27
- rotation bug fixes
- systemd control files now bundled in tarball

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 20 2012 Paul Fox <pgf@laptop.org> - 26-2
- fix libudev-devel requirement

* Wed Apr 18 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 26-1
- support absolute input devices

* Mon Mar 26 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 25-1
- merge of XO-3 touchscreen support, support for 1.75 touchscreens

* Fri Feb  3 2012 Paul Fox <pgf@laptop.org> - 24-1
- use new psmouse driver control to disable touchpad in ebook mode
- implement absolute rotation selection in olpc-rotate

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Nov 19 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 23-1
- Release 23

* Sat Nov 19 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 22-2
- cleanup spec

* Mon Nov 14 2011 Paul Fox <pgf@laptop.org> - 22-1
- changing brightness no longer affects mono/color
- use ctrl-brightness-down/up will toggle mono/color

* Wed Oct 19 2011 Daniel Drake <dsd@laptop.org> - 21-1
- Unmute audio on any volume change

* Fri Sep 16 2011 Daniel Drake <dsd@laptop.org> - 20-1
- ebook mode improvements, XO-1.75 touchscreen support

* Thu Aug  4 2011 Daniel Drake <dsd@laptop.org> - 19-1
- libudev port

* Sun Jun 26 2011 Peter Robinson <pbrobinson@gmail.com> - 17-2
- Add ARM to exclusive platforms

* Sun Feb 20 2011 Daniel Drake <dsd@laptop.org> - 17-1
- new version, fixes rotation transforms

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 25 2011 Daniel Drake <dsd@laptop.org> - 16-1
- use XRandR-1.2 for screen rotation

* Mon Nov  8 2010 Daniel Drake <dsd@laptop.org> - 15-1
- fix rotation of d-pad
- honor flag file that indicates xrandr goes backwards
- ignore repeated rotate keys
- update for new hal addons location

* Fri Mar 12 2010 Paul Fox <pgf@laptop.org> - 12-1
- reduce periodic logging
- bring olpc-kbdshim more in sync with olpc-kbdshim-hal (source changes only)
- experimental code for using dbad as a pointing device

* Wed Jan 20 2010 Paul Fox <pg@laptop.org> - 11-1
- don't pass through command keystrokes when we have a command
  configured, even if that command fails.

* Tue Dec 29 2009 Paul Fox <pg@laptop.org> - 10-1
- tell uinput not to autorepeat (thanks to daniel drake, d.l.o ticket #9690)

* Tue Dec  1 2009 Paul Fox <pg@laptop.org> - 9-1
- add support for binding of local volume keys
- added olpc-volume script

* Thu Jul 30 2009 Paul Fox <pg@laptop.org> - 8-1
- add timestamps to events, to reduce racing during suspend/resume

* Tue Jul 28 2009 Paul Fox <pg@laptop.org> - 7-1
- fix touchpad rotation for F-11, which includes X11 amd/geode
  driver that fixes the earlier rotation direction issue. 
  (2.11.x and later are fixed.)
- revise Makefile for easier pre-release management

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 10 2009 Paul Fox <pg@laptop.org> - 6-3
- spec tweaks

* Sat Jun 6 2009 Paul Fox <pg@laptop.org> - 6-2
- final acceptance review changes
- olpc-brightness added

* Mon May 4 2009 Paul Fox <pg@laptop.org> - 6-1
- add local binding of rotate and brightness keys to
  eliminate sugar patching
- revise README

* Sat May 2 2009 Paul Fox <pg@laptop.org> - 5-1
- we now "grab" the arrow keys so they cause scrolling too
- initial fedora review comments incorporated in spec file.

* Sun Apr 12 2009 Paul Fox <pgf@laptop.org> - 4-1
- version numbering resync

* Sat Apr 11 2009 Paul Fox <pgf@laptop.org> - 3-3
- fix sugar patch

* Tue Apr 7 2009 Paul Fox <pgf@laptop.org> - 3-2
- convert to HAL-based operation

* Fri Mar 13 2009 Paul Fox <pgf@laptop.org> - 2-2
- add comments to the post handler, fix rpmlint errors, rename
  LICENSING to COPYING
