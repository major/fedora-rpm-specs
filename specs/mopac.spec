%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9
%global blaslib flexiblas
%global cmake_blas_flags -DBLAS_TYPE=FLEXIBLAS -DLAPACK_TYPE=FLEXIBLAS
%else
%global blaslib openblas
%global blasvar o
%global cmake_blas_flags -DBLAS_LIBRARIES=%{_libdir}/lib%{blaslib}%{blasvar}.so -DLAPACK_LIBRARIES=%{_libdir}/lib%{blaslib}%{blasvar}.so
%endif

# EPEL builds need this knob to build out-of-root
%undefine __cmake_in_source_build
%global soversion 2

Name:           mopac
Version:        23.0.1
Release:        2%{?dist}
Summary:        A semiempirical quantum chemistry program
License:        LGPL-3.0-or-later
URL:            http://openmopac.net
Source0:        https://github.com/openmopac/mopac/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  %{blaslib}-devel
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  gcc-gfortran
BuildRequires:  cmake
BuildRequires:  make

# Turn off rpath
Patch1:         mopac-22.0.5-rpath.patch

# For license file
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
The modern open-source version of the Molecular Orbital PACkage
(MOPAC), a semiempirical quantum chemistry program based on Dewar and
Thiel's NDDO approximation.

%package libs
Summary:        MOPAC runtime libraries

%description libs
This package contains MOPAC's runtime libraries.

%package devel
Summary:        MOPAC development library
Requires:       %{name}-libs%{_isa} = %{version}-%{release}

%description devel
This package contains MOPAC's development library.

%prep
%setup -q
%patch -P1 -p1 -b .rpath

%build
%cmake -DENABLE_MKL=OFF -DCMAKE_INSTALL_RPATH_USE_LINK_PATH=OFF \
       %{cmake_blas_flags}

%cmake_build

%install
%cmake_install

%check
# Turn off use of OpenMP parallel BLAS since CTest runs in parallel
export OMP_NUM_THREADS=1
%ctest

%files
%{_bindir}/mopac
%{_bindir}/mopac-makpol
%{_bindir}/mopac-param

%files libs
%license COPYING COPYING.lesser
%doc README.md AUTHORS.rst
%{_libdir}/libmopac.so.%{soversion}*

%files devel
%{_libdir}/libmopac.so
%{_includedir}/mopac.h

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 23.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Nov 16 2024 Susi Lehtola <jussilehtola@fedoraproject.org> - 23.0.1-1
- Update to 23.0.1.

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 22.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 17 2024 Miroslav Suchý <msuchy@redhat.com> - 22.1.1-2
- convert license to SPDX

* Mon Jan 29 2024 Susi Lehtola <jussilehtola@fedoraproject.org> - 22.1.1-1
- Update to 22.1.1.

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 22.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 22.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Sep 28 2023 Susi Lehtola <jussilehtola@fedoraproject.org> - 22.1.0-1
- Update to 22.1.0.

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 19 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 22.0.6-1
- Update to 22.0.6.

* Wed Nov 09 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 22.0.5-1
- Update to 22.0.5.

* Thu Jul 28 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 22.0.4-1
- Update to 22.0.4.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jun 25 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 22.0.3-1
- Update to 22.0.3.

* Tue Jun 21 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 22.0.2-1
- Update to 22.0.2.

* Thu Jun 09 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 22.0.1-2
- Fix build in mock.

* Tue May 17 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 22.0.1-1
- Update to 22.0.1.

* Mon May 02 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 22.0.0-1
- First release.

