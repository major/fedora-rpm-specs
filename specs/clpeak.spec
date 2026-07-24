Name:       clpeak
Version:    2.0.18
Release:    %autorelease
Summary:    Measure the peak achievable performance of GPU compute devices
License:    Apache-2.0
URL:        https://github.com/krrishnarraj/%{name}
Source:     %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Patch:      clpeak-fix-amx-tf32.patch


BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: glslc
BuildRequires: opencl-headers
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(OpenCL)
BuildRequires: pkgconfig(vulkan)
BuildRequires: vulkan-headers


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
%autosetup -p1


%build
%cmake
%cmake_build


%install
%cmake_install
# Remove the duplicate license file installed by CMake to standard datadir
rm -rf %{buildroot}%{_datadir}/clpeak

%check
%ctest


%files
%license LICENSE
%doc README.md
%{_bindir}/clpeak


%changelog
%autochangelog
