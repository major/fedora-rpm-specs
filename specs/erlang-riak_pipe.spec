%global realname riak_pipe


Name:		erlang-%{realname}
Version:	3.0.16
Release:	%autorelease
BuildArch:	noarch
Summary:	Riak Pipelines
License:	Apache-2.0
URL:		https://github.com/basho/%{realname}
VCS:		git:%{url}.git
Source:		%{url}/archive/riak_kv-%{version}/%{realname}-%{version}.tar.gz
BuildRequires:	erlang-cluster_info
BuildRequires:	erlang-exometer_core
BuildRequires:	erlang-lager
BuildRequires:	erlang-rebar3
BuildRequires:	erlang-rebar3-eqc
BuildRequires:	erlang-riak_core


%description
%{summary}.


%prep
%autosetup -p1 -n %{realname}-riak_kv-%{version}


%build
%{erlang3_compile}


%install
%{erlang3_install}
install -p -m 644 priv/app.slave0.config %{buildroot}%{erlang_appdir}/priv


%check
%{erlang3_test}


%files
%license LICENSE
%doc README.org
%{erlang_appdir}/


%changelog
%autochangelog
