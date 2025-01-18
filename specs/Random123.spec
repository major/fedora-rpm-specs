%global debug_package %{nil}

Name:       Random123
Version:    1.14.0
Release:    11%{?dist}
Summary:    Library of random number generators

# Automatically converted from old format: BSD - review is highly recommended.
License:    LicenseRef-Callaway-BSD
URL:        https://github.com/DEShawResearch/random123/
Source0:    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:      0001-add-missing-headers.patch
# https://github.com/DEShawResearch/random123/pull/12
Patch:      enable-riscv.patch

# gccfeatures.h mentions what arches are supported
# these aren't on the list
ExcludeArch:    mips64r2 mips32r2 s390

BuildRequires:  make
BuildRequires:  doxygen
# For tests
BuildRequires:  gcc gcc-c++
BuildRequires:  patch

%description
Random123 is a library of "counter-based" random number generators (CBRNGs), in
which the Nth random number can be obtained by applying a stateless mixing
function to N instead of the conventional approach of using N iterations of a
stateful transformation. CBRNGs were originally developed for use in MD
applications on Anton, but they are ideal for a wide range of applications on
modern multi-core CPUs, GPUs, clusters, and special-purpose hardware. Three
families of non-cryptographic CBRNGs are described in a paper presented at the
SC11 conference: ARS (based on the Advanced Encryption System (AES)), Threefry
(based on the Threefish encryption function), and Philox (based on integer
multiplication). They all satisfy rigorous statistical testing (passing
BigCrush in TestU01), vectorize and parallelize well (each generator can
produce at least 264 independent streams), have long periods (the period of
each stream is at least 2128), require little or no memory or state, and have
excellent performance (a few clock cycles per byte of random output). The
Random123 library can be used with CPU (C and C++) and GPU (CUDA and OpenCL)
applications.

%package devel
Summary:   Development files for %{name}
Provides:  %{name} = %{version}-%{release}

%description devel
Development files for %{name}.

%package doc
Summary:    Documentation for %{name}

%description doc
Documentation for %{name}.

%prep
%autosetup -n random123-%{version} -S patch -p1


%build
# Header only library
pushd docs
    doxygen Doxyfile
popd

%install
mkdir -p -m 0755 $RPM_BUILD_ROOT/%{_includedir}/%{name}/
cp -a include/Random123/*  $RPM_BUILD_ROOT/%{_includedir}/%{name}/

%check
pushd tests
    cp GNUmakefile Makefile
    %set_build_flags
    make
popd

%files devel
%license LICENSE
%{_includedir}/%{name}/

%files doc
%doc examples

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.14.0-10
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jul 04 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.14.0-1
- Update to latest release
- Drop no longer needed s390x patch (merged upstream)

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.2-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Mar 08 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.13.2-2
- Include patch to support s390x (sent and accepted upstream)
- Enable s390x build

* Sun Feb 23 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.13.2-1
- Update to latest release
- Run new tests
- Update arches supported
- Drop unneeded patch

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 28 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.09-7
- Add aarch64 patch

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Apr 06 2016 Ankur Sinha <ankursinha AT fedoraproject DOT org> 1.09-1
- Update to new release
- Remove noarch

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Aug 04 2015 Ankur Sinha <ankursinha AT fedoraproject DOT org> 1.08-3
- Update as per reviewer comments in rhbz 1150445

* Fri Jul 31 2015 Ankur Sinha <ankursinha AT fedoraproject DOT org> 1.08-2
- Fix doc build errors.

* Wed Jan 08 2014 Ankur Sinha <ankursinha AT fedoraproject DOT org> 1.08-1
- Initial rpm build


