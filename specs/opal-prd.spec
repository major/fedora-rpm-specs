%global project skiboot

Name:		opal-prd
Version:	7.1
Release:	6%{?dist}
Summary:	OPAL Processor Recovery Diagnostics Daemon

License:	Apache-2.0
URL:		http://github.com/open-power/skiboot

# Presently opal-prd is supported on ppc64le architecture only.
ExclusiveArch:	ppc64le

BuildRequires:	systemd
BuildRequires:	openssl
BuildRequires:	gcc
BuildRequires:	openssl-devel
BuildRequires:	python3-devel

Requires(post):	systemd
Requires(preun):	systemd
Requires(postun):	systemd

Source0: https://github.com/open-power/%{project}/archive/v%{version}/%{project}-%{version}.tar.gz
Source1: opal-prd-rsyslog
Source2: opal-prd-logrotate
Source3: ffspart.man

# Annocheck FAIL: bind-now fortify pie
Patch0: opal-prd-ffspart-annocheck.patch

%description
This package provides a daemon to load and run the OpenPower firmware's
Processor Recovery Diagnostics binary. This is responsible for run time
maintenance of OpenPower Systems hardware.


%package -n	opal-utils
Summary:	OPAL firmware utilities

%description -n opal-utils
This package contains utility programs.

The 'gard' utility, can read, parse and clear hardware gard partitions
on OpenPower platforms. The 'getscom' and 'putscom' utilities provide
an interface to query or modify the registers of the different chipsets
of an OpenPower system. 'pflash' is a tool to access the flash modules
on such systems and update the OpenPower firmware.


%prep
%autosetup -p1 -n %{project}-%{version}


%build
OPAL_PRD_VERSION=%{version} make V=1 CC="gcc" CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}" ASFLAGS="-m64 -Wa,--generate-missing-build-notes=yes" -C external/opal-prd
GARD_VERSION=%{version}     make V=1 CC="gcc" CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}" -C external/gard
PFLASH_VERSION=%{version}   make V=1 CC="gcc" CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}" -C external/pflash
XSCOM_VERSION=%{version}    make V=1 CC="gcc" CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}" -C external/xscom-utils
FFSPART_VERSION=%{version}  make V=1 CC="gcc" CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}" -C external/ffspart


%install
OPAL_PRD_VERSION=%{version} make -C external/opal-prd install DESTDIR=%{buildroot} prefix=/usr
GARD_VERSION=%{version}     make -C external/gard install DESTDIR=%{buildroot} prefix=/usr
PFLASH_VERSION=%{version}   make -C external/pflash install DESTDIR=%{buildroot} prefix=/usr
XSCOM_VERSION=%{version}    make -C external/xscom-utils install DESTDIR=%{buildroot} prefix=/usr
FFSPART_VERSION=%{version}  make -C external/ffspart install DESTDIR=%{buildroot} prefix=/usr

mkdir -p %{buildroot}%{_unitdir}
install -m 644 -p external/opal-prd/opal-prd.service %{buildroot}%{_unitdir}/opal-prd.service

# log opal-prd messages to /var/log/opal-prd.log
mkdir -p %{buildroot}%{_sysconfdir}/{rsyslog.d,logrotate.d}
install -m 644 -p %{SOURCE1} %{buildroot}/%{_sysconfdir}/rsyslog.d/opal-prd.conf
install -m 644 -p %{SOURCE2} %{buildroot}/%{_sysconfdir}/logrotate.d/opal-prd

# install phberr script
install -D -p -m 644 external/pci-scripts/ppc.py %{buildroot}%{python3_sitelib}/ppc/__init__.py
install -D -p -m 755 external/pci-scripts/phberr.py %{buildroot}%{_bindir}/phberr

# install ffspart manpage
install -m 644 -p %{SOURCE3} %{buildroot}%{_mandir}/man1/ffspart.1

%post
%systemd_post opal-prd.service

%preun
%systemd_preun opal-prd.service

%postun
%systemd_postun_with_restart opal-prd.service


%files
%doc README.md
%license LICENCE
%config(noreplace) %{_sysconfdir}/logrotate.d/opal-prd
%config(noreplace) %{_sysconfdir}/rsyslog.d/opal-prd.conf
%{_sbindir}/opal-prd
%{_unitdir}/opal-prd.service
%{_mandir}/man8/*

%files -n opal-utils
%doc README.md
%license LICENCE
%{_bindir}/phberr
%{_sbindir}/opal-gard
%{_sbindir}/getscom
%{_sbindir}/putscom
%{_sbindir}/pflash
%{_sbindir}/getsram
%{_sbindir}/ffspart
%{python3_sitelib}/ppc/
%{_mandir}/man1/*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Apr 24 2024 Than Ngo <than@redhat.com> - 7.1-4
- fixed Annocheck FAIL: bind-now fortify pie

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Sep 19 2023 Than Ngo <than@redhat.com> - 7.1-1
- update to 7.1

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 10 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 7.0-6
- Rebuilt for Python 3.12

* Thu Feb 16 2023 Than Ngo <than@redhat.com> - 7.0-5
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 26 2021 Dan Horák <dan@danny.cz> - 7.0-1
- update to 7.0

* Thu Jul 22 2021 Dan Horák <dan@danny.cz> - 6.8.1-1
- update to 6.8.1

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 12 2021 Dan Horák <dan@danny.cz> - 6.8-2
- drop the firmware subpackage

* Mon May 31 2021 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 6.8-1
- update to 6.8 (#1965683)

* Wed May 26 2021 Than Ngo <than@redhat.com> - 6.7.1-4
- using stop instead ~ action as it's deprecated in rsyslog

* Mon May 10 2021 Than Ngo <than@redhat.com> - 6.7.1-3
- Add missing manpage for ffspart

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 07 2021 Dan Horák <dan@danny.cz> - 6.7.1-1
- update to 6.7.1 (#1913304)

* Tue Nov 03 2020 Dan Horák <dan@danny.cz> - 6.7-2
- install phberr script
- fix %%install to avoid recompilation

* Tue Nov 03 2020 Dan Horák <dan@danny.cz> - 6.7-1
- update to 6.7

* Fri Oct 23 2020 Dan Horák <dan@danny.cz> - 6.6.4-1
- update to 6.6.4 (#1890868)

* Thu Sep 10 2020 Dan Horák <dan@danny.cz> - 6.6.3-1
- update to 6.6.3

* Mon Aug 10 2020 Dan Horák <dan@danny.cz> - 6.6.2-3
- build and install ffspart
- add BR: openssl for skibot image signing

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 03 2020 Dan Horák <dan@danny.cz> - 6.6.2-1
- update to 6.6.2

* Tue Jun 09 2020 Dan Horák <dan@danny.cz> - 6.6.1-1
- update to 6.6.1

* Thu Apr 23 2020 Dan Horák <dan@danny.cz> - 6.6-1
- update to 6.6

* Fri Mar 20 2020 Dan Horák <dan@danny.cz> - 6.5.4-1
- update to 6.5.4

* Wed Mar 11 2020 Dan Horák <dan@danny.cz> - 6.5.3-1
- update to 6.5.3

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 12 2019 Dan Horák <dan@danny.cz> - 6.5.2-1
- update to 6.5.2

* Thu Oct 24 2019 Dan Horák <dan@danny.cz> - 6.5.1-1
- update to 6.5.1

* Mon Aug 19 2019 Dan Horák <dan@danny.cz> - 6.5-1
- update to 6.5

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 2019 Dan Horák <dan@danny.cz> - 6.4-1
- update to 6.4

* Fri May 24 2019 Than Ngo <than@redhat.com> - 6.3.1-1
- update to 6.3.1
- log messages to /var/log/opal-prd.log

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 20 2018 Than Ngo <than@redhat.com> - 6.2-2
- add man pages

* Thu Dec 20 2018 Than Ngo <than@redhat.com> - 6.2-1
- update to 6.2

* Thu Sep 27 2018 Than Ngo <than@redhat.com> - 6.1-4
- log opal-prd messages to /var/log/opal-prd.log

* Fri Sep 21 2018 Than Ngo <than@redhat.com> - 6.1-3
- Fixed opal-prd crash
- Fixed annocheck distro flag failures

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 12 2018 Dan Horák <dan@danny.cz> - 6.1-1
- Update to latest upstream 6.1

* Mon May 28 2018 Dan Horák <dan@danny.cz> - 6.0.4-1
- Update to latest upstream 6.0.4

* Thu May 17 2018 Dan Horák <dan@danny.cz> - 6.0.1-1
- Update to latest upstream 6.0.1

* Mon Apr 09 2018 Dan Horák <dan@danny.cz> - 5.11-1
- Update to latest upstream 5.11

* Mon Mar 12 2018 Than Ngo <than@redhat.com> - 5.10.2-1
- update to latest upstream 5.10.2

* Thu Mar 08 2018 Than Ngo <than@redhat.com> - 5.10.1-2
- fixed bz#1552650 - incomplete Fedora build flags injection

* Fri Mar 02 2018 Dan Horák <dan[at]danny.cz> - 5.10.1-1
- Update to latest upstream 5.10.1

* Wed Feb 28 2018 Dan Horák <dan[at]danny.cz> - 5.10-1
- Update to latest upstream 5.10

* Mon Feb 26 2018 Dan Horák <dan[at]danny.cz> - 5.9.8-3
- fix firmware build (#1545784)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Dan Horák <dan[at]danny.cz> - 5.9.8-1
- Update to latest upstream 5.9.8

* Fri Aug 4 2017 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 5.7.0-1
- Update to latest upstream 5.7.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 19 2017 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 5.5.0-2
- Fix build warning
- Include skiboot.lid.xz file

* Tue Apr 18 2017 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 5.5.0-1
- Update to latest upstream 5.5.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Mar 21 2016 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 5.2.0
- Update to latest upstream 5.2.0

* Fri Feb 26 2016 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 5.1.13-4
- Fix stack frame compilation issue on gcc6
- Remove ppc64 from ExclusiveArch list

* Mon Feb 22 2016 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 5.1.13-3
- Fix opal-prd recompilation issse during install

* Mon Feb 22 2016 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 5.1.13-2
- Added "Requires(post|preun|postun) tags"

* Tue Feb 09 2016 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 5.1.13
- Update to latest upstream 5.1.13
- Fixed specfile based on Dan's review comment (#1284527)

* Wed Nov 25 2015 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 5.1.11-4
- Fixed specfile based on Dan's review comment (#1284527)

* Tue Nov 24 2015 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 5.1.11-3
- Consistent use of build macros
- Removed defattr from files section

* Tue Nov 24 2015 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 5.1.11-2
- Minor update to spec file

* Mon Nov 23 2015 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 5.1.11
- Initial Fedora packaging
