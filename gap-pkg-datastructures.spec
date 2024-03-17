%global pkgname  datastructures

Name:           gap-pkg-%{pkgname}
Version:        0.3.0
Release:        %autorelease
Summary:        Standard data structures for GAP

License:        GPL-2.0-or-later
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://gap-packages.github.io/datastructures/
VCS:            https://github.com/gap-packages/datastructures
Source0:        %{vcs}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make

Requires:       gap-core%{?_isa}

%description
The datastructures package aims at providing standard datastructures,
consolidating existing code and improving on it, in particular in view
of HPC-GAP.

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
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

%build
export LC_ALL=C.UTF-8

# This is NOT an autoconf-generated script.  Do NOT use %%configure.
./configure %{gap_archdir}
%make_build

# Build the documentation
gap makedoc.g

%install
mkdir -p %{buildroot}%{gap_archdir}/pkg/%{pkgname}/doc
cp -a *.g bin gap tst  %{buildroot}%{gap_archdir}/pkg/%{pkgname}
%gap_copy_docs

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{gap_archdir};" tst/testall.g

%files
%doc CHANGES.md README.md
%license COPYRIGHT.md LICENSE
%{gap_archdir}/pkg/%{pkgname}/
%exclude %{gap_archdir}/pkg/%{pkgname}/doc/

%files doc
%docdir %{gap_archdir}/pkg/%{pkgname}/doc/
%{gap_archdir}/pkg/%{pkgname}/doc/

%changelog
%autochangelog
