%global realname providers

Name:     erlang-%{realname}
Version:  1.9.0
Release:  %autorelease
Summary:  An Erlang providers library
License:  Apache-2.0
URL:      https://github.com/tsloughter/%{realname}
VCS:      git:%{url}.git
Source0:  %{url}/archive/%{version}/%{realname}-%{version}.tar.gz
BuildArch:  noarch
BuildRequires: erlang-erlware_commons
BuildSystem: rebar3

%description
%{summary}.

%files
%license LICENSE
%doc README.md
%{erlang_appdir}/

%changelog
%autochangelog
