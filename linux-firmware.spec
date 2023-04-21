%global debug_package %{nil}
%global firmware_release 149

%global _firmwarepath	/usr/lib/firmware
%define _binaries_in_noarch_packages_terminate_build 0

Name:		linux-firmware
Version:	20230404
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
%if 0%{?fedora} > 38
Recommends:	atheros-firmware
Recommends:	brcmfmac-firmware
Recommends:	mt7xxx-firmware
Recommends:	realtek-firmware
%else
Requires:	atheros-firmware
Requires:	brcmfmac-firmware
Requires:	mt7xxx-firmware
Requires:	realtek-firmware
%endif
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

# WiFi/Bluetooth firmwares
%package -n atheros-firmware
Summary:	Firmware for Qualcomm Atheros WiFi/Bluetooth adapters
License:	Redistributable, no modification permitted
Requires:	linux-firmware-whence
%description -n atheros-firmware
Firmware for Qualcomm Atheros ath6k/ath9k/ath10k/ath11k WiFi adapters.

%package -n brcmfmac-firmware
Summary:	Firmware for Broadcom/Cypress brcmfmac WiFi/Bluetooth adapters
License:	Redistributable, no modification permitted
Requires:	linux-firmware-whence
%description -n brcmfmac-firmware
Firmware for Broadcom/Cypress brcmfmac WiFi/Bluetooth adapters.

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

%package -n mt7xxx-firmware
Summary:	Firmware for Mediatek 7600/7900 series WiFi/Bluetooth adapters
License:	Redistributable, no modification permitted
Requires:	linux-firmware-whence
%description -n mt7xxx-firmware
Firmware for Mediatek 7600/7900 series WiFi/Bluetooth adapters

%package -n realtek-firmware
Summary:	Firmware for Realtek WiFi/Bluetooth adapters
License:	Redistributable, no modification permitted
Requires:	linux-firmware-whence
%description -n realtek-firmware
Firmware for Realtek WiFi/Bluetooth adapters

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
	-i -e '/^ar3k/d' \
	-i -e '/^ath6k/d' \
	-i -e '/^ath9k_htc/d' \
	-i -e '/^ath10k/d' \
	-i -e '/^ath11k/d' \
	-i -e '/^brcm/d' \
	-i -e '/^cypress/d' \
	-i -e '/^i915/d' \
	-i -e '/^iwlwifi/d' \
	-i -e '/^nvidia\/g/d' \
	-i -e '/^nvidia\/tu/d' \
	-i -e '/^libertas\/sd8686/d' \
	-i -e '/^libertas\/usb8388/d' \
	-i -e '/^liquidio/d' \
	-i -e '/^mellanox/d' \
	-i -e '/^mediatek\/mt76/d' \
	-i -e '/^mediatek\/mt79/d' \
	-i -e '/^mediatek\/BT/d' \
	-i -e '/^mediatek\/WIFI/d' \
	-i -e '/^mrvl\/prestera/d' \
	-i -e '/^mrvl\/sd8787/d' \
	-i -e '/^netronome/d' \
	-i -e '/^qca/d' \
	-i -e '/^radeon/d' \
	-i -e '/^rtl_bt/d' \
	-i -e '/^rtlwifi/d' \
	-i -e '/^rtw88/d' \
	-i -e '/^rtw89/d' \
	linux-firmware.files
sed -i -e 's!^!/usr/lib/firmware/!' linux-firmware.{files,dirs}
sed -i -e 's/^/"/;s/$/"/' linux-firmware.files
sed -e 's/^/%%dir /' linux-firmware.dirs >> linux-firmware.files


%files -f linux-firmware.files
%dir %{_firmwarepath}
%license LICENCE.* LICENSE.* GPL*

%files whence
%license WHENCE

# GPU firmwares
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

# WiFi/Bluetooth firmwares
%files -n atheros-firmware
%license LICENCE.atheros_firmware
%license LICENSE.QualcommAtheros_ar3k
%license LICENSE.QualcommAtheros_ath10k
%license LICENCE.open-ath9k-htc-firmware
%license qca/NOTICE.txt
%{_firmwarepath}/ar3k/
%{_firmwarepath}/ath6k/
%{_firmwarepath}/ath9k_htc/
%{_firmwarepath}/ath10k/
%{_firmwarepath}/ath11k/
%{_firmwarepath}/qca/

%files -n brcmfmac-firmware
%license LICENCE.broadcom_bcm43xx
%license LICENCE.cypress
%{_firmwarepath}/brcm/
%{_firmwarepath}/cypress/

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

%files -n mt7xxx-firmware
%license LICENCE.mediatek
%license LICENCE.ralink_a_mediatek_company_firmware
%{_firmwarepath}/mediatek/mt76*
%{_firmwarepath}/mediatek/mt79*
%{_firmwarepath}/mediatek/BT*
%{_firmwarepath}/mediatek/WIFI*

%files -n realtek-firmware
%license LICENCE.rtlwifi_firmware.txt
%{_firmwarepath}/rtl_bt/
%{_firmwarepath}/rtlwifi/
%{_firmwarepath}/rtw88/
%{_firmwarepath}/rtw89/

# SMART NIC and network switch firmwares
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
* Sun Apr 09 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 20230404-149
- Split Realtek, Qcom Atheros, Mediatek, brcmfmac WiFi/BT firmwares to subpackages
- Update to upstream 20230404 release
- nvidia: update Tu10x and Tu11x signed firmware to support newer Turing HW
- update firmware for MT7922 WiFi/Bluetooth device
- Amphion: Update vpu firmware
- iwlwifi: add new FWs from core78-32 release
- iwlwifi: update 9000-family firmwares to core78-32
- amdgpu: Update SDMA 6.0.1 firmware
- amdgpu: Add PSP 13.0.11 firmware
- amdgpu: Update PSP 13.0.4 firmware
- amdgpu: Update GC 11.0.1 firmware
- amdgpu: Update DCN 3.1.4 firmware
- amdgpu: Add GC 11.0.4 firmware
- rtw88: 8822c: Update normal firmware to v9.9.15
- Update firmware for Intel Bluetooth 9462/9560/AX101/AX203/AX210/AX211
- add firmware files for NXP BT chipsets
- rtw89: 8852b: update format-1 fw to v0.29.29.0
- rtw89: 8852b: add format-1 fw v0.29.26.0
- rtw89: 8852b: rollback firmware to v0.27.32.1
- i915: Update MTL DMC to v2.12
- i915: Update ADLP DMC to v2.19
- mediatek: Update mt8192/mt8195 SCP firmware to support MM21 and MT21
- iwlwifi: update core69 and core72 firmwares for So device

* Sun Mar 12 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 20230310-148
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
