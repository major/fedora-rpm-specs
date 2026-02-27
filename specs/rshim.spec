# SPDX-License-Identifier: GPL-2.0-only
# Copyright (C) 2019 Mellanox Technologies. All Rights Reserved.
#

Name: rshim
Version: 2.6.6
Release: %autorelease
Summary: User-space driver for Mellanox BlueField SoC
# Most code dual licensed: GPL-2.0 or BSD-3-Clause
# fwpkg_unpack.py: MIT
License: (GPL-2.0-only OR BSD-3-Clause) AND MIT
URL: https://github.com/mellanox/rshim-user-space
Source0: https://github.com/Mellanox/rshim-user-space/archive/refs/tags/%{name}-%{version}.tar.gz

BuildRequires: gcc, autoconf, automake, make
BuildRequires: pkgconfig(libpci), pkgconfig(libusb-1.0), pkgconfig(fuse3)
BuildRequires: systemd
BuildRequires: systemd-rpm-macros

Requires: kmod(cuse.ko)
Suggests: kernel-modules-extra

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
# fuse3 requires a 64bit off_t (-D_FILE_OFFSET_BITS=64 on 32bit)
ExcludeArch: %{ix86}

%description
This is the user-space driver to access the BlueField SoC via the rshim
interface. It provides ways to push boot stream, debug the target or login
via the virtual console or network interface.

%prep
%autosetup -p1 -n rshim-user-space-%{name}-%{version}

%build
./bootstrap.sh
%configure
%make_build

%install
%make_install

# Leave /etc for the user's configs and overrides
mkdir -p %{buildroot}%{_prefix}/lib/systemd/network
mv %{buildroot}/etc/systemd/network/10-tmfifo-net.link \
   %{buildroot}%{_prefix}/lib/systemd/network/

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
%{_sbindir}/bf-pldm-ver
%{_sbindir}/bf-reg
%{_sbindir}/bfb-install
%{_sbindir}/bfb-tool
%{_sbindir}/fwpkg_unpack.py
%{_sbindir}/mlx-mkbfb
%{_sbindir}/rshim
%{_unitdir}/rshim.service
%{_mandir}/man1/mlx-mkbfb.1.gz
%{_mandir}/man8/bf-pldm-ver.8.gz
%{_mandir}/man8/bf-reg.8.gz
%{_mandir}/man8/bfb-install.8.gz
%{_mandir}/man8/bfb-tool.8.gz
%{_mandir}/man8/rshim.8.gz
%{_prefix}/lib/systemd/network/10-tmfifo-net.link

%changelog
%autochangelog
