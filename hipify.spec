%global upstreamname HIPIFY

%global rocm_release 5.7
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}

# This is a clang tool so best to build with clang
%global toolchain clang

Name:           hipify
Version:        %{rocm_version}
Release:        2%{?dist}
Summary:        Convert CUDA to HIP

Url:            https://github.com/ROCm-Developer-Tools
License:        MIT
Source0:        %{url}/%{upstreamname}/archive/refs/tags/rocm-%{version}.tar.gz#/%{upstreamname}-%{version}.tar.gz
Patch0:         0001-prepare-hipify-cmake-for-fedora.patch

BuildRequires:  cmake
BuildRequires:  compiler-rt
BuildRequires:  clang-devel
BuildRequires:  lld
BuildRequires:  llvm-devel
BuildRequires:  perl
BuildRequires:  zlib-devel

Requires:       perl

# ROCm is really only on x86_64
ExclusiveArch:  x86_64

%description
HIPIFY is a set of tools to translate CUDA source code into portable
HIP C++ automatically.

%prep
%autosetup -p1 -n %{upstreamname}-rocm-%{version}

%build
%cmake
%cmake_build

%check
echo "void f(int *a, const cudaDeviceProp *b) { cudaChooseDevice(a,b); }" > b.cu
echo "void f(int *a, const hipDeviceProp_t *b) { hipChooseDevice(a,b); }" > e.hip
./bin/hipify-perl b.cu -o t.hip
diff e.hip t.hip

%install
%cmake_install
rm -rf %{buildroot}/usr/hip


%files
%doc README.md
%license LICENSE.txt
%exclude %{_bindir}/findcode.sh
%exclude %{_bindir}/finduncodep.sh
%{_bindir}/hipconvertinplace-perl.sh
%{_bindir}/hipconvertinplace.sh
%{_bindir}/hipexamine-perl.sh
%{_bindir}/hipexamine.sh
%{_bindir}/hipify-clang
%{_bindir}/hipify-perl

%changelog
* Fri Oct 13 2023 Tom Rix <trix@redhat.com> - 5.7.0-2
- Address review comments

* Sun Oct 1 2023 Tom Rix <trix@redhat.com> - 5.7.0-1
- Initial package
