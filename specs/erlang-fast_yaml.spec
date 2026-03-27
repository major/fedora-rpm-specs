%global srcname fast_yaml
%global p1_utils_ver 1.0.29

Name: erlang-%{srcname}
Version: 1.0.40
Release: %autorelease
License: Apache-2.0
Summary: An Erlang wrapper for libyaml "C" library
URL:     https://github.com/processone/%{srcname}
VCS:     git:%{url}.git
Source0: %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
Provides:  erlang-p1_yaml = %{version}-%{release}
Obsoletes: erlang-p1_yaml < 1.0.2
BuildRequires: gcc
BuildRequires: erlang-rebar3
BuildRequires: erlang-rebar3-pc
BuildRequires: erlang-p1_utils >= %{p1_utils_ver}
BuildRequires: libyaml-devel
Requires: erlang-p1_utils >= %{p1_utils_ver}

%description
P1 YAML is an Erlang wrapper for libyaml "C" library.

%prep
%autosetup -n %{srcname}-%{version}

%build
%{erlang3_compile}

%install
%{erlang3_install}
install -p -D -m 755 priv/lib/* --target-directory=%{buildroot}%{erlang_appdir}/priv/lib/

%check
%{erlang3_test}

%files
%license LICENSE.txt
%doc CHANGELOG.md
%doc README.md
%{erlang_appdir}

%changelog
%autochangelog
