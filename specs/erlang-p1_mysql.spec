%global srcname p1_mysql

Name:       erlang-%{srcname}
Version:    1.0.27
Release:    %autorelease
BuildArch:  noarch
Summary:    Pure Erlang MySQL driver, used by ejabberd
License:    BSD-3-Clause
URL:        https://github.com/processone/%{srcname}
VCS:        git:%{url}.git
Source0:    %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
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
%license COPYING
%doc README.md
%{erlang_appdir}

%changelog
%autochangelog
