%global gap_pkgname backtrackkit
%global gap_upname  BacktrackKit
%global giturl      https://github.com/peal/BacktrackKit

Name:           gap-pkg-%{gap_pkgname}
Version:        1.1.0
Release:        %autorelease
Summary:        Implementation of Jeffrey Leon's Partition Backtrack framework

License:        MPL-2.0
URL:            https://peal.github.io/BacktrackKit/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/%{gap_upname}-%{version}.tar.gz

BuildArch:      noarch
BuildSystem:    gap
BuildOption(build): --packagedirs ..
BuildOption(install): examples gap tst
BuildOption(check): tst/testall.g

BuildRequires:  gap(autodoc) >= 2019.09.04
BuildRequires:  gap(datastructures) >= 0.2.6
BuildRequires:  gap(digraphs) >= 1.1.1
BuildRequires:  gap(images) >= 1.3.0
BuildRequires:  gap(primgrp) >= 3.4.0
BuildRequires:  gap(quickcheck)
BuildRequires:  gap-devel >= 4.13

Requires:       gap(datastructures) >= 0.2.6
Requires:       gap(digraphs) >= 1.1.1
Requires:       gap(images) >= 1.3.0
Requires:       gap(primgrp) >= 3.4.0
Requires:       gap-core >= 4.13

Provides:       gap(BacktrackKit) = %{version}-%{release}
Provides:       gap(backtrackkit) = %{version}-%{release}

%description
This package provides a simple implementation of Leon's partition backtrack
framework.

This package is intended to be a package for learning the algorithms of
partition backtrack, and the performance is extremely poor -- orders of
magnitude slower than the algorithms in GAP.  If you want to see a modern,
high-performance extension to partition backtrack, look at the vole package.

%package doc
# The content is MPL-2.0.  The remaining licenses cover the various fonts
# embedded in PDFs.
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
# StandardSymL: GPL-1.0-or-later
License:        MPL-2.0 AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        BacktrackKit documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -n %{gap_upname}-%{version}

%files
%doc README.md
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
