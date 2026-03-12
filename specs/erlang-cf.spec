%global realname cf

Name:     erlang-%{realname}
Version:  0.3.1
Release:  %autorelease
BuildArch:noarch
Summary:  Terminal color helper
License:  BSD-3-Clause
URL:      https://github.com/project-fifo/%{realname}
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
