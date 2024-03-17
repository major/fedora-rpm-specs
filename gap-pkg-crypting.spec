%global pkgname crypting

Name:           gap-pkg-%{pkgname}
Version:        0.10.4
Release:        %autorelease
Summary:        Hashes and Crypto in GAP

License:        BSD-3-Clause
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://gap-packages.github.io/crypting/
VCS:            https://github.com/gap-packages/crypting
Source0:        %{vcs}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make

Requires:       gap-core%{?_isa}

%description
This package implements some cryptographic primitives.  At the moment
this is a custom implementation of SHA256 and HMAC, which is needed to
sign messages in the Jupyter kernel.

Bindings to a full crypto library are a possibility for the future, and
pull-requests (after discussion) are appreciated.

%package doc
# The content is BSD-3-Clause.  The remaining licenses cover the various fonts
# embedded in PDFs.
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
License:        BSD-3-Clause AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
BuildArch:      noarch
Summary:        Crypting documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

%build
export LC_ALL=C.UTF-8

# This is NOT an autoconf-generated configure script.  Do NOT use %%configure.
./configure %{gap_archdir}
%make_build

# Build the documentation
gap makedoc.g

%install
mkdir -p %{buildroot}%{gap_archdir}/pkg/%{pkgname}/doc
cp -a *.g bin gap tst %{buildroot}%{gap_archdir}/pkg/%{pkgname}
%gap_copy_docs

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{gap_archdir};" tst/testall.g

%files
%doc README.md
%license COPYRIGHT.md LICENSE
%{gap_archdir}/pkg/%{pkgname}/
%exclude %{gap_archdir}/pkg/%{pkgname}/doc/

%files doc
%docdir %{gap_archdir}/pkg/%{pkgname}/doc/
%{gap_archdir}/pkg/%{pkgname}/doc/

%changelog
%autochangelog
