# Copyright (C) 2023 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

Name:          openssl-pkcs11-sign-provider
Version:       1.0.1
Release:       %autorelease
Summary:       A PKCS#11 provider for OpenSSL 3.0 (private key operations only)
License:       Apache-2.0
URL:           https://github.com/opencryptoki/%{name}
Source0:       %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz

Requires:      openssl >= 3.0.8

BuildRequires: openssl-devel >= 3.0.8
BuildRequires: opencryptoki-devel >= 3.17.0
BuildRequires: gcc
BuildRequires: g++
BuildRequires: autoconf-archive
BuildRequires: automake
BuildRequires: libtool
# for test
BuildRequires: openssl >= 3.0.8
BuildRequires: gnutls-utils
BuildRequires: sed
BuildRequires: opencryptoki >= 3.17.0

%description
This package contains a provider module for OpenSSL 3.0, interfacing to
PKCS#11 for operations with private keys in PKCS#11 tokens.

%global modulesdir %(pkg-config --variable=modulesdir libcrypto)

%prep
%autosetup

%build
%configure --libdir=%{modulesdir}
%make_build
for file in openssl-*.cnf.sample; do mv $file $file.%{_arch}; done

%check
# Uncomment the following line to enable checks during package build.
# Note: for test-module ock, a working opencryptoki and p11-kit setup
# is required for testing.
# make check

%install
%make_install

%files
%license COPYING
%doc README.md openssl-*.cnf.sample.%{_arch}
%{modulesdir}/pkcs11sign.so
%{_mandir}/man5/pkcs11sign.cnf.5*
%{_mandir}/man7/pkcs11sign.7*

%changelog
%autochangelog
