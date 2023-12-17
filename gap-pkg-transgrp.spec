%global pkgname transgrp

Name:           gap-pkg-%{pkgname}
Version:        3.6.5
Release:        1%{?dist}
Summary:        Transitive groups library

# Artistic-2.0: presentation of the data in the data files
# GPL-2.0-only OR GPL-3.0-only: the code
License:        Artistic-2.0 AND (GPL-2.0-only OR GPL-3.0-only)
BuildArch:      noarch
ExclusiveArch:  %{gap_arches} noarch
URL:            https://www.gap-system.org/Packages/transgrp.html
Source0:        https://www.math.colostate.edu/~hulpke/transgrp/%{pkgname}%{version}.tar.gz
Source1:        https://www.math.colostate.edu/~hulpke/transgrp/trans32.tgz

BuildRequires:  gap-devel
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

# There is no ext manual anymore
sed -i '/UseReferences.*ext/d' doc/manual.tex

%build
export LC_ALL=C.UTF-8

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
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{gap_libdir};" --bare -c 'LoadPackage("GAPDoc");' tst/testall.g

%files
%doc README.md
%license LICENSE
%{gap_libdir}/pkg/%{pkgname}/
%exclude %{gap_libdir}/pkg/%{pkgname}/data/
%exclude %{gap_libdir}/pkg/%{pkgname}/dat32/
%exclude %{gap_libdir}/pkg/%{pkgname}/doc/
%exclude %{gap_libdir}/pkg/%{pkgname}/htm/

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
* Fri Dec 15 2023 Jerry James <loganjerry@gmail.com> - 3.6.5-1
- Version 3.6.5

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Apr  5 2023 Jerry James <loganjerry@gmail.com> - 3.6.4-1
- Version 3.6.4
- Add Artistic-2.0 to License

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Jerry James <loganjerry@gmail.com> - 3.6.3-4
- Update for split GAP directories

* Thu Nov 10 2022 Jerry James <loganjerry@gmail.com> - 3.6.3-3
- Use upstream's method of bootstrapping
- Clarify license of the doc subpackage

* Mon Sep 26 2022 Jerry James <loganjerry@gmail.com> - 3.6.3-3
- Update for gap 4.12.0
- Convert License tags to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Jerry James <loganjerry@gmail.com> - 3.6.3-1
- Version 3.6.3

* Mon May  9 2022 Jerry James <loganjerry@gmail.com> - 3.6.2-1
- Version 3.6.2

* Sat Apr  2 2022 Jerry James <loganjerry@gmail.com> - 3.6.1-1
- Version 3.6.1

* Sat Apr  2 2022 Jerry James <loganjerry@gmail.com> - 3.6-1
- Version 3.6

* Fri Feb 11 2022 Jerry James <loganjerry@gmail.com> - 3.5-1
- Version 3.5

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun  8 2021 Jerry James <loganjerry@gmail.com> - 3.3-1
- Version 3.3

* Mon May 17 2021 Jerry James <loganjerry@gmail.com> - 3.2-1
- Version 3.2

* Tue Apr  6 2021 Jerry James <loganjerry@gmail.com> - 3.1-1
- Version 3.1

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug  1 2020 Jerry James <loganjerry@gmail.com> - 3.0-1
- Version 3.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 25 2020 Jerry James <loganjerry@gmail.com> - 2.0.5-1
- Version 2.0.5

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 13 2019 Jerry James <loganjerry@gmail.com> - 2.0.4-2
- Remove hidden file

* Fri Feb  1 2019 Jerry James <loganjerry@gmail.com> - 2.0.4-1
- Initial RPM
