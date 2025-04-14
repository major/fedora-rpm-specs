%global realname cowlib

Name:		erlang-%{realname}
Version:	2.15.0
Release:	%autorelease
BuildArch:	noarch
Summary:	Support library for manipulating Web protocols
License:	Apache-2.0
URL:		https://github.com/ninenines/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{version}/%{realname}-%{version}.tar.gz
BuildRequires:  erlang-proper
BuildRequires:  erlang-rebar3

%description
%{summary}.

%prep
%autosetup -n %{realname}-%{version}

%build
%{erlang3_compile}

%install
%{erlang3_install}

%check
# FIXME QuickCheck tests doesn't work with Proper atm
%{erlang3_test}

%files
%license LICENSE
%doc README.asciidoc
%{erlang_appdir}/

%changelog
%autochangelog
