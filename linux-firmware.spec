%global debug_package %{nil}

%global _firmwarepath	/usr/lib/firmware
%define _binaries_in_noarch_packages_terminate_build 0

Name:		linux-firmware
Version:	20230919
Release:	2%{?dist}
Summary:	Firmware files used by the Linux kernel
License:	GPL+ and GPLv2+ and MIT and Redistributable, no modification permitted
URL:		http://www.kernel.org/
BuildArch:	noarch

Source0:	https://www.kernel.org/pub/linux/kernel/firmware/%{name}-%{version}.tar.xz

BuildRequires:	make
BuildRequires:	git-core

Requires:	linux-firmware-whence
Provides:	kernel-firmware = %{version}
Obsoletes:	kernel-firmware < %{version}
Conflicts:	microcode_ctl < 2.1-0

%if 0%{?fedora} && 0%{?fedora} < 39
Requires:	atheros-firmware
Requires:	brcmfmac-firmware
Requires:	mt7xxx-firmware
Requires:	realtek-firmware
%else
Recommends:	amd-gpu-firmware
Recommends:	intel-gpu-firmware
Recommends:	nvidia-gpu-firmware
Recommends:	atheros-firmware
Recommends:	brcmfmac-firmware
Recommends:	mt7xxx-firmware
Recommends:	realtek-firmware
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

%package -n iwlegacy-firmware
Summary:	Firmware for Intel(R) Wireless WiFi Link 3945(A)BG and 4965AGN adapters
License:	Redistributable, no modification permitted
Requires:	linux-firmware-whence
Obsoletes:	iwl3945-firmware < %{version}-%{release}
Obsoletes:	iwl4965-firmware < %{version}-%{release}
Provides:	iwl3945-firmware = %{version}-%{release}
Provides:	iwl4965-firmware = %{version}-%{release}
%description -n iwlegacy-firmware
This package contains the firmware required by the iwlegacy driver
for Linux. This includes the 3945(A)BG and 4965AGN WiFi NICs. Usage
of the firmware is subject to the terms and conditions contained
inside the provided LICENSE file. Please read it carefully.

%package -n iwlwifi-dvm-firmware
Summary:	DVM Firmware for Intel(R) Wireless WiFi adapters
License:	Redistributable, no modification permitted
Requires:	linux-firmware-whence
Obsoletes:	iwl100-firmware < %{version}-%{release}
Obsoletes:	iwl105-firmware < %{version}-%{release}
Obsoletes:	iwl135-firmware < %{version}-%{release}
Obsoletes:	iwl1000-firmware < 1:%{version}-%{release}
Obsoletes:	iwl2000-firmware < %{version}-%{release}
Obsoletes:	iwl2030-firmware < %{version}-%{release}
Obsoletes:	iwl5000-firmware < %{version}-%{release}
Obsoletes:	iwl5150-firmware < %{version}-%{release}
Obsoletes:	iwl6000-firmware < %{version}-%{release}
Obsoletes:	iwl6000g2a-firmware < %{version}-%{release}
Obsoletes:	iwl6000g2b-firmware < %{version}-%{release}
Obsoletes:	iwl6050-firmware < %{version}-%{release}
Provides:	iwl100-firmware = %{version}-%{release}
Provides:	iwl105-firmware = %{version}-%{release}
Provides:	iwl135-firmware = %{version}-%{release}
Provides:	iwl1000-firmware = 1:%{version}-%{release}
Provides:	iwl2000-firmware = %{version}-%{release}
Provides:	iwl2030-firmware = %{version}-%{release}
Provides:	iwl5000-firmware = %{version}-%{release}
Provides:	iwl5150-firmware = %{version}-%{release}
Provides:	iwl6000-firmware = %{version}-%{release}
Provides:	iwl6000g2a-firmware = %{version}-%{release}
Provides:	iwl6000g2b-firmware = %{version}-%{release}
Provides:	iwl6050-firmware = %{version}-%{release}
%description -n iwlwifi-dvm-firmware
This package contains the firmware required by the iwlwifi driver
for Linux built with DVM firmware support (CONFIG_IWLDVM=y/m). Usage of
the firmware is subject to the terms and conditions contained inside the
provided LICENSE file. Please read it carefully.

%package -n iwlwifi-mvm-firmware
Summary:	MVM Firmware for Intel(R) Wireless WiFi adapters
License:	Redistributable, no modification permitted
Requires:	linux-firmware-whence
Obsoletes:	iwl3160-firmware < 1:%{version}-%{release}
Obsoletes:	iwl7260-firmware < 1:%{version}-%{release}
Obsoletes:	iwlax2xx-firmware < %{version}-%{release}
Provides:	iwl3160-firmware = 1:%{version}-%{release}
Provides:	iwl7260-firmware = 1:%{version}-%{release}
Provides:	iwlax2xx-firmware = %{version}-%{release}
%description -n iwlwifi-mvm-firmware
This package contains the firmware required by the iwlwifi driver
for Linux built with MVM firmware support (CONFIG_IWLMVM=y/m).  Usage of
the firmware is subject to the terms and conditions contained inside the
provided LICENSE file. Please read it carefully.

%package -n libertas-firmware
Summary:	Firmware for Marvell Libertas SD/USB WiFi Network Adapters
License:	Redistributable, no modification permitted
Requires:	linux-firmware-whence
Obsoletes:      libertas-sd8686-firmware < %{version}-%{release}
Obsoletes:      libertas-sd8787-firmware < %{version}-%{release}
Obsoletes:      libertas-usb8388-firmware < 2:%{version}-%{release}
Obsoletes:      libertas-usb8388-olpc-firmware < %{version}-%{release}
Provides:       libertas-sd8686-firmware < %{version}-%{release}
Provides:       libertas-sd8787-firmware < %{version}-%{release}
Provides:       libertas-usb8388-firmware < 2:%{version}-%{release}
Provides:       libertas-usb8388-olpc-firmware < %{version}-%{release}
%description -n libertas-firmware
Firmware for the Marvell Libertas series of WiFi Network Adapters
Including the SD 8686/8787 and USB 8388/8388.

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

%package -n qcom-firmware
Summary:	Firmware for Qualcomm SoCs
License:	Redistributable, no modification permitted
Requires:	linux-firmware-whence
Requires:	atheros-firmware = %{version}-%{release}
%description -n qcom-firmware
Firmware for various compoents in Qualcomm SoCs including Adreno
GPUs, Venus video encode/decode, Audio DSP, Compute DSP, WWAN
modem, Sensor DSPs.

# Random other hardware
%package -n dvb-firmware
Summary:	Firmware for various DVB broadcast receivers
License:	Redistributable, no modification permitted
Requires:	linux-firmware-whence
%description -n dvb-firmware
Firmware for various DVB broadcast receivers. These include the
Siano DTV devices, devices based on Conexant chipsets (cx18,
cx23885, cx23840, cx231xx), Xceive xc4000/xc5000, DiBcom dib0700,
Terratec H5 DRX-K, ITEtech IT9135 Ax and Bx, and av7110.

%prep
%autosetup -S git -p1

%build

%install
mkdir -p %{buildroot}/%{_firmwarepath}
mkdir -p %{buildroot}/%{_firmwarepath}/updates

%if 0%{?fedora} >= 34 || 0%{?rhel} >= 9
make DESTDIR=%{buildroot}/ FIRMWAREDIR=%{_firmwarepath} install-xz
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
	-i -e '/^av7110/d' \
	-i -e '/^brcm/d' \
	-i -e '/^cmmb/d' \
	-i -e '/^cypress/d' \
	-i -e '/^dvb/d' \
	-i -e '/^i915/d' \
	-i -e '/^isdbt/d' \
	-i -e '/^iwlwifi/d' \
	-i -e '/^nvidia\/g/d' \
	-i -e '/^nvidia\/tu/d' \
	-i -e '/^lgs8g75/d' \
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
	-i -e '/^qcom/d' \
	-i -e '/^radeon/d' \
	-i -e '/^rtl_bt/d' \
	-i -e '/^rtlwifi/d' \
	-i -e '/^rtw88/d' \
	-i -e '/^rtw89/d' \
	-i -e '/^sms1xxx/d' \
	-i -e '/^tdmb/d' \
	-i -e '/^v4l-cx2/d' \
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
%dir %{_firmwarepath}/nvidia
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

%files -n iwlegacy-firmware
%license LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-3945-*.ucode*
%{_firmwarepath}/iwlwifi-4965-*.ucode*

%files -n iwlwifi-dvm-firmware
%license LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-100-*.ucode*
%{_firmwarepath}/iwlwifi-105-*.ucode*
%{_firmwarepath}/iwlwifi-135-*.ucode*
%{_firmwarepath}/iwlwifi-1000-*.ucode*
%{_firmwarepath}/iwlwifi-2000-*.ucode*
%{_firmwarepath}/iwlwifi-2030-*.ucode*
%{_firmwarepath}/iwlwifi-5000-*.ucode*
%{_firmwarepath}/iwlwifi-5150-*.ucode*
%{_firmwarepath}/iwlwifi-6000-*.ucode*
%{_firmwarepath}/iwlwifi-6000g2a-*.ucode*
%{_firmwarepath}/iwlwifi-6000g2b-*.ucode*
%{_firmwarepath}/iwlwifi-6050-*.ucode*

%files -n iwlwifi-mvm-firmware
%license LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-3160-*.ucode*
%{_firmwarepath}/iwlwifi-3168-*.ucode*
%{_firmwarepath}/iwlwifi-7260-*.ucode*
%{_firmwarepath}/iwlwifi-7265-*.ucode*
%{_firmwarepath}/iwlwifi-7265D-*.ucode*
%{_firmwarepath}/iwlwifi-8000C-*.ucode*
%{_firmwarepath}/iwlwifi-8265-*.ucode*
%{_firmwarepath}/iwlwifi-9000-*.ucode*
%{_firmwarepath}/iwlwifi-9260-*.ucode*
%{_firmwarepath}/iwlwifi-cc-a0-*.ucode*
%{_firmwarepath}/iwlwifi-Qu*.ucode*
%{_firmwarepath}/iwlwifi-ty-a0*
%{_firmwarepath}/iwlwifi-so-a0*

%files -n libertas-firmware
%license LICENCE.Marvell
%dir %{_firmwarepath}/libertas
%dir %{_firmwarepath}/mrvl
%{_firmwarepath}/libertas/sd8686*
%{_firmwarepath}/libertas/usb8388_olpc.bin*
%{_firmwarepath}/libertas/usb8388_v9.bin*
%{_firmwarepath}/mrvl/sd8787*

%files -n mt7xxx-firmware
%license LICENCE.mediatek
%license LICENCE.ralink_a_mediatek_company_firmware
%dir %{_firmwarepath}/mediatek
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

# Silicon Vendor specific
%files -n qcom-firmware
%license LICENSE.qcom LICENSE.qcom_yamato qcom/NOTICE.txt
%dir %{_firmwarepath}/qcom
%{_firmwarepath}/qcom/*

# Random other hardware
%files -n dvb-firmware
%license LICENSE.dib0700 LICENCE.it913x LICENCE.siano
%license LICENCE.xc4000 LICENCE.xc5000 LICENCE.xc5000c
%dir %{_firmwarepath}/av7110/
%{_firmwarepath}/av7110/*
%{_firmwarepath}/cmmb*
%{_firmwarepath}/dvb*
%{_firmwarepath}/isdbt*
%{_firmwarepath}/lgs8g75*
%{_firmwarepath}/sms1xxx*
%{_firmwarepath}/tdmb*
%{_firmwarepath}/v4l-cx2*

%changelog
* Mon Oct 02 2023 Neal Gompa <ngompa@fedoraproject.org> - 20230919-2
- Flip conditional to make weak-installing firmware the default

* Tue Sep 19 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 20230919-1
- Update to upstream 20230919 release
- amd-ucode: Add note on fam19h warnings
- i915: update MTL HuC to version 8.5.4
- amdgpu: update DMCUB to 0.0.183.0 for various AMDGPU ASICs
- qcom: add link to sc8280xp audioreach firmware
- qcom: sm8250: add RB5 sensors DSP firmware
- qcom: Update vpu-1.0 firmware
- qcom: sm8250: update DSP firmware
- qcom: add firmware for the onboard WiFi on qcm2290 / qrb4210
- qcom: add venus firmware files for v6.0
- qcom: add firmware for QRB4210 platforms
- qcom: add firmware for QCM2290 platforms
- qcom: add GPU firmware for QCM2290 / QRB2210
- ath10k/WCN3990: move wlanmdsp to qcom/sdm845
- QCA: Update Bluetooth WCN685x 2.1 firmware to 2.1.0-00605
- Fix carl9170fw shell scripts for shellcheck errors
- i915: Update MTL DMC to v2.16
- Update firmware file for Intel Bluetooth AX200/AX201/AX203/AX210/AX211
- Update firmware for qat_4xxx devices
- Update AMD SEV firmware
- rtw89: 8852b: update fw to v0.29.29.3
- rtw89: 8851b: update fw to v0.29.41.2
- i915: add GSC 102.0.0.1655 for MTL
- cirrus: Add CS35L41 firmware for HP G11 models
- Update AMD cpu microcode
- rtl_bt: Add firmware v2 file for RTL8852C
- Revert "rtl_bt: Update RTL8852C BT USB firmware to 0x040D_7225"
- cxgb4: Update firmware to revision 1.27.4.0

* Thu Aug 10 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 20230804-153
- Update AMD cpu microcode

* Sun Aug 06 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 20230804-152
- Update to upstream 20230804 release
- Split out QCom Arm IP firmware
- Merge Marvell libertas WiFi firmware
- Mellanox: Add new mlxsw_spectrum firmware xx.2012.1012
- Add URL for latest FW binaries for NXP BT chipsets
- rtw89: 8851b: update firmware to v0.29.41.1
- qcom: sdm845: add RB3 sensors DSP firmware
- amdgpu: Update DMCUB for DCN314 & Yellow Carp
- ice: add LAG-supporting DDP package
- i915: Update MTL DMC to v2.13
- i915: Update ADLP DMC to v2.20
- cirrus: Add CS35L41 firmware for Dell Oasis Models
- copy-firmware: Fix linking directories when using compression
- copy-firmware: Fix test: unexpected operator
- qcom: sc8280xp: LENOVO: remove directory sym link
- qcom: sc8280xp: LENOVO: Remove execute bits
- amdgpu: update VCN 4.0.0 firmware
- amdgpu: add initial SMU 13.0.10 firmware
- amdgpu: add initial SDMA 6.0.3 firmware
- amdgpu: add initial PSP 13.0.10 firmware
- amdgpu: add initial GC 11.0.3 firmware
- Update AMD fam17h cpu microcode
- Update AMD cpu microcode
- amdgpu: update various generation VCN firmware
- amdgpu: update DMCUB to v0.0.175.0 for various AMDGPU ASICs
- Updated NXP SR150 UWB firmware
- wfx: update to firmware 3.16.1
- mediatek: Update mt8195 SCP firmware to support 10bit mode
- i915: update DG2 GuC to v70.8.0
- i915: update to GuC 70.8.0 and HuC 8.5.1 for MTL
- cirrus: Add CS35L41 firmware for ASUS ROG 2023 Models
- Partially revert "amdgpu: DMCUB updates for DCN 3.1.4 and 3.1.5"
- Update firmware for MT7922 WiFi/Bluetooth device
- Update firmware file for Intel Bluetooth AX200/201/203/210/211
- Fix qcom ASoC tglp WHENCE entry
- check_whence: Check link targets are valid
- iwlwifi: add new FWs from core80-39 release
- iwlwifi: update cc/Qu/QuZ firmwares for core80-39 release
- qcom: Add Audio firmware for SC8280XP X13s

* Sun Jul 02 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 20230625-151
- Update to upstream 20230625 release
- Move to upstreamed compression support
- Minor spec cleanups
- wilc1000: update WILC1000 firmware to v16.0
- ice: update ice DDP wireless_edge package to 1.3.10.0
- amdgpu: DMCUB updates for DCN 3.1.4 and 3.1.5
- amdgpu: update DMCUB to v0.0.172.0 for various AMDGPU ASICs
- qcom: Update the microcode files for Adreno a630 GPUs.
- qcom: sdm845: rename the modem firmware
- qcom: sdm845: update remoteproc firmware
- rtl_bt: Update RTL8852A BT USB firmware to 0xDAC7_480D
- rtl_bt: Update RTL8852C BT USB firmware to 0x040D_7225
- update firmware for MT7921/MT7922 WiFi device
- update firmware for mediatek MT7921/MT7922 bluetooth chip (MT7922)
- i915: Add HuC v8.5.0 for MTL
- mediatek: Update mt8195 SCP firmware to support hevc
- qcom: apq8016: add Dragonboard 410c WiFi and modem firmware
- cirrus: Add firmware for new Asus ROG Laptops
- brcm: Add symlinks from Pine64 devices to AW-CM256SM.txt
- amdgpu: Update GC 11.0.1 and 11.0.4
- rtw89: 8851b: add firmware v0.29.41.0
- amdgpu: various firmware updates for amd.5.5 release
- ice: update ice DDP comms package to 1.3.40.0
- rtlwifi: Add firmware v6.0 for RTL8192FU
- rtlwifi: Update firmware for RTL8188EU to v28.0
- cxgb4: Update firmware to revision 1.27.3.0

* Fri May 26 2023 Herton R. Krzesinski <herton@redhat.com>
- Join iwl3945-firmware and iwl4965-firmware into iwlegacy-firmware package.
- Create iwlwifi-dvm-firmware subpackage and fold some subpackages into it.
- Create iwlwifi-mvm-firmware subpackage and fold some subpackages into it.

* Tue May 16 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 20230515-150
- Update to upstream 20230515 release
- Drop ancient iwlwifi versioning and use upstream date format version
- cirrus: Add firmware and tuning files for HP G10 series laptops
- update firmware for mediatek bluetooth chip (MT7922)
- WHENCE: Cleanup Realtek BT firmware provenance
- update firmware for MT7922 WiFi device
- cnm: update chips&media wave521c firmware.
- cirrus: Add firmware and tuning files for Lenovo ThinkPad P1 Gen 6
- i915: Add GuC v70.6.6 for MTL
- amdgpu: update DCN 3.1.6 DMCUB firmware
- rtl_bt: Update RTL8852B BT USB firmware to 0xDBC6_B20F
- rtl_bt: Update RTL8761B BT USB firmware to 0xDFC6_D922
- rtl_bt: Update RTL8761B BT UART firmware to 0x9DC6_D922
- rtl_nic: update firmware of USB devices
- Update firmware file for Intel Bluetooth AX20x/AX21x
- update firmware for MT7981
- qca: Update firmware files for BT chip WCN6750
- mt76xx: Move the old Mediatek WiFi firmware to mediatek
- rtl_bt: Add firmware and config files for RTL8851B
- Update AMD cpu microcode
- add firmware for MT7981
- update firmware for MT7921 WiFi device
- update firmware for mediatek bluetooth chip (MT7921)
- update Intel qat firmware
- Add firmware for Cirrus CS35L41 on Lenovo Laptops
- update firmware for MT7916
- rtw89: 8852b: update format-1 fw to v0.29.29.1
- rtw89: 8852c: update fw to v0.27.56.13
- ath11k: WCN6855 hw2.0: update board-2.bin
- ath11k: WCN6750 hw1.0: update to WLAN.MSL.1.0.1-01160-QCAMSLSWPLZ-1
- ath11k: QCN9074 hw1.0: update to WLAN.HK.2.7.0.1-01744-QCAHKSWPL_SILICONZ-1
- ath11k: IPQ8074 hw2.0: update to WLAN.HK.2.7.0.1-01744-QCAHKSWPL_SILICONZ-1
- ath11k: IPQ8074 hw2.0: update board-2.bin
- ath11k: IPQ6018 hw1.0: update to WLAN.HK.2.7.0.1-01744-QCAHKSWPL_SILICONZ-1
- ath11k: IPQ6018 hw1.0: update board-2.bin
- ath10k: QCA99X0 hw2.0: update board-2.bin
- ath10k: QCA9984 hw1.0: update board-2.bin
- ath10k: QCA9888 hw2.0: update board-2.bin
- ath10k: QCA6174 hw3.0: update board-2.bin
- ath10k: QCA4019 hw1.0: update board-2.bin

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
