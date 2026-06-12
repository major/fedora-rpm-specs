%global gap_pkgname permut
%global giturl      https://github.com/gap-packages/permut

Name:           gap-pkg-%{gap_pkgname}
Version:        2.0.5
Release:        %autorelease
Summary:        Permutability in finite groups for GAP

License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/permut/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{gap_upname}-%{version}.tar.bz2

BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): lib tst
BuildOption(check): tst/testall.g

BuildRequires:  gap(autodoc) >= 2019.07.17
BuildRequires:  gap(format) >= 1.3
BuildRequires:  gap-devel >= 4.7.4
BuildRequires:  gap-pkg-format-doc >= 1.3

Requires:       gap(format) >= 1.3
Requires:       gap-core >= 4.7.4

Provides:       gap(permut) = %{version}-%{release}

%description
The package permut contains some functions to deal with permutability in
finite groups.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# Nimbus: AGPL-3.0-only
# RSFS: LicenseRef-Rsfs
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND AGPL-3.0-only AND LicenseRef-Rsfs
Summary:        Permut documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
Requires:       gap-pkg-format-doc >= 1.3

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -n %{gap_upname}-%{version}

%files
%doc CHANGES README.md
%license LICENSE
%dir %{gap_libdir}/pkg/%{gap_upname}/
%{gap_libdir}/pkg/%{gap_upname}/*.g
%{gap_libdir}/pkg/%{gap_upname}/lib/
%{gap_libdir}/pkg/%{gap_upname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{gap_upname}/doc/
%{gap_libdir}/pkg/%{gap_upname}/doc/

%changelog
%autochangelog
