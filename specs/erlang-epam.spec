%global srcname epam

Name:       erlang-%{srcname}
Version:    1.0.14
Release:    %autorelease
Summary:    Library for ejabberd for PAM authentication support
License:    Apache-2.0
URL:        https://github.com/processone/%{srcname}
VCS:        git:%{url}.git
Source0:    %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildRequires: gcc
BuildRequires: erlang-rebar3
BuildRequires: erlang-rebar3-pc
BuildRequires: pam-devel
Provides: erlang-p1_pam = %{version}-%{release}
Obsoletes: erlang-p1_pam < 1.0.3-4%{?dist}

%description
An Erlang library for ejabberd that helps with PAM authentication.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%build
%{erlang3_compile}

%install
%{erlang3_install}

install -d $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/priv/bin
install -pm755 priv/bin/%{srcname} $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/priv/bin/

%check
%{erlang3_test}

%files
%license LICENSE.txt
%doc CHANGELOG.md
%doc README.md
%{erlang_appdir}/

%changelog
%autochangelog
