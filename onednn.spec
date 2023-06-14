Name:           onednn
Version:        3.1.1
Release:        1%{?dist}
Summary:        oneAPI Deep Neural Network Library

License:        Apache-2.0 and BSD-2-Clause and BSD-3-Clause and BSL-1.0 and MIT
URL:            https://github.com/oneapi-src/oneDNN/
Source0:        %{url}/archive/v%{version}/onednn-%{version}.tar.gz

# https://github.com/oneapi-src/oneDNN/pull/1554
# https://github.com/fujitsu/xbyak_aarch64/pull/81
Patch0:			aarch64-gcc13.patch

# This package only work in 64bit arches for now
ExclusiveArch:  x86_64 aarch64 ppc64le s390x

BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++

# Optionals not yet enabled
BuildRequires:  pkgconfig(OpenCL)
#BuildRequires:  pkgconfig(tbb)

# Virtual provides mkldnn
Provides: mkldnn = %{version}-%{release}
Provides: mkl-dnn = %{version}-%{release}
Obsoletes: mkl-dnn < 1.3
# Provides oneDNN
Provides: oneDNN = %{version}-%{release}


%description
oneAPI Deep Neural Network Library (oneDNN) is an open-source cross-platform
performance library of basic building blocks for deep learning applications.
oneDNN is part of oneAPI. The library is optimized for Intel(R) Architecture
Processors, Intel Graphics, and Arm* 64-bit Architecture (AArch64)-based
processors. oneDNN has experimental support for the following architectures:
NVIDIA* GPU, OpenPOWER* Power ISA (PPC64), IBMz* (s390x), and RISC-V.

oneDNN is intended for deep learning applications and framework developers
interested in improving application performance on Intel CPUs and GPUs.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n oneDNN-%{version}


%build
%cmake
%cmake_build


%install
%cmake_install

# Remove docs
rm -rf %{buildroot}%{_docdir}/dnnl

%ldconfig_scriptlets


# Some ocl/gpu tests will fails if lacking an appropriate implementation
%{?_with_tests:
%check
%ctest
}


%files
%license LICENSE THIRD-PARTY-PROGRAMS
%doc README.md CONTRIBUTING.md CODE_OF_CONDUCT.md
%{_libdir}/libdnnl.so.3
%{_libdir}/libdnnl.so.3.*


%files devel
%dir %{_includedir}/oneapi
%{_includedir}/oneapi/dnnl
%{_includedir}/dnnl*.h*
%{_libdir}/libdnnl.so
%dir %{_libdir}/cmake/dnnl
%{_libdir}/cmake/dnnl/*.cmake


%changelog
* Mon Jun 12 2023 Nicolas Chauvet <kwizart@gmail.com> - 3.1.1-1
- Update to 3.1.1

* Thu May 04 2023 Nicolas Chauvet <kwizart@gmail.com> - 3.1-1
- Update to 3.1

* Mon Mar 06 2023 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 3.0.1-2
- oneDNN did not migrate the latest fujitsu/xbyak_aarch64 yet

* Mon Mar 06 2023 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 3.0.1-1
- Update to 3.0.1

* Sat Feb 11 2023 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 3.0-1
- Update to 3.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Sep 28 2022 Nicolas Chauvet <kwizart@gmail.com> - 2.7-1
- Update to 2.7

* Wed Aug 10 2022 Nicolas Chauvet <kwizart@gmail.com> - 2.6.1-1
- Update to 2.6.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Nicolas Chauvet <kwizart@gmail.com> - 2.6-1
- Update to 2.6
- Drop previous compat libraries

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 06 2021 Nicolas Chauvet <kwizart@gmail.com> - 2.4.4-1
- Update to 2.4.4

* Fri Oct 08 2021 Nicolas Chauvet <kwizart@gmail.com> - 2.4-1
- Update to 2.4

* Mon Aug 16 2021 Nicolas Chauvet <kwizart@gmail.com> - 2.3.2-2
- Enable s390x
- Enable ctest
- Fix compilation issue on non-x86 arches

* Mon Aug 16 2021 Nicolas Chauvet <kwizart@gmail.com> - 2.3.2-1
- Update to 2.3.2

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed May 26 2021 Nicolas Chauvet <kwizart@gmail.com> - 2.2.2-1
- Update to 2.2.2

* Sat Apr 03 2021 Nicolas Chauvet <kwizart@gmail.com> - 2.2-1
- Update to 2.2

* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 2.1-2
- Rebuilt for removed libstdc++ symbol (#1937698)

* Wed Feb 17 2021 Nicolas Chauvet <kwizart@gmail.com> - 2.1-1
- Update to 2.1

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 03 2020 Nicolas Chauvet <kwizart@gmail.com> - 1.6-1
- Update to 1.6

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Nicolas Chauvet <kwizart@gmail.com> - 1.5-1
- Update to 1.5
- Enable aarch64

* Mon Apr 20 2020 Nicolas Chauvet <kwizart@gmail.com> - 1.4-1
- Update to 1.4

* Sat Apr 04 2020 Nicolas Chauvet <kwizart@gmail.com> - 1.3-1
- Update to 1.3
- Switch to onednn

* Sat Apr  6 2019 Nicolas Chauvet <kwizart@gmail.com> - 0.18.1-1
- Initial spec file.
