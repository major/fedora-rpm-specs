#global candidate rc0

# Binaries not used in standard manner so debuginfo is useless
%global debug_package %{nil}

# This is a noarch package that can be built on any host architecture.
# The default configuration is to allow building only on aarch64 via
# "ExclusiveArch: aarch64".  Use "--with cross" to enable building on
# any host.
%bcond_with cross

# Rockchip rk3588 support
# https://gitlab.collabora.com/hardware-enablement/rockchip-3588/trusted-firmware-a.git
## git archive --format=tar --prefix=arm-trusted-firmware-rk35-%{rk35tag}/ %{rk35tag} | xz > arm-trusted-firmware-rk35-%{rk35tag}.tar.xz
%global rk35tag 002d8e85c

Name:    arm-trusted-firmware
Version: 2.10.0
Release: 7%{?candidate:.%{candidate}}%{?dist}
Summary: ARM Trusted Firmware
License: BSD
URL:     https://github.com/ARM-software/arm-trusted-firmware/wiki
Source0: https://github.com/ARM-software/arm-trusted-firmware/archive/v%{version}%{?candidate:-%{candidate}}.tar.gz#/%{name}-%{version}%{?candidate:-%{candidate}}.tar.gz
Source1: aarch64-bl31
Source2: arm-trusted-firmware-rk35-%{rk35tag}.tar.xz

%if %{with cross}
BuildRequires: gcc-aarch64-linux-gnu
%define cross_compile aarch64-linux-gnu-
%else
ExclusiveArch: aarch64
%define cross_compile %{nil}
%endif

BuildArch:     noarch

BuildRequires: dtc
BuildRequires: gcc
# This is needed for rk3399 which while aarch64 has an onboard Cortex-M0 base PMU
BuildRequires: gcc-arm-linux-gnu
BuildRequires: openssl-devel

%description
ARM Trusted firmware is a reference implementation of secure world software for
ARMv8-A including Exception Level 3 (EL3) software. It provides a number of
standard ARM interfaces like Power State Coordination (PSCI), Trusted Board
Boot Requirements (TBBR) and Secure Monitor.

Note: the contents of this package are generally just consumed by bootloaders
such as u-boot. As such the binaries aren't of general interest to users.

%package     -n arm-trusted-firmware-armv8
Summary:     ARM Trusted Firmware for ARMv8-A

%description -n arm-trusted-firmware-armv8
ARM Trusted Firmware binaries for various  ARMv8-A SoCs.

Note: the contents of this package are generally just consumed by bootloaders
such as u-boot. As such the binaries aren't of general interest to users.

%prep
%autosetup -n %{name}-%{version}%{?candidate:-%{candidate}} -p1

cp %SOURCE1 .
# Fix the name of the cross compile for the rk3399 Cortex-M0 PMU
sed -i 's/arm-none-eabi-/arm-linux-gnu-/' plat/rockchip/rk3399/drivers/m0/Makefile
tar xf %{SOURCE2}

%build

%undefine _auto_set_build_flags

for soc in $(cat aarch64-bl31)
do
# At the moment we're only making the secure firmware (bl31)
case $(echo $soc) in
  "k3")
    make HOSTCC="gcc $RPM_OPT_FLAGS" CROSS_COMPILE="%{cross_compile}" PLAT=$(echo $soc) TARGET_BOARD=generic SPD=opteed bl31
    make HOSTCC="gcc $RPM_OPT_FLAGS" CROSS_COMPILE="%{cross_compile}" PLAT=$(echo $soc) TARGET_BOARD=j784s4 SPD=opteed K3_USART=0x8 bl31
    make HOSTCC="gcc $RPM_OPT_FLAGS" CROSS_COMPILE="%{cross_compile}" PLAT=$(echo $soc) TARGET_BOARD=lite SPD=opteed bl31
    ;;
  "qemu_sbsa")
    make HOSTCC="gcc $RPM_OPT_FLAGS" CROSS_COMPILE="%{cross_compile}" PLAT=$(echo $soc) all fip
    ;;
  *)
    make HOSTCC="gcc $RPM_OPT_FLAGS" CROSS_COMPILE="%{cross_compile}" PLAT=$(echo $soc) bl31
    ;;
esac
done

# Build rk35 fork
pushd arm-trusted-firmware-rk35-%{rk35tag}
for soc in rk3588
do
# At the moment we're only making the secure firmware (bl31)
make HOSTCC="gcc $RPM_OPT_FLAGS" CROSS_COMPILE="%{cross_compile}" PLAT=$(echo $soc) bl31
done
popd

%install

mkdir -p %{buildroot}/%{_datadir}/%{name}

# At the moment we just support adding bl31.bin (except qemu_sbsa)
for soc in $(cat aarch64-bl31)
do
 for file in bl31.bin bl1.bin fip.bin
 do
  if [ -f build/$(echo $soc)/release/$(echo $file) ]; then
    install -pD -m 0644 build/$(echo $soc)/release/$(echo $file) %{buildroot}%{_datadir}/%{name}/$(echo $soc)/$(echo $file)
  elif [ $(echo $soc) = "k3" ]; then
    # TI K3 platforms have a different directory layout, binaries are in build/k3/$board directory
    for board in generic j784s4 lite
    do
      if [ -f build/$(echo $soc)//$(echo $board)/release/$(echo $file) ]; then
        install -pD -m 0644 build/$(echo $soc)/$(echo $board)/release/$(echo $file) %{buildroot}%{_datadir}/%{name}/$(echo $soc)-$(echo $board)/$(echo $file)
      fi
    done
  fi
 done
done

# Rockchips wants the bl31.elf, plus rk3399 wants power management co-processor bits
for soc in rk3399 rk3368 rk3328
do
 for file in bl31/bl31.elf m0/rk3399m0.bin m0/rk3399m0.elf
 do
  if [ -f build/$(echo $soc)/release/$(echo $file) ]; then
    install -pD -m 0644 build/$(echo $soc)/release/$(echo $file) %{buildroot}/%{_datadir}/%{name}/$(echo $soc)/$(echo $file)
  fi
 done
done

# Install rk35 fork
pushd arm-trusted-firmware-rk35-%{rk35tag}
for soc in rk3588
do
 for file in bl31/bl31.elf
 do
  if [ -f build/$(echo $soc)/release/$(echo $file) ]; then
    install -pD -m 0644 build/$(echo $soc)/release/$(echo $file) %{buildroot}/%{_datadir}/%{name}/$(echo $soc)/$(echo $file)
  fi
 done
done
popd

%files -n arm-trusted-firmware-armv8
%license license.rst
%doc readme.rst
%{_datadir}/%{name}

%changelog
* Mon Feb 19 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 2.10.0-7
- Minor build improvements and cleanups

* Thu Feb 15 2024 Michael Brown <mbrown@fensystems.co.uk> - 2.10.0-6
- Add qemu_sbsa platform

* Tue Feb 13 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 2.10.0-5
- Add initial rk3588 support

* Tue Feb 13 2024 Michael Brown <mbrown@fensystems.co.uk> - 2.10.0-4
- Convert to BuildArch: noarch

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Nov 23 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 2.10.0-1
- Update to 2.10,0

* Tue Nov 14 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 2.10-0.1.rc0
- Update to 2.10 RC0

* Mon Aug 28 2023 Enric Balletbo i Serra <eballetbo@redhat.com> - 2.9-3
- Add support for TI k3 SoCs

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun May 28 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 2.9-1
- Update to 2.9 GA

* Wed May 17 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 2.9-0.1.rc0
- Update to 2.9 RC0

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov 24 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 2.8-1
- Update to 2.8

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 02 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 2.7-1
- Update to 2.7 GA

* Wed May 25 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 2.7-0.1.rc0
- Update to 2.7rc0

* Mon May 16 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 2.6-3
- Enable Allwinner H616 support

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Nov 26 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 2.6-1
- Update to 2.6

* Tue Nov 23 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 2.6-0.2.rc1
- Update to 2.6 RC1

* Mon Nov 15 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 2.6-0.1.rc0
- Update to 2.6.0 RC0

* Tue Nov 02 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 2.5-3
- Fix for rk3399 suspend/resume

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed May 19 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 2.5-1
- Update to 2.5

* Thu May 13 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 2.5-0.1.rc1
- New 2.5 RC1 release

* Mon Feb 01 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 2.4-3
- Enable newer Amlogic devices

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 17 20:42:48 GMT 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 2.4-1
- New 2.4 GA release

* Fri Oct 30 17:48:26 GMT 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 2.4-0.1.rc0
- New 2.4 RC0 release

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 22 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 2.3-1
- New 2.3 GA release

* Fri Apr 10 2020 Peter Robinson <pbrobinson@fedoraproject.org> 2.3-0.1-rc0
- New 2.3 rc0 release

* Thu Mar 12 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 2.2-6
- Re-enable imx8qm imx8qx

* Thu Feb 27 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 2.2-5
- Temporarily drop imx8q ATF

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec  4 2019 Peter Robinson <pbrobinson@fedoraproject.org> 2.2-3
- Minor build fixes and cleanup

* Thu Nov 28 2019 Peter Robinson <pbrobinson@fedoraproject.org> 2.2-2
- Add Rockchip reboot fix

* Tue Nov  5 2019 Peter Robinson <pbrobinson@fedoraproject.org> 2.2-1
- New 2.2 GA release

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Mar 31 2019 Peter Robinson <pbrobinson@fedoraproject.org> 2.1-1
- New 2.1 GA release

* Tue Mar 26 2019 Peter Robinson <pbrobinson@fedoraproject.org> 2.1-0.2-rc1
- New 2.1 rc1 release

* Wed Mar 20 2019 Peter Robinson <pbrobinson@fedoraproject.org> 2.1-0.1-rc0
- New 2.1 rc0 release

* Sat Mar 16 2019 Pablo Greco <pablo@fliagreco.com.ar>  2.0-5.20190209
- Support building in el7 with devtoolset-7

* Sat Feb  9 2019 Peter Robinson <pbrobinson@fedoraproject.org> 2.0-4.20190209
- Upstream snapshot

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-3.20181204
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec  4 2018 Peter Robinson <pbrobinson@fedoraproject.org> 2.0-2.20181204
- Upstream snapshot
- Enable Marvell a3700, AMLogic gxbb

* Tue Dec  4 2018 Peter Robinson <pbrobinson@fedoraproject.org> 2.0-1
- New 2.0 GA release

* Fri Sep 21 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.6-1
- New 1.6 GA release

* Tue Sep 18 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.6-0.2-rc1
- New 1.6 rc1 release

* Mon Sep 10 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.6-0.1-rc0
- New 1.6 rc0 release

* Thu Aug 30 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.5-4.20180830
- Move to upstream snapshot
- Move from AllWinner 1.0 fork to upstream support
- Build ATF for imx8qm imx8qx rpi3 sun50i_a64 sun50i_h6

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 24 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.5-2
- Move AllWinner ATF to tagged releases. Update to 1.0-aw-6

* Fri Mar 23 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.5-1
- New 1.5 GA release

* Sun Mar 18 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.5-0.4-rc3
- New 1.5 rc3 release

* Fri Mar  9 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.5-0.3-rc2
- New 1.5 rc2 release

* Mon Mar  5 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.5-0.2-rc1
- New 1.5 rc1 release

* Sat Mar  3 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.5-0.1-rc0
- New 1.5 rc0 release
- Aarch64 fixes for Spectre and Meltdown (CVE-2017-5715) rhbz #1532143

* Sun Feb 25 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.4-5
- Updates for Rockchips 33xx series of SoCs
- Build zynqmp

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul  8 2017 Peter Robinson <pbrobinson@fedoraproject.org> 1.4.0-1
- New 1.4 release

* Fri Jun 30 2017 Peter Robinson <pbrobinson@fedoraproject.org> 1.4-0.1-rc0
- New 1.4 rc0 release
- Build hikey960

* Thu Jun  8 2017 Peter Robinson <pbrobinson@fedoraproject.org> 1.3-3.f9a050e
- Move to upstream git snapshot
- Build new hikey and rk3328

* Tue Apr 25 2017 Peter Robinson <pbrobinson@fedoraproject.org> 1.3-2
- Add support for AllWinner SoCs

* Mon Apr 24 2017 Peter Robinson <pbrobinson@fedoraproject.org> 1.3-1
- Initial package
