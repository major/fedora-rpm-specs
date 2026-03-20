%global srcname fast_yaml
%global p1_utils_ver 1.0.28

Name: erlang-%{srcname}
Version: 1.0.39
Release: %autorelease
License: Apache-2.0
Summary: An Erlang wrapper for libyaml "C" library
URL:     https://github.com/processone/%{srcname}/
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
install -d $RPM_BUILD_ROOT%{_libdir}/erlang/lib/%{srcname}-%{version}/priv/lib
install -pm755 priv/lib/* $RPM_BUILD_ROOT%{_libdir}/erlang/lib/%{srcname}-%{version}/priv/lib

%check
%{erlang3_test}

%files
%license LICENSE.txt
%doc CHANGELOG.md
%doc README.md
%{erlang_appdir}

%changelog
%autochangelog
