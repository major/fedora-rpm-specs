Name:          bolt
Version:       0.9.8
Release:       4%{?dist}
Summary:       Thunderbolt device manager
License:       LGPL-2.1-or-later
URL:           https://gitlab.freedesktop.org/bolt/bolt
Source0:       %{url}/-/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:        0001-test-test-unix-skip-unix-domain-socket-test.patch

BuildRequires: gcc
BuildRequires: asciidoc
BuildRequires: meson
BuildRequires: libudev-devel
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(systemd)
BuildRequires: polkit-devel
BuildRequires: systemd
%{?systemd_requires}

# for the integration test (optional)
%if 0%{?fedora} || 0%{?rhel} > 8
BuildRequires: python3-gobject-base
BuildRequires: python3-dbus
BuildRequires: python3-dbusmock
BuildRequires: umockdev-devel
%endif

%description
bolt is a system daemon to manage Thunderbolt devices via a D-BUS
API. Thunderbolt 3 introduced different security modes that require
devices to be authorized before they can be used. The D-Bus API can be
used to list devices, enroll them (authorize and store them in the
local database) and forget them again (remove previously enrolled
devices). It also emits signals if new devices are connected (or
removed). During enrollment devices can be set to be automatically
authorized as soon as they are connected.  A command line tool, called
boltctl, can be used to control the daemon and perform all the above
mentioned tasks.

%prep
%autosetup -p1

%build
%meson -Ddb-name=boltd
%meson_build

%check
%meson_test

%install
%meson_install

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license COPYING
%doc README.md CHANGELOG.md
%{_bindir}/boltctl
%{_libexecdir}/boltd
%{_unitdir}/%{name}.service
%{_udevrulesdir}/*-%{name}.rules
%{_datadir}/dbus-1/system.d/org.freedesktop.bolt.conf
%{_datadir}/dbus-1/interfaces/org.freedesktop.bolt.xml
%{_datadir}/polkit-1/actions/org.freedesktop.bolt.policy
%{_datadir}/polkit-1/rules.d/org.freedesktop.bolt.rules
%{_datadir}/dbus-1/system-services/org.freedesktop.bolt.service
%{_mandir}/man1/boltctl.1*
%{_mandir}/man8/boltd.8*
%ghost %dir %{_localstatedir}/lib/boltd

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri May 31 2024 Kate Hsuan <hpa@redhat.com> - 0.9.8-2
- Update python3-gobject-base dependency for test

* Wed May 22 2024 Kate Hsuan <hpa@redhat.com> - 0.9.8-1
- A new NHI for REMBRANDT.
- systemd configuration improvement.
- Fixed: Determine the string length before writing file.
- Fixed: Free on error to prevent resource leak.

* Fri Mar 1 2024 Kate Hsuan <hpa@redhat.com> - 0.9.7-1
- bolt 0.9.7 release
- Support 'nopcie' security level
- Bug fixes

* Thu Feb 1 2024 Kate Hsuan <hpa@redhat.com> - 0.9.6-4
- Update SPDX license

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Sep 13 2023 Kate Hsuan <hpa@redhat.com> - 0.9.6-1
- Update 0.9.6 release
- Fixing for compiler warning and log message issues

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Feb 14 2023 Kate hsuan <hpa@redhat.com> - 0.9.5-1
- Updated to upstream version

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 23 2022 Simon Steinbeiss <simon.steinbeiss@redhat.com> - 0.9.3-1
- New upstream release

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 27 2022 Christian Kellner <ckellner@redhat.com> - 0.9.2-1
- bolt 0.9.2 release

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.9.1-3
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec  1 2020 Christian Kellner <ckellner@redhat.com> - 0.9.1-1
- bolt 0.9.1 release
- Update description with less emphasis on Thunderbolt version

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 15 2020 Christian Kellner <ckellner@redhat.com> - 0.9-1
- bolt 0.9 release
  Drop all patches (all merged upstream).

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Christian Kellner <christian@kellner.me> - 0.8-3
- Add patch to ignore uevents from wakeup devices. See upstream issue
  https://gitlab.freedesktop.org/bolt/bolt/issues/156
- Add patch to fix BoltError not being a typedef.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 13 2019 Christian Kellner <ckellner@redhat.com> - 0.8-1
- bolt 0.8 release
  D-Bus Configuration moved from sysconfdir to datadir.
  Package new CHNAGELOG.md.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan  1 2019 Christian Kellner <gicmo@redhat.com> - 0.7-1
- bolt 0.7 release

* Wed Nov 28 2018 Christian Kellner <ckellner@redhat.com> - 0.6-1
- bolt 0.6 release

* Fri Sep 21 2018 Christian Kellner <ckellner@redhat.com> - 0.5-1
- bolt 0.5 release
- Remove forge macros again and use gitlab as authorative source
- Testing depedencies are now only pulled in on Fedora

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 28 2018 Christian Kellner <ckellner@redhat.com> - 0.4-1
- bolt 0.4 upstream release

* Tue Apr 10 2018 Christian Kellner <ckellner@redhat.com> - 0.3-1
- bolt 0.3 upstream release
- Update BuildRequires to include gcc
- Use forge macros

* Tue Mar  6 2018 Christian Kellner <ckellner@redhat.com> - 0.2-1
- bolt 0.2 upstream release
- Update BuildRequires dependencies.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 17 2017 Christian Kellner <ckellner@redhat.com> - 0.1-2
- Set database path to /var/lib/boltd, create it during
  installation, which is needed for the service file to work.

* Thu Dec 14 2017 Christian Kellner <ckellner@redhat.com> - 0.1-1
- Initial upstream release
