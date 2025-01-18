Name:           eventlog
Version:        0.2.13
Release:        29%{?dist}
Summary:        Syslog-ng v2/v3 support library

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://www.balabit.com/network-security/syslog-ng/opensource-logging-system
Source:         http://www.balabit.com/downloads/files/syslog-ng/open-source-edition/3.4.4/source/%{name}_%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make

%description
The EventLog library aims to be a replacement of the simple syslog() API
provided on UNIX systems. The major difference between EventLog and syslog
is that EventLog tries to add structure to messages.

EventLog provides an interface to build, format and output an event record.
The exact format and output method can be customized by the administrator
via a configuration file.

This package is the runtime part of the library.


%package devel
Summary:        Syslog-ng v2/v3 support library development files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The EventLog library aims to be a replacement of the simple syslog() API
provided on UNIX systems. The major difference between EventLog and syslog
is that EventLog tries to add structure to messages.

EventLog provides an interface to build, format and output an event record.
The exact format and output method can be customized by the administrator
via a configuration file.

This package contains the development files.


%package static
Summary:        Syslog-ng v2/v3 support static library files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description static
The EventLog library aims to be a replacement of the simple syslog() API
provided on UNIX systems. The major difference between EventLog and syslog
is that EventLog tries to add structure to messages.

EventLog provides an interface to build, format and output an event record.
The exact format and output method can be customized by the administrator
via a configuration file.

This package contains the static library files.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

rm -f %{buildroot}%{_libdir}/libevtlog.la



%ldconfig_scriptlets


%files
%doc AUTHORS ChangeLog COPYING CREDITS NEWS README
%{_libdir}/libevtlog.so.*

%files devel
%doc doc/*
%{_libdir}/libevtlog.so
%{_libdir}/pkgconfig/eventlog.pc
%dir %{_includedir}/%{name}
%{_includedir}/%{name}

%files static
%{_libdir}/libevtlog.a


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.13-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 0.2.13-28
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.13-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.13-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.13-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.13-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.13-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.13-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.13-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.13-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.13-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.13-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.13-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.13-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.13-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.13-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 Matthias Runge <mrunge@redhat.com> - 0.2.13-13
- add buildrequirement gcc

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.13-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.13-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.13-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.13-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct 17 2013 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.2.13-4
- Updated the Source and URL fields

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan  7 2013 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.2.13-1
- update to version 0.2.13

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 20 2012 Matthias Runge <mrunge@matthias-runge.de> - 0.2.12-5
- temporarily switch back from /usr/sbin/ldconfig to /sbin/ldconfig
  until UsrMove is landed in rawhide

* Fri Feb  3 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.2.12-4
- Fedora 17’s unified filesystem (/usr-move)
  http://fedoraproject.org/wiki/Features/UsrMove
- Dropped the BuildRoot and the default attributes lines.

* Sun Jan 15 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.2.12-3
- Summary update.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Apr 13 2011 Matthias Runge <mrunge@matthias-runge.de> - 0.2.12-1
- update to version 0.2.12

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 24 2009 Douglas E. Warner <silfreed@silfreed.net> 0.2.7-3
- re-added the -static package

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Apr 09 2008 Douglas E. Warner <silfreed@silfreed.net> 0.2.7-1
- updated to 0.2.7 library
- removed static library

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.2.5-9
- Autorebuild for GCC 4.3

* Thu Jun  7 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.2.5-8
- Fixed URL typo.

* Thu Jun  7 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.2.5-7
- New upstream download location
  (https://lists.balabit.hu/pipermail/syslog-ng/2007-May/010258.html)

* Sun Mar 11 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.2.5-6
- The -devel subpackage now obsoletes the -static subpackage if the
  latter one is not created.

* Fri Mar  9 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.2.5-5
- Optional creation of the -static subpackage.

* Sun Feb 25 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.2.5-4
- Install the dynamic library in /lib.

* Sat Feb 10 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.2.5-3
- Create a -static subpackage.

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> - 0.2.5-2
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Sun Jul 16 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.2.5-1
- Update to 0.25.

* Tue Feb 28 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.2.4-1
- Update to 0.24.

* Sun Oct 16 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.2.3-1
- Update to 0.2.3+20051004 snapshot.

* Fri Apr 22 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.2.3-1
- Update to 0.2.3+20050422 snapshot.
- FLAGS are now being inherited by configure (patch accepted upstream).
- Static lib created by default.
- Copyright information (README and COPYING files).

* Sat Jan 15 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:0.2.2-0.fdr.0
- Update to 0.2.2.

* Wed Jan 12 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:0.2.1-0.fdr.0
- Initial build (version 0.2.1).

