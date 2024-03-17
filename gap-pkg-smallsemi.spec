%global pkgname smallsemi

Name:           gap-pkg-%{pkgname}
Version:        0.6.13
Release:        %autorelease
Summary:        GAP library of small semigroups

License:        GPL-3.0-or-later
BuildArch:      noarch
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://gap-packages.github.io/smallsemi/
VCS:            https://github.com/gap-packages/smallsemi
Source0:        %{vcs}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc

Requires:       gap-core

%description
The Smallsemi package is a data library of semigroups of small size.  It
provides all semigroups with at most 8 elements as well as information
of various kinds about these objects.

%package doc
# The content is GFDL-1.1-no-invariants-or-later.  The remaining licenses cover
# the various fonts embedded in PDFs.
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
License:        GFDL-1.1-no-invariants-or-later AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Small semigroups documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

%build
export LC_ALL=C.UTF-8
gap makedoc.g

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc
cp -a *.g data gap tst %{buildroot}%{gap_libdir}/pkg/%{pkgname}
%gap_copy_docs

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{gap_libdir};" tst/testall.g

%files
%doc CHANGELOG README
%license LICENSE
%{gap_libdir}/pkg/%{pkgname}/
%exclude %{gap_libdir}/pkg/%{pkgname}/doc/

%files doc
%docdir %{gap_libdir}/pkg/%{pkgname}/doc/
%{gap_libdir}/pkg/%{pkgname}/doc/

%changelog
%autochangelog
