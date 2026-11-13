%global srcname idna

Name:       erlang-%{srcname}
Version:    8.0.0
Release:    %autorelease
BuildArch:  noarch
License:    MIT
Summary:    A pure Erlang IDNA implementation that folllows RFC5891
URL:        https://github.com/benoitc/erlang-%{srcname}
VCS:        git:%{url}.git
Source:     %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildSystem: rebar3

%description
%{summary}.

%files
%license LICENSE
%doc CHANGELOG
%doc README.md
%{erlang_appdir}

%changelog
%autochangelog
