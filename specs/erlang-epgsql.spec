%global realname epgsql

Summary:	Erlang PostgreSQL client library
Name:		erlang-%{realname}
Version:	4.8.0
Release:	%autorelease
BuildArch:	noarch
License:	BSD-3-Clause
URL:		https://github.com/%{realname}/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{version}/%{realname}-%{version}.tar.gz
BuildRequires:	erlang-rebar3

%description
Library that gives possibility to Erlang programs to connect PostgreSQL
databases by plain TCP and execute simple SQL statements.

%prep
%autosetup -p1 -n %{realname}-%{version}

%build
%{erlang3_compile}

%install
%{erlang3_install}

%check
# TODO Requires PostgreSQL connection
#%%{erlang3_test}

%files
%license LICENSE
%doc CHANGES README.md TODO
%{erlang_appdir}/

%changelog
%autochangelog
