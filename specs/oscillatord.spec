Name:           oscillatord
Version:        3.10.5
Release:        %autorelease
Summary:        Daemon for disciplining an oscillator

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
ExcludeArch:    %{ix86}
URL:            https://github.com/leoleovich/oscillatord
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  gpsd-devel
BuildRequires:  json-c-devel
BuildRequires:  liboscillator-disciplining-devel >= %{version}
BuildRequires:  pps-tools-devel
BuildRequires:  sed
BuildRequires:  systemd
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  ubloxcfg-devel >= 1.16-1.20260223git499048b

Requires: liboscillator-disciplining = %{version}
Requires: ubloxcfg >= 1.16-1.20260223git499048b

%description
The oscillatord daemon takes input from a PHC clock, reporting once per second,
the phase error between an oscillator and a reference GNSS receiver. For an
example of such a device, please see the ptp_ocp kernel driver.

The phase error read is then used as an input to the disciplining-minipod
library which will compute a setpoint, used by oscillatord to control an
oscillator and discipline it to the 1PPS from a GNSS receiver. Oscillatord also
sets PHC'stime at start up, using Output from a GNSS receiver.

To communicate with GNSS receiver's serial it uses ubloxcfg

%prep
%autosetup
# Drop hardcoded CFLAGS
sed -e 's/-O0//g' -i CMakeLists.txt

%build
%cmake -DBUILD_UTILS=1
%cmake_build

%install
%cmake_install

%post
%systemd_post oscillatord.service

%preun
%systemd_preun oscillatord.service

%postun
%systemd_postun_with_restart oscillatord.service

%files
%license LICENSE
%doc README.md example_configurations
%{_bindir}/*
%{_unitdir}/%{name}.service
%exclude %{_unitdir}/%{name}@.service

%changelog
* Fri Nov 13 2026 Oleg Obleukhov <leoleovich@fedoraproject.org> - 3.10.5-1
- Update to 3.10.5

* Mon Sep 07 2026 leoleovich <leoleovich@meta.com> - 3.10.4-2
- [oscillatord] exclude default config from rpm

* Fri Sep 04 2026 Oleg Obleukhov <leoleovich@fedoraproject.org> - 3.10.4-1
- Update to 3.10.4

* Fri Aug 14 2026 Oleg Obleukhov <leoleovich@fedoraproject.org> - 3.10.3-1
- Update to 3.10.3

* Fri Aug 14 2026 Oleg Obleukhov <leoleovich@fedoraproject.org> - 3.10.1-1
- Update to 3.10.1

* Fri Aug 14 2026 Oleg Obleukhov <leoleovich@fedoraproject.org> - 3.10.0-3
- New repository

* Thu Jul 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Tue Jun 23 2026 Oleg Obleukhov <leoleovich@fedoraproject.org> - 3.10.0-1
- Update to 3.10.0

* Wed Jun 03 2026 Oleg Obleukhov <leoleovich@fedoraproject.org> - 3.9.3-1
- Update to 3.9.3

* Thu May 21 2026 Yixin Wei <esoapw@fedoraproject.org> - 3.9.2-1
- Update to 3.9.2

* Fri May 15 2026 Yixin Wei <esoapw@fedoraproject.org> - 3.9.1-2
- Exclude i686: ubloxcfg-1.16 has no i686 binaries (per ubloxcfg 4fa4187)

* Tue May 05 2026 Yixin Wei <esoapw@fedoraproject.org> - 3.9.1-1
- Update to 3.9.1; drop pkg-config sed (handled upstream)

* Fri Apr 17 2026 Yixin Wei <esoapw@fedoraproject.org> - 3.9.0-4
- Fix pkg-config name: ubloxcfg 1.16 renamed libubloxcfg.pc to ubloxcfg.pc

* Thu Apr 16 2026 Yixin Wei <esoapw@fedoraproject.org> - 3.9.0-3
- Remove systemd service sed fix, now handled by CMake upstream (99d9c6a)

* Wed Apr 15 2026 Yixin Wei <esoapw@fedoraproject.org> - 3.9.0-2
- Update sources for 3.9.0

* Wed Apr 15 2026 Yixin Wei <esoapw@fedoraproject.org> - 3.9.0-1
- Update to 3.9.0, require ubloxcfg >= 1.16

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Wed Aug 20 2025 Patrick Cullen <cullenptrck@gmail.com> - 3.8.4-2
- Update to 3.8.4

* Wed Aug 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.4-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Apr 01 2025 Vadim Fedorenko <vadfed@fb.com> - 3.8.3-1
- Update to 3.8.3

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Aug 22 2024 Yaroslav Kolomiiets <yarek@fedoraproject.org> - 3.8.2-1
- Update to 3.8.2

* Wed Aug 21 2024 Yaroslav Kolomiiets <yarek@fedoraproject.org> - 3.8.1-1
- Update to 3.8.1

* Tue Aug 06 2024 Vadim Fedorenko <vadfed@fb.com> - 3.8.0-1
- Update to 3.8.0

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 3.7.0-3
- convert GPLv2+ license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Apr 08 2024 Patrick Cullen <cullenptrck@gmail.com> - 3.7.0-1
- Update to 3.7.0

* Tue Feb 13 2024 Patrick Cullen <cullenptrck@gmail.com> - 3.6.3-1
- Update to 3.6.3

* Fri Feb 02 2024 Patrick Cullen <cullenptrck@gmail.com> - 3.6.2-1
- Update to 3.6.2

* Wed Jan 31 2024 Patrick Cullen <cullenptrck@gmail.com> - 3.6.1-1
- Update to 3.6.1

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 15 2023 Patrick Cullen <cullenptrck@gmail.com> - 3.6.0-1
- Update to 3.6.0

* Wed Oct 11 2023 Patrick Cullen <cullenptrck@gmail.com> - 3.5.6-1
- Update to 3.5.6

* Tue Sep 26 2023 Oleg Obleukhov <leoleovich@fedoraproject.org> - 3.5.4-1
- Update to 3.5.4

* Tue Sep 05 2023 Oleg Obleukhov <leoleovich@fedoraproject.org> - 3.5.3-1
- Update to 3.5.3

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Mar 28 2023 Oleg Obleukhov <leoleovich@fedoraproject.org> - 3.5.1-1
- Update to 3.5.1

* Tue Feb 21 2023 Oleg Obleukhov <leoleovich@fedoraproject.org> - 3.5.0-1
- Update to 3.5.0

* Tue Feb 14 2023 Oleg Obleukhov <leoleovich@fedoraproject.org> - 3.4.5-1
- Update to 3.4.5

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 11 2023 Alexander Bulimov <abulimov@fedoraproject.org> - 3.4.3-1
- Update to 3.4.3

* Tue Jan 03 2023 Alexander Bulimov <abulimov@fedoraproject.org> - 3.4.2-3
- Drop C99 patch that was merged upstream

* Tue Jan 03 2023 Oleg Obleukhov <leoleovich@gmail.com> - 3.4.2-2
- RPMAUTOSPEC: unresolvable merge
