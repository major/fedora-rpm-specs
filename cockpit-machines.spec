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
Version:        289
Release:        1%{?dist}
Summary:        Cockpit user interface for virtual machines
License:        LGPL-2.1-or-later AND MIT
URL:            https://github.com/cockpit-project/cockpit-machines

Source0:        https://github.com/cockpit-project/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
BuildArch:      noarch
BuildRequires:  libappstream-glib
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
Requires: (libvirt-daemon-driver-interface if virt-install)
Requires: (libvirt-daemon-config-network if virt-install)
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
# Optional components
Recommends: virt-install >= 3.0.0
Recommends: libosinfo
Recommends: python3-gobject-base
Suggests: (qemu-virtiofsd or virtiofsd)

Provides: bundled(npm(@babel/runtime)) = 7.21.0
Provides: bundled(npm(@novnc/novnc)) = 1.4.0
Provides: bundled(npm(@patternfly/patternfly)) = 5.0.0-alpha.40
Provides: bundled(npm(@patternfly/react-console)) = 5.0.0-alpha.1
Provides: bundled(npm(@patternfly/react-core)) = 5.0.0-alpha.72
Provides: bundled(npm(@patternfly/react-icons)) = 5.0.0-alpha.10
Provides: bundled(npm(@patternfly/react-styles)) = 5.0.0-alpha.7
Provides: bundled(npm(@patternfly/react-table)) = 5.0.0-alpha.74
Provides: bundled(npm(@patternfly/react-tokens)) = 5.0.0-alpha.7
Provides: bundled(npm(@spice-project/spice-html5)) = 0.2.1
Provides: bundled(npm(attr-accept)) = 2.2.2
Provides: bundled(npm(available-typed-arrays)) = 1.0.5
Provides: bundled(npm(call-bind)) = 1.0.2
Provides: bundled(npm(date-fns)) = 2.28.0
Provides: bundled(npm(deep-equal)) = 2.0.5
Provides: bundled(npm(define-properties)) = 1.2.0
Provides: bundled(npm(es-get-iterator)) = 1.1.3
Provides: bundled(npm(file-saver)) = 1.3.8
Provides: bundled(npm(file-selector)) = 0.6.0
Provides: bundled(npm(focus-trap)) = 7.4.0
Provides: bundled(npm(for-each)) = 0.3.3
Provides: bundled(npm(function-bind)) = 1.1.1
Provides: bundled(npm(functions-have-names)) = 1.2.3
Provides: bundled(npm(get-intrinsic)) = 1.2.0
Provides: bundled(npm(gopd)) = 1.0.1
Provides: bundled(npm(has-bigints)) = 1.0.2
Provides: bundled(npm(has-property-descriptors)) = 1.0.0
Provides: bundled(npm(has-symbols)) = 1.0.3
Provides: bundled(npm(has-tostringtag)) = 1.0.0
Provides: bundled(npm(has)) = 1.0.3
Provides: bundled(npm(internal-slot)) = 1.0.5
Provides: bundled(npm(is-arguments)) = 1.1.1
Provides: bundled(npm(is-bigint)) = 1.0.4
Provides: bundled(npm(is-boolean-object)) = 1.1.2
Provides: bundled(npm(is-callable)) = 1.2.7
Provides: bundled(npm(is-date-object)) = 1.0.5
Provides: bundled(npm(is-map)) = 2.0.2
Provides: bundled(npm(is-number-object)) = 1.0.7
Provides: bundled(npm(is-regex)) = 1.1.4
Provides: bundled(npm(is-set)) = 2.0.2
Provides: bundled(npm(is-string)) = 1.0.7
Provides: bundled(npm(is-symbol)) = 1.0.4
Provides: bundled(npm(is-typed-array)) = 1.1.10
Provides: bundled(npm(is-weakmap)) = 2.0.1
Provides: bundled(npm(is-weakset)) = 2.0.2
Provides: bundled(npm(isarray)) = 2.0.5
Provides: bundled(npm(js-tokens)) = 4.0.0
Provides: bundled(npm(lodash)) = 4.17.21
Provides: bundled(npm(loose-envify)) = 1.4.0
Provides: bundled(npm(object-assign)) = 4.1.1
Provides: bundled(npm(object-inspect)) = 1.12.3
Provides: bundled(npm(object-is)) = 1.1.5
Provides: bundled(npm(object-keys)) = 1.1.1
Provides: bundled(npm(object.assign)) = 4.1.4
Provides: bundled(npm(prop-types)) = 15.8.1
Provides: bundled(npm(react-dom)) = 18.2.0
Provides: bundled(npm(react-dropzone)) = 14.2.3
Provides: bundled(npm(react-is)) = 16.13.1
Provides: bundled(npm(react)) = 18.2.0
Provides: bundled(npm(redux-thunk)) = 2.4.2
Provides: bundled(npm(redux)) = 4.1.2
Provides: bundled(npm(regenerator-runtime)) = 0.13.11
Provides: bundled(npm(regexp.prototype.flags)) = 1.5.0
Provides: bundled(npm(scheduler)) = 0.23.0
Provides: bundled(npm(side-channel)) = 1.0.4
Provides: bundled(npm(stop-iteration-iterator)) = 1.0.0
Provides: bundled(npm(tabbable)) = 6.1.1
Provides: bundled(npm(throttle-debounce)) = 3.0.1
Provides: bundled(npm(tslib)) = 2.5.0
Provides: bundled(npm(which-boxed-primitive)) = 1.0.2
Provides: bundled(npm(which-collection)) = 1.0.1
Provides: bundled(npm(which-typed-array)) = 1.1.9
Provides: bundled(npm(xterm-addon-canvas)) = 0.3.0
Provides: bundled(npm(xterm-addon-fit)) = 0.2.1
Provides: bundled(npm(xterm)) = 4.19.0
Provides: bundled(npm(xterm)) = 5.1.0

%description
Cockpit component for managing virtual machines.

If "virt-install" is installed, you can also create new virtual machines.

%prep
%setup -q -n %{name}

%build
# Nothing to build

%install
%make_install
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*

%files
%doc README.md
%license LICENSE dist/index.js.LEGAL.txt dist/index.css.LEGAL.txt
%{_datadir}/cockpit/*
%{_datadir}/metainfo/*

# The changelog is automatically generated and merged
%changelog
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


