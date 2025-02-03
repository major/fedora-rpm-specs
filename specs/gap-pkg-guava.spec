%global pkgname guava
%global giturl  https://github.com/gap-packages/guava

Name:           gap-pkg-%{pkgname}
Version:        3.20
Release:        %autorelease
Summary:        Computing with error-correcting codes

License:        GPL-2.0-or-later
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://gap-packages.github.io/guava/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/%{pkgname}-%{version}.tar.gz
# Patch to fix C compiler warnings that indicate possible runtime problems.
Patch:          %{name}-warning.patch
# Use popcount instructions where available.
Patch:          %{name}-popcount.patch

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-sonata
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  parallel

Requires:       gap-core%{?_isa}

Recommends:     gap-pkg-sonata

%global _docdir_fmt %{name}

%description
GUAVA is a package that implements coding theory algorithms in GAP.
Codes can be created and manipulated and information about codes can be
calculated.

GUAVA consists of various files written in the GAP language, and an
external program from J. S. Leon for dealing with automorphism groups of
codes and isomorphism testing functions.  Several algorithms that need
the speed are integrated in the GAP kernel.

The functions within GUAVA can be divided into four categories:
- Construction of codes.  GUAVA can construct non-linear, linear and
  cyclic codes over an arbitrary finite field.  Examples are
  HadamardCode, ReedMullerCode, BestKnownLinearCode, QRCode and
  GoppaCode.
- Manipulation of codes.  These functions allow the user to transform
  one code into another or to construct a new code from two codes.
  Examples are PuncturedCode, DualCode, DirectProductCode and UUVCode.
- Computation of information about codes.  This information is stored in
  the code record.  Examples are MinimumDistance, OuterDistribution,
  IsSelfDualCode and AutomorphismGroup.
- Generation of bounds on linear codes.  The table by Brouwer and
  Verhoeff (as it existed in the mid-1990s) is incorporated into GUAVA.
  For example, BoundsMinimumDistance.

%package doc
# The content is GFDL-1.2-no-invariants-or-later.  The remaining licenses cover
# the various fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
# StandardSymL: GPL-1.0-or-later
License:        GFDL-1.2-no-invariants-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        GUAVA documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -p0 -n %{pkgname}-%{version}

%conf
# Avoid name collisions in the documentation
cp -p src/ctjhai/README README.ctjhai

%build
# This is NOT an autoconf-generated script.  Do not use %%configure.
./configure %{gap_archdir}

# Building with %%{?_smp_mflags} fails
make CFLAGS='%{build_cflags} -DLONG_EXTERNAL_NAMES'

# Compress large tables
parallel %{?_smp_mflags} --no-notice gzip --best ::: tbl/*.g

# Build documentation
gap makedoc.g
pushd src/leon/doc
pdftex manual.tex
popd

%install
mkdir -p %{buildroot}%{gap_archdir}/pkg/%{pkgname}/doc
cp -a *.g bin lib tbl tst %{buildroot}%{gap_archdir}/pkg/%{pkgname}
%gap_copy_docs

%check
# Tests that generate random values often fail.
# Only run the deterinistic tests.
cd tst
gap -l '%{buildroot}%{gap_archdir};' << EOF
LoadPackage("guava");
if Test("bugfix.tst", rec( compareFunction := "uptowhitespace" ) ) = false then GAP_EXIT_CODE(1); fi;
if Test("decoding.tst", rec( compareFunction := "uptowhitespace" ) ) = false then GAP_EXIT_CODE(1); fi;
if Test("external.tst", rec( compareFunction := "uptowhitespace" ) ) = false then GAP_EXIT_CODE(1); fi;
if Test("guava.tst", rec( compareFunction := "uptowhitespace" ) ) = false then GAP_EXIT_CODE(1); fi;
if Test("guava01.tst", rec( compareFunction := "uptowhitespace" ) ) = false then GAP_EXIT_CODE(1); fi;
if Test("guava02.tst", rec( compareFunction := "uptowhitespace" ) ) = false then GAP_EXIT_CODE(1); fi;
if Test("guava08.tst", rec( compareFunction := "uptowhitespace" ) ) = false then GAP_EXIT_CODE(1); fi;
if Test("hadamard.tst", rec( compareFunction := "uptowhitespace" ) ) = false then GAP_EXIT_CODE(1); fi;
if Test("QCLDPCCodeFromGroup.tst", rec( compareFunction := "uptowhitespace" ) ) = false then GAP_EXIT_CODE(1); fi;
if Test("table.tst", rec( compareFunction := "uptowhitespace" ) ) = false then GAP_EXIT_CODE(1); fi;
EOF

%files
%doc CHANGES HISTORY README.md README.ctjhai
%license COPYING
%dir %{gap_archdir}/pkg/%{pkgname}/
%{gap_archdir}/pkg/%{pkgname}/*.g
%{gap_archdir}/pkg/%{pkgname}/bin/
%{gap_archdir}/pkg/%{pkgname}/lib/
%{gap_archdir}/pkg/%{pkgname}/tbl/
%{gap_archdir}/pkg/%{pkgname}/tst/

%files doc
%doc src/leon/doc/manual.pdf
%docdir %{gap_archdir}/pkg/%{pkgname}/doc/
%{gap_archdir}/pkg/%{pkgname}/doc/

%changelog
%autochangelog
