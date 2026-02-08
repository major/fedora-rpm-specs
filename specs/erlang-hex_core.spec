%global realname hex_core

Name:     erlang-%{realname}
Version:  0.12.0
Release:  %autorelease
Summary:  Reference implementation of Hex specifications
License:  Apache-2.0
URL:      https://github.com/hexpm/%{realname}
VCS:      git:%{url}.git
Source0:  %{url}/archive/v%{version}/%{realname}-%{version}.tar.gz
Patch:    erlang-hex_core-0001-Disable-non-deterministic-tarball-checksum-tests.patch
BuildArch:     noarch
BuildRequires: erlang-gpb
BuildRequires: erlang-proper
BuildRequires: erlang-rebar3
BuildRequires: erlang-rebar3-gpb

%description
%{summary}.

%prep
%autosetup -p1 -n %{realname}-%{version}

%build
{%erlang3_compile}

%install
%{erlang3_install}

%check
%{erlang3_test}

%files
%license LICENSE
%doc README.md examples/
%{erlang_appdir}/

%changelog
%autochangelog
