# When bootstrapping a new architecture, there is no gap-pkg-aclib package
# yet.  It is only needed by this package to run some tests, but it requires
# this package to funtion at all.  Therefore, do this:
# 1. Build this package in bootstrap mode
# 2. Build gap-pkg-cryst in bootstrap mode
# 3. Build gap-pkg-crystcat
# 4. Build gap-pkg-aclib
# 5. Build this package in non-bootstrap mode
# 6. Build gap-pkg-cryst in non-bootstrap mode
%bcond bootstrap 0

%global gap_pkgname    polenta
%global gap_skip_check %{?with_bootstrap}
%global giturl         https://github.com/gap-packages/polenta

Name:           gap-pkg-%{gap_pkgname}
Version:        1.3.11
Release:        %autorelease
Summary:        Polycyclic presentations for matrix groups

License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/polenta/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{gap_upname}-%{version}.tar.bz2

BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): exam lib tst
BuildOption(check): tst/testall.g

%if %{without bootstrap}
BuildRequires:  gap(aclib) >= 1.0
%endif
BuildRequires:  gap(alnuth) >= 2.2.3
BuildRequires:  gap(autodoc) >= 2016.01.21
BuildRequires:  gap(polycyclic) >= 2.10.1
BuildRequires:  gap(radiroot) >= 2.4
BuildRequires:  gap-devel >= 4.7
BuildRequires:  gap-pkg-alnuth-doc >= 2.2.3

Requires:       gap(alnuth) >= 2.2.3
Requires:       gap(polycyclic) >= 2.10.1
Requires:       gap(radiroot) >= 2.4
Requires:       gap-core >= 4.7

%if %{without bootstrap}
Recommends:     gap(aclib) >= 1.0
%endif

Provides:       gap(Polenta) = %{version}-%{release}
Provides:       gap(polenta) = %{version}-%{release}

%description
The Polenta package provides methods to compute polycyclic presentations of
matrix groups (finite or infinite).  As a by-product, this package gives some
functionality to compute certain module series for modules of solvable groups.
For example, if G is a rational polycyclic matrix group, then we can compute
the radical series of the natural Q[G]-module Q^d.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Polenta documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
Requires:       gap-pkg-alnuth-doc >= 2.2.3

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -n %{gap_upname}-%{version}

%check -p
# POLENTA.tst and POLENTA2.tst require more memory than some koji builders have
# available, so we disable them.  The maintainer should run them on a machine
# with a minimum of 16 GB of RAM prior to updating to a new version.
sed -i 's/"POLENTA\.tst"/#&/;/POLENTA2/s/Add/;#&/' tst/testall.g

%files
%doc CHANGES README.md TODO
%license LICENSE
%dir %{gap_libdir}/pkg/%{gap_upname}/
%{gap_libdir}/pkg/%{gap_upname}/*.g
%{gap_libdir}/pkg/%{gap_upname}/exam/
%{gap_libdir}/pkg/%{gap_upname}/lib/
%{gap_libdir}/pkg/%{gap_upname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{gap_upname}/doc/
%{gap_libdir}/pkg/%{gap_upname}/doc/

%changelog
%autochangelog
