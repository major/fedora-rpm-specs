%global srcname base64url


Name:      erlang-%{srcname}
Version:   1.0.1
Release:   %autorelease
BuildArch: noarch

License: MIT
Summary: URL safe base64-compatible codec
URL: https://github.com/dvv/%{srcname}
Source0: %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires: erlang-rebar3


%description
Standalone URL safe base64-compatible codec.


%prep
%autosetup -n %{srcname}-%{version}


%build
%{erlang3_compile}


%check
%{erlang3_test}


%install
%{erlang3_install}


%files
%license LICENSE.txt
%doc README.md
%{erlang_appdir}


%changelog
%autochangelog