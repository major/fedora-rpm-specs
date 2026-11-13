%global realname erlfmt

Name:		erlang-%{realname}
Version:	1.8.0
Release:	%autorelease
BuildArch:	noarch
Summary:	An automated code formatter for Erlang
License:	Apache-2.0
URL:		https://github.com/WhatsApp/%{realname}
VCS:		git:%{url}.git
Source:		%{url}/archive/v%{version}/%{realname}-%{version}.tar.gz
BuildRequires:	erlang-getopt
BuildOption(check): -e
BuildSystem:	rebar3

%description
An opinionated Erlang code formatter. By automating the process of formatting
the code, it frees your team up to focus on what the code does, instead of what
it looks like.

%files
%license LICENSE
%doc README.md doc/
%{erlang_appdir}/

%changelog
%autochangelog
