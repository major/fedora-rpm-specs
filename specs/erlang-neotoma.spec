%global realname neotoma

Name:		erlang-%{realname}
Version:	1.7.4
Release:	%autorelease
BuildArch:	noarch
Summary:	Erlang library and packrat parser-generator for parsing expression grammars
License:	MIT
URL:		https://github.com/seancribbs/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{version}/%{realname}-%{version}.tar.gz
BuildSystem:	rebar3

%description
%{summary}.

%install -a
mkdir -p %{buildroot}%{erlang_appdir}/priv
install -p -m 0644 priv/neotoma_parse.peg priv/peg_includes.hrl %{buildroot}%{erlang_appdir}/priv/

%files
%license LICENSE
%doc extra/ README.textile
%{erlang_appdir}/

%changelog
%autochangelog
