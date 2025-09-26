%global gap_pkgname transgrp

Name:           gap-pkg-%{gap_pkgname}
Version:        3.6.5
Release:        %autorelease
Summary:        Transitive groups library

License:        GPL-2.0-only OR GPL-3.0-only
URL:            https://www.gap-system.org/Packages/transgrp.html
VCS:            git:https://github.com/hulpke/transgrp.git
Source:         https://www.math.colostate.edu/~hulpke/transgrp/%{gap_upname}%{version}.tar.gz

BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): data htm lib tst
BuildOption(check): --bare -c 'LoadPackage("GAPDoc");LoadPackage("smallgrp");' tst/testall.g

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-smallgrp
BuildRequires:  GAPDoc-latex
BuildRequires:  tth

Requires:       gap-core
Requires:       %{name}-data = %{version}-%{release}

%description
A library of transitive groups.  This package contains the code for
accessing the library.  The actual data is in the data subpackage.

%package data
Summary:        Data files for groups of degree other than 32 and 48
License:        Artistic-2.0
Requires:       %{name} = %{version}-%{release}

# This can be removed when Fedora 46 reaches EOL
Obsoletes:      %{name}-data32 < 3.6.5-11

%description data
This package contains a library of transitive groups.  Groups of degree 15-30
are due to Alexander Hulpke.  Groups of degree 32 are due to John Cannon and
Derek Holt.  Groups of degree 34-48 are due to Derek Holt and Gordon Royle.
Not all degrees greater than 30 are yet available.

Groups of degree 32 are not included in Fedora due to the large size of the
file (about 266 MB).  Download it separately from
https://www.math.colostate.edu/~hulpke/transgrp/trans32.tgz if you need it.

Groups of degree 48 are not included in Fedora due to the large size of the
file (about 30 GB).  Download it separately from
https://zenodo.org/record/5935751 if you need it.

%package doc
# The content is GPL-2.0-only OR GPL-3.0-only.  The remaining licenses cover
# the various fonts embedded in PDFs.  Note that Artistic-2.0 is omitted
# since that covers the data files only.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# Nimbus: AGPL-3.0-only
License:        (GPL-2.0-only OR GPL-3.0-only) AND OFL-1.1-RFN AND Knuth-CTAN AND AGPL-3.0-only
Summary:        Transitive groups library documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -n %{gap_upname}

%conf
# There is no ext manual anymore
sed -i '/UseReferences.*ext/d' doc/manual.tex

%build
# Build the documentation
mkdir ../../doc
ln -s %{gap_libdir}/doc/ref ../../doc
cd doc
ln -s %{gap_libdir}/etc/convert.pl .
ln -s %{gap_libdir}/doc/gapmacro.tex .
ln -s %{gap_libdir}/doc/manualindex .
./make_doc
cd -
rm -fr ../../doc doc/{convert.pl,gapmacro.tex,manualindex}

%files
%doc README.md
%license LICENSE
%dir %{gap_libdir}/pkg/%{gap_upname}/
%{gap_libdir}/pkg/%{gap_upname}/*.g
%{gap_libdir}/pkg/%{gap_upname}/lib/
%{gap_libdir}/pkg/%{gap_upname}/tst/

%files data
%{gap_libdir}/pkg/%{gap_upname}/data/

%files doc
%docdir %{gap_libdir}/pkg/%{gap_upname}/doc/
%docdir %{gap_libdir}/pkg/%{gap_upname}/htm/
%{gap_libdir}/pkg/%{gap_upname}/doc/
%{gap_libdir}/pkg/%{gap_upname}/htm/

%changelog
%autochangelog
