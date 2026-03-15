%global realname edown

Name:		erlang-%{realname}
Version:	0.9.2
Release:	%autorelease
BuildArch:	noarch
Summary:	EDoc extension for generating GitHub-flavored Markdown
License:	Apache-2.0
URL:		https://github.com/uwiger/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch:		erlang-edown-0001-Remove-pre-18.0-code.patch
Patch:		erlang-edown-0002-Don-t-use-git-command-for-branch-retrieval.patch
BuildRequires:	erlang-edoc
BuildSystem:	rebar3

%description
%{summary}.

%files
%doc NOTICE README.md doc/
%{erlang_appdir}/

%changelog
%autochangelog
