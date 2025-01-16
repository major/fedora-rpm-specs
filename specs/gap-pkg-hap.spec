# TODO: This package wants homology, if the Pascal issues can be resolved:
# http://ljk.imag.fr/membres/Jean-Guillaume.Dumas/Homology/

%global pkgname hap
%global giturl  https://github.com/gap-packages/hap

# When bootstrapping a new architecture, the hapcryst package is not yet
# available.  Therefore:
# 1. Build this package in bootstrap mode.
# 2. Build gap-pkg-hapcryst.
# 3. Build this package in non-bootstrap mode.
%bcond bootstrap 0

Name:           gap-pkg-%{pkgname}
Version:        1.66
Release:        %autorelease
Summary:        Homological Algebra Programming for GAP

License:        GPL-2.0-or-later
BuildArch:      noarch
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://gap-packages.github.io/hap/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/%{pkgname}-%{version}.tar.gz
# Adapt to ImageMagick 7.x
Patch:          %{name}-imagemagick7.patch
# Adapt to Singular 4.4
Patch:          %{name}-singular4.4.patch

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

# This can be removed when F40 reaches EOL
Obsoletes:      gap-pkg-happrime < 0.6-8

%description
HAP is a homological algebra library for use with the GAP computer
algebra system, and is still under development.  Its initial focus is on
computations related to the cohomology of groups.  Both finite and
infinite groups are handled, with emphasis on integral coefficients.

Recent additions include some functions for computing homology of
crossed modules and simplicial groups, and also some functions for
handling simplicial complexes, cubical complexes and regular
CW-complexes in the context of topological data analysis.

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

# This can be removed when F40 reaches EOL
Obsoletes:      gap-pkg-happrime-doc < 0.6-8

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version} -p1

%conf
fixtimestamp() {
  touch -r $1.orig $1
  rm -f $1.orig
}

# Don't force the web browser to be firefox
sed -i.orig 's/"firefox"/"xdg-open"/' lib/externalSoftware.gap
fixtimestamp lib/externalSoftware.gap

# Remove obsolete files
find . \( -name \*keep\* -o -name \*working\* -o -name \*.swp \) -delete
rm -fr lib/*/*.old lib/Functors/*.ancient lib/GOuterGroups/*.trial

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
chmod a-x lib/Kelvin/{*.xml,kelvin.gd,*.gi,init.g,tutex/*.txt} \
          lib/Khaled/init.g \
          lib/Perturbations/Gcomplexes/{*.gz,bsSL2Z} \
          www/SideLinks/About/*.g

%build
# Build the documentation
mkdir ../pkg
ln -s ../%{pkgname}-%{version} ../pkg
gap -l "$PWD/..;" makedoc.g
rm -fr ../pkg

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc
cp -a *.g boolean date lib tst tutorial version www \
   %{buildroot}%{gap_libdir}/pkg/%{pkgname}
rm -f %{buildroot}%{gap_libdir}/pkg/%{pkgname}/tutorial/clean
rm -fr %{buildroot}%{gap_libdir}/pkg/%{pkgname}/lib/CompiledGAP
%gap_copy_docs

%if %{without bootstrap}
%check
# Produce less chatter while running the test
polymake --reconfigure - <<< exit;

# Now we can run the actual test; the 2G default is not enough on s390x
# Do not run the very slow tests
gap -l '%{buildroot}%{gap_libdir};' -o 3G tst/testquick.g
%endif

%files
%doc README.md
%license www/copyright/*.html
%dir %{gap_libdir}/pkg/%{pkgname}/
%{gap_libdir}/pkg/%{pkgname}/*.g
%{gap_libdir}/pkg/%{pkgname}/boolean
%{gap_libdir}/pkg/%{pkgname}/date
%{gap_libdir}/pkg/%{pkgname}/lib/
%{gap_libdir}/pkg/%{pkgname}/tst/
%{gap_libdir}/pkg/%{pkgname}/version
%{gap_libdir}/pkg/%{pkgname}/www/

%files doc
%docdir %{gap_libdir}/pkg/%{pkgname}/doc/
%{gap_libdir}/pkg/%{pkgname}/doc/
%{gap_libdir}/pkg/%{pkgname}/tutorial/

%changelog
%autochangelog
