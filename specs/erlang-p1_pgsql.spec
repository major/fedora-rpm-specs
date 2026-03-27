%global srcname p1_pgsql
%global stringprep_ver 1.0.34

Name:       erlang-%{srcname}
Version:    1.1.41
Release:    %autorelease
BuildArch:  noarch
License:    ErlPL-1.1
Summary:    Pure Erlang PostgreSQL driver
URL:        https://github.com/processone/%{srcname}
VCS:        git:%{url}.git
Source0:    %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
Provides:   erlang-pgsql = %{version}-%{release}
Obsoletes:  erlang-pgsql < 0-16
BuildRequires: erlang-rebar3
BuildRequires: erlang-stringprep >= %{stringprep_ver}
Requires: erlang-stringprep >= %{stringprep_ver}

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
