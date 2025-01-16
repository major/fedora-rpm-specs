%global pkgname fining
%global giturl  https://github.com/gap-packages/FinInG

Name:           gap-pkg-%{pkgname}
Version:        1.5.6
Release:        %autorelease
Summary:        Finite incidence geometry

License:        GPL-2.0-or-later
BuildArch:      noarch
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://www.fining.org/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{pkgname}-%{version}.tar.bz2

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-atlasrep
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-cvec
BuildRequires:  gap-pkg-design
BuildRequires:  gap-pkg-forms
BuildRequires:  gap-pkg-genss
BuildRequires:  gap-pkg-grape
BuildRequires:  gap-pkg-orb
BuildRequires:  tex(makecell.sty)

Requires:       gap-pkg-cvec
Requires:       gap-pkg-forms
Requires:       gap-pkg-genss
Requires:       gap-pkg-grape
Requires:       gap-pkg-orb

Recommends:     gap-pkg-design

%description
FinInG is a GAP package for computation in Finite Incidence Geometry
developed by John Bamberg, Anton Betten, Philippe Cara, Jan De Beule,
Michel Lavrauw and Max Neunhoeffer.  It provides functionality:
- to create and explore finite incidence structures, such as finite
  projective spaces, finite classical polar spaces, generalized
  polygons, coset geometries, finite affine spaces, and many more;
- to explore algebraic varieties in finite projective and finite affine
  spaces;
- that deals with the automorphism groups of incidence structures, and
  functionality integrating these automorphism groups with the group
  theoretical capabilities of GAP;
- to explore various morphisms between finite incidence structures.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
# StandardSymL: GPL-1.0-or-later
# Tipa: LPPL-1.3a
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only AND LPPL-1.3a
Summary:        FinInG documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

%build
gap makedoc.g

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc
cp -a *.g examples lib tst %{buildroot}%{gap_libdir}/pkg/%{pkgname}
%gap_copy_docs

%check
gap -l '%{buildroot}%{gap_libdir};' tst/testall.g

%files
%doc README.md
%dir %{gap_libdir}/pkg/%{pkgname}/
%{gap_libdir}/pkg/%{pkgname}/*.g
%{gap_libdir}/pkg/%{pkgname}/lib/
%{gap_libdir}/pkg/%{pkgname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{pkgname}/doc/
%docdir %{gap_libdir}/pkg/%{pkgname}/examples/
%{gap_libdir}/pkg/%{pkgname}/doc/
%{gap_libdir}/pkg/%{pkgname}/examples/

%changelog
%autochangelog
