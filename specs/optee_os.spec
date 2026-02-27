# Binaries not used in standard manner so debuginfo is useless
%global debug_package %{nil}

Name:      optee_os
Version:   4.9.0
Release:   2%{?dist}
Summary:   Trusted side of the TEE

# The TEE core of optee_os is provided under the BSD 2-Clause license. But
# there are also other software such as libraries included in optee_os.
# This "other" software will have different licenses that are compatible
# with BSD 2-Clause (i.e., non-contaminating licenses unlike GPL-v2 for example).
License:   BSD-2-Clause AND Apache-2.0 AND (BSD-2-Clause AND BSD-3-Clause) AND (BSD-2-Clause AND MIT) AND (BSD-2-Clause AND MIT-CMU) AND BSD-3-Clause AND BSD-Source-Code AND BSL-1.0 AND (GPL-2.0 OR BSD-2-Clause) AND (GPL-2.0-or-later OR BSD-2-Clause) AND (GPL-2.0 or BSD-3-Clause) AND (GPL-2.0+ or BSD-3-Clause) AND (GPL-2.0 OR MIT) AND (GPL-2.0+ OR MIT) AND ISC AND MIT AND Unlicense AND (Unlicense AND BSD-2-Clause) AND Zlib

URL:       https://www.trustedfirmware.org
Source0:   https://github.com/OP-TEE/optee_os/archive/%{version}/%{name}-%{version}.tar.gz
Source1:   aarch64-platforms

BuildRequires: dtc
BuildRequires: gcc
BuildRequires: gcc-arm-linux-gnu
BuildRequires: make
BuildRequires: python3-cryptography
BuildRequires: python3-pyelftools

ExclusiveArch: aarch64

%description
OP-TEE is a Trusted Execution Environment (TEE) designed as companion to a
non-secure Linux kernel running on Arm; Cortex-A cores using the TrustZone
technology. OP-TEE implements TEE Internal Core API v1.1.x which is the API
exposed to Trusted Applications.

Note: the contents of this package are generally just consumed by bootloaders
such as u-boot. As such the binaries aren't of general interest to users.

%package     -n optee-os-firmware-armv8
Summary:     OP-TEE Firmware for ARMv8-A
BuildArch:   noarch

%description -n optee-os-firmware-armv8
OP-TEE firmware for various ARMv8-A SoCs.

Note: the contents of this package are generally just consumed by bootloaders
such as u-boot. As such the binaries aren't of general interest to users.

%prep
%autosetup -n %{name}-%{version} -p1

cp %SOURCE1 .

%build
%undefine _auto_set_build_flags

for platform in $(cat aarch64-platforms)
do
make HOSTCC="gcc $RPM_OPT_FLAGS" CROSS_COMPILE64="" CROSS_COMPILE=arm-linux-gnu- PLATFORM="$(echo $platform)" CFG_ARM64_core=y O=builds/$(echo $platform)
done

%install
mkdir -p %{buildroot}%{_datadir}/%{name}

for platform in $(cat aarch64-platforms)
do
  mkdir -p %{buildroot}%{_datadir}/%{name}/$(echo $platform)/
  install -p -m 0644 builds/$(echo $platform)/core/tee-pager_v2.bin  /%{buildroot}%{_datadir}/%{name}/$(echo $platform)/
  # rockchip expects the .elf
  install -p -m 0644 builds/$(echo $platform)/core/tee.elf /%{buildroot}%{_datadir}/%{name}/$(echo $platform)
done

%files -n optee-os-firmware-armv8
%license LICENSE
%doc README.md
%{_datadir}/%{name}

%changelog
* Wed Feb 25 2026 Peter Robinson <pbrobinson@fedoraproject.org> - 4.9.0-2
- Enable new platforms, slight build reorg

* Tue Jan 20 2026 Peter Robinson <pbrobinson@fedoraproject.org> - 4.9.0-1
- Update to 4.9.0

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Sat Oct 25 2025 Peter Robinson <pbrobinson@fedoraproject.org> - 4.8.0-1
- Update to 4.8.0

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Jul 17 2025 Peter Robinson <pbrobinson@fedoraproject.org> - 4.7.0-1
- Update to 4.7.0
- Enable rk3588

* Mon Apr 28 2025 Peter Robinson <pbrobinson@fedoraproject.org> - 4.6.0-1
- Update to 4.6.0

* Thu Jan 30 2025 Peter Robinson <pbrobinson@fedoraproject.org> - 4.5.0-1
- Enable Xilinx ZYNQMP and Versal platforms

* Wed Jan 22 2025 Enric Balletbo i Serra <eballetb@redhat.com> - 4.5.0-0
- Update to 4.5.0

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Oct 23 2024 Zbigniew Jedrzejewski-Szmek <zbyszek@in.waw.pl> - 4.4.0-2
- Only build on aarch64

* Mon Oct 21 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 4.4.0-1
- Update to 4.4.0

* Fri Oct 11 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 4.3.0-4
- Ship tee-pager_v2.bin for all targets

* Thu Aug 1 2024 Enric Balletbo i Serra <eballetbo@redhat.com> - 4.3.0-3
- Make optee-os-firmware-armv8 noarch

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 15 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 4.3.0-1
- Update to 4.3.0

* Fri Apr 12 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 4.2.0-1
- Update to 4.2.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 4.1.0-1
- Update up 4.1.0

* Wed Jan 10 2024 Enric Balletbo i Serra <eballetbo@redhat.com> - 4.0.0-2
- Build k3-j721e OP-TEE

* Thu Nov 02 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 4.0.0-1
- Update to 4.0.0
- Build rk3399 and sunxi-a64 OP-TEE

* Tue Oct 10 2023 Enric Balletbo i Serra <eballetbo@redhat.com> - 3.22.0-4
- Add CFG_CONSOLE_UART=0x8 a extra arguments used for building OP-TEE on TI J784S4 boards

* Wed Oct 4 2023 Enric Balletbo i Serra <eballetbo@redhat.com> - 3.22.0-3
- According to the uboot build documentation use tee-raw.bin instead of tee-pager_v2.bin (is the same binary)

* Thu Sep 21 2023 Enric Balletbo i Serra <eballetbo@redhat.com> - 3.22.0-2
- Add support for TI AM62x boards

* Tue Sep 19 2023 Enric Balletbo i Serra <eballetbo@redhat.com> - 3.22.0-1
- Initial package
