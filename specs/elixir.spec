%global upstream elixir-lang
%global debug_package %{nil}

Name:     elixir
Version:  1.18.2

%global __requires_exclude_from ^%{_datadir}/%{name}/%{version}/bin/.+\\.ps1$

Release:  %autorelease
Summary:  A modern approach to programming for the Erlang VM
License:  Apache-2.0
URL:      https://elixir-lang.org/
VCS:      git:https://github.com/%{upstream}/%{realname}.git
Source0:  https://github.com/%{upstream}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:  https://github.com/%{upstream}/%{name}/releases/download/v%{version}/Docs.zip#/%{name}-%{version}-doc.zip
# See https://bugzilla.redhat.com/1470583
#BuildArch:      noarch
BuildRequires: erlang-compiler
BuildRequires: erlang-crypto
BuildRequires: erlang-dialyzer
%ifarch %{java_arches}
# Requires for unit-testing but not strictly necessary for anything else
# https://gitlab.alpinelinux.org/alpine/aports/-/issues/15654
BuildRequires: erlang-doc
%endif
BuildRequires: erlang-erts
BuildRequires: erlang-eunit
BuildRequires: erlang-inets
BuildRequires: erlang-kernel
BuildRequires: erlang-parsetools
BuildRequires: erlang-public_key
BuildRequires: erlang-rebar3
BuildRequires: erlang-sasl
BuildRequires: erlang-stdlib
BuildRequires: erlang-tools
BuildRequires: erlang-xmerl
BuildRequires: git
BuildRequires: sed
BuildRequires: make
%ifarch %{java_arches}
# Requires for unit-testing but not strictly necessary for anything else
# https://gitlab.alpinelinux.org/alpine/aports/-/issues/15654
Recommends: erlang-doc
%endif


%description
Elixir is a programming language built on top of the Erlang VM.
As Erlang, it is a functional language built to support distributed,
fault-tolerant, non-stop applications with hot code swapping.

%prep
# Unpack the HTML documentation (Source1)
%setup -q -T -c -n %{name}-%{version}/docs -a 1
find -name ".build" -exec rm \{\} \;

# Unpack elixir itself (Source0)
%autosetup -p1 -D

# Remove windows-specific scripts
find -name '*.bat' -exec rm \{\} \;

# This contains a failing test. We want `make test` for most tests, but
# this deals with ANSI codes which rpmbuild strips.
rm lib/elixir/test/elixir/io/ansi_test.exs

# Remove VCS-specific files
find . -name .gitignore -delete
find . -name .gitkeep -delete

# Let the Makefile speak!
sed -i '/^Q\s*:=/d' Makefile

%build
# No nonger necessary starting from RPM 4.20.
# https://github.com/rpm-software-management/rpm/pull/2616
export LANG=C.UTF-8
export REBAR3=/usr/bin/rebar3
export ERL_LIBS=/usr/share/erlang/lib/
make compile
make build_man

%check

# Remove vendored rebar3, as it is provided by the erlang-rebar3 package.
rm -f ./lib/mix/test/fixtures/rebar3
export REBAR3=/usr/bin/rebar3

# No nonger necessary starting from RPM 4.20.
# https://github.com/rpm-software-management/rpm/pull/2616
export LANG=C.UTF-8
export ERL_LIBS=/usr/share/erlang/lib/
make test

%install
mkdir -p %{buildroot}/%{_datadir}/%{name}/%{version}
cp -ra bin lib %{buildroot}/%{_datadir}/%{name}/%{version}

mkdir -p %{buildroot}/%{_bindir}
ln -s %{_datadir}/%{name}/%{version}/bin/{elixir,elixirc,iex,mix} %{buildroot}/%{_bindir}/

# Manual pages
mkdir -p %{buildroot}/%{_mandir}/man1
cp -a man/elixir.1 man/elixirc.1 man/iex.1 man/mix.1 %{buildroot}/%{_mandir}/man1

%files
%license LICENSE
%{_bindir}/elixir
%{_bindir}/elixirc
%{_bindir}/iex
%{_bindir}/mix
%{_datadir}/%{name}
%{_mandir}/man1/elixir.1*
%{_mandir}/man1/elixirc.1*
%{_mandir}/man1/iex.1*
%{_mandir}/man1/mix.1*

%package doc
Summary: Documentation for the elixir language and tools

%description doc
HTML documentation for eex, elixir, iex, logger and mix.

%files doc
%license docs/LICENSE
%doc docs/doc/eex docs/doc/elixir docs/doc/iex docs/doc/logger docs/doc/mix

%changelog
%autochangelog
