Name:            libnxt
%global forgeurl https://github.com/schodet/%{name}
%global tag      0.4.2
Version:         %{tag}

%forgemeta

Release:         8%{?dist}
Summary:         Utility for flashing LEGO Mindstorms NXT firmware
License:         GPL-2.0-or-later
Url:             %{forgeurl}
Source0:         %{forgesource}
# Short document describing how to reflash the NXT firmware
Source1:         file://%{name}-NXT-REFLASH-HOWTO

BuildRequires:   gcc
BuildRequires:   /usr/bin/git
BuildRequires:   python3
BuildRequires:   libusb1-devel
BuildRequires:   meson
BuildRequires:   scdoc
BuildRequires:   arm-none-eabi-gcc-cs

%if 0%{?fedora} > 39
# As per https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
# This is needed because arm-none-eabi-gcc-cs does the same thing.
ExcludeArch:    %{ix86}
%endif


%description
LibNXT is an utility library for talking to the LEGO Mindstorms NXT.
 It currently does:
 * Handling USB communication and locating the NXT in the USB tree.
 * Interaction with the Atmel AT91SAM boot assistant.
 * Flashing of a firmware image to the NXT.
 * Execution of code directly in RAM.


%prep
%forgeautosetup -S git
cp -p %{SOURCE1} NXT-REFLASH-HOWTO


%build
%meson
%meson_build


%install
%meson_install


%files
%license COPYING
%doc README NXT-REFLASH-HOWTO
%{_bindir}/fwexec
%{_bindir}/fwflash
%{_mandir}/man1/fwexec.1*
%{_mandir}/man1/fwflash.1*

%changelog
* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Oct 07 2024 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.4.2-7
- Rebuilt for updated license tag

* Mon Jul 29 2024 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.4.2-6
- ExcludeArch ix86 (fixes FTBFS, rhbz#2300908)

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jul 25 2022 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.42-1
- Fix FTBFS in F37
- Update to the latest available version
- Switch to use the new upstream

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 01 2019 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.3-22
- Fix FTBFS rhbz#1736034

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.3-19
- Fix FTBFS RH BZ #1604623
- Switch from using python2 to python3
- Modernize spec file

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.3-17
- Add missing BR (gcc)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 05 2013 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.3-8
- switch to use arm-none-eabi-gcc-cs toolkit, fixes rhbz#992103,
- add patch to detach kernel driver,
- specfile cleanup.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Sep 13 2010 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.3-2
- Fix for respecting CFLAGS and LDFLAGS during the build,
- Fix for strict-aliasing rules problem,
- Describe purpose of the patches,
- Firmware reflash HOWTO added.

* Mon Jul 19 2010 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.3-1
- Initial RPM release
