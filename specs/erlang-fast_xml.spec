%global srcname fast_xml
%global p1_utils_ver 1.0.29

Name: erlang-%{srcname}
Version: 1.1.58
Release: %autorelease
License: Apache-2.0
Summary: Fast Expat based Erlang XML parsing and manipulation library
URL:     https://github.com/processone/%{srcname}
VCS:     git:%{url}.git
Source0: %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
Provides:  erlang-p1_xml = %{version}-%{release}
Obsoletes: erlang-p1_xml < 1.1.11
BuildRequires: erlang-edoc
BuildRequires: erlang-p1_utils >= %{p1_utils_ver}
BuildRequires: erlang-rebar3
BuildRequires: erlang-rebar3-pc
BuildRequires: expat-devel
BuildRequires: gcc

%description
Fast Expat based Erlang XML parsing and manipulation library, with a strong
focus on XML stream parsing from network. It supports full XML structure
parsing, suitable for small but complete XML chunks, and XML stream parsing
suitable for large XML document, or infinite network XML stream like XMPP.
This module can parse files much faster than built-in module xmerl. Depending
on file complexity and size xml_stream:parse_element/1 can be 8-18 times faster
than calling xmerl_scan:string/2.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%build
%{erlang3_compile}

%install
%{erlang3_install}
install -p -D -m 755 priv/lib/* --target-directory=$RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/priv/lib/

%check
%{erlang3_test}

%files
%license LICENSE.txt
%doc CHANGELOG.md README.md
%{erlang_appdir}

%changelog
%autochangelog
