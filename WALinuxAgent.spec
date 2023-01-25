%global with_legacy 0
%global dracut_modname 97walinuxagent

Name:           WALinuxAgent
Version:        2.8.0.11
Release:        3%{?dist}
Summary:        The Microsoft Azure Linux Agent

License:        ASL 2.0
URL:            https://github.com/Azure/%{name}
Source0:        https://github.com/Azure/%{name}/archive/v%{version}.tar.gz
Source1:        module-setup.sh

Patch0:         0001-Rudimentary-Fedora-OS-implementation.patch
Patch1:         0001-waagent.service-set-ConditionVirtualization-microsof.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-distro
Requires:       %name-udev = %version-%release
%if 0%{?fedora}
Requires:       ntfsprogs
%endif
Requires:       openssh
Requires:       openssh-server
Requires:       openssl
Requires:       parted
Requires:       python3-pyasn1
Requires:       iptables

BuildRequires:   systemd
Requires(post):  systemd
Requires(preun): systemd
Requires(postun): systemd

%description
The Microsoft Azure Linux Agent supports the provisioning and running of Linux
VMs in the Microsoft Azure cloud. This package should be installed on Linux disk
images that are built to run in the Microsoft Azure environment.

%if 0%{?with_legacy}
%package legacy
Summary:        The Microsoft Azure Linux Agent (legacy)
Requires:       %name = %version-%release
Requires:       python2
Requires:       net-tools

%description legacy
The Microsoft Azure Linux Agent supporting old version of extensions.
%endif

%package udev
Summary:        Udev rules for Microsoft Azure

%description udev
Udev rules specific to Microsoft Azure Virtual Machines.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%py3_build

%install
%{__python3} setup.py install -O1 --skip-build --root %{buildroot} --lnx-distro redhat

mkdir -p -m 0700 %{buildroot}%{_sharedstatedir}/waagent
mkdir -p %{buildroot}%{_localstatedir}/log
touch %{buildroot}%{_localstatedir}/log/waagent.log

mkdir -p %{buildroot}%{_udevrulesdir}
mv %{buildroot}%{_sysconfdir}/udev/rules.d/*.rules %{buildroot}%{_udevrulesdir}/

rm -rf %{buildroot}/%{python3_sitelib}/tests
rm -rf %{buildroot}/%{python3_sitelib}/__main__.py
rm -rf %{buildroot}/%{python3_sitelib}/__pycache__/__main__*.py*

sed -i 's,#!/usr/bin/env python,#!/usr/bin/python3,' %{buildroot}%{_sbindir}/waagent
%if 0%{?with_legacy}
sed -i 's,#!/usr/bin/env python,#!/usr/bin/python2,' %{buildroot}%{_sbindir}/waagent2.0
%else
rm -f %{buildroot}%{_sbindir}/waagent2.0
%endif
sed -i 's,/usr/bin/python ,/usr/bin/python3 ,' %{buildroot}%{_unitdir}/waagent.service

mv %{buildroot}%{_sysconfdir}/logrotate.d/waagent.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

install -m0755 -D -t %{buildroot}%{_prefix}/lib/dracut/modules.d/%{dracut_modname}/ %{SOURCE1}

%post
%systemd_post waagent.service

%preun
%systemd_preun waagent.service

%postun
%systemd_postun_with_restart waagent.service

%files
%doc LICENSE.txt NOTICE README.md
%ghost %{_localstatedir}/log/waagent.log
%dir %attr(0700, root, root) %{_sharedstatedir}/waagent
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%{_sbindir}/waagent
%config(noreplace) %{_sysconfdir}/waagent.conf
%{_unitdir}/waagent.service
%{_unitdir}/azure.slice
%{_unitdir}/azure-vmextensions.slice
%{python3_sitelib}/azurelinuxagent
%{python3_sitelib}/*.egg-info

%files udev
%{_udevrulesdir}/*.rules
%{_prefix}/lib/dracut/modules.d/%{dracut_modname}/*.sh

%if 0%{?with_legacy}
%files legacy
%{_sbindir}/waagent2.0
%endif

%changelog
* Fri Jan 20 2023 Dusty Mabe <dusty@dustymabe.com> - 2.8.0.11-3
- Move module-setup.sh into git

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Oct 31 2022 Vitaly Kuznetsov <vkuznets@redhat.com> - 2.8.0.11-1
- Update to 2.8.0.11 (#2128547)

* Tue Oct 18 2022 Chris Patterson <cpatterson@microsoft.com> - 2.7.3.0-2
- Add ConditionVirtualization=|microsoft triggering condition

* Wed Aug 03 2022 Vitaly Kuznetsov <vkuznets@redhat.com> - 2.7.3.0-1
- Update to 2.7.3.0 (#2110155)

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 30 2022 Vitaly Kuznetsov <vkuznets@redhat.com> - 2.7.1.0-1
- Update to 2.7.1.0 (#2097244)

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.7.0.6-2
- Rebuilt for Python 3.11

* Fri Apr 22 2022 Vitaly Kuznetsov <vkuznets@redhat.com> - 2.7.0.6-1
- Update to 2.7.0.6 (#2040980)

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 03 2022 Vitaly Kuznetsov <vkuznets@redhat.com> - 2.5.0.2-1
- Update to 2.5.0.2 (#2008699)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 19 2021 Vitaly Kuznetsov <vkuznets@redhat.com> - 2.3.1.1-1
- Update to 2.3.1.1 (#1982512)
- Require iptables for setting up persistent firewall rules

* Tue Jun 15 2021 Vitaly Kuznetsov <vkuznets@redhat.com> - 2.3.0.2-1
- Update to 2.3.0.2 (#1971116)

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.2.54.2-2
- Rebuilt for Python 3.10

* Fri May 21 2021 Vitaly Kuznetsov <vkuznets@redhat.com> - 2.2.54.2-1
- Update to 2.2.54.2 (#1916966)

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.2.52-6
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Fri Feb 19 2021 Vitaly Kuznetsov <vkuznets@redhat.com> - 2.2.52-5
- Require ntfsprogs on Fedora only 

* Tue Jan 26 2021 Vitaly Kuznetsov <vkuznets@redhat.com> - 2.2.52-4
- Fix distro resolution for RedHat

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.52-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 15 2021 Vitaly Kuznetsov <vkuznets@redhat.com> - 2.2.52-2
- Add udev rules to initramfs (#1909287)

* Wed Dec 09 2020 Vitaly Kuznetsov <vkuznets@redhat.com> - 2.2.52-1
- Update to 2.2.52 (#1849923)
- Add not yet upstream patches supporting Python3.9 changes

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.48.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 09 2020 Vitaly Kuznetsov <vkuznets@redhat.com> - 2.2.48.1-1
- Update to 2.2.48.1 (#1641605)
- Split udev rules to a separate subpackage (#1748432)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.2.46-2
- Rebuilt for Python 3.9

* Wed Apr 15 2020 Vitaly Kuznetsov <vkuznets@redhat.com> - 2.2.46-1
- Update to 2.2.46

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.40-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.40-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Wed Aug 21 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.40-5
- Rebuilt for Python 3.8

* Wed Aug 21 2019 Vitaly Kuznetsov <vkuznets@redhat.com> - 2.2.40-4
- Disable Python2 dependent 'legacy' subpackage (#1741029)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.40-3
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 03 2019 Vitaly Kuznetsov <vkuznets@redhat.com> - 2.2.40-1
- Update to 2.2.40
- Fix FTBFS in the preparation for Python3.8 (#1705219)

* Thu Mar 14 2019 Vitaly Kuznetsov <vkuznets@redhat.com> - 2.2.38-1
- Update to 2.2.38 (CVE-2019-0804)

* Thu Mar 14 2019 Vitaly Kuznetsov <vkuznets@redhat.com> - 2.2.37-1
- Update to 2.2.37

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 20 2018 Vitaly Kuznetsov <vkuznets@redhat.com> - 2.2.32-1
- Update to 2.2.32.2

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.25-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.2.25-3
- Rebuilt for Python 3.7

* Wed Apr 25 2018 Vitaly Kuznetsov <vkuznets@redhat.com> - 2.2.25-2
- Move net-tools dependency to WALinuxAgent-legacy (#1106781)

* Mon Apr 16 2018 Vitaly Kuznetsov <vkuznets@redhat.com> - 2.2.25-1
- Update to 2.2.25
- Switch to Python3
- Legacy subpackage with waagent2.0 supporting old extensions

* Wed Feb 28 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.0.18-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Apr 02 2016 Scott K Logan <logans@cottsay.net> - 2.0.18-1
- Update to 2.0.18

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul 02 2015 Scott K Logan <logans@cottsay.net> - 2.0.14-1
- Update to 2.0.14

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 01 2015 Scott K Logan <logans@cottsay.net> - 2.0.13-1
- Update to 2.0.13

* Thu Apr 02 2015 Scott K Logan <logans@cottsay.net> - 2.0.12-1
- Update to 2.0.12-Oracle

* Sat Jan 10 2015 Scott K Logan <logans@cottsay.net> - 2.0.11-2
- Use systemd for rhel7
- Own logrotate.d
- Fix python2-devel dep

* Sat Dec 20 2014 Scott K Logan <logans@cottsay.net> - 2.0.11-1
- Initial package
