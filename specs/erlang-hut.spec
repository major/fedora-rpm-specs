%global realname hut

Name:		erlang-%{realname}
Version:	1.4.0
Release:	%autorelease
BuildArch:	noarch
Summary:	A helper library for making Erlang libraries logging framework agnostic
License:	MIT
URL:		https://github.com/tolbrino/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/v%{version}/%{realname}-%{version}.tar.gz
BuildSystem:	rebar3

%description
A a minimal library for Erlang libraries and small applications to stay
agnostic to the logging framework in use. Its purpose is to allow the
developers of umbrella applications to use their logging framework of choice
and ensure that dependency stick to that choice as well.

%files
%license LICENSE
%doc README.md
%{erlang_appdir}/

%changelog
%autochangelog
