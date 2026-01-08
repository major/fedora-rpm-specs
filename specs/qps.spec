Name:           qps
Version:        2.12.0
Release:        1%{?dist}
Summary:        Qt process viewer and manager

License:        GPL-2.0-or-later
URL:            https://lxqt-project.org/
Source0:        https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(lxqt)
BuildRequires:  perl

Requires:       hicolor-icon-theme

%description
Qps is a visual process manager, an X11 version of "top" or "ps" that
displays processes in a window and lets you sort and manipulate them.

Qps can:
  o  Change nice value of a process.
  o  Alter the scheduling policy and soft realtime priority of a process.
  o  Display the TCP/UDP sockets used by a process, and names of the
     connected hosts (Linux only).
  o  Display the memory mappings of the process (which files and shared
     libraries are loaded   where).
  o  Display the open files of a process, and the state of unix domain sockets.
  o  Kill or send any other signal to selected processes.
  o  Display the load average as a graph, and use this as its icon when
     iconified.
  o  Show (as graph or numbers) current CPU, memory and swap usage.
  o  Sort the process table on any attribute (size, cpu usage, owner etc).
  o  On SMP systems running Linux 2.6 or later (or Solaris), display cpu usage
     for each processor, and which CPU a process is running on.
  o  Display the environment variables of any process.
  o  Show the process table in tree form, showing the parent-child
     relationship.
  o  Execute user-defined commands on selected processes.



%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install
%find_lang %{name} --with-qt

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.lxqt.Qps.appdata.xml

%files -f %{name}.lang
%license COPYING
%doc CHANGELOG README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_metainfodir}/org.lxqt.Qps.appdata.xml
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%{_mandir}/man1/%{name}.1.gz

%changelog
* Tue Jan 6 2026 Basil Crow <me@basilcrow.com> - 2.12.0-1
- Revive packaging

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May  8 2009 Ville Skyttä <ville.skytta at iki.fi> - 1.10.2-4
- Don't strip binaries before -debuginfo is created (#499744).

* Wed Mar 04 2009 Caolán McNamara <caolanm@redhat.com> - 1.10.2-3
- include stdio.h for printf

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Sep 6 2008 Arindam Ghosh <makghosh@fedoraproject.org> - 1.10.2-1
- new upstream release
- fix gcc4.3 mass-rebuild failure
- updated license tag

* Wed Sep 3 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.9.19-0.4.b
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.9.19-0.3.b
- Autorebuild for GCC 4.3

* Mon Mar 19 2007 Dawid Gajownik <gajownik[AT]gmail.com> - 1.9.19-0.2.b
- Update to 1.9.9b

* Mon Mar  5 2007 Dawid Gajownik <gajownik[AT]gmail.com> - 1.9.19-0.1.a
- Update to 1.9.19a

