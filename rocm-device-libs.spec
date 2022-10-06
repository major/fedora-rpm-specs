# bitcode has no debuginfo
%global debug_package %{nil}

%global llvm_maj_ver 15
%global upstreamname ROCm-Device-Libs

Name:           rocm-device-libs
Version:        5.3.0
Release:        1%{?dist}
Summary:        AMD ROCm LLVM bit code libraries

Url:            https://github.com/RadeonOpenCompute/ROCm-Device-Libs
License:        NCSA
Source0:        https://github.com/RadeonOpenCompute/%{upstreamname}/archive/refs/tags/rocm-%{version}.tar.gz#/%{upstreamname}-%{version}.tar.gz
# Upstream is working on a solution, patch is adapted from debian:
#https://salsa.debian.org/rocm-team/rocm-device-libs/-/blob/master/debian/patches/cmake-amdgcn-bitcode.patch
Patch0:         0001-Use-FHS-compliant-install.patch

BuildRequires:  cmake
BuildRequires:  clang-devel
BuildRequires:  clang(major) = %{llvm_maj_ver}
BuildRequires:  llvm-devel(major) = %{llvm_maj_ver}
BuildRequires:  zlib-devel
Requires:       clang(major) = %{llvm_maj_ver}

#Only the following architectures are useful for ROCm packages:
ExclusiveArch:  x86_64 aarch64 ppc64le

%description
This package contains a set of AMD specific device-side language runtime
libraries in the form of bit code. Specifically:
 - Open Compute library controls
 - Open Compute Math library
 - Open Compute Kernel library
 - OpenCL built-in library
 - HIP built-in library
 - Heterogeneous Compute built-in library

%prep
%autosetup -p1 -n %{upstreamname}-rocm-%{version}

%build
%cmake -DCMAKE_BUILD_TYPE="RELEASE"
%cmake_build

%install
%cmake_install

%files
%license LICENSE.TXT
%doc README.md doc/*.md
# No need to install this twice:
%exclude %{_docdir}/ROCm-Device-Libs/LICENSE.TXT
%{_libdir}/cmake/AMDDeviceLibs
%{_libdir}/amdgcn

%changelog
* Mon Oct 03 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 5.3.0-1
- Update to 5.3.0

* Tue Sep 13 2022 Nikita Popov <npopov@redhat.com> - 5.2.0-3
- Rebuild against LLVM 15

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 03 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 5.2.0-1
- Update to 5.2.0

* Wed Jun 08 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 5.1.0-4
- Update FHS patch (adapted from Debian)

* Tue Apr 05 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 5.1.0-3
- Enable ppc64le

* Thu Mar 31 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 5.1.0-2
- Add clang specific major version requires
- BR a specific clang/llvm major version combination

* Thu Mar 31 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 5.1.0-1
- Update to 5.1.0
- Add llvm version requirement to make sure the right version is used

* Fri Feb 11 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0.0-1
- Update to 5.0.0

* Mon Jan 17 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 4.5.2-1
- Initial package
