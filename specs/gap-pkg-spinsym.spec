%global gap_pkgname spinsym
%global giturl      https://github.com/gap-packages/spinsym

Name:           gap-pkg-%{gap_pkgname}
Version:        1.5.2
Release:        %autorelease
Summary:        GAP package for Brauer tables of spin-symmetric groups

License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/spinsym/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{gap_upname}-%{version}.tar.gz

BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): gap symdata tst
BuildOption(check): tst/testall.g

BuildRequires:  gap(autodoc) >= 2016.01.21
BuildRequires:  gap(ctbllib) >= 1.2.2
BuildRequires:  gap(gapdoc) >= 1.5
BuildRequires:  gap-devel >= 4.5

Requires:       gap(ctbllib) >= 1.2.2
Requires:       gap-core >= 4.5

Provides:       gap(SpinSym) = %{version}-%{release}
Provides:       gap(spinsym) = %{version}-%{release}

%description
This package contains some p-modular character tables of Schur covers of
symmetric and alternating groups.  It also provides some more functionalities
related to these groups, for example, a method to construct character tables
of their maximal Young subgroups.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
# StandardSymL: GPL-1.0-or-later
License:        GPL-2.0-or-later AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        SpinSym documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -n %{gap_upname}-%{version}

%files
%doc README
%license LICENSE
%dir %{gap_libdir}/pkg/%{gap_upname}/
%{gap_libdir}/pkg/%{gap_upname}/*.g
%{gap_libdir}/pkg/%{gap_upname}/gap/
%{gap_libdir}/pkg/%{gap_upname}/symdata/
%{gap_libdir}/pkg/%{gap_upname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{gap_upname}/doc/
%{gap_libdir}/pkg/%{gap_upname}/doc/

%changelog
%autochangelog
