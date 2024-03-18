%global pkgname openmath
%global upname  OpenMath

# When bootstrapping a new architecture, there is no gap-pkg-scscp package yet.
# However, we only need that package to build documentation; it needs this
# package to function at all.  Therefore, do the following:
# 1. Build this package in bootstrap mode (the documentation has broken links)
# 2. Build gap-pkg-scscp
# 3. Build this package in non-bootstrap mode.
%bcond bootstrap 0

Name:           gap-pkg-%{pkgname}
Version:        11.5.3
Release:        %autorelease
Summary:        Import and export of OpenMath objects for GAP

License:        GPL-2.0-or-later
BuildArch:      noarch
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://gap-packages.github.io/openmath/
VCS:            https://github.com/gap-packages/openmath
Source0:        %{vcs}/releases/download/v%{version}/%{upname}-%{version}.tar.gz

%global _docdir_fmt %{name}

BuildRequires:  gap-devel
BuildRequires:  GAPDoc-latex
BuildRequires:  gap-pkg-io
%if %{without bootstrap}
BuildRequires:  gap-pkg-scscp-doc
%endif

Requires:       gap-pkg-io

%description
This package provides an OpenMath phrasebook for GAP.  It allows GAP
users to import and export mathematical objects encoded in OpenMath, for
the purpose of exchanging them with other OpenMath-enabled applications.
For details about the OpenMath encoding, see https://openmath.org/.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
License:        GPL-2.0-or-later AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        OpenMath documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%if %{without bootstrap}
Requires:       gap-pkg-scscp-doc
%endif

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{upname}-%{version}

%build
export LC_ALL=C.UTF-8

# Link to main GAP documentation
ln -s %{gap_libdir}/doc ../../doc
mkdir ../pkg
ln -s ../%{upname}-%{version} ../pkg
gap -l "$PWD/..;" makedoc.g
rm -fr ../../doc ../pkg

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{upname}/doc
cp -a *.g cds gap hasse private tst %{buildroot}%{gap_libdir}/pkg/%{upname}
%gap_copy_docs -n %{upname}

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{gap_libdir};" tst/testall.g

%files
%doc CHANGES README.md
%license COPYING
%{gap_libdir}/pkg/%{upname}/
%exclude %{gap_libdir}/pkg/%{upname}/doc/

%files doc
%doc examples
%docdir %{gap_libdir}/pkg/%{upname}/doc/
%{gap_libdir}/pkg/%{upname}/doc/

%changelog
%autochangelog
