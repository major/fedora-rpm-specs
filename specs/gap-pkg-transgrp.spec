%global pkgname transgrp

Name:           gap-pkg-%{pkgname}
Version:        3.6.5
Release:        %autorelease
Summary:        Transitive groups library

# Artistic-2.0: presentation of the data in the data files
# GPL-2.0-only OR GPL-3.0-only: the code
License:        Artistic-2.0 AND (GPL-2.0-only OR GPL-3.0-only)
BuildArch:      noarch
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://www.gap-system.org/Packages/transgrp.html
VCS:            git:https://github.com/hulpke/transgrp.git
Source0:        https://www.math.colostate.edu/~hulpke/transgrp/%{pkgname}%{version}.tar.gz
Source1:        https://www.math.colostate.edu/~hulpke/transgrp/trans32.tgz

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-smallgrp
BuildRequires:  GAPDoc-latex
BuildRequires:  parallel
BuildRequires:  tth

Requires:       gap-core
Requires:       %{name}-data = %{version}-%{release}

%description
A library of transitive groups.  This package contains the code for
accessing the library.  The actual data is in the data and data32
subpackages.

%package data
Summary:        Data files for groups of degree other than 32 and 48
License:        Artistic-2.0
Requires:       %{name} = %{version}-%{release}

%description data
This package contains a library of transitive groups.  Groups of degree
15-30 are due to Alexander Hulpke.  Groups of degree 32 are due to John
Cannon and Derek Holt.  Groups of degree 34-48 are due to Derek Holt and
Gordon Royle.  Not all degrees greater than 30 are yet available.

Groups of degree 32 are available in the gap-pkg-data32 package.

Groups of degree 48 are not included in Fedora due to the large size of
the file (about 30 GB).  Download it separately from
https://zenodo.org/record/5935751 if you need it.

%package data32
Summary:        Library of transitive groups of degree 32
License:        Artistic-2.0
Requires:       %{name} = %{version}-%{release}

%description data32
This package contains a library of transitive groups of degree 32, due
to John Cannon and Derek Holt.

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
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname} -a 1

%conf
# There is no ext manual anymore
sed -i '/UseReferences.*ext/d' doc/manual.tex

%build
# Compress large group files
parallel %{?_smp_mflags} --no-notice gzip --best ::: dat32/*.grp

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

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc
cp -a *.g data dat32 htm lib tst %{buildroot}%{gap_libdir}/pkg/%{pkgname}
%gap_copy_docs

%check
gap -l '%{buildroot}%{gap_libdir};' --bare -c 'LoadPackage("GAPDoc");LoadPackage("smallgrp");' tst/testall.g

%files
%doc README.md
%license LICENSE
%dir %{gap_libdir}/pkg/%{pkgname}/
%{gap_libdir}/pkg/%{pkgname}/*.g
%{gap_libdir}/pkg/%{pkgname}/lib/
%{gap_libdir}/pkg/%{pkgname}/tst/

%files data
%{gap_libdir}/pkg/%{pkgname}/data/

%files data32
%{gap_libdir}/pkg/%{pkgname}/dat32/

%files doc
%docdir %{gap_libdir}/pkg/%{pkgname}/doc/
%docdir %{gap_libdir}/pkg/%{pkgname}/htm/
%{gap_libdir}/pkg/%{pkgname}/doc/
%{gap_libdir}/pkg/%{pkgname}/htm/

%changelog
%autochangelog
