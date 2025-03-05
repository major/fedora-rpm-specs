%global debug_package %{nil}

# Tarfile created using git 		
# git clone https://github.com/raspberrypi/firmware.git
# cd firmware/boot
# tar cJvf ../bcm283x-firmware-%{gitshort}.tar.xz *bin *dat *elf bcm2709*dtb bcm271*dtb LICENCE.broadcom COPYING.linux overlays/
%define gitshort 4cb13e0

Name:          bcm283x-firmware
Version:       20250224
Release:       1.%{gitshort}%{?dist}
Summary:       Firmware for the Broadcom bcm283x/bcm271x used in the Raspberry Pi
# see LICENSE.broadcom
# DT Overlays covered under Linux Kernel GPLv2
SourceLicense: GPL-2.0-only WITH Linux-syscall-note AND LicenseRef-Fedora-Firmware
License:       LicenseRef-Fedora-Firmware
URL:           https://github.com/raspberrypi/

ExclusiveArch: aarch64

BuildRequires: efi-filesystem
BuildRequires: efi-srpm-macros
Requires:      efi-filesystem
Requires:      bcm283x-overlays
Requires:      bcm2835-firmware
Requires:      bcm2711-firmware

Source0:       %{name}-%{gitshort}.tar.xz
Source1:       config.txt

# This reverts a FW DT commit that doesn't have the corresponding change in the upstream kernel
# https://github.com/raspberrypi/linux/commit/0491a0aecb999b1a013ad4a6ad3816c535ac6e73
Source10:      bcm2711-rpi-400.dtb
Source11:      bcm2711-rpi-4-b.dtb
Source12:      bcm2711-rpi-cm4.dtb
Source13:      bcm2711-rpi-cm4-io.dtb
Source14:      bcm2711-rpi-cm4s.dtb

%description
Firmware for the Broadcom bcm283x and bcm2711 series of systems on a chip as
shipped in the Raspberry Pi series of devices.

%package     -n bcm283x-overlays
Summary:     HAT Overlays for the Raspberry Pi
License:     GPL-2.0-only WITH Linux-syscall-note

%description -n bcm283x-overlays
Hardware Attached Ontop (HATs) overlays for the Raspberry Pi series of devices.

%package     -n bcm2835-firmware
Summary:     Firmware for the Raspberry Pi 2, 3, 3+ and CM3
Requires:    bcm283x-firmware
Requires:    bcm283x-overlays

%description -n bcm2835-firmware
Firmware for the Raspberry Pi 3 series (3, 3+ and CM3) and Zero2W

%package     -n bcm2711-firmware
Summary:     Firmware for the Raspberry Pi 4 and CM4
Requires:    bcm283x-firmware
Requires:    bcm283x-overlays

%description -n bcm2711-firmware
Firmware for the Raspberry Pi 4 and CM4


%prep
%setup -q -n %{name}-%{gitshort} -c %{name}-%{gitshort}

%build

%install
mkdir -p %{buildroot}%{efi_esp_root}/overlays
install -p %{SOURCE1} %{buildroot}%{efi_esp_root}/config.txt
install -p *bin %{buildroot}%{efi_esp_root}
install -p *dat %{buildroot}%{efi_esp_root}
install -p *elf %{buildroot}%{efi_esp_root}
install -p bcm2710*dtb %{buildroot}%{efi_esp_root}
# Rebuilding due to non upstream DMA40 problems with sound
# install -p bcm2711*dtb %{buildroot}%{efi_esp_root}
install -p bcm2712*dtb %{buildroot}%{efi_esp_root}
install -p overlays/README %{buildroot}%{efi_esp_root}/overlays
install -p overlays/*.dtbo %{buildroot}%{efi_esp_root}/overlays

install -p %{SOURCE10} %{SOURCE11} %{SOURCE12} %{SOURCE13} %{SOURCE14} %{buildroot}%{efi_esp_root}

%files
# DT Overlays covered under Linux Kernel GPLv2
%license LICENCE.broadcom COPYING.linux
%config(noreplace) %{efi_esp_root}/config.txt
%{efi_esp_root}/bootcode.bin

%files -n bcm283x-overlays
%{efi_esp_root}/overlays

%files -n bcm2835-firmware
%{efi_esp_root}/bcm2710*
%{efi_esp_root}/fixup*
%{efi_esp_root}/start*
%exclude %{efi_esp_root}/fixup4*
%exclude %{efi_esp_root}/start4*

%files -n bcm2711-firmware
%{efi_esp_root}/bcm2711*
%{efi_esp_root}/bcm2712*
%{efi_esp_root}/fixup4*
%{efi_esp_root}/start4*

%changelog
* Mon Feb 24 2025 Peter Robinson <pbrobinson@fedoraproject.org> - 20250224-1.4cb13e0
- Update for 6.12 DT overlays

* Tue Feb 18 2025 Peter Robinson <pbrobinson@fedoraproject.org> - 20250217-1.9995946
- Update to latest firmware

* Mon Nov 18 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 20241118-1.545e5aa
- Update to latest firmware

* Fri Sep 13 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 20240913-1.48cd9f9
- Update to latest firmware

* Tue Aug 27 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 20240823-1.6c7d171
- Update to latest firmware

* Tue Jul 23 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 20240723-1.8d5579c
- Update to latest firmware
- Minor config.txt tweaks for camera examples

* Sun May 26 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 20240524-1.458df3a
- Update to latest firmware

* Tue Mar 19 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 20240229-3.dc94391
- Update RPi400 to upstream fix

* Mon Mar 18 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 20240229-2.dc94391
- Update RPi400 firmware DTB
- Reorder config.txt to be closer to upstream

* Thu Feb 15 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 20240229-1.dc94391
- Update to latest firmware
- Rebuild RPi4 FW DT to fix dma40 sound/display issue

* Thu Feb 15 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 20240214-2.f01fa5f
- Update to latest firmware

* Thu Feb 15 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 20240214-1.b208f8c
- Update to latest firmware

* Sat Nov 25 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 20231123-1.93d3f79
- Update to latest firmware
- Updates to config.txt

* Fri Oct 20 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 20231017-1.ce3a0b4
- Update to latest firmware
- Updates for config.txt and minor fixes

* Mon Sep 25 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 20230921-1.6b37a45
- Update to latest firmware

* Tue Aug 22 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 20230810-1.74ad049
- Update to latest firmware

* Fri Jul 28 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 20230728-1.e03ae3c
- Update to latest firmware

* Tue Mar 14 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 20230308-2.379d5bf
- Update config.txt for single U-Boot binary

* Sat Jan 28 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 20230308-1.379d5bf
- Update to latest firmware
- Drop armhfp pieces

* Sat Jan 28 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 20230118-1.2578acb
- Update to latest firmware

* Mon Aug 29 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 20220826-1.ecc243c
- Update to latest firmware

* Tue Aug 09 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 20220809-1.915a708
- Update to latest firmware

* Mon Jul 18 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 20220718-1.c818048
- Update to latest firmware

* Sat Jun 11 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 20220527-2.f145afc
- Updates for default config.txt

* Fri May 27 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 20220527-1.f145afc
- Update to latest firmware

* Mon Apr 25 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 20220425-1.1210acf
- Update to latest firmware

* Tue Mar 08 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 20220301-1.f47c013
- Update to latest firmware
- Fix issue on armhfp devices (rhbz #2061440)

* Wed Feb  9 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 20220209-1.577aef2
- Update to latest firmware

* Thu Jan 27 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 20220124-1.9c04ed2
- Update to latest firmware

* Wed Jan  5 2022 Peter Robinson <pbrobinson@fedoraproject.org> 20220104-1.fbbde90
- Update to latest firmware
- Fixes for 2837 series devices

* Wed Dec 22 2021 Peter Robinson <pbrobinson@fedoraproject.org> 20211222-1.536baf3
- Update to latest firmware

* Sat Dec 11 2021 Peter Robinson <pbrobinson@fedoraproject.org> 20211207-1.303d001
- Update to latest firmware

* Sun Nov 21 2021 Peter Robinson <pbrobinson@fedoraproject.org> 20211116-1.12bc6e3
- Update to latest firmware
- Update config.txt for Raspberry Pi Zero 2 support

* Sun Nov 14 2021 Peter Robinson <pbrobinson@fedoraproject.org> 20211111-1.2095dee
- Update to latest firmware

* Fri Oct 29 2021 Peter Robinson <pbrobinson@fedoraproject.org> 20211028-1.d8754a9
- Update to latest firmware
- Initial Raspberry Pi Zero 2 support

* Sun Oct  3 2021 Peter Robinson <pbrobinson@fedoraproject.org> 20210930-1.b5257da
- Update to latest firmware

* Tue Sep 21 2021 Peter Robinson <pbrobinson@fedoraproject.org> 20210921-1.f9bc224
- Update to latest firmware

* Fri Aug 20 2021 Peter Robinson <pbrobinson@fedoraproject.org> 20210819-1.25e2b59
- Update to latest firmware

* Fri Jul 16 2021 Peter Robinson <pbrobinson@fedoraproject.org> 20210714-1.7208c3d
- Update to latest firmware
- Support supplying random-seed to kernel for KASLR

* Sun Jul 11 2021 Peter Robinson <pbrobinson@fedoraproject.org> 20210709-0.98835e7
- Update to latest firmware

* Sun May 09 2021 Peter Robinson <pbrobinson@fedoraproject.org> 20210430-1.1a46874
- Update to latest firmware

* Sun Apr 11 2021 Peter Robinson <pbrobinson@fedoraproject.org> 20210407-1.8c7c524
- Update to latest firmware

* Fri Mar 12 2021 Peter Robinson <pbrobinson@fedoraproject.org> 20210310-1.0591568
- Update to latest firmware
- Put back nasty config hack as some usecases are still broken

* Thu Feb 25 2021 Peter Robinson <pbrobinson@fedoraproject.org> 20210225-1.5985247
- Update to latest firmware
- Default updates for config.txt

* Wed Feb 24 2021 Peter Robinson <pbrobinson@fedoraproject.org> 20210224-1.7872272
- Update to latest firmware

* Wed Jan 13 2021 Peter Robinson <pbrobinson@fedoraproject.org> 20210108-1.934252b
- Latest firmware update

* Tue Dec 15 2020 Peter Robinson <pbrobinson@fedoraproject.org> 20201216-1.8a5549c
- Updates to device tree overlays

* Tue Dec  8 2020 Peter Robinson <pbrobinson@fedoraproject.org> 20201208-1.919aee0
- Latest firmware update
- First version with RPi-400 support
- Tweaks for UART/boot issues

* Mon Oct 12 2020 Peter Robinson <pbrobinson@fedoraproject.org> 20201008-2.63b1922
- Enable UART for all devices to work around firmware boot issues

* Sat Oct 10 2020 Peter Robinson <pbrobinson@fedoraproject.org> 20201008-1.63b1922
- Latest firmware update

* Thu Oct 01 2020 Peter Robinson <pbrobinson@fedoraproject.org> 20200928-2.f0eab3a
- Workaround for RPi4-8Gb

* Tue Sep 29 2020 Peter Robinson <pbrobinson@fedoraproject.org> 20200928-1.f0eab3a
- Latest firmware update

* Thu Sep 17 2020 Peter Robinson <pbrobinson@fedoraproject.org> 20200917-1.7b99da7
- Latest firmware update

* Thu Sep 03 2020 Peter Robinson <pbrobinson@fedoraproject.org> 20200903-1.baec4d2
- Latest firmware update
- Adjust firmware packaging

* Mon Apr  6 2020 Peter Robinson <pbrobinson@fedoraproject.org> 20200401-1.c2c6ce8
- Latest firmware update

* Sat Mar 28 2020 Peter Robinson <pbrobinson@fedoraproject.org> 20200328-1.5574077
- Latest firmware update

* Sat Mar  7 2020 Peter Robinson <pbrobinson@fedoraproject.org> 20200306-1.163d84c
- Latest firmware update

* Sun Feb 16 2020 Peter Robinson <pbrobinson@fedoraproject.org> 20200212-1.f4b5869
- Latest firmware update

* Fri Jan 31 2020 Peter Robinson <pbrobinson@fedoraproject.org> 20200130-1.63bdbe0
- Latest firmware update

* Wed Jan 15 2020 Peter Robinson <pbrobinson@fedoraproject.org> 20200114-1.d5b8d8d
- Latest firmware update

* Tue Jan  7 2020 Peter Robinson <pbrobinson@fedoraproject.org> 20200106-1.dc56225
- Latest firmware update

* Sat Dec  7 2019 Peter Robinson <pbrobinson@fedoraproject.org> 20191205-1.9d6be5b
- Latest firmware update

* Tue Nov 19 2019 Peter Robinson <pbrobinson@fedoraproject.org> 20191118-1.68ec481
- Latest firmware update

* Wed Oct  2 2019 Peter Robinson <pbrobinson@fedoraproject.org> 20190930-1.a16470a
- Latest firmware update

* Sat Sep 21 2019 Peter Robinson <pbrobinson@fedoraproject.org> 20190920-1.c3f9eee
- Latest firmware update

* Wed Aug 28 2019 Peter Robinson <pbrobinson@fedoraproject.org> 20190828-1.18bf532
- Latest firmware update

* Sun Aug  4 2019 Peter Robinson <pbrobinson@fedoraproject.org> 20190801-1.3822340
- Latest firmware update

* Sun Jul 21 2019 Peter Robinson <pbrobinson@fedoraproject.org> 20190715-1.cba4be2
- Latest firmware, updates for RPi4, fixes for older RPi devices

* Mon Jun 24 2019 Peter Robinson <pbrobinson@fedoraproject.org> 20190624-1.64b5649
- Initial firmware support for the Raspberry Pi 4

* Sun May 12 2019 Peter Robinson <pbrobinson@fedoraproject.org> 20190403-2.9fd387c
- Updated device tree bits

* Sun Apr 14 2019 Peter Robinson <pbrobinson@fedoraproject.org> 20190403-1.8b12e99
- Latest firmware update

* Sun Mar 17 2019 Peter Robinson <pbrobinson@fedoraproject.org> 20190212-4.83977fe
- Ship missing 2836 Raspberry Pi 2 dtb on F-29

* Wed Mar 13 2019 Peter Robinson <pbrobinson@fedoraproject.org> 20190212-3.83977fe
- Upstream dts for 5.0
- Add Raspberry Pi 2 dtb

* Thu Mar  7 2019 Peter Robinson <pbrobinson@fedoraproject.org> 20190212-2.83977fe
- Use upstream kernel DTBs for F-29
- Minor config updates

* Thu Feb 14 2019 Peter Robinson <pbrobinson@fedoraproject.org> 20190212-1.83977fe
- Latest firmware update
- config.txt updates for HAT/overlay support

* Tue Jan 22 2019 Peter Robinson <pbrobinson@fedoraproject.org> 20190122-1.81cca1a
- Latest firmware update
- Tweak config.txt, add details about gpu_mem for camera

* Wed Jan  9 2019 Peter Robinson <pbrobinson@fedoraproject.org> 20190109-1.9baae76
- Latest firmware update
- Ship Raspbery Pi base DTs

* Wed Dec 19 2018 Peter Robinson <pbrobinson@fedoraproject.org> 20181218-1.1ea8781
- Latest firmware update
- Updates to config.txt, use eXtended firmware by default

* Wed Dec  5 2018 Peter Robinson <pbrobinson@fedoraproject.org> 20181204-1.afd824a
- Latest firmware update

* Sun Nov 18 2018 Peter Robinson <pbrobinson@fedoraproject.org> 20181105-1.55e5912
- Latest firmware update

* Fri Oct 12 2018 Peter Robinson <pbrobinson@fedoraproject.org> 20181009-1.fbad640
- Latest firmware update

* Sun Sep 23 2018 Peter Robinson <pbrobinson@fedoraproject.org> 20180921-1.404dfef
- Latest firmware update

* Mon Sep  3 2018 Peter Robinson <pbrobinson@fedoraproject.org> 20180829-3.ec3f856
- Minor fixup

* Sat Sep  1 2018 Peter Robinson <pbrobinson@fedoraproject.org> 20180829-2.ec3f856
- Tweak migration process

* Fri Aug 31 2018 Peter Robinson <pbrobinson@fedoraproject.org> 20180829-1.ec3f856
- Latest firmware update
- Change locations of firmware
- Migration bits for ARMv7
- Prepare for supporting HATs/overlays using config.txt

* Mon Aug 13 2018 Peter Robinson <pbrobinson@fedoraproject.org> 20180810-1.953a339
- Latest upstream firmware

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20180629-2.93683f1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul  1 2018 Peter Robinson <pbrobinson@fedoraproject.org> 20180629-1.93683f1
- Latest upstream firmware

* Wed Apr 18 2018 Peter Robinson <pbrobinson@fedoraproject.org> 20180525-1.784fe6c
- Latest upstream firmware

* Wed Apr 18 2018 Peter Robinson <pbrobinson@fedoraproject.org> 20180416-1.a154f21
- Firmware fix for some Raspberry Pi 3+ issues

* Thu Apr 12 2018 Peter Robinson <pbrobinson@fedoraproject.org> 20180409-1.d46b40b
- Upstream firmware fixes

* Sun Apr  8 2018 Peter Robinson <pbrobinson@fedoraproject.org> 20180406-1.3aa8060
- Upstream firmware fixes
- Ship DT overlays
- Update config.txt

* Tue Mar 20 2018 Peter Robinson <pbrobinson@fedoraproject.org> 20180316-1.25cf637
- Upstream firmware fixes

* Wed Mar 14 2018 Peter Robinson <pbrobinson@fedoraproject.org> 20180314-1.086a848
- Add support for Raspberry Pi 3+ (Happy Pi day)

* Thu Mar  8 2018 Peter Robinson <pbrobinson@fedoraproject.org> 20180307-1.7fdcd00
- Upstream firmware fixes

* Sun Feb 25 2018 Peter Robinson <pbrobinson@fedoraproject.org> 20180209-1.b1a7f4a
- Latest firmware, updated license text

* Wed Jan  3 2018 Peter Robinson <pbrobinson@fedoraproject.org> 20171201-1.9426e18
- Latest firmware

* Sun Oct 15 2017 Peter Robinson <pbrobinson@fedoraproject.org> 20171011-1.a88e126
- Latest firmware

* Thu Sep 14 2017 Peter Robinson <pbrobinson@fedoraproject.org> 20170912-1.2067241
- Update to 2067241 firmware with various fixes/improvements

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20170703-3.5f54395
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20170703-2.5f54395
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Peter Robinson <pbrobinson@fedoraproject.org>
- Allow OS rather than firmware control CEC

* Mon Jul  3 2017 Peter Robinson <pbrobinson@fedoraproject.org> 20170703-1.5f54395
- Update to 5f54395 firmware (upstream fix for serial baud rate regression)

* Mon Jul  3 2017 Peter Robinson <pbrobinson@fedoraproject.org> 20170613-2.73f44c6
- Move back to firmware 73f44c6 (20170515) to fix regresion on serial console

* Wed Jun 14 2017 Peter Robinson <pbrobinson@fedoraproject.org> 20170613-1.7a661e0
- Latest firmware

* Mon May 15 2017 Peter Robinson <pbrobinson@fedoraproject.org> 20170504-1.284e48a
- Enable DMA driver in initrd
- Latest firmware

* Wed Apr 19 2017 Peter Robinson <pbrobinson@fedoraproject.org> 20170404-2.b038854
- Add config-64.txt for default 64 bit options for the RPi3

* Wed Apr 12 2017 Peter Robinson <pbrobinson@fedoraproject.org> 20170404-1.b038854
- Latest firmware, minor config tweaks

* Sun Mar 26 2017 Peter Robinson <pbrobinson@fedoraproject.org> 20170324-1.76fc4dd
- Drop bcm2835_dma from initrd, it's too unstable
- Latest firmware fixes

* Tue Mar 14 2017 Peter Robinson <pbrobinson@fedoraproject.org> 20170314-2.509beaa
- Add bcm2835_dma to initrd list

* Tue Mar 14 2017 Peter Robinson <pbrobinson@fedoraproject.org> 20170314-1.509beaa
- Latest firmware fixes
- Transition mechanism for MMC changes

* Thu Feb  9 2017 Peter Robinson <pbrobinson@fedoraproject.org> 20170208-1.db5fd5e
- Latest firmware fixes

* Thu Feb  2 2017 Peter Robinson <pbrobinson@fedoraproject.org> 20170131-1.72b44d8
- Latest firmware fixes

* Wed Dec 28 2016 Peter Robinson <pbrobinson@fedoraproject.org> 20161209-1.6d45dcf
- Latest firmware fixes

* Sat Oct 22 2016 Peter Robinson <pbrobinson@fedoraproject.org> 20161020-1.a0e54e7
- Latest firmware fixes
- Minor config tweaks

* Sat Sep 24 2016 Peter Robinson <pbrobinson@fedoraproject.org> 20160913-2.c93fb48
- Minor config tweaks

* Wed Sep 14 2016 Peter Robinson <pbrobinson@fedoraproject.org> 20160913-1.c93fb48
- Numerous config enhancements
- Latest firmware fixes

* Sat Aug 27 2016 Peter Robinson <pbrobinson@fedoraproject.org> 20160823-1.d0bc6ce
- Latest firmware fixes

* Tue Jul 12 2016 Peter Robinson <pbrobinson@fedoraproject.org> 20160712-1.6ab4d20
- Latest firmware fixes

* Mon May 16 2016 Peter Robinson <pbrobinson@fedoraproject.org> 20160513-1.c17fa41
- Config options for HW rev 3
- Latest firmware fixes

* Sat Apr 30 2016 Peter Robinson <pbrobinson@fedoraproject.org> 20160430-1.611d798
- Latest firmware update

* Mon Mar  7 2016 Peter Robinson <pbrobinson@fedoraproject.org> 20160307-1.a192a05
- Latest firmware update

* Wed Mar  2 2016 Peter Robinson <pbrobinson@fedoraproject.org> 20160229-1.9cd1c6c
- Latest firmware update
- Build for aarch64

* Mon Feb  8 2016 Peter Robinson <pbrobinson@fedoraproject.org> 20160201-1.cb2ffaa
- Latest firmware update

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20151219-2.1efc1ec
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 21 2015 Peter Robinson <pbrobinson@fedoraproject.org> 20151219-1.1efc1ec
- Latest firmware update

* Mon Oct  5 2015 Peter Robinson <pbrobinson@fedoraproject.org> 20151004-1.b06b317
- Latest firmware update

* Fri Aug 28 2015 Peter Robinson <pbrobinson@fedoraproject.org> 20150824-1.c6ae1d6
- Latest firmware update

* Fri Jul 24 2015 Peter Robinson <pbrobinson@fedoraproject.org> 20150723-1.43c4847
- Latest firmware update

* Tue Jun 30 2015 Peter Robinson <pbrobinson@fedoraproject.org> 20150630-1.89881b5
- Latest firmware update

* Wed Jun 24 2015 Peter Robinson <pbrobinson@fedoraproject.org> 20150623-1.856e2e1
- Latest firmware update

* Sun Jun 21 2015 Peter Robinson <pbrobinson@fedoraproject.org> 20150619-1.8b9d7b8
- Latest firmware update
- update config.txt for default kernel name

* Fri Jun 19 2015 Peter Robinson <pbrobinson@fedoraproject.org> 20150617-2.fc6c989
- Add cmdline.txt, update config.txt

* Fri Jun 19 2015 Peter Robinson <pbrobinson@fedoraproject.org> 20150617-1.fc6c989
- Latest firmware update
- Add default config.txt

* Thu Jun 18 2015 Peter Robinson <pbrobinson@fedoraproject.org> 20150615-3.37600d5
- Fix license field

* Thu Jun 18 2015 Peter Robinson <pbrobinson@fedoraproject.org> 20150615-2.37600d5
- Updates for review

* Mon Jun 15 2015 Peter Robinson <pbrobinson@fedoraproject.org> 20150615-1.37600d5
- Initial version
