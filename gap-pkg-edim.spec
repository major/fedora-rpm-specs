%global pkgname edim
%global upname EDIM

Name:           gap-pkg-%{pkgname}
Version:        1.3.5
Release:        10%{?dist}
Summary:        Elementary divisors of integer matrices

License:        GPL-2.0-or-later
URL:            https://www.math.rwth-aachen.de/~Frank.Luebeck/%{upname}/
Source0:        https://www.math.rwth-aachen.de/~Frank.Luebeck/%{upname}/%{upname}-%{version}.tar.bz2

BuildRequires:  gap-devel
BuildRequires:  GAPDoc-latex
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make

Requires:       gap-core%{?_isa}

%description
The main purpose of the EDIM package is to publish an implementation of
an algorithm (found by the package author) for computing prime parts of
the elementary divisors of integer matrices (i.e., the diagonal entries
of the Smith normal form).

The programs are developed and already successfully used for large
matrices (up to rank >12000) with moderate entries and many non-trivial
elementary divisors which are products of some small primes. But they
should be useful for other types of matrices as well.

Among the other functions of the package are:
- an inversion algorithm for large rational matrices (using a p-adic
  method)
- a program for finding the largest elementary divisor of an integral
  matrix (particularly interesting when this is much smaller than the
  determinant) and
- implementations of some normal form algorithms described by Havas,
  Majewski, Matthews, Sterling (using LLL- or modular techniques).

%package doc
Summary:        EDIM documentation
# doc/mathml.css is MPLv1.1; all other files are GPLv2+
License:        GPLv2+ and MPLv1.1
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
BuildArch:      noarch

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{upname}-%{version}

# Fix encodings
for fil in doc/edim.bib doc/edim.bbl; do
  iconv -f iso8859-1 -t utf-8 $fil > $fil.utf8
  touch -r $fil $fil.utf8
  mv -f $fil.utf8 $fil
done

%build
export LC_ALL=C.UTF-8

# This is NOT an autoconf-generated script.  Do not use %%configure.
./configure %{_gap_dir}
%make_build

# Link to main GAP documentation
ln -s %{_gap_dir}/doc ../../doc
mkdir ../pkg
ln -s ../%{upname}-%{version} ../pkg
gap -l "$PWD/..;%{_gap_dir}" < makedocrel.g
rm -fr ../../doc ../pkg

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg/%{upname}-%{version}/bin/%{_gap_arch}
cp -p bin/%{_gap_arch}/.libs/ediv.so \
   %{buildroot}%{_gap_dir}/pkg/%{upname}-%{version}/bin/%{_gap_arch}
cp -a doc lib tst VERSION *.g %{buildroot}%{_gap_dir}/pkg/%{upname}-%{version}
rm -f %{buildroot}%{_gap_dir}/pkg/%{upname}-%{version}/doc/clean
rm -f %{buildroot}%{_gap_dir}/pkg/%{upname}-%{version}/doc/*.{aux,bbl,blg,brf,idx,ilg,ind,log,out,pnr}

%check
export LC_ALL=C.UTF-8
gap -q -l "%{buildroot}%{_gap_dir};%{_gap_dir}" < tst/test.g 2>&1 | tee log
! grep -Fq 'false' log
rm -f log

%files
%doc CHANGES README TODO
%license GPL
%{_gap_dir}/pkg/%{upname}-%{version}/
%exclude %{_gap_dir}/pkg/%{upname}-%{version}/doc/

%files doc
%docdir %{_gap_dir}/pkg/%{upname}-%{version}/doc/
%{_gap_dir}/pkg/%{upname}-%{version}/doc/

%changelog
* Tue Aug 16 2022 Jerry James <loganjerry@gmail.com> - 1.3.5-10
- Convert License tag to SPDX

* Sun Jul 24 2022 Jerry James <loganjerry@gmail.com> - 1.3.5-10
- Rebuild due to changed binary dir name on s390x

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar 11 2020 Jerry James <loganjerry@gmail.com> - 1.3.5-4
- Rebuild for gap 4.11.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov  5 2019 Jerry James <loganjerry@gmail.com> - 1.3.5-2
- Bump and rebuild due to update snafu

* Tue Aug 13 2019 Jerry James <loganjerry@gmail.com> - 1.3.5-1
- New upstream version

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Jerry James <loganjerry@gmail.com> - 1.3.3-5
- Rebuild for changed bin dir name in gap 4.10.1

* Fri Feb  1 2019 Jerry James <loganjerry@gmail.com> - 1.3.3-4
- Rebuild for gap 4.10.0
- Add -doc subpackage

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 17 2018 Jerry James <loganjerry@gmail.com> - 1.3.3-1
- New upstream version

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Apr  7 2016 Jerry James <loganjerry@gmail.com> - 1.3.2-5
- Rebuild for gap 4.8.3

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 11 2015 Jerry James <loganjerry@gmail.com> - 1.3.2-3
- Drop scriptlets; gap-core now uses rpm file triggers
- Rebuild documentation from source
- Turn test failures into build failures

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 20 2015 Jerry James <loganjerry@gmail.com> - 1.3.2-1
- Initial RPM (bz 1223627)
