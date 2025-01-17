Summary:        Generic library for real-time communications
Name:           libre
Version:        3.19.0
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            https://github.com/baresip/re
Source0:        https://github.com/baresip/re/archive/v%{version}/re-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
%if 0%{?fedora} || 0%{?rhel} >= 9
BuildRequires:  openssl-devel
%else
# https://github.com/baresip/re/pull/1015
BuildRequires:  openssl3-devel
%endif
BuildRequires:  zlib-devel
# Cover multiple third party repositories
Obsoletes:      libre0 < 0.6.1-2
Provides:       libre0 = %{version}-%{release}
Provides:       libre0%{?_isa} = %{version}-%{release}
Obsoletes:      re < 0.6.1-2
Provides:       re = %{version}-%{release}
Provides:       re%{?_isa} = %{version}-%{release}
# librem was merged into libre 3.0.0
Obsoletes:      librem < 3.0.0-1
Provides:       librem = %{version}-%{release}
Provides:       librem%{?_isa} = %{version}-%{release}

%description
Libre is a generic library for real-time communications with async I/O
support. Features are a SIP stack (RFC 3261), SDP, RTP and RTCP, SRTP and
SRTCP (Secure RTP), DNS client, STUN/TURN/ICE stack, BFCP, HTTP stack with
client/server, Websockets, Jitter buffer, async I/O (poll, epoll, select,
kqueue), UDP/TCP/TLS/DTLS transport, JSON parser and Real Time Messaging
Protocol (RTMP).

%package devel
Summary:        Development files for the re library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
%if 0%{?fedora} || 0%{?rhel} >= 9
Requires:       openssl-devel
%else
Requires:       openssl3-devel
%endif
Requires:       zlib-devel
# Cover multiple third party repositories
Obsoletes:      libre0-devel < 0.6.1-2
Provides:       libre0-devel = %{version}-%{release}
Provides:       libre0-devel%{?_isa} = %{version}-%{release}
Obsoletes:      re-devel < 0.6.1-2
Provides:       re-devel = %{version}-%{release}
Provides:       re-devel%{?_isa} = %{version}-%{release}
# librem was merged into libre 3.0.0
Obsoletes:      librem-devel < 3.0.0-1
Provides:       librem-devel = %{version}-%{release}
Provides:       librem-devel%{?_isa} = %{version}-%{release}

%description devel
The libre-devel package includes header files and libraries necessary for
developing programs which use the re C library.

%prep
%autosetup -p1 -n re-%{version}

%build
%cmake \
%if 0%{?rhel} == 8
  -DOPENSSL_ROOT_DIR:PATH="%{_includedir}/openssl3;%{_libdir}/openssl3"
%endif

%cmake_build

%install
%cmake_install

# Remove static library
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}.a

%check
%cmake_build --target retest
%{__cmake_builddir}/test/retest -d test/data/ -v -r

%ldconfig_scriptlets

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_libdir}/%{name}.so.29*

%files devel
%{_libdir}/%{name}.so
%{_includedir}/re/
%{_libdir}/cmake/%{name}/
%{_libdir}/cmake/re/
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Thu Jan 16 2025 Robert Scheck <robert@fedoraproject.org> 3.19.0-1
- Upgrade to 3.19.0 (#2338170)

* Sun Dec 22 2024 Robert Scheck <robert@fedoraproject.org> 3.18.0-2
- Add upstream patch for address support via rtnetlink API

* Thu Dec 12 2024 Robert Scheck <robert@fedoraproject.org> 3.18.0-1
- Upgrade to 3.18.0 (#2331646)

* Thu Nov 07 2024 Robert Scheck <robert@fedoraproject.org> 3.17.0-1
- Upgrade to 3.17.0 (#2324466)

* Thu Oct 03 2024 Robert Scheck <robert@fedoraproject.org> 3.16.0-1
- Upgrade to 3.16.0 (#2316094)

* Sat Sep 14 2024 Robert Scheck <robert@fedoraproject.org> 3.15.0-1
- Upgrade to 3.15.0 (#2309407)

* Tue Jul 23 2024 Robert Scheck <robert@fedoraproject.org> 3.14.0-1
- Upgrade to 3.14.0 (#2299504)

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jun 27 2024 Robert Scheck <robert@fedoraproject.org> 3.13.0-1
- Upgrade to 3.13.0 (#2293041)

* Mon May 20 2024 Robert Scheck <robert@fedoraproject.org> 3.12.0-1
- Upgrade to 3.12.0

* Thu Apr 11 2024 Robert Scheck <robert@fedoraproject.org> 3.11.0-1
- Upgrade to 3.11.0 (#2274320)

* Sun Mar 10 2024 Robert Scheck <robert@fedoraproject.org> 3.10.0-1
- Upgrade to 3.10.0 (#2268236)

* Thu Feb 01 2024 Robert Scheck <robert@fedoraproject.org> 3.9.0-1
- Upgrade to 3.9.0 (#2262287)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Dec 28 2023 Robert Scheck <robert@fedoraproject.org> 3.8.0-1
- Upgrade to 3.8.0 (#2256017)

* Sun Nov 26 2023 Robert Scheck <robert@fedoraproject.org> 3.7.0-1
- Upgrade to 3.7.0 (#2251345)

* Tue Nov 07 2023 Robert Scheck <robert@fedoraproject.org> 3.6.2-1
- Upgrade to 3.6.2 (#2248185)

* Sun Nov 05 2023 Robert Scheck <robert@fedoraproject.org> 3.6.1-1
- Upgrade to 3.6.1 (#2247959)

* Sun Oct 29 2023 Robert Scheck <robert@fedoraproject.org> 3.6.0-1
- Upgrade to 3.6.0 (#2244979)

* Sun Sep 17 2023 Robert Scheck <robert@fedoraproject.org> 3.5.1-1
- Upgrade to 3.5.1 (#2238874)

* Sat Aug 12 2023 Robert Scheck <robert@fedoraproject.org> 3.4.0-1
- Upgrade to 3.4.0 (#2231129)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 07 2023 Robert Scheck <robert@fedoraproject.org> 3.3.0-1
- Upgrade to 3.3.0 (#2220894)

* Wed May 31 2023 Robert Scheck <robert@fedoraproject.org> 3.2.0-1
- Upgrade to 3.2.0 (#2211344)

* Thu Apr 27 2023 Robert Scheck <robert@fedoraproject.org> 3.1.0-1
- Upgrade to 3.1.0 (#2190309)

* Mon Mar 20 2023 Robert Scheck <robert@fedoraproject.org> 3.0.0-1
- Upgrade to 3.0.0 (#2179923)

* Fri Feb 17 2023 Robert Scheck <robert@fedoraproject.org> 2.12.0-1
- Upgrade to 2.12.0 (#2170480)

* Thu Feb 02 2023 Florian Weimer <fweimer@redhat.com> - 2.11.0-3
- Fix C99 compatibility issues

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jan 14 2023 Robert Scheck <robert@fedoraproject.org> 2.11.0-1
- Upgrade to 2.11.0 (#2160220)

* Wed Dec 07 2022 Robert Scheck <robert@fedoraproject.org> 2.10.0-1
- Upgrade to 2.10.0 (#2151699)

* Tue Nov 01 2022 Robert Scheck <robert@fedoraproject.org> 2.9.0-1
- Upgrade to 2.9.0 (#2139163)

* Sat Oct 01 2022 Robert Scheck <robert@fedoraproject.org> 2.8.0-1
- Upgrade to 2.8.0 (#2131446)

* Thu Sep 01 2022 Robert Scheck <robert@fedoraproject.org> 2.7.0-1
- Upgrade to 2.7.0

* Wed Aug 03 2022 Robert Scheck <robert@fedoraproject.org> 2.6.1-1
- Upgrade to 2.6.1 (#2114898)

* Mon Aug 01 2022 Robert Scheck <robert@fedoraproject.org> 2.6.0-1
- Upgrade to 2.6.0 (#2112887)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jul 02 2022 Robert Scheck <robert@fedoraproject.org> 2.5.0-1
- Upgrade to 2.5.0 (#2103279)

* Wed Jun 01 2022 Robert Scheck <robert@fedoraproject.org> 2.4.0-1
- Upgrade to 2.4.0 (#2092574)

* Mon May 02 2022 Robert Scheck <robert@fedoraproject.org> 2.3.0-1
- Upgrade to 2.3.0 (#2080807)

* Sat Apr 09 2022 Robert Scheck <robert@fedoraproject.org> 2.2.2-1
- Upgrade to 2.2.2 (#2073697)

* Sat Apr 02 2022 Robert Scheck <robert@fedoraproject.org> 2.2.1-1
- Upgrade to 2.2.1 (#2071123)

* Mon Mar 28 2022 Robert Scheck <robert@fedoraproject.org> 2.2.0-1
- Upgrade to 2.2.0 (#2069304)

* Sun Mar 13 2022 Robert Scheck <robert@fedoraproject.org> 2.1.1-1
- Upgrade to 2.1.1 (#2063340)

* Fri Mar 11 2022 Robert Scheck <robert@fedoraproject.org> 2.1.0-1
- Upgrade to 2.1.0 (#2063340)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 2.0.1-3
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Apr 22 2021 Robert Scheck <robert@fedoraproject.org> 2.0.1-1
- Upgrade to 2.0.1 (#1952270)

* Sat Apr 10 2021 Robert Scheck <robert@fedoraproject.org> 2.0.0-1
- Upgrade to 2.0.0 (#1948215)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 12 2020 Robert Scheck <robert@fedoraproject.org> 1.1.0-2
- Removed patch accepting 401 to re-register without stale=true

* Sat Oct 10 2020 Robert Scheck <robert@fedoraproject.org> 1.1.0-1
- Upgrade to 1.1.0 (#1887081)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 28 2020 Robert Scheck <robert@fedoraproject.org> 0.6.1-2
- Add patch to accept 401 to re-register without stale=true
- Changes to match the Fedora Packaging Guidelines (#1843264 #c1)

* Thu May 28 2020 Robert Scheck <robert@fedoraproject.org> 0.6.1-1
- Upgrade to 0.6.1 (#1843264)
- Initial spec file for Fedora and Red Hat Enterprise Linux
