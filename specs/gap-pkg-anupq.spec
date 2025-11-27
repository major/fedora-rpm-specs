%global gap_pkgname anupq
%global giturl      https://github.com/gap-packages/anupq

# This package plays weird tricks with pointers to implement arrays with a
# starting index other than zero.  The weird tricks confuse fortify at level 3,
# so we turn it down to keep fortify from aborting.
%global _fortify_level 2

Name:           gap-pkg-%{gap_pkgname}
Version:        3.3.3
Release:        %autorelease
Summary:        ANU p-Quotient for GAP

License:        Artistic-2.0
URL:            https://gap-packages.github.io/anupq/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{gap_upname}-%{version}.tar.bz2

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
BuildSystem:    gap
BuildOption(build): --packagedirs ..
BuildOption(install): bin examples lib standalone testPq tst
BuildOption(check): tst/testinstall.g

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-autpgrp
BuildRequires:  gap-pkg-autpgrp-doc
BuildRequires:  gcc

Requires:       gap-core%{?_isa}
Requires:       gap-pkg-autpgrp

%description
This package gives access to the following algorithms from inside GAP:
1. A p-quotient algorithm to compute a power-commutator presentation for a
   group of prime power order.
2. A p-group generation algorithm to generate descriptions of groups of prime
   power order.
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
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -n %{gap_upname}-%{version}

%conf
cp -p standalone-doc/README README.standalone

%build -p
%configure --with-gaproot=%{gap_archdir} --disable-silent-rules
%make_build
ln -s %{gap_libdir}/doc ../../doc

%build -a
rm -fr ../../doc

# Build the standalone documentation
cd standalone-doc
pdflatex guide
pdflatex guide
pdflatex guide
cd -

%files
%doc CHANGES README.md README.standalone standalone-doc/guide.pdf
%license LICENSE
%dir %{gap_archdir}/pkg/%{gap_upname}/
%{gap_archdir}/pkg/%{gap_upname}/*.g
%{gap_archdir}/pkg/%{gap_upname}/bin/
%{gap_archdir}/pkg/%{gap_upname}/lib/
%{gap_archdir}/pkg/%{gap_upname}/standalone/
%{gap_archdir}/pkg/%{gap_upname}/testPq
%{gap_archdir}/pkg/%{gap_upname}/tst/

%files doc
%docdir %{gap_archdir}/pkg/%{gap_upname}/doc/
%docdir %{gap_archdir}/pkg/%{gap_upname}/examples/
%{gap_archdir}/pkg/%{gap_upname}/doc/
%{gap_archdir}/pkg/%{gap_upname}/examples/

%changelog
%autochangelog
