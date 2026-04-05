%global realname rebar

# Bootstrapping
%global bootstrap 0

Name:     erlang-%{realname}3
Version:  3.27.0
Release:  %autorelease
Summary:  Tool for working with Erlang projects
License:  Apache-2.0 and MIT
URL:      https://github.com/erlang/%{realname}3
VCS:      git:%{url}.git
Source0:  %{url}/archive/%{version}/%{realname}3-%{version}.tar.gz
Source1:  rebar3.sh
Patch:    erlang-rebar3-0001-Skip-deps.patch
Patch:    erlang-rebar3-0002-Unbundle-hex_core-ver.-0.7.1.patch
Patch:    erlang-rebar3-0003-WIP-ignore-deps-on-demand.patch
Patch:    erlang-rebar3-0004-WIP-prefer-locally-installed-plugins.patch
Patch:    erlang-rebar3-0005-WIP-don-t-update-packages-if-IGNORE_MISSING_DEPS-is-.patch
Patch:    erlang-rebar3-0006-Adjust-for-hex_code-ver.-0.15.patch
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

# This one cannot be picked up automatically
Requires:	erlang-cth_readable
# This one cannot be picked up automatically
Requires:	erlang-eunit_formatters

Requires:	erlang-rpm-macros >= 0.3.6

%description
Rebar3 is an Erlang tool that makes it easy to create, develop, and release
Erlang libraries, applications, and systems in a repeatable manner.

%prep
%autosetup -p1 -n %{realname}3-%{version}

%build
ebin_paths=$(perl -e 'print join(":", grep { !/rebar/} (glob("%{_libdir}/erlang/lib/*/ebin"), glob("%{_datadir}/erlang/lib/*/ebin")))')

%if 0%{?bootstrap}
DIAGNOSTIC=1 ./bootstrap bare compile --paths $ebin_paths --separator :
%else
rm -rf ./vendor
DEBUG=1 %{realname}3 bare compile --paths $ebin_paths --separator :
%endif

%install
# Install rebar script itself
install -D -p -m 0755 %{SOURCE1} %{buildroot}%{_bindir}/rebar3

mkdir -p %{buildroot}%{_datadir}/erlang/lib/%{realname}-%{version}/ebin/
%if 0%{?bootstrap}
install -p -m644 _build/bootstrap/lib/rebar/ebin/*.beam %{buildroot}%{_datadir}/erlang/lib/%{realname}-%{version}/ebin/
install -p -m644 _build/bootstrap/lib/rebar/ebin/%{realname}.app %{buildroot}%{_datadir}/erlang/lib/%{realname}-%{version}/ebin/
%else
install -p -m644 ./ebin/*.beam %{buildroot}%{_datadir}/erlang/lib/%{realname}-%{version}/ebin/
install -p -m644 ./ebin/%{realname}.app %{buildroot}%{_datadir}/erlang/lib/%{realname}-%{version}/ebin/
%endif

# Copy templates folder
mkdir -p %{buildroot}%{_erllibdir}/%{realname}-%{version}/priv
cp -a apps/rebar/priv/templates/ %{buildroot}%{_erllibdir}/%{realname}-%{version}/priv/templates

# Install shell-completion scripts
install -D -p -m644 ./apps/rebar/priv/shell-completion/bash/%{realname}3 %{buildroot}%{bash_completions_dir}/%{realname}3
install -D -p -m644 ./apps/rebar/priv/shell-completion/fish/%{realname}3.fish %{buildroot}%{fish_completions_dir}/%{realname}3.fish
install -D -p -m644 ./apps/rebar/priv/shell-completion/zsh/_%{realname}3 %{buildroot}%{zsh_completions_dir}/_%{realname}3

mkdir -p %{buildroot}%{_mandir}/man1/
install -p -m644 manpages/%{realname}3.1 %{buildroot}%{_mandir}/man1/

%files
%license LICENSE
%doc README.md rebar.config.sample THANKS
%{_bindir}/%{realname}3
# Requires Erlang/OTP 27, guarded, safe to ignore.
# ERROR: Cant find json:encode/1 while processing '.../ebin/rebar_prv_manifest.beam'
# Requires older error_logger, guarded, safe to ignore.
# ERROR: Cant find error_logger:swap_handler/1 while processing '.../ebin/rebar_prv_shell.beam'
%{_datadir}/erlang/lib/%{realname}-%{version}
%{_mandir}/man1/%{realname}3.1*
%{bash_completions_dir}/%{realname}3
%{fish_completions_dir}/%{realname}3.fish
%{zsh_completions_dir}/_%{realname}3

%changelog
%autochangelog
