%global pkgname irredsol

Name:           gap-pkg-%{pkgname}
Version:        1.4.3
Release:        4%{?dist}
Summary:        Irreducible soluble linear groups over finite fields

License:        BSD-2-Clause
URL:            http://www.icm.tu-bs.de/~bhoeflin/%{pkgname}/
Source0:        https://github.com/bh11/%{pkgname}/releases/download/IRREDSOL-%{version}/%{pkgname}-%{version}.tar.bz2
# Fix references to the primgrp manual
Patch0:         %{name}-ref.patch
BuildArch:      noarch

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-crisp-doc
BuildRequires:  gap-pkg-primgrp-doc
BuildRequires:  parallel
BuildRequires:  perl-interpreter
BuildRequires:  tth

Requires:       gap-core

Recommends:     gap-pkg-crisp

%description
IRREDSOL is a GAP package which provides a library of all irreducible
soluble subgroups of GL(n, q), up to conjugacy, where n is a positive
integer and q a prime power satisfying q^n <= 2000000, and a library
of all primitive soluble groups of degree at most 2000000.

%package doc
Summary:        IRREDSOL documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-pkg-crisp-doc
Requires:       gap-pkg-primgrp-doc

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -p0 -n %{pkgname}-%{version}

%build
# Link to main GAP documentation and CRISP documentation
crispdir=$(basename $(ls -1d %{_gap_dir}/pkg/crisp*))
primgrpdir=$(basename $(ls -1d %{_gap_dir}/pkg/primgrp*))
ln -s %{_gap_dir}/etc ../../etc
ln -s %{_gap_dir}/doc ../../doc
ln -s %{_gap_dir}/pkg ../../pkg
ln -s %{_gap_dir}/pkg/$crispdir ..
ln -s %{_gap_dir}/pkg/$crispdir ../crisp
ln -s %{_gap_dir}/pkg/$primgrpdir ..
pushd doc
sed -e "/UseReferences/s/crisp/$crispdir/" \
    -e "/UseReferences/s/primgrp/$primgrpdir/" \
    -i manual.tex
pdftex manual
makeindex manual
pdftex manual
pdftex manual
rm -f ../htm/*
perl %{_gap_dir}/etc/convert.pl -t -c -n IRREDSOL . ../htm
popd
rm -f ../../{doc,etc,pkg} ../crisp

# Fixup links
sed -e "s,../crisp/,../$crispdir/," \
    -e "s,../primgrp/,../$primgrpdir/," \
    -i htm/CHAP*.htm

# Compress large data files
parallel %{?_smp_mflags} --no-notice gzip --best ::: data/*.grp fp/*.fp

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg
cp -a ../%{pkgname}-%{version} %{buildroot}%{_gap_dir}/pkg
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/{LICENSE,README}.txt
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/*.{aux,bbl,blg,brf,idx,ilg,in,ind,log,new,out,pnr}

%check
gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" < tst/testall.g

%files
%doc README.txt
%license LICENSE.txt
%{_gap_dir}/pkg/%{pkgname}-%{version}/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/htm/

%files doc
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/htm/
%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%{_gap_dir}/pkg/%{pkgname}-%{version}/htm/

%changelog
* Tue Aug 16 2022 Jerry James <loganjerry@gmail.com> - 1.4.3-4
- Convert License tag to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul  1 2021 Jerry James <loganjerry@gmail.com> - 1.4.3-1
- Version 1.4.3

* Sat Apr 24 2021 Jerry James <loganjerry@gmail.com> - 1.4.2-1
- Version 1.4.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Mar  8 2020 Jerry James <loganjerry@gmail.com> - 1.4.1-1
- Version 1.4.1

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb  2 2019 Jerry James <loganjerry@gmail.com> - 1.4-5
- Rebuild for gap 4.10.0
- Add -ref patch
- Add -doc subpackage

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug  5 2017 Jerry James <loganjerry@gmail.com> - 1.4-1
- New upstream version

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri May 27 2016 Jerry James <loganjerry@gmail.com> - 1.3.1-1
- Initial RPM
