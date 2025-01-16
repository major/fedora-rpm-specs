%global pkgname crystcat

Name:           gap-pkg-%{pkgname}
Version:        1.1.10
Release:        %autorelease
Summary:        Crystallographic groups catalog

License:        GPL-2.0-or-later
BuildArch:      noarch
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://www.math.uni-bielefeld.de/~gaehler/gap/packages.php
VCS:            git:https://github.com/gap-packages/crystcat.git
Source:         https://www.math.uni-bielefeld.de/~gaehler/gap/CrystCat/%{pkgname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-cryst-doc
BuildRequires:  tth

Requires:       gap-pkg-cryst

%description
The GAP 4 package CrystCat provides a catalog of crystallographic groups
of dimensions 2, 3, and 4 which covers most of the data contained in the
book "Crystallographic groups of four-dimensional space" by H. Brown, R.
Bülow, J. Neubüser, H. Wondratschek, and H. Zassenhaus (John Wiley, New
York, 1978).  This catalog was previously available in the library of
GAP 3.  The present version for GAP 4 has been moved into a separate
package, because it requires the package Cryst, which is loaded
automatically by CrystCat.  The benefit of this is that space groups
extracted from the catalog now have the rich set of methods provided by
Cryst at their disposal, and are no longer dumb lists of generators.
Moreover, space groups are now fully supported in both the
representation acting from the left and the representation acting from
the right.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# Nimbus: AGPL-3.0-only
# StandardSymL: GPL-1.0-or-later
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND AGPL-3.0-only AND GPL-1.0-or-later
Summary:        CrystCat documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-pkg-cryst-doc

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}

%build
# Link to main GAP documentation
ln -s %{gap_libdir}/etc ../../etc
ln -s %{gap_libdir}/doc ../../doc
ln -s %{gap_libdir}/pkg/cryst ..
pushd doc
./make_doc
popd
rm -f ../../{doc,etc} ../cryst

# Compress large group files
gzip --best grp/crystcat.grp

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc
cp -a *.g grp htm lib tst %{buildroot}%{gap_libdir}/pkg/%{pkgname}
%gap_copy_docs

%check
gap -l '%{buildroot}%{gap_libdir};' tst/testall.g

%files
%doc Changelog README
%license GPL
%dir %{gap_libdir}/pkg/%{pkgname}/
%{gap_libdir}/pkg/%{pkgname}/*.g
%{gap_libdir}/pkg/%{pkgname}/grp/
%{gap_libdir}/pkg/%{pkgname}/lib/
%{gap_libdir}/pkg/%{pkgname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{pkgname}/doc/
%docdir %{gap_libdir}/pkg/%{pkgname}/htm/
%{gap_libdir}/pkg/%{pkgname}/doc/
%{gap_libdir}/pkg/%{pkgname}/htm/

%changelog
%autochangelog
