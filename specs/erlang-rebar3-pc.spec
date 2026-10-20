%global realname pc

Name:		erlang-rebar3-%{realname}
Version:	1.15.0
Release:	%autorelease
Summary:	A port compiler for Rebar3
License:	MIT
URL:		https://github.com/blt/port_compiler
VCS:		git:%{url}.git
Source:		%{url}/archive/v%{version}/port_compiler-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	rebar3
# Required for port compiling but cannot be picked up automatically yet
Requires:	erlang-erl_interface

%description
This plugin is intended to replicate the Rebar2 support for compiling native
code. It is not a drop-in replacement in terms of command-line interface but
the exact configuration interface in projects' rebar.configs have been
preserved.

%files
%license LICENSE
%doc README.md
%{erlang_appdir}

%changelog
%autochangelog
