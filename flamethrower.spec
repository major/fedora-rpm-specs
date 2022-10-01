%undefine __cmake_in_source_build
# Optional DNS over HTTP support
%bcond_without doh

Name:		flamethrower
Version:	0.11.0
Release:	13%{?dist}
Summary:	A DNS performance and functional testing utility

License:	Apache-2.0
URL:		https://github.com/DNS-OARC/flamethrower
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://github.com/DNS-OARC/flamethrower/pull/74
Patch1:		flamethrower-0.11-catch2.patch
# https://github.com/DNS-OARC/flamethrower/pull/75
Patch2:		flamethrower-0.11-http-parser.patch
# https://github.com/DNS-OARC/flamethrower/pull/77
Patch3:		flamethrower-0.11-3rd-json.patch
# https://github.com/DNS-OARC/flamethrower/pull/85
Patch4:		flamethrower-0.11-3rd-base64.patch
# https://github.com/DNS-OARC/flamethrower/pull/87
Patch5:		flamethrower-0.11-uvw.patch
Patch6:		flamethrower-0.11-uvw-compat.patch
# https://github.com/DNS-OARC/flamethrower/pull/88
Patch7:		flamethrower-0.11-gcc12.patch

BuildRequires:	gcc-c++, make
BuildRequires:	cmake
BuildRequires:	libuv-devel
BuildRequires:	ldns-devel
BuildRequires:	gnutls-devel
BuildRequires:	catch-devel
BuildRequires:	pandoc
BuildRequires:	http-parser-devel
BuildRequires:	json-devel
BuildRequires:  docopt-cpp-devel
BuildRequires:  uvw-devel
%if %{with doh}
BuildRequires:	libnghttp2-devel
%endif
# 3rd/base64url from https://renenyffenegger.ch/notes/development/Base64/Encoding-and-decoding-base-64-with-cpp/index
# also https://github.com/ReneNyffenegger/cpp-base64
Provides: bundled(cpp-base64)

%description
Flamethrower is a small, fast, configurable tool for
functional testing, benchmarking, and stress testing
DNS servers and networks. It supports IPv4, IPv6, UDP and TCP,
and has a modular system for generating queries used in the tests.

It was built as an alternative to dnsperf, and many
of the command line options are compatible.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%cmake -DCMAKE_SKIP_BUILD_RPATH=TRUE \
	-DUSE_HTTP_PARSER=ON \
%if %{with doh}
-DDOH_ENABLE=ON \
%endif

%cmake_build


%install
%cmake_install
install -m 0644 -pD man/flame.1 ${RPM_BUILD_ROOT}%{_mandir}/man1/flame.1

%check
%ctest

%files
%doc README.md
%license LICENSE
%{_bindir}/flame
%{_libdir}/libflamecore.so
%{_mandir}/man1/flame.1*


%changelog
* Fri Sep 30 2022 Petr Menšík <pemensik@redhat.com> - 0.11.0-13
- Update License tag to SPDX identifier

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Petr Menšík <pemensik@redhat.com> - 0.11.0-11
- Build on gcc 12 again

* Thu Jan 20 2022 Petr Menšík <pemensik@redhat.com> - 0.11.0-10
- Use uvw-devel package

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Nov 24 2021 Petr Menšík <pemensik@redhat.com> - 0.11.0-8
- Use docopt-cpp package

* Sat Sep 18 2021 Petr Menšík <pemensik@redhat.com> - 0.11.0-7
- Make the package compilable on EPEL8

* Thu Aug 05 2021 Petr Menšík <pemensik@redhat.com> - 0.11.0-6
- Use http_parser instead of bundled url_parser

* Mon Aug 02 2021 Petr Menšík <pemensik@redhat.com> - 0.11.0-5
- Build with latest catch library (#1987476)
- Declare bundled libraries in package

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 19 2020 Adam Williamson <awilliam@redhat.com> - 0.11.0-2
- Rebuild for libldns soname bump

* Tue Sep 22 2020 Petr Menšík <pemensik@redhat.com> - 0.11.0-1
- Update to 0.11.0

* Fri Aug 07 2020 Petr Menšík <pemensik@redhat.com> - 0.10.2-4
- Update spec to recent cmake macros, fixes rawhide (#1863562)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 02 2020 Petr Menšík <pemensik@redhat.com> - 0.10.2-1
- Update to 0.10.2

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 07 2019 Petr Menšík <pemensik@redhat.com> - 0.10-3
- Remove explicit library requires

* Wed Oct 02 2019 Petr Menšík <pemensik@redhat.com> - 0.10-2
- Use make install, improve descriptions
- Correct permissions of manual
- Use bindir

* Tue Sep 10 2019 Petr Menšík <pemensik@redhat.com> - 0.10-1
- Initial release


