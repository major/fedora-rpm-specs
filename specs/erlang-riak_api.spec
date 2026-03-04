%global realname riak_api

Name:		erlang-%{realname}
Version:	3.0.16
Release:	%autorelease
BuildArch:	noarch
Summary:	Riak Client APIs
License:	Apache-2.0
URL:		https://github.com/basho/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/riak_kv-%{version}/%{realname}-%{version}.tar.gz
BuildRequires:	erlang-meck
BuildRequires:	erlang-mochiweb
BuildRequires:	erlang-rebar3
BuildRequires:	erlang-riak_core
BuildRequires:	erlang-riak_pb
BuildRequires:	erlang-webmachine

%description
This OTP application encapsulates services for presenting Riak's public-facing
interfaces. Currently this means a generic interface for exposing Protocol
Buffers-based services; HTTP services via Webmachine will be moved here at a
later time.

%prep
%autosetup -p1 -n %{realname}-riak_kv-%{version}

%build
%{erlang3_compile}

%install
%{erlang3_install}
install -D -p -m 644 priv/riak_api.schema %{buildroot}%{erlang_appdir}/priv/riak_api.schema

%check
%{erlang3_test}

%files
%doc README.md
%{erlang_appdir}/

%changelog
%autochangelog
