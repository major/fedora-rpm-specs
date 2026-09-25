%global gap_pkgname vole
%global giturl      https://github.com/peal/vole

Name:           gap-pkg-%{gap_pkgname}
Version:        0.6.0
Release:        %autorelease
Summary:        Backtrack search in permutation groups with graphs

# MPL-2.0: this project
# The remaining licenses are for the rust dependencies; see LICENSE.rust
License:        %{shrink: MPL-2.0
                  AND (MIT OR Apache-2.0)
                  AND Unicode-DFS-2016
                  AND (BSD-2-Clause OR Apache-2.0 OR MIT)
                  AND MIT
                  AND (Unlicense OR MIT)
                }
URL:            https://peal.github.io/vole/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/%{gap_upname}-%{version}.tar.gz
# Write vole.trace in /tmp instead of failing to write it under /usr
Patch:          %{name}-write-to-tmp.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
BuildSystem:    gap
BuildOption(build): --packagedirs ..
BuildOption(install): dependencies gap tst
BuildOption(check): --packagedirs .. tst/testall.g

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  gap(autodoc) >= 2019.09.04
BuildRequires:  gap(backtrackkit) >= 1.1.0
BuildRequires:  gap(datastructures) >= 0.2.6
BuildRequires:  gap(digraphs) >= 1.1.1
BuildRequires:  gap(ferret) >= 1.0.2
BuildRequires:  gap(graphbacktracking) >= 1.1.0
BuildRequires:  gap(images) >= 1.3.0
BuildRequires:  gap(io) >= 4.7.0
BuildRequires:  gap(json) >= 2.0.1
BuildRequires:  gap(orbitalgraphs) >= 0.1
BuildRequires:  gap(primgrp) >= 3.4.0
BuildRequires:  gap(quickcheck) >= 0.1
BuildRequires:  gap-devel >= 4.13.0
BuildRequires:  gap-pkg-backtrackkit-doc >= 1.1.0
BuildRequires:  gap-pkg-digraphs-doc >= 1.1.1
BuildRequires:  gap-pkg-images-doc >= 1.3.0

Requires:       gap(backtrackkit) >= 1.1.0
Requires:       gap(datastructures) >= 0.2.6
Requires:       gap(digraphs) >= 1.1.1
Requires:       gap(graphbacktracking) >= 1.1.0
Requires:       gap(images) >= 1.3.0
Requires:       gap(io) >= 4.7.0
Requires:       gap(json) >= 2.0.1
Requires:       gap(primgrp) >= 3.4.0
Requires:       gap-core >= 4.13.0

Recommends:     flamegraph
Recommends:     gap(orbitalgraphs) >= 0.1

Provides:       gap(vole) = %{version}-%{release}

%description
This package contains an implementation of fundamental group theory algorithms
in Rust for GAP.

It aims to implement some highly efficient backtrack search algorithms in
finite permutation groups.  These algorithms are intended to solve a range of
problems, including (but not limited to):

- Subgroup intersection
- Normalizer
- Centralizer
- Graph isomorphism
- Coset intersection
- Canonical image

These algorithms are based on the theory introduced by the paper
“Permutation group algorithms based on directed graphs” (2021) [1], by
Christopher Jefferson, Markus Pfeiffer, Rebecca Waldecker, and Wilf A. Wilson.
This theory extends the well-established “partition backtrack” framework of
Jeffrey Leon, and works with labeled digraphs as the fundamental objects of
these algorithms.

[1] https://doi.org/10.1016/j.jalgebra.2021.06.015

FEDORA NOTE: If tracing is requested, the vole binary attempts to write
vole.trace in the same directory as the binary.  That directory is not
writable by regular users, leading to the vole program exiting with an error.
The Fedora build instead writes to /tmp/vole.trace.

%package doc
# The content is MPL-2.0.  The remaining licenses cover the various fonts
# embedded in PDFs.
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
# StandardSymL: GPL-1.0-or-later
License:        MPL-2.0 AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Vole documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
Requires:       gap-pkg-backtrackkit-doc >= 1.1.0
Requires:       gap-pkg-digraphs-doc >= 1.1.1
Requires:       gap-pkg-images-doc >= 1.3.0

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -n %{gap_upname}-%{version} -p1

cd rust
%cargo_prep
cd -

%generate_buildrequires
cd rust
# We do not pass -t because Fedora lacks criterion
%cargo_generate_buildrequires

%build -p
cd rust
%cargo_build
%cargo_license_summary
%{cargo_license} > ../LICENSE.rust
cd -

%install -a
mkdir -p %{buildroot}%{gap_archdir}/pkg/%{gap_upname}/rust/target/release
install -m 0755 -p rust/target/release/{graphiso,vole} \
    %{buildroot}%{gap_archdir}/pkg/%{gap_upname}/rust/target/release

%files
%doc README.md
%license LICENSE
%license LICENSE.rust
%dir %{gap_archdir}/pkg/%{gap_upname}/
%{gap_archdir}/pkg/%{gap_upname}/*.g
%{gap_archdir}/pkg/%{gap_upname}/dependencies/
%{gap_archdir}/pkg/%{gap_upname}/gap/
%{gap_archdir}/pkg/%{gap_upname}/rust/
%{gap_archdir}/pkg/%{gap_upname}/tst/

%files doc
%docdir %{gap_archdir}/pkg/%{gap_upname}/doc/
%{gap_archdir}/pkg/%{gap_upname}/doc/

%changelog
%autochangelog
