Name:    testssl
Version: 3.2~rc3
%global ver 3.2rc3
Release: %autorelease

Summary: Testing TLS/SSL encryption
License: GPL-2.0-only
URL:     https://testssl.sh/
Source0: https://github.com/drwetter/testssl.sh/archive/refs/tags/v%{ver}.tar.gz

BuildArch: noarch

BuildRequires: coreutils
BuildRequires: sed

Requires: bash
# dig, host, nslookup
Requires: bind-utils
# /etc/pki/tls
Requires: ca-certificates
Requires: coreutils
Requires: gawk
# locale
Requires: glibc-common
Requires: grep
Requires: hostname
# tput
Requires: ncurses
Requires: openssl >= 1
# ps
Requires: procps-ng
Requires: sed
# hexdump, kill
Requires: util-linux

%description
testssl.sh is a free command line tool which checks a server's service on any
port for the support of TLS/SSL ciphers, protocols as well as recent
cryptographic flaws and more.

%prep
%autosetup -n %{name}.sh-%{ver}
sed --in-place '1s#^\#!/usr/bin/env bash$#\#!/bin/bash#' %{name}.sh etc/client-simulation.txt
sed --in-place 's#^TESTSSL_INSTALL_DIR=.*$#TESTSSL_INSTALL_DIR="%{_datadir}/%{name}"#' %{name}.sh
sed --in-place 's#^CA_BUNDLES_PATH=.*$#CA_BUNDLES_PATH="/etc/pki/tls"#' %{name}.sh
sed --in-place '0,/.SH "COPYRIGHT"/s#testssl\\.sh#testssl#g' doc/%{name}.1

%build

%install
install -D --preserve-timestamps %{name}.sh %{buildroot}%{_bindir}/%{name}

for file in ca_hashes.txt cipher-mapping.txt client-simulation.txt common-primes.txt tls_data.txt README.md
do
        install -D --preserve-timestamps --mode=0644 etc/${file} %{buildroot}%{_datadir}/%{name}/etc/${file}
done

install -d %{buildroot}%{_mandir}/man1
install -m 644 doc/%{name}.1 %{buildroot}%{_mandir}/man1/

%files
%doc CHANGELOG.md Readme.md
%license LICENSE
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/testssl.1*

%changelog
%autochangelog
