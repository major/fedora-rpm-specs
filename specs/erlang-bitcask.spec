%global realname bitcask

Name:		erlang-%{realname}
Version:	2.1.0
Release:	%autorelease
Summary:	Eric Brewer-inspired key/value store
License:	Apache-2.0
URL:		https://github.com/basho/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{version}/%{realname}-%{version}.tar.gz
Source1:	bitcask.licensing
Patch:		erlang-bitcask-0001-Don-t-use-deprecated-erlang-now-0.patch
Patch:		erlang-bitcask-0004-Fix-32-bit-portability-issues-in-NIF-code.patch
BuildRequires:	erlang-cuttlefish
BuildRequires:	erlang-meck
BuildRequires:	erlang-rebar3-eqc
BuildRequires:	erlang-rebar3-pc
BuildRequires:	gcc
BuildSystem:	rebar3

%description
%{summary}.

%install -a
cp -arv priv/bitcask.schema %{buildroot}%{erlang_appdir}/priv
cp -arv priv/bitcask_multi.schema %{buildroot}%{erlang_appdir}/priv

%files
%doc README.md THANKS doc/
%{erlang_appdir}/

%changelog
%autochangelog
