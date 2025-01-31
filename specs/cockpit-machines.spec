#
# Copyright (C) 2021 Red Hat, Inc.
#
# Cockpit is free software; you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation; either version 2.1 of the License, or
# (at your option) any later version.
#
# Cockpit is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Cockpit; If not, see <http://www.gnu.org/licenses/>.
#

Name:           cockpit-machines
Version:        327
Release:        1%{?dist}
Summary:        Cockpit user interface for virtual machines
License:        LGPL-2.1-or-later AND MIT
URL:            https://github.com/cockpit-project/cockpit-machines

Source0:        https://github.com/cockpit-project/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
BuildArch:      noarch
%if 0%{?suse_version}
BuildRequires:  appstream-glib
%else
BuildRequires:  libappstream-glib
%endif
BuildRequires:  make
BuildRequires: gettext
%if 0%{?rhel} && 0%{?rhel} <= 8
BuildRequires: libappstream-glib-devel
%endif

Requires: cockpit-bridge >= 215
%if 0%{?suse_version}
Requires: libvirt-daemon-qemu
%else
Requires: libvirt-daemon-driver-qemu
Requires: libvirt-daemon-driver-network
Requires: libvirt-daemon-driver-nodedev
Requires: libvirt-daemon-driver-storage-core
Requires: libvirt-daemon-config-network
Recommends: libvirt-daemon-driver-storage-disk
%if 0%{?rhel}
Requires: qemu-kvm
%else
# smaller footprint on Fedora, as qemu-kvm is really expensive on a server
Requires: qemu-kvm-core
Recommends: qemu-block-curl
Recommends: qemu-char-spice
Recommends: qemu-device-usb-host
Recommends: qemu-device-usb-redirect
# HACK: https://bugzilla.redhat.com/show_bug.cgi?id=2170110
%if 0%{?fedora} >= 38
Requires: (qemu-audio-spice if qemu-char-spice)
%endif
%endif
%endif
Requires: libvirt-client
Requires: libvirt-dbus >= 1.2.0
Requires: virt-install >= 3.0.0
# Optional components
Recommends: libosinfo
Recommends: python3-gobject-base
Suggests: (qemu-virtiofsd or virtiofsd)

Provides: bundled(npm(@novnc/novnc)) = 1.4.0
Provides: bundled(npm(@novnc/novnc)) = 1.5.0
Provides: bundled(npm(@patternfly/patternfly)) = 5.4.2
Provides: bundled(npm(@patternfly/react-console)) = 5.1.0
Provides: bundled(npm(@patternfly/react-core)) = 5.4.12
Provides: bundled(npm(@patternfly/react-icons)) = 5.4.2
Provides: bundled(npm(@patternfly/react-styles)) = 5.4.1
Provides: bundled(npm(@patternfly/react-table)) = 5.4.14
Provides: bundled(npm(@patternfly/react-tokens)) = 5.4.1
Provides: bundled(npm(@spice-project/spice-html5)) = 0.2.1
Provides: bundled(npm(@xterm/addon-canvas)) = 0.7.0
Provides: bundled(npm(@xterm/xterm)) = 5.5.0
Provides: bundled(npm(attr-accept)) = 2.2.5
Provides: bundled(npm(dequal)) = 2.0.3
Provides: bundled(npm(file-saver)) = 1.3.8
Provides: bundled(npm(file-selector)) = 2.1.2
Provides: bundled(npm(focus-trap)) = 7.6.2
Provides: bundled(npm(ipaddr.js)) = 2.2.0
Provides: bundled(npm(js-tokens)) = 4.0.0
Provides: bundled(npm(lodash)) = 4.17.21
Provides: bundled(npm(loose-envify)) = 1.4.0
Provides: bundled(npm(object-assign)) = 4.1.1
Provides: bundled(npm(prop-types)) = 15.8.1
Provides: bundled(npm(react-dom)) = 18.3.1
Provides: bundled(npm(react-dropzone)) = 14.3.5
Provides: bundled(npm(react-is)) = 16.13.1
Provides: bundled(npm(react)) = 18.3.1
Provides: bundled(npm(redux-thunk)) = 3.1.0
Provides: bundled(npm(redux)) = 5.0.1
Provides: bundled(npm(scheduler)) = 0.23.2
Provides: bundled(npm(tabbable)) = 6.2.0
Provides: bundled(npm(throttle-debounce)) = 5.0.2
Provides: bundled(npm(tslib)) = 2.8.1
Provides: bundled(npm(xterm-addon-fit)) = 0.2.1
Provides: bundled(npm(xterm)) = 4.19.0

%description
Cockpit component for managing libvirt virtual machines.

%prep
%setup -q -n %{name}

%build
# Nothing to build

%install
%make_install PREFIX=/usr
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*

%files
%doc README.md
%license LICENSE dist/index.js.LEGAL.txt dist/index.css.LEGAL.txt
%{_datadir}/cockpit/*
%{_datadir}/metainfo/*

# The changelog is automatically generated and merged
%changelog
* Wed Jan 29 2025 Packit <hello@packit.dev> - 327-1
- Translation updates

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 326-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Dec 18 2024 Packit <hello@packit.dev> - 326-1
- Download and install unsupported and older operating systems

* Wed Dec 04 2024 Packit <hello@packit.dev> - 325-1
- Improve rendering of VM descriptions
- Translation updates

* Wed Nov 20 2024 Packit <hello@packit.dev> - 324-1
- Limit size of descriptions

* Wed Nov 06 2024 Packit <hello@packit.dev> - 323-1
- Action to add a TPM

* Wed Oct 23 2024 Packit <hello@packit.dev> - 322-1
- Bug fixes and translation updates

* Wed Oct 09 2024 Packit <hello@packit.dev> - 321-1
- Drop usage of virtinterfaced

* Wed Sep 25 2024 Packit <hello@packit.dev> - 320-1
- Improve snapshot memory path handling
- Add support for VM descriptions

* Wed Sep 04 2024 Packit <hello@packit.dev> - 319-1
- Translation updates
- Bug fixes

* Tue Aug 20 2024 Packit <hello@packit.dev> - 318-1
- Translation updates
- Test fixes

* Thu Aug 08 2024 Packit <hello@packit.dev> - 317-1
- Bug fixes

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 316-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 10 2024 Packit <hello@packit.dev> - 316-1
- Bug fixes and performance improvements

* Wed Jun 26 2024 Packit <hello@packit.dev> - 315-1
- Translation updates and bug fixes

* Wed Jun 12 2024 Packit <hello@packit.dev> - 314-1
- Fix translation extraction
- Translation updates

* Thu May 30 2024 Packit <hello@packit.dev> - 313-1
- Updates to translations

* Thu Apr 25 2024 Packit <hello@packit.dev> - 312-1
- Bug fixes and performance improvements
Resolves: jira#RHEL-33468

* Wed Apr 10 2024 Packit <hello@packit.dev> - 311-1
- Allow pasting multiple SSH keys at once in Create VM dialog
- Fix detaching host device for running VMs

* Wed Mar 27 2024 Packit <hello@packit.dev> - 310-1
- Bug fixes and performance improvements

* Wed Mar 13 2024 Packit <hello@packit.dev> - 309-1
 - "bug fixes and performance improvements"

* Tue Feb 20 2024 Packit <hello@packit.dev> - 308-1
- Add TPM when switching to EFI
- Translation updates (RHEL-14230)

* Wed Feb 14 2024 Packit <hello@packit.dev> - 307-1
- Mass SPICE replacement
- Pre-formatted Block Device storage pool support

* Wed Jan 31 2024 Packit <hello@packit.dev> - 306-1
- Machines: Action to Replace SPICE devices
- Machines: Create external snapshots when supported

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 305-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 305-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Packit <hello@packit.dev> - 305-1
- many small bug fixes

* Fri Dec 15 2023 Martin Pitt <mpitt@redhat.com> - 304-1
- Performance and stability improvements

* Wed Nov 29 2023 Packit <hello@packit.dev> - 303-1
- Change "Add disk" default behavior

* Wed Nov 15 2023 Packit <hello@packit.dev> - 302-1
- Performance and stability improvements

* Thu Nov 02 2023 Packit <hello@packit.dev> - 301.1-1
- Test fixes

* Wed Oct 18 2023 Packit <hello@packit.dev> - 300-1
- Add SSH keys to VM creation dialog

* Wed Sep 20 2023 Packit <hello@packit.dev> - 299-1
- Performance and stability improvements

* Wed Sep 06 2023 Packit <hello@packit.dev> - 298-1
- Bug fixes and stability improvements

* Wed Aug 23 2023 Packit <hello@packit.dev> - 297-1
- Bug fixes and stability improvements

* Wed Aug 09 2023 Packit <hello@packit.dev> - 296-1
- Update to PatternFly 5

* Wed Jul 26 2023 Packit <hello@packit.dev> - 295-1
- Performance and stability improvements

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 294-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Packit <hello@packit.dev> - 294-1
- Bug fixes and translation updates

* Wed Jun 28 2023 Packit <hello@packit.dev> - 293-1
- Confirm shutdown actions
- Show virtual interface's TAP device

* Thu Jun 15 2023 Packit <hello@packit.dev> - 292-1
- Add manifest condition for the Python bridge

* Thu Jun 01 2023 Packit <hello@packit.dev> - 291-1
- Maintenance and translation updates

* Tue May 16 2023 Packit <hello@packit.dev> - 290-1
- Apply watchdog changes on next boot if hotplug fails

* Fri May 05 2023 Packit <hello@packit.dev> - 289.1-1
- Fix alignment of icons in main view

* Thu May 04 2023 Packit <hello@packit.dev> - 289-1
- Update to PatternFly 5 Alpha
- Option to use RAW volume during VM creation
- Redesign VM’s CPU configuration

* Wed Apr 19 2023 Packit <hello@packit.dev> - 288-1
- Indicate need for shutdown
- Delete storage file upon disk detachment

* Thu Apr 06 2023 Packit <hello@packit.dev> - 287-1
- Show an alert when virtualization is disabled in BIOS/EFI

* Wed Mar 22 2023 Packit <hello@packit.dev> - 286-1
- Create VM based on cloud image and start it later

* Wed Mar 08 2023 Packit <hello@packit.dev> - 285-1
- Stability and performance improvements

* Wed Feb 22 2023 Packit <hello@packit.dev> - 284-1
- Stability and performance improvements

* Wed Feb 08 2023 Packit <hello@packit.dev> - 283-1
- Stability and performance improvements

* Wed Jan 25 2023 Packit <hello@packit.dev> - 282-1
- Option to forcefully revert a snapshot
- Fix tabular numbers font

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 281-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 11 2023 Packit <hello@packit.dev> - 281-1
- Summarize system and user session differences
- Virtual watchdog device support

* Tue Jan 03 2023 Packit <hello@packit.dev> - 280-1
- Start using tabular fonts
- Other UI fixes and improvements


* Thu Dec 01 2022 Packit <hello@packit.dev> - 279-1
- Autodetect file's format when attaching disk


* Wed Nov 16 2022 Packit <hello@packit.dev> - 278-1
- Stability and performance improvements


* Mon Nov 07 2022 Packit <hello@packit.dev> - 277-1
- Dark theme support
- Allow TRIM/UNMAP requests by default for newly added disks
- Insert and eject CD & DVD media


* Wed Oct 19 2022 Packit <hello@packit.dev> - 276-1
- Add connection information to the VM detail page


* Wed Sep 21 2022 Packit <hello@packit.dev> - 275-1
- Improvements of offline token management


* Wed Sep 07 2022 Packit <hello@packit.dev> - 274-1
 - Stability and performance improvements


* Wed Aug 24 2022 Packit <hello@packit.dev> - 273-1
- Fix downloading of RHEL images


* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 272-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Packit <hello@packit.dev> - 272-1
- Download RHEL images


* Thu Jun 23 2022 Packit <hello@packit.dev> - 271-1
- Test fixes


* Sat Jun 11 2022 Packit <hello@packit.dev> - 270.2-1
- Fix test/reference setup in release tarball for tests


* Thu Jun 09 2022 Packit <hello@packit.dev> - 270.1-1
- Fix release tarball


* Wed Jun 08 2022 Packit <hello@packit.dev> - 270-1
- Tests improvements and stabilization


* Tue May 24 2022 Marius Vollmer <mvollmer@redhat.com> - 269-1
- Machines: Redesign content removal dialogs

* Thu May 12 2022 Allison Karlitskaya <allison.karlitskaya@redhat.com> - 268-1
- Provide default name for new VMs

* Thu Apr 28 2022 Jelle van der Waa <jvanderwaa@redhat.com> - 267-1
- Tests improvements and stabilization

* Wed Apr 13 2022 Martin Pitt <martin@piware.de> - 266-1
- Redesign VM creation
- Remove static hosts from virtual network's DHCP

* Wed Mar 30 2022 Matej Marusak <mmarusak@redhat.com> - 265-1
- Translation updates
- Tests robustification

* Wed Mar 16 2022 Simon Kobyda <skobyda@redhat.com> - 264-1
- Disk serial number
- Multiple fixes of host device attachement

* Wed Mar 02 2022 Martin Pitt <martin@piware.de> - 263-1
- Delete storage files also when the VM is shut off
- Translation updates (rhbz#2017343)

* Thu Feb 24 2022 Martin Pitt <martin@piware.de> - 262-1
- Fix broken VM deletion dialog layout
- Translation updates (rhbz#2017343)

* Wed Feb 16 2022 Jelle van der Waa <jvanderwaa@redhat.com> - 261-1
- Tests improvements and stabilization

* Mon Jan 24 2022 Matej Marusak <mmarusak@redhat.com> - 260-1
- Tests improvements and stabilization

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 259-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 05 2022 Simon Kobyda <skobyda@redhat.com> - 259-1
- Update to upstream 259 release

* Mon Dec 13 2021 Martin Pitt <martin@piware.de> - 258.1-1
- Test fixes

* Thu Dec 09 2021 Marius Vollmer <mvollmer@redhat.com> - 258-1
- Move storage pool actions outside of the expanded row
- Move the 'Overview' tab content from the network rows to the expanded row directly

* Fri Nov 19 2021 Katerina Koukiou <kkoukiou@redhat.com> - 257-1
- Test fixes for RHEL gating

* Wed Nov 10 2021 Katerina Koukiou <kkoukiou@redhat.com> - 256-1
- Now officially supported on Arch Linux (https://archlinux.org/)
- Support selecting between consoles of the same type

* Wed Oct 27 2021 Jelle van der Waa <jvanderwaa@redhat.com> - 255-1
- Translation updates

* Wed Oct 13 2021 Martin Pitt <martin@piware.de> - 254-1
- Support configuring static MAC → IP address mappings

* Wed Sep 29 2021 Matej Marusak <mmarusak@redhat.com> - 253-1
- Support adding and removing host devices

* Wed Sep 15 2021 Katerina Koukiou <kkoukiou@redhat.com> - 252-1
- Add support for renaming VMs

* Wed Sep 01 2021 Simon Kobyda <skobyda@redhat.com> - 251-1
- Bug fixes and improvements

* Tue Aug 24 2021 Matej Marusak <mmarusak@redhat.com> - 250.1-1
- Test fixes for RHEL gating

* Wed Aug 18 2021 Marius Vollmer <mvollmer@redhat.com> - 250-1
- Update to upstream 250 release

* Wed Aug 04 2021 Martin Pitt <martin@piware.de> - 249.1-1
- Test fixes for Fedora/RHEL gating

* Wed Aug 04 2021 Martin Pitt <martin@piware.de> - 249-1
- Disable non-shared storage migration on RHEL
- Lots of bug fixes
- Translation updates

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 248-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul 21 2021 Matej Marusak <mmarusak@redhat.com> - 248-1
- Some nice bug fixes

* Wed Jul 07 2021 Allison Karlitskaya <allison.karlitskaya@redhat.com> - 247-1
- A myriad of bug fixes

* Wed Jun 23 2021 Katerina Koukiou <kkoukiou@redhat.com> - 246-1
- Share host files with the guest using virtiofs
- Show list of pass-through devices


* Wed Jun 09 2021 Marius Vollmer <mvollmer@redhat.com> - 245-1
- Updated translations
- Fixed localization of VncConsole


* Wed May 19 2021 Martin Pitt <martin@piware.de> - 244.1-1
- Fix crash on VM deletion with cockpit 244


* Wed May 12 2021 Katerina Koukiou <kkoukiou@redhat.com> - 244-1
- Edit the MAC address of a VM’s network interface


* Thu Apr 22 2021 Martin Pitt <martin@piware.de> - 243.1-1
- Fix tooltip on Plug/Unplug button
- Integration test fixes


* Wed Apr 14 2021 Matej Marusak <mmarusak@redhat.com> - 243-1
- PatternFly 4 updates
- Translation updates
- Correctly manage editing of unknown bus type


* Thu Apr 01 2021 Katerina Koukiou <kkoukiou@redhat.com> - 242.1-1
- Add MIT to the list of licenses in spec file


