%global pkgname circle
%global giturl  https://github.com/gap-packages/circle

Name:           gap-pkg-%{pkgname}
Version:        1.6.6
Release:        %autorelease
Summary:        Adjoint groups of finite rings

License:        GPL-2.0-or-later
BuildArch:      noarch
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://gap-packages.github.io/circle/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-laguna
BuildRequires:  GAPDoc-latex
BuildRequires:  tth

Requires:       gap-core

%description
Let R be an associative ring, not necessarily with a unit element.  The
set of all elements of R forms a monoid with the neutral element 0 from
R under the operation r*s = r + s + rs defined for all r,s from R.  This
operation is called 'circle multiplication'; it is also known as 'star
multiplication'.  The monoid of elements of R under circle
multiplication is called the adjoint semigroup of R.  The group of all
invertible elements of this monoid is called the adjoint group of R.

These notions naturally lead to a number of questions about the
connection between a ring and its adjoint group, for example, how the
ring properties will determine properties of the adjoint group; which
groups can appear as adjoint groups of rings; which rings can have
adjoint groups with prescribed properties, etc.

The main objective of the GAP package 'Circle' is to extend GAP
functionality for computations in adjoint groups of associative rings to
make it possible to use the GAP system for the investigation of such
questions.

Circle provides functionality to construct circle objects that will
respect circle multiplication r*s = r + s + rs, create multiplicative
groups, generated by these objects, and compute groups of elements,
invertible with respect to this operation, for finite radical algebras
and finite associative rings without one.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
License:        GPL-2.0-or-later AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Circle documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

%build
mkdir -p ../pkg
ln -s ../%{pkgname}-%{version} ../pkg
gap -l "$PWD/..;" makedoc.g
rm -fr ../pkg

# Fix paths in the extracted example files
sed -i "s,$PWD/\.\.,%{gap_libdir},g" tst/circle*.tst

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc
cp -a *.g lib tst %{buildroot}%{gap_libdir}/pkg/%{pkgname}
rm %{buildroot}%{gap_libdir}/pkg/%{pkgname}/tst/README.md
%gap_copy_docs

%check
gap -l '%{buildroot}%{gap_libdir};' tst/testall.g

%files
%doc README.md
%license COPYING
%dir %{gap_libdir}/pkg/%{pkgname}/
%{gap_libdir}/pkg/%{pkgname}/*.g
%{gap_libdir}/pkg/%{pkgname}/lib/
%{gap_libdir}/pkg/%{pkgname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{pkgname}/doc/
%{gap_libdir}/pkg/%{pkgname}/doc/

%changelog
%autochangelog
