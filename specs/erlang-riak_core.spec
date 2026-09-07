%global realname riak_core


Name:		erlang-%{realname}
Version:	3.0.16
Release:	%autorelease
BuildArch:	noarch
Summary:	Distributed systems infrastructure used by Riak
# ./src/bloom.erl, ./src/riak_core_gen_server.erl is under ErlPL-1.1
# ./src/dvvset.erl, ./src/gen_nb_server.erl is under MIT
# ./src/riak_core_priority_queue.erl is under MPL-1.1
# The rest is under ASL2.0
License:	Apache-2.0 and ErlPL-1.1 and MIT and MPL-1.1
URL:		https://github.com/basho/%{realname}
VCS:		git:%{url}.git
Source:		%{url}/archive/riak_kv-%{version}/%{realname}-%{version}.tar.gz
# Fedora-specific
Patch:	erlang-riak_core-0001-Don-t-use-pbkdf2-as-application.patch
# Fedora-specific (unbundle mochiglobal)
Patch:	erlang-riak_core-0002-Revert-Copy-in-mochiglobal-as-riak_core_mochiglobal.patch
# Fedora-specific (we have more directories to search for code artifacts)
Patch:	erlang-riak_core-0003-Be-more-greedy-while-loading-schemas.patch
# Fedora-specific (we have more directories to search for code artifacts)
Patch:	erlang-riak_core-0004-Load-cuttlefish-schemas-from-noarch-dir-as-well.patch
Patch:	erlang-riak_core-0006-Don-t-threat-warnings-as-errors.patch
# https://github.com/basho/riak_core/pull/639
Patch:	erlang-riak_core-0007-Use-poolboy-API-for-stopping-poolboy.patch
Patch:	erlang-riak_core-0008-Ignore-completely-reply-value.patch
Patch:	erlang-riak_core-0009-Fix-test-with-self-signed-certificates.patch
BuildRequires:	erlang-basho_stats >= 1.1.0
BuildRequires:	erlang-clique >= 0.3.12
BuildRequires:	erlang-cluster_info >= 2.1.0
BuildRequires:	erlang-eleveldb >= 3.0.10
BuildRequires:	erlang-exometer_core >= 1.6.1
BuildRequires:	erlang-folsom
BuildRequires:	erlang-hut
BuildRequires:	erlang-lager >= 3.8.0
BuildRequires:	erlang-meck
BuildRequires:	erlang-mochiweb
# FIXME not packaged - see patch no. 1
# BuildRequires:	erlang-pbkdf2 >= 2.1.0
BuildRequires:	erlang-poolboy >= 1.5.2
BuildRequires:	erlang-rebar3
BuildRequires:	erlang-rebar3-eqc
BuildRequires:	erlang-riak_ensemble >= 3.0.10
BuildRequires:	erlang-riak_sysmon >= 2.2.1
BuildRequires:	openssl


%description
%{summary}.


%prep
%autosetup -p1 -n %{realname}-riak_kv-%{version}
# Exometer removed Folsom support
rm -f src/riak_core_exo_monitor.erl


%build
%{erlang3_compile}


%install
%{erlang3_install}
install -D -p -m 644 priv/riak_core.schema %{buildroot}%{erlang_appdir}/priv/riak_core.schema


%check
# Rebuild certificates
openssl req -x509 -newkey rsa:4096 -keyout ./test/site1-key.pem -out ./test/site1-cert.pem -sha256 -days 365 -subj "/CN=site1.example.com" -nodes
openssl req -x509 -newkey rsa:4096 -keyout ./test/site2-key.pem -out ./test/site2-cert.pem -sha256 -days 365 -subj "/CN=site1.example.com" -nodes

%{erlang3_test}


%files
%license LICENSE
%doc README.md docs/*
%{erlang_appdir}/


%changelog
%autochangelog
