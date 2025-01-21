%global __cmake_in_source_build 1

Name:           tcmu-runner
# Automatically converted from old format: LGPLV2+ or ASL 2.0 - review is highly recommended.
License:        LGPL-2.1-or-later OR Apache-2.0
Summary:        A daemon that supports LIO userspace backends
Version:        1.5.4
Release:        11%{?dist}
URL:            https://github.com/open-iscsi/tcmu-runner
Source:         https://github.com/open-iscsi/tcmu-runner/archive/v%{version}.tar.gz
Patch0:         read_conf.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  cmake glib2-devel libnl3-devel glusterfs-api-devel kmod-devel zlib-devel librbd-devel
BuildRequires:  gperftools-devel systemd
Requires:       targetcli
# Ceph/librbd does not have 32bit builds so we cannot either
ExcludeArch:	i686 armv7hl

%description
A daemon that handles the complexity of the LIO kernel target's userspace
passthrough interface (TCMU). It presents a C plugin API for extension modules
that handle SCSI requests in ways not possible or suitable to be handled
by LIO's in-kernel backstores.

%package -n libtcmu
Summary:        A library to ease supporting LIO userspace processing

%description -n libtcmu
libtcmu provides a library for processing SCSI commands exposed by the
LIO kernel target's TCM-User backend.

%package -n libtcmu-devel
Summary:        Development headers for libtcmu
Requires:       %{name} = %{version}-%{release}

%description -n libtcmu-devel
Development header(s) for developing against libtcmu.

%prep
%setup -q
%patch -P0 -p1

%build
%cmake -DSUPPORT_SYSTEMD=ON .
make %{?_smp_mflags}
gzip --stdout tcmu-runner.8 > tcmu-runner.8.gz

%install
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_mandir}/man8/
install -m 644 tcmu-runner.8.gz %{buildroot}%{_mandir}/man8/
mkdir -p %{buildroot}%{_includedir}
cp -a libtcmu.h libtcmu_common.h libtcmu_log.h tcmu-runner.h %{buildroot}%{_includedir}/

%ldconfig_scriptlets -n libtcmu

%files
%{_bindir}/tcmu-runner
%dir %{_libdir}/tcmu-runner
%{_libdir}/tcmu-runner/*
%{_sysconfdir}/dbus-1/system.d/tcmu-runner.conf
%{_datarootdir}/dbus-1/system-services/org.kernel.TCMUService1.service
%{_unitdir}/tcmu-runner.service
%{_sysconfdir}/logrotate.d/tcmu-runner
%dir %{_sysconfdir}/tcmu/
%config %{_sysconfdir}/tcmu/tcmu.conf
%doc README.md
%license LICENSE.*
%{_mandir}/man8/tcmu-runner.8.gz


%files -n libtcmu
%{_libdir}/*.so.*

%files -n libtcmu-devel
%{_includedir}/libtcmu.h
%{_includedir}/libtcmu_common.h
%{_includedir}/libtcmu_log.h
%{_includedir}/tcmu-runner.h
%{_libdir}/*.so


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.5.4-10
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 24 2021 Maurizio Lombardi <mlombard@redhat.com> - 1.5.4-2
- Fix possible infinite loop when reading the config file

* Mon May 17 2021 Maurizio Lombardi <mlombard@redhat.com> - 1.5.4-1
- Update to version 1.5.4

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 25 2021 Maurizio Lombardi
- Add fix for CVE-2020-28374

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 Jeff Law <law@redhat.com> - 1.5.2-3
- Use __cmake_in_source_build

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 20 2019 Tom Callaway <spot@fedoraproject.org> - 1.5.2-1
- update to 1.5.2

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Oct 26 2016 Andy Grover <agrover@redhat.com> - 1.1.3-1
- New upstream version

* Mon Aug 15 2016 Andy Grover <agrover@redhat.com> - 1.1.1-1
- New upstream version
- include tcmu-runner.h in -devel

* Wed Aug 3 2016 Andy Grover <agrover@redhat.com> - 1.1.0-1
- New upstream version
- Don't install tcmu-synthesizer, it's an example program

* Wed Apr 6 2016 Andy Grover <agrover@redhat.com> - 1.0.4-1
- New upstream version
- Add man page for tcmu-runner

* Wed Mar 30 2016 Andy Grover <agrover@redhat.com> - 1.0.3-1
- New upstream version

* Thu Mar 24 2016 Andy Grover <agrover@redhat.com> - 1.0.2-1
- New upstream version

* Fri Mar 18 2016 Andy Grover <agrover@redhat.com> - 1.0.1-1
- New upstream version

* Mon Mar 7 2016 Andy Grover <agrover@redhat.com> - 1.0.0-1
- New upstream version
- Add libtcmu and libtcmu-devel subpackages

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 14 2015 Andy Grover <agrover@redhat.com> - 0.9.2-1
- New upstream version

* Tue Oct 13 2015 Andy Grover <agrover@redhat.com> - 0.9.1-1
- Initial Fedora packaging
