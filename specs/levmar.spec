# SOlib major and minor version
%global major 2
%global minor 6

%if 0%{?fedora} >= 33
%bcond_without flexiblas
%endif

Name:		levmar
Version:	2.6
Release:	18%{?dist}
Summary:	Levenberg-Marquardt nonlinear least squares algorithm
URL:		http://www.ics.forth.gr/~lourakis/levmar/

Source0:	http://www.ics.forth.gr/~lourakis/levmar/levmar-%{version}.tgz

# Patch to fix compilation of the shared library and compile the demo program
Patch0:		levmar-cmake-shared.patch

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
BuildRequires:	gcc
BuildRequires:	cmake
BuildRequires:	dos2unix
BuildRequires:  chrpath
%if %{with flexiblas}
BuildRequires:	flexiblas-devel
%else
BuildRequires:	blas-devel, lapack-devel
%endif

%description
levmar is a native ANSI C implementation of the Levenberg-Marquardt
optimization algorithm.  Both unconstrained and constrained (under linear
equations, inequality and box constraints) Levenberg-Marquardt variants are
included.  The LM algorithm is an iterative technique that finds a local
minimum of a function that is expressed as the sum of squares of nonlinear
functions.  It has become a standard technique for nonlinear least-squares
problems and can be thought of as a combination of steepest descent and the
Gauss-Newton method.  When the current solution is far from the correct on,
the algorithm behaves like a steepest descent method: slow, but guaranteed
to converge.  When the current solution is close to the correct solution, it
becomes a Gauss-Newton method.

%package devel
Summary:	Development files for levmar library, and demo program
Requires:	levmar = %{version}-%{release}

%description devel
Development files for the levmar library, and demo program.

%prep
%autosetup -p1
dos2unix -k README.txt

%if %{with flexiblas}
sed -i 's/lapack;blas/flexiblas;flexiblas/g' CMakeLists.txt
%endif

%build
%cmake -DLINSOLVERS_RETAIN_MEMORY:BOOL=OFF -DNEED_F2C:BOOL=OFF
%cmake_build

%install
install -D -p -m 755 "%{_vpath_builddir}/liblevmar.so.%{major}.%{minor}" "%{buildroot}%{_libdir}/liblevmar.so.%{major}.%{minor}"
install -D -p -m 644 levmar.h "%{buildroot}%{_includedir}/levmar.h"
install -D -p -m 755 "%{_vpath_builddir}/lmdemo" "%{buildroot}%{_bindir}/lmdemo"
ln -s "liblevmar.so.%{major}.%{minor}" "%{buildroot}%{_libdir}/liblevmar.so.%{major}"
ln -s "liblevmar.so.%{major}.%{minor}" "%{buildroot}%{_libdir}/liblevmar.so"
chrpath --delete "%{buildroot}%{_bindir}/lmdemo"

%ldconfig_scriptlets

%check
"%{_vpath_builddir}/lmdemo"

%files
%doc README.txt LICENSE
%{_libdir}/liblevmar.so.%{major}.%{minor}
%{_libdir}/liblevmar.so.%{major}

%files devel
%{_includedir}/levmar.h
%{_libdir}/liblevmar.so
%{_bindir}/lmdemo

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.6-17
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 09 2021 Alejandro Alvarez Ayllon <aalvarez@fedoraproject.org> - 2.6-9
- Clear RPATH from lmdemo

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 27 2020 Iñaki Úcar <iucar@fedoraproject.org> - 2.6-6
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Mon Aug 17 2020 Alejandro Alvarez Ayllon <a.alvarezayllon@gmail.com> - 2.6-5
- Use new cmake macros

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Alejandro Alvarez Ayllon <a.alvarezayllon@gmail.com> - 2.6-1
- levmar 2.6

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 28 2010 Eric Smith <eric@brouhaha.com> - 2.5-4
- preserve timestamp of README in prep

* Sun Jan 24 2010 Eric Smith <eric@brouhaha.com> - 2.5-3
- don't need f2c
- spec cleanup based on review comments from Jussi Lehtola

* Sat Jan 23 2010 Eric Smith <eric@brouhaha.com> - 2.5-2
- spec cleanup based on review comments from Jussi Lehtola

* Fri Jan 22 2010 Eric Smith <eric@brouhaha.com> - 2.5-1
- initial version
