%global gap_pkgname autpgrp
%global giturl      https://github.com/gap-packages/autpgrp

Name:           gap-pkg-%{gap_pkgname}
Version:        1.11.1
Release:        %autorelease
Summary:        Compute the automorphism group of a p-Group in GAP

License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/autpgrp/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{gap_upname}-%{version}.tar.gz

BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): gap htm tst
BuildOption(check): tst/testall.g

BuildRequires:  gap-devel
BuildRequires:  tth

Requires:       gap-core

%description
The AutPGrp package introduces a new function to compute the automorphism
group of a finite p-group.  The underlying algorithm is a refinement of the
methods described in O'Brien (1995).  In particular, this implementation is
more efficient in both time and space requirements and hence has a wider range
of applications than the ANUPQ method.  Our package is written in GAP code and
it makes use of a number of methods from the GAP library such as the MeatAxe
for matrix groups and permutation group functions.  We have compared our
method to the others available in GAP.  Our package usually out-performs all
but the method designed for finite abelian groups.  We note that our method
uses the small groups library in certain cases and hence our algorithm is more
effective if the small groups library is installed.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# Nimbus: AGPL-3.0-only
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND AGPL-3.0-only
Summary:        Automorphism group documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -n %{gap_upname}-%{version}

%conf
# Use the system GAP macro file instead of the bundled version
rm -f doc/gapmacro.tex
ln -s %{gap_libdir}/doc/gapmacro.tex doc

%build
# Link to main GAP documentation
ln -s %{gap_libdir}/etc ../../etc
ln -s %{gap_libdir}/doc ../../doc
pushd doc
./make_doc
popd
rm -f ../../{doc,etc}

%files
%doc README CHANGES.md
%license LICENSE
%dir %{gap_libdir}/pkg/%{gap_upname}/
%{gap_libdir}/pkg/%{gap_upname}/*.g
%{gap_libdir}/pkg/%{gap_upname}/gap/
%{gap_libdir}/pkg/%{gap_upname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{gap_upname}/doc/
%docdir %{gap_libdir}/pkg/%{gap_upname}/htm/
%{gap_libdir}/pkg/%{gap_upname}/doc/
%{gap_libdir}/pkg/%{gap_upname}/htm/

%changelog
%autochangelog
