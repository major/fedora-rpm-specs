# SPDX-License-Identifier: BSD-3-Clause
# Copyright (c) 2025 Robin Jarry

%global forgeurl https://github.com/DPDK/grout
%global _lto_cflags %nil
%if %{defined el9}
%global toolset gcc-toolset-13
%global __meson /usr/bin/scl run %toolset -- /usr/bin/meson
%endif

Name: grout
Version: 0.14.1
Summary: Graph router based on DPDK
License: BSD-3-Clause
Group: System Environment/Daemons

%forgemeta

URL: %{forgeurl}
Release: %{autorelease}
Source0: %{forgesource}
Source1: https://fast.dpdk.org/rel/dpdk-25.11.tar.xz

%if %{defined toolset}
BuildRequires: %toolset
BuildRequires: scl-utils
%else
BuildRequires: gcc >= 13
%endif
BuildRequires: libcap-devel
BuildRequires: libcmocka-devel
BuildRequires: libecoli-devel >= 0.8.0
BuildRequires: libevent-devel
BuildRequires: libmnl-devel
BuildRequires: libsmartcols-devel
BuildRequires: make
BuildRequires: meson
BuildRequires: ninja-build
BuildRequires: numactl-devel
BuildRequires: pkgconf
BuildRequires: scdoc
BuildRequires: socat
BuildRequires: systemd

# DPDK dependencies
BuildRequires: libarchive-devel
BuildRequires: python3-pyelftools
BuildRequires: rdma-core-devel

# No point in running a DPDK application on 32 bit x86: see fedora#2336884
ExcludeArch: %{ix86}
# DPDK does not build on s390x: see fedora#2336876
ExcludeArch: s390x

%description
grout stands for Graph Router. In English, "grout" refers to thin mortar that
hardens to fill gaps between tiles.

grout is a DPDK based network processing application. It uses the rte_graph
library for data path processing.

Its main purpose is to simulate a network function or a physical router for
testing/replicating real (usually closed source) VNF/CNF behavior with an
open-source tool.

It comes with a client library to configure it over a standard UNIX socket and
a CLI that uses that library. The CLI can be used as an interactive shell, but
also in scripts one command at a time, or by batches.

%package devel
Summary: Development headers for building %{name} API clients
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the development headers to build %{name} API clients.

%prep
%forgesetup
%autopatch -p1
%setup -q -T -D -a 1
mv dpdk-* subprojects/dpdk

%build
export GROUT_VERSION=v%{version}-%{release}
%meson -Dfrr=disabled -Ddpdk_static=true
%meson_build

%install
%meson_install --skip-subprojects

install -D -m 0644 main/grout.default %{buildroot}%{_sysconfdir}/default/grout
install -D -m 0644 main/grout.init %{buildroot}%{_sysconfdir}/grout.init
install -D -m 0644 main/grout.service %{buildroot}%{_unitdir}/grout.service
install -D -m 0755 main/grout.bash-completion %{buildroot}%{_datadir}/bash-completion/completions/grout
install -D -m 0755 cli/grcli.bash-completion %{buildroot}%{_datadir}/bash-completion/completions/grcli

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%files
%doc README.md
%license licenses/BSD-3-clause.txt
%config(noreplace) %{_sysconfdir}/default/grout
%config(noreplace) %{_sysconfdir}/grout.init
%attr(644, root, root) %{_unitdir}/grout.service
%attr(755, root, root) %{_datadir}/bash-completion/completions/grout
%attr(755, root, root) %{_datadir}/bash-completion/completions/grcli
%attr(755, root, root) %{_bindir}/grcli
%attr(755, root, root) %{_bindir}/grout
%attr(644, root, root) %{_mandir}/man1/grcli*
%attr(644, root, root) %{_mandir}/man7/grout-frr.7*
%attr(644, root, root) %{_mandir}/man8/grout.8*

%files devel
%doc README.md
%license licenses/BSD-3-clause.txt
%{_includedir}/gr_*.h

%changelog
%autochangelog
