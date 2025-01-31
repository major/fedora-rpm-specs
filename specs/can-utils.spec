Name:		can-utils
Version:	2025.01
Release:	1%{?dist}
Summary:	SocketCAN user space utilities and tools

# most utilities are dual-licensed but some are GPLv2 only
# Automatically converted from old format: GPLv2 and (GPLv2 or BSD) - review is highly recommended.
License:	GPL-2.0-only AND (GPL-2.0-only OR LicenseRef-Callaway-BSD)
URL:		https://github.com/linux-can/can-utils
Source0:	https://github.com/linux-can/can-utils/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Use this to extract new snapshots from upstream git repo
Source1:	can-snapshot.sh

BuildRequires:	cmake
BuildRequires:	gcc
BuildRequires:	glibc-devel

%description
CAN is a message-based network protocol designed for vehicles originally
created by Robert Bosch GmbH. SocketCAN is a set of open source CAN
drivers and a networking stack contributed by Volkswagen Research to
the Linux kernel.

This package contains some user space utilities for Linux SocketCAN subsystem.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Development file for %{name}.

%prep
%autosetup -p1

%build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_libdir}
%cmake_build

# Extract the dual license from one of the sources
head -39 asc2log.c | tail -37 | cut -c4- > COPYING

%install
%cmake_install

%files
%license COPYING
%doc README.md
%{_bindir}/asc2log
%{_bindir}/bcmserver
%{_bindir}/can-calc-bit-timing
%{_bindir}/canbusload
%{_bindir}/candump
%{_bindir}/canfdtest
%{_bindir}/cangen
%{_bindir}/cangw
%{_bindir}/canlogserver
%{_bindir}/canplayer
%{_bindir}/cansend
%{_bindir}/cansequence
%{_bindir}/cansniffer
%{_bindir}/isotpdump
%{_bindir}/isotpperf
%{_bindir}/isotprecv
%{_bindir}/isotpsend
%{_bindir}/isotpserver
%{_bindir}/isotpsniffer
%{_bindir}/isotptun
%{_bindir}/j1939acd
%{_bindir}/j1939cat
%{_bindir}/j1939spy
%{_bindir}/j1939sr
%{_bindir}/j1939-timedate-cli
%{_bindir}/j1939-timedate-srv
%{_bindir}/log2asc
%{_bindir}/log2long
%{_bindir}/mcp251xfd-dump
%{_bindir}/slcan_attach
%{_bindir}/slcand
%{_bindir}/slcanpty
%{_bindir}/testj1939

%files devel
%{_bindir}/isobusfs-cli
%{_bindir}/isobusfs-srv
%{_includedir}/isobusfs*
%{_libdir}/libisobusfs*.so

%changelog
* Wed Jan 29 2025 Peter Robinson <pbrobinson@fedoraproject.org> - 2025.01-1
- Update to 2025.01

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2023.03-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug  28 2024 Miroslav Suchý <msuchy@redhat.com> - 2023.03-5
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2023.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2023.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2023.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 14 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 2023.03-1
- Update to 2023.03

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2021.08.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2021.08.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2021.08.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2021.08.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Aug 22 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 2021.08.0-1
- Update to 2021.08.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan  3 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 2020.12.0-1
- Update to 2020.12.0

* Mon Nov  9 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 2020.11.0-1
- Update to 2020.11.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2020.02.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb 22 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 2020.02.04-1
- Update to 2020.02.04

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2018.02.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.02.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.02.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2018.02.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Peter Robinson <pbrobinson@fedoraproject.org> 2018.02.0-1
- Upstream 2018.02.0 release

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20170830git-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 24 2017 Panu Matilainen <pmatilai@redhat.com> - 20170830git-1
- New snapshot from upstream
- Package README.md file now that it has somewhat meaningful content

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20160229git-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20160229git-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20160229git-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Apr 14 2016 Panu Matilainen <pmatilai@redhat.com> - 20160229git-1
- Initial packaging
