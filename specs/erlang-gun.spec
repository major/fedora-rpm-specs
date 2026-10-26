%global realname gun

Name:		erlang-%{realname}
Version:	2.7.0
Release:	%autorelease
BuildArch:	noarch
Summary:	Erlang HTTP client with support for HTTP/1.1, HTTP/2, Websocket and more
License:	ISC
URL:		https://github.com/ninenines/%{realname}
VCS:		git:%{url}.git
Source:		%{url}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch:		erlang-gun-0001-Fix-testing-with-rebar.patch
BuildRequires:	erlang-cowlib
BuildRequires:	erlang-ct_helper
BuildOption(check): -e -c
BuildSystem:	rebar3

%description
%{summary}.

%files
%license LICENSE
%doc README.asciidoc
%{erlang_appdir}/

%changelog
%autochangelog
