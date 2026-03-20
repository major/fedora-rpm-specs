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
Patch: erlang-fast_tls-0001-Use-the-system-ciphers-by-default.patch
Provides:  erlang-p1_tls = %{version}-%{release}
Obsoletes: erlang-p1_tls < 1.0.1
BuildRequires: gcc
BuildRequires: erlang-p1_utils >= %{p1_utils_ver}
BuildRequires: erlang-rebar3
BuildRequires: erlang-rebar3-pc
BuildRequires: openssl-devel
Requires: erlang-p1_utils >= %{p1_utils_ver}

%description
TLS / SSL native driver for Erlang / Elixir. This is used by ejabberd.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%build
%{erlang3_compile}

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
