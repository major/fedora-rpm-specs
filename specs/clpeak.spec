Name:       clpeak
Version:    2.0.7
Release:    %autorelease
Summary:    Measure the peak achievable performance of GPU compute devices
License:    Apache-2.0
URL:        https://github.com/krrishnarraj/%{name}
Source0:    %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: glslc
BuildRequires: mesa-libGL-devel
BuildRequires: ocl-icd-devel
BuildRequires: opencl-headers
BuildRequires: vulkan-headers
BuildRequires: vulkan-loader-devel


%description
A synthetic micro-benchmark that measures the peak achievable
performance of GPU compute devices. It exercises tight vector / MAD /
MMA loops and vendor-SDK GEMM libraries (cuBLASLt on NVIDIA, MPS on
Apple) to expose what the hardware is capable of — from raw ALU peaks to
near-vendor-advertised matrix throughput.

clpeak began as an OpenCL-only tool. It now ships four interchangeable
backends — OpenCL, Vulkan, CUDA, and Metal — running back-to-back on the
same hardware, so cross-stack differences (driver lowering, instruction
scheduling, extension exposure) become visible alongside the raw peak
numbers.

%prep
%autosetup


%build
%cmake
%cmake_build


%install
%cmake_install
rm -v %{buildroot}/%{_datadir}/clpeak/LICENSE


%check
%ctest


%files
%license LICENSE
%doc README.md
%{_bindir}/clpeak


%changelog
%autochangelog
