%global realname mozjs

Name: erlang-%{realname}
Version: 2.0.1
Release: %autorelease
License: Apache-2.0
Summary: A NIF module for Erlang to Mozilla's Spidermonkey Javascript runtime
URL:     https://github.com/erlang-mozjs/erlang-mozjs
VCS:     git:%{url}.git
Source0: %{url}/archive/%{version}/erlang-%{realname}-%{version}.tar.gz
BuildRequires: erlang-jsx
BuildRequires: erlang-rebar3
BuildRequires: erlang-rebar3-pc
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: mozjs140-devel
Obsoletes: erlang-js < 2.0.0
Provides: erlang-js%{?_isa} = %{version}-%{release}

%description
A NIF library that embeds Mozilla's SpiderMonkey JavaScript engine in Erlang.
Originally created to facilitate usage of Riak's MapReduce by non-Erlang
programmers, it supports multiple concurrent JavaScript VMs, runtime evaluation
of JavaScript code, and invocation of JavaScript functions.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%{erlang3_compile}

%install
%{erlang3_install}

%check
%{erlang3_test}

%files
%license LICENSE
%doc README.md
%{erlang_appdir}

%changelog
%autochangelog
