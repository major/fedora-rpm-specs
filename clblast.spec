# TESTING NOTE: An OpenCL device is needed to run the tests.  Since the koji
# builders may or may not have a GPU, we use the CPU-only POCL implementation.

Name:           clblast
Version:        1.5.3
Release:        3%{?dist}
Summary:        Tuned OpenCL BLAS routines

License:        Apache-2.0
URL:            https://cnugteren.github.io/clblast/clblast.html
Source0:        https://github.com/CNugteren/CLBlast/archive/%{version}/%{name}-%{version}.tar.gz
# Fix name clashes between macros in altivec.h and standard types on ppc64le
Patch0:         %{name}-altivec.patch

%if 0%{?fedora}
%bcond_without check
%bcond_without pocl
%else
%bcond_with check
%bcond_with pocl
%endif

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  ocl-icd-devel
BuildRequires:  pkgconfig(flexiblas)
%if %{with pocl}
BuildRequires:  pocl-devel
%endif

%description
CLBlast is a modern, lightweight, performant and tunable OpenCL BLAS
library written in C++11.  It is designed to leverage the full
performance potential of a wide variety of OpenCL devices from different
vendors, including desktop and laptop GPUs, embedded GPUs, and other
accelerators.  CLBlast implements BLAS routines: basic linear algebra
subprograms operating on vectors and matrices.  See the CLBlast website
for performance reports on various devices as well as the latest CLBlast
news.

The library is not tuned for all possible OpenCL devices: if
out-of-the-box performance is poor, please run the tuners first.

%package devel
Summary:        Headers and libraries for CLBlast
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocl-icd-devel%{?_isa}

%description devel
Headers and libraries for developing applications that use CLBlast.

%package tuners
Summary:        Tuners for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description tuners
Programs to tune %{name} for your OpenCL device.

%prep
%autosetup -p0 -n CLBlast-%{version}

# Fix the path to the openblas headers
sed -i 's,openblas/include,include/openblas,' cmake/Modules/FindCBLAS.cmake
# Add paths for FlexiBLAS
sed -i 's,include/openblas,include/openblas include/flexiblas,' cmake/Modules/FindCBLAS.cmake
sed -i 's,NAMES cblas blas,NAMES cblas blas flexiblas,' cmake/Modules/FindCBLAS.cmake

%build
%cmake -DTESTS:BOOL=ON
%cmake_build

%install
%cmake_install

%if %{with check}
%ifarch x86_64
%check
%ctest
%endif
%endif

%files
%license LICENSE
%doc CHANGELOG README.md ROADMAP.md
%{_libdir}/lib{%name}.so.1
%{_libdir}/lib{%name}.so.%{version}

%files devel
%doc doc
%{_includedir}/%{name}*.h
%{_libdir}/lib{%name}.so
%{_libdir}/cmake/CLBlast/
%{_libdir}/pkgconfig/%{name}.pc

%files tuners
%{_bindir}/clblast*

%changelog
* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 21 2022 Tom Rix <trix@redhat.com> - 1.5.3-2
- Prepare for building on epel

* Thu Sep 29 2022 Jerry James <loganjerry@gmail.com> - 1.5.3-1
- Version 1.5.3
- Drop upstreamed -reference patch
- Run tests on all arches

* Mon Aug 15 2022 Jerry James <loganjerry@gmail.com> - 1.5.2-5
- Convert License field to SPDX

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 20 2021 Jerry James <loganjerry@gmail.com> - 1.5.2-1
- Version 1.5.2
- Add -reference patch to reduce copying

* Fri Aug 07 2020 Iñaki Úcar <iucar@fedoraproject.org> - 1.5.1-4
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 18 2020 Jerry James <loganjerry@gmail.com> - 1.5.1-1
- Version 1.5.1

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 15 2018 Jerry James <loganjerry@gmail.com> - 1.5.0-1
- New upstream version

* Sat Sep  1 2018 Jerry James <loganjerry@gmail.com> - 1.4.1-1
- Initial RPM
