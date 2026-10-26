%global realname cowlib

Name:		erlang-%{realname}
Version:	2.21.0
Release:	%autorelease
BuildArch:	noarch
Summary:	Support library for manipulating Web protocols
License:	Apache-2.0
URL:		https://github.com/ninenines/%{realname}
VCS:		git:%{url}.git
Source:		%{url}/archive/%{version}/%{realname}-%{version}.tar.gz
BuildRequires:	erlang-proper
BuildSystem:	rebar3

%description
%{summary}.

%files
%license LICENSE
%doc README.asciidoc
%{erlang_appdir}/

%changelog
%autochangelog
