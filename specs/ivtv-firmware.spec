%define version_enc 2.06.039
%define version_dec 2.02.023

Summary: Firmware for the Hauppauge PVR 250/350/150/500/USB2 model series
Name: ivtv-firmware
Version: 20080701
Release: 49%{?dist}
Epoch: 2
License: Redistributable, no modification permitted
URL: http://dl.ivtvdriver.org/ivtv/firmware/
Source0: http://dl.ivtvdriver.org/ivtv/firmware/%{name}-%{version}.tar.gz
BuildArch: noarch
Obsoletes: ivtv-firmware-audio <= 0.0.1
Provides: ivtv-firmware-audio = 0.0.1
Obsoletes: %{name}-dec < %{version_dec}
Provides: %{name}-dec = %{version_dec}
Obsoletes: %{name}-enc < %{version_enc}
Provides: %{name}-enc = %{version_enc}

%description
This package contains the firmware for WinTV Hauppauge PVR
250/350/150/500/USB2 cards.

%prep
%setup -q -c

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/lib/firmware

# Remove the file shipped in linux-firmare
rm -f v4l-cx25840.fw

install -p *.fw %{buildroot}/lib/firmware/
install -p v4l-cx2341x-init.mpg %{buildroot}/lib/firmware/v4l-cx2341x-init.mpg
# license requires that the licenses go in the same place as the firmware
for f in license-*.txt
do
  install -p $f %{buildroot}/lib/firmware/%{name}-$f
done

%files
%doc license-*.txt
/lib/firmware/*.fw
/lib/firmware/v4l-cx2341x-init.mpg
/lib/firmware/%{name}-license-*.txt

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2:20080701-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:20080701-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:20080701-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:20080701-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2:20080701-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2:20080701-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2:20080701-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2:20080701-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2:20080701-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2:20080701-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2:20080701-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2:20080701-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2:20080701-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2:20080701-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2:20080701-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2:20080701-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 25 2017 Matthew Miller <mtatdm@fedoraproject.org> - 2:20080701-33
- add dist tag as per guidelines https://fedoraproject.org/wiki/Packaging:DistTag

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2:20080701-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2:20080701-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2:20080701-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jun 29 2015 Josh Boyer <jwboyer@fedoraproject.org> - 2:20080701-29
- Rebuild (again)

* Tue Jun 23 2015 Josh Boyer <jwboyer@fedoraproject.org> - 2:20080701-28
- Rebuild without the file shipped in linux-firmware (rhbz 1232773)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:20080701-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:20080701-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:20080701-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:20080701-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:20080701-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:20080701-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:20080701-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:20080701-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Aug 24 2008 Axel Thimm <Axel.Thimm@ATrpms.net> - 2:20080701-18
- Update to 20080701.

* Wed Mar  5 2008 Axel Thimm <Axel.Thimm@ATrpms.net> - 2:20070217-17
- Many fixes by Jarod Wilson.
- Rip out legacy support.

* Sat Feb  2 2008 Axel Thimm <Axel.Thimm@ATrpms.net> - 2:20070217-16
- Place licenses next to firmware images.

* Sat Dec 22 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 2:20070217-15.1
- Own directories from legacy paths.

* Wed Oct 24 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 2:20070217-15
- Add v4l-cx2341x-init.mpg as a pseudo-firmware.

* Wed Feb 28 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 2:20070217-13
- Modify versioning to follow date.

* Mon May 29 2006 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update firmwares to recommended versions.
- Merge in audio firmware.

* Tue Jan  4 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Initial build for audio firmware.

* Thu Oct 28 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update firmware to 1.8a.
- split package into enc/dec firmwares.
- version acording to origin, note that the two firmwares have
  different versions, so none is really suitable for the main package.

* Wed Mar  3 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Change versioning (previous was based on Windows driver).
- need to bump epoch for that :(

* Sat Feb 28 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.8 (22035).

* Mon Dec 29 2003 Axel Thimm <Axel.Thimm@ATrpms.net>
- Initial build.


