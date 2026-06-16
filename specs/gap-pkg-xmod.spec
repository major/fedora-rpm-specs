%global gap_pkgname xmod
%global gap_upname  XMod
%global giturl      https://github.com/gap-packages/xmod

Name:           gap-pkg-%{gap_pkgname}
Version:        2.98
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

BuildRequires:  gap(autodoc)
BuildRequires:  gap(autpgrp) >= 1.10.2
BuildRequires:  gap(groupoids) >= 1.78
BuildRequires:  gap(hap) >= 1.29
BuildRequires:  gap(smallgrp) >= 1.4.2
BuildRequires:  gap(utils) >= 0.81
BuildRequires:  gap-devel >= 4.11.0
BuildRequires:  tex(xy.sty)

Requires:       gap(autpgrp) >= 1.10.2
Requires:       gap(groupoids) >= 1.78
Requires:       gap(hap) >= 1.29
Requires:       gap(smallgrp) >= 1.4.2
Requires:       gap(utils) >= 0.81
Requires:       gap-core >= 4.11.0

Provides:       gap(xmod) = %{version}-%{release}
Provides:       gap(XMod) = %{version}-%{release}

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
Requires:       gap-online-help

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
