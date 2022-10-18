%global debug_package %{nil}
%global firmware_release 142

%global _firmwarepath	/usr/lib/firmware
%define _binaries_in_noarch_packages_terminate_build 0

Name:		linux-firmware
Version:	20221012
Release:	%{firmware_release}%{?dist}
Summary:	Firmware files used by the Linux kernel
License:	GPL+ and GPLv2+ and MIT and Redistributable, no modification permitted
URL:		http://www.kernel.org/
BuildArch:	noarch

Source0:	https://www.kernel.org/pub/linux/kernel/firmware/%{name}-%{version}.tar.xz
Patch1:		0001-Add-support-for-compressing-firmware-in-copy-firmwar.patch
Patch2:		0001-brcm-add-symlink-for-Pi-Zero-2-W-NVRAM-file.patch

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

* Thu Dec 16 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 20211216-127
- Update to upstream 20211216 release
- Update AMD cpu microcode
- amdgpu: add cyan skillfish firmware from 21.40
- amdgpu: numerous firmware updates from 21.40
- bnx2x: Add FW 7.13.21.0
- cxgb4: Update firmware to revision 1.26.4.0
- i915: Add DMC firmware v2.14 for ADL-P
- iwlwifi: add new FWs from core64-96 release
- iwlwifi: update 9000-family firmwares to core64-96
- Updates for Intel Bluetooth 9260/9462/9560
- Updates for Intel Bluetooth AX200/AX201/AX210/AX211
- Update firmware for Mediatek Bluetooth (MT7921)
- wilc1000: update WILC1000 firmware to v15.4.1
- mrvl: prestera: Update Marvell Prestera Switchdev v4.0
- QCA: Add Bluetooth firmware/default nvm file for WCN685x
- rtl_bt: Update RTL8761B BT UART firmware to 0x0CA9_8A6B
- rtl_bt: Update RTL8761B BT USB firmware to 0x09A9_8A6B
- rtl_bt: Update RTL8852A BT USB firmware to 0xDBA9_6937
- Update ath10k/QCA6174/hw3.0/board-2.bin

* Thu Oct 28 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 20211027-126
- Update to upstream 20211027 release
- Move Marvell Prestera Switchdev/ASIC firmware to subpackage
- i915: Update ADLP DMC v2.12
- Updated Intel Bluetooth: 9260/9462/9560/AX200/AX201/AX210/AX211
- Update Mediatek bluetooth/WiFi firmware (MT7921)
- cxgb4: Update firmware to revision 1.26.2.0
- amdgpu: Add initial firmware for Beige Goby
- amdgpu: update VCN firmware - raven/raven2/picasso/renio/vangogh/sienna cichlid/navy flounder/dimgrey cavefish
- brcm: Add 43455 based AP6255 NVRAM for the ACEPC T8 Mini PC
- rtw89: 8852a: update fw to v0.13.30.0
- QCA: Update Bluetooth firmware for WCN685x
- Update NXP Management Complex firmware to version 10.28.1
- Mellanox: Add new mlxsw_spectrum firmware xx.2010.1006
- bnx2x: Add FW 7.13.20.0
- Update AMD cpu microcode

* Wed Oct  6 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 20210919-125
- Cross Recommends iwl7260-firmware <-> iwlax2xx-firmware

* Mon Oct  4 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 20210919-124
- Attempt another pass at installing new AX2xx if iwl7260 is installed

* Sat Oct  2 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 20210919-123
- Update to upstream 20210919 release
- Split Intel wireless AX2xx series to a separate package
- qed: Add firmware 8.59.1.0
- Update Intel Bluetooth firmware AX211/AX210/AX201/AX200/9560/9260/8265
- Add firmware for mediatek bluetooth chip (MT7922)
- Update firmware for mediatek bluetooth chip (MT7921)
- Update AMD SEV firmware
- amdgpu: add firmware for Yellow Carp
- rtl_bt: Update RTL8852A/RTL8822C/RTL8822C firmware
- rtl_nic: update firmware of RTL8153C
- Mellanox: Add new mlxsw_spectrum firmware xx.2008.3326
- iwlwifi: add FWs for new So device types with multiple RF modules

* Sun Aug 22 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 20210818-122
- Update to upstream 20210818 release
- amdgpu: revert back to older picasso/raven/raven2 sdma firmware
- amdgpu: add initial vangogh support
- amdgpu: update various generations for firmware 21.30
- i915: Add v2.03 DMC for RKL/Add v2.12 DMC for TGL
- Update mediatek bluetooth (MT7921), new support (MT7922)
- Update firmware file for Intel Bluetooth AX210
- qca: Add firmware files for BT chip WCN6750.
- iwlwifi: add ty firmware from Core63-43

* Fri Jul 16 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 20210716-121
- Update to upstream 20210716 release
- update NXP 8897/8997 firmware images
- rtlwifi: de-dupe rtl8723b/rtl8192e SDIO/USB WiFi firmware
- Mediatek: update WiFi/bluetooth chip (MT7921)
- Mediatek: update MT7915 firmware to 20201105
- Mellanox: Add new mlxsw_spectrum firmware xx.2008.2946
- cxgb4: Update firmware to revision 1.26.0.0
- firmware/i915/guc: Add HuC v7.9.3 for TGL & DG1
- firmware/i915/guc: Add GuC v62.0.3 for ADL-P
- firmware/i915/guc: Add GuC v62.0.0 for all platforms
- nvidia: fix symlinks for tu104/tu106 acr unload firmware
- iwlwifi: new/updated 8000/9000/other from core60-51 release
- Update firmware file for Intel Bluetooth AX210/201/200
- rtw88: 8822c: Update normal firmware to v9.9.10
- rtl_bt: Update RTL8852A BT(UART I/F) FW to 0xD9A8_A0CD
- rtl_bt: Update RTL8822C BT(UART I/F) FW to 0x05A8_C6B4
- rtl_bt: Update RTL8822C BT(USB I/F) FW to 0x09A8_A0CB
- rtl_bt: Add rtl8761b/rtl8761bu firmware
- QCA: Update Bluetooth firmware for QCA6174/QCA6390
- QCA: Add Bluetooth firmware for WCN685x
- amdgpu: update 21.20 vcn firmware for green sardine, renoir, navi10/12/14
- amdgpu: add initial dimgrey cavefish firmware from 21.20
- amdgpu: updated 21.20 firmware for: Picasso, green sardine, arcturus
  vega10/12/20, navi10/12/14, raven1/2, renoir, navy flounder
- cypress: update firmware: cyw54591/cyw43570 pcie
- cypress: update firmware: cyw4373/cyw4356/cyw4354/cyw43455/cyw43430/cyw43340/cyw43012 sdio

* Wed May 12 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 20210511-120
- Update to upstream 20210511 release
- nvidia: Update Tegra194 XUSB firmware to v60.09
- nvidia: Update Tegra186 XUSB firmware to v55.18
- nvidia: Update Tegra210 XUSB firmware to v50.26
- nvidia: Add VIC firmware for Tegra194
- update firmware for cadence mhdp8546
- i915: Add ADL-P DMC Support
- qcom: add gpu firmwares for sc7280
- qcom: Add venus firmware files for VPU-2.0
- qcom: update venus firmware files for v5.4
- qcom: sm8250: update remoteproc firmware
- qcom: update a650 firmware files
- QCA: Update Bluetooth firmware for QCA6174
- WHENCE: link to similar config file for rtl8821a support
- rtw89: 8852a: update fw to v0.13.8.0
- rtw88: 8822c: Update normal firmware to v9.9.9
- rtl_bt: Update RTL8852A BT USB firmware to 0xD9A8_7893
- rtl_bt: Add rtl8723bs_config-OBDA0623.bin symlink
- rtl_bt: Update RTL8822C BT(UART I/F) FW to 0x59A_76A3
- rtl_nic: add new firmware for RTL8153 and RTL8156 series
- Intel: Update firmware for Intel Bluetooth AX210/201/200, 9560, 9260, 8265
- Intel BT 7265: Fix Security Issues
- mrvl: prestera: Add Marvell Prestera Switchdev firmware 3.0 version
- amdgpu: update GPU firmwares from 21.10
- amdgpu: add initial support for arcturus, navy flounder
- amdgpu: add new polaris 12 MC firmware
- amdgpu: update navi10/14 smc firmware
- cxgb4: Update firmware to revision 1.25.4.0
- Mellanox: Add new mlxsw_spectrum firmware xx.2008.2438
- nfp: update Agilio SmartNIC flower firmware to rev AOTC-2.14.A.6
- brcm: add missing symlink for Pi Zero W NVRAM file
- brcm: Add a link to enable khadas VIM2's WiFi
- brcm: Link CM4's WiFi firmware with DMI machine name.
- brcm: Add nvram for the Chuwi Hi8 (CWI509) tablet
- brcm: Add nvram for the Predia Basic tablet

* Mon Mar 15 2021 Peter Robinson <pbrobinson@fedoraproject.org> 20210315-119
- Update to upstream 20210315 release
- Update to Intel Bluetooth AX200/201 firmware
- rtw88: 8822c: Update normal firmware to v9.9.6
- rtw89: 8852a: add firmware v0.9.12.2
- iwlwifi: updates for 9000-family/7265D/core59-66 (cc, Qu, QuZ, ty)
- amdgpu: add initial firmware for green sardine
- Silabs new WF200 firmware
- Mellanox: Add new mlxsw_spectrum firmware xx.2008.2406
- Added Mediatek bluetooth chip (MT7921)

* Mon Mar 08 2021 Peter Robinson <pbrobinson@fedoraproject.org> 20210208-118
- Fix for Raspberry Pi 4 WiFi

* Mon Feb  8 2021 Peter Robinson <pbrobinson@fedoraproject.org> 20210208-117
- Update to upstream 20210208 release
- rtl_bt: Updates for RTL8822C, RTL8821C, added RTL8852A
- Link Cypress brcmfmac firmwares to old brcm location
- brcm NVRAM updates for Raspberry Pi, added 96boards Rock960
- QCom SM8250 (SD865) firmware for Compute, Audio DSPs, Adreno a650, venus VPU-1.0
- i915: Added firmware for DG1, ADL-S
- Uodated bluetooth firmware for Intel Bluetooth AX200/201/210
- rtw88: RTL8821C: Update firmware to v24.8
- New MT7921 firmware
- Mellanox: Add new mlxsw_spectrum firmware xx.2008.2304

* Sat Dec 19 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 20201218-116
- Update to upstream 20201218 release
- AMD gpu: Updates for vega10/12/20, renoir, navi10/12/14, raven1/2
- AMD gpuL add sienna cichlid
- Update AMD SEV firmware
- Add Mellanox mlxsw_spectrum xx.2008.2018 firmware
- i915: Add GuC firmware v49.0.1
- Intel bluetooth updates for AX200/201/210, 9560, 9260
- Add Lontium LT9611UXC DSI to HDMI bridge firmware
- Update QCA WCN3991 firmware
- Update mediatek MT8173 VPU firmware to v1.1.6

* Thu Nov 19 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 20201118-115
- Update to upstream 20201118 release
- rtw88: RTL8822C: Update firmware to v9.9.4
- amdgpu: update picasso/raven/raven2 VCN firmware
- rtl_bt: Update RTL8822C BT(USB I/F) FW to 0x099A_281A
- QCA: Update Bluetooth firmware for QCA6390
- qcom : updated venus firmware files for v5.4
- QCA : Fixed BT SSR due to command timeout / IO fatal error
- ath11k: Updated firmware for QCA6390/IPQ8074/IPQ6018
- ath10l: Updated firmware for QCA9984/QCA9888/QCA6174

* Thu Nov 19 2020 Dave Airlie <airlied@redhat.com> - 20201022-114
- Update AMDGPU fw for 6800

* Fri Oct 23 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 20201022-113
- Update to upstream 20201022 release
- All symlinks created using WHENCE links option
- Update Marvell Switchdev firmware with ABI changes
- Mellanox: Add new mlxsw_spectrum firmware xx.2008.1312
- Cadence MHDP8546 DP bridge
- Intel Bluetooth updates for: 7265(D1)
- iwlwifi: update 3168, 7265D, 8000C, 8265, core56-54 firmwares
- QCA WCN3991 updates
- TI VPDMA 1b8.bin firmware
- amdgpu: navi10/12/14/picasso/raven/renoir/vega10/12/20 update to 20.40
- ice: add comms for Intel E800 series driver, firmware to 1.3.16.0
- qcom : updated venus firmware
- i915: Add DG1 DMC v2.02
- mediatek: VPU: separate venc service
- ath10k: add SDIO firmware for QCA9377 WiFi
- rtl_bt: Update RTL8821C BT FW to 0xAA6C_A99E
- cypress: add Cypress firmware and clm_blob files for:
  43012, 43340, 43362, 4339, 43430, 43455, 4354, 4356, 43570, 4373, 54591

* Fri Sep 18 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 20200918-112
- amdgpu firmware for 20.30: navi10/12
- wl18xx: update firmware file 8.9.0.0.83
- mt7615: update firmware to 20200814
- qcom: Add updated a5xx and a6xx microcode
- mediatek: update MT7915 firmware to 20200819
- Intel Bluetooth updates 9260/9560/AX201/AX200
- AMD SEV firmware update
- Mellanox: Add new mlxsw_spectrum firmware xx.2008.1310

* Mon Aug 17 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 20200817-111
- Update to upstream 20200817 release
- Link Raspberry Pi 3A+ WiFi NVRAM to the 3B+ NVRAM
- Update RTL8822C BT UART firmware to 0x0599_8A4F
- i915: Add DMC FW 2.02 for RKL, 2.08 for TGL, HuC FW v7.5.0 for TGL
- amdgpu: update vega20/12/10, renoir, raven/2, picasso, navi10/14 firmware for 20.30
- update NXP SDSD-8997 firmware image
- Mellanox: Add new mlxsw_spectrum firmware xx.2008.1036

* Tue Jul 21 2020 Peter Robinson <pbrobinson@fedoraproject.org> 20200721-110
- Update to upstream 20200721 release
- Bluetooth updates for Intel AX200/AX201/9560/9260, QCom QCA6390
- rtl_nic updated RTL8125B
- WiFi: WCN3991, MT7663, wilc1000 FW v15.4
- amdgpu: add UVD firmware for SI asics

* Fri Jun 19 2020 Peter Robinson <pbrobinson@fedoraproject.org> 20200619-109
- Update to upstream 20200619 release
- Bluetooth updates: Intel 9260/9560/AX200/AX201
- mlxsw_spectrum firmware xx.2007.1168
- rtl_nic firmware for RTL8125B
- rtw88: RTL8822C firmware v9.9
- cxgb4 firmware 1.24.17.0
- mrvl: firmware for Prestera ASIC devices

* Tue May 19 2020 Peter Robinson <pbrobinson@fedoraproject.org> 20200519-108
- Update to upstream 20200519 release
- Bluetooth updates: Intel 9260/9560/AX200/AX201, new QCA9377
- wifi: rtw88: support RTL8723DE, update RTL8821C
- wifi: intel: update 8265/7265D/3168/8000C/9000/9260cc/Qu

* Tue Apr 21 2020 Peter Robinson <pbrobinson@fedoraproject.org> 20200421-107
- Update to upstream 20200421 release
- amdgpu: Update vega20/12/10, renoir, raven, raven2, picasso, navi10/14 for 20.10
- Bluetooth updates for Intel AX201/AX200, RTL8822C, QCA6390
- Add firmware for MT7663 Wifi/BT combo and mt8183 SCP devices
- cxgb4: Update firmware to 1.24.14.0, T6 config update

* Mon Mar 16 2020 Peter Robinson <pbrobinson@fedoraproject.org> 20200316-106
- Update to upstream 20200316 release
- Bluetooth firmware updates: Intel, QCom, RTL8822C
- Agilio SmartNIC flower firmware to rev AOTC-2.12.A.13
- amdgpu: Update to raven2, renoir, navi10, vega10, vega12, vega20
- Intel i915: HuC, DMC firmware updates
- nvidia: add TU116/117 signed firmware
- amlogic: video decoder firmware updates
- rtl_nic: update firmware for RTL8153A

* Wed Jan 22 2020 Peter Robinson <pbrobinson@fedoraproject.org> 20200122-105
- Update to upstream 20200122 release
- Intel bluetooth updates: AX200/AX201/9560
- nvidia: TU102/TU104/TU106 signed firmware
- AMD: update navi10/14, radeon, vega10/12/20, picasso, raven firmware
- qed, mediatek, Mellanox updates
- QCom SDM845 WLAN firmware
- ath10k: updates for WCN3990, QCA9984, QCA988X, QCA9888, QCA9887, QCA6174
- Update AMD cpu microcode for processor family 17h

* Mon Dec 16 2019 Peter Robinson <pbrobinson@fedoraproject.org> 20191215-104
- Update to upstream 20191215 release
- qcom: Add SDM845 firmwares for modem, Audio DSP, Compute DSP
- Realtek firmwares for RTL8153, RTL8822CU, RTL8168fp/RTL8117, rtw88
- Storage firmwares for mlxsw, cxgb4, QL4xxxx, bnx2x
- amdgpu: raven/navi14/navi10 , i915
- NXP Management Complex: LS108x, LS208x, LX2160.
- Raspberry Pi 4 WiFi NVRAM

* Tue Oct 22 2019 Josh Boyer <jwboyer@fedoraproject.org> 20191022-103
- Rework to use upstream install

* Mon Sep 23 2019 Peter Robinson <pbrobinson@fedoraproject.org> 20190923-102
- Update Intel WiFi and Bluetooth firmwares
- Mellanox new mlxsw_spectrum firmware 13.2000.1886
- Some new Broadcom NVRAM for new devices
- Firmware rtl8125a-3 for Realtek's 2.5Gbps chip RTL8125
- Updated nvidia tegra firmwares
- Updated i915, QCom Adreno a630, amdgpu Navi10 firmware

* Thu Aug 15 2019 Peter Robinson <pbrobinson@fedoraproject.org> 20190815-101
- Updates for various ath10k and rtw88 Wireless firmwares
- Update NXP Layerscape Management Complex firmware
- update Agilio SmartNIC flower firmware
- cxgb4 firmware update

* Tue Aug  6 2019 Peter Robinson <pbrobinson@fedoraproject.org> 20190717-100
- Pull in upstream intel iwliwfi firmware updates WiFi/BT firmware issues (RHBZ 1733369)

* Wed Jul 17 2019 Peter Robinson <pbrobinson@fedoraproject.org> 20190717-99
- Update to upstream 20190717 release
- New/updated Intel iwlwifi/bluetooth firmware for various generations
- New RS9116 chipset firmware for rsi
- Updated Intel i915 / AMD gpu firmware

* Mon Jul 15 2019 Dave Airlie <airlied@redhat.com> - 20190618-98
- Add some navi firmware (not upstream yet, soon)

* Wed Jun 19 2019 Peter Robinson <pbrobinson@fedoraproject.org> 20190618-97
- Update to upstream 20190618 release
- Updated mhdp8546 DP, nvidia, AMD firmware
- New/updated wireless for Redpine 9113, Intel 9260/9560/22161 Bluetooth
- i.MX SDMA and CNN55XX crypto firmware update

* Tue May 14 2019 Peter Robinson <pbrobinson@fedoraproject.org> 20190514-96
- Update to upstream 20190514 release

* Tue Apr 16 2019 Peter Robinson <pbrobinson@fedoraproject.org> 20190416-95
- Update to upstream 20190416 release

* Wed Mar 13 2019 Josh Boyer <jwboyer@fedoraproject.org> 20190312-94
- Update to upstream 20190312 release
- amgpug, rtl, AMD SEV, and other various updates

* Thu Feb 14 2019 Peter Robinson <pbrobinson@fedoraproject.org> 20190213-93.git710963fe
- ath10k updates for QCA6174/QCA9888/QCA988X/QCA9984
- Marvell updates for SD8977/SD8897-B0/PCIe-USB8997
- amdgpu: add firmware for vega20 from 18.50
- nvidia: add TU10x typec controller firmware
- bnx2x: Add FW 7.13.11.0

* Thu Feb  7 2019 Peter Robinson <pbrobinson@fedoraproject.org> 20190118-92.gita8b75cac
- Split out LiquidIO and Netronome firmware to their own package
- Ship just one copy of WHENCE

* Tue Jan 22 2019 Peter Robinson <pbrobinson@fedoraproject.org> 20190118-91.gita8b75cac
- Latest Intel 9000 series WiFi/Bluetooth firmware
- Marvell WiFi (USB8801), cxgb4, amdgpu updates
- Raspberrp Pi 3-series NMRAM updates

* Wed Dec 19 2018 Justin M. Forbes <jforbes@fedoraproject.org> - 20181219-89.git0f22c852
- Latest upstream snapshot

* Fri Oct 12 2018 Peter Robinson <pbrobinson@fedoraproject.org> 20181008-88.gitc6b6265d
- update BT firmwares for QCA ROME, TI CC2560(A), mt7668u
- Update WiFi firmware for Marvell SD8997, iwlwifi 7000, 8000 and 9000 series, Realtek rtw88
- nvidia: add GV100 signed firmware
- Agilio SmartNIC firmwares
- Raspberry Pi 3/3B+ WiFi fixes

* Mon Oct  1 2018 Peter Robinson <pbrobinson@fedoraproject.org> 20180913-87.git44d4fca9
- Latest upstream snapshot
- Minor spec cleanups

* Wed Aug 15 2018 Josh Boyer <jwboyer@fedoraproject.org> - 20180815-86.gitf1b95fe5
- Latest upstream snapshot

* Fri May 25 2018 Josh Boyer <jwboyer@fedoraproject.org> - 20180525-85.git7518922b
- Latest upstream snapshot

* Mon May 07 2018 Josh Boyer <jwboyer@fedoraproject.org> - 20180507-84.git8fc2d4e5
- Latest upstream snapshot

* Mon Apr 02 2018 Josh Boyer <jwboyer@fedoraproject.org> - 20180402-83.git8c1e439c
- Latest upstream snapshot

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 20171215-82.git2451bb22.1
- Escape macros in %%changelog

* Fri Jan 05 2018 Josh Boyer <jwboyer@fedoraproject.org> 20171215-92.git2451bb22
- Add amd-ucode for fam17h

* Fri Dec 15 2017 Josh Boyer <jwboyer@fedoraproject.org> 20171215-81.git2451bb22
- Updated skl DMC, cnl audio, netronome SmartNIC, amdgpu vega10 and raven,
  intel bluetooth, brcm CYW4373, and liquidio vswitch firmwares

* Sun Nov 26 2017 Josh Boyer <jwboyer@fedoraproject.org> 20171126-80.git17e62881
- Updated bcm 4339 4354 4356 4358 firmware, new bcm 43430
- Fixes CVE-2016-0801 CVE-2017-0561 CVE-2017-9417

* Thu Nov 23 2017 Peter Robinson <pbrobinson@fedoraproject.org> 20171123-79.git90436ce
- Updated Intel GPU, amdgpu, iwlwifi, mvebu wifi, liquidio, QCom a530 & Venus, mlxsw, qed
- Add iwlwifi 9000 series

* Wed Oct 11 2017 Peter Robinson <pbrobinson@fedoraproject.org> 20171009-78.gitbf04291
- Updated cxgb4, QCom gpu, Intel OPA IB, amdgpu, rtlwifi
- Ship the license in %%license for all sub packages
- Modernise spec

* Mon Sep 18 2017 Josh Boyer <jwboyer@fedoraproject.org> - 20170828-77.gitb78acc9
- Add patches to fix ath10k regression (rhbz 1492161)

* Mon Aug 28 2017 Josh Boyer <jwboyer@fedoraproject.org> - 20170828-76.gitb78acc9
- Update to latest upstream snapshot
- ath10k, iwlwifi, kabylake, liquidio, amdgpu, and cavium crypot updates

* Thu Jun 22 2017 Josh Boyer <jwboyer@fedoraproject.org> - 20170622-75.gita3a26af2
- Update to latest upstream snapshot
- imx, qcom, and tegra ARM related updates

* Mon Jun 05 2017 Josh Boyer <jwboyer@fedoraproject.org> - 20170605-74.git37857004
- Update to latest upstream snapshot

* Wed Apr 19 2017 Josh Boyer <jwboyer@fedoraproject.org> - 20170419-73.gitb1413458
- Update to the latest upstream snapshot
- New nvidia, netronome, and marvell firmware
- Updated intel audio firmware

* Mon Mar 13 2017 Josh Boyer <jwboyer@fedoraproject.org> - 20170313-72.git695f2d6d
- Update to the latest upstream snapshot
- New nvidia, AMD, and i915 GPU firmware
- Updated iwlwifi and intel bluetooth firmware

* Mon Feb 13 2017 Josh Boyer <jwboyer@fedoraproject.org> - 20170213-71.git6d3bc888
- Update to the latest upstream snapshot

* Wed Feb 01 2017 Stephen Gallagher <sgallagh@redhat.com> - 20161205-70.git91ddce49
- Add missing %%license macro

* Mon Dec 05 2016 Josh Boyer <jwboyer@fedoraproject.org> 20161205-69.git91ddce49
- Update to the latest upstream snapshot
- New intel bluetooth and rtlwifi firmware

* Fri Sep 23 2016 Josh Boyer <jwboyer@fedoraproject.org> 20160923-68.git42ad5367
- Update to the latest upstream snapshot
- ath10k, amdgpu, mediatek, brcm, marvell updates
 
* Tue Aug 16 2016 Josh Boyer <jwboyer@fedoraproject.org> 20160816-67.git7c3dfc0b
- Update to the latest upstream snapshot (rhbz 1367203)
- Intel audio, rockchip, amdgpu, iwlwifi, nvidia pascal updates

* Thu Jun 09 2016 Josh Boyer <jwboyer@fedoraproject.org> 20160609-66.gita4bbc811
- Update to the latest upstream snapshot
- Intel bluetooth, radeon smc, Intel braswell/broxton audio, cxgb4 updates

* Thu May 26 2016 Josh Boyer <jwboyer@fedoraproject.org> 20160526-65.git80d463be
- Update to the latest upstream snapshot
- amdgpu, Skylake audio, and rt2xxx wifi firmware updates

* Thu May 05 2016 Josh Boyer <jwboyer@fedoraproject.org> 20160505-64.git8afadbe5
- Update to the latest upstream snapshot
- AMD, intel, and QCA6xxx updates (rhbz 1294263)

* Mon Mar 21 2016 Josh Boyer <jwboyer@fedoraproject.org> 20160321-63.git5f8ca0c
- Update to latest upstream snapshot
- New Skylake GuC and audio firmware, AMD ucode updates

* Wed Mar 16 2016 Josh Boyer <jwboyer@fedoraproject.org> 20160316-62.gitdeb1d836
- Update to latest upstream snapshot
- New firmware for iwlwifi 3168, 7265D, 8000C, and 8265 devices

* Thu Feb 04 2016 Josh Boyer <jwboyer@fedoraproject.org> 20160204-61.git91d5dd13
- Update to latest upstream snashot
- rtlwifi, iwlwifi, intel bluetooth, skylake audio updates

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20151214-60.gitbbe4917c.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 14 2015 Josh Boyer <jwboyer@fedoraproject.org> 20151214-60.gitbbe4917c
- Update to latest upstream snapshot
- Includes firmware for mt7601u (rhbz 1264631)

* Mon Nov 30 2015 Josh Boyer <jwboyer@fedoraproject.org> 20151130-59.gita109a8ff
- Update to latest upstream snapshot
- Includes -16 ucode for iwlwifi, skylake dmc and audio updates, brcm updates
  bnx2x, and others

* Fri Oct 30 2015 Josh Boyer <jwboyer@fedoraproject.org> 20151030-58.git66d3d8d7
- Update to latest upstream snapshot
- Includes ath10k and mwlwifi firmware updates (rhbz 1276360)

* Mon Oct 12 2015 Josh Boyer <jwboyer@fedoraproject.org> 20151012-57.gitd82d3c1e
- Update to latest upstream snapshot
- Includes skylake and intel bluetooth firmware updates

* Fri Sep 04 2015 Josh Boyer <jwboyer@fedoraproject.org> 20150904-56.git6ebf5d57
- Update to latest upstream git snapshot
- Includes amdgpu firmware and skylake updates

* Thu Sep 03 2015 Josh Boyer <jwboyer@fedoraproject.org> 20150903-55.git38358cfc
- Add firmware from Alex Deucher for amdgpu driver (rhbz 1259542)

* Thu Sep 03 2015 Josh Boyer <jwboyer@fedoraproject.org>
- Update to latest upstream git snapshot
- Updates for nvidia, bnx2x, and atmel devices

* Wed Jul 15 2015 Josh Boyer <jwboyer@fedoraproject.org> 20150715-54.git69640304
- Update to latest upstream git snapshot
- New iwlwifi firmware for 726x/316x/8000 devices
- New firmware for i915 skylake and radeon devices
- Various other updates

* Tue Jun 23 2015 Josh Boyer <jwboyer@fedoraproject.org> 20150521-53.git3161bfa4
- Don't obsolete ivtv-firmware any longer (rhbz 1232773)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20150521-52.git3161bfa4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 21 2015 Josh Boyer <jwboyer@fedoraproject.org> 20150521-52.git3161bfa4
- Update to latest upstream git snapshot
- Updated iwlwifi 316x/726x firmware
- Add cx18-firmware Obsoletes from David Ward (rhbz 1222164)

* Wed May 06 2015 Josh Boyer <jwboyer@fedoraproject.org> 20150415-51.gitec89525b
- Obsoletes ivtv-firmware (rbhz 1211055)

* Fri May 01 2015 Josh Boyer <jwboyer@fedoraproject.org> 20150415-50.gitec89525b
- Add v4l-cx25840.fw back now that ivtv-firmware is retired (rhbz 1211055)

* Tue Apr 14 2015 Josh Boyer <jwboyer@fedoraproject.org> 20150415-49.gitec89525b
- Fix conflict with ivtv-firmware (rhbz 1203385)

* Fri Apr 10 2015 Josh Boyer <jwboyer@fedoraproject.org> 20150415-47.gitec89525b
- Update to the latest upstream git snapshot

* Thu Mar 19 2015 Josh Boyer <jwboyer@fedoraproject.org>
- Ship the cx18x firmware files (rhbz 1203385)

* Mon Mar 16 2015 Josh Boyer <jwboyer@fedoraproject.org> 20150316-46.git020e534e
- Update to latest upstream git snapshot

* Fri Feb 13 2015 Josh Boyer <jwboyer@fedoraproject.org> 20150213-45.git17657c35
- Update to latest upstream git snapshot
- Firmware for Surface Pro 3 WLAN/Bluetooth (rhbz 1185804)

* Thu Jan 15 2015 Josh Boyer <jwboyer@fedoraproject.org> 20150115-44.git78535e88.fc22
- Update to latest upstream git snapshot
- Adjust iwl{3160,7260} version numbers (rhbz 1167695)

* Tue Oct 14 2014 Josh Boyer <jwboyer@fedoraproject.org> 20141013-43.git0e5f6377.fc22
- Fix 3160/7260 version numbers (rhbz 1110522)

* Mon Oct 13 2014 Josh Boyer <jwboyer@fedoraproject.org> 20141013-42.git0e5f6377.fc22
- Update to latest upstream git snapshot

* Fri Sep 12 2014 Josh Boyer <jwboyer@fedoraproject.org> 20140912-41.git365e80cce.fc22
- Update to the latest upstream git snapshot

* Thu Aug 28 2014 Josh Boyer <jwboyer@fedoraproject.org>
- Update to latest upstream git snapshot for new radeon firmware (rhbz 1130738)
- Fix versioning after mass rebuild and for iwl5000-firmware (rhbz 1130979)

* Fri Aug 08 2014 Kyle McMartin <kyle@fedoraproject.org> 20140808-39.gitce64fa89.1
- Update from upstream linux-firmware.
- Nuke unapplied radeon patches.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20140605-38.gita4f3bc03.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jun 05 2014 Josh Boyer <jwboyer@fedoraproject.org> - 20140605-38.gita4f3bc03
- Updates for Intel 3160/7260/7265 firmware (1087717)
- Add firmware for rtl8723be (rhbz 1091753)
- Updates for radeon CIK, SI/CI, and Mullins/Beema GPUs (rhbz 1094153)
- Various other firmware updates

* Mon Mar 17 2014 Josh Boyer <jwboyer@fedoraproject.org>
- Updates for Intel 3160/7260 and BCM43362 (rhbz 1071590)

* Tue Mar 04 2014 Josh Boyer <jwboyer@fedoraproject.org>
- Fixup Intel wireless package descriptions and Source0 (rhbz 1070600)

* Fri Jan 31 2014 Josh Boyer <jwboyer@fedoraproject.org> - 20140131-35.gitd7f8a7c8
- Update to new snapshot
- Updates for Intel 3160/7260, radeon HAWAII GPUs, and some rtlwifi chips
- Fixes bugs 815579 1046935

* Tue Oct 01 2013 Kyle McMartin <kyle@fedoraproject.org> - 20131001-32.gitb8ac7c7e
- Update to a new git snapshot, drop radeon patches.

* Mon Sep 16 2013 Josh Boyer <jwboyer@fedoraproject.org> - 20130724-31.git31f6b30
- Obsolete ql2x00-firmware packages again (rhbz 864959)

* Sat Jul 27 2013 Josh Boyer <jwboyer@redhat.com> - 20130724-30.git31f6b30
- Add AMD ucode back in now that microcode_ctl doesn't provide it

* Fri Jul 26 2013 Dave Airlie <airlied@redhat.com> 20130724-29.git31f6b30
- add radeon firmware which are lost on the way upstream (#988268)

* Thu Jul 25 2013 Josh Boyer <jwboyer@redhat.com> - 20130724-28.git31f6b30
- Temporarily remove AMD microcode (rhbz 988263)
- Remove Creative CA0132 HD-audio files as they're in alsa-firmware

* Wed Jul 24 2013 Josh Boyer <jwboyer@redhat.com> - 20130724-27.git31f6b30
- Update to latest upstream
- New rtl, iwl, and amd firmware

* Fri Jun 07 2013 Josh Boyer <jwboyer@redhat.com> - 20130607-26.git2892af0
- Update to latest upstream release
- New radeon, bluetooth, rtl, and wl1xxx firmware

* Mon May 20 2013 Kyle McMartin <kyle@redhat.com> - 20130418-25.gitb584174
- Use a common version number for both the iwl*-firmware packages and
  linux-firmware itself.
- Don't reference old kernel-firmware package in %%description

* Mon May 20 2013 Kyle McMartin <kyle@redhat.com> - 20130418-0.3.gitb584174
- Bump iwl* version numbers as well...

* Mon May 20 2013 Kyle McMartin <kyle@redhat.com> - 20130418-0.2.gitb584174
- UsrMove: move firmware to /usr/lib/firmware
- Remove duplicate /usr/lib/firmware/updates entry (already in linux-firmware.dirs)
- Simplify sed by using '!' instead of '/' as regexp delimiter
- Fix date error (commited on Mon Feb 04, so change that entry)

* Thu Apr 18 2013 Josh Boyer <jwboyer@redhat.com> - 20130418-0.1.gitb584174
- Update to latest upstream git tree

* Tue Mar 19 2013 Josh Boyer <jwboyer@redhat.com>
- Own the firmware directories (rhbz 919249)

* Thu Feb 21 2013 Josh Boyer <jwboyer@redhat.com> - 20130201-0.4.git65a5163
- Obsolete netxen-firmware.  Again.  (rhbz 913680)

* Mon Feb 04 2013 Josh Boyer <jwboyer@redhat.com> - 20130201-0.3.git65a5163
- Obsolete ql2[45]00-firmware packages (rhbz 906898)
 
* Fri Feb 01 2013 Josh Boyer <jwboyer@redhat.com> 
- Update to latest upstream release
- Provide firmware for carl9170 (rhbz 866051)

* Wed Jan 23 2013 Ville Skyttä <ville.skytta@iki.fi> - 20121218-0.2.gitbda53ca
- Own subdirs created in /lib/firmware (rhbz 902005)

* Wed Jan 23 2013 Josh Boyer <jwboyer@redhat.com>
- Correctly obsolete the libertas-usb8388-firmware packages (rhbz 902265)

* Tue Dec 18 2012 Josh Boyer <jwboyer@redhat.com>
- Update to latest upstream.  Adds brcm firmware updates

* Wed Oct 10 2012 Josh Boyer <jwboyer@redhat.com>
- Consolidate rt61pci-firmware and rt73usb-firmware packages (rhbz 864959)
- Consolidate netxen-firmware and ql2[123]xx-firmware packages (rhbz 864959)

* Tue Sep 25 2012 Josh Boyer <jwboyer@redhat.com>
- Update to latest upstream.  Adds marvell wifi updates (rhbz 858388)

* Tue Sep 18 2012 Josh Boyer <jwboyer@redhat.com>
- Add patch to create libertas subpackages from Daniel Drake (rhbz 853198)

* Fri Sep 07 2012 Josh Boyer <jwboyer@redhat.com> 20120720-0.2.git7560108
- Add epoch to iwl1000 subpackage to preserve upgrade patch (rhbz 855426)

* Fri Jul 20 2012 Josh Boyer <jwboyer@redhat.com> 20120720-0.1.git7560108
- Update to latest upstream.  Adds more realtek firmware and bcm4334

* Tue Jul 17 2012 Josh Boyer <jwboyer@redhat.com> 20120717-0.1.gitf1f86bb
- Update to latest upstream.  Adds updated realtek firmware

* Thu Jun 07 2012 Josh Boyer <jwboyer@redhat.com> 20120510-0.5.git375e954
- Bump release to get around koji

* Thu Jun 07 2012 Josh Boyer <jwboyer@redhat.com> 20120510-0.4.git375e954
- Drop udev requires.  Systemd now provides udev

* Tue Jun 05 2012 Josh Boyer <jwboyer@redhat.com> 20120510-0.3.git375e954
- Fix location of BuildRequires so git is inclued in the buildroot
- Create iwlXXXX-firmware subpackages (rhbz 828050)

* Thu May 10 2012 Josh Boyer <jwboyer@redhat.com> 20120510-0.1.git375e954
- Update to latest upstream.  Adds new bnx2x and radeon firmware

* Wed Apr 18 2012 Josh Boyer <jwboyer@redhat.com> 20120418-0.1.git85fbcaa
- Update to latest upstream.  Adds new rtl and ath firmware

* Wed Mar 21 2012 Dave Airlie <airlied@redhat.com> 20120206-0.3.git06c8f81
- use git to apply the radeon firmware

* Wed Mar 21 2012 Dave Airlie <airlied@redhat.com> 20120206-0.2.git06c8f81
- add radeon southern islands/trinity firmware

* Tue Feb 07 2012 Josh Boyer <jwboyer@redhat.com> 20120206-0.1.git06c8f81
- Update to latest upstream git snapshot.  Fixes rhbz 786937

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20110731-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Aug 04 2011 Tom Callaway <spot@fedoraproject.org> 20110731-2
- resolve conflict with netxen-firmware

* Wed Aug 03 2011 David Woodhouse <dwmw2@infradead.org> 20110731-1
- Latest firmware release with v1.3 ath9k firmware (#727702)

* Sun Jun 05 2011 Peter Lemenkov <lemenkov@gmail.com> 20110601-2
- Remove duplicated licensing files from /lib/firmware

* Wed Jun 01 2011 Dave Airlie <airlied@redhat.com> 20110601-1
- Latest firmware release with AMD llano support.

* Thu Mar 10 2011 Dave Airlie <airlied@redhat.com> 20110304-1
- update to latest upstream for radeon ni/cayman, drop nouveau fw we don't use it anymore

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20110125-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 25 2011 David Woodhouse <dwmw2@infradead.org> 20110125-1
- Update to linux-firmware-20110125 (new bnx2 firmware)

* Fri Jan 07 2011 Dave Airlie <airlied@redhat.com> 20101221-1
- rebase to upstream release + add new radeon NI firmwares.

* Thu Aug 12 2010 Hicham HAOUARI <hicham.haouari@gmail.com> 20100806-4
- Really obsolete ueagle-atm4-firmware

* Thu Aug 12 2010 Hicham HAOUARI <hicham.haouari@gmail.com> 20100806-3
- Obsolete ueagle-atm4-firmware

* Fri Aug 06 2010 David Woodhouse <dwmw2@infradead.org> 20100806-2
- Remove duplicate radeon firmwares; they're upstream now

* Fri Aug 06 2010 David Woodhouse <dwmw2@infradead.org> 20100806-1
- Update to linux-firmware-20100806 (more legacy firmwares from kernel source)

* Fri Apr 09 2010 Dave Airlie <airlied@redhat.com> 20100106-4
- Add further radeon firmwares

* Wed Feb 10 2010 Dave Airlie <airlied@redhat.com> 20100106-3
- add radeon RLC firmware - submitted upstream to dwmw2 already.

* Tue Feb 09 2010 Ben Skeggs <bskeggs@redhat.com> 20090106-2
- Add firmware needed for nouveau to operate correctly (this is Fedora
  only - do not upstream yet - we just moved it here from Fedora kernel)

* Wed Jan 06 2010 David Woodhouse <David.Woodhouse@intel.com> 20090106-1
- Update

* Fri Aug 21 2009 David Woodhouse <David.Woodhouse@intel.com> 20090821-1
- Update, fix typos, remove some files which conflict with other packages.

* Thu Mar 19 2009 David Woodhouse <David.Woodhouse@intel.com> 20090319-1
- First standalone kernel-firmware package.
