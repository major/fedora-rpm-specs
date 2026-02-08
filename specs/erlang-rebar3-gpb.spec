%global realname rebar3_gpb_plugin

Name:		erlang-rebar3-gpb
Version:	2.23.6
Release:	%autorelease
Summary:	A protobuf compiler for Rebar3
License:	MIT
URL:		https://github.com/lrascao/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{version}/%{realname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	erlang-gpb
BuildRequires:	erlang-rebar3

%description
A Rebar3 plugin for automatically compiling .proto files using the gpb protobuf
compiler.

%prep
%autosetup -p1 -n %{realname}-%{version}

%build
%{erlang3_compile}

%check
%{erlang3_test}

%install
%{erlang3_install}

%files
%license LICENSE
%doc README.md
%{erlang_appdir}

%changelog
%autochangelog
