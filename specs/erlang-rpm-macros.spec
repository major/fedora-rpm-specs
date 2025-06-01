Name:		erlang-rpm-macros
Version:	0.3.10
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
Requires:       (erlang-srpm-macros = %{?epoch:%{epoch}:}%{version}-%{release} if erlang-srpm-macros)
Requires:	erlang-rebar3
Requires:	rpm-build >= 4.11
# Requires for BEAM parsing
Requires:	python3-pybeam
# Requires for so-lib parsing
Requires:	python3-pyelftools
Requires:	python3-rpm

%description
Macros for simplifying building of Erlang packages.

%package -n erlang-srpm-macros
Summary:        Minimal implementation of buildrequires
Requires:       (erlang-rpm-macros = %{?epoch:%{epoch}:}%{version}-%{release} if erlang-rpm-macros)
Requires:       (rpm-build >= 4.14.90 if rpm-build)

%description -n erlang-srpm-macros
This package contains a minimal implementation of buildrequires. When used in
%%generate_buildrequires, it will generate BuildRequires for erang-rpm-macros.
When both packages are installed, the full version takes precedence.

%prep
%autosetup -p1

%build
# Nothing to build

%install
install -d %{buildroot}%{_rpmconfigdir}/fileattrs
install -d %{buildroot}%{_rpmconfigdir}/macros.d
install -p -m 0755 erlang-find-provides.py %{buildroot}%{_rpmconfigdir}/erlang-find-provides
install -p -m 0755 erlang-find-requires.py %{buildroot}%{_rpmconfigdir}/erlang-find-requires
install -p -m 0644 macros.aaa-erlang-srpm %{buildroot}%{_rpmmacrodir}/
install -p -m 0644 macros.erlang %{buildroot}%{_rpmmacrodir}/
install -p -m 0644 erlang.attr %{buildroot}%{_rpmconfigdir}/fileattrs/

%check
make check

%files
%license LICENSE
%doc README
%{_rpmconfigdir}/erlang-find-provides
%{_rpmconfigdir}/erlang-find-requires
%{_rpmconfigdir}/fileattrs/erlang.attr
%{_rpmmacrodir}/macros.erlang

%files -n erlang-srpm-macros
%license LICENSE
%{_rpmmacrodir}/macros.aaa-erlang-srpm

%changelog
%autochangelog
