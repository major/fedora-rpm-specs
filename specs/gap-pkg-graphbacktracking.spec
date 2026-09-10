%global gap_pkgname graphbacktracking
%global gap_upname  GraphBacktracking
%global giturl      https://github.com/peal/GraphBacktracking

Name:           gap-pkg-%{gap_pkgname}
Version:        1.1.0
Release:        %autorelease
Summary:        Implementation of a graph backtracking algorithm for GAP

License:        MPL-2.0
URL:            https://peal.github.io/GraphBacktracking/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/%{gap_upname}-%{version}.tar.gz

BuildArch:      noarch
BuildSystem:    gap
BuildOption(build): --packagedirs ..
BuildOption(install): gap tst
BuildOption(check): tst/testall.g

BuildRequires:  gap(autodoc) >= 2018.02.14
BuildRequires:  gap(backtrackkit) >= 1.1.0
BuildRequires:  gap(digraphs) >= 1.1.1
BuildRequires:  gap(images) >= 1.3.0
BuildRequires:  gap(quickcheck)
BuildRequires:  gap-devel >= 4.13
BuildRequires:  gap-pkg-backtrackkit-doc >= 1.1.0

Requires:       gap(backtrackkit) >= 1.1.0
Requires:       gap(digraphs) >= 1.1.1
Requires:       gap(images) >= 1.3.0
Requires:       gap-core >= 4.13

Provides:       gap(GraphBacktracking) = %{version}-%{release}
Provides:       gap(graphbacktracking) = %{version}-%{release}

%description
This package provides an implementation of the graph backtracking algorithm,
as described in the paper "Computing canonical images in permutation groups
with Graph Backtracking" [1] by Christopher Jefferson, Rebecca Waldecker, and
Wilf A. Wilson.  It extends the BacktrackKit package to support graph
backtracking.

This algorithm can be used to perform calculations in permutation groups, such
as:
* Group and coset intersection
* Finding canonical images of combinatorial structures in any permutation
  group

This package is intended for learning and exploring the graph backtracking
algorithm.  The performance is **extremely poor**.  For a modern,
high-performance version of this algorithm, please see the vole [2] package.

[1] https://arxiv.org/abs/2209.02534
[2] https://github.com/peal/vole

%package doc
# The content is MPL-2.0.  The remaining licenses cover the various fonts
# embedded in PDFs.
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
License:        MPL-2.0 AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        GraphBacktracking documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
Requires:       gap-pkg-backtrackkit-doc >= 1.1.0

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -n %{gap_upname}-%{version}

%files
%doc README.md
%dir %{gap_libdir}/pkg/%{gap_upname}/
%{gap_libdir}/pkg/%{gap_upname}/*.g
%{gap_libdir}/pkg/%{gap_upname}/gap/
%{gap_libdir}/pkg/%{gap_upname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{gap_upname}/doc/
%{gap_libdir}/pkg/%{gap_upname}/doc/

%changelog
%autochangelog
