%global pkgname alnuth
%global giturl  https://github.com/gap-packages/alnuth

# When bootstrapping a new architecture, there is no gap-pkg-radiroot package
# yet.  It is only needed by this package to run some tests, but it requires
# this package to funtion at all.  Therefore, do this:
# 1. Build this package in bootstrap mode
# 2. Build gap-pkg-radiroot
# 3. Build this package in non-bootstrap mode
%bcond bootstrap 0

Name:           gap-pkg-%{pkgname}
Version:        3.2.1
Release:        %autorelease
Summary:        Algebraic number theory for GAP

License:        GPL-2.0-or-later
BuildArch:      noarch
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://gap-packages.github.io/alnuth/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz

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
Alnuth is an extension for the computer algebra system GAP and forms
part of a standard installation.  The functionality of Alnuth lies in
ALgebraic NUmber THeory.  It provides an interface from GAP to certain
number theoretic functions from the computer algebra system PARI/GP.
Most computations with Alnuth rely on this interface.

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
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

%build
# Link to main GAP documentation
ln -s %{gap_libdir}/etc ../../etc
ln -s %{gap_libdir}/doc ../../doc
pushd doc
./make_doc
popd
rm -f ../../{doc,etc}

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc
cp -a *.g exam gap gp htm tst %{buildroot}%{gap_libdir}/pkg/%{pkgname}
%gap_copy_docs

%if %{without bootstrap}
%check
# Tests that depend on RadiRoot will fail during a bootstrap build.
gap -l '%{buildroot}%{gap_libdir};' tst/testall.g
%endif

%files
%doc CHANGES.md README.md
%license GPL
%dir %{gap_libdir}/pkg/%{pkgname}/
%{gap_libdir}/pkg/%{pkgname}/*.g
%{gap_libdir}/pkg/%{pkgname}/exam/
%{gap_libdir}/pkg/%{pkgname}/gap/
%{gap_libdir}/pkg/%{pkgname}/gp/
%{gap_libdir}/pkg/%{pkgname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{pkgname}/doc/
%docdir %{gap_libdir}/pkg/%{pkgname}/htm/
%{gap_libdir}/pkg/%{pkgname}/doc/
%{gap_libdir}/pkg/%{pkgname}/htm/

%changelog
%autochangelog
