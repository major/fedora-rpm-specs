%global realname ranch

Name:		erlang-%{realname}
Version:	2.2.0
Release:	%autorelease
BuildArch:	noarch
Summary:	Socket acceptor pool for TCP protocols
License:	ISC
URL:		https://github.com/ninenines/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch:		erlang-ranch-0001-Fix-testing-with-rebar.patch
Patch:		erlang-ranch-0002-Don-t-care-about-return-value.patch
BuildRequires:	erlang-ct_helper
BuildRequires:	erlang-rebar3

%description
%{summary}.

%prep
%autosetup -p1 -n %{realname}-%{version}
# FIXME we don't have stampede yet
rm -f test/stampede_SUITE.erl
# FIXME this test is very fragile and cannot be run with Rebar3 directly
rm -f test/upgrade_SUITE.erl

%build
%{erlang3_compile}

%install
%{erlang3_install}

%check
%{erlang3_test}

%files
%license LICENSE
%doc README.asciidoc doc/ examples/
%{erlang_appdir}/

%changelog
%autochangelog
