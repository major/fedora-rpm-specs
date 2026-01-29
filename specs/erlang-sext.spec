%global realname sext

Name:		erlang-%{realname}
Version:	1.8.0
Release:	%autorelease
BuildArch:	noarch
Summary:	Sortable Erlang Term Serialization
License:	Apache-2.0
URL:		https://github.com/uwiger/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch:		erlang-sext-0001-Handle-OTP-26-external-term-format-changes.patch
BuildRequires:	erlang-edown
BuildRequires:	erlang-rebar3

%description
A sortable serialization library This library offers a serialization format (a
la term_to_binary()) that preserves the Erlang term order.

%prep
%autosetup -p1 -n %{realname}-%{version}

%build
%{erlang3_compile}

%install
%{erlang3_install}

%check
%{erlang3_test}

%files
%license LICENSE
%doc NOTICE README.md examples/
%{erlang_appdir}/

%changelog
%autochangelog
