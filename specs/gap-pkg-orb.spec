%global pkgname orb
%global giturl  https://github.com/gap-packages/orb

%bcond bootstrap 0

Name:           gap-pkg-%{pkgname}
Version:        4.9.2
Release:        %autorelease
Summary:        Methods to enumerate orbits in GAP

License:        GPL-3.0-or-later
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://gap-packages.github.io/orb/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz
# Predownloaded data from ATLAS needed for the tests
Source1:        %{name}-testdata.tar.xz

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-io
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make

# Only pull in test dependencies in non-bootstrap mode, because gap-pkg-cvec
# requires this package to run at all.
%if %{without bootstrap}
BuildRequires:  gap-pkg-atlasrep
BuildRequires:  gap-pkg-browse
BuildRequires:  gap-pkg-ctbllib
BuildRequires:  gap-pkg-cvec
BuildRequires:  gap-pkg-tomlib
%endif

Requires:       gap-pkg-io%{?_isa}

%description
This package enables enumerating orbits in various ways from within GAP.

%package doc
# The content is GPL-3.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
# StandardSymL: GPL-1.0-or-later
License:        GPL-3.0-or-later AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        ORB documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version} -b 1

# Account for changed hash values on big endian architectures
# https://github.com/gap-packages/orb/issues/70
%ifarch s390x
sed -i 's/799/741/;s/573/237/' tst/bugfix.tst
%endif

%build
# This is NOT an autoconf-generated script.  Do NOT use %%configure.
./configure --with-gaproot=%{gap_archdir}
%make_build V=1
gap makedoc.g

%install
mkdir -p %{buildroot}%{gap_archdir}/pkg/%{pkgname}/doc
cp -a *.g bin examples gap tst %{buildroot}%{gap_archdir}/pkg/%{pkgname}
%gap_copy_docs

%if %{without bootstrap}
%check
# Skip the speed test; this is for correctness only
rm -f tst/orbitspeedtest.g

# Tell ATLAS where to find downloaded files
mkdir ~/.gap
cat > ~/.gap/gap.ini << EOF
SetUserPreference( "AtlasRep", "AtlasRepDataDirectory", "%{_builddir}/atlasrep/" );
EOF

gap -l '%{buildroot}%{gap_archdir};' tst/testall.g
%endif

%files
%doc CHANGES README.md
%license LICENSE
%dir %{gap_archdir}/pkg/%{pkgname}/
%{gap_archdir}/pkg/%{pkgname}/*.g
%{gap_archdir}/pkg/%{pkgname}/bin/
%{gap_archdir}/pkg/%{pkgname}/gap/
%{gap_archdir}/pkg/%{pkgname}/tst/

%files doc
%docdir %{gap_archdir}/pkg/%{pkgname}/doc/
%docdir %{gap_archdir}/pkg/%{pkgname}/examples/
%{gap_archdir}/pkg/%{pkgname}/doc/
%{gap_archdir}/pkg/%{pkgname}/examples/

%changelog
%autochangelog
