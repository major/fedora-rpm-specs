%global realname gpb

Name:		erlang-%{realname}
Version:	4.21.3
Release:	%autorelease
BuildArch:	noarch
Summary:	A Google Protobuf implementation for Erlang
# Source code licensed under LGPL-2.1-or-later, data files in ./priv directory
# are licensed under BSD-3-Clause
License:	LGPL-2.1-or-later AND BSD-3-Clause
URL:		https://github.com/tomas-abrahamsson/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{version}/%{realname}-%{version}.tar.gz
Source1:	protoc-erl
BuildRequires:	erlang-rebar3
Obsoletes:	erlang-protobuffs < 0.9.3
Provides:	erlang-protobuffs = %{version}-%{release}

%description
%{summary}.

%prep
%autosetup -p1 -n %{realname}-%{version}
echo "%{version}" > gpb.vsn

%build
%{erlang3_compile}

%install
%{erlang3_install}
# Install Erlang protobuf compiler script
install -D -p -m 0755 %{SOURCE1} %{buildroot}%{_bindir}/protoc-erl
# Install useful definitions
cp -arv priv/ %{buildroot}%{erlang_appdir}/

%check
%{erlang3_test}

%files
%license COPYING.LIB
%doc README.md README.nif-cc doc/dev-guide/*.md
%{_bindir}/protoc-erl
%{erlang_appdir}/

%changelog
%autochangelog
