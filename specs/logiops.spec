%global forgeurl https://github.com/PixlOne/logiops

Name:    logiops
Version: 0.3.5
Release: 2%{?dist}
Summary: Unofficial driver for Logitech mice and keyboard
%forgemeta

# Automatically converted from old format: GPLv3 - review is highly recommended.
License: GPL-3.0-only
URL:     %{forgeurl}

Source:  %{forgesource}

# Change from static to dynamic lib
Patch0:  logiops-use-ipcgull-shared-lib.patch

Requires:  ipcgull

BuildRequires:  cmake
BuildRequires:  systemd-devel
BuildRequires:  systemd-udev
BuildRequires:  systemd-rpm-macros
BuildRequires:  libconfig-devel
BuildRequires:  libevdev-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ipcgull-devel

%description
This is an unofficial driver for Logitech mice and keyboard.

This is currently only compatible with HID++ >2.0 devices.

%prep
%forgesetup
%patch -p1 0
rmdir src/ipcgull

%build
%{cmake}
%{cmake_build}

%install
%{cmake_install}

%post
%systemd_post logid.service

%preun
%systemd_preun logid.service

%postun
%systemd_postun_with_restart logid.service

%files
%{_bindir}/logid
%{_unitdir}/logid.service
%{_datadir}/dbus-1/system.d/pizza.pixl.LogiOps.conf
%license LICENSE
%doc README.md
%doc TESTED.md
%doc logid.example.cfg

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 30 2024 Nicolas De Amicis <deamicis@bluewin.ch> - 0.3.5-1
- Fixes CVE-2024-45752

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.3.4-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri May 31 2024 Nicolas De Amicis <deamicis@bluewin.ch> - 0.3.4-1
- Bump to 0.3.4: Fix building on GCC 14

* Sun Feb 04 2024 Nicolas De Amicis <deamicis@bluewin.ch> - 0.3.3-4
- Adding missing algorithm header

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 26 2023 Nicolas De Amicis <deamicis@bluewin.ch> - 0.3.3-1
- New version 0.3.3 and add dependency to ipcgull lib

* Fri May 05 2023 Nicolas De Amicis <deamicis@bluewin.ch> - 0.3.1-1
- New version 0.3.1

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3^1.gitdbe2b28-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3^1.gitdbe2b28-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Mar 08 2022 Nicolas De Amicis <deamicis@bluewin.ch> - 0.2.3^1.gitdbe2b28-10
- Updated to latest commit dbe2b28 from upstream

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3^1.git6bb4700-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Oct 06 2021 Nicolas De Amicis <deamicis@bluewin.ch> - 0.2.3^1.git6bb4700-8
- Updated to latest commit 6bb4700 from upstream

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Apr 13 2021 Nicolas De Amicis <deamicis@bluewin.ch> - 0.2.3-6
- New version 0.2.3

* Wed Mar 31 2021 Jonathan Wakely <jwakely@redhat.com> - 0.2.2-5
- Rebuilt for removed libstdc++ symbols (#1937698)

* Tue Mar 02 2021 Zbigniew JÄ™drzejewski-Szmek <zbyszek@in.waw.pl> - 0.2.2-4
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Mon Feb 15 2021 Nicolas De Amicis <deamicis@bluewin.ch> - 0.2.2-3
- Fix build error (thread import) see bug 1923298

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 31 2020 Nicolas De Amicis <deamicis@bluewin.ch> - 0.2.2-1
- Initial packaging
