# When bootstrapping a new architecture, there is no gap-pkg-radiroot package
# yet.  It is only needed by this package to run some tests, but it requires
# this package to funtion at all.  Therefore, do this:
# 1. Build this package in bootstrap mode
# 2. Build gap-pkg-radiroot
# 3. Build this package in non-bootstrap mode
%bcond bootstrap 0

%global gap_pkgname    alnuth
%global gap_skip_check %{?with_bootstrap}
%global giturl         https://github.com/gap-packages/alnuth

Name:           gap-pkg-%{gap_pkgname}
Version:        3.2.1
Release:        %autorelease
Summary:        Algebraic number theory for GAP

License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/alnuth/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{gap_upname}-%{version}.tar.gz

BuildArch:      noarch
BuildSystem:    gap
BuildOption(build): --packagedirs ..
BuildOption(install): exam gap gp htm tst
BuildOption(check): tst/testall.g

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-polycyclic
%if %{without bootstrap}
BuildRequires:  gap-pkg-radiroot
%endif
BuildRequires:  pari-gp
BuildRequires:  tth

Requires:       gap-pkg-polycyclic
Requires:       pari-gp

%description
Alnuth is an extension for the computer algebra system GAP and forms part of a
standard installation.  The functionality of Alnuth lies in ALgebraic NUmber
THeory.  It provides an interface from GAP to certain number theoretic
functions from the computer algebra system PARI/GP.  Most computations with
Alnuth rely on this interface.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# Nimbus: AGPL-3.0-only
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND AGPL-3.0-only
Summary:        Alnuth documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -n %{gap_upname}-%{version}

%build
# Link to main GAP documentation
ln -s %{gap_libdir}/etc ../../etc
ln -s %{gap_libdir}/doc ../../doc
cd doc
./make_doc
cd -
rm -f ../../{doc,etc}

%files
%doc CHANGES.md README.md
%license GPL
%dir %{gap_libdir}/pkg/%{gap_upname}/
%{gap_libdir}/pkg/%{gap_upname}/*.g
%{gap_libdir}/pkg/%{gap_upname}/exam/
%{gap_libdir}/pkg/%{gap_upname}/gap/
%{gap_libdir}/pkg/%{gap_upname}/gp/
%{gap_libdir}/pkg/%{gap_upname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{gap_upname}/doc/
%docdir %{gap_libdir}/pkg/%{gap_upname}/htm/
%{gap_libdir}/pkg/%{gap_upname}/doc/
%{gap_libdir}/pkg/%{gap_upname}/htm/

%changelog
%autochangelog
