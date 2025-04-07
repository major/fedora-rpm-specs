%global srcname luerl

Name:       erlang-%{srcname}
Version:    1.3.0
Release:    %autorelease
BuildArch:  noarch
License:    Apache-2.0
Summary:    Lua in Erlang
URL:        https://github.com/rvirding/%{srcname}
VCS:        git:%{url}.git
Source0:    %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
BuildRequires: dos2unix
BuildRequires: erlang-rebar3

%description
An experimental implementation of Lua 5.2 written solely in pure Erlang.

%prep
%autosetup -n %{srcname}-%{version}
dos2unix examples/hello/hello2-3.lua

%build
%{erlang3_compile}

%check
%{erlang3_test}

%install
%{erlang3_install}

%files
%license LICENSE
%doc examples
%doc README.md
%doc src/NOTES
%{erlang_appdir}

%changelog
%autochangelog
