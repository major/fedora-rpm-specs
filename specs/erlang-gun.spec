%global realname gun

Name:		erlang-%{realname}
Version:	2.2.0
Release:	%autorelease
BuildArch:	noarch
Summary:	Erlang HTTP client with support for HTTP/1.1, HTTP/2, Websocket and more
License:	ISC
URL:		https://github.com/ninenines/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch1:		erlang-gun-0001-Fix-testing-with-rebar.patch
BuildRequires:	erlang-cowlib
BuildRequires:	erlang-ct_helper
BuildRequires:	erlang-rebar3

%description
%{summary}.

%prep
%autosetup -p1 -n %{realname}-%{version}

%build
%{erlang3_compile}

%install
%{erlang3_install}

%check
# FIXME requires Golang utility for code generation
#%%{erlang3_test}

%files
%license LICENSE
%doc README.asciidoc
%{erlang_appdir}/

%changelog
%autochangelog
