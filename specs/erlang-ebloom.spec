%global realname ebloom

Name:		erlang-%{realname}
Version:	2.1.0
Release:	%autorelease
Summary:	A NIF wrapper around a basic bloom filter
# c_src/bloom_filter.hpp and c_src/serialyzer.hpp are licensed under CPL
# and the rest of the sources are licensed under ASL 2.0
License:	Apache-2.0 AND CPL-1.0
URL:		https://github.com/basho/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{version}/%{realname}-%{version}.tar.gz
BuildRequires:	erlang-rebar3
BuildRequires:	erlang-rebar3-pc
BuildRequires:	gcc-c++

%description
%{summary}.

%prep
%autosetup -p1 -n %{realname}-%{version}

%build
%{erlang3_compile}

%install
%{erlang3_install}

%check
%{erlang3_test}

%files
%{erlang_appdir}/

%changelog
%autochangelog
