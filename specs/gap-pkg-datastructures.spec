%global gap_pkgname datastructures
%global giturl      https://github.com/gap-packages/datastructures

Name:           gap-pkg-%{gap_pkgname}
Version:        0.4.1
Release:        %autorelease
Summary:        Standard data structures for GAP

License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/datastructures/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{gap_upname}-%{version}.tar.gz
# Fix an instance of undefined behavior due to a left shift of a signed integer
# https://github.com/gap-packages/datastructures/pull/160
Patch:          %{name}-undefined-behavior.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
BuildSystem:    gap
BuildOption(install): bin gap tst
BuildOption(check): tst/testall.g

BuildRequires:  gap(autodoc) >= 2016.01.21
BuildRequires:  gap(gapdoc) >= 1.5
BuildRequires:  gap-devel >= 4.12
BuildRequires:  gcc
BuildRequires:  make

Requires:       gap-core%{?_isa} >= 4.12

Provides:       gap(datastructures) = %{version}-%{release}

%description
The datastructures package aims at providing standard datastructures,
consolidating existing code and improving on it, in particular in view of
HPC-GAP.

The following data structures are provided:
- queues
- doubly linked lists
- heaps
- priority queues
- hashtables
- dictionaries

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
License:        GPL-2.0-or-later AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Data structures documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -n %{gap_upname}-%{version} -p1

%build -p
# This is NOT an autoconf-generated script.  Do NOT use %%configure.
./configure %{gap_archdir}
%make_build

%files
%doc CHANGES.md README.md
%license COPYRIGHT.md LICENSE
%dir %{gap_archdir}/pkg/%{gap_upname}/
%{gap_archdir}/pkg/%{gap_upname}/*.g
%{gap_archdir}/pkg/%{gap_upname}/bin/
%{gap_archdir}/pkg/%{gap_upname}/gap/
%{gap_archdir}/pkg/%{gap_upname}/tst/

%files doc
%docdir %{gap_archdir}/pkg/%{gap_upname}/doc/
%{gap_archdir}/pkg/%{gap_upname}/doc/

%changelog
%autochangelog
