%global realname clique

Name:		erlang-%{realname}
Version:	0.3.12
Release:	%autorelease
BuildArch:	noarch
Summary:	CLI Framework for Erlang
License:	Apache-2.0
URL:		https://github.com/basho/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch1:		erlang-clique-0001-Don-t-hide-dependency-on-mochiweb.patch
BuildRequires:	erlang-cuttlefish
BuildRequires:	erlang-mochiweb
BuildSystem:	rebar3

%description
Clique is an opinionated framework for building command line interfaces in
Erlang. It provides users with an interface that gives them enough power to
build complex CLIs, but enough constraint to make them appear consistent.

%files
%license LICENSE
%doc README.md
%{erlang_appdir}/

%changelog
%autochangelog
