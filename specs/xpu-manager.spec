%global upstream_name xpumanager

Name: xpu-manager
Version: 2.1.0
Release: %{autorelease}
Summary: Intel XPU System Management Interface
License: MIT
ExclusiveArch: x86_64
URL: https://github.com/intel/xpumanager
Source0: %{url}/archive/v%{version}/%{upstream_name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: cli11-devel
BuildRequires: gcc-c++
BuildRequires: hwloc-devel
BuildRequires: intel-gsc-devel
BuildRequires: intel-metee-devel
BuildRequires: libcurl-devel
BuildRequires: libudev-devel
BuildRequires: libpciaccess-devel
BuildRequires: meson
BuildRequires: oneapi-level-zero-devel
BuildRequires: pybind11-json-devel

%description
A free and open-source solution built on top of the Intel oneAPI Level Zero
interface for monitoring and managing Intel GPUs. It is responsible for GPU
administration, location, topology, telemetry, diagnostics, firmware updating,
and GPU configuration. It supports local command-line interface and a local
library call interface for integration with third-party solutions.

%package -n     xpu-smi
Summary:        Intel XPU System Management Interface
Requires:       intel-gsc
Requires:       intel-level-zero
Requires:       intel-metrics-discovery
Requires:       intel-metrics-library
Requires:       oneapi-level-zero
Recommends:     intel-vpl-gpu-rt
Recommends:     libva-intel-media-driver
Recommends:     libvpl
%description -n xpu-smi
A free and open-source solution built on top of the Intel oneAPI Level Zero
interface for monitoring and managing Intel GPUs. It is responsible for GPU
administration, location, topology, telemetry, diagnostics, firmware updating,
and GPU configuration. It supports local command-line interface and a local
library call interface for integration with third-party solutions.

%prep
%autosetup -n %{upstream_name}-%{version}
# Extra, we don't actually need them
rm -rf THIRD_PARTY_LICENSES

%build
%meson \
   -Duse_system_levelzero=true \
   -Duse_system_igsc=true

%meson_build

%install
%meson_install

%files -n xpu-smi
%license LICENSE
%{_bindir}/xpu-smi
%{_datadir}/xpum/
%doc README.md


%changelog
%autochangelog
