%global realname basho_stats

Name:		erlang-%{realname}
Version:	1.1.0
Release:	%autorelease
BuildArch:	noarch
Summary:	Basic Erlang statistics library
License:	Apache-2.0
URL:		https://github.com/basho/%{realname}
VCS:		git:%{url}.git
Source:		%{url}/archive/%{version}/%{realname}-%{version}.tar.gz
BuildRequires:	erlang-rebar3-eqc
BuildSystem:	rebar3

%description
%{summary}.

%files
%{erlang_appdir}/

%changelog
%autochangelog
