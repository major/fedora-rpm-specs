%global soname 1

Name:           mrcpp
Version:        1.5.0
Release:        7%{?dist}
Summary:        A numerical mathematics library based on multiresolution analysis
License:        LGPL-3.0-or-later
URL:            https://github.com/MRChemSoft/mrcpp/
Source0:        https://github.com/MRChemSoft/mrcpp/archive/v%{version}/%{name}-%{version}.tar.gz

# Relax Eigen3 version check, https://github.com/MRChemSoft/mrcpp/issues/186
Patch0:         mrcpp-1.4.0-eigen3.patch
# Disable rpath
Patch1:         mrcpp-1.4.0-rpath.patch
# Patch in catchv3 support, see https://github.com/MRChemSoft/mrcpp/pull/213
Patch2:         mrcpp-1.5.0-catchv3.patch

%if 0%{?rhel} == 9
# Compile fails on ppc64le with the error /usr/include/eigen3/Eigen/src/Core/arch/AltiVec/MatrixProduct.h:1199:26: error: inlining failed in call to 'always_inline' 'Eigen::internal::bload<Eigen::internal::blas_data_mapper<double, long, 0, 0, 1>, double __vector(2), long, 2l, 0, 0>(Eigen::internal::PacketBlock<double __vector(2), 4>&, Eigen::internal::blas_data_mapper<double, long, 0, 0, 1> const&, long, long)void': target specific option mismatch
ExcludeArch:    ppc64le
%endif

# We need the data
Requires:       %{name}-data = %{version}-%{release}

BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  json-devel
BuildRequires:  eigen3-devel
BuildRequires:  xcfun-devel
BuildRequires:  catch-devel

# Eigen3 is a header-only library; this is for dependency tracking
BuildRequires:  eigen3-static

# The tests fail on s390x and upstream doesn't support it
ExcludeArch:    s390x

%description
The MultiResolution Computation Program Package (MRCPP) is a general
purpose numerical mathematics library based on multiresolution
analysis and the multiwavelet basis which provide low-scaling
algorithms as well as rigorous error control in numerical
computations.

%package devel
Summary:        Development headers and libraries for mrcpp
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The MultiResolution Computation Program Package (MRCPP) is a general
purpose numerical mathematics library based on multiresolution
analysis and the multiwavelet basis which provide low-scaling
algorithms as well as rigorous error control in numerical
computations.

This package contains the development headers and libraries.

%package data
Summary:        Runtime data for mrcpp
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description data
The MultiResolution Computation Program Package (MRCPP) is a general
purpose numerical mathematics library based on multiresolution
analysis and the multiwavelet basis which provide low-scaling
algorithms as well as rigorous error control in numerical
computations.

This package contains the runtime data.

%prep
%setup -q
# EPEL still can't handle the new patch style
%patch -P0 -p1 -b .eigen3
%patch -P1 -p1 -b .rpath
%patch -P2 -p1 -b .catchv3
# Remove bundled catch
rm -rf external/catch/

%build
export CXXFLAGS="%{optflags} -I%{_includedir}/catch2"
%cmake -DENABLE_ARCH_FLAGS=OFF -DENABLE_OPENMP=ON -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install
# Remove the tests, we don't want to ship them
rm %{buildroot}%{_bindir}/mrcpp-tests

%check
%ctest

%files
%license LICENSE
%doc CHANGELOG.md CONTRIBUTING.md README.md VERSION
%{_libdir}/libmrcpp.so.%{soname}*

%files data
%{_datadir}/MRCPP/

%files devel
%{_datadir}/cmake/MRCPP/
%{_libdir}/libmrcpp.so
%{_includedir}/MRCPP/

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 17 2024 Miroslav Suchý <msuchy@redhat.com> - 1.5.0-5
- convert license to SPDX

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 14 2023 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.5.0-1
- Update to 1.5.0.

* Fri Jan 20 2023 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.4.2-1
- Update to 1.4.2.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 14 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.4.1-3
- FTBSFS; ExcludeArch s390x since the tests fail on that architecture.

* Fri Jan 14 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.4.1-2
- Add BR: eigen3-static for dependency tracking.

* Thu Jan 13 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.4.1-1
- Update to 1.4.1, fixing overflow.
- More review fixes.

* Mon Dec 27 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.4.0-2
- Review fixes

* Sat Dec 25 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.4.0-1
- First release
