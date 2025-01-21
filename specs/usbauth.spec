#
# spec file for package usbauth
#
# Copyright (c) 2019 SUSE LLC
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2017 Stefan Koch <stefan.koch10@gmail.com>
# Copyright (c) 2015 SUSE LLC. All Rights Reserved.
# Author: Stefan Koch <skoch@suse.de>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           usbauth
Version:        1.0.5
Summary:        USB firewall against BadUSB attacks
URL:            https://github.com/kochstefan/usbauth-all/tree/master/usbauth
Source:         https://github.com/kochstefan/usbauth-all/archive/v%{version}.tar.gz

Release:        7%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only

Requires:       systemd
Requires:       udev
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  libusbauth-configparser-devel
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  libudev-devel


%description
It is a firewall against BadUSB attacks.
A config file describes in which way devices would be accepted.

%prep
%autosetup -n usbauth-all-%{version} -p1

%build
pushd %{name}/
autoreconf -f -i
%configure
%make_build
popd

%install
pushd %{name}/
%make_install udevrulesdir=%_udevrulesdir
popd

%files
%license %{name}/COPYING
%doc %{name}/README
%doc %_mandir/*/*
%_sbindir/usbauth
%config %_sysconfdir/dbus-1/system.d/org.opensuse.usbauth.conf
%config(noreplace) %_sysconfdir/usbauth.conf
%_udevrulesdir/20-usbauth.rules


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.5-6
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Mar 11 2023 stefan.koch10@gmail.com - 1.0.5-2
- improve manpage install

* Sat Mar 04 2023 stefan.koch10@gmail.com - 1.0.5-1
- update to v1.0.5

* Tue Jan 22 2019 stefan.koch10@gmail.com - 1.0.1-1
- initial package for usbauth USB firewall against BadUSB attacks