%global realname riak_dt

Name:		erlang-%{realname}
Version:	3.0.0
Release:	%autorelease
BuildArch:	noarch
Summary:	Convergent replicated data types in Erlang
License:	Apache-2.0
URL:		https://github.com/basho/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/riak_kv-%{version}/%{realname}-%{version}.tar.gz
Patch:		erlang-riak_dt-0001-A-couple-of-failing-tests-which-look-to-be-caused-by.patch
Patch:		erlang-riak_dt-0001-FIXME-disable-plugins.patch
BuildRequires:	erlang-rebar3

%description
A set of state based CRDTs implemented in Erlang.

%prep
%autosetup -p1 -n %{realname}-riak_kv-%{version}

%build
%{erlang3_compile}

%install
%{erlang3_install}

%check
# Some tests requires a proprietary library - QuickCheck
%{erlang3_test}

%files
%license LICENSE
%doc README.md
%{erlang_appdir}/

%changelog
%autochangelog
