# Testsuite needs root-privileges.
%bcond_with     testsuite


Name:           checksec
Version:        2.6.0
Release:        %autorelease
Summary:        Tool to check system for binary-hardening

License:        BSD
URL:            https://github.com/slimm609/%{name}.sh
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         0001-Fix-compatibility-with-binutils-2.41-on-ppc64le.patch

BuildArch:      noarch

%if %{with testsuite}
BuildRequires:  binutils
BuildRequires:  file
BuildRequires:  findutils
BuildRequires:  gawk
BuildRequires:  libxml2
BuildRequires:  openssl
BuildRequires:  procps-ng
%if 0%{?fedora} || 0%{?rhel} >= 6
BuildRequires:  %{_bindir}/jsonlint
%endif
%endif

Requires:       binutils
Requires:       file
Requires:       findutils
Requires:       gawk
Requires:       which
Requires:       /usr/bin/nm

%description
Modern Linux distributions offer some mitigation techniques to make it harder
to exploit software vulnerabilities reliably. Mitigations such as RELRO,
NoExecute (NX), Stack Canaries, Address Space Layout Randomization (ASLR) and
Position Independent Executables (PIE) have made reliably exploiting any
vulnerabilities that do exist far more challenging. The checksec script is
designed to test what *standard* Linux OS and PaX (http://pax.grsecurity.net/)
security features are being used.

As of version 1.3 the script also lists the status of various Linux kernel
protection mechanisms.

%{name} can check binary-files and running processes for hardening features.


%prep
%autosetup -n %{name}.sh-%{version} -p 1

# Fix shebang.
sed -i 's~^#!/usr/bin/env bash~#!/usr/bin/bash~' checksec

# Disable --update command.
sed -i 's/pkg_release=false/pkg_release=true/' checksec


%build
# noop


%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man1
install -pm 0755 %{name} %{buildroot}%{_bindir}
install -pm 0644 extras/man/%{name}.1 %{buildroot}%{_mandir}/man1


%if %{with testsuite}
%check
pushd tests
./xml-checks.sh || exit 2
%if 0%{?fedora} || 0%{?rhel} >= 6
./json-checks.sh || exit 2
%endif
popd
%endif


%files
%license LICENSE.txt
%doc ChangeLog README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
%autochangelog
