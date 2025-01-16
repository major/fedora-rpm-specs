%global pkgname sonata
%global giturl  https://github.com/gap-packages/sonata

Name:           gap-pkg-%{pkgname}
Version:        2.9.6
Release:        %autorelease
Summary:        GAP package for systems of nearrings

License:        GPL-2.0-or-later
BuildArch:      noarch
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://gap-packages.github.io/sonata/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  parallel
BuildRequires:  tth

Requires:       gap-core

Suggests:       xgap

%description
SONATA stands for "systems of nearrings and their applications".  It
provides methods for the construction and the analysis of finite
nearrings.  A left nearring is an algebra (N;+,*), where (N,+) is a (not
necessarily abelian) group, (N,*) is a semigroup, and x*(y+z) = x*y + x*z
holds for all x,y,z in N.

As a typical example of a nearring, we may consider the set of all
mappings from a group G into G, where the addition is the pointwise
addition of mappings in G, and the multiplication is composition of
functions.  If functions are written on the right of their arguments,
then the left distributive law holds, while the right distributive law
is not satisfied for non-trivial G.

The SONATA package provides methods for the construction and analysis of
finite nearrings.
1. Methods for constructing all endomorphisms and all fixed-point-free
   automorphisms of a given group.
2. Methods for constructing the following nearrings of functions on a
   group G:
   - the nearring of polynomial functions of G (in the sense of
     Lausch-Nöbauer);
   - the nearring of compatible functions of G;
   - distributively generated nearrings such as I(G), A(G), E(G);
   - centralizer nearrings.
3. A library of all small nearrings (up to order 15) and all small
   nearrings with identity (up to order 31).
4. Functions to obtain solvable fixed-point-free automorphism groups on
   abelian groups, nearfields, planar nearrings, as well as designs from
   those.
5. Various functions to study the structure (size, ideals, N-groups, ...)
   of nearrings, to determine properties of nearring elements, and to
   decide whether two nearrings are isomorphic.
6. If the package XGAP is installed, the lattices of one- and two-sided
   ideals of a nearring can be studied interactively using a graphical
   representation.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN
Summary:        SONATA documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

%conf
# Use the main gap package's macro file
rm -f doc/gapmacro.tex
ln -s %{gap_libdir}/doc/gapmacro.tex doc/gapmacro.tex

# Fix the documentation build script
sed -e 's,\.\./\.\./\.\./\.\./etc/convert\.pl,%{gap_libdir}/etc/convert.pl,' \
    -e 's,\.\./\.\./\.\./\.\./doc/manualindex,%{gap_libdir}/doc/manualindex,' \
    -i doc/make_doc

%build
# Build the documentation
pushd doc
./make_doc
popd

# Compress large data files
parallel %{?_smp_mflags} --no-notice gzip --best ::: nr/*.nr nri/*.nr

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc/{ref,tut}
cp -a *.g grp lib nr nri tst %{buildroot}%{gap_libdir}/pkg/%{pkgname}
%gap_copy_docs -d doc/ref
%gap_copy_docs -d doc/tut
cp -a doc/htm %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc

%check
gap -l '%{buildroot}%{gap_libdir};' tst/testall.g

%files
%doc README
%license LICENSE
%dir %{gap_libdir}/pkg/%{pkgname}/
%{gap_libdir}/pkg/%{pkgname}/*.g
%{gap_libdir}/pkg/%{pkgname}/grp/
%{gap_libdir}/pkg/%{pkgname}/lib/
%{gap_libdir}/pkg/%{pkgname}/nr/
%{gap_libdir}/pkg/%{pkgname}/nri/
%{gap_libdir}/pkg/%{pkgname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{pkgname}/doc/
%{gap_libdir}/pkg/%{pkgname}/doc/

%changelog
%autochangelog
