# Absent libuv-devel on s390x at RHEL/CentOS 8
%if 0%{?rhel} && 0%{?rhel} == 8 && "%{_arch}" == "s390x"
%bcond_with libuv
%else
%bcond_without libuv
%endif

Name:           libwebsockets
Version:        4.5.7
Release:        %autorelease
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
BuildRequires:  glib2-devel
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
CFLAGS="$RPM_OPT_FLAGS -Wno-discarded-qualifiers"
%cmake \
    -D LWS_WITH_HTTP2=ON \
    -D LWS_IPV6=ON \
    -D LWS_WITH_ZIP_FOPS=ON \
    -D LWS_WITH_SOCKS5=ON \
    -D LWS_WITH_RANGES=ON \
    -D LWS_WITH_ACME=ON \
    -D LWS_WITH_GLIB=ON \
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
    %nil

%cmake_build

%install
%cmake_install
find %{buildroot} -name '*.la' -delete
find %{buildroot} -name '*.a' -delete
find %{buildroot} -name '*_static.pc' -delete

%ldconfig_scriptlets

%files
%license LICENSE
%doc README.md changelog
%{_libdir}/%{name}.so.21
%{_libdir}/%{name}-evlib_ev.so
%{_libdir}/%{name}-evlib_glib.so
%if %{with libuv}
%{_libdir}/%{name}-evlib_uv.so
%endif

%files devel
%license LICENSE
%doc READMEs/README.coding.md READMEs/ changelog
%{_includedir}/*.h
%{_includedir}/%{name}/
%{_libdir}/%{name}.so
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
