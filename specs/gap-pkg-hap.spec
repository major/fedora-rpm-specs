# TODO: This package wants homology, if the Pascal issues can be resolved:
# http://ljk.imag.fr/membres/Jean-Guillaume.Dumas/Homology/

# When bootstrapping a new architecture, the hapcryst package is not yet
# available.  Therefore:
# 1. Build this package in bootstrap mode.
# 2. Build gap-pkg-hapcryst.
# 3. Build this package in non-bootstrap mode.
%bcond bootstrap 0

%global gap_pkgname    hap
%global gap_skip_check %{?with_bootstrap}
%global giturl         https://github.com/gap-packages/hap

Name:           gap-pkg-%{gap_pkgname}
Version:        1.74
Release:        %autorelease
Summary:        Homological Algebra Programming for GAP

License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/hap/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/%{gap_upname}-%{version}.tar.gz
# Adapt to ImageMagick 7.x
Patch:          %{name}-imagemagick7.patch

BuildArch:      noarch
BuildSystem:    gap
BuildOption(build): --packagedirs ..
BuildOption(install): boolean date lib tst tutorial version www
# The 2G default is not enough on s390x; do not run the very slow tests
BuildOption(check): -o 3G tst/testquick.g

BuildRequires:  asymptote
BuildRequires:  gap-devel
BuildRequires:  GAPDoc-latex
BuildRequires:  gap-pkg-aclib
BuildRequires:  gap-pkg-congruence
BuildRequires:  gap-pkg-crystcat
BuildRequires:  gap-pkg-edim
BuildRequires:  gap-pkg-fga
%if %{without bootstrap}
BuildRequires:  gap-pkg-hapcryst
%endif
BuildRequires:  gap-pkg-laguna
BuildRequires:  gap-pkg-nq
BuildRequires:  gap-pkg-polycyclic
BuildRequires:  gap-pkg-polymaking
BuildRequires:  gap-pkg-singular
BuildRequires:  gap-pkg-smallgrp
BuildRequires:  graphviz
BuildRequires:  ImageMagick
BuildRequires:  perl-generators
BuildRequires:  xdg-utils

Requires:       coreutils
Requires:       gap-pkg-aclib
Requires:       gap-pkg-crystcat
Requires:       gap-pkg-fga
Requires:       gap-pkg-nq
Requires:       gap-pkg-polycyclic
Requires:       gap-pkg-smallgrp
Requires:       xdg-utils

Recommends:     asymptote
Recommends:     gap-pkg-congruence
Recommends:     gap-pkg-edim
Recommends:     gap-pkg-laguna
Recommends:     gap-pkg-polymaking
Recommends:     gap-pkg-singular

Suggests:       gap-pkg-hapcryst
Suggests:       gap-pkg-xmod
Suggests:       graphviz
Suggests:       ImageMagick
Suggests:       openssh-clients

%description
HAP is a homological algebra library for use with the GAP computer algebra
system, and is still under development.  Its initial focus is on computations
related to the cohomology of groups.  Both finite and infinite groups are
handled, with emphasis on integral coefficients.

Recent additions include some functions for computing homology of crossed
modules and simplicial groups, and also some functions for handling simplicial
complexes, cubical complexes and regular CW-complexes in the context of
topological data analysis.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
# StandardSymL: GPL-1.0-or-later
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        HAP documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -n %{gap_upname}-%{version} -p1

%conf
fixtimestamp() {
  touch -r $1.orig $1
  rm -f $1.orig
}

# Don't force the web browser to be firefox
sed -i.orig 's/"firefox"/"xdg-open"/' lib/externalSoftware.gap
fixtimestamp lib/externalSoftware.gap

# Remove obsolete files
rm -fr lib/*/*.old lib/Functors/*.ancient lib/GOuterGroups/*.trial \
  lib/Congruence/keep
find . \( -name \*keep\* -o -name \*working\* -o -name \*.swp \) -delete

# Clean up documentation to force complete rebuild
cd doc
./clean
cd -
cd tutorial
./clean
cd -

# Fix end of line encoding
sed -i.orig 's/\r//' www/SideLinks/HAPpagestyles.css
fixtimestamp www/SideLinks/HAPpagestyles.css

# Remove incorrect executable bits
chmod a-x lib/Perturbations/Gcomplexes/bsSL2Z \
          www/SideLinks/About/7dimBieberback.g

%install -a
rm -f %{buildroot}%{gap_libdir}/pkg/%{gap_upname}/tutorial/clean
rm -fr %{buildroot}%{gap_libdir}/pkg/%{gap_upname}/lib/CompiledGAP

%if %{without bootstrap}
%check -p
# Produce less chatter while running the test
polymake --reconfigure - <<< exit;
%endif

%files
%doc README.md
%license www/copyright/*.html
%dir %{gap_libdir}/pkg/%{gap_upname}/
%{gap_libdir}/pkg/%{gap_upname}/*.g
%{gap_libdir}/pkg/%{gap_upname}/boolean
%{gap_libdir}/pkg/%{gap_upname}/date
%{gap_libdir}/pkg/%{gap_upname}/lib/
%{gap_libdir}/pkg/%{gap_upname}/tst/
%{gap_libdir}/pkg/%{gap_upname}/version
%{gap_libdir}/pkg/%{gap_upname}/www/

%files doc
%docdir %{gap_libdir}/pkg/%{gap_upname}/doc/
%{gap_libdir}/pkg/%{gap_upname}/doc/
%{gap_libdir}/pkg/%{gap_upname}/tutorial/

%changelog
%autochangelog
