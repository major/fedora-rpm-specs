%global srcname yconf

%global fast_yaml_ver 1.0.37

Name:       erlang-%{srcname}
Version:    1.0.17
Release:    %autorelease
BuildArch:  noarch
License:    Apache-2.0
Summary:    YAML configuration processor
URL:        https://github.com/processone/%{srcname}
VCS:        git:%{url}.git
Source0:    %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildRequires: erlang-fast_yaml >= %{fast_yaml_ver}
BuildRequires: erlang-rebar3

Requires: erlang-fast_yaml >= %{fast_yaml_ver}


%description
%{summary}.


%prep
%autosetup -n %{srcname}-%{version}


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
