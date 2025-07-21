%global pkgname groupoids
%global giturl  https://github.com/gap-packages/groupoids

Name:           gap-pkg-%{pkgname}
Version:        1.78
Release:        %autorelease
Summary:        Groupoids, group graphs, and groupoid graphs

License:        GPL-2.0-or-later
BuildArch:      noarch
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://gap-packages.github.io/groupoids/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-fga
BuildRequires:  gap-pkg-semigroups
BuildRequires:  gap-pkg-utils
BuildRequires:  tex(xy.sty)

Requires:       gap-pkg-fga
Requires:       gap-pkg-utils

Recommends:     gap-pkg-semigroups

%description
The Groupoids package provides functions for computation with finite
groupoids and their morphisms.

The first part is concerned with the standard constructions for
connected groupoids, and for groupoids with more than one component.
Groupoid morphisms are also implemented, and recent work includes the
implementation of automorphisms of a finite, connected groupoid: by
permutation of the objects; by automorphism of the root group; and by
choice of rays to each object.  The automorphism group of such a
groupoid is also computed, together with an isomorphism of a quotient of
permutation groups.

The second part implements graphs of groups and graphs of groupoids.  A
graph of groups is a directed graph with a group at each vertex and with
isomorphisms between subgroups on each arc.  This construction enables
normal form computations for free products with amalgamation, and for
HNN extensions, when the vertex groups come with their own rewriting
systems.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
# StandardSymL: GPL-1.0-or-later
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Groupoids documentation
Requires:       %{name} = %{version}-%{release}
Requires:       GAPDoc-doc

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version} -p1

%build
mkdir ../pkg
ln -s ../%{pkgname}-%{version} ../pkg
gap -l "$PWD/..;" makedoc.g
rm -fr ../pkg

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc
cp -a *.g lib tst %{buildroot}%{gap_libdir}/pkg/%{pkgname}
%gap_copy_docs

%check
# Skip tests that tend to get OOM killed
SKIP='manual/gpd.tst extra/rt-act.tst'
for test in $SKIP; do
  rm %{buildroot}%{gap_libdir}/pkg/%{pkgname}/tst/$test
done
gap -l '%{buildroot}%{gap_libdir};' tst/testall.g
for test in $SKIP; do
  cp -p tst/$test %{buildroot}%{gap_libdir}/pkg/%{pkgname}/tst/$test
done

%files
%doc CHANGES.md README.md
%license LICENSE.txt
%dir %{gap_libdir}/pkg/%{pkgname}/
%{gap_libdir}/pkg/%{pkgname}/*.g
%{gap_libdir}/pkg/%{pkgname}/lib/
%{gap_libdir}/pkg/%{pkgname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{pkgname}/doc/
%{gap_libdir}/pkg/%{pkgname}/doc/

%changelog
%autochangelog
