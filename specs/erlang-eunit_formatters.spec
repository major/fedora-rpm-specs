%global realname eunit_formatters

Name:     erlang-%{realname}
Version:  0.6.0
Release:  %autorelease
BuildArch:noarch
Summary:  Better output format for eunit test suites
License:  Apache-2.0
URL:      https://github.com/seancribbs/%{realname}
VCS:      git:%{url}.git
Source0:  %{url}/archive/v%{version}/%{realname}-%{version}.tar.gz
BuildSystem: rebar3

%description
%{summary}.

%files
%license LICENSE
%doc README.md
%{erlang_appdir}/

%changelog
%autochangelog
