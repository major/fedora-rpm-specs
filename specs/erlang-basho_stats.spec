%global realname basho_stats

Name:		erlang-%{realname}
Version:	1.1.0
Release:	%autorelease
BuildArch:	noarch
Summary:	Basic Erlang statistics library
License:	Apache-2.0
URL:		https://github.com/basho/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch:		erlang-basho_stats-0001-We-still-do-not-use-eqc-for-checking.patch
BuildSystem:	rebar3

%description
%{summary}.

%files
%{erlang_appdir}/

%changelog
%autochangelog
