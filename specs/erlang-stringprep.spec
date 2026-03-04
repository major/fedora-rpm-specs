%global srcname stringprep
%global p1_utils_ver 1.0.28

Name: erlang-%{srcname}
Version: 1.0.33
Release: %autorelease
License: Apache-2.0 and TCL
Summary: A framework for preparing Unicode strings to help input and comparison
URL: https://github.com/processone/stringprep/
VCS: git:%{url}.git
Source0: %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
Provides: erlang-p1_stringprep = %{version}-%{release}
Obsoletes: erlang-p1_stringprep < 1.0.3
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: erlang-rebar3
BuildRequires: erlang-rebar3-pc
BuildRequires: erlang-p1_utils >= %{p1_utils_ver}
Requires: erlang-p1_utils >= %{p1_utils_ver}

%description
Stringprep is a framework for preparing Unicode test strings in order to
increase the likelihood that string input and string comparison work. The
principle are defined in RFC-3454: Preparation of Internationalized Strings.
This library is leverage Erlang native NIF mechanism to provide extremely fast
and efficient processing.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%build
%{erlang3_compile}

%install
%{erlang3_install}

install -d $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/priv/lib
install -pm755 priv/lib/* $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/priv/lib/

%check
%{erlang3_test}

%files
%license LICENSE.txt LICENSE.TCL LICENSE.ALL
%doc CHANGELOG.md
%doc README.md
%{erlang_appdir}

%changelog
%autochangelog
