#
# spec file for package usbauth
#
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
Version:        1.0.1
Summary:        USB firewall against BadUSB attacks
Url:            https://github.com/kochstefan/usbauth-all/tree/master/usbauth

Release:        8%{?dist}
License:        GPLv2

# Generate a source tarball:
# git clone https://github.com/kochstefan/usbauth-all.git
# cd usbauth-all
# git checkout vVERSION
# tar cvfj usbauth-VERSION.tar.bz2 usbauth
Source0:        %{name}-%{version}.tar.bz2

Requires:       systemd
Requires:       udev
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  libudev-devel
BuildRequires:  libusbauth-configparser-devel

BuildRequires:  dbus-devel


%description
It is a firewall against BadUSB attacks.
A config file describes in which way devices would be accepted.

%prep
%setup -q -n %{name}

%build
autoreconf -f -i
%configure
%make_build

%install
%make_install udevrulesdir=%_udevrulesdir

%files
%license COPYING
%doc README
%_sbindir/usbauth
%config %_sysconfdir/dbus-1/system.d/org.opensuse.usbauth.conf
%config(noreplace) %_sysconfdir/usbauth.conf
%_udevrulesdir/20-usbauth.rules
%_mandir/man1/usbauth.1.*


%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 22 2019 stefan.koch10@gmail.com - 1.0.1-1
- initial package for usbauth USB firewall against BadUSB attacks
