%global realname ebloom

Name:		erlang-%{realname}
Version:	2.1.0
Release:	%autorelease
Summary:	A NIF wrapper around a basic bloom filter
# c_src/bloom_filter.hpp is licensed under CPL 1.0,
# the rest of the sources are licensed under ASL 2.0
License:	Apache-2.0 AND CPL-1.0
URL:		https://github.com/basho/%{realname}
VCS:		git:%{url}.git
Source:		%{url}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch:		erlang-ebloom-0001-bloom_filter-replace-custom-serializer-with-portable.patch
Patch:		erlang-ebloom-0002-Drop-compat-script.patch
BuildRequires:	erlang-rebar3-pc
BuildRequires:	gcc-c++
BuildSystem:	rebar3

%description
%{summary}.

%files
%{erlang_appdir}/

%changelog
%autochangelog
