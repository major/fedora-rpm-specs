# When bootstrapping a new architecture, there is no gap-pkg-scscp package yet.
# However, we only need that package to build documentation; it needs this
# package to function at all.  Therefore, do the following:
# 1. Build this package in bootstrap mode (the documentation has broken links)
# 2. Build gap-pkg-scscp
# 3. Build this package in non-bootstrap mode.
%bcond bootstrap 0

%global gap_pkgname openmath
%global gap_upname  OpenMath
%global giturl      https://github.com/gap-packages/openmath

Name:           gap-pkg-%{gap_pkgname}
Version:        11.5.3
Release:        %autorelease
Summary:        Import and export of OpenMath objects for GAP

License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/openmath/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{gap_upname}-%{version}.tar.gz

%global _docdir_fmt %{name}

BuildArch:      noarch
BuildSystem:    gap
BuildOption(build): --packagedirs ..
BuildOption(install): cds gap hasse private tst
BuildOption(check): tst/testall.g

BuildRequires:  gap-devel
BuildRequires:  GAPDoc-latex
BuildRequires:  gap-pkg-io
%if %{without bootstrap}
BuildRequires:  gap-pkg-scscp-doc
%endif

Requires:       gap-pkg-io

%description
This package provides an OpenMath phrasebook for GAP.  It allows GAP users to
import and export mathematical objects encoded in OpenMath, for the purpose of
exchanging them with other OpenMath-enabled applications.  For details about
the OpenMath encoding, see https://openmath.org/.

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
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -n %{gap_upname}-%{version}

%build -p
# Link to main GAP documentation
ln -s %{gap_libdir}/doc ../../doc

%files
%doc CHANGES README.md
%license COPYING
%dir %{gap_libdir}/pkg/%{gap_upname}/
%{gap_libdir}/pkg/%{gap_upname}/*.g
%{gap_libdir}/pkg/%{gap_upname}/cds/
%{gap_libdir}/pkg/%{gap_upname}/gap/
%{gap_libdir}/pkg/%{gap_upname}/hasse/
%{gap_libdir}/pkg/%{gap_upname}/private/
%{gap_libdir}/pkg/%{gap_upname}/tst/

%files doc
%doc examples
%docdir %{gap_libdir}/pkg/%{gap_upname}/doc/
%{gap_libdir}/pkg/%{gap_upname}/doc/

%changelog
%autochangelog
