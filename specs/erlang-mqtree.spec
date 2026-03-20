%global srcname mqtree
%global p1_utils_ver 1.0.28

Name:       erlang-%{srcname}
Version:    1.0.19
Release:    %autorelease
License:    Apache-2.0
Summary:    Index tree for MQTT topic filters
URL:        https://github.com/processone/%{srcname}/
VCS:        git:%{url}.git
Source0:    %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
Patch:      erlang-mqtree-0001-Remove-bundled-uthash.patch
BuildRequires: erlang-p1_utils >= %{p1_utils_ver}
BuildRequires: erlang-rebar3
BuildRequires: erlang-rebar3-pc
BuildRequires: gcc
BuildRequires: openssl-devel
BuildRequires: uthash-devel
Requires: erlang-p1_utils >= %{p1_utils_ver}

%description
An Erlang NIF implementation of N-ary tree to keep MQTT topic filters for
efficient matching.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%build
%{erlang3_compile}

%install
%{erlang3_install}

install -d %{buildroot}%{_erllibdir}/%{srcname}-%{version}/priv/lib
install -pm755 priv/lib/* %{buildroot}%{_erllibdir}/%{srcname}-%{version}/priv/lib/

%check
%{erlang3_test}

%files
%license LICENSE
%doc README.md
%{erlang_appdir}

%changelog
%autochangelog
