Name:           qps
Version:        1.10.2
Release:        6%{?dist}
Summary:        Visual process manager

Group:          Applications/System
License:        GPLv2+
URL:            http://qps.kldp.net/
Source0:        http://kldp.net/frs/download.php/4776/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  desktop-file-utils
BuildRequires:  qt4-devel >= 4.3.0

Patch0:         qps-1.10.2-includes.patch
Patch1:         qps-1.10.2-nostrip.patch


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
%setup -q
%patch0 -p1 -b .includes
%patch1 -p1 -b .nostrip

iconv --from-code ISO88591 --to-code UTF8 ./CHANGES \
--output CHANGES.utf-8 && mv CHANGES.utf-8 ./CHANGES
 

%build
qmake-qt4
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
install -D -p -m 0755 qps %{buildroot}%{_bindir}/qps
install -D -p -m 0644 qps.1 %{buildroot}%{_mandir}/man1/qps.1
install -D -p -m 0644 icon/icon.xpm %{buildroot}%{_datadir}/pixmaps/qps.xpm
install -D -p -m 0644 qps.desktop %{buildroot}%{_datadir}/applications/qps.desktop

desktop-file-install --vendor=fedora \
        --remove-category=Application \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/qps.desktop


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc CHANGES COPYING
%{_bindir}/qps
%{_datadir}/applications/*
%{_datadir}/pixmaps/qps.xpm
%{_mandir}/man1/qps.1*


%changelog
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

