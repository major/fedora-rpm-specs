%global srcname luerl

Name:       erlang-%{srcname}
Version:    1.5.1
Release:    %autorelease
BuildArch:  noarch
License:    Apache-2.0
Summary:    Lua in Erlang
URL:        https://github.com/rvirding/%{srcname}
VCS:        git:%{url}.git
Source0:    %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
Patch:      erlang-luerl-0001-Temporarily-disable-prebar-plugins.patch
Patch:      erlang-luerl-0002-Convert-to-UNIX-line-endings.patch
BuildRequires: erlang-rebar3

%description
An experimental implementation of Lua 5.2 written solely in pure Erlang.

%prep
%autosetup -p1 -n %{srcname}-%{version}

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
