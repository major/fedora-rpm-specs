%global gap_pkgname crisp
%global giturl      https://github.com/bh11/crisp

Name:           gap-pkg-%{gap_pkgname}
Version:        1.4.8
Release:        %autorelease
Summary:        Computing subgroups of finite soluble groups

License:        BSD-2-Clause
URL:            http://www.icm.tu-bs.de/~bhoeflin/crisp/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/CrISP-%{version}/%{gap_upname}-%{version}.tar.bz2

BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): htm lib tst
BuildOption(check): tst/testall.g

BuildRequires:  gap-devel
BuildRequires:  tth

Requires:       gap-core

%description
CRISP (Computing with Radicals, Injectors, Schunck classes and Projectors)
provides algorithms for computing subgroups of finite soluble groups related
to group classes.  In particular, it allows computing F-radicals and
F-injectors for Fitting classes (and Fitting sets) F, F-residuals for
formations F, and X-projectors for Schunck classes X.  In order to carry out
these computations, the group classes F and X must be given by an algorithm
which decides membership in the group class.

Moreover, CRISP contains algorithms for the computation of normal subgroups
invariant under a prescribed set of automorphisms and belonging to a given
group class.  This includes an improved method to compute the set of all
normal subgroups of a finite soluble group, its characteristic subgroups, and
the socle and p-socles for given primes p.

%package doc
# The content is BSD-2-Clause.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# Nimbus: AGPL-3.0-only
# RSFS: LicenseRef-Rsfs
# StandardSymL: GPL-1.0-or-later
License:        BSD-2-Clause AND OFL-1.1-RFN AND Knuth-CTAN AND AGPL-3.0-only AND LicenseRef-Rsfs AND GPL-1.0-or-later
Summary:        CRISP documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -n %{gap_upname}-%{version}

%build
# Link to main GAP documentation
ln -s %{gap_libdir}/doc ../../doc

pushd doc
pdftex manual
makeindex -s manual.mst manual
pdftex manual
pdftex manual
popd

rm -fr htm
mkdir htm
perl %{gap_libdir}/etc/convert.pl -n CRISP -c -i -t doc htm

rm ../../doc

%files
%doc README.txt
%license LICENSE.txt
%dir %{gap_libdir}/pkg/%{gap_upname}/
%{gap_libdir}/pkg/%{gap_upname}/*.g
%{gap_libdir}/pkg/%{gap_upname}/lib/
%{gap_libdir}/pkg/%{gap_upname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{gap_upname}/doc/
%docdir %{gap_libdir}/pkg/%{gap_upname}/htm/
%{gap_libdir}/pkg/%{gap_upname}/doc/
%{gap_libdir}/pkg/%{gap_upname}/htm/

%changelog
%autochangelog
