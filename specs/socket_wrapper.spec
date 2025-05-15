Name:           socket_wrapper
Version:        1.5.0
Release:        %autorelease

License:        BSD-3-Clause
Summary:        A library passing all socket communications through Unix sockets
Url:            http://cwrap.org/

Source0:        https://ftp.samba.org/pub/cwrap/%{name}-%{version}.tar.gz
Source1:        https://ftp.samba.org/pub/cwrap/%{name}-%{version}.tar.gz.asc
Source2:        socket_wrapper.keyring

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libcmocka-devel >= 1.1.0

Recommends:     cmake
Recommends:     pkgconfig

%description
socket_wrapper aims to help client/server software development teams willing to
gain full functional test coverage. It makes it possible to run several
instances of the full software stack on the same machine and perform locally
functional testing of complex network configurations.

To use it set the following environment variables:

LD_PRELOAD=libsocket_wrapper.so
SOCKET_WRAPPER_DIR=/path/to/swrap_dir

This package doesn't have a devel package because this project is for
development/testing.

%package -n libsocket_wrapper_noop
Summary:        A library providing dummies for socket_wrapper

%description -n libsocket_wrapper_noop
Applications with the need to call socket_wrapper_enabled() should link against
-lsocket_wrapper_noop in order to resolve the symbol at link time.

%package -n libsocket_wrapper_noop-devel
Summary:        Development headers for libsocket_wrapper_noop
Requires:       libsocket_wrapper_noop = %{version}-%{release}

%description -n libsocket_wrapper_noop-devel
Development headers for applications with the need to call
socket_wrapper_enabled().

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%cmake \
    -DUNIT_TESTING=ON

%cmake_build

%install
%cmake_install

%ldconfig_scriptlets

%ldconfig_scriptlets -n libsocket_wrapper_noop

%check
%ctest

ls -l %{__cmake_builddir}/src/libsocket_wrapper.so
LD_PRELOAD=%{__cmake_builddir}/src/libsocket_wrapper.so bash -c '>/dev/null'

%files
%doc AUTHORS README.md CHANGELOG
%license LICENSE
%{_libdir}/libsocket_wrapper.so*
%dir %{_libdir}/cmake/socket_wrapper
%{_libdir}/cmake/socket_wrapper/socket_wrapper-config-version.cmake
%{_libdir}/cmake/socket_wrapper/socket_wrapper-config.cmake
%{_libdir}/pkgconfig/socket_wrapper.pc
%{_mandir}/man1/socket_wrapper.1*

%files -n libsocket_wrapper_noop
%{_libdir}/libsocket_wrapper_noop.so.*

%files -n libsocket_wrapper_noop-devel
%{_includedir}/socket_wrapper.h
%{_libdir}/libsocket_wrapper_noop.so
%{_libdir}/cmake/socket_wrapper/socket_wrapper_noop-config*.cmake
%{_libdir}/pkgconfig/socket_wrapper_noop.pc

%changelog
%autochangelog
