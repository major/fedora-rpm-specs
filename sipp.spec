Summary:	SIP test tool / traffic generator
Name:		sipp
Version:	3.6.0
Release:	11%{?dist}
License:	GPLv2+
URL:		https://github.com/SIPp/sipp
VCS:            scm:git:https://github.com/SIPp/sipp.git
Source0:	https://github.com/SIPp/sipp/releases/download/v%{version}/%{name}-%{version}.tar.gz
Patch1:		sipp-0001-Removal-of-bundled-gmock-gtest.patch
Patch2:		sipp-0002-Fix-for-gtest-higher-than-1.8.0.patch
BuildRequires: make
BuildRequires:	autoconf
BuildRequires:	autoconf-archive
BuildRequires:	automake
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	gmock-devel
BuildRequires:	gtest-devel
BuildRequires:	libpcap-devel
BuildRequires:	libtool
BuildRequires:	lksctp-tools-devel
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig(openssl)


%description
SIPp is a free Open Source test tool / traffic generator for the SIP protocol.
It includes a few basic SipStone user agent scenarios (UAC and UAS) and
establishes and releases multiple calls with the INVITE and BYE methods. It
can also reads custom XML scenario files describing from very simple to
complex call flows. It features the dynamic display of statistics about
running tests (call rate, round trip delay, and message statistics), periodic
CSV statistics dumps, TCP and UDP over multiple sockets or multiplexed with
retransmission management and dynamically adjustable call rates.


%prep
%autosetup -p1

%build
autoreconf -ivf
echo "#define SIPP_VERSION \"v%{version}\"" > include/version.h
%configure --with-openssl --with-pcap --with-sctp
make %{?_smp_mflags}


%install
install -D -p -m 755 sipp %{buildroot}%{_bindir}/%{name}
mkdir -p %{buildroot}%{_datadir}/%{name}/pcap
install -p -m 644 pcap/*.pcap %{buildroot}%{_datadir}/%{name}/pcap


%check
%if 0%{?fedora}
make check
%endif


%files
%license LICENSE.txt
%doc README.md THANKS
%caps(cap_net_raw=ep) %{_bindir}/%{name}
%{_datadir}/%{name}


%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 3.6.0-8
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 16 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.6.0-5
- Migrate to modern openssl.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Peter Lemenkov <lemenkov@gmail.com> - 3.6.0-2
- Grant capability for opening a raw socket (rhbz #1794953)

* Mon Dec 16 2019 Peter Lemenkov <lemenkov@gmail.com> - 3.6.0-1
- Ver. 3.6.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 25 2019 Peter Lemenkov <lemenkov@gmail.com> - 3.5.2-1
- Ver. 3.5.2

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Peter Lemenkov <lemenkov@gmail.com> - 3.5.1-5
- Fix FTBFS on F-28 and higher

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar  8 2017 Peter Lemenkov <lemenkov@gmail.com> - 3.5.1-1
- Ver. 3.5.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Feb 23 2016 Peter Lemenkov <lemenkov@gmail.com> - 3.5.0-3
- Fix qop parameter in auth Digest.

* Sat Feb 13 2016 Peter Lemenkov <lemenkov@gmail.com> - 3.5.0-2
- Disable tests on EPEL7 (too old gtest/gmock)

* Sat Feb 13 2016 Peter Lemenkov <lemenkov@gmail.com> - 3.5.0-1
- Ver. 3.5.0
- Fixed FTBFS in EPEL7 for AArch64 (see rhbz#1306382).

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 23 2015 Peter Lemenkov <lemenkov@gmail.com> - 3.4.1-1
- Ver. 3.4.1
- Dropped upstreamed patch
- Removed compatibility with outdated distributions

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.3-7
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 30 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 3.3-5
- Fix FTBFS with -Werror=format-security (#1037326, #1107309)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Peter Lemenkov <lemenkov@gmail.com> - 3.3-2
- Fix for autoreconf on EL5

* Fri Feb 15 2013 Peter Lemenkov <lemenkov@gmail.com> - 3.3-1
- Ver. 3.3

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-5
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 03 2011 Peter Lemenkov <lemenkov@gmail.com> - 3.2-3
- Fix authorization
- Cherry-picked two patches from svn trunk

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 27 2011 Peter Lemenkov <lemenkov@gmail.com> 3.2-1
- Ver 3.2
- Patches rebased

* Fri Jan 29 2010 Peter Lemenkov <lemenkov@gmail.com> 3.1-9.svn586
- Fix for RHBZ #559620
- Reorganized patches.

* Mon Jan 25 2010 Peter Lemenkov <lemenkov@gmail.com> 3.1-8.svn586
- Update to svn ver. 586 (fixes lots of small but nasty issues)
- Removed patch1, patch3

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 3.1-7
- rebuilt with new openssl

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jun 18 2009 Peter Lemenkov <lemenkov@gmail.com> 3.1-5
- Fixed issue with 5-digit port numbers

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 17 2009 Tomas Mraz <tmraz@redhat.com> 3.1-3
- rebuild with new openssl

* Sun Jul  6 2008 Peter Lemenkov <lemenkov@gmail.com> 3.1-2
- CVE-2008-2085

* Wed Apr 30 2008 Peter Lemenkov <lemenkov@gmail.com> 3.1-1
- Ver 3.1

* Thu Feb 21 2008  Peter Lemenkov <lemenkov@gmail.com> 3.0-3
- Fixed build with GCC 4.3
- No need to remove .svn leftover

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 3.0-2
- Autorebuild for GCC 4.3

* Thu Jan 10 2008 Peter Lemenkov <lemenkov@gmail.com> 3.0-1
- Version 3.0
- Updated license field
- Preserved timestamp for *.pcap files

* Wed Dec 05 2007 Release Engineering <rel-eng at fedoraproject dot org> - 2.0.1-5
- Rebuild for deps

* Fri Sep  7 2007 Peter Lemenkov <lemenkov@gmail.com> 2.0.1-4
- Removed .svn entries (close BZ #282431)
- Added macro for builds for EL-4

* Wed Jul 25 2007 Peter Lemenkov <lemenkov@gmail.com> 2.0.1-3.2
- finally added correct BR for EL-4

* Wed Jul 25 2007 Peter Lemenkov <lemenkov@gmail.com> 2.0.1-3.1
- rebuild

* Wed Jul 25 2007 Peter Lemenkov <lemenkov@gmail.com> 2.0.1-3
- Added tcpdump instead of libpcap as BR for EL-4

* Sun Jun 10 2007 Peter Lemenkov <lemenkov@gmail.com> 2.0.1-2
- rebuild

* Wed Jun  6 2007 Peter Lemenkov <lemenkov@gmail.com> 2.0.1-1
- Version 2.0.1

* Sat May 12 2007 Peter Lemenkov <lemenkov@gmail.com> 2.0-1
- Version 2.0

* Wed Jan 17 2007 Peter Lemenkov <lemenkov@gmail.com> 1.1-0.rc8
- small cleanup

* Thu Dec 21 2006 Peter Lemenkov <lemenkov@gmail.com> 1.1-0.rc8
- Version 1.1rc8

* Wed Nov 22 2006 Peter Lemenkov <lemenkov@gmail.com> 1.1rc6-0
- Initial build for FE

