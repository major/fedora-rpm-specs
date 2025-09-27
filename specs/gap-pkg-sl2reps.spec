%global gap_pkgname sl2reps
%global giturl      https://github.com/snw-0/sl2-reps

Name:           gap-pkg-%{gap_pkgname}
Version:        1.1
Release:        %autorelease
Summary:        Construct representations of SL(2,Z)

License:        GPL-2.0-or-later
URL:            https://snw-0.github.io/sl2-reps/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/sl2-reps-%{version}.tar.gz

BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): gap tst
BuildOption(check): tst/testall.g

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc

Requires:       gap-core

%description
This package provides methods for constructing and testing matrix
presentations of the representations of SL(2,Z) whose kernels are congruence
subgroups of SL(2,Z).

Irreducible representations of prime-power level are constructed individually
by using the Weil representations of quadratic modules, and from these a list
of all representations of a given degree or level can be produced.  The format
is designed for the study of modular tensor categories in particular,
providing symmetric matrix presentations of each representation.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
# StandardSymL: GPL-1.0-or-later
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        SL2Reps documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -n sl2-reps-%{version}

%files
%doc README.md
%license LICENSE.txt
%dir %{gap_libdir}/pkg/%{gap_upname}/
%{gap_libdir}/pkg/%{gap_upname}/*.g
%{gap_libdir}/pkg/%{gap_upname}/gap/
%{gap_libdir}/pkg/%{gap_upname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{gap_upname}/doc/
%{gap_libdir}/pkg/%{gap_upname}/doc/

%changelog
%autochangelog
