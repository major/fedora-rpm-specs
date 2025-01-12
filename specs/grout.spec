# SPDX-License-Identifier: BSD-3-Clause
# Copyright (c) 2025 Robin Jarry

%global _lto_cflags %nil
%global forgeurl https://github.com/DPDK/grout

Name: grout
Version: 0.5
Summary: Graph router based on DPDK
License: BSD-3-Clause
Group: System Environment/Daemons

%forgemeta

URL: %{forgeurl}
Release: %{autorelease}
Source: %{forgesource}

BuildRequires: dpdk-devel >= 24.11.1-2
BuildRequires: gcc
BuildRequires: libcmocka-devel
BuildRequires: libecoli-devel >= 0.4.0-2
BuildRequires: libevent-devel
BuildRequires: libsmartcols-devel
BuildRequires: make
BuildRequires: meson
BuildRequires: ninja-build
BuildRequires: numactl-devel
BuildRequires: pkgconf
BuildRequires: scdoc
BuildRequires: socat
BuildRequires: systemd

# No point in running a DPDK application on 32 bit x86: see fedora#2336884
ExcludeArch: i686
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

%build
%meson
%meson_build

%check
%meson_test

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
%license LICENSE
%config(noreplace) %{_sysconfdir}/default/grout
%config(noreplace) %{_sysconfdir}/grout.init
%attr(644, root, root) %{_unitdir}/grout.service
%attr(755, root, root) %{_datadir}/bash-completion/completions/grout
%attr(755, root, root) %{_datadir}/bash-completion/completions/grcli
%attr(755, root, root) %{_bindir}/grcli
%attr(755, root, root) %{_sbindir}/grout
%attr(644, root, root) %{_mandir}/man1/grcli.1*
%attr(644, root, root) %{_mandir}/man8/grout.8*

%files devel
%doc README.md
%license LICENSE
%{_includedir}/gr_*.h

%changelog
%autochangelog
