%global pkgname congruence

Name:           gap-pkg-%{pkgname}
Version:        1.2.5
Release:        %autorelease
Summary:        Congruence subgroups of SL(2,Integers)

License:        GPL-2.0-or-later
BuildArch:      noarch
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://gap-packages.github.io/congruence/
VCS:            https://github.com/gap-packages/congruence
Source0:        %{vcs}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  GAPDoc-latex

Requires:       gap-core

%description
The Congruence package provides functions to construct several types of
canonical congruence subgroups in SL_2(Z), and also intersections of a
finite number of such subgroups.  Furthermore, it implements the
algorithm for generating Farey symbols for congruence subgroups and
using them to produce a system of independent generators for these
subgroups.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
# StandardSymL: GPL-1.0-or-later
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Congruence documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

%build
export LC_ALL=C.UTF-8

# Link to main GAP documentation
ln -s %{gap_libdir}/doc ../../doc
mkdir ../pkg
ln -s ../%{pkgname}-%{version} ../pkg
gap -l "$PWD/..;" makedoc.g
rm -fr ../../doc ../pkg

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc
cp -a *.g lib tst %{buildroot}%{gap_libdir}/pkg/%{pkgname}
%gap_copy_docs

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{gap_libdir};" tst/testall.g

%files
%doc README.md
%license COPYING
%{gap_libdir}/pkg/%{pkgname}/
%exclude %{gap_libdir}/pkg/%{pkgname}/doc/

%files doc
%docdir %{gap_libdir}/pkg/%{pkgname}/doc/
%{gap_libdir}/pkg/%{pkgname}/doc/

%changelog
%autochangelog
