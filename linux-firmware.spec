%global debug_package %{nil}
%global firmware_release 148

%global _firmwarepath	/usr/lib/firmware
%define _binaries_in_noarch_packages_terminate_build 0

Name:		linux-firmware
Version:	20230310
Release:	%{firmware_release}%{?dist}
Summary:	Firmware files used by the Linux kernel
License:	GPL+ and GPLv2+ and MIT and Redistributable, no modification permitted
URL:		http://www.kernel.org/
BuildArch:	noarch

Source0:	https://www.kernel.org/pub/linux/kernel/firmware/%{name}-%{version}.tar.xz
Patch1:		0001-Add-support-for-compressing-firmware-in-copy-firmwar.patch

BuildRequires:	make
Requires:	linux-firmware-whence
Provides:	kernel-firmware = %{version}
Obsoletes:	kernel-firmware < %{version}
Conflicts:	microcode_ctl < 2.1-0
%if 0%{?fedora} > 36
Recommends:	amd-gpu-firmware
Recommends:	intel-gpu-firmware
Recommends:	nvidia-gpu-firmware
%else
Requires:	amd-gpu-firmware
Requires:	intel-gpu-firmware
Requires:	nvidia-gpu-firmware
%endif

%description
This package includes firmware files required for some devices to
operate.

%package whence
Summary:	WHENCE License file
License:	GPL+ and GPLv2+ and MIT and Redistributable, no modification permitted
%description whence
This package contains the WHENCE license file which documents the vendor license details.

# GPU firmwares
%package -n amd-gpu-firmware
Summary:	Firmware for AMD GPUs
License:	Redistributable, no modification permitted
Requires:	linux-firmware-whence
%description -n amd-gpu-firmware
Firmware for AMD amdgpu and radeon GPUs.

%package -n intel-gpu-firmware
Summary:	Firmware for Intel GPUs
License:	Redistributable, no modification permitted
Requires:	linux-firmware-whence
%description -n intel-gpu-firmware
Firmware for Intel GPUs including GuC (Graphics Microcontroller), HuC (HEVC/H.265
Microcontroller) and DMC (Display Microcontroller) firmware for Skylake and later
platforms.

%package -n nvidia-gpu-firmware
Summary:	Firmware for NVIDIA GPUs
License:	Redistributable, no modification permitted
Requires:	linux-firmware-whence
%description -n nvidia-gpu-firmware
Firmware for NVIDIA GPUs.

# WiFi firmwares
%package -n iwl100-firmware
Summary:	Firmware for Intel(R) Wireless WiFi Link 100 Series Adapters
License:	Redistributable, no modification permitted
Version:	39.31.5.1
Release:	%{firmware_release}%{?dist}
Requires:	linux-firmware-whence
%description -n iwl100-firmware
This package contains the firmware required by the Intel wireless drivers
for Linux to support the iwl100 hardware.  Usage of the firmware
is subject to the terms and conditions contained inside the provided
LICENSE file. Please read it carefully.

%package -n iwl105-firmware
Summary:	Firmware for Intel(R) Centrino Wireless-N 105 Series Adapters
License:	Redistributable, no modification permitted
Version:	18.168.6.1
Release:	%{firmware_release}%{?dist}
Requires:	linux-firmware-whence
%description -n iwl105-firmware
This package contains the firmware required by the Intel wireless drivers
for Linux to support the iwl105 hardware.  Usage of the firmware
is subject to the terms and conditions contained inside the provided
LICENSE file. Please read it carefully.

%package -n iwl135-firmware
Summary:	Firmware for Intel(R) Centrino Wireless-N 135 Series Adapters
License:	Redistributable, no modification permitted
Version:	18.168.6.1
Release:	%{firmware_release}%{?dist}
Requires:	linux-firmware-whence
%description -n iwl135-firmware
This package contains the firmware required by the Intel wireless drivers
for Linux to support the iwl135 hardware.  Usage of the firmware
is subject to the terms and conditions contained inside the provided
LICENSE file. Please read it carefully.

%package -n iwl1000-firmware
Summary:	Firmware for Intel® PRO/Wireless 1000 B/G/N network adaptors
License:	Redistributable, no modification permitted
Version:	39.31.5.1
Epoch:		1
Release:	%{firmware_release}%{?dist}
Requires:	linux-firmware-whence
%description -n iwl1000-firmware
This package contains the firmware required by the Intel wireless drivers
for Linux to support the iwl1000 hardware.  Usage of the firmware
is subject to the terms and conditions contained inside the provided
LICENSE file. Please read it carefully.

%package -n iwl2000-firmware
Summary:	Firmware for Intel(R) Centrino Wireless-N 2000 Series Adapters
License:	Redistributable, no modification permitted
Version:	18.168.6.1
Release:	%{firmware_release}%{?dist}
Requires:	linux-firmware-whence
%description -n iwl2000-firmware
This package contains the firmware required by the Intel wireless drivers
for Linux to support the iwl2000 hardware.  Usage of the firmware
is subject to the terms and conditions contained inside the provided
LICENSE file. Please read it carefully.

%package -n iwl2030-firmware
Summary:	Firmware for Intel(R) Centrino Wireless-N 2030 Series Adapters
License:	Redistributable, no modification permitted
Version:	18.168.6.1
Release:	%{firmware_release}%{?dist}
Requires:	linux-firmware-whence
%description -n iwl2030-firmware
This package contains the firmware required by the Intel wireless drivers
for Linux to support the iwl2030 hardware.  Usage of the firmware
is subject to the terms and conditions contained inside the provided
LICENSE file. Please read it carefully.

%package -n iwl3160-firmware
Summary:	Firmware for Intel(R) Wireless WiFi Link 3160 Series Adapters
License:	Redistributable, no modification permitted
Epoch:		1
Version:	25.30.13.0
Release:	%{firmware_release}%{?dist}
Requires:	linux-firmware-whence
%description -n iwl3160-firmware
This package contains the firmware required by the Intel wireless drivers
for Linux.  Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%package -n iwl3945-firmware
Summary:	Firmware for Intel® PRO/Wireless 3945 A/B/G network adaptors
License:	Redistributable, no modification permitted
Version:	15.32.2.9
Release:	%{firmware_release}%{?dist}
Requires:	linux-firmware-whence
%description -n iwl3945-firmware
This package contains the firmware required by the iwl3945 driver
for Linux.  Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%package -n iwl4965-firmware
Summary:	Firmware for Intel® PRO/Wireless 4965 A/G/N network adaptors
License:	Redistributable, no modification permitted
Version:	228.61.2.24
Release:	%{firmware_release}%{?dist}
Requires:	linux-firmware-whence
%description -n iwl4965-firmware
This package contains the firmware required by the iwl4965 driver
for Linux.  Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%package -n iwl5000-firmware
Summary:	Firmware for Intel® PRO/Wireless 5000 A/G/N network adaptors
License:	Redistributable, no modification permitted
Version:	8.83.5.1_1
Release:	%{firmware_release}%{?dist}
Requires:	linux-firmware-whence
%description -n iwl5000-firmware
This package contains the firmware required by the iwl5000 driver
for Linux.  Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%package -n iwl5150-firmware
Summary:	Firmware for Intel® PRO/Wireless 5150 A/G/N network adaptors
License:	Redistributable, no modification permitted
Version:	8.24.2.2
Release:	%{firmware_release}%{?dist}
Requires:	linux-firmware-whence
%description -n iwl5150-firmware
This package contains the firmware required by the iwl5150 driver
for Linux.  Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%package -n iwl6000-firmware
Summary:	Firmware for Intel(R) Wireless WiFi Link 6000 AGN Adapter
License:	Redistributable, no modification permitted
Version:	9.221.4.1
Release:	%{firmware_release}%{?dist}
Requires:	linux-firmware-whence
%description -n iwl6000-firmware
This package contains the firmware required by the Intel wireless drivers
for Linux.  Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%package -n iwl6000g2a-firmware
Summary:	Firmware for Intel(R) Wireless WiFi Link 6005 Series Adapters
License:	Redistributable, no modification permitted
Version:	18.168.6.1
Release:	%{firmware_release}%{?dist}
Requires:	linux-firmware-whence
%description -n iwl6000g2a-firmware
This package contains the firmware required by the Intel wireless drivers
for Linux.  Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%package -n iwl6000g2b-firmware
Summary:	Firmware for Intel(R) Wireless WiFi Link 6030 Series Adapters
License:	Redistributable, no modification permitted
Version:	18.168.6.1
Release:	%{firmware_release}%{?dist}
Requires:	linux-firmware-whence
%description -n iwl6000g2b-firmware
This package contains the firmware required by the Intel wireless drivers
for Linux.  Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%package -n iwl6050-firmware
Summary:	Firmware for Intel(R) Wireless WiFi Link 6050 Series Adapters
License:	Redistributable, no modification permitted
Version:	41.28.5.1
Release:	%{firmware_release}%{?dist}
Requires:	linux-firmware-whence
%description -n iwl6050-firmware
This package contains the firmware required by the Intel wireless drivers
for Linux.  Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%package -n iwl7260-firmware
Summary:	Firmware for Intel(R) Wireless WiFi Link 726x/8000/9000 Series Adapters
License:	Redistributable, no modification permitted
Epoch:		1
Version:	25.30.13.0
Release:	%{firmware_release}%{?dist}
Requires:	linux-firmware-whence
Recommends:     iwlax2xx-firmware
%description -n iwl7260-firmware
This package contains the firmware required by the Intel wireless drivers
for Linux.  Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%package -n iwlax2xx-firmware
Summary:	Firmware for Intel(R) Wireless WiFi Link AX2xx Series Adapters
License:	Redistributable, no modification permitted
Requires:	linux-firmware-whence
Recommends:     iwl7260-firmware
%description -n iwlax2xx-firmware
This package contains the firmware required by the Intel wireless drivers
for Linux.  Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%package -n libertas-sd8686-firmware
Summary:	Firmware for Marvell Libertas SD 8686 Network Adapter
License:	Redistributable, no modification permitted
Requires:	linux-firmware-whence
%description -n libertas-sd8686-firmware
Firmware for Marvell Libertas SD 8686 Network Adapter

%package -n libertas-sd8787-firmware
Summary:	Firmware for Marvell Libertas SD 8787 Network Adapter
License:	Redistributable, no modification permitted
Requires:	linux-firmware-whence
%description -n libertas-sd8787-firmware
Firmware for Marvell Libertas SD 8787 Network Adapter

%package -n libertas-usb8388-firmware
Summary:	Firmware for Marvell Libertas USB 8388 Network Adapter
License:	Redistributable, no modification permitted
Epoch:		2 
Requires:	linux-firmware-whence
%description -n libertas-usb8388-firmware
Firmware for Marvell Libertas USB 8388 Network Adapter

%package -n libertas-usb8388-olpc-firmware
Summary:	OLPC firmware for Marvell Libertas USB 8388 Network Adapter
License:	Redistributable, no modification permitted
Requires:	linux-firmware-whence
%description -n libertas-usb8388-olpc-firmware
Firmware for Marvell Libertas USB 8388 Network Adapter with OLPC mesh network
support.

# SMART NIC and network switch firmwares
%package -n liquidio-firmware
Summary:	Firmware for Cavium LiquidIO Intelligent Server Adapter
License:	Redistributable, no modification permitted
Requires:	linux-firmware-whence
%description -n liquidio-firmware
Firmware for Cavium LiquidIO Intelligent Server Adapter

%package -n mlxsw_spectrum-firmware
Summary:	Firmware for Mellanox Spectrum 1/2/3 Switches
License:	Redistributable, no modification permitted
Requires:	linux-firmware-whence
%description -n mlxsw_spectrum-firmware
Firmware for Mellanox Spectrumi series 1/2/3 ethernet switches.

%package -n mrvlprestera-firmware
Summary:	Firmware for Marvell Prestera Switchdev/ASIC devices
License:	Redistributable, no modification permitted
Requires:	linux-firmware-whence
%description -n mrvlprestera-firmware
Firmware for Marvell Prestera Switchdev/ASIC devices

%package -n netronome-firmware
Summary:	Firmware for Netronome Smart NICs
License:	Redistributable, no modification permitted
Requires:	linux-firmware-whence
%description -n netronome-firmware
Firmware for Netronome Smart NICs

%prep
%autosetup -p1

%build

%install
mkdir -p %{buildroot}/%{_firmwarepath}
mkdir -p %{buildroot}/%{_firmwarepath}/updates

%if 0%{?fedora} >= 34 || 0%{?rhel} >= 9
make DESTDIR=%{buildroot}/ FIRMWAREDIR=%{_firmwarepath} installcompress
%else
make DESTDIR=%{buildroot}/ FIRMWAREDIR=%{_firmwarepath} install
%endif

#Cleanup files we don't want to ship
pushd %{buildroot}/%{_firmwarepath}
# Remove firmware shipped in separate packages already
# Perhaps these should be built as subpackages of linux-firmware?
rm -rf ess korg sb16 yamaha

# Remove source files we don't need to install
rm -rf carl9170fw
rm -rf cis/{src,Makefile}
rm -f atusb/ChangeLog
rm -f av7110/{Boot.S,Makefile}
rm -f dsp56k/{bootstrap.asm,concat-bootstrap.pl,Makefile}
rm -f iscis/{*.c,*.h,README,Makefile}
rm -f keyspan_pda/{keyspan_pda.S,xircom_pgs.S,Makefile}
rm -f usbdux/*dux */*.asm

# No need to install old firmware versions where we also provide newer versions
# which are preferred and support the same (or more) hardware
rm -f libertas/sd8686_v8*
rm -f libertas/usb8388_v5.bin*

# Remove firmware for Creative CA0132 HD as it's in alsa-firmware
rm -f ctefx.bin* ctspeq.bin*

# Remove superfluous infra files
rm -f check_whence.py configure Makefile README
popd

# Create file list but exclude firmwares that we place in subpackages
FILEDIR=`pwd`
pushd %{buildroot}/%{_firmwarepath}
find . \! -type d > $FILEDIR/linux-firmware.files
find . -type d | sed -e '/^.$/d' > $FILEDIR/linux-firmware.dirs
popd
sed -i -e 's:^./::' linux-firmware.{files,dirs}
sed \
	-i -e '/^amdgpu/d' \
	-i -e '/^radeon/d' \
	-i -e '/^i915/d' \
	-i -e '/^iwlwifi/d' \
	-i -e '/^nvidia\/g/d' \
	-i -e '/^nvidia\/tu/d' \
	-i -e '/^libertas\/sd8686/d' \
	-i -e '/^libertas\/usb8388/d' \
	-i -e '/^liquidio/d' \
	-i -e '/^mellanox/d' \
	-i -e '/^mrvl\/prestera/d' \
	-i -e '/^mrvl\/sd8787/d' \
	-i -e '/^netronome/d' \
	linux-firmware.files
sed -i -e 's!^!/usr/lib/firmware/!' linux-firmware.{files,dirs}
sed -i -e 's/^/"/;s/$/"/' linux-firmware.files
sed -e 's/^/%%dir /' linux-firmware.dirs >> linux-firmware.files


%files -f linux-firmware.files
%dir %{_firmwarepath}
%license LICENCE.* LICENSE.* GPL*

%files whence
%license WHENCE

%files -n amd-gpu-firmware
%license LICENSE.radeon LICENSE.amdgpu
%{_firmwarepath}/amdgpu/
%{_firmwarepath}/radeon/

%files -n intel-gpu-firmware
%license LICENSE.i915
%{_firmwarepath}/i915/

%files -n nvidia-gpu-firmware
%license LICENCE.nvidia
%{_firmwarepath}/nvidia/g*/
%{_firmwarepath}/nvidia/tu*/

%files -n iwl100-firmware
%license LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-100-5.ucode*

%files -n iwl105-firmware
%license LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-105-*.ucode*

%files -n iwl135-firmware
%license LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-135-*.ucode*

%files -n iwl1000-firmware
%license LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-1000-*.ucode*

%files -n iwl2000-firmware
%license LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-2000-*.ucode*

%files -n iwl2030-firmware
%license LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-2030-*.ucode*

%files -n iwl3160-firmware
%license LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-3160-*.ucode*
%{_firmwarepath}/iwlwifi-3168-*.ucode*

%files -n iwl3945-firmware
%license LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-3945-*.ucode*

%files -n iwl4965-firmware
%license LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-4965-*.ucode*

%files -n iwl5000-firmware
%license LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-5000-*.ucode*

%files -n iwl5150-firmware
%license LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-5150-*.ucode*

%files -n iwl6000-firmware
%license LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-6000-*.ucode*

%files -n iwl6000g2a-firmware
%license LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-6000g2a-*.ucode*

%files -n iwl6000g2b-firmware
%license LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-6000g2b-*.ucode*

%files -n iwl6050-firmware
%license LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-6050-*.ucode*

%files -n iwl7260-firmware
%license LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-7260-*.ucode*
%{_firmwarepath}/iwlwifi-7265-*.ucode*
%{_firmwarepath}/iwlwifi-7265D-*.ucode*
%{_firmwarepath}/iwlwifi-8000C-*.ucode*
%{_firmwarepath}/iwlwifi-8265-*.ucode*
%{_firmwarepath}/iwlwifi-9000-*.ucode*
%{_firmwarepath}/iwlwifi-9260-*.ucode*

%files -n iwlax2xx-firmware
%license LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-cc-a0-*.ucode*
%{_firmwarepath}/iwlwifi-Qu*.ucode*
%{_firmwarepath}/iwlwifi-ty-a0*
%{_firmwarepath}/iwlwifi-so-a0*

%files -n libertas-sd8686-firmware
%license LICENCE.Marvell
%dir %{_firmwarepath}/libertas
%{_firmwarepath}/libertas/sd8686*

%files -n libertas-sd8787-firmware
%license LICENCE.Marvell
%dir %{_firmwarepath}/mrvl
%{_firmwarepath}/mrvl/sd8787*

%files -n libertas-usb8388-firmware
%license LICENCE.Marvell
%dir %{_firmwarepath}/libertas
%{_firmwarepath}/libertas/usb8388_v9.bin*

%files -n libertas-usb8388-olpc-firmware
%license LICENCE.Marvell
%dir %{_firmwarepath}/libertas
%{_firmwarepath}/libertas/usb8388_olpc.bin*

%files -n liquidio-firmware
%license LICENCE.cavium_liquidio
%dir %{_firmwarepath}/liquidio
%{_firmwarepath}/liquidio/*

%files -n mrvlprestera-firmware
%license LICENCE.Marvell
%dir %{_firmwarepath}/mrvl/prestera
%{_firmwarepath}/mrvl/prestera/*

%files -n mlxsw_spectrum-firmware
%dir %{_firmwarepath}/mellanox/
%{_firmwarepath}/mellanox/*

%files -n netronome-firmware
%license LICENCE.Netronome
%dir %{_firmwarepath}/netronome
%{_firmwarepath}/netronome/*

%changelog
* Sun Feb 12 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 20230310-148
- Update to upstream 20230310 release
- qat: update licence text
- rtl_bt: Update RTL8822C BT USB firmware to 0x0CC6_D2E3
- rtl_bt: Update RTL8822C BT UART firmware to 0x05C6_D2E3
- add fw for qat_4xxx
- Fix symlinks for Intel firmware
- update firmware for mediatek bluetooth chip (MT7921)
- update firmware for MT7921 WiFi device
- iwlwifi: update core69 and core72 firmwares for Ty device
- rtlwifi: Add firmware v16.0 for RTL8710BU aka RTL8188GU
- brcm: Add nvram for the Lenovo Yoga Book X90F / X90L convertible
- brcm: Fix Xiaomi Inc Mipad2 nvram/.txt file macaddr
- brcm: Add nvram for the Advantech MICA-071 tablet
- rtl_bt: Update RTL8852C BT USB firmware to 0xD7B8_FABF
- rtl_bt: Add firmware and config files for RTL8821CS
- rtw89: 8852b: update fw to v0.29.29.0
- liquidio: remove lio_23xx_vsw.bin
- intel: avs: Add AudioDSP base firmware for CNL-based platforms
- intel: avs: Add AudioDSP base firmware for APL-based platforms
- intel: avs: Add AudioDSP base firmware for SKL-based platforms
- ath11k: WCN6855 hw2.0: update to WLAN.HSP.1.1-03125-QCAHSPSWPL_V1_V2_SILICONZ_LITE-3.6510.23
- ath11k: WCN6855 hw2.0: update board-2.bin
- ath11k: WCN6750 hw1.0: update board-2.bin
- ath11k: IPQ5018 hw1.0: add to WLAN.HK.2.6.0.1-00861-QCAHKSWPL_SILICONZ-1
- ath11k: IPQ5018 hw1.0: add board-2.bin
- ath10k: QCA6174 hw3.0: update firmware-sdio-6.bin to version WLAN.RMH.4.4.1-00174
- ath10k: WCN3990 hw1.0: update board-2.bin
- cnm: update chips&media wave521c firmware.
- amdgpu: Update GC 11.0.1 firmware
- intel: catpt: Add AudioDSP base firmware for BDW platforms

* Sun Feb 12 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 20230210-147
- Update to upstream 20230210 release
- Update AMD cpu microcode
- brcm: revert firmware files for Cypress devices
- brcm: restore previous firmware file for BCM4329 device
- rtw88: 8822c: Update normal firmware to v9.9.14
- i915: Add DMC v2.11 for MTL
- Add firmware for Cirrus CS35L41 on UM3402 ASUS Laptop
- Add missing tuning files for HP Laptops using Cirrus Amps
- i915: Add DMC v2.18 for ADLP
- amdgpu: Add VCN 4.0.2 firmware
- amdgpu: Add PSP 13.0.4 firmware
- amdgpu: Add SDMA 6.0.1 fimware
- amdgpu: Add GC 11.0.1 firmware
- amdgpu: Add DCN 3.1.4 firmware
- iwlwifi: remove old intermediate 5.15+ firmwares
- iwlwifi: remove 5.10 and 5.15 intermediate old firmwares
- iwlwifi: remove 5.4 and 5.10 intermediate old firmwares
- iwlwifi: remove 4.19 and 5.4 intermediate old firmwares
- iwlwifi: remove old unsupported older than 4.14 LTS
- update firmware for MT7921 WiFi device
- update firmware for mediatek bluetooth chip (MT7921)
- amdgpu: update vangogh firmware

* Mon Jan 23 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 20230117-146
- Update to upstream 20230117 release
- Update for Intel Bluetooth AX200/201/210/211/9260/9560
- brcm: add configuration files for CyberTan WC121
- qcom: add firmware files for Adreno A200
- rtw89: 8852c: update fw to v0.27.56.10
- QCA: Add Bluetooth firmware for QCA2066
- amdgpu: a bunch of additions/updates from amd-5.4
- iwlwifi: add/update new FWs from core76-35 release
- iwlwifi: update cc/Qu/QuZ firmwares for core76-35 release
- iwlwifi: add new FWs from core75-47 release
- iwlwifi: update 9000-family firmwares to core75-47
- amdgpu: update renoir PSP/DMCUB firmware
- amdgpu: update copyright date for LICENSE.amdgpu
- update firmware for MT7921/MT7922 WiFi device
- update firmware for mediatek bluetooth chip (MT7921/MT7922)
- cxgb4: Update firmware to revision 1.27.1.0
- qca: Update firmware files for BT chip WCN6750

* Tue Dec 20 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 20221109-145
- Update to upstream 20221214 release
- amdgpu: updated various generations to firmware for amd-5.4
- amdgpu: add various new firmware for amd-5.4
- sr150 : Add NXP SR150 UWB firmware
- brcm: add/update firmware files for brcmfmac driver
- rtl_bt: Update RTL8821C BT(USB I/F) FW to 0x75b8_f098
- QCA: Add Bluetooth firmware 2.0.0-00515 for QCA WCN785x
- update firmware for MT7916/MT7915/MT7986/MT7921
- i915: Add DMC v2.08 for DG2, DMC v2.10 for MTL

* Tue Nov 15 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 20221109-144
- Fix regression in shipping iwlwifi firmware

* Thu Nov 10 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 20221109-143
- Update to upstream 20221109 release
- Update firmware file for Intel Bluetooth 9462/9560/AX20x/AX21x
- amdgpu: update DMCUB firmware for DCN 3.1.6
- rtl_bt: Update RTL8822C BT UART firmware to 0xFFB8_ABD6
- rtl_bt: Update RTL8822C BT USB firmware to 0xFFB8_ABD3
- mrvl: prestera: Update Marvell Prestera Switchdev FW to v4.1
- iwlwifi: add new FWs from core74_pv-60 release
- qcom: drop split a530_zap firmware file
- qcom/vpu-1.0: drop split firmware in favour of the mbn file
- qcom/venus-4.2: drop split firmware in favour of the mbn file
- qcom/venus-4.2: replace split firmware with the mbn file
- qcom/venus-1.8: replace split firmware with the mbn file
- iwlwifi: add new PNVM binaries from core74-44 release
- iwlwifi: add new FWs from core69-81 release
- qcom: update venus firmware files for VPU-2.0
- qcom: remove split SC7280 venus firmware images
- qcom: update venus firmware file for v5.4
- qcom: replace split SC7180 venus firmware images with symlink
- rtw89: 8852b: update fw to v0.27.32.1
- rtlwifi: update firmware for rtl8192eu to v35.7
- rtlwifi: Add firmware v4.0 for RTL8188FU
- i915: Add HuC 7.10.3 for DG2
- cnm: update chips&media wave521c firmware.
- brcm: add symlink for Pi Zero 2 W NVRAM file
- Add firmware for Cirrus CS35L41 on ASUS/Lenovo/HP Laptops
- iwlwifi: add new FWs from core72-129 release
- iwlwifi: update 9000-family firmwares to core72-129

* Sun Oct 16 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 20221012-142
- Add link for one variant of Raspberry Pi Zero 2W WiFi module

* Thu Oct 13 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 20221012-141
- Update to upstream 20221012 release
- rtl_bt: Update RTL8852C BT USB firmware to 0xD5B8_A40A
- amdgpu: update various generations of RLC firmware
- mediatek: Update mt8195 SOF firmware to v0.4.1
- qcom: add squashed version of a530 zap shader
- rtw89: 8852c: update fw to v0.27.56.1
- mediatek: Update mt8186 SCP firmware
- Update AMD cpu microcode
- mediatek: mt8195: Update scp.img to v2.0.11956
- mediatek: Add new mt8195 SOF firmware
- mediatek: Update mt8186 SOF firmware to v0.2.1
- update firmware for mediatek bluetooth chip (MT7922)
- rtl_bt: Update RTL8852A BT USB firmware to 0xD9B8_8207
- update firmware for mediatek bluetooth chip (MT7921)
- update firmware for MT7921/MT7922 WiFi device
- cxgb4: Update firmware to revision 1.27.0.0
- i915: Add versionless HuC files for current platforms
- i915: Add GuC v70.5.1 for DG1, DG2, TGL and ADL-P
- qca: Update firmware files for BT chip WCN3991.
- Removing crnv32

* Thu Sep 29 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 20220913-140
- Update to upstream 20220913 release
- amdgpu: update yellow carp DMCUB firmware
- amdgpu: add firmware for VCN 3.1.2 IP block
- amdgpu: add firmware for SDMA 5.2.6 IP block
- amdgpu: add firmware for PSP 13.0.5 IP block
- amdgpu: add firmware for GC 10.3.6 IP block
- amdgpu: add firmware for DCN 3.1.5 IP block
- qcom: rename Lenovo ThinkPad X13s firmware paths
- rtw89: 8852c: update fw to v0.27.42.0
- Mellanox: Add new mlxsw_spectrum firmware xx.2010.3146
- amdgpu: update beige goby/dimgrey cavefish/navy flounder/sienna cichlid VCN firmware
- rtl_bt: Update RTL8852C BT USB firmware to 0xDFB8_5A33
- mediatek: reference the LICENCE file for MediaTek firmwares

* Tue Sep 13 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 20220815-139
- Use requires for GPU firmware on < Fedora 37

* Tue Aug 16 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 20220815-138
- Update to upstream 20220815 release
- mediatek: Update mt8183/mt8192/mt8195 SCP firmware
- mediatek: Add new mt8186 SOF firmware
- ice: Update package to 1.3.30.0
- QCA: Update Bluetooth WCN685x 2.1 firmware to 2.1.0-00438
- brcm: Add nvram for Lenovo Yoga Tablet 2 830F/L and 1050F/L tablets
- brcm: Add nvram for the Xiaomi Mi Pad 2 tablet
- brcm: Add nvram for the Asus TF103C tablet
- Add amd-ucode README file
- qca: Update firmware files for BT chip WCN6750
- Update firmware file for Intel Bluetooth 9462/9560/AX200/AX201/AX210/AX211
- Mellanox: Add new mlxsw_spectrum firmware xx.2010.3020
- qcom: Add firmware for Lenovo ThinkPad X13s
- Add firmware for Cirrus CS35L41
- i915: Add GuC v70.4.1 for DG2
- i915: Add DMC v2.07 for DG2
- amdgpu: update various GPUs to release 22.20
- amdgpu: partially revert "amdgpu: update beige goby to release 22.20"
- amdgpu: update psp 13.0.8 TA firmware
- amdgpu: update DMCUB firmware for DCN 3.1.6
- amdgpu: Update Yellow Carp VCN firmware
- WHENCE: Fix dangling symlinks

* Fri Aug 12 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 20220708-137
- Split out AMD/Intel/NVIDIA GPU firmware into sub packages

* Sun Jul 17 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 20220708-136
- Update to upstream 20220708 release
- WHENCE: Correct dangling symlinks
- Correct WHENCE entry for wfx firmware
- bnx2: Drop unsupported Broadcom NetXtremeII firmware
- bnx2: drop unsupported firmwares
- bnx2: sort firmware names in filesystem order
- Remove old Broadcom Everest (bnx2x) v4/5 firmware
- Drop Token Ring network firmwares
- Drop TDA7706 radio firmware
- Drop Intel WiMax firmware
- Drop Computone IntelliPort Plus serial firmware
- Drop ATM Ambassador devices firmware
- brocade: drop old unsupported firmware revs
- amdgpu: update yellow carp DMCUB firmware
- update firmwares for MT7622/MT7921/MT7922 WiFi device
- update firmware for mediatek bluetooth chips (MT7921/MT7922)
- Update firmwares for Intel Bluetooth 9462/9560/AX200/AX201/AX210/AX211
- mediatek: Add SCP firmware for MT8186
- rtw88: 8822c: Update normal firmware to v9.9.13
- amdgpu: update Yellow Carp VCN firmware
- qed: update 8.59.1.0 firmware
- Link some devices that ship with the AW-CM256SM
- Add initial AzureWave AW-CM256SM NVRAM file
- Remove the Pine64 Quartz copy of the RPi NVRAM
- qca: Update firmware files for BT chip WCN6750.
- QCA: Update Bluetooth WCN685x 2.1 firmware to 2.1.0-00409

* Tue Jun 14 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 20220610-135
- Fixes for Cypress AW-CM256SM WiFi module

* Fri Jun 10 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 20220610-134
- Update to upstream 20220610 release
- add symlinks to AP6212 for StarFive based boards
- wilc1000: update WILC1000 firmware to v15.6
- add new FWs from core70-87 release
- update 9000-family firmwares to core70-87
- Update RTL8852A BT USB firmware to 0xDFB8_0634
- replace mkdir by install
- remove old unsupported iwlwifi 3160/7260/7265/8000/8265 firmware
- Update mt8192 SCP firmware
- WCN6855 hw2.0: update to WLAN.HSP.1.1-03125-QCAHSPSWPL_V1_V2_SILICONZ_LITE-3.6510.9
- ath11k: move regdb.bin before board-2.bin
- QCA9984 hw1.0: update firmware-5.bin to 10.4-3.9.0.2-00157
- QCA9888 hw2.0: update board-2.bin
- QCA9888 hw2.0: update firmware-5.bin to 10.4-3.9.0.2-00157
- QCA4019 hw1.0: update board-2.bin
- WCN3990 hw1.0: add board-2.bin
- Update various AMDGPU firmware for 22.10
- Update firmware for Intel Bluetooth 9462/9560/AX200/AX201/AX210/AX211

* Thu May 26 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 20220509-133
- Split Mellanox Spectrum 1/2/3 Switches firmware to a sub package

* Mon May  9 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 20220509-132
- Update to upstream 20220509 release
- mediatek: Update mt8183/mt8192/mt8195 SCP firmware
- update firmware for mediatek bluetooth chip (MT7922)
- update firmware for MT7922 WiFi device
- ice: Update package to 1.3.28.0
- i915: Add GuC v70.1.2 for DG2
- i915: Add DMC v2.06 for DG2
- i915: Add GuC v70.1.1 for all platforms
- rtl_bt: Update RTL8852A BT USB firmware to 0xDBB7_C1D9
- rtl_bt: Add firmware and config files for RTL8852C
- rtw89: 8852c: add new firmware v0.27.20.0 for RTL8852C
- amdgpu: update yellow carp DMCUB firmware
- amdgpu: update psp_13_0_8 firmware
- amdgpu: update gc_10_3_7_rlc firmware
- amdgpu: update dcn_3_1_6_dmcub firmware
- qcom: add firmware files for Adreno a220/a330/a420 & related generations
- qcom: apq8096: add modem firmware
- qcom: apq8096: add aDSP firmware
- Mellanox: Add lc_ini_bundle for xx.2010.1006
- Mellanox: xx.2010.1502: Distribute non-xz-compressed lc_ini_bundle
- Mellanox: Add new mlxsw_spectrum firmware xx.2010.1502
- Numerous additions/updates for various generations of ath11k/ath10k

* Thu Apr 14 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 20220411-131
- Update to upstream 20220411 release
- Update AMD cpu microcode
- nvidia: add GA102/GA103/GA104/GA106/GA107 signed firmware
- brcm: rename Rock960 NVRAM to AP6356S and link devices to it
- Update firmware file for Intel Bluetooth 9260/9462/9560/AX200/AX201/AX210/AX211
- amdgpu: update green navi10/12/14/renoir/sardine VCN firmware
- update firmware for MT7921 WiFi device
- update firmware for mediatek bluetooth chip (MT7921)
- rtw88: 8821c: Update normal firmware to v24.11.00
- ice: Add wireless edge file for Intel E800 series driver
- ice: update ice DDP comms package to 1.3.31.0
- amdgpu: update PSP 13.0.8 firmware
- amdgpu: update GC 10.3.7 firmware
- rtl_bt: Add firmware and config files for RTL8852B

* Thu Mar 10 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 20220310-130
- Update to upstream 20220310 release
- Update AMD cpu microcode
- ath11k: add links for WCN6855 hw2.1
- ath11k: WCN6855 hw2.0: add WLAN.HSP.1.1-03125-QCAHSPSWPL_V1_V2_SILICONZ_LITE-3
- ath11k: WCN6855 hw2.0: add board-2.bin and regdb.bin
- add firmware for MT7986
- update firmware for MT7921 WiFi device
- update firmware for mediatek bluetooth chip(MT7921)
- amdgpu: update picasso/raven/raven2 VCN firmware
- amdgpu: Update GPU firmwares to the 21.50 release
- amdgpu: add firmware for SDMA 5.2.7 IP block
- amdgpu: add firmware for PSP 13.0.8 IP block
- amdgpu: add firmware for DCN 3.1.6 IP block
- amdgpu: add firmware for GC 10.3.7 IP block
- rtw89: 8852a: update fw to v0.13.36.0
- iwlwifi: add/Update new FWs from core68-60 release
- Update Intel Bluetooth FW for 7265/8260/8265/9260/9462/9560/AX2xx
- Update AMD SEV firmware
- Mellanox: Add new mlxsw_spectrum firmware xx.2010.1406
- rtl_bt: Update RTL8852A BT USB firmware to 0xDFB7_6D7A
- rtl_bt: Update RTL8822C BT USB firmware to 0x19B7_6D7D
- rtl_bt: Update RTL8822C BT UART firmware to 0x15B7_6D7D
- wfx: update to firmware 3.14
- wfx: add antenna configuration files

* Wed Feb  9 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 20220209-129
- Update to upstream 20220209 release
- i915: Add DMC firmware v2.16 for ADL-P
- i915: Add GuC v69.0.3 for all platforms
- mediatek: Update MT8173 VPU firmware to v1.1.7
- mediatek: update firmware for MT7921 WiFi and bluetooth
- mediatek: update firmware for MT7915
- mediatek: add firmware for MT7916
- Firmware updates for Intel Bluetooth 9260/9462/9560/AX200/AX201/AX210/AX211
- iwlwifi: add new FWs from core63-136 release
- iwlwifi: update 9000-family firmwares to core66-88
- Mellanox: Add new mlxsw_spectrum firmware xx.2010.1232
- add marvell CPT firmware images
- WHENCE: add missing symlink for NanoPi R1
- amdgpu: update yellow carp dmcub firmware
- QCA: Add Bluetooth nvm file for WCN685x
- QCA: Update Bluetooth WCN685x 2.1 firmware to 2.1.0-00324
- QCA: Update Bluetooth WCN685x 2.0 firmware to 2.0.0-00609
- cxgb4: Update firmware to revision 1.26.6.0
- cnm: add chips&media wave521c firmware.
- rtw88: 8822c: Update normal firmware to v9.9.11
- rtw89: 8852a: update fw to v0.13.33.0

* Mon Jan 10 2022 Adam Williamson <awilliam@redhat.com> - 20211216-128
- Don't put Prestera firmwares in main package as well as subpackage
