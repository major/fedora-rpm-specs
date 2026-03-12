%global realname gen_leader
%global git_commit d9689e6e80cd8a437bc207d37cb53290ecd64b35

Name:		erlang-%{realname}
Version:	1.0
Release:	%autorelease
BuildArch:	noarch
Summary:	A leader election behavior modeled after gen_server
License:	ErlPL-1.1
URL:		https://github.com/garret-smith/%{realname}_revival
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{git_commit}/%{realname}-%{version}.tar.gz
BuildSystem:	rebar3

%description
This application implements a leader election behavior modeled after gen_server.
This behavior intends to make it reasonably straightforward to implement a fully
distributed server with master-slave semantics.

%files
%doc README.markdown examples/
%{erlang_appdir}/

%changelog
%autochangelog
