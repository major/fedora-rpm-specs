Name:       clpeak
Version:    2.0.14
Release:    %autorelease
Summary:    Measure the peak achievable performance of GPU compute devices
License:    Apache-2.0
URL:        https://github.com/krrishnarraj/%{name}
Source:     %{url}/archive/%{version}/%{name}-%{version}.tar.gz


BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: glslc
BuildRequires: opencl-headers
BuildRequires: vulkan-headers
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(OpenCL)
BuildRequires: pkgconfig(vulkan)


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

# Starting with clpeak-2.0.14 below ugly hacks are needed to fix install paths
# Fix incorrect installation paths in upstream CMakeLists.txt
sed -i 's/RUNTIME DESTINATION ./RUNTIME DESTINATION bin/' CMakeLists.txt
# Remove upstream license installation to avoid installing to /usr/LICENSE
sed -i '/install(FILES LICENSE DESTINATION .)/d' CMakeLists.txt

%build
%cmake
%cmake_build


%install
%cmake_install


%check
%ctest


%files
%license LICENSE
%doc README.md
%{_bindir}/clpeak


%changelog
%autochangelog
