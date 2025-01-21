%global appname switchmail
%global __python /usr/bin/python3

Summary: The Mail Transport Agent Switcher
Name: system-switch-mail
Version: 2.0.1
Release: 23%{?dist}
Url: http://than.fedorapeople.org/system-switch-mail
Source0: http://than.fedorapeople.org/system-switch-mail/%{name}-%{version}.tar.xz
Patch0: system-switch-mail-2.0.1-python3.patch
License: GPL-2.0-or-later
BuildArch: noarch

Requires: newt-python3
Requires: polkit

BuildRequires: make
BuildRequires:  python3-devel
BuildRequires: gettext
BuildRequires: intltool
BuildRequires: desktop-file-utils

%description
The system-switch-mail is the Mail Transport Agent Switcher.
It enables users to easily switch between various Mail Transport Agent
that they have installed.

%package gui
Summary: A GUI interface for Mail Transport Agent Switcher
Requires: %{name} = %{version}-%{release}
Requires: usermode-gtk
Requires: python3-gobject-base
Requires: desktop-file-utils
Obsoletes: %{name}-gnome < 2.0

%description gui
The system-switch-mail-gnome package contains a GNOME interface for the
Mail Transport Agent Switcher.

%prep
%autosetup -p1

%build
make %{?_smp_mflags}

%install
make PYTHON=%{__python3} DESTDIR=%{buildroot} mandir=%{_mandir} sysconfdir=%{_sysconfdir} install
desktop-file-validate %{buildroot}%{_datadir}/applications/%{appname}.desktop
%py_byte_compile %{__python3} %{buildroot}%{_datadir}/%{name}/

%find_lang %{name}

%files -f %{name}.lang
%doc COPYING AUTHORS
%{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/backend.py*
%{_datadir}/%{name}/%{appname}-tui.py*
%{_mandir}/man1/*

%files gui
%{_datadir}/polkit-1/actions/org.fedoraproject.switchmail.policy
%{_datadir}/applications/*
%{_datadir}/%{name}/%{appname}-gui.py*
%{_datadir}/%{name}/%{appname}.glade
%{_datadir}/%{name}/__pycache__
%{_datadir}/pixmaps/*.png

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Mar 06 2024 Than Ngo <than@redhat.com> - 2.0.1-21
- fixed bz#2268132, drop usermode

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Feb 21 2023 Than Ngo <than@redhat.com> - 2.0.1-18
- migrated to SPDX license

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 07 2020 Than Ngo <than@redhat.com> - 2.0.1-12
- added bytecode

* Tue Aug 25 2020 Than Ngo <than@redhat.com> - 2.0.1-11
- fixed bz#1865563 - FTBFS

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-10
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 20 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-7
- Drop the build dependency on Python 2

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 25 2018 Than Ngo <than@redhat.com> - 2.0.1-4
- fixed FTBFS

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 03 2018 Than Ngo <than@redhat.com> - 2.0.1-2
- replace with python3
- enable byte compilation and included it

* Wed Mar 28 2018 Than Ngo <than@redhat.com> - 2.0.1-1
- add missing icon
- fix wrong exec entry in desktop file

* Sat Mar 24 2018 Than Ngo <than@redhat.com> - 2.0.0-1
- release 2.0.0 with python3 and gtk3 support

* Fri Jul 28 2017 Than Ngo <than@redhat.com> - 1.0.3-1
- release 1.0.3

* Fri Apr 28 2017 Than Ngo <than@redhat.com> - 1.0.2-1
- release 1.0.2

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 31 2017 Than Ngo <than@redhat.com> - 1.0.1-11
- fixed bz#1412714, add TUI support

* Tue Jun 28 2016 Than Ngo <than@redhat.com> - 1.0.1-10
- fixed bz#493849, S-c-tools cleanup ui
- fixed bz#493899, make OK button insensitive when no action has been taken
- fixed bz#493924, port to PolicyKit
- fixed bz#493617, System Configuration Tools Cleanup Project

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 Than Ngo <than@redhat.com> - 1.0.1-1
- bz#226473, merge Review: system-switch-mail

* Tue Sep 29 2009 Than Ngo <than@redhat.com> - 1.0-1
- update po files

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.26-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.26-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 01 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.5.26-4
- Rebuild for Python 2.6

* Sat Sep  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.5.26-3
- fix license tag

* Tue Mar 11 2008 Than Ngo <than@redhat.com> 0.5.26-2
- fix permission of po files (bz#436888)
- update po files

* Fri Mar 07 2008 Than Ngo <than@redhat.com> 0.5.26-1
- 0.5.26 release
   - use chkconfig to configure selected MTA to start automatically (#436359)
   - add missing file in POTFILES.in (#433456)
   - use correct python version (#427571)
   - chkconfig off/on after mta is switched (#246092)
   - Require newt-python (#251363)
   - remove obsolete translation (#332461)
   - add man page (#427570)

* Tue Apr 10 2007 Than Ngo <than@redhat.com> - 0.5.25-13
- add support for ssmtp and esmtp

* Mon Dec 18 2006 Phil Knirsch <pknirsch@redhat.com> - 0.5.25-12
- Resolves: bz#216602, one more update for kn and si po files

* Mon Dec 04 2006 Than Ngo <than@redhat.com> - 0.5.25-11
- Resolved: bz#216602, update po files

* Mon Jul 17 2006 Than Ngo <than@redhat.com> 0.5.25-10
- update po files

* Tue Mar 07 2006 Than Ngo <than@redhat.com> 0.5.25-8
- fix deprecated functions in gtk #159155

* Mon Feb 27 2006 Than Ngo <than@redhat.com> 0.5.25-7
- fix consolehelper config #160931

* Sat Dec 17 2005 Than Ngo <than@redhat.com> 0.5.25-6
- update po files

* Wed Oct 26 2005 Than Ngo <than@redhat.com> 0.5.25-5
- add new common pam configuration file #170650 
- update po files

* Wed May 11 2005 Than Ngo <than@redhat.com> 0.5.25-4
- fix location for menu item #157173

* Fri Oct 01 2004 Than Ngo <than@redhat.com> 0.5.25-3
- update translation

* Tue Sep 21 2004 Than Ngo <than@redhat.com> 0.5.25-2
- rebuilt

* Mon Apr 05 2004 Than Ngo <than@redhat.com> 0.5.25-1
- 0.5.25 release

* Thu Feb 19 2004 Than Ngo <than@redhat.com> 0.5.24-1
- 0.5.24 release

* Sun Feb 15 2004 Than Ngo <than@redhat.com> 0.5.23-1
- 0.5.23 release

* Tue Nov 25 2003 Than Ngo <than@redhat.com> 0.5.22-1
- 0.5.22: renamed to system-switch-mail, support Exim MTA    

* Mon Sep 29 2003 Than Ngo <than@redhat.com> 0.5.21-1
- 0.5.21, fixed Categories

* Thu Aug 14 2003 Than Ngo <than@redhat.com> 0.5.20-1
- 0.5.20, use intltool instead pygettext,
  thanks to Miloslav Trmac (bug #82319, #83464)

* Thu Jul 17 2003 Than Ngo <than@redhat.com> 0.5.19-1
- 0.5.19
- exim support
- UTF8 issue in PO files

* Wed Feb  5 2003 Than Ngo <than@redhat.com> 0.5.18-1
- 0.5.18

* Mon Feb  3 2003 Than Ngo <than@redhat.com> 0.5.17-1
- 0.5.17

* Tue Dec 10 2002 Than Ngo <than@redhat.com> 0.5.16-1
- rename to redhat-switch-mail
- start service after successfully switched

* Sat Nov  9 2002 Than Ngo <than@redhat.com> 0.5.15-1
- updated po files
- remove some unpackaged files

* Tue Sep  3 2002 Than Ngo <than@redhat.com> 0.5.14-1
- Updated po files

* Mon Aug 26 2002 Than Ngo <than@redhat.com> 0.5.13-1
- Fix some inconsistent interface (bug #72443)

* Mon Aug 12 2002 Karsten Hopp <karsten@redhat.de>
- fix german translation. String output was completely broken
- use SystemSetup keyword

* Wed Aug  7 2002 Than Ngo <than@redhat.com> 0.5.11-1
- move to X-Red-Hat-Extra (bug #70992)
- Updated po files

* Tue Aug  6 2002 Than Ngo <than@redhat.com> 0.5.10-1
- Fixed a bug in warningDialog (bug #70828)
- Updated po files

* Fri Jul 26 2002 Than Ngo <than@redhat.com> 0.5.9-1
- Use pam_timestamp.so

* Thu Jul 25 2002 Than Ngo <than@redhat.com> 0.5.8-1
- new desktop file
- update po files

* Wed Jun 12 2002 Harald Hoyer <harald@redhat.de>
- fallback for C locale

* Wed Jun 12 2002 Than Ngo <than@redhat.com> 0.5.6-1
- fixed traceback bug (bug #66465)

* Mon Jun  3 2002 Harald Hoyer <harald@redhat.de>
- dropped gnome2, fixed automake Req

* Wed May 29 2002 Phil Knirsch <pknirsch@redhat.com> 0.5.3-1
- Included all fixes for gnome2 by Harald Hoyer <harald@redhat.com>

* Wed May 29 2002 Phil Knirsch <pknirsch@redhat.com> 0.5.2-2
- Fixed to build in new environment.

* Wed Apr 24 2002 Than Ngo <than@redhat.com> 0.5.2-1
- fixed a bug in runing in text mode in X

* Wed Apr 10 2002 Than Ngo <than@redhat.com> 0.5.1-1
- release 0.5.1
- update translations

* Mon Apr  8 2002 Than Ngo <than@redhat.com> 0.5.0-1
- release 0.5.0

* Sun Mar 31 2002 Than Ngo <than@redhat.com> 0.4.0-1
- release 0.4.0

* Sat Mar 02 2002 Than Ngo <than@redhat.com> 0.3.0-1
- update to 0.3.0 (bug #60590, #60591)

* Tue Feb 26 2002 Than Ngo <than@redhat.com> 0.2.0-1
- update to 0.2.0

* Thu Jan 31 2002 Bill Nottingham <notting@redhat.com> 0.1.1-1
- %%defattr in -gnome package

* Mon Jan 28 2002 Than Ngo <than@redhat.com> 0.1.0-1
- initial packaging
