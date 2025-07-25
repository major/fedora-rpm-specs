%define source_name usb-modeswitch

Name:       usb_modeswitch
Version:    2.6.2
Release:    3%{?dist}
Summary:    USB Modeswitch gets mobile broadband cards in operational mode
Summary(de):    USB Modeswitch aktiviert UMTS-Karten
License:    GPL-2.0-or-later
URL:        http://www.draisberghof.de/usb_modeswitch/

Source0:    http://www.draisberghof.de/%{name}/%{source_name}-%{version}.tar.bz2
Source1:    http://www.draisberghof.de/usb_modeswitch/device_reference.txt

# Submitted upstream (2014-11-24)
Patch0: device_reference-utf8.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  libusbx-devel
# "tcl" or "jimsh"), use the light-weight installation:
#BuildRequires: jimtcl-devel
BuildRequires:  systemd
Requires:   usb_modeswitch-data >= 20121109
Requires:   systemd

%description
USB Modeswitch brings up your datacard into operational mode. When plugged
in they identify themselves as cdrom and present some non-Linux compatible
installation files. This tool deactivates this cdrom-device and enables
the real communication device. It supports most devices built and
sold by Huawei, T-Mobile, Vodafone, Option, ZTE, Novatel.

%description    -l de
USB Modeswitch deaktiviert die CDROM-Emulation einiger UMTS-Karten.
Dadurch erkennt Linux die Datenkarte und kann damit Internet-
Verbindungen aufbauen. Die gängigen Karten von Huawei, T-Mobile,
Vodafone, Option, ZTE und Novatell werden unterstützt.


%prep
%setup -q -n %{source_name}-%{version}
cp -f %{SOURCE1} device_reference.txt

%patch 0 -p0


%build
%{set_build_flags}
# this will require jimtcl-devel
#make_build all-with-dynlink-dispatcher
%make_build


%install
mkdir -p %{buildroot}%{_unitdir}
%make_install \
    SYSDIR=%{buildroot}%{_unitdir} \
    SBINDIR=%{buildroot}%{_sbindir} \
    UDEVDIR=%{buildroot}%{_prefix}/lib/udev


%files
%{_sbindir}/usb_modeswitch
%{_sbindir}/usb_modeswitch_dispatcher
%{_mandir}/man1/usb_modeswitch.1.gz
%{_mandir}/man1/usb_modeswitch_dispatcher.1.gz
%{_prefix}/lib/udev/usb_modeswitch
%{_unitdir}/usb_modeswitch@.service
%config(noreplace) %{_sysconfdir}/usb_modeswitch.conf
%doc README ChangeLog device_reference.txt
%license COPYING


%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Feb 27 2025 Sérgio Basto <sergio@serjux.com> - 2.6.2-2
- Revert the move of usb_modeswitch to /usr/lib/udev/rules.d, usb_modeswitch is
  not an rule

* Thu Feb 20 2025 Sérgio Basto <sergio@serjux.com> - 2.6.2-1
- Update usb_modeswitch to 2.6.2
- Resolves: rhbz#2346392
- Fix build related to /usr/sbin move

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Nov  2 2023 Íñigo Huguet <ihuguet@redhat.com> - 2.6.1-9
- Really use SPDX license specifier

* Thu Aug 24 2023 Till Maas <opensource@till.name> - 2.6.1-8
- Cleanup spec: use %%license, use %%patch 0
- Use spdx license specifier

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 18 2020 Sérgio Basto <sergio@serjux.com> - 2.6.1-1
- Update usb_modeswitch to 2.6.1
- Drop patch1, http://www.draisberghof.de/usb_modeswitch/bb/viewtopic.php?f=2&t=2733
- Drop BR jimtcl-devel, if we don't install dynlink-dispatcher

* Tue Sep 29 2020 Sérgio Basto <sergio@serjux.com> - 2.6.0-3
- Use make macros (https://src.fedoraproject.org/rpms/usb_modeswitch/pull-request/1)
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 24 2020 Lubomir Rintel <lkundrak@v3.sk> - 2.6.0-1
- New 2.6.0 release

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 28 2018 Lubomir Rintel <lkundrak@v3.sk> - 2.5.2-1
- New 2.5.2 release

* Fri Feb 23 2018 Florian Weimer <fweimer@redhat.com> - 2.5.1-3
- Use LDFLAGS from redhat-rpm-config

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Aug 18 2017 Lubomir Rintel <lkundrak@v3.sk> - 2.5.1-1
- New 2.5.1 release

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul 29 2016 Lubomir Rintel <lkundrak@v3.sk> - 2.4.0-5
- Bump the release number to be higher than in Fedora 24

* Thu Jul 21 2016 Lubomir Rintel <lkundrak@v3.sk> - 2.4.0-3
- Fix undefined behavior in config parser (rh #1352055)

* Wed Jul 20 2016 Lubomir Rintel <lkundrak@v3.sk> - 2.4.0-2
- Add the previously omitted systemd service file (rh #1352055)
- Fix crash with invalid arguments (rh #1358472)

* Wed Jun 22 2016 Lubomir Rintel <lkundrak@v3.sk> - 2.4.0-1
- New 2.4.0 release

* Tue May 03 2016 Lubomir Rintel <lkundrak@v3.sk> - 2.3.0-1
- New 2.3.0 release

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Aug 18 2015 Lubomir Rintel <lkundrak@v3.sk> - 2.2.5-1
- New 2.2.5 release

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Feb 22 2015 Peter Robinson <pbrobinson@fedoraproject.org> 2.2.1-1
- New 2.2.1 release

* Mon Nov 24 2014 Till Maas <opensource@till.name> - 2.2.0-2
- Update device_reference.txt, make it proper UTF-8

* Tue Aug 26 2014 Robert M. Albrecht <mail@romal.de> - 2.2.0-1
- New upstream release
- Fixed a typo in the description

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 16 2014 Peter Robinson <pbrobinson@fedoraproject.org> 2.1.1-1
- Update to 2.1.1

* Tue Jan 28 2014 Dan Williams <dcbw@redhat.com> - 2.0.1-2
- Resurrect manpage patch

* Mon Jan  6 2014 Peter Robinson <pbrobinson@fedoraproject.org> 2.0.1-1
- Update to 2.0.1 and build against libusbx (RHBZ 994974)
- Use distro jimtcl (RHBZ 967314)
- Fix build on aarch64
- Cleanup and modernise spec

* Wed Aug 28 2013 Thomas Haller <thaller@redhat.com> 1.2.7-3
- Add manual page for usb_modeswitch_dispatcher and fix errors in
  manual page of usb_modeswitch (rhbz#948451, rhbz#884203).

* Mon Aug 26 2013 Dan Williams <dcbw@redhat.com> - 1.2.7-2
- Fix udev helper path

* Fri Aug 16 2013 Dan Williams <dcbw@redhat.com> - 1.2.7-1
- New upstream release

* Fri Jul 26 2013 Dan Williams <dcbw@redhat.com> - 1.2.6-2
- Fix udev directories

* Wed Jun 12 2013 Huzaifa Sidhpurwala <huzaifas@redhat.com> - 1.2.6
- New upstream release.

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 13 2012 Huzaifa Sidhpurwala <huzaifas@redhat.com> - 1.2.5-1
- New upstream release. Resolves rhbz#875832

* Fri Aug 24 2012 Huzaifa Sidhpurwala <huzaifas@redhat.com> - 1.2.4-1
- New upstream release. Resolves rhbz#785539

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 24 2012 Dan Williams <dcbw@redhat.com> 1.2.3-1
- Update to new upstream release
- Build TCL tool as a static binary to remove dependency on TCL itself rhbz#760839

* Wed Jan 25 2012 Huzaifa Sidhpurwala <huzaifas@redhat.com> 1.2.2-2
- Add usb_modeswitch.sh udev script and move Tcl dispatcher script to sbindir,
  resolves rhbz#782614, patch from Dominic Cleal
- Fix bus/device-based search, from deb#656248

* Fri Jan 20 2012 Huzaifa Sidhpurwala <huzaifas@redhat.com> 1.2.2
- New upstream version 1.2.2

* Fri Jan 06 2012 Huzaifa Sidhpurwala <huzaifas@redhat.com> 1.2.1-1
- New upstream version 1.2.1

* Tue Oct 25 2011 Huzaifa Sidhpurwala <huzaifas@redhat.com> 1.2.0-1
- New upstream
- use device_reference.txt from upstream

* Mon Mar 28 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 1.1.7-1
- New upstream release.  Resolves rhbz#625004
- Update spec to match current guidelines
- Fix relevant rpmlint errors and warnings

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 30 2010 Dan Williams <dcbw@redhat.com> 1.1.6-1
- New upstream version
