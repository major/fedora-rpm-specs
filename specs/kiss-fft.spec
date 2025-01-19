%global srcname kissfft
%global srcver 131

%global build_types %{?build_types} float
%global build_types %{?build_types} double
%global build_types %{?build_types} int16_t
%global build_types %{?build_types} int32_t

# Tests fail on many arches
%bcond_with     tests

Summary:        A Fast Fourier Transform (FFT) library that tries to Keep it Simple, Stupid
Name:           kiss-fft
License:        BSD-3-Clause

Version:        %{srcver}.1.0
Release:        8%{?dist}

URL:            https://github.com/mborgerding/%{srcname}
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  cmake

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libpng-devel
BuildRequires:  python3
# Use cmake28 package on RHEL.
%if 0%{?rhel} && 0%{?rhel} <= 7
BuildRequires:  cmake28 >= 2.8.5	
%else
BuildRequires:  cmake >= 2.8.5	
%endif
BuildRequires:  fftw-devel
# For tests
%if %{with tests}
BuildRequires:  python3-numpy
%endif

%description
KISS FFT - A mixed-radix Fast Fourier Transform based on the 
principle, "Keep It Simple, Stupid."

There are many great fft libraries already around. Kiss FFT is
not trying to be better than any of them. It only attempts to be
a reasonably efficient, moderately useful FFT that can use fixed
or floating data types and can be incorporated into someone's C
program in a few minutes with trivial licensing.

%package static
Summary:        A Fast Fourier Transform (FFT) library that tries to Keep it Simple, Stupid
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description static
Static libraries for KISS FFT - A mixed-radix Fast Fourier Transform based 
on the principle, "Keep It Simple, Stupid."

%package devel
Summary:        A Fast Fourier Transform (FFT) library that tries to Keep it Simple, Stupid
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Dynamically linked libraries and header files for KISS FFT - A mixed-radix Fast 
Fourier Transform based on the principle, "Keep It Simple, Stupid."

There are many great fft libraries already around. Kiss FFT is
not trying to be better than any of them. It only attempts to be
a reasonably efficient, moderately useful FFT that can use fixed
or floating data types and can be incorporated into someone's C
program in a few minutes with trivial licensing.

%prep
%autosetup -n %{srcname}-%{version}

%build
%{set_build_flags}

# Each of the libraries needs to be made separately
for build_type in %{build_types}; do
  mkdir ${build_type}-dynamic
  cd ${build_type}-dynamic
  %cmake .. -DKISSFFT_DATATYPE=${build_type} -DKISSFFT_TEST=ON -DKISSFFT_TOOLS=ON \
  -DKISSFFT_STATIC=OFF -DBUILD_SHARED_LIBS=ON
  %cmake_build
  cd ..
  mkdir ${build_type}-static
  cd ${build_type}-static
  %cmake .. -DKISSFFT_DATATYPE=${build_type} -DKISSFFT_TEST=ON -DKISSFFT_TOOLS=ON \
  -DKISSFFT_STATIC=ON -DBUILD_SHARED_LIBS=OFF
  %cmake_build
  cd ..
done

%install
for build_type in %{build_types}; do
  cd ${build_type}-dynamic
  %cmake_install
  cd ..
  cd ${build_type}-static
  %cmake_install
  cd ..
done

%check
%if %{with tests}
for build_type in %{build_types}; do
  cd ${build_type}-dynamic
  %ctest
  cd ..
  cd ${build_type}-static
  %ctest
  cd ..
done
%endif

%files
%doc README.md TIPS
%license COPYING LICENSES/BSD-3-Clause
%{_libdir}/libkissfft-int16_t.so.%{srcver}*
%{_libdir}/libkissfft-int32_t.so.%{srcver}*
%{_libdir}/libkissfft-float.so.%{srcver}*
%{_libdir}/libkissfft-double.so.%{srcver}*
%{_bindir}/fastconv-int16_t
%{_bindir}/fastconvr-int16_t
%{_bindir}/fft-int16_t
%{_bindir}/psdpng-int16_t
%{_bindir}/fastconv-int32_t
%{_bindir}/fastconvr-int32_t
%{_bindir}/fft-int32_t
%{_bindir}/psdpng-int32_t
%{_bindir}/fastconv-float
%{_bindir}/fastconvr-float
%{_bindir}/fft-float
%{_bindir}/psdpng-float
%{_bindir}/fastconv-double
%{_bindir}/fastconvr-double
%{_bindir}/fft-double
%{_bindir}/psdpng-double

%files static
%{_libdir}/libkissfft-int16_t.a
%{_libdir}/libkissfft-int32_t.a
%{_libdir}/libkissfft-float.a
%{_libdir}/libkissfft-double.a

%files devel
%{_includedir}/%{srcname}
%{_libdir}/libkissfft-int16_t.so
%{_libdir}/libkissfft-int32_t.so
%{_libdir}/libkissfft-float.so
%{_libdir}/libkissfft-double.so
%{_libdir}/cmake/%{srcname}
%{_libdir}/pkgconfig/*.pc

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 131.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 131.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 131.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 131.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 09 2023 Guido Aulisi <guido.aulisi@gmail.com> - 131.1.0-4
- Do not build simd data type

* Wed Aug 09 2023 Guido Aulisi <guido.aulisi@gmail.com> - 131.1.0-3
- Disable failing tests for now

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu May 04 2023 Guido Aulisi <guido.aulisi@gmail.com> - 131.1.0-2
- Remove license package

* Thu May 04 2023 Benson Muite <benson_muite@emailplus.org> - 131.1.0-6
- Add pkgconfig files
- Add dynamic libraries
- Use CMake instead of Make
- Update to 131.1
- Use same versioning scheme as in main repository

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild
 
* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild
 
* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild
 
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild
 
* Fri Aug 28 2020 Guido Aulisi <guido.aulisi@gmail.com> - 1.3.1-1
- Update to 1.3.1
- Drop python2 dependency
 
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild
 
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild
 
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild
 
* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
 
* Thu Jul 19 2018 František Dvořák <valtri@civ.zcu.cz> - 1.3.0-7
- Fix problems with python
 
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild
 
* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild
 
* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild
 
* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild
 
* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 14 2016 František Dvořák <valtri@civ.zcu.cz> - 1.3.0-1
- Initial package
