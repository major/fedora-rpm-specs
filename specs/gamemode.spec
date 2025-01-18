Name:		gamemode
Version:	1.8.2
Release:	2%{?dist}
Summary:	Optimize system performance for games on demand
License:	BSD-3-Clause
URL:		https://github.com/FeralInteractive/gamemode
Source0:	%{url}/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires: gcc
BuildRequires: asciidoc
BuildRequires: meson
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(inih) >= 49
BuildRequires: pkgconfig(systemd)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: polkit-devel
BuildRequires: systemd

%description
GameMode is a daemon/lib combo for GNU/Linux that allows games to
request a set of optimizations be temporarily applied to the host OS.
GameMode was designed primarily as a stop-gap solution to problems
with the Intel and AMD CPU "powersave" or "ondemand" governors, but is
now host to a range of optimisation features and configurations, like
tweaking various settings: the CPU govenor, the I/O priority, the
kernel scheduler, the GPU performance mode and gpu overclocking
(NVIDIA). It can also excute custom scripts when launching games.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for development with %{name}.

%prep
%autosetup -p1

%build
%meson
%meson_build

%check
%meson_test

%install
%meson_install

%files
%license LICENSE.txt
%doc	 README.md
%{_bindir}/gamemoded
%{_bindir}/gamemodelist
%{_bindir}/gamemoderun
%{_bindir}/gamemode-simulate-game
%{_libexecdir}/cpucorectl
%{_libexecdir}/cpugovctl
%{_libexecdir}/gpuclockctl
%{_libexecdir}/procsysctl
%{_datadir}/polkit-1/actions/com.feralinteractive.GameMode.policy
%{_datadir}/dbus-1/services/com.feralinteractive.GameMode.service
%{_datadir}/polkit-1/rules.d/gamemode.rules
%{_datadir}/gamemode/gamemode.ini
%{_libdir}/libgamemode*.so.*
%{_sysusersdir}/gamemode.conf
%{_userunitdir}/gamemoded.service
%{_mandir}/man8/gamemoded.8*
%{_mandir}/man1/gamemoderun.1*
%{_mandir}/man1/gamemodelist.1*
%{_mandir}/man1/gamemode-simulate-game.1*
%{_metainfodir}/io.github.feralinteractive.gamemode.metainfo.xml
%config(noreplace) %{_sysconfdir}/security/limits.d/10-gamemode.conf

%files devel
%{_includedir}/gamemode_client.h
%{_libdir}/pkgconfig/gamemode*.pc
%{_libdir}/pkgconfig/libgamemodeauto.pc
%{_libdir}/libgamemode*.so

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Neal Gompa <ngompa@fedoraproject.org> - 1.8.2-1
- Rebase to v1.8.2

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 1.7-7
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Sep 03 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 1.7-1
- Update to 1.7

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 15 2020 Christian Birk <mail@birkc.de> - 1.6-1
- New upstream release (1.6)
- Add new binary gamemode-simulate-game
- Add new manpages for gamemoderun and gamemode-simulate-game
- Add new metadata and a inital config file

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun  4 2020 Christian Kellner <ckellner@redhat.com> - 1.5.1-1
- New upstream release (1.5.1)
- Require inih package because gamemode now uses the system installed one.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Christian Kellner <ckellner@redhat.com> - 1.5-1
- New upstream release (1.5)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 21 2019 Christian Kellner <christian@kellner.me> - 1.4-1
- New upstream release (1.4)
- Add dbus-1 dependency, required by the client library.

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 1.3.1-3
- Rebuild with Meson fix for #1699099

* Mon Apr  8 2019 Christian Kellner <christian@kellner.me> - 1.3.1-2
- Ship unversioned .so in main package, because old games require that one.
  Resolves: rhbz#1694938

* Mon Apr  1 2019 Christian Kellner <christian@kellner.me> - 1.3.1-1
- New upstream release (1.3.1)
  Resloves: rhbz#1694254
- Drop the patch(es) (all upstreamed).

* Thu Mar 28 2019 Christian Kellner <christian@kellner.me> - 1.3-1
- New upstream Release (1.3)
  Resolves: rhbz#1689371
- Includes a new gamemoderun script to easily invoce gamemode.
- Add patch that ensures all strncpy calls leave strings properly null
  terminated and other code cleanups (all but one are upstreamed already).

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Christian Kellner <christian@kellner.me> - 1.2-1
- New upstream release
  Resolves: #1607099
- Drop all patches (all upstreamed)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Christian Kellner <christian@kellner.me>  - 1.1-1
- Initial package
  Resolves: #1596293
- Patch to move manpage to section 8
  Upstream commit 28fcb09413bbf95507788024b98b675cbf656f6c
- Patch for dbus auto-activation
  Merged PR https://github.com/FeralInteractive/gamemode/pull/62
- Patch for proper library versioning
  Merged PR https://github.com/FeralInteractive/gamemode/pull/63

