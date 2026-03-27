%global srcname ezlib
%global p1_utils_ver 1.0.29

Name:       erlang-%{srcname}
Version:    1.0.16
Release:    %autorelease
License:    Apache-2.0
Summary:    Native zlib driver for Erlang
URL:        https://github.com/processone/%{srcname}
VCS:        git:%{url}.git
Source0:    %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
Provides:   erlang-p1_zlib = %{version}-%{release}
Obsoletes:  erlang-p1_zlib <= 1.0.1-2
BuildRequires: erlang-p1_utils >= %{p1_utils_ver}
BuildRequires: erlang-rebar3
BuildRequires: erlang-rebar3-pc
BuildRequires: gcc
BuildRequires: zlib-devel
Requires: erlang-p1_utils >= %{p1_utils_ver}

%description
A native zlib driver for Erlang / Elixir, used by ejabberd.

%prep
%autosetup -n %{srcname}-%{version}

%build
%{erlang3_compile}

%install
%{erlang3_install}
install -p -D -m 755 priv/lib/ezlib.so --target-directory=%{buildroot}%{erlang_appdir}/priv/lib/

%check
%{erlang3_test}

%files
%license LICENSE.txt
%doc CHANGELOG.md
%doc README.md
%{erlang_appdir}

%changelog
%autochangelog
