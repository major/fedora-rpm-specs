%global gap_pkgname normalizinterface
%global gap_upname  NormalizInterface
%global giturl      https://github.com/gap-packages/NormalizInterface

Name:           gap-pkg-%{gap_pkgname}
Version:        1.4.1
Release:        %autorelease
Summary:        GAP wrapper for Normaliz

License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/NormalizInterface/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{gap_upname}-%{version}.tar.bz2

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
BuildSystem:    gap
BuildOption(install): bin etc examples lib tst
BuildOption(check): tst/testall.g

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gcc-c++
BuildRequires:  libnormaliz-devel
BuildRequires:  make

Requires:       gap-core%{?_isa}

%description
Normaliz is software for computations with rational cones and affine monoids.
It pursues two main computational goals: finding the Hilbert basis, a minimal
generating system of the monoid of lattice points of a cone; and counting
elements degree-wise in a generating function, the Hilbert series.

As a recent extension, Normaliz can handle unbounded polyhedra.  The Hilbert
basis computation can be considered as solving a linear diophantine system of
inhomogeneous equations, inequalities and congruences.

This package allows creating libnormaliz cone objects from within GAP, and
gives access to it in the GAP environment.  In this way GAP can be used as an
interactive interface to libnormaliz.

%package doc
# The content is GPL-2.0-or-later.
# The remaining licenses cover the various fonts embedded in PDFs:
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
License:        GPL-2.0-or-later AND GPL-1.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND AGPL-3.0-only
Summary:        Documentation for the GAP %{gap_upname} package
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -n %{gap_upname}-%{version} -p1

%conf
# Defeat attempts to set an rpath
sed -i 's/\(NORMALIZ_RPATH_EXTRA=\)"-.*"/\1""/' configure

%build -p
sed -i '/GMP_PREFIX/s,-none,-%{_prefix},' configure
%configure --with-gaproot=%{gap_archdir}
%make_build

%files
%doc CHANGES README.md
%license LICENSE
%dir %{gap_archdir}/pkg/%{gap_upname}/
%{gap_archdir}/pkg/%{gap_upname}/*.g
%{gap_archdir}/pkg/%{gap_upname}/bin/
%{gap_archdir}/pkg/%{gap_upname}/etc/
%{gap_archdir}/pkg/%{gap_upname}/lib/
%{gap_archdir}/pkg/%{gap_upname}/tst/

%files doc
%docdir %{gap_archdir}/pkg/%{gap_upname}/doc/
%docdir %{gap_archdir}/pkg/%{gap_upname}/examples/
%{gap_archdir}/pkg/%{gap_upname}/doc/
%{gap_archdir}/pkg/%{gap_upname}/examples/

%changelog
%autochangelog
