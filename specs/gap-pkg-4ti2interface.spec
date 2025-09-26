%global gap_pkgname 4ti2interface
%global gap_upname  4ti2Interface
%global upver       2024.11-01
%global giturl      https://github.com/homalg-project/homalg_project

Name:           gap-pkg-%{gap_pkgname}
Version:        %(tr - . <<< %{upver})
Release:        %autorelease
Summary:        GAP interface to 4ti2

License:        GPL-2.0-or-later
URL:            https://homalg-project.github.io/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/%{gap_upname}-%{upver}.tar.gz
# Adapt to the Fedora 4ti2 package use of environment modules
Patch:          %{name}-binaries.patch

BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): examples gap tst
BuildOption(check): tst/testall.g

BuildRequires:  4ti2
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-io

Requires:       4ti2
Requires:       gap-pkg-io

%description
This package is a GAP interface to 4ti2.

%package doc
# The content is GPL-2.0-or-later.
# The remaining licenses cover the various fonts embedded in PDFs:
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
License:        GPL-2.0-or-later AND GPL-1.0-or-later AND Knuth-CTAN AND AGPL-3.0-only
Summary:        Documentation for the GAP 4ti2Interface package
Requires:       %{name} = %{version}-%{release}

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -n homalg_project-%{gap_upname}-%{upver}/%{gap_upname} -p1

%files
%doc README.md
%license LICENSE
%dir %{gap_libdir}/pkg/%{gap_upname}/
%{gap_libdir}/pkg/%{gap_upname}/*.g
%{gap_libdir}/pkg/%{gap_upname}/gap/
%{gap_libdir}/pkg/%{gap_upname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{gap_upname}/doc/
%docdir %{gap_libdir}/pkg/%{gap_upname}/examples/
%{gap_libdir}/pkg/%{gap_upname}/doc/
%{gap_libdir}/pkg/%{gap_upname}/examples/

%changelog
%autochangelog
