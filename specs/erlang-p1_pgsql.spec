%global srcname p1_pgsql

Name:       erlang-%{srcname}
Version:    1.1.31
Release:    %autorelease
BuildArch:  noarch
License:    ErlPL-1.1
Summary:    Pure Erlang PostgreSQL driver
URL:        https://github.com/processone/%{srcname}
VCS:        git:%{url}.git
Source0:    %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
Patch1:     erlang-p1_pgsql-0001-Use-generic-crypto-functions.patch
Provides:   erlang-pgsql = %{version}-%{release}
Obsoletes:  erlang-pgsql < 0-16
BuildRequires: erlang-epgsql
BuildRequires: erlang-rebar3

%description
%{summary}.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%build
%{erlang3_compile}

%install
%{erlang3_install}

%check
%{erlang3_test}

%files
%license EPLICENSE
%doc README.md
%{erlang_appdir}/

%changelog
%autochangelog
