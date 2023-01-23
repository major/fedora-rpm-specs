#
# spec file for package usbauth-notifier
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2017-2018 Stefan Koch <stefan.koch10@gmail.com>
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


Name:           usbauth-notifier
Version:        1.0.2
Summary:        Notifier for USB Firewall to use with desktop environments
Url:            https://github.com/kochstefan/usbauth-all/tree/master/usbauth-notifier

Release:        8%{?dist}
License:        GPLv2

# Generate a source tarball:
# git clone https://github.com/kochstefan/usbauth-all.git
# cd usbauth-all
# git checkout vVERSION
# tar cvfj usbauth-notifier-VERSION.tar.bz2 usbauth-notifier
Source0:        %{name}-%{version}.tar.bz2

Requires:       usbauth
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  libnotify-devel
BuildRequires:  libtool
BuildRequires:  libudev-devel
BuildRequires:  libusbauth-configparser-devel

Requires(pre):  shadow-utils
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig

%description
A notifier for the usbauth firewall against BadUSB attacks.
The user could manually allow or deny USB devices.

%prep
%setup -q -n %{name}

%build
autoreconf -f -i
%configure
%make_build

%pre
getent group usbauth >/dev/null || groupadd -r usbauth
getent group usbauth-notifier >/dev/null || groupadd -r usbauth-notifier
exit 0

%install
%make_install
%find_lang %name

%files -f %name.lang
%license COPYING
%doc README
%dir %_sysconfdir/xdg/autostart
%_sysconfdir/xdg/autostart/usbauth-notifier.desktop
%attr(04750,root,usbauth) %_libexecdir/usbauth-npriv
%dir %attr(00750,root,usbauth-notifier) %_libexecdir/usbauth-notifier
%attr(02755,root,usbauth) %_libexecdir/usbauth-notifier/usbauth-notifier
%_mandir/man1/usbauth-notifier.1*
%_mandir/man1/usbauth-npriv.1*


%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 30 2019 stefan.koch10@gmail.com - 1.0.2-1
- move binaries from bindir to libexecdir

* Sat Jan 12 2019 stefan.koch10@gmail.com - 1.0-1
- initial notifier package to use with desktop environments for usbauth USB Firewall
