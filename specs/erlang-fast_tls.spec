%global srcname fast_tls
%global p1_utils_ver 1.0.28

Name: erlang-%{srcname}
Version: 1.1.25
Release: %autorelease
License: Apache-2.0
Summary: TLS / SSL native driver for Erlang / Elixir
URL: https://github.com/processone/%{srcname}/
VCS: git:%{url}.git
Source0: %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
# Set the default cipher list to PROFILE=SYSTEM.
# https://fedoraproject.org/wiki/Packaging:CryptoPolicies
Patch1: erlang-fast_tls-0001-Use-the-system-ciphers-by-default.patch
Patch2: erlang-fast_tls-0002-Disable-Rebar3-plugins.patch
Provides:  erlang-p1_tls = %{version}-%{release}
Obsoletes: erlang-p1_tls < 1.0.1
BuildRequires: gcc
BuildRequires: erlang-p1_utils >= %{p1_utils_ver}
BuildRequires: erlang-rebar3
BuildRequires: openssl-devel
Requires: erlang-p1_utils >= %{p1_utils_ver}


%description
TLS / SSL native driver for Erlang / Elixir. This is used by ejabberd.


%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%{erlang3_compile}

# FIXME we don't have a port compiler plugin for rebar3 yet
mkdir -p priv/lib
gcc c_src/fast_tls.c	$CFLAGS -fPIC -c -I%{_libdir}/erlang/usr/include -o c_src/fast_tls.o
gcc c_src/ioqueue.c	$CFLAGS -fPIC -c -I%{_libdir}/erlang/usr/include -o c_src/ioqueue.o
gcc c_src/p1_sha.c	$CFLAGS -fPIC -c -I%{_libdir}/erlang/usr/include -o c_src/p1_sha.o
gcc c_src/fast_tls.o c_src/ioqueue.o $LDFLAGS -shared -L%{_libdir}/erlang/usr/lib -lei -L%{_libdir} -lssl -lcrypto -o priv/lib/fast_tls.so
gcc c_src/p1_sha.o $LDFLAGS -shared -L%{_libdir}/erlang/usr/lib -lei -L%{_libdir} -lssl -lcrypto -o priv/lib/p1_sha.so


%install
%{erlang3_install}

install -d $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/priv/lib
install -pm755 priv/lib/* $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/priv/lib/


%check
%{erlang3_test}


%files
%license LICENSE.txt
%doc CHANGELOG.md
%doc README.md
%{erlang_appdir}


%changelog
%autochangelog
