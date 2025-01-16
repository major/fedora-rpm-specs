%global pkgname normalizinterface
%global upname  NormalizInterface
%global giturl  https://github.com/gap-packages/NormalizInterface

Name:           gap-pkg-%{pkgname}
Version:        1.3.7
Release:        %autorelease
Summary:        GAP wrapper for Normaliz

License:        GPL-2.0-or-later
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://gap-packages.github.io/NormalizInterface/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{upname}-%{version}.tar.bz2
# Adapt to normaliz 3.10.*
Patch:          https://github.com/gap-packages/NormalizInterface/pull/114.patch

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gcc-c++
BuildRequires:  libnormaliz-devel
BuildRequires:  make

Requires:       gap-core%{?_isa}

%description
Normaliz is software for computations with rational cones and affine
monoids.  It pursues two main computational goals: finding the Hilbert
basis, a minimal generating system of the monoid of lattice points of a
cone; and counting elements degree-wise in a generating function, the
Hilbert series.

As a recent extension, Normaliz can handle unbounded polyhedra.  The
Hilbert basis computation can be considered as solving a linear
diophantine system of inhomogeneous equations, inequalities and
congruences.

This package allows creating libnormaliz cone objects from within GAP,
and gives access to it in the GAP environment.  In this way GAP can be
used as an interactive interface to libnormaliz.

%package doc
# The content is GPL-2.0-or-later.
# The remaining licenses cover the various fonts embedded in PDFs:
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
License:        GPL-2.0-or-later AND GPL-1.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND AGPL-3.0-only
Summary:        Documentation for the GAP %{upname} package
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{upname}-%{version} -p1

%conf
# Defeat attempts to set an rpath
sed -i 's/\(NORMALIZ_RPATH_EXTRA=\)"-.*"/\1""/' configure

%build
sed -i '/GMP_PREFIX/s,-none,-%{_prefix},' configure
%configure --with-gaproot=%{gap_archdir}
%make_build
gap makedoc.g

%install
mkdir -p %{buildroot}%{gap_archdir}/pkg/%{upname}/doc
cp -a bin etc examples lib tst *.g  %{buildroot}%{gap_archdir}/pkg/%{upname}
%gap_copy_docs -n %{upname}

%check
gap -l '%{buildroot}%{gap_archdir};' tst/testall.g

%files
%doc CHANGES README.md
%license LICENSE
%dir %{gap_archdir}/pkg/%{upname}/
%{gap_archdir}/pkg/%{upname}/*.g
%{gap_archdir}/pkg/%{upname}/bin/
%{gap_archdir}/pkg/%{upname}/etc/
%{gap_archdir}/pkg/%{upname}/lib/
%{gap_archdir}/pkg/%{upname}/tst/

%files doc
%docdir %{gap_archdir}/pkg/%{upname}/doc/
%docdir %{gap_archdir}/pkg/%{upname}/examples/
%{gap_archdir}/pkg/%{upname}/doc/
%{gap_archdir}/pkg/%{upname}/examples/

%changelog
%autochangelog
