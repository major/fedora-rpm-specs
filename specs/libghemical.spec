Name:           libghemical
Summary:        Libraries for the Ghemical chemistry package
Version:        3.0.0
Release:        26%{?dist}

# SPDX confirmed
License:        GPL-2.0-or-later
URL:            http://www.bioinformatics.org/ghemical/ghemical/index.html
Source0:        http://www.bioinformatics.org/ghemical/download/current/%{name}-%{version}.tar.gz

BuildRequires:  flexiblas-devel
BuildRequires:  flex
BuildRequires:  glib2-devel
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  make
BuildRequires:  libtool
BuildRequires:  intltool
BuildRequires:  libint-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  mpqc-devel
BuildRequires:  mopac7-devel

# Libint releases can have API breakages, leading to segfaults.
Requires:       libint(api)%{?_isa} = %{_libint_apiversion}

%description
Data files and dynamic libraries for the Ghemical chemistry package.
These libraries implement the quantum-mechanics and molecular
mechanics models used to compute molecular properties.

%package devel
Summary:    Header files and static libraries from %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   pkgconfig

%description devel
Libraries and header include files for developing programs based on %{name}.

%prep
%autosetup

%build
sed -i 's/blas/flexiblas/g' configure.ac
sed -i 's/lapack/flexiblas/g' configure.ac
autoreconf -ivf

%configure --enable-mopac7 --enable-mpqc --disable-static --disable-sctest
%make_build

sed -ir -e 's/^Libs:.*/Libs: -L${libdir} -lghemical/g' libghemical.pc

%install
%make_install

find %{buildroot}%{_libdir} -name *.la -exec rm -rf {} \;

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog TODO
%license COPYING
%{_datadir}/%{name}/
%{_libdir}/libghemical.so.5.0.1
%{_libdir}/libghemical.so.5

%files devel
%{_includedir}/ghemical/
%{_libdir}/libghemical.so
%{_libdir}/pkgconfig/libghemical.pc


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Dec 15 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.0-22
- SPDX migration

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Nov 06 2021 Antonio Trande <sagitter@fedoraproject.org> - 3.0.0-17
- SPEC file revisited

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 27 2020 Iñaki Úcar <iucar@fedoraproject.org> - 3.0.0-14
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0
.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.0-7
- F-28: rebuild for gfortran 8

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-6.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 29 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.0-2.1
- F-26: rebuild against gfortran 7

* Fri May  6 2016 Mamoru TASAKA <mtasaka@fedoraproject.org>
- Rebuild

* Fri May  6 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.0-1
- 3.0.0

* Fri May  6 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.99.1-32
- Rebuild with fixed mpqc (sc-config)
- Kill libghemical-use-atlas.patch, fixed in mpqc side

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.99.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.99.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.99.1-29
- Rebuilt for GCC 5 C++11 ABI change

* Tue Nov 18 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.99.1-28
- Once revert to the version which is currently buildroot
- Add needed BRs
- Fix Requires for libint api

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.99.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Dec 23 2013 Susi Lehtola <jussilehtola@fedoraproject.org> 2.99.1-26
- Rebuild for new libint.

* Sun Sep 22 2013 Carl Byington <carl@five-ten-sg.com> 2.99.1-25
- rebuild for new atlas and blas libraries

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.99.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 29 2013 Carl Byington <carl@five-ten-sg.com> 2.99.1-23
- add autoreconf for aarch64

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.99.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 25 2012 Jussi Lehtola <jussilehtola@fedoraproject.org> - 2.99.1-21
- Rebuild due to changed libint.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.99.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.99.1-19
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.99.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 08 2010 Carl Byington <carl@five-ten-sg.com> 2.99.1-17
- rebuild for libint changes

* Sun Jun 20 2010 Carl Byington <carl@five-ten-sg.com> 2.99.1-16
- new tag need for make build

* Tue Apr 20 2010 Carl Byington <carl@five-ten-sg.com> 2.99.1-15
- patch libghemical.pc to avoid unnecessary parts

* Thu Apr 08 2010 Carl Byington <carl@five-ten-sg.com> 2.99.1-14
- patch configure.ac to pull in the required sc_ libs

* Mon Apr 05 2010 Carl Byington <carl@five-ten-sg.com> 2.99.1-13
- improved package description
- link against mopac7 since we need that
- remove unnecessary build-requires

* Sat Apr 03 2010 Carl Byington <carl@five-ten-sg.com> 2.99.1-12
- merge -data and -libs packages into main package

* Sat Jan 09 2010 Carl Byington <carl@five-ten-sg.com> 2.99.1-11
- add COPYING license file to doc

* Mon Jan 04 2010 Carl Byington <carl@five-ten-sg.com> 2.99.1-10
- use blas and lapack from atlas.

* Wed Dec 23 2009 Carl Byington <carl@five-ten-sg.com> 2.99.1-9
- devel requires pkgconfig for EPEL

* Wed Dec 23 2009 Carl Byington <carl@five-ten-sg.com> 2.99.1-8
- install -p to preserve timestamps
- trim changelog
- explicit includedir name
- add pkgconfig for EPEL

* Sun Dec 20 2009 Carl Byington <carl@five-ten-sg.com> 2.99.1-7
- explicit names in %%files section rather than wildcards

* Sat Dec 05 2009 Carl Byington <carl@five-ten-sg.com> 2.99.1-6
- remove unnecessary f2c requirement

* Wed Dec 02 2009 Carl Byington <carl@five-ten-sg.com> 2.99.1-5
- convert to fedora compatible spec file
- remove static libraries

* Fri Oct 16 2009 Guillaume Bedot <littletux@mandriva.org> 2.99.1-4mdv2010.0
- Revision: 457836
- rebuild

