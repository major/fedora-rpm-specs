%undefine __cmake_in_source_build
# Optional DNS over HTTP support
%bcond_without doh
# Simple test requiring online connection
%bcond_with online

Name:		flamethrower
Version:	0.11.0
Release:	%autorelease
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
# https://github.com/DNS-OARC/flamethrower/pull/94
Patch8:		flamethrower-0.12-httpsession.patch

BuildRequires:	gcc-c++, make
BuildRequires:	cmake
BuildRequires:	libuv-devel
BuildRequires:	ldns-devel
BuildRequires:	gnutls-devel
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
export LD_LIBRARY_PATH="${RPM_BUILD_ROOT}%{_libdir}"
${RPM_BUILD_ROOT}%{_bindir}/flame --help
%if %{with online}
	COMMON="-Q 30 -g randomlabel -l 3 -r test dns.google"
	PROTOS="udp tcp dot"
	%if %{with doh}
		PROTOS+=" doh"
	%endif
	for PROTO in $PROTOS
	do
		${RPM_BUILD_ROOT}%{_bindir}/flame -P $PROTO $COMMON
	done
%endif

%files
%doc README.md
%license LICENSE
%{_bindir}/flame
%{_libdir}/libflamecore.so
%{_mandir}/man1/flame.1*


%changelog
%autochangelog
