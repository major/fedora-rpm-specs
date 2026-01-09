%global srcname oauth2

Name:       erlang-%{srcname}
Version:    0.9.5
Release:    %autorelease
BuildArch:  noarch
License:    MIT
Summary:    An Oauth2 implementation for Erlang
URL:        https://github.com/kivra/%{srcname}
VCS:        git:%{url}.git
Source0:    %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
BuildRequires: erlang-meck
BuildRequires: erlang-proper
BuildRequires: erlang-rebar3

%description
This library is designed to simplify the implementation of the server side of
OAuth2.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%build
%{erlang3_compile}

%install
%{erlang3_install}

%check
%{erlang3_test}

%files
%license LICENSE
%doc README.md
%{erlang_appdir}/

%changelog
%autochangelog
