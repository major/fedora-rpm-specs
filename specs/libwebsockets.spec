%global _default_patch_fuzz 2
# Absent libuv-devel on s390x at RHEL/CentOS 8
%if 0%{?rhel} && 0%{?rhel} == 8 && "%{_arch}" == "s390x"
%bcond_with libuv
%else
%bcond_without libuv
%endif

Name:           libwebsockets
Version:        4.3.3
Release:        3%{?dist}
Summary:        Lightweight C library for Websockets

# base64-decode.c and ssl-http2.c is under MIT license with FPC exception.
# sha1-hollerbach is under BSD
# https://fedorahosted.org/fpc/ticket/546
# Test suite is licensed as Public domain (CC-zero)
License:        LicenseRef-Callaway-LGPLv2 AND LicenseRef-Callaway-Public-Domain AND LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT AND Zlib
URL:            http://libwebsockets.org
Source0:        https://github.com/warmcat/libwebsockets/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-g++
BuildRequires:  libev-devel
%if %{with libuv}
BuildRequires:  libuv-devel
%endif
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel

Provides:       bundled(sha1-hollerbach)
Provides:       bundled(base64-decode)
Provides:       bundled(ssl-http2)

%description
This is the libwebsockets C library for lightweight websocket clients and
servers.

%package devel
Summary:        Headers for developing programs that will use %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%if %{with libuv}
Requires:       libuv-devel
%endif
Requires:       libev-devel
Requires:       openssl-devel

%description devel
This package contains the header files needed for developing
%{name} applications.

%prep
%autosetup -p1

%build
mkdir -p build
cd build

%cmake \
    -D LWS_WITH_HTTP2=ON \
    -D LWS_IPV6=ON \
    -D LWS_WITH_ZIP_FOPS=ON \
    -D LWS_WITH_SOCKS5=ON \
    -D LWS_WITH_RANGES=ON \
    -D LWS_WITH_ACME=ON \
%if %{with libuv}
    -D LWS_WITH_LIBUV=ON \
%endif
    -D LWS_BUILD_HASH=no_hash \
    -D LWS_LINK_TESTAPPS_DYNAMIC=ON \
    -D LWS_UNIX_SOCK=ON \
    -D LWS_USE_BUNDLED_ZLIB=OFF \
    -D LWS_WITH_DISKCACHE=ON \
    -D LWS_WITH_EXTERNAL_POLL=ON \
    -D LWS_WITH_FTS=ON \
    -D LWS_WITH_HTTP_PROXY=ON \
    -D LWS_WITH_LIBEV=ON \
    -D LWS_WITH_LIBEVENT=OFF \
    -D LWS_WITH_LWSAC=ON \
    -D LWS_WITH_STATIC=OFF \
    -D LWS_WITH_THREADPOOL=ON \
    -D LWS_WITHOUT_BUILTIN_GETIFADDRS=ON \
    -D LWS_WITHOUT_BUILTIN_SHA1=ON \
    -D LWS_WITHOUT_CLIENT=OFF \
    -D LWS_WITHOUT_SERVER=OFF \
    -D LWS_WITHOUT_TEST_CLIENT=ON \
    -D LWS_WITHOUT_TEST_PING=ON \
    -D LWS_WITHOUT_TEST_SERVER_EXTPOLL=ON \
    -D LWS_WITHOUT_TEST_SERVER=ON \
    -D LWS_WITHOUT_TESTAPPS=ON \
    ..

%cmake_build

%install
cd build
%cmake_install
find %{buildroot} -name '*.la' -delete
find %{buildroot} -name '*.a' -delete
find %{buildroot} -name '*.cmake' -delete
find %{buildroot} -name '*_static.pc' -delete

%ldconfig_scriptlets

%files
%license LICENSE
%doc README.md changelog
%{_libdir}/%{name}.so.19
%{_libdir}/%{name}-evlib_ev.so
%if %{with libuv}
%{_libdir}/%{name}-evlib_uv.so
%endif

%files devel
%license LICENSE
%doc READMEs/README.coding.md READMEs/ changelog
%{_includedir}/*.h
%{_includedir}/%{name}/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Oct 31 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 4.3.3-2
- Build with external polling support

* Wed Sep 18 2024 Fabian Affolter <mail@fabian-affolter.ch> - 4.3.3-1
- Update to latest upstream release (closes rhbz#2250868)

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 4.3.2-9
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Aug 18 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 4.3.2-5
- Upstream patches for OpenSSLv3

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Sep 26 2022 Milivoje Legenovic <m.legenovic@gmail.com> - 4.3.2-2
- Move two plugin *.so files from devel to libs package

* Wed Aug 17 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 4.3.2-1
- Update to 4.3.2

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Feb 20 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 4.3.1-1
- Update to 4.3.1

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 4.2.2-2
- Rebuilt with OpenSSL 3.0.0

* Wed Sep 01 2021 Fabian Affolter <mail@fabian-affolter.ch> - 4.2.2-1
- Update to latest upstream release 4.2.2 (closes rhbz#1998770)

* Wed Aug 25 2021 Fabian Affolter <mail@fabian-affolter.ch> - 4.2.0-1
- Update to latest upstream release 4.2.0 (rhbz#1950346)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 4.1.6-1
- Update to latest upstream release 4.1.6 (#1903395)

* Thu Oct 29 2020 Fabian Affolter <mail@fabian-affolter.ch> - 4.1.4-1
- Update to latest upstream release 4.1.4 (#1887452)

* Mon Oct 12 2020 Fabian Affolter <mail@fabian-affolter.ch> - 4.1.3-1
- Update to latest upstream release 4.1.3 (#1887452)

* Wed Sep 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 4.1.2-1
- Update to latest upstream release 4.1.2 (#1855481)

* Wed Sep 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 4.1.1-1
- Update to latest upstream release 4.1.1 (#1855481)

* Mon Sep 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 4.1.0-1
- Update to latest upstream release 4.1.0 (#1855481)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.20-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 15 2020 Fabian Affolter <mail@fabian-affolter.ch> - 4.0.20-1
- Update to latest upstream release 4.0.20 (#1855481)

* Sun Jun 21 2020 Fabian Affolter <mail@fabian-affolter.ch> - 4.0.19-1
- Update to latest upstream release 4.0.19 (#1829592)

* Tue Jun 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 4.0.16-1
- Update to latest upstream release 4.0.16 (#1829592)

* Fri Jun 05 2020 Fabian Affolter <mail@fabian-affolter.ch> - 4.0.15-1
- Update to latest upstream release 4.0.15 (#1829592)

* Sun May 24 2020 Fabian Affolter <mail@fabian-affolter.ch> - 4.0.12-1
- Update to latest upstream release 4.0.12 (#1829592)

* Mon May 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 4.0.10-1
- Update to latest upstream release 4.0.10 (#1829592)

* Fri May 01 2020 Fabian Affolter <mail@fabian-affolter.ch> - 4.0.3-1
- Update to latest upstream release 4.0.2 (#1829592)

* Thu Apr 30 2020 Fabian Affolter <mail@fabian-affolter.ch> - 4.0.2-1
- Update to latest upstream release 4.0.2 (#1829592)

* Sat Apr 18 2020 Robert Scheck <robert@fedoraproject.org> - 4.0.1-2
- Handle absent libuv-devel on s390x architecture at RHEL/CentOS 8

* Tue Mar 10 2020 Fabian Affolter <mail@fabian-affolter.ch> - 4.0.1-1
- Update to latest upstream release 4.0.1 (#1811270)

* Mon Mar 09 2020 Fabian Affolter <mail@fabian-affolter.ch> - 4.0.0-1
- Update to latest upstream release 4.0.0 (#1811270)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.2.2-1
- Update to latest upstream release 3.2.2 (#1792585)

* Thu Dec 19 2019 Peter Robinson <pbrobinson@fedoraproject.org> 3.2.1-1
- Update to 3.2.1

* Mon Sep  2 2019 Peter Robinson <pbrobinson@fedoraproject.org> 3.2.0-1
- Update to 3.2.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb  9 2019 Peter Robinson <pbrobinson@fedoraproject.org> 3.1.0-2
- devel requires libev-devel

* Sat Feb  9 2019 Peter Robinson <pbrobinson@fedoraproject.org> 3.1.0-1
- Update to 3.1.0
- Enable new features/functionality

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan  7 2019 Peter Robinson <pbrobinson@fedoraproject.org> 3.0.1-2
- Add libuv-devel Requires to devel package

* Tue Dec 18 2018 Fabian Affolter <mail@fabian-affolter.ch> - 3.0.1-1
- Update to latest upstream release 3.0.1 (#1604687)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 07 2018 Fabian Affolter <mail@fabian-affolter.ch> - 3.0.0-1
- Update to latest upstream release 3.0.0 (#1575605)

* Thu Mar 15 2018 Fabian Affolter <mail@fabian-affolter.ch> - 2.4.2-1
- Update to latest upstream release 2.4.2 (#1504377)

* Fri Feb 16 2018 Fabian Affolter <mail@fabian-affolter.ch> - 2.4.1-1
- Update to latest upstream release 2.4.1 (#1504377)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Oct 20 2017 Fabian Affolter <mail@fabian-affolter.ch> - 2.4.0-1
- Update to latest upstream release 2.4.0 (#1504377)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Sat Jul 29 2017 Fabian Affolter <mail@fabian-affolter.ch> - 2.3.0-1
- Update to latest upstream release 2.3.0 (#1472509)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 11 2017 Fabian Affolter <mail@fabian-affolter.ch> - 2.2.0-1
- Update to latest upstream release 2.2.1 (#1437272)

* Sat Mar 25 2017 Fabian Affolter <mail@fabian-affolter.ch> - 2.2.0-1
- Update to latest upstream release 2.2.0 (#1422477)

* Tue Mar 14 2017 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.1-1
- Update to latest upstream release 2.1.1 (#1422477)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov 17 2016 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.0-2
- Move tests (#1390538)

* Thu Nov 17 2016 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.0-1
- Update to latest upstream release 2.1.0 (#1376257)

* Mon Oct 31 2016 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.3-1
- Update to latest upstream release 2.0.3

* Wed Aug 03 2016 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.2-1
- Update to latest upstream release 2.0.2 (#1358988)

* Sat Apr 16 2016 Fabian Affolter <mail@fabian-affolter.ch> - 1.7.5-1
- Update licenses
- Update to latest upstream release 1.7.5

* Tue Mar 22 2016 Fabian Affolter <mail@fabian-affolter.ch> - 1.7.4-1
- Update licenses
- Update to latest upstream release 1.7.4

* Sun Jan 24 2016 Fabian Affolter <mail@fabian-affolter.ch> - 1.6.1-2
- Update to latest upstream release 1.6.1

* Fri Jan 22 2016 Fabian Affolter <mail@fabian-affolter.ch> - 1.5.1-2
- Update spec file
- Update to latest upstream release 1.5.1

* Wed Mar 04 2015 Fabian Affolter <mail@fabian-affolter.ch> - 1.3-2
- Introduce license tag
- Including .cmake files in dev package
- Switch to github source

* Wed Mar 04 2015 Fabian Affolter <mail@fabian-affolter.ch> - 1.3-1
- Initial package for Fedora
