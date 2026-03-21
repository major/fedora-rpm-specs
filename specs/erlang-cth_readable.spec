%global realname cth_readable

Name:     erlang-%{realname}
Version:  1.6.1
Release:  %autorelease
Summary:  Common test hooks for more readable erlang logs
License:  BSD-3-Clause
URL:      https://github.com/ferd/%{realname}
VCS:      git:%{url}.git
Source0:  %{url}/archive/v%{version}/%{realname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  erlang-lager
BuildSystem:	rebar3

%description
%{summary}.

%prep -a
# These test suites are intentional failure fixtures for testing
# cth_readable's output capture hooks. They are designed to fail
# and cannot pass when run via standalone rebar3 ct.
rm test/failonly_SUITE.erl
rm test/show_logs_SUITE.erl
rm test/sample_SUITE.erl

%files
%license LICENSE
%doc README.md
%{erlang_appdir}/

%changelog
%autochangelog
