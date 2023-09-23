# Binaries not used in standard manner so debuginfo is useless
%global debug_package %{nil}

Name:      optee_os
Version:   3.22.0
Release:   2%{?dist}
Summary:   Trusted side of the TEE

# The TEE core of optee_os is provided under the BSD 2-Clause license. But
# there are also other software such as libraries included in optee_os.
# This "other" software will have different licenses that are compatible
# with BSD 2-Clause (i.e., non-contaminating licenses unlike GPL-v2 for example).
License:   BSD-2-Clause AND Apache-2.0 AND (BSD-2-Clause AND BSD-3-Clause) AND (BSD-2-Clause AND MIT) AND (BSD-2-Clause AND MIT-CMU) AND BSD-3-Clause AND BSD-Source-Code AND BSL-1.0 AND (GPL-2.0 OR BSD-2-Clause) AND (GPL-2.0-or-later OR BSD-2-Clause) AND (GPL-2.0 or BSD-3-Clause) AND (GPL-2.0+ or BSD-3-Clause) AND (GPL-2.0 OR MIT) AND (GPL-2.0+ OR MIT) AND ISC AND MIT AND Unlicense AND (Unlicense AND BSD-2-Clause) AND Zlib

URL:       https://www.trustedfirmware.org
Source:    https://github.com/OP-TEE/optee_os/archive/%{version}/%{name}-%{version}.tar.gz

# Trustzone is an ARM specific technology
ExclusiveArch: aarch64
BuildRequires: gcc
BuildRequires: gcc-arm-linux-gnu
BuildRequires: make
BuildRequires: python3-cryptography
BuildRequires: python3-pyelftools

%description
OP-TEE is a Trusted Execution Environment (TEE) designed as companion to a
non-secure Linux kernel running on Arm; Cortex-A cores using the TrustZone
technology. OP-TEE implements TEE Internal Core API v1.1.x which is the API
exposed to Trusted Applications.

Note: the contents of this package are generally just consumed by bootloaders
such as u-boot. As such the binaries aren't of general interest to users.

%ifarch aarch64
%package     -n optee-os-firmware-armv8
Summary:     OP-TEE Firmware for ARMv8-A

%description -n optee-os-firmware-armv8
OP-TEE firmware for various ARMv8-A SoCs.

Note: the contents of this package are generally just consumed by bootloaders
such as u-boot. As such the binaries aren't of general interest to users.
%endif

%prep
%autosetup -n %{name}-%{version} -p1

%build

%undefine _auto_set_build_flags

%ifarch aarch64
# For now only secure firmwares for k3-j784s4 and k3-am62x platforms are built
make HOSTCC="gcc $RPM_OPT_FLAGS" CROSS_COMPILE64="" CROSS_COMPILE=arm-linux-gnu- PLATFORM=k3-j784s4 CFG_ARM64_core=y O=out/k3-j784s4
make HOSTCC="gcc $RPM_OPT_FLAGS" CROSS_COMPILE64="" CROSS_COMPILE=arm-linux-gnu- PLATFORM=k3-am62x CFG_ARM64_core=y CFG_WITH_SOFTWARE_PRNG=y O=out/k3-am62x
%endif


%install

mkdir -p %{buildroot}%{_datadir}/%{name}

%ifarch aarch64
# At the moment we just support adding tee-pager_v2.bin 
mkdir -p %{buildroot}%{_datadir}/%{name}/k3-j784s4/
install -p -m 0644 out/k3-j784s4/core/tee-pager_v2.bin  /%{buildroot}%{_datadir}/%{name}/k3-j784s4/

mkdir -p %{buildroot}%{_datadir}/%{name}/k3-am62x/
install -p -m 0644 out/k3-am62x/core/tee-pager_v2.bin  /%{buildroot}%{_datadir}/%{name}/k3-am62x/

%endif

%ifarch aarch64
%files -n optee-os-firmware-armv8
%license LICENSE
%doc README.md
%{_datadir}/%{name}
%endif

%changelog
* Thu Sep 21 2023 Enric Balletbo i Serra <eballetbo@redhat.com> - 3.22.0-2
- Add support for TI AM62x boards

* Tue Sep 19 2023 Enric Balletbo i Serra <eballetbo@redhat.com> - 3.22.0-1
- Initial package
