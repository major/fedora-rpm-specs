%global realname ssl_verify_fun

Name:     erlang-%{realname}
Version:  1.1.7
Release:  %autorelease
Summary:  Collection of ssl verification functions for Erlang
License:  MIT
URL:      https://github.com/deadtrickster/%{realname}.erl
VCS:      git:%{url}.git
Source0:  %{url}/archive/%{version}/%{realname}-%{version}.tar.gz
BuildArch:   noarch
BuildSystem: rebar3

%description
%{summary}.

%files
%license LICENSE
%doc README.md
%{erlang_appdir}/

%changelog
%autochangelog
