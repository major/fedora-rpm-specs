%global gap_pkgname xmod
%global gap_upname  XMod
%global giturl      https://github.com/gap-packages/xmod

Name:           gap-pkg-%{gap_pkgname}
Version:        2.95
Release:        %autorelease
Summary:        Crossed Modules and Cat1-Groups for GAP

License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/xmod/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{gap_upname}-%{version}.tar.gz

BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): examples lib tst
BuildOption(check): tst/testall.g

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-autpgrp
BuildRequires:  gap-pkg-crisp
BuildRequires:  gap-pkg-groupoids
BuildRequires:  gap-pkg-hap
BuildRequires:  gap-pkg-nq
BuildRequires:  gap-pkg-smallgrp
BuildRequires:  gap-pkg-utils
BuildRequires:  tex(xy.sty)

Requires:       gap-pkg-autpgrp
Requires:       gap-pkg-crisp
Requires:       gap-pkg-groupoids
Requires:       gap-pkg-hap
Requires:       gap-pkg-smallgrp
Requires:       gap-pkg-utils

%description
This package allows for computation with crossed modules, cat1-groups,
morphisms of these structures, derivations of crossed modules and the
corresponding sections of cat1-groups.  Experimental functions for crossed
squares are now included.  In October 2015 a new section on isoclinism of
crossed modules was added.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
# RSFS: LicenseRef-Rsfs
# StandardSymL: GPL-1.0-or-later
# XY: GPL-1.0-or-later
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only AND LicenseRef-Rsfs
Summary:        XMod documentation
Requires:       %{name} = %{version}-%{release}
Requires:       GAPDoc-doc

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -n %{gap_upname}-%{version} -p1

%files
%doc CHANGES.md README.md
%license LICENSE.txt
%dir %{gap_libdir}/pkg/%{gap_upname}/
%{gap_libdir}/pkg/%{gap_upname}/*.g
%{gap_libdir}/pkg/%{gap_upname}/lib/
%{gap_libdir}/pkg/%{gap_upname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{gap_upname}/doc/
%docdir %{gap_libdir}/pkg/%{gap_upname}/examples/
%{gap_libdir}/pkg/%{gap_upname}/doc/
%{gap_libdir}/pkg/%{gap_upname}/examples/

%changelog
%autochangelog
