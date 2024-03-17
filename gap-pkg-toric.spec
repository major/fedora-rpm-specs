%global pkgname toric
%global upname  Toric

Name:           gap-pkg-%{pkgname}
Version:        1.9.5
Release:        %autorelease
Summary:        Computations with toric varieties in GAP

License:        MIT
BuildArch:      noarch
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://gap-packages.github.io/toric/
VCS:            https://github.com/gap-packages/toric
Source0:        %{vcs}/releases/download/v%{version}/%{upname}-%{version}.tar.gz
# Fix a misplaced comma and other problems in a BibTeX entry
# https://github.com/gap-packages/toric/pull/12
Patch0:         0001-Fix-problems-with-the-Gua05-BibTeX-entry.patch

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc

Requires:       gap-core

%description
Toric implements some computations related to toric varieties and
combinatorial geometry in GAP.  Affine toric varieties can be created
and related information about them can be calculated.

%package doc
# The content is MIT.  The remaining licenses cover the various fonts embedded
# in PDFs.
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
# StandardSymL: GPL-1.0-or-later
License:        MIT AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Toric documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -p1 -n %{upname}-%{version}

# Linux filesystems are case-sensitive
mv doc/toric.xml doc/Toric.xml

%build
export LC_ALL=C.UTF-8
gap makedoc.g

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{upname}/doc
cp -a *.g lib tst %{buildroot}%{gap_libdir}/pkg/%{upname}
%gap_copy_docs -n %{upname}

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{gap_libdir};" tst/testall.g

%files
%doc CHANGES README.md
%license LICENSE
%{gap_libdir}/pkg/%{upname}/
%exclude %{gap_libdir}/pkg/%{upname}/doc

%files doc
%docdir %{gap_libdir}/pkg/%{upname}/doc/
%{gap_libdir}/pkg/%{upname}/doc/

%changelog
%autochangelog
