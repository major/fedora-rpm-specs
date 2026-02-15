%global realname riakc

Name:		erlang-riak_client
Version:	3.0.13
Release:	%autorelease
BuildArch:	noarch
Summary:	Erlang client for Riak
License:	Apache-2.0
URL:		https://github.com/basho/riak-erlang-client
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{version}/riak_client-%{version}.tar.gz
Patch:		erlang-riak_client-0001-Allow-more-Erlang-versions.patch
Patch:		erlang-riak_client-0002-Add-deprecation-for-Erlang-20-as-well.patch
Patch:		erlang-riak_client-0003-Fix-edoc-generation.patch
BuildRequires:	erlang-rebar3
BuildRequires:	erlang-riak_pb

%description
%{summary}.

%prep
%autosetup -p1 -n riak-erlang-client-%{version}

%build
%{erlang3_compile}

%install
%{erlang3_install}

%check
%{erlang3_test}

%files
%license LICENSE
%doc README.md
%{erlang_appdir}/

%changelog
%autochangelog
