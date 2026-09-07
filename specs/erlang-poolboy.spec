%global realname poolboy

Name:		erlang-%{realname}
Version:	1.5.2
Release:	%autorelease
BuildArch:	noarch
Summary:	A hunky Erlang worker pool factory
License:	Unlicense OR ISC
URL:		https://github.com/devinus/%{realname}
VCS:		git:%{url}.git
Source:		%{url}/archive/%{version}/%{realname}-%{version}.tar.gz
BuildRequires:	erlang-rebar3-eqc
BuildSystem:	rebar3

%description
%{summary}.

%files
%license LICENSE UNLICENSE
%doc README.md
%{erlang_appdir}/

%changelog
%autochangelog
