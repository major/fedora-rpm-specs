%global realname bear

Name:		erlang-%{realname}
Version:	1.1
Release:	%autorelease
BuildArch:	noarch
Summary:	A set of statistics functions for erlang
License:	Apache-2.0
URL:		https://github.com/folsom-project/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{version}/%{realname}-%{version}.tar.gz
BuildSystem:	rebar3

%description
A set of statistics functions for Erlang. Currently bear is focused on use
inside the Folsom Erlang metrics library but all of these functions are generic
and useful in other situations.

%files
%license LICENSE
%doc README.md
%{erlang_appdir}/

%changelog
%autochangelog
