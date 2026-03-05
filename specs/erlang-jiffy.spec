%global realname jiffy

Name:           erlang-%{realname}
Version:        1.1.3
Release:        %autorelease
Summary:        Erlang JSON parser
# Main sources are licensed under MIT, double-conversion is licensed under
# BSD-3-Clause, test files are licensed under BSD-3-Clause-Modification
SourceLicense:  MIT AND BSD-3-Clause AND BSD-3-Clause-Modification
License:        MIT
URL:            https://github.com/davisp/%{realname}
VCS:            git:%{url}.git
Source0:        %{url}/archive/%{version}/%{realname}-%{version}.tar.gz
# Use double conversion from the system instead of the bundled one
Patch:          erlang-jiffy-0001-Use-double-conversion-from-the-system.patch
BuildRequires:  double-conversion-devel
BuildRequires:  erlang-rebar3
BuildRequires:  erlang-rebar3-pc
BuildRequires:  gcc-c++
Provides:       %{realname} = %{version}
Obsoletes:      %{realname} < %{version}

%description
A JSON parser for Erlang implemented as a NIF.

%prep
%autosetup -p 1 -n %{realname}-%{version}
# Use double conversion from the system instead of the bundled one
rm -r c_src/double-conversion

%build
%{erlang3_compile}

%install
%{erlang3_install}

%check
%{erlang3_test}

%files
%doc README.md
%license LICENSE
%{erlang_appdir}/

%changelog
%autochangelog
