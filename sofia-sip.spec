Name:           sofia-sip
Version:        1.13.9
Release:        1%{?dist}
Summary:        Sofia SIP User-Agent library

License:        LGPLv2+
URL:            http://sofia-sip.sourceforge.net/
Source0:        https://github.com/freeswitch/%{name}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  openssl-devel
BuildRequires:  glib2-devel
BuildRequires:  lksctp-tools-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:  libtool >= 1.5.17

%description
Sofia SIP is a RFC-3261-compliant library for SIP user agents and
other network elements.  The Session Initiation Protocol (SIP) is an
application-layer control (signaling) protocol for creating,
modifying, and terminating sessions with one or more
participants. These sessions include Internet telephone calls,
multimedia distribution, and multimedia conferences.

%package devel
Summary:        Sofia-SIP Development Package
Requires:       sofia-sip = %{version}-%{release}
Requires:       pkgconfig

%description devel
Development package for Sofia SIP UA library.

%package glib
Summary:        Glib bindings for Sofia-SIP
Requires:       sofia-sip = %{version}-%{release}

%description glib
GLib interface to Sofia SIP User Agent library.

%package glib-devel
Summary:        Glib bindings for Sofia SIP development files
Requires:       sofia-sip-glib = %{version}-%{release}
Requires:       sofia-sip-devel = %{version}-%{release}
Requires:       pkgconfig

%description  glib-devel
Development package for Sofia SIP UA Glib library. This package
includes libraries and include files for developing glib programs
using Sofia SIP.

%package utils
Summary:        Sofia-SIP Command Line Utilities
Requires:       sofia-sip = %{version}-%{release}

%description utils
Command line utilities for the Sofia SIP UA library.


%prep
%autosetup

%build
sh autogen.sh
%configure --disable-rpath --disable-static --without-doxygen --disable-stun
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -name \*.la -delete
find %{buildroot} -name \*.h.in -delete
find . -name installdox -delete

%ldconfig_scriptlets
%ldconfig_scriptlets glib

%files
%doc AUTHORS ChangeLog ChangeLog.ext-trees COPYING COPYRIGHTS
%doc README README.developers RELEASE TODO
%{_libdir}/libsofia-sip-ua.so.*

%files devel
#%doc libsofia-sip-ua/docs/html
%dir %{_includedir}/sofia-sip-1.13
%dir %{_includedir}/sofia-sip-1.13/sofia-sip
%{_includedir}/sofia-sip-1.13/sofia-sip/*.h
%exclude %{_includedir}/sofia-sip-1.13/sofia-sip/su_source.h
%dir %{_includedir}/sofia-sip-1.13/sofia-resolv
%{_includedir}/sofia-sip-1.13/sofia-resolv/*.h
%{_libdir}/libsofia-sip-ua.so
%{_libdir}/pkgconfig/sofia-sip-ua.pc
%{_datadir}/sofia-sip

%files glib
%{_libdir}/libsofia-sip-ua-glib.so.*

%files glib-devel
%{_includedir}/sofia-sip-1.13/sofia-sip/su_source.h
%{_libdir}/libsofia-sip-ua-glib.so
%{_libdir}/pkgconfig/sofia-sip-ua-glib.pc

%files utils
%{_bindir}/addrinfo
%{_bindir}/localinfo
%{_bindir}/sip-date
%{_bindir}/sip-dig
%{_bindir}/sip-options


%changelog
* Sat Sep 17 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 1.13.9-1
- Update for 1.13.9

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 02 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 1.13.8-1
- Update for 1.13.8

* Fri Jan 28 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 1.13.7-1
- Update for 1.13.7

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Oct 23 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 1.13.6-1
- Update for 1.13.6

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.13.4-3
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 15 2021 Torrey sorensen <torbuntu@fedoraproject.org> - 1.13.4-1
- Update for 1.13.4

* Fri Apr 23 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 1.13.3-1
- Update for 1.13.3

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.11-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild
 
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.11-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild
 
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.11-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild
 
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.11-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild
 
* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.11-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
 
* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.11-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild
 
* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.11-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild
 
* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.11-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild
 
* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.11-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild
 
* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.11-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild
 
* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
 
* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild
 
* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild
 
* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild
 
* Thu Dec  5 2013 Brian Pepple <bpepple@fedoraproject.org> - 1.12.11-8
- Add patch to fix compiler error. (#981056)
 
* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild
 
* Thu Jul 11 2013 Debarshi Ray <rishi@fedoraproject.org> 1.12.11-6
- Rebuilt to fix broken binary possibly caused by broken toolchain
 
* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild
 
* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild
 
* Thu May 24 2012 Brian Pepple <bpepple@fedoraproject.org> - 1.12.11-3
- Do not use enable-sctp option. (#817579)
 
* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild
 
* Tue Sep 27 2011 Brian Pepple <bpepple@fedoraproject.org> - 1.12.11-1
- Update to 1.12.11.
- Drop non-weak symbol patch. Fixed upstream.
- Drop buildroot and clean section. No longer necessary.
 
* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
 
* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 1.12.10-5
- rebuilt with new openssl
 
* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild
 
* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild
 
* Sat Jan 17 2009 Tomas Mraz <tmraz@redhat.com> - 1.12.10-2
- rebuild with new openssl
 
* Tue Dec  9 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.12.10-1
- Update to 1.12.10
 
* Sat Jun 14 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.12.9-1
- Update to 1.12.9
- Disable building API documentation because it won't build on PPC/PPC64 (at least in a reasonable amount of time).
 
* Mon Feb 11 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.12.8-1
- Update to 1.12.8
 
* Thu Dec 06 2007 Release Engineering <rel-eng at fedoraproject dot org> - 1.12.6-12
- Rebuild for deps
 
* Tue Aug 28 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.12.6-11
- Update license tag.
 
* Tue Jul 31 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.12.6-10
- Clean up
 
* Tue Jul 31 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.12.6-9
- Enable building on PPC64
 
* Tue Jul  3 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.12.6-8
- Disable checks for now, they all pass in local mock builds but fail when built with plague.
 
* Tue Jul  3 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.12.6-7
- Enable more debugging output from "make check"
 
* Tue Jul  3 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.12.6-6
- Block building on ppc64
 
* Mon Jul  2 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.12.6-5
- Update description.
 
* Fri Jun 29 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.12.6-4
- Get rid of .h.in files.
 
* Fri Jun 29 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.12.6-3
- Link glib library with main library.
 
* Tue Jun 26 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.12.6-2
- Re-run libtoolize and auto* to fix rpath issues.
- Add --disable-rpath to the configure line.
- The devel packages need to BR pkgconfig.
 
* Wed Apr 25 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.12.6-1
- Update to 1.12.6
 
* Fri Apr 13 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.12.5-4.work6
- Update to 1.12.5work6
- Add workaround to get tests working.
 
* Mon Mar  5 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.12.5-2
- Update to 1.12.5work1
 
* Thu Jan 11 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.12.4-1
- First version for Fedora Extras
