%global gap_pkgname laguna
%global giturl      https://github.com/gap-packages/laguna

Name:           gap-pkg-%{gap_pkgname}
Version:        3.9.7
Release:        %autorelease
Summary:        Lie AlGebras and UNits of group Algebras

License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/laguna/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{gap_upname}-%{version}.tar.gz

BuildArch:      noarch
BuildSystem:    gap
BuildOption(build): --packagedirs ..
BuildOption(install): lib tst
BuildOption(check): tst/testall.g

BuildRequires:  gap-devel
BuildRequires:  GAPDoc-latex
BuildRequires:  gap-pkg-sophus

Requires:       gap-core

Recommends:     gap-pkg-sophus

%description
The LAGUNA package replaces the LAG package and provides functionality for
calculation of the normalized unit group of the modular group algebra of the
finite p-group and for investigation of Lie algebra associated with group
algebras and other associative algebras.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
# StandardSymL: GPL-1.0-or-later
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        LAGUNA documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -n %{gap_upname}-%{version}

%conf
# Fix end of line encodings
sed -i 's/\r/\n/g' doc/theory.xml

%files
%doc ChangeLog README.md
%license COPYING
%dir %{gap_libdir}/pkg/%{gap_upname}/
%{gap_libdir}/pkg/%{gap_upname}/*.g
%{gap_libdir}/pkg/%{gap_upname}/lib/
%{gap_libdir}/pkg/%{gap_upname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{gap_upname}/doc/
%{gap_libdir}/pkg/%{gap_upname}/doc/

%changelog
%autochangelog
