# SPDX-License-Identifier: GPL-2.0-only
# Copyright (C) 2019 Mellanox Technologies. All Rights Reserved.
#

Name: rshim
Version: 2.0.17
Release: %autorelease
Summary: User-space driver for Mellanox BlueField SoC
License: GPL-2.0-only
URL: https://github.com/mellanox/rshim-user-space
Source0: https://github.com/Mellanox/rshim-user-space/archive/refs/tags/%{name}-%{version}.tar.gz

BuildRequires: gcc, autoconf, automake, make
BuildRequires: pkgconfig(libpci), pkgconfig(libusb-1.0), pkgconfig(fuse)
BuildRequires: systemd
BuildRequires: systemd-rpm-macros

Requires: kmod(cuse.ko)
Suggests: kernel-modules-extra

%description
This is the user-space driver to access the BlueField SoC via the rshim
interface. It provides ways to push boot stream, debug the target or login
via the virtual console or network interface.

%prep
%setup -q -n rshim-user-space-%{name}-%{version}

%build
./bootstrap.sh
%configure
%make_build

%install
%make_install

%post
%systemd_post rshim.service

%preun
%systemd_preun rshim.service

%postun
%systemd_postun_with_restart rshim.service

%files
%license LICENSE
%doc README.md
%config(noreplace) %{_sysconfdir}/rshim.conf
%{_sbindir}/rshim
%{_sbindir}/bfb-install
%{_unitdir}/rshim.service
%{_mandir}/man8/rshim.8.gz
%{_mandir}/man8/bfb-install.8.gz

%changelog
%autochangelog
