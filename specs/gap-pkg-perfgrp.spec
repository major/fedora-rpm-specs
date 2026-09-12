%global gap_pkgname perfgrp
%global giturl      https://github.com/gap-packages/perfgrp

Name:           gap-pkg-%{gap_pkgname}
Version:        1.0.0
Release:        %autorelease
Summary:        GAP Library of Finite Perfect Groups

License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/perfgrp/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/v%{version}/%{gap_upname}-%{version}.tar.gz
# Predownloaded data from ATLAS needed for the tests
# To generate, supply an empty tarball, then run the build with the network
# enabled; e.g., by running mock with --enable-network.  Then run
# `tar -cJf %%{name}-testdata.tar.xz %%{_builddir}/atlasrep`.
Source1:        %{name}-testdata.tar.xz

BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): data gap tst
BuildOption(check): tst/testall.g

BuildRequires:  gap(atlasrep)
BuildRequires:  gap(autodoc) >= 2019.04.10
BuildRequires:  gap-devel >= 4.15
BuildRequires:  parallel

Requires:       gap-core >= 4.15

Provides:       gap(PerfGrp) = %{version}-%{release}
Provides:       gap(perfgrp) = %{version}-%{release}

%description
The GAP library of finite perfect groups provides, up to isomorphism, a list
of all perfect groups whose sizes are less than 2,000,000.  The groups of
orders up to 10^6 have been enumerated by Derek F. Holt and Wilhelm Plesken
and published in their book "Perfect Groups" (Oxford University Press, 1989).
The remaining groups were enumerated by Alexander Hulpke, `The perfect groups
of order up to two million`, Math. Comp. **91** (2022), no. 334, 1007-1017,
https://doi.org/10.1090/mcom/3684.

In addition, this package provides methods for computing the perfect and
simple subgroups of a finite group, via the attributes
RepresentativesPerfectSubgroups, RepresentativesSimpleSubgroups and
ConjugacyClassesPerfectSubgroups.

This code used to be part of the GAP core system, and was moved into a
separate package to reduce the size of the GAP distribution and to allow
independent updates of the data.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# font embedded in PDFs.
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
License:        MPL-2.0 AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        PerfGrp documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -n %{gap_upname}-%{version} -b 1

%build -a
# Compress large tables
parallel %{?_smp_mflags} --no-notice gzip --best ::: data/*.grp

%check -p
# Tell ATLAS where to find downloaded files
mkdir ~/.gap
cat > ~/.gap/gap.ini << EOF
SetUserPreference( "AtlasRep", "AtlasRepDataDirectory", "%{_builddir}/atlasrep/" );
EOF

%files
%doc README.md
%license LICENSE
%dir %{gap_libdir}/pkg/%{gap_upname}/
%{gap_libdir}/pkg/%{gap_upname}/*.g
%{gap_libdir}/pkg/%{gap_upname}/data/
%{gap_libdir}/pkg/%{gap_upname}/gap/
%{gap_libdir}/pkg/%{gap_upname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{gap_upname}/doc/
%{gap_libdir}/pkg/%{gap_upname}/doc/

%changelog
%autochangelog
