%global realname getopt

Name:		erlang-%{realname}
Version:	1.0.3
Release:	%autorelease
BuildArch:	noarch
Summary:	Erlang module to parse command line arguments using the GNU getopt syntax
License:	BSD-3-Clause
URL:		https://github.com/jcomellas/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/v%{version}/%{realname}-%{version}.tar.gz
BuildSystem:	rebar3

%description
%{summary}.

%prep -a
chmod 0644 examples/*.escript

%files
%license LICENSE.txt
%doc README.md examples/
%{erlang_appdir}/

%changelog
%autochangelog
