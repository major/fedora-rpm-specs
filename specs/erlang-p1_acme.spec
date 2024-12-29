%global srcname p1_acme

%global base64url_ver 1.0.1
%global idna_ver 6.0.0
%global jiffy_ver 1.1.1
%global jose_ver 1.11.10
%global yconf_ver 1.0.17

Name:       erlang-%{srcname}
Version:    1.0.25
Release:    %autorelease
BuildArch:  noarch
License:    Apache-2.0
Summary:    ACME client library for Erlang
URL:        https://github.com/processone/%{srcname}
VCS:        git:%{url}.git
Source0:    %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildRequires: erlang-base64url >= %{base64url_ver}
BuildRequires: erlang-idna >= %{idna_ver}
BuildRequires: erlang-jiffy >= %{jiffy_ver}
BuildRequires: erlang-jose >= %{jose_ver}
BuildRequires: erlang-rebar3
BuildRequires: erlang-yconf >= %{yconf_ver}
Requires: erlang-base64url >= %{base64url_ver}
Requires: erlang-idna >= %{idna_ver}
Requires: erlang-jiffy >= %{jiffy_ver}
Requires: erlang-jose >= %{jose_ver}
Requires: erlang-yconf >= %{yconf_ver}

%description
%{summary}.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%build
%{erlang3_compile}

%check
%{erlang3_test}

%install
%{erlang3_install}

%files
%license LICENSE.txt
%doc CHANGELOG.md
%doc README.md
%{erlang_appdir}

%changelog
%autochangelog
