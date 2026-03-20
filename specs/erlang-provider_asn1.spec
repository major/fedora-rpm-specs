%global srcname provider_asn1

Name: erlang-%{srcname}
Version: 0.4.1
Release: %autorelease
BuildArch: noarch
License: MIT
Summary: Compile ASN.1 with Rebar3
URL: https://github.com/knusbaum/provider_asn1
VCS: git:%{url}.git
Source0: %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildRequires: erlang-rebar3

%description
%{summary}.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%build
%{erlang3_compile}

%install
%{erlang3_install}

%check
%{erlang3_test}

%files
%license LICENSE
%doc README.md
%{erlang_appdir}

%changelog
%autochangelog
