%global srcname cache_tab
%global p1_utils_ver 1.0.29

Name: erlang-%{srcname}
Version: 1.0.34
Release: %autorelease
License: Apache-2.0
Summary: Erlang cache table application
URL:     https://github.com/processone/%{srcname}
VCS:     git:%{url}.git
Source:  %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildRequires: gcc
BuildRequires: erlang-rebar3-pc
BuildRequires: erlang-p1_utils >= %{p1_utils_ver}
BuildSystem:   rebar3
Requires: erlang-p1_utils >= %{p1_utils_ver}

%description
This application is intended to proxy back-end operations for Key-Value insert,
lookup and delete and maintain a cache of those Key-Values in-memory, to save
back-end operations. Operations are intended to be atomic between back-end and
cache tables. The lifetime of the cache object and the max size of the cache
can be defined as table parameters to limit the size of the in-memory tables.

%files
%license LICENSE.txt
%doc CHANGELOG.md
%doc README.md
%{erlang_appdir}/

%changelog
%autochangelog
