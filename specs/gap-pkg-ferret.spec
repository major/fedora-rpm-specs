%global gap_pkgname ferret
%global giturl      https://github.com/gap-packages/ferret

Name:           gap-pkg-%{gap_pkgname}
Version:        1.0.15
Release:        %autorelease
Summary:        Backtracking search in permutation groups

# YAPB++/simple_graph/gason is MIT
# YAPB++/source/library/fnv_hash.hpp is Public Domain
# However, none of those files are part of the final binary.
License:        MPL-2.0
URL:            https://gap-packages.github.io/ferret/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{gap_upname}-%{version}.tar.gz

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
BuildSystem:    gap
BuildOption(install): bin lib tst
BuildOption(check): tst/testall.g

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-atlasrep
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-ctbllib
BuildRequires:  gap-pkg-io
BuildRequires:  gap-pkg-tomlib
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make

Requires:       gap-core%{?_isa}

%description
Ferret is a reimplementation of parts of Jeffery Leon's Partition Backtrack
framework in C++, with extensions including:

- Ability to intersect many groups simultaneously.
- Improved refiners based on orbital graphs.

This package currently supports:

- Group intersection.
- Stabilizing many structures including sets, sets of sets, graphs, sets of
  tuples and tuples of sets.

This package can be used by users in two ways:

- When the package is loaded many built-in GAP functions such as
  'Intersection' and 'Stabilizer' are replaced with more optimized
  implementations.  This requires no changes to existing code.

- The function 'Solve' provides a unified interface to accessing all the
  functionality of the package directly.

%package doc
# The content is MPL-2.0.  The remaining licenses cover the various fonts
# embedded in PDFs.
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
License:        MPL-2.0 AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Ferret documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -n %{gap_upname}-%{version} -p1

%build -p
%configure --with-gaproot=%{gap_archdir}
%make_build

%files
%doc README
%license LICENSE
%dir %{gap_archdir}/pkg/%{gap_upname}/
%{gap_archdir}/pkg/%{gap_upname}/*.g
%{gap_archdir}/pkg/%{gap_upname}/bin/
%{gap_archdir}/pkg/%{gap_upname}/lib/
%{gap_archdir}/pkg/%{gap_upname}/tst/

%files doc
%docdir %{gap_archdir}/pkg/%{gap_upname}/doc/
%{gap_archdir}/pkg/%{gap_upname}/doc/

%changelog
%autochangelog
