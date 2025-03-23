Name:           rocm
Version:        6.3.3
Release:        2%{?dist}
Summary:        ROCm Metapackage
License:        MIT

Source0:        License.txt

# ROCm only working on x86_64
ExclusiveArch:  x86_64

Requires: amdsmi
Requires: hipblas
Requires: hipblaslt
Requires: hipcc
Requires: hipfft
Requires: hiprand
Requires: hipsolver
Requires: hipsparse
Requires: miopen
Requires: mivisionx
Requires: rccl
Requires: rocal
Requires: rocalution
Requires: rocblas
Requires: rocdecode
Requires: rocfft
Requires: rocjpeg
Requires: rocm-clang
Requires: rocm-clinfo
Requires: rocm-core
Requires: rocm-hip
Requires: rocminfo
Requires: rocm-omp
Requires: rocm-opencl
Requires: rocm-rpp
Requires: rocm-runtime
Requires: rocm-smi
Requires: rocrand
Requires: rocsolver
Requires: rocsparse
Requires: roctracer

%description
This is a meta package for all of the ROCm packages.

%package devel
Summary:        Development environment for ROCm
Requires: amdsmi-devel
Requires: half-devel
Requires: hipblas-common-devel
Requires: hipblas-devel
Requires: hipblaslt-devel
Requires: hipify
Requires: hipcub-devel
Requires: hipfft-devel
Requires: hiprand-devel
Requires: hipsolver-devel
Requires: hipsparse-devel
Requires: miopen-devel
Requires: mivisionx-devel
Requires: python3-tensile-devel
Requires: rccl-devel
Requires: rocal-devel
Requires: rocalution-devel
Requires: rocblas-devel
Requires: rocdecode-devel
Requires: rocfft-devel
Requires: rocjpeg-devel
Requires: rocm-clang-devel
Requires: rocm-cmake
Requires: rocm-compilersupport-macros
Requires: rocm-core-devel
Requires: rocm-hip-devel
Requires: rocm-omp-static
Requires: rocm-opencl-devel
Requires: rocm-rpm-macros
Requires: rocm-rpm-macros-modules
Requires: rocm-rpp-devel
Requires: rocm-runtime-devel
Requires: rocm-smi-devel
Requires: rocprim-devel
Requires: rocrand-devel
Requires: rocsolver-devel
Requires: rocsparse-devel
Requires: rocthrust-devel
Requires: roctracer-devel
Requires: rocwmma-devel

%description devel
This is a meta package for all of the ROCm devel packages.

%package test
Summary:        Tests for ROCm
Requires: kfdtest

%description test
This is a meta package for all of the ROCm test packages.

%prep
%setup -cT
install -pm 644 %{SOURCE0} .

%files
%license License.txt

%files devel
%license License.txt

%files test
%license License.txt

%changelog
* Fri Mar 21 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.3-2
- Add rocal
- Move hipify to devel

* Fri Mar 14 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.3-1
- Initial package
