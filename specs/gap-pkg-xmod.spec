%global pkgname XMod
%global giturl  https://github.com/gap-packages/xmod

Name:           gap-pkg-xmod
Version:        2.92
Release:        %autorelease
Summary:        Crossed Modules and Cat1-Groups for GAP

License:        GPL-2.0-or-later
BuildArch:      noarch
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://gap-packages.github.io/xmod/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz

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
corresponding sections of cat1-groups.  Experimental functions for
crossed squares are now included.  In October 2015 a new section on
isoclinism of crossed modules was added.

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
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version} -p1

%build
gap makedoc.g

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc
cp -a *.g examples lib tst %{buildroot}%{gap_libdir}/pkg/%{pkgname}
%gap_copy_docs

%check
gap -l '%{buildroot}%{gap_libdir};' tst/testall.g

%files
%doc CHANGES.md README.md
%license LICENSE.txt
%dir %{gap_libdir}/pkg/%{pkgname}/
%{gap_libdir}/pkg/%{pkgname}/*.g
%{gap_libdir}/pkg/%{pkgname}/lib/
%{gap_libdir}/pkg/%{pkgname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{pkgname}/doc/
%docdir %{gap_libdir}/pkg/%{pkgname}/examples/
%{gap_libdir}/pkg/%{pkgname}/doc/
%{gap_libdir}/pkg/%{pkgname}/examples/

%changelog
%autochangelog
