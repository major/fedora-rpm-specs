%global pkgname  cvec

Name:           gap-pkg-%{pkgname}
Version:        2.8.1
Release:        %autorelease
Summary:        Compact vectors over finite fields

License:        GPL-2.0-or-later
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://gap-packages.github.io/cvec/
VCS:            https://github.com/gap-packages/cvec
Source0:        %{vcs}/releases/download/v%{version}/%{pkgname}-%{version}.tar.bz2
# Predownloaded data from ATLAS needed for the tests
Source1:        %{name}-testdata.tar.xz

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
The CVEC package provides an implementation of compact vectors over
finite fields.  Contrary to earlier implementations no table lookups are
used but only word-based processor arithmetic.  This allows for bigger
finite fields and higher speed.

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
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version} -b 1

%build
export LC_ALL=C.UTF-8

# This is NOT an autotools-generated configure script; do NOT use %%configure
./configure --with-gaproot=%{gap_archdir}
%make_build V=1

# Build the documentation
make doc

%install
mkdir -p %{buildroot}%{gap_archdir}/pkg/%{pkgname}/doc
cp -a bin example gap local test tst *.g %{buildroot}%{gap_archdir}/pkg/%{pkgname}
%gap_copy_docs

%check
export LC_ALL=C.UTF-8

# Tell ATLAS where to find downloaded files
mkdir ~/.gap
cat > ~/.gap/gap.ini << EOF
SetUserPreference( "AtlasRep", "AtlasRepDataDirectory", "%{_builddir}/atlasrep/" );
EOF

gap -l "%{buildroot}%{gap_archdir};" tst/testall.g

%files
%doc CHANGES README.md TIMINGS TODO
%license LICENSE
%{gap_archdir}/pkg/%{pkgname}/
%exclude %{gap_archdir}/pkg/%{pkgname}/doc/
%exclude %{gap_archdir}/pkg/%{pkgname}/example/

%files doc
%docdir %{gap_archdir}/pkg/%{pkgname}/doc/
%docdir %{gap_archdir}/pkg/%{pkgname}/example/
%{gap_archdir}/pkg/%{pkgname}/doc/
%{gap_archdir}/pkg/%{pkgname}/example/

%changelog
%autochangelog
