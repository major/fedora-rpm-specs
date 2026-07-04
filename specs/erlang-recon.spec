%global realname recon

Name: erlang-%{realname}
Version: 2.5.6
Release: %autorelease
BuildArch: noarch
License: BSD-3-Clause
Summary: A collection of functions and scripts to debug Erlang in production
URL: https://github.com/ferd/recon
VCS: git:%{url}.git
Source0: %{url}/archive/%{version}/%{realname}-%{version}.tar.gz
BuildRequires: erlang-rebar3

%description
Recon wants to be a set of tools usable in production to diagnose Erlang
problems or inspect production environment safely.

%prep
%autosetup -p1 -n %{realname}-%{version}

%build
%{erlang3_compile}

%install
%{erlang3_install}

%check
%{erlang3_test}

%files
%license LICENSE
%doc CHANGELOG.md
%doc README.md
%{erlang_appdir}

%changelog
%autochangelog
