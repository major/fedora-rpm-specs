%global gap_pkgname fining
%global giturl      https://github.com/gap-packages/FinInG

Name:           gap-pkg-%{gap_pkgname}
Version:        1.5.6
Release:        %autorelease
Summary:        Finite incidence geometry

License:        GPL-2.0-or-later
URL:            https://www.fining.org/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{gap_upname}-%{version}.tar.bz2

BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): examples lib tst
BuildOption(check): tst/testall.g

BuildRequires:  gap(autodoc) >= 2022.07.10
BuildRequires:  gap(cvec) >= 2.7.6
BuildRequires:  gap(design)
BuildRequires:  gap(forms) >= 1.2.5
BuildRequires:  gap(gapdoc) >= 1.6.3
BuildRequires:  gap(genss) >= 1.6.6
BuildRequires:  gap(grape) >= 4.8.2
BuildRequires:  gap(orb) >= 4.8.3
BuildRequires:  gap-devel >= 4.10
BuildRequires:  tex(makecell.sty)

Requires:       gap(cvec) >= 2.7.6
Requires:       gap(forms) >= 1.2.5
Requires:       gap(genss) >= 1.6.6
Requires:       gap(grape) >= 4.8.2
Requires:       gap(orb) >= 4.8.3
Requires:       gap-core >= 4.10

Recommends:     gap(design)
Recommends:     graphviz
Recommends:     which

Provides:       gap(FinInG) = %{version}-%{release}
Provides:       gap(fining) = %{version}-%{release}

%description
FinInG is a GAP package for computation in Finite Incidence Geometry developed
by John Bamberg, Anton Betten, Philippe Cara, Jan De Beule, Michel Lavrauw and
Max Neunhoeffer.  It provides functionality:
- to create and explore finite incidence structures, such as finite projective
  spaces, finite classical polar spaces, generalized polygons, coset
  geometries, finite affine spaces, and many more;
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
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -n %{gap_upname}-%{version}

%files
%doc README.md
%dir %{gap_libdir}/pkg/%{gap_upname}/
%{gap_libdir}/pkg/%{gap_upname}/*.g
%{gap_libdir}/pkg/%{gap_upname}/lib/
%{gap_libdir}/pkg/%{gap_upname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{gap_upname}/doc/
%docdir %{gap_libdir}/pkg/%{gap_upname}/examples/
%{gap_libdir}/pkg/%{gap_upname}/doc/
%{gap_libdir}/pkg/%{gap_upname}/examples/

%changelog
%autochangelog
