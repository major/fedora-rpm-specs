%global gap_pkgname cvec
%global giturl      https://github.com/gap-packages/cvec

Name:           gap-pkg-%{gap_pkgname}
Version:        2.8.4
Release:        %autorelease
Summary:        Compact vectors over finite fields

License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/cvec/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{gap_upname}-%{version}.tar.bz2

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
BuildSystem:    gap
BuildOption(install): bin example gap local test tst
BuildOption(check): tst/testall.g

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-atlasrep
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-ctbllib
BuildRequires:  gap-pkg-io-doc
BuildRequires:  gap-pkg-orb-doc
BuildRequires:  gap-pkg-tomlib
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make

Requires:       gap-pkg-io%{?_isa}
Requires:       gap-pkg-orb%{?_isa}

%description
The CVEC package provides an implementation of compact vectors over finite
fields.  Contrary to earlier implementations no table lookups are used but
only word-based processor arithmetic.  This allows for bigger finite fields
and higher speed.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
# StandardSymL: GPL-1.0-or-later
License:        GPL-2.0-or-later AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        CVEC documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-pkg-io-doc
Requires:       gap-pkg-orb-doc

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -n %{gap_upname}-%{version}

%build
# This is NOT an autotools-generated configure script; do NOT use %%configure
./configure --with-gaproot=%{gap_archdir}
%make_build V=1

# Build the documentation
make doc

%files
%doc CHANGES README.md TIMINGS TODO
%license LICENSE
%dir %{gap_archdir}/pkg/%{gap_upname}/
%{gap_archdir}/pkg/%{gap_upname}/*.g
%{gap_archdir}/pkg/%{gap_upname}/bin/
%{gap_archdir}/pkg/%{gap_upname}/gap/
%{gap_archdir}/pkg/%{gap_upname}/local/
%{gap_archdir}/pkg/%{gap_upname}/test/
%{gap_archdir}/pkg/%{gap_upname}/tst/

%files doc
%docdir %{gap_archdir}/pkg/%{gap_upname}/doc/
%docdir %{gap_archdir}/pkg/%{gap_upname}/example/
%{gap_archdir}/pkg/%{gap_upname}/doc/
%{gap_archdir}/pkg/%{gap_upname}/example/

%changelog
%autochangelog
