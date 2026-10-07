%global srcname oauth2

Name:       erlang-%{srcname}
Version:    1.0.10
Release:    %autorelease
BuildArch:  noarch
License:    MIT
Summary:    An Oauth2 implementation for Erlang
URL:        https://github.com/kivra/%{srcname}
VCS:        git:%{url}.git
Source:     %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
BuildRequires: erlang-meck
BuildRequires: erlang-proper
BuildSystem:   rebar3

%description
This library is designed to simplify the implementation of the server side of
OAuth2.

%files
%license LICENSE
%doc README.md
%{erlang_appdir}/

%changelog
%autochangelog
