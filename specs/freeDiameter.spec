Name:           freeDiameter
Version:        1.6.0
Release:        %autorelease
Summary:        A Diameter protocol open implementation
License:        BSD-3-Clause
URL:            https://github.com/freeDiameter/freeDiameter
Source0:        https://github.com/%{name}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gnutls-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libidn2-devel
BuildRequires:  libpq-devel
BuildRequires:  lksctp-tools-devel

%description
freeDiameter is an open source Diameter protocol implementation. It provides an
extensible platform for deploying a Diameter network for your Authentication,
Authorization and Accounting needs.

%package devel
Summary:        Library for freeDiameter package
Requires:       %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains the shared library
for %{name} package.

%prep
%autosetup
# Remove empty test config files (0 bytes upstream)
rm -f doc/single_host/test_app1.conf doc/single_host/test_app2.conf

%build
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_BUILD_TYPE=None . -Wno-dev
%cmake_build

# testcnx requires a running peer, testsctp requires SCTP kernel support;
# both fail in the build environment
%check
# testostr's expected hash is endianness-dependent; fails on s390x
%ifnarch s390x
%ctest -E 'testcnx|testsctp'
%else
%ctest -E 'testcnx|testsctp|testostr'
%endif

%install
%cmake_install

%ldconfig_scriptlets

%files
%doc doc
%{_bindir}/freeDiameterd
%{_bindir}/%{name}d-%{version}
%{_libdir}/libfdcore.so.*
%{_libdir}/libfdproto.so.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/%{name}/
%{_libdir}/libfdcore.so
%{_libdir}/libfdproto.so

%changelog
%autochangelog
