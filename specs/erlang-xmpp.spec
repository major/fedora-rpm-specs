%global srcname xmpp

%global ezlib_ver 1.0.16
%global fast_tls_ver 1.1.26
%global fast_xml_ver 1.1.58
%global idna_ver 7.1.0
%global p1_utils_ver 1.0.29
%global stringprep_ver 1.0.34

Name:       erlang-%{srcname}
Version:    1.13.1
Release:    %autorelease
Summary:    Erlang/Elixir XMPP parsing and serialization library
License:    Apache-2.0
URL:        https://github.com/processone/xmpp/
VCS:        git:%{url}.git
Source0:    %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildRequires: erlang-ezlib >= %{ezlib_ver}
BuildRequires: erlang-fast_tls >= %{fast_tls_ver}
BuildRequires: erlang-fast_xml >= %{fast_xml_ver}
BuildRequires: erlang-idna >= %{idna_ver}
BuildRequires: erlang-p1_utils >= %{p1_utils_ver}
BuildRequires: erlang-provider_asn1
BuildRequires: erlang-rebar3
BuildRequires: erlang-rebar3-pc
BuildRequires: erlang-stringprep >= %{stringprep_ver}
BuildRequires: gcc
Requires: erlang-ezlib >= %{ezlib_ver}
Requires: erlang-fast_tls >= %{fast_tls_ver}
Requires: erlang-fast_xml >= %{fast_xml_ver}
Requires: erlang-idna >= %{idna_ver}
Requires: erlang-p1_utils >= %{p1_utils_ver}
Requires: erlang-stringprep >= %{stringprep_ver}

%description
XMPP is an Erlang XMPP parsing and serialization library, built on top of Fast
XML.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%build
%{erlang3_compile}

%install
%{erlang3_install}

install -p -D -m 755 priv/lib/* --target-directory=%{buildroot}%{erlang_appdir}/priv/lib/

%check
%{erlang3_test}

%files
%license LICENSE.txt
%doc CHANGELOG.md
%doc doc
%doc README.md
%{erlang_appdir}

%changelog
%autochangelog
