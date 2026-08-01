%global srcname base64url

Name:      erlang-%{srcname}
Version:   1.0.1
Release:   %autorelease
BuildArch: noarch
License:   MIT
Summary:   Standalone URL safe base64-compatible codec
URL:       https://github.com/dvv/%{srcname}
VCS:       git:%{url}.git
Source0:   %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildSystem: rebar3

%description
%{summary}.

%files
%license LICENSE.txt
%doc README.md
%{erlang_appdir}/

%changelog
%autochangelog
