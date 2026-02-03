%global realname meck

Name:		erlang-%{realname}
Version:	1.1.0
Release:	%autorelease
BuildArch:	noarch
Summary:	A mocking library for Erlang
License:	Apache-2.0
URL:		https://github.com/eproxus/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/v%{version}/%{realname}-%{version}.tar.gz
Patch:		erlang-meck-0001-Disable-erlang-unite-test-output-highlighting.patch
Patch:		erlang-meck-0002-Temporary-disable-ex_doc-and-rebar3_ex_doc.patch
Patch:		erlang-meck-0003-Fix-tests-with-short-domain-names-default.patch
BuildRequires:	erlang-hamcrest
BuildRequires:	erlang-rebar3
# WARNING this library calls to unexported cover:compile_beam/2,
# cover:get_term/1, cover:write/2. It's intentional - it replaces all calls to
# `cover` module with the `pproxy` module with slightly different API.
BuildRequires:	erlang-tools

%description
With meck you can easily mock modules in Erlang. Since meck is intended to be
used in testing, you can also perform some basic validations on the mocked
modules, such as making sure no function is called in a way it should not.

%prep
%autosetup -p1 -n %{realname}-%{version}

%build
%{erlang3_compile}

%install
%{erlang3_install}

%check
%{erlang3_test}

%files
%license LICENSE
%doc README.md NOTICE
%{erlang_appdir}/

%changelog
%autochangelog
