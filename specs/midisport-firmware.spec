Name:		midisport-firmware
Version:	1.2
Release:	36%{dist}
Summary:	Firmware for the M-Audio/Midiman USB MIDI and Audio devices
License:	LicenseRef-Fedora-Firmware
URL:		http://usb-midi-fw.sourceforge.net/
Source0:	http://downloads.sourceforge.net/usb-midi-fw/midisport-firmware-%{version}.tar.gz
Patch0:		midisport-firmware-1.2-udev-attrs.patch
BuildArch:	noarch
Requires:	fxload
BuildRequires:	systemd

%description
This package contains the firmware for M-Audio/Midiman USB MIDI & Audio devices.

Supported devices:
 - MidiSport 1x1
 - MidiSport 2x2
 - MidiSport 4x4
 - MidiSport 8x8
 - MidiSport Uno
 - Keystation
 - Oxygen
 - Radium

(You do not need a firmware download for the USB Audio Quattro, Duo, or
MidiSport 2x4.)


%prep
%autosetup -p1

%build
sed -i -e 's|@fxload@|/sbin/fxload|g' -e 's|@firmwaredir@|/lib/firmware|g' 42-midisport-firmware.rules.in

%install
mkdir -p $RPM_BUILD_ROOT/lib/firmware
install -pm 0644 *.ihx $RPM_BUILD_ROOT/lib/firmware

mkdir -p $RPM_BUILD_ROOT%{_udevrulesdir}
install -pm 0644 42-midisport-firmware.rules.in $RPM_BUILD_ROOT/%{_udevrulesdir}/42-midisport-firmware.rules

%files
%doc LICENSE README Changelog
/lib/firmware/MidiSport1x1.ihx
/lib/firmware/MidiSport2x2.ihx
/lib/firmware/MidiSport4x4.ihx
/lib/firmware/MidiSportKS.ihx
/lib/firmware/MidiSportLoader.ihx
/lib/firmware/MidiSport8x8-2.10.ihx
/lib/firmware/MidiSport8x8-2.21.ihx
%config %{_udevrulesdir}/42-midisport-firmware.rules

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Apr 22 2024 Charles R. Anderson <cra@alum.wpi.edu> - 1.2-34
- Convert License tag to SPDX format
- Use autosetup

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 18 2018 Charles R. Anderson <cra@wpi.edu> - 1.2-20
- Remove Group: and rm -rf buildroot from install section

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 31 2015 Charles R. Anderson <cra@wpi.edu> - 1.2-14
- move udev rules to /usr/lib/udev/rules.d (rhbz#1226696)
- remove Buildroot tag
- avoid single quote in description which messes up emacs syntax
  highlighting

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 13 2011 Charles R. Anderson <cra@wpi.edu> - 1.2-8
- Use ATTRS idVendor/idProduct/bcdDevice to match devices in udev rules (#718904)
- Expand package description

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 06 2010 Dave Jones <davej@redhat.com>
- Fix the Source: line to point to sourceforges new download server/path.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 29 2009 Dave Jones <davej@redhat.com> [1.2-4.fc11]
- Fix up path for firmware files in udev rules. (#478911)
  (diff from Patrik Elmberg)

* Thu Aug 14 2008 Dave Jones <davej@redhat.com>
- Use udev rules from upstream package instead of our own.

* Thu Aug 14 2008 Dave Jones <davej@redhat.com>
- License clarification.

* Thu Feb 28 2008 Dave Jones <davej@redhat.com> - 1.2-1
- Initial import.
