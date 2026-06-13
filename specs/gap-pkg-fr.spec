%global gap_pkgname fr
%global giturl      https://github.com/gap-packages/fr

Name:           gap-pkg-%{gap_pkgname}
Version:        2.4.13
Release:        %autorelease
Summary:        Computations with functionally recursive groups

License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/fr/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{gap_upname}-%{version}.tar.gz
# Work around for https://github.com/frankluebeck/GAPDoc/issues/77
Patch:          %{name}-gapdoc-bug.patch

BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): gap guest tst
BuildOption(check): tst/testall.g

BuildRequires:  gap(autodoc) >= 2022.07.10
BuildRequires:  gap(fga) >= 1.1
BuildRequires:  gap(gapdoc) >= 1.0
BuildRequires:  gap(gbnp) >= 0.9
BuildRequires:  gap(io) >= 4.0
BuildRequires:  gap(lpres) >= 0.1
BuildRequires:  gap(nq) >= 2.4
BuildRequires:  gap(polycyclic) >= 2.2
BuildRequires:  gap-devel >= 4.8

# cat is invoked
Requires:       coreutils
Requires:       gap(fga) >= 1.1
Requires:       gap(io) >= 4.0
Requires:       gap(polycyclic) >= 2.2
Requires:       gap-core >= 4.8

Recommends:     ImageMagick
Recommends:     gap(gbnp) >= 0.9
Recommends:     gap(lpres) >= 0.1
Recommends:     gap(nq) >= 2.4
Recommends:     graphviz

Provides:       gap(FR) = %{version}-%{release}
Provides:       gap(fr) = %{version}-%{release}

%description
This package implements Functionally Recursive and Mealy automata in GAP.
These objects can be manipulated as group elements, and various specific
commands allow their manipulation as automorphisms of infinite rooted trees.
Permutation quotients can also be created and manipulated as standard GAP
groups or semigroups.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
# StandardSymL: GPL-1.0-or-later
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        FR documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -n %{gap_upname}-%{version} -p1

%files
%doc BUGS CHANGES README.md TODO
%license COPYING
%dir %{gap_libdir}/pkg/%{gap_upname}/
%{gap_libdir}/pkg/%{gap_upname}/*.g
%{gap_libdir}/pkg/%{gap_upname}/gap/
%{gap_libdir}/pkg/%{gap_upname}/guest/
%{gap_libdir}/pkg/%{gap_upname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{gap_upname}/doc/
%{gap_libdir}/pkg/%{gap_upname}/doc/

%changelog
%autochangelog
