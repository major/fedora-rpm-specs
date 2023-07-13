# This is the commit corresponding to the untagged 23.07 release
# https://github.com/Mellanox/mlnx-tools/issues/60
%global commit 54a51a79b3f161577e7226c30c3a5c01183fb956

Name:           mlnx-tools
Version:        23.07
Release:        %autorelease
Summary:        Mellanox userland tools and scripts

License:        CPL-1.0 OR BSD-2-Clause OR GPL-2.0-only
URL:            https://github.com/Mellanox/mlnx-tools
Source:         %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz
# Add missing license files
Patch:          %{url}/pull/59.patch

BuildRequires:  make
BuildRequires:  sed

Requires:       ethtool
Requires:       iproute
Requires:       pciutils
Requires:       systemd-udev

BuildArch:      noarch

%description
This package provides various Mellanox userland tools and scripts.

%prep
%autosetup -p1 -n %{name}-%{commit}

# Fix Python shebangs
sed -i "\|#!/usr/bin/python|d" python/Python/dcbnetlink.py
sed -i 's:#!/usr/bin/python:#!/usr/bin/python3:' \
  python/mlnx_dump_parser \
  python/mlnx_perf \
  python/mlnx_qos \
  python/mlx_fs_dump \
  python/tc_wrap.py

sed -i 's:#!/usr/bin/env python:#!/usr/bin/env python3:' \
  python/ib2ib_setup \
  python/mlnx_tune

%build
# Nothing to build

%install
%make_install SBIN_DIR="%{_sbindir}" SBIN_TDIR="%{_sbindir}"

%files
%license LICENSE.BSD-2-Clause LICENSE.CPL-1.0 LICENSE.GPL-2.0
%doc README.md doc/ib2ib_setup.txt
/lib/udev/mlnx_bf_udev
%{_bindir}/mlnx_dump_parser
%{_bindir}/mlnx_perf
%{_bindir}/mlnx_qos
%{_bindir}/mlx_fs_dump
%{_bindir}/tc_wrap.py
%{_sbindir}/cma_roce_mode
%{_sbindir}/cma_roce_tos
%{_sbindir}/common_irq_affinity.sh
%{_sbindir}/compat_gid_gen
%{_sbindir}/ib2ib_setup
%{_sbindir}/mlnx-sf
%{_sbindir}/mlnx_affinity
%{_sbindir}/mlnx_bf_configure
%{_sbindir}/mlnx_bf_configure_ct
%{_sbindir}/mlnx_tune
%{_sbindir}/mlnxofedctl
%{_sbindir}/set_irq_affinity.sh
%{_sbindir}/set_irq_affinity_bynode.sh
%{_sbindir}/set_irq_affinity_cpulist.sh
%{_sbindir}/show_counters
%{_sbindir}/show_gids
%{_sbindir}/show_irq_affinity.sh
%{_sbindir}/show_irq_affinity_hints.sh
%{_sbindir}/sysctl_perf_tuning
%{_datadir}/mlnx-tools
%{_mandir}/man8/ib2ib_setup.8*
%{_mandir}/man8/mlnxofedctl.8*

%changelog
%autochangelog
