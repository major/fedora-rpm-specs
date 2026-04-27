%global realname jiffy

Name:           erlang-%{realname}
Version:        2.0.0
Release:        %autorelease
Summary:        Erlang JSON parser
# Main sources and tests are licensed under MIT.
# Bundled ryu is licensed under Apache-2.0 or BSL-1.0.
# Bundled fast_float is licensed under Apache-2.0 or BSL-1.0 or MIT.
# Yajl tests are licensed under BSD-3-Clause.
# Big List of Naughty Strings tests are licensed under MIT.
SourceLicense:  MIT AND BSD-3-Clause AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR BSL-1.0 OR MIT)
License:        MIT
URL:            https://github.com/davisp/%{realname}
VCS:            git:%{url}.git
Source0:        %{url}/archive/%{version}/%{realname}-%{version}.tar.gz
BuildRequires:  erlang-rebar3
BuildRequires:  erlang-rebar3-pc
BuildRequires:  gcc-c++
Provides:       bundled(ryu)
Provides:       bundled(fast_float)
Provides:       %{realname} = %{version}
Obsoletes:      %{realname} < %{version}

%description
A JSON parser for Erlang implemented as a NIF.

%prep
%autosetup -p 1 -n %{realname}-%{version}

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
