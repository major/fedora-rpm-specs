%global pkgname transgrp

Name:           gap-pkg-%{pkgname}
Version:        3.6.3
Release:        2%{?dist}
Summary:        Transitive groups library
BuildArch:      noarch

License:        GPLv2 or GPLv3
URL:            https://www.gap-system.org/Packages/%{pkgname}.html
Source0:        https://www.math.colostate.edu/~hulpke/%{pkgname}/%{pkgname}%{version}.tar.gz
Source1:        https://www.math.colostate.edu/~hulpke/%{pkgname}/trans32.tgz

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
Summary:        Data files for groups of degree other than 32
License:        Artistic 2.0
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
License:        Artistic 2.0
Requires:       %{name} = %{version}-%{release}

%description data32
This package contains a library of transitive groups of degree 32, due
to John Cannon and Derek Holt.

%package doc
Summary:        Transitive groups library documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname} -a 1

%build
# Compress large group files
parallel %{?_smp_mflags} --no-notice gzip --best ::: dat32/*.grp data/*.grp

# Build the documentation
mkdir ../../doc
ln -s %{_gap_dir}/doc/ref ../../doc
cd doc
ln -s %{_gap_dir}/etc/convert.pl .
ln -s %{_gap_dir}/doc/gapmacro.tex .
ln -s %{_gap_dir}/doc/manualindex .
./make_doc
cd -
rm -fr ../../doc doc/{convert.pl,gapmacro.tex,manualindex}

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg/%{pkgname}
cp -a *.g data dat32 doc htm lib tst %{buildroot}%{_gap_dir}/pkg/%{pkgname}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}/doc/make_doc
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}/doc/*.{aux,bbl,blg,idx,ilg,ind,log,out,pnr}

%check
gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" < tst/testall.g

%files
%doc README.md
%license LICENSE
%{_gap_dir}/pkg/%{pkgname}/
%exclude %{_gap_dir}/pkg/%{pkgname}/data/
%exclude %{_gap_dir}/pkg/%{pkgname}/dat32/
%exclude %{_gap_dir}/pkg/%{pkgname}/doc/
%exclude %{_gap_dir}/pkg/%{pkgname}/htm/

%files data
%{_gap_dir}/pkg/%{pkgname}/data/

%files data32
%{_gap_dir}/pkg/%{pkgname}/dat32/

%files doc
%docdir %{_gap_dir}/pkg/%{pkgname}/doc/
%docdir %{_gap_dir}/pkg/%{pkgname}/htm/
%{_gap_dir}/pkg/%{pkgname}/doc/
%{_gap_dir}/pkg/%{pkgname}/htm/

%changelog
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
