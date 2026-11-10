%global realname ranch

Name:		erlang-%{realname}
Version:	2.4.0
Release:	%autorelease
BuildArch:	noarch
Summary:	Socket acceptor pool for TCP protocols
License:	ISC
URL:		https://github.com/ninenines/%{realname}
VCS:		git:%{url}.git
Source:		%{url}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch:		erlang-ranch-0001-Fix-testing-with-rebar.patch
BuildRequires:	erlang-ct_helper
BuildSystem:	rebar3

%description
%{summary}.

%prep -a
# FIXME we don't have stampede yet
rm -f test/stampede_SUITE.erl
# FIXME this test is very fragile and cannot be run with Rebar3 directly
rm -f test/upgrade_SUITE.erl

%files
%license LICENSE
%doc README.asciidoc doc/ examples/
%{erlang_appdir}/

%changelog
%autochangelog
