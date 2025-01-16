%global pkgname ctbllib

# When bootstrapping a new architecture, there is no gap-pkg-spinsym package
# yet.  We need it to run tests, but it needs this package to function at all.
# Therefore, do the following:
# 1. Build this package in bootstrap mode.
# 2. Build gap-pkg-spinsym
# 4. Build this package in non-bootstrap mode.
%bcond bootstrap 0

Name:           gap-pkg-%{pkgname}
Version:        1.3.9
Release:        %autorelease
Summary:        GAP Character Table Library

License:        GPL-3.0-or-later
BuildArch:      noarch
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/
Source0:        %{url}%{pkgname}-%{version}.tar.gz
# Predownloaded data from ATLAS needed for the tests
Source1:        %{name}-testdata.tar.xz

# The makedocrel script determines that the package being built is outside of
# the normal GAP install directories and refuses to do anything with it.
Patch:          %{name}-makedocrel.patch

BuildRequires:  gap-devel
BuildRequires:  GAPDoc-latex
BuildRequires:  gap-pkg-atlasrep-doc
BuildRequires:  gap-pkg-browse-doc
BuildRequires:  gap-pkg-cohomolo
BuildRequires:  gap-pkg-grpconst
BuildRequires:  gap-pkg-smallgrp-doc
%if %{without bootstrap}
BuildRequires:  gap-pkg-spinsym
%endif
BuildRequires:  gap-pkg-tomlib-doc
BuildRequires:  netpbm-progs
BuildRequires:  parallel
BuildRequires:  tex(epic.sty)

Requires:       gap-pkg-atlasrep

Recommends:     gap-pkg-browse
Recommends:     gap-pkg-primgrp
Recommends:     gap-pkg-smallgrp
Recommends:     gap-pkg-spinsym
Recommends:     gap-pkg-tomlib
Recommends:     gap-pkg-transgrp

%description
This package provides the Character Table Library by Thomas Breuer.

%package doc
# The content is GPL-3.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# LaTeX: LPPL-1.3a
# Nimbus: AGPL-3.0-only
# RSFS: LicenseRef-Rsfs
# StandardSymL: GPL-1.0-or-later
License:        GPL-3.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND LPPL-1.3a AND AGPL-3.0-only AND LicenseRef-Rsfs
Summary:        Character Table Library documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-pkg-atlasrep-doc
Requires:       gap-pkg-browse-doc
Requires:       gap-pkg-smallgrp-doc
Requires:       gap-pkg-tomlib-doc

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version} -b1 -p1

%conf
# Remove spurious executable bit
chmod a-x doc/utils.xml

%build
# Compress large tables
parallel %{?_smp_mflags} --no-notice gzip --best ::: data/*.tbl

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{pkgname}
cp -a *.g data dlnames gap4 htm tst %{buildroot}%{gap_libdir}/pkg/%{pkgname}

# Building documentation has to be done after installation, because otherwise
# GAP sees an old version of ctbllib in the buildroot rather than this version,
# and the ctbllib version check kills the build.
cp -a doc doc2 %{buildroot}%{gap_libdir}/pkg/%{pkgname}
gap -l '%{buildroot}%{gap_libdir};' makedocrel.g
rm -fr doc doc2
mv %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc{,2} .
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc{,2}
%gap_copy_docs
%gap_copy_docs -d doc2

%check
# Tell ATLAS where to find downloaded files
mkdir ~/.gap
cat > ~/.gap/gap.ini << EOF
SetUserPreference( "AtlasRep", "AtlasRepDataDirectory", "%{_builddir}/atlasrep/" );
EOF

# Basic installation test
gap -l '%{buildroot}%{gap_libdir};' << EOF
ReadPackage( "ctbllib", "tst/testinst.g" );
EOF

%if %{without bootstrap}
# Somewhat less basic test.  Skip the interactive tests.
# Do not run testall.g.  It takes a long time to run.
mkdir -p ../pkg
ln -s ../%{pkgname}-%{version} ../pkg
sed -i '/BrowseCTblLibInfo();/d' gap4/ctbltocb.g tst/docxpl.tst
gap -l "$PWD/..;" tst/testauto.g
rm -fr ../pkg
%endif

%files
%doc README.md
%dir %{gap_libdir}/pkg/%{pkgname}/
%{gap_libdir}/pkg/%{pkgname}/*.g
%{gap_libdir}/pkg/%{pkgname}/data/
%{gap_libdir}/pkg/%{pkgname}/dlnames/
%{gap_libdir}/pkg/%{pkgname}/gap4/
%{gap_libdir}/pkg/%{pkgname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{pkgname}/doc/
%docdir %{gap_libdir}/pkg/%{pkgname}/doc2/
%docdir %{gap_libdir}/pkg/%{pkgname}/htm/
%{gap_libdir}/pkg/%{pkgname}/doc/
%{gap_libdir}/pkg/%{pkgname}/doc2/
%{gap_libdir}/pkg/%{pkgname}/htm/

%changelog
%autochangelog
