Name:           kefir
Version:        0.4.0
Release:        %{autorelease}
Summary:        An implementation of C17 language compiler from scratch

# Entire project is under GPL-3.0-only
# Except, runtime library which is under BSD-3-Clause
License:        GPL-3.0-only AND BSD-3-Clause
URL:            https://kefir.protopopov.lv
Source0:        %{url}/releases/kefir-%{version}.tar.gz
Source1:        %{url}/releases/kefir-0.4.0.tar.gz.asc
Source2:        https://www.protopopov.lv/static/files/jprotopopov.gpg 

BuildRequires:  binutils
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  groff
BuildRequires:  m4
BuildRequires:  make
BuildRequires:  mandoc
# Needed for tests
BuildRequires:  libatomic
# Only compiles for x86_64
ExclusiveArch:  x86_64

%description
an implementation of C17 language compiler from scratch. No existing open
source compiler infrastructure is being reused. The main priority is
self-sufficiency of the project, compatibility with platform ABI and
compliance with C17 language standard. Any omissions or incompatibilities
between the language standard and Kefir behavior which are not explicitly
documented (see Implementation & Usage quirks section below) shall be
considered bugs.

Kefir supports modern x86-64 Linux, FreeBSD, OpenBSD and NetBSD environments
(see Supported environments section below). Compiler is also able to produce
JSON streams containing program representation on various stages of
compilation (tokens, AST, IR), as well as printing source code in preprocessed
form. The compiler targets GNU As (Intel syntax with/without prefixes and ATT
syntax are supported) and Yasm assemblers. Kefir is able to produce debug
information in DWARF5 format for GNU As. Position-independent code generation
is supported. Kefir features cc-compatible command line interface.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -c -n %{name}-%{version}

%build
LC_ALL=C.UTF-8 %make_build all \
    PROFILE=reldebug \
    CC=gcc \
    DESTDIR=%{buildroot} \
    prefix=%{_prefix} \
    libdir=%{_libdir} \
    sysconfdir=%{_sysconfdir}

%install
%make_install \
    prefix=%{_prefix} \
    libdir=%{_libdir} \
    sysconfdir=%{_sysconfdir}

rm -fr %{buildroot}%{_datadir}/licenses

%check
make test

%files
%license source/runtime/LICENSE
%license COPYING
%doc CHANGELOG
%doc README.md
%{_bindir}/kefir
%{_bindir}/kefir-cc
%{_bindir}/kefir-cc1
%{_bindir}/kefir-detect-host-env
%{_mandir}/man1/kefir.1.*
%{_mandir}/man1/kefir-cc1.1.*
%{_mandir}/man1/kefir-detect-host-env.1.*
%{_sysconfdir}/kefir.local
%{_includedir}/kefir
%{_libdir}/libkefir.so
%{_libdir}/libkefir.so.0.0
%{_libdir}/libkefir.a
%{_libdir}/libkefirrt.a

%changelog
%autochangelog
