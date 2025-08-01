Name:             umockdev
Version:          0.19.2
Release:          1%{?dist}
Summary:          Mock hardware devices

License:          LGPL-2.1-or-later
URL:              https://github.com/martinpitt/%{name}
Source0:          https://github.com/martinpitt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires:    git
BuildRequires:    meson
BuildRequires:    gtk-doc
BuildRequires:    gobject-introspection-devel
BuildRequires:    glib2-devel
BuildRequires:    libgudev1-devel systemd-devel
BuildRequires:    libpcap-devel
BuildRequires:    vala
BuildRequires:    chrpath
BuildRequires:    systemd-udev

%description
With this program and libraries you can easily create mock udev objects.
This is useful for writing tests for software which talks to
hardware devices.

%package devel
Summary: Development packages for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains the libraries to develop
using %{name}.

%prep
%autosetup -S git -n %{name}-%{version}

%build
%meson -Dgtk_doc=true
%meson_build

%check
# don't be too picky about timing; upstream CI and local developer tests
# are strict, but many koji arches are emulated and utterly slow
export SLOW_TESTBED_FACTOR=10
%meson_test

%install
%meson_install

# Remove rpath
chrpath --delete %{buildroot}%{_bindir}/umockdev-record \
	%{buildroot}%{_bindir}/umockdev-run
chrpath --delete %{buildroot}%{_libdir}/libumockdev.so.*
chrpath --delete %{buildroot}%{_libdir}/libumockdev-preload.so.*

rm -rf $RPM_BUILD_ROOT/%{_datadir}/doc/umockdev

%ldconfig_scriptlets

%files
%license COPYING
%doc README.md
%{_bindir}/umockdev-*
%{_libdir}/libumockdev.so.*
%{_libdir}/libumockdev-preload.so*
%{_libdir}/girepository-1.0/UMockdev-1.0.typelib

%files devel
%doc docs/script-format.txt docs/examples/battery.c docs/examples/battery.py
%{_libdir}/libumockdev.so
%{_libdir}/pkgconfig/umockdev-1.0.pc
%{_datadir}/gir-1.0/UMockdev-1.0.gir
%{_includedir}/umockdev-1.0
%{_datadir}/gtk-doc/html/umockdev/
%{_datadir}/vala/vapi/umockdev-1.0.vapi

%changelog
* Wed Jul 30 2025 Packit <hello@packit.dev> - 0.19.2-1
- preload: Trap dirfd access to /dev, fstat(), and open_tree()

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jan 02 2025 Packit <hello@packit.dev> - 0.19.1-1
- preload: Restore errno in ioctl_emulate_open()
- preload: Only emulate ioctls on emulated devices
- Fix ioctl_tree_execute() ret type and initialization (thanks Helge Deller)
- tests: Disable spidev on big-endian 32-bit platforms (thanks Helge Deller)

* Fri Dec 27 2024 Packit <hello@packit.dev> - 0.19.0-1
- API: Add UMockdev.Testbed.wait_script() to sync to scripts/evemu replays
- API: UMockdev.Testbed.load_script_from_string()
- API: UMockdev.Testbed.load_evemu_events_from_string()
- Make uevent synthesis thread-safe (thanks Bob Henz)
- Handle "connection refused" when sending a uevent (thanks Bob Henz)

* Wed Sep 04 2024 Packit <hello@packit.dev> - 0.18.4-1
- Add ioctls for Chromium OS EC devices (thanks Abhinav Baid)
- Generate "remove" uevent in umockdev_testbed_remove_device() (thanks Bob Henz)
- Recursively remove children with uevents (thanks Bob Henz)
- preload: Fix sigmask block and restore race (thanks barath)

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu May 23 2024 Packit <hello@packit.dev> - 0.18.3-1
- preload: Re-fix time64 redirects for glibc < 2.39.9

* Tue May 21 2024 Packit <hello@packit.dev> - 0.18.2-1
- preload: Fix time64 redirect for glibc 2.39.9

* Sun Mar 24 2024 Packit <hello@packit.dev> - 0.18.1-1
- preload: Provide wrappers for functions specific to 64-bit time_t (thanks Steve Langasek)
- preload: Fix building with _FILE_OFFSET_BITS (thanks Zixing Liu and Steve Langasek)

* Sun Mar 03 2024 Packit <hello@packit.dev> - 0.18.0-1
- Record and restore SELinux context for mocked /dev nodes
- preload: wrap fstatfs() and statfs() on musl
- Fix build with meson 1.4

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 26 2023 Packit <hello@packit.dev> - 0.17.18-1
- preload: Don't read udev cache data from system (thanks Bastien Nocera)
- spec: Update License: to SPDX format
- Various test fixes

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Apr 16 2023 Packit <hello@packit.dev> - 0.17.17-1
- Fix race with worker thread accessing $UMOCKDEV_DIR
- Disable -Wincompatible-function-pointer-types for clang

* Sun Jan 29 2023 Packit <hello@packit.dev> - 0.17.16-1
<!-- generated by eloquent/github-release-action -->
<!-- original source:
- preload: Wrap __getcwd_chk()
- uevent_sender: Fix fd leak in sendmsg_one
- Fix gcc -fanalyzer complaints
-->

<ul>
<li>preload: Wrap __getcwd_chk()</li>
<li>uevent_sender: Fix fd leak in sendmsg_one</li>
<li>Fix gcc -fanalyzer complaints</li>
</ul>

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov 24 2022 Packit <hello@packit.dev> - 0.17.15-1
<!-- generated by eloquent/github-release-action -->
<!-- original source:
- test fixes
-->

<ul>
<li>test fixes</li>
</ul>


* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Packit <hello@packit.dev> - 0.17.13-1
- preload: Wrap fstatfs(), to work with systemd 251 also with Python tests
- Fix tests in Gentoo sandbox build


* Thu May 19 2022 Packit <hello@packit.dev> - 0.17.12-1
- Work around packit propose_downstream bug


* Tue May 10 2022 Packit <hello@packit.dev> - 0.17.10-1
- Adjust to systemd 251-rc2: Set $SYSTEMD_DEVICE_VERIFY_SYSFS, parse new udevadm format, update tests


* Sun Apr 10 2022 Packit <hello@packit.dev> - 0.17.9-1
- preload: Wrap fortified version of readlinkat (thanks Martin Liska)


* Wed Mar 23 2022 Packit Service <user-cont-team+packit-service@redhat.com> - 0.17.8-1
- Fix some potential crashes spotted by Coverity
- Enable Fedora builds and bodhi updates via packit


* Tue Mar 01 2022 Packit Service <user-cont-team+packit-service@redhat.com> - 0.17.7-1
- Fix uevent race condition in umockdev_testbed_add_from_string()


* Fri Jan 21 2022 Packit Service <user-cont-team+packit-service@redhat.com> - 0.17.6-1
- Increase uevent buffer size (#167)
- Skip /umockdev-testbed-vala/detects_running_outside_testbed during normal
  builds for the time being, as it is brittle on several architectures (#169)


* Tue Jan 18 2022 Packit Service <user-cont-team+packit-service@redhat.com> - 0.17.5-1
- Relax overzealous stat nlink unit test


* Mon Jan 10 2022 Packit Service <user-cont-team+packit-service@redhat.com> - 0.17.2-1
- preload: Wrap statx() and fstatat(), to fix `ls` and other tools on
  recent glibc versions. (#160)


* Tue Dec 14 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 0.17.1-1
- Fix /sys/dev/* symlinks; regression from 0.15.3 (#155)


* Sat Dec 11 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 0.17.0-1
- Add ioctls necessary to record/replay hidraw devices (thanks Daiki Ueno)
- meson: Respect includedir option (thanks Florentin Dubois)
- tests: Fix for Fedora koji emulated architectures s390x and arm
- Enable automatic Fedora package updates with packit


* Wed Sep 15 2021 Bastien Nocera <bnocera@redhat.com> - 0.16.3-1
+ umockdev-0.16.3-1
- Update to 0.16.3

* Mon Aug 30 2021 Bastien Nocera <bnocera@redhat.com> - 0.16.2-2
+ umockdev-0.16.2-2
- Better build fix patch

* Wed Aug 25 2021 Bastien Nocera <bnocera@redhat.com> - 0.16.2-1
+ umockdev-0.16.2-1
- Update to 0.16.2

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 02 2021 Bastien Nocera <bnocera@redhat.com> - 0.16.1-1
+ umockdev-0.16.1-1
- Update to 0.16.1

* Thu Jul 01 2021 Bastien Nocera <bnocera@redhat.com> - 0.16.0-1
+ umockdev-0.16.0-1
- Update to 0.16.0

* Thu May 20 2021 Martin Pitt <mpitt@redhat.com> - 0.15.5-2
- Drop gphoto2 build dependency (rhbz#1962633)

* Tue May 04 2021 Bastien Nocera <bnocera@redhat.com> - 0.15.5-1
+ umockdev-0.15.5-1
- Update to 0.15.5

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 03 2021 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 0.15.4-1
- Update to 0.15.4 (#1901619)

* Sun Dec 27 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 0.15.3-1
- Update to 0.15.3 (#1901619)

* Tue Nov 17 2020 Bastien Nocera <bnocera@redhat.com> - 0.15.1-1
+ umockdev-0.15.1-1
- Update to 0.15.1

* Fri Oct 23 2020 Bastien Nocera <bnocera@redhat.com> - 0.14.4-1
+ umockdev-0.14.4-1
- Update to 0.14.4

* Thu Oct 22 2020 Bastien Nocera <bnocera@redhat.com> - 0.14.3-2
+ umockdev-0.14.3-2
- Better debug for missing functions

* Mon Aug 24 2020 Bastien Nocera <bnocera@redhat.com> - 0.14.3-1
+ umockdev-0.14.3-1
- Update to 0.14.3

* Fri Jul 31 2020 Bastien Nocera <bnocera@redhat.com> - 0.14.2-1
+ umockdev-0.14.2-1
- Update to 0.14.2 (#1861973)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 12 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 0.14.1-1
- Update to 0.14.1 (#1802194)

* Sun Feb 09 2020 Bastien Nocera <bnocera@redhat.com> - 0.14-1
+ umockdev-0.14-1
- Fix FTBS (#1800217)

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 02 2019 Bastien Nocera <bnocera@redhat.com> - 0.13.2-1
+ umockdev-0.13.2-1
- Update to 0.13.2 (#1747088)

* Mon Aug 19 2019 Bastien Nocera <bnocera@redhat.com> - 0.13.1-1
+ umockdev-0.13.1-1
- Update to 0.13.1 (#1742178)

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 29 2019 Christian Kellner <ckellner@redhat.com> - 0.12.1-1
- Update to umockdev-0.12.1

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 06 2018 Bastien Nocera <bnocera@redhat.com> - 0.11.3-1
+ umockdev-0.11.3-1
- Update to 0.11.3 (#1550306)

* Wed Mar 28 2018 Bastien Nocera <bnocera@redhat.com> - 0.11.2-1
+ umockdev-0.11.2-1
- Update to 0.11.2 (#1550306)

* Thu Mar 01 2018 Bastien Nocera <bnocera@redhat.com> - 0.11.1-1
+ umockdev-0.11.1-1
- Update to 0.11.1

* Mon Feb 12 2018 Bastien Nocera <bnocera@redhat.com> - 0.11-1
+ umockdev-0.11-1
- Update to 0.11 (#1544128)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Fedora Release Monitoring  <release-monitoring@fedoraproject.org> - 0.10-1
- Update to 0.10 (#1490889)

* Thu Aug 10 2017 Bastien Nocera <bnocera@redhat.com> - 0.9.2-1
- Update to 0.9.2

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 26 2017 Bastien Nocera <bnocera@redhat.com> - 0.8.13-1
+ umockdev-0.8.13-1
- Update to 0.8.13

* Tue Jan 24 2017 Bastien Nocera <bnocera@redhat.com> - 0.8.12-1
+ umockdev-0.8.12-1
- Update to 0.8.12

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Sep 23 2015 Bastien Nocera <bnocera@redhat.com> 0.8.11-1
- Update to 0.8.11

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 29 2015 Bastien Nocera <bnocera@redhat.com> 0.8.8-3
- Fix license/doc mixup
- Add isa to Requires

* Wed Apr 29 2015 Bastien Nocera <bnocera@redhat.com> 0.8.8-2
- Review comments

* Mon Apr 27 2015 Bastien Nocera <bnocera@redhat.com> 0.8.8-1
- Initial package for Fedora
