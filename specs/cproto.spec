Summary: Generates function prototypes and variable declarations from C code
Name: cproto
Version: 4.8a
Release: %autorelease
License: LicenseRef-Fedora-Public-Domain
Source0: https://invisible-island.net/archives/cproto/cproto-%{version}.tgz
Source1: https://invisible-island.net/archives/cproto/cproto-%{version}.tgz.asc
# Thomas Dickey's GPG public key, retrieved from https://invisible-island.net/public/dickey@invisible-island.net-rsa3072.asc
Source2: dickey-invisible-island.net-rsa3072.asc
URL: https://invisible-island.net/cproto/
BuildRequires: byacc
BuildRequires: flex
BuildRequires: gcc-c++
BuildRequires: gpgverify
BuildRequires: make

%description
Cproto generates function prototypes and variable declarations from C
source code. Cproto can also convert function definitions between the
old style and the ANSI C style. This conversion will overwrite the
original files, however, so be sure to make a backup copy of your
original files in case something goes wrong. Cproto uses a Yacc
generated parser, so it should not be confused by complex function
definitions as much as other prototype generators.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%configure
%make_build

%install
%make_install

%check
%make_build check

%files
%license LICENSE
%doc AUTHORS CHANGES MANIFEST README
%{_bindir}/cproto
%{_mandir}/man1/cproto.1*

%changelog
%autochangelog
