%global srcname stun
%global fast_tls_ver 1.1.26
%global p1_utils_ver 1.0.29

Name:      erlang-%{srcname}
Version:   1.2.23
Release:   %autorelease
BuildArch: noarch
License:   Apache-2.0
Summary:   STUN and TURN library for Erlang / Elixir
URL:       https://github.com/processone/%{srcname}
VCS:       git:%{url}.git
Source0:   %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
Provides:  erlang-p1_stun = %{version}-%{release}
Obsoletes: erlang-p1_stun < 1.0.1
BuildRequires: erlang-edoc
BuildRequires: erlang-fast_tls >= %{fast_tls_ver}
BuildRequires: erlang-p1_utils >= %{p1_utils_ver}
BuildSystem:   rebar3
Requires: erlang-fast_tls >= %{fast_tls_ver}
Requires: erlang-p1_utils >= %{p1_utils_ver}

%description
STUN and TURN library for Erlang / Elixir. Both STUN (Session Traversal
Utilities for NAT) and TURN standards are used as techniques to establish media
connection between peers for VoIP (for example using SIP or Jingle) and WebRTC.

%files
%license LICENSE.txt
%doc CHANGELOG.md
%doc README.md
%{erlang_appdir}

%changelog
%autochangelog
