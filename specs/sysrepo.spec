Name: sysrepo
Version: 2.2.12
Release: 7%{?dist}
Summary: YANG-based configuration and operational data store
Url: https://github.com/sysrepo/sysrepo
Source: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source2: sysrepo.sysusers
Source3: sysrepo-plugind.sysusers
Source4: sysrepo-plugind.service
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(libyang) >= 2.0.7
# for tests
BuildRequires:  pkgconfig(cmocka)
# for sysrepo-plugind systemd support
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  systemd-rpm-macros


%package devel
Summary:   Development files for sysrepo
Requires:  %{name}%{?_isa} = %{version}-%{release}
Requires:  pkgconfig

%package plugind
Summary:   sysrepo plugin daemon
Requires:  %{name}%{?_isa} = %{version}-%{release}

%package tools
Summary:   sysrepo executable tools
Requires:  %{name}%{?_isa} = %{version}-%{release}


%description
YANG-based configuration and operational data store - runtime Applications can
use sysrepo to store their configuration modeled by provided YANG model
instead of using e.g. flat configuration files. Sysrepo will ensure data
consistency of the data stored in the data store and enforce data constraints
defined by YANG model.

The library is implemented in C and provides an API for other software
to use for accessing sysrepo datastore.

%description devel
Headers of sysrepo library.

%description plugind
Sysrepo plugin daemon and service.

%description tools
Executable tools for sysrepo:

* sysrepoctl - manipulation of YANG modules (schemas)
* sysrepocfg - manipulation of YANG instance data


%prep
%autosetup -p1

%build
%cmake -DCMAKE_BUILD_TYPE=RELWITHDEBINFO -DSYSREPO_UMASK=007 -DSYSREPO_GROUP=sysrepo -DNACM_SRMON_DATA_PERM=660
%cmake_build

%install
%cmake_install
install -D -p -m 0644 %{SOURCE2} %{buildroot}%{_sysusersdir}/sysrepo.conf
install -D -p -m 0644 %{SOURCE3} %{buildroot}%{_sysusersdir}/sysrepo-plugind.conf
install -D -p -m 0644 %{SOURCE4} %{buildroot}%{_unitdir}/sysrepo-plugind.service
mkdir -p -m=770 %{buildroot}%{_sysconfdir}/sysrepo

%pre
%if 0%{?fedora}
    %sysusers_create_compat %{SOURCE2}
%else
    getent group sysrepo 1>/dev/null || groupadd -r sysrepo
%endif

%postun
# sysrepo apps shared memory
rm -rf /dev/shm/sr_*
rm -rf /dev/shm/srsub_*

%pre plugind
%if 0%{?fedora}
    %sysusers_create_compat %{SOURCE3}
%else
    getent passwd sysrepo-plugind 1>/dev/null || useradd -r -M -s /sbin/nologin -c "sysrepo plugind user" -g sysrepo sysrepo-plugind
%endif

%post plugind
%systemd_post %{name}-plugind.service

%postun plugind
%systemd_postun_with_restart %{name}-plugind.service


%files
%license LICENSE
%doc README.md
%{_sysusersdir}/sysrepo.conf
%{_libdir}/libsysrepo.so.7*
%attr(0770,root,sysrepo) %{_sysconfdir}/sysrepo

%files devel
%{_libdir}/libsysrepo.so
%{_libdir}/pkgconfig/sysrepo.pc
%{_includedir}/sysrepo*.h
%{_includedir}/sysrepo/*.h
%dir %{_includedir}/sysrepo/

%files plugind
%{_unitdir}/sysrepo-plugind.service
%{_sysusersdir}/sysrepo-plugind.conf
%{_bindir}/sysrepo-plugind
%{_datadir}/man/man8/sysrepo-plugind.8.gz
%dir %{_libdir}/sysrepo-plugind/plugins

%files tools
%{_bindir}/sysrepocfg
%{_bindir}/sysrepoctl
%{_datadir}/man/man1/sysrepocfg.1.gz
%{_datadir}/man/man1/sysrepoctl.1.gz


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 4 2024 Miroslav Suchý <msuchy@redhat.com> - 2.2.12-6
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 15 2022 Jakub Ružička <jakub.ruzicka@nic.cz> - 2.2.12-1
- New version

* Fri Jul 29 2022 Jakub Ružička <jakub.ruzicka@nic.cz> - 2.1.84-1
- New version

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.64-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 11 2022 Jakub Ružička <jakub.ruzicka@nic.cz> - 2.1.64-1
- New version (Closes: rhbz#2042998)
- Improve *.so file pattern
- Create /etc/sysrepo in install, not post
- Sync small upstream improvements

* Thu Apr 14 2022 Jakub Ružička <jakub.ruzicka@nic.cz> - 2.1.42-2
- Improved users and service handling.

* Mon Mar 28 2022 Jakub Ružička <jakub.ruzicka@nic.cz> - 2.1.42-1
- New version
- Add sysrepo-plugind sub-package and service
- Reorder .spec for clarity

* Thu Jan 20 2022 Jakub Ružička <jakub.ruzicka@nic.cz> - 2.0.53-1
- Initial packaging
