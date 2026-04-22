Name:           qps
Version:        2.12.0
Release:        2%{?dist}
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
%autochangelog

