%global srcname iconv
%global p1_utils_ver 1.0.19

Name:       erlang-%{srcname}
Version:    1.0.13
Release:    %autorelease
Summary:    Fast encoding conversion library for Erlang / Elixir
License:    Apache-2.0
URL:        https://github.com/processone/%{srcname}
VCS:        scm:git:%{url}.git
Source0:    %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
Provides:   erlang-p1_iconv = %{version}-%{release}
Obsoletes:  erlang-p1_iconv <= 1.0.0-2
BuildRequires: gcc
BuildRequires: erlang-p1_utils >= %{p1_utils_ver}
BuildRequires: erlang-rebar3
BuildRequires: erlang-rebar3-pc
Requires: erlang-p1_utils >= %{p1_utils_ver}

%description
Erlang bindings for libiconv. This is used by ejabberd.

%prep
%autosetup -n %{srcname}-%{version}

%build
%configure --enable-nif
%{erlang3_compile}

%install
%{erlang3_install}

install -d $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/priv/lib
install -pm755 priv/lib/iconv.so $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/priv/lib/

%check
%{erlang3_test}

%files
%license LICENSE.txt
%doc README.md
%{erlang_appdir}

%changelog
%autochangelog
