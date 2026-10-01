%global srcname esip
%global fast_tls_ver 1.1.26
%global p1_utils_ver 1.0.29
%global stun_ver 1.2.23

Name: erlang-%{srcname}
Version: 1.0.61
Release: %autorelease
License: Apache-2.0
Summary: ProcessOne SIP server component in Erlang
URL: https://github.com/processone/%{srcname}
VCS: git:%{url}.git
Source0: %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildRequires: erlang-fast_tls >= %{fast_tls_ver}
BuildRequires: erlang-p1_utils >= %{p1_utils_ver}
BuildRequires: erlang-rebar3-pc
BuildRequires: erlang-stun >= %{stun_ver}
BuildRequires: gcc
BuildSystem:   rebar3
Obsoletes: erlang-p1_sip < 1.0.2
Provides: erlang-p1_sip = %{version}-%{release}
Requires: erlang-fast_tls >= %{fast_tls_ver}
Requires: erlang-p1_utils >= %{p1_utils_ver}
Requires: erlang-stun >= %{stun_ver}

%description
%{summary}.

%install -a
install -d $RPM_BUILD_ROOT%{_erllibdir}/esip-%{version}/include
install -d $RPM_BUILD_ROOT%{_erllibdir}/esip-%{version}/priv/lib

install -pm644 include/* $RPM_BUILD_ROOT%{_erllibdir}/esip-%{version}/include/
install -pm755 priv/lib/*.so $RPM_BUILD_ROOT%{_erllibdir}/esip-%{version}/priv/lib/

%files
%license LICENSE.txt
%doc CHANGELOG.md README.md
%{erlang_appdir}

%changelog
%autochangelog
