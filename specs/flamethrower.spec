%undefine __cmake_in_source_build
# Optional DNS over HTTP support
%bcond_without doh
# Simple test requiring online connection
%bcond_with online
# http-parser upstream is dead. Use bundled part of it until replaced.
# TODO: propose uri-parser or ada-url to upstream as a replacement
%bcond_with http_parser

Name:		flamethrower
Version:	0.12.0
Release:	%autorelease
Summary:	A DNS performance and functional testing utility

License:	Apache-2.0
URL:		https://github.com/DNS-OARC/flamethrower
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://github.com/DNS-OARC/flamethrower/pull/112
Patch1:		flamethrower-0.12.0-unbundle-meson.patch

BuildRequires:	gcc-c++
BuildRequires:	cmake
BuildRequires:	meson
BuildRequires:	ninja-build
BuildRequires:	pkgconfig(libuv)
BuildRequires:	pkgconfig(ldns)
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	cmake(nlohmann_json)
BuildRequires:	docopt-cpp-devel
# cmake(uvw) does not have version
BuildRequires:	uvw-devel >= 3.4
BuildRequires:	cmake(httplib)
BuildRequires:	pandoc
%if %{with doh}
BuildRequires:	pkgconfig(libnghttp2)
%endif
# Not used again, http-parser is missing dependencies
%if %{with http_parser}
BuildRequires:	http-parser-devel
%endif

# cpp-httplib upstream no longer supports 32 bits
# https://github.com/yhirose/cpp-httplib/issues/2148
ExcludeArch: %{ix86}

# 3rd/base64url from https://renenyffenegger.ch/notes/development/Base64/Encoding-and-decoding-base-64-with-cpp/index
# also https://github.com/ReneNyffenegger/cpp-base64
Provides: bundled(cpp-base64)

%if %{without http_parser}
# 3rd/url-parser is a part of http-parser
# https://github.com/nodejs/http-parser
Provides: bundled(http-parser) = 2.9.1
Provides: bundled(url-parser) = 2.9.1
%endif

%description
Flamethrower is a small, fast, configurable tool for
functional testing, benchmarking, and stress testing
DNS servers and networks. It supports IPv4, IPv6, UDP and TCP,
and has a modular system for generating queries used in the tests.

It was built as an alternative to dnsperf, and many
of the command line options are compatible.

%prep
%autosetup -p1

# Remove bundled source we are able to use from the system
rm -rf 3rd/{json,docopt.cpp,uvw,cpp-httplib}

%build
%meson -Dbundles=false \
%if %{with doh}
  -Ddoh=true \
%endif
# end of meson

%meson_build


%install
%meson_install
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
%{_mandir}/man1/flame.1*


%changelog
%autochangelog
