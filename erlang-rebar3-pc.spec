%global realname pc
%global upstream blt

Name:		erlang-rebar3-%{realname}
Version:	1.14.0
Release:        %autorelease
Summary:	A port compiler for rebar3
License:	MIT
URL:		https://github.com/%{upstream}/port_compiler
VCS:		scm:git:https://github.com/%{upstream}/port_compiler.git
Source0:	%{url}/archive/v%{version}/port_compiler-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	erlang-rebar3

%description
This plugin is intended to replicate the rebar2 support for compiling native
code. It is not a drop-in replacement in terms of command-line interface but
the exact configuration interface in projects' rebar.configs have been
preserved.

%prep
%autosetup -p1 -n port_compiler-%{version}


%build
%{erlang3_compile}


%check
%{erlang3_test}


%install
%{erlang3_install}


%files
%license LICENSE
%doc README.md
%{erlang_appdir}


%changelog
%autochangelog
