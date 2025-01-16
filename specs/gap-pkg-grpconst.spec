%global pkgname grpconst
%global giturl  https://github.com/gap-packages/grpconst

Name:           gap-pkg-%{pkgname}
Version:        2.6.5
Release:        %autorelease
Summary:        Constructing groups of a given order

License:        GPL-2.0-or-later
BuildArch:      noarch
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://gap-packages.github.io/grpconst/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  GAPDoc-latex
BuildRequires:  gap-pkg-autpgrp
BuildRequires:  gap-pkg-irredsol
BuildRequires:  gap-pkg-smallgrp
BuildRequires:  tth

Requires:       gap-pkg-autpgrp
Requires:       gap-pkg-irredsol
Requires:       gap-pkg-smallgrp

%description
This package contains GAP implementations of three different approaches
to constructing up to isomorphism all groups of a given order.

The FrattiniExtensionMethod constructs all soluble groups of a given
order.  On request it gives only those that are (or are not) nilpotent
or supersolvable or that do (or do not) have normal Sylow subgroups for
some given set of primes.  The program's output may be expressed in a
compact coded form, if desired.

The CyclicSplitExtensionMethod constructs all (necessarily soluble)
groups whose given orders are of the form p^n*q for different primes p
and q and which have at least one normal Sylow subgroup.  The method,
which relies upon having available a list of all groups of order p^n, is
often faster than the Frattini extension method for the groups to which
it applies.

The UpwardsExtensions method takes as its input a permutation group G
and positive integer s and returns a list of permutation groups, one for
each extension of G by a soluble group of order a divisor of s.  Usually
it is used for nonsoluble G only, since for soluble groups the above
methods are more efficient.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# Nimbus: AGPL-3.0-only
# StandardSymL: GPL-1.0-or-later
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only AND LicenseRef-Rsfs
Summary:        GrpConst documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

%build
# Link to main GAP documentation
ln -s %{gap_libdir}/etc ../../etc
ln -s %{gap_libdir}/doc ../../doc
cd doc
./make_doc
cd -
rm -f ../../{doc,etc}

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc
cp -a *.g gap htm tst %{buildroot}%{gap_libdir}/pkg/%{pkgname}
%gap_copy_docs

%check
gap -l '%{buildroot}%{gap_libdir};' tst/testall.g

%files
%doc README
%license LICENSE
%dir %{gap_libdir}/pkg/%{pkgname}/
%{gap_libdir}/pkg/%{pkgname}/*.g
%{gap_libdir}/pkg/%{pkgname}/gap/
%{gap_libdir}/pkg/%{pkgname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{pkgname}/doc/
%docdir %{gap_libdir}/pkg/%{pkgname}/htm/
%{gap_libdir}/pkg/%{pkgname}/doc/
%{gap_libdir}/pkg/%{pkgname}/htm/

%changelog
%autochangelog
