%global pkgname anupq
%global giturl  https://github.com/gap-packages/anupq

# This package plays weird tricks with pointers to implement arrays with a
# starting index other than zero.  The weird tricks confuse fortify at level 3,
# so we turn it down to keep fortify from aborting.
%global _fortify_level 2

Name:           gap-pkg-%{pkgname}
Version:        3.3.1
Release:        %autorelease
Summary:        ANU p-Quotient for GAP

License:        Artistic-2.0
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://gap-packages.github.io/anupq/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{pkgname}-%{version}.tar.bz2

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-autpgrp
BuildRequires:  gap-pkg-autpgrp-doc
BuildRequires:  gcc

Requires:       gap-core%{?_isa}
Requires:       gap-pkg-autpgrp

%description
This package gives access to the following algorithms from inside GAP:
1. A p-quotient algorithm to compute a power-commutator presentation for
   a group of prime power order.
2. A p-group generation algorithm to generate descriptions of groups of
   prime power order.
3. A standard presentation algorithm used to compute a canonical
   power-commutator presentation of a p-group.
4. An algorithm which can be used to compute the automorphism group of a
   p-group.

%package doc
# The content is Artistic-2.0.
# The remaining licenses cover the various fonts embedded in PDFs:
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
# StandardSymL: GPL-1.0-or-later
License:        Artistic-2.0 AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        ANUPQ documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-pkg-autpgrp-doc

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

%conf
cp -p standalone-doc/README README.standalone

%build
%configure --with-gaproot=%{gap_archdir} --disable-silent-rules
%make_build

# Build the documentation
ln -s %{gap_libdir}/doc ../../doc
mkdir -p ../pkg
ln -s ../%{pkgname}-%{version} ../pkg
ln -s %{gap_libdir}/pkg/AutoDoc ../pkg
ln -s %{gap_libdir}/pkg/autpgrp-* ../pkg
ln -s %{gap_libdir}/pkg/GAPDoc ../pkg
gap makedoc.g
rm -fr ../../doc ../pkg

# Build the standalone documentation
cd standalone-doc
pdflatex guide
pdflatex guide
pdflatex guide
cd -

%install
mkdir -p %{buildroot}%{gap_archdir}/pkg/%{pkgname}/doc
cp -a bin examples lib standalone testPq tst *.g  %{buildroot}%{gap_archdir}/pkg/%{pkgname}
%gap_copy_docs

%check
gap -l '%{buildroot}%{gap_archdir};' tst/testinstall.g

%files
%doc CHANGES README.md README.standalone standalone-doc/guide.pdf
%license LICENSE
%dir %{gap_archdir}/pkg/%{pkgname}/
%{gap_archdir}/pkg/%{pkgname}/*.g
%{gap_archdir}/pkg/%{pkgname}/bin/
%{gap_archdir}/pkg/%{pkgname}/lib/
%{gap_archdir}/pkg/%{pkgname}/standalone/
%{gap_archdir}/pkg/%{pkgname}/testPq
%{gap_archdir}/pkg/%{pkgname}/tst/

%files doc
%docdir %{gap_archdir}/pkg/%{pkgname}/doc/
%docdir %{gap_archdir}/pkg/%{pkgname}/examples/
%{gap_archdir}/pkg/%{pkgname}/doc/
%{gap_archdir}/pkg/%{pkgname}/examples/

%changelog
%autochangelog
