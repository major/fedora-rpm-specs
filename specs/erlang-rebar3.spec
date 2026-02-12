%global realname rebar3
%global otp_app_name rebar

# Bootstrapping
%global bootstrap 1

Name:     erlang-%{realname}
Version:  3.26.0
Release:  %autorelease
Summary:  Tool for working with Erlang projects
License:  Apache-2.0 and MIT
URL:      https://github.com/erlang/%{realname}
VCS:      git:%{url}.git
Source0:  %{url}/archive/%{version}/%{realname}-%{version}.tar.gz
Source1:  rebar3.escript
Patch:    erlang-rebar3-0001-Skip-deps.patch
Patch:    erlang-rebar3-0002-Unbundle-hex_core-ver.-0.7.1.patch
Patch:    erlang-rebar3-0003-WIP-ignore-deps-on-demand.patch
Patch:    erlang-rebar3-0004-WIP-prefer-locally-installed-plugins.patch
Patch:    erlang-rebar3-0005-WIP-don-t-update-packages-if-IGNORE_MISSING_DEPS-is-.patch
%if 0%{?bootstrap}
# noop
%else
BuildRequires:  erlang-rebar3
%endif

BuildArch: noarch
BuildRequires:  erlang-bbmustache
BuildRequires:  erlang-certifi
BuildRequires:  erlang-cf
BuildRequires:  erlang-cth_readable
BuildRequires:  erlang-dialyzer
BuildRequires:  erlang-edoc
BuildRequires:  erlang-erl_interface
BuildRequires:  erlang-erlware_commons
BuildRequires:  erlang-erts
BuildRequires:  erlang-eunit_formatters
BuildRequires:  erlang-getopt
BuildRequires:  erlang-hex_core
BuildRequires:  erlang-parsetools
BuildRequires:  erlang-providers
BuildRequires:  erlang-relx
BuildRequires:  erlang-rpm-macros
BuildRequires:  erlang-ssl_verify_fun
BuildRequires:  perl-interpreter

# FIXME wip
#Requires:	erlang-abnfc
#Requires:	erlang-gpb

# This one cannot be picked up automatically
Requires:	erlang-cth_readable
# Requires for port compiling - no direct references in Rebar's src/*.erl files
Requires:	erlang-erl_interface
# This one cannot be picked up automatically
Requires:	erlang-eunit_formatters

Requires:	erlang-rpm-macros >= 0.3.6

%description
Rebar3 is an Erlang tool that makes it easy to create, develop, and release
Erlang libraries, applications, and systems in a repeatable manner.

%prep
%autosetup -p1 -n %{realname}-%{version}
# Remove bundled hex_core v. 0.10.1
rm -rf apps/rebar/src/vendored/

%build
ebin_paths=$(perl -e 'print join(":", grep { !/rebar/} (glob("%{_libdir}/erlang/lib/*/ebin"), glob("%{_datadir}/erlang/lib/*/ebin")))')

%if 0%{?bootstrap}
DIAGNOSTIC=1 ./bootstrap bare compile --paths $ebin_paths --separator :
%else
DEBUG=1 %{realname} bare compile --paths $ebin_paths --separator :
%endif

%install
# Install rebar script itself
install -D -p -m 0755 %{SOURCE1} %{buildroot}%{_bindir}/rebar3

mkdir -p %{buildroot}%{_datadir}/erlang/lib/%{realname}-%{version}/ebin/
install -p -m644 _build/bootstrap/lib/rebar/ebin/*.beam %{buildroot}%{_datadir}/erlang/lib/%{realname}-%{version}/ebin/
install -p -m644 _build/bootstrap/lib/rebar/ebin/%{otp_app_name}.app %{buildroot}%{_datadir}/erlang/lib/%{realname}-%{version}/ebin/

# Copy the contents of priv folder
cp -a apps/rebar/priv %{buildroot}%{_erllibdir}/%{realname}-%{version}/

mkdir -p %{buildroot}%{_mandir}/man1/
install -p -m644 manpages/%{realname}.1 %{buildroot}%{_mandir}/man1/

%files
%license LICENSE
%doc README.md rebar.config.sample THANKS
%{_bindir}/%{realname}
%{_datadir}/erlang/lib/%{realname}-%{version}
%{_mandir}/man1/%{realname}.1*

%changelog
%autochangelog
