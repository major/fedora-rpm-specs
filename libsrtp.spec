%global shortname srtp

Name:		libsrtp
Version:	2.3.0
Release:	11%{?dist}
Summary:	An implementation of the Secure Real-time Transport Protocol (SRTP)
License:	BSD
URL:		https://github.com/cisco/libsrtp
Source0:	https://github.com/cisco/libsrtp/archive/v%{version}.tar.gz
BuildRequires:	gcc, nss-devel, libpcap-devel
BuildRequires: make
BuildRequires: procps-ng
# Fix shared lib so ldconfig doesn't complain
Patch0:		libsrtp-2.3.0-shared-fix.patch
# Fix namespace issue in test/util.c
Patch1:		libsrtp-2.3.0-test-util.patch
# Link test binaries against shared lib
Patch2:		libsrtp-2.3.0-shared-test-fix.patch
# Fix issue with NSS 3.63 incompatibility
# credit to George Joseph
Patch3:		libsrtp-2.3.0-nss-3.63-fix.patch

%description
This package provides an implementation of the Secure Real-time
Transport Protocol (SRTP), the Universal Security Transform (UST), and
a supporting cryptographic kernel.

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	pkgconfig

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package tools
Summary:	Tools for testing and decoding SRTP
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description tools
Tools for testing and decoding SRTP

%prep
%setup -q -n %{name}-%{version}
%patch 0 -p1 -b .sharedfix
%patch 1 -p1 -b .utilfix
%patch 2 -p1 -b .test-shared-fix
%patch 3 -p1 -b .nssfix

%if 0%{?rhel} > 0
%ifarch ppc64
sed -i 's/-z noexecstack//' Makefile.in
%endif
%endif

%build
export CFLAGS="%{optflags} -fPIC"
%configure --enable-nss
make %{?_smp_mflags} shared_library test

%install
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -exec rm -f {} ';'

install -D -p -m 0755 test/dtls_srtp_driver %{buildroot}%{_bindir}/dtls_srtp_driver
install -D -p -m 0755 test/rdbx_driver %{buildroot}%{_bindir}/rdbx_driver
install -D -p -m 0755 test/replay_driver %{buildroot}%{_bindir}/replay_driver
install -D -p -m 0755 test/roc_driver %{buildroot}%{_bindir}/roc_driver
install -D -p -m 0755 test/rtp_decoder %{buildroot}%{_bindir}/rtp_decoder
install -D -p -m 0755 test/rtpw %{buildroot}%{_bindir}/rtpw
install -D -p -m 0755 test/srtp_driver %{buildroot}%{_bindir}/srtp_driver
install -D -p -m 0755 test/test_srtp %{buildroot}%{_bindir}/test_srtp

%ldconfig_scriptlets

%check
# the test code does by default not use the libsrtp we built here, but the one installed on the system
# force LD_LIBRARY_PATH to use the one built in this spec
export LD_LIBRARY_PATH="%{_builddir}/%{name}-%{version}"
sed -i -e 's#LD_LIBRARY_PATH=.*#LD_LIBRARY_PATH=\"%{_builddir}/%{name}-%{version}\"#' test/rtpw_test.sh test/rtpw_test_gcm.sh
make runtest

%files
%license LICENSE
%doc CHANGES README.md
%{_libdir}/*.so.*

%files devel
%{_includedir}/%{shortname}2/
%{_libdir}/pkgconfig/libsrtp2.pc
%{_libdir}/*.so

%files tools
%{_bindir}/*

%changelog
* Fri Jul 07 2023 Wim Taymans <wtaymans@redhat.com> - 2.3.0-11
- add %check (thanks to Gerd v. Egidy) Related: rhbz#2163492

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Apr 15 2021 Tom Callaway <spot@fedoraproject.org> - 2.3.0-6
- fix NSS incompatibility, thanks to George Joseph

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 12 2020 Tom Callaway <spot@fedoraproject.org> - 2.3.0-4
- add -tools subpackage (thanks to Gerd v. Egidy)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan  7 2020 Tom Callaway <spot@fedoraproject.org> - 2.3.0-1
- update to 2.3.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Tom Callaway <spot@fedoraproject.org> - 1.5.4-9
- add BuildRequires: gcc

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Mar  2 2016 Tom Callaway <spot@fedoraproject.org> - 1.5.4-3
- use upstream provided .pc file (bz1313590)

* Fri Feb 12 2016 Tom Callaway <spot@fedoraproject.org> - 1.5.4-2
- fix shared lib generation to silence ldconfig

* Thu Feb 11 2016 Tom Callaway <spot@fedoraproject.org> - 1.5.4-1
- update to 1.5.4
- fix MIPS name collision (bz1305950 ) Thanks to Michal Toman

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Nov 14 2014 Tom Callaway <spot@fedoraproject.org> - 1.5.0-2
- fix library linking typo

* Fri Nov 14 2014 Tom Callaway <spot@fedoraproject.org>
- api changes between 1.4.4 and 1.5.0, bump sover to 1.0.0
- fix linking issue to make proper libsrtp.so.1

* Fri Oct 31 2014 Leif Madsen <leif@leifmadsen.com> - 1.5.0-1
- Update for 1.5.0 release.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.4-13.20101004cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.4-12.20101004cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 15 2014 Dennis Gilmore <dennis@ausil.us> - 1.4.4-11.20101004cvs
- update the config.h header aarch64 is a 64 bit arch though there is no multilib

* Mon Feb 10 2014 Tom Callaway <spot@fedoraproject.org> - 1.4.4-10.20101004cvs
- rename internal functions to avoid conflicts (bz 956340)

* Mon Dec 30 2013 Tom Callaway <spot@fedoraproject.org> - 1.4.4-9.20101004cvs
- apply fix for CVE-2013-2139 from https://github.com/cisco/libsrtp/pull/27

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.4-8.20101004cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.4-7.20101004cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Sep 25 2012 Karsten Hopp <karsten@redhat.com> 1.4.4-6.20101004cvs
- use __PPC64__, not __ppc64__ which is undefined on PPC64 arch

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.4-5.20101004cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 21 2012 Tom Callaway <spot@fedoraproject.org> - 1.4.4-4.20101004cvs
- handle config.h multilib (bz787537)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.4-3.20101004cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.4-2.20101004cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 25 2011 Jeffrey C. Ollie <jeff@ocjtech.us>
- Don't use '-z noexecstack' option for linker on PPC64 (EL6)

* Mon Oct  4 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 1.4.4-1.20101004cvs
- initial package
