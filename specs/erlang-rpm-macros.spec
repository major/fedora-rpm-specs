Name:		erlang-rpm-macros
Version:	0.3.9
Release:	%autorelease
Summary:	Macros for simplifying building of Erlang packages
License:	MIT
URL:		https://github.com/fedora-erlang/erlang-rpm-macros
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:	noarch
# These BRs needed only for testing
BuildRequires:	erlang-crypto
BuildRequires:	erlang-erlsyslog
BuildRequires:	erlang-erts
BuildRequires:	make
BuildRequires:	python3-pybeam
BuildRequires:	python3-pyelftools
BuildRequires:	python3-rpm
Requires:	erlang-rebar3
Requires:	rpm-build >= 4.11
# Requires for BEAM parsing
Requires:	python3-pybeam
# Requires for so-lib parsing
Requires:	python3-pyelftools
Requires:	python3-rpm

%description
Macros for simplifying building of Erlang packages.

%prep
%autosetup -p1

%build
# Nothing to build

%install
install -d %{buildroot}%{_rpmconfigdir}/fileattrs
install -d %{buildroot}%{_rpmconfigdir}/macros.d
install -p -m 0755 erlang-find-provides.py %{buildroot}%{_rpmconfigdir}/erlang-find-provides
install -p -m 0755 erlang-find-requires.py %{buildroot}%{_rpmconfigdir}/erlang-find-requires
install -p -m 0644 macros.erlang %{buildroot}%{_rpmconfigdir}/macros.d/
install -p -m 0644 erlang.attr %{buildroot}%{_rpmconfigdir}/fileattrs/

%check
make check

%files
%license LICENSE
%doc README
%{_rpmconfigdir}/erlang-find-provides
%{_rpmconfigdir}/erlang-find-requires
%{_rpmconfigdir}/fileattrs/erlang.attr
%{_rpmconfigdir}/macros.d/macros.erlang

%changelog
%autochangelog
