%{?python_enable_dependency_generator}

%global modulenames     ec2hibernatepolicy
%global selinuxtype     targeted
%global moduletype      services
%global project         amazon-ec2-hibinit-agent

# Usage: _format var format
#   Expand 'modulenames' into various formats as needed
#   Format must contain '$x' somewhere to do anything useful
%global _format() export %1=""; for x in %{modulenames}; do %1+=%2; %1+=" "; done;

Name:           ec2-hibinit-agent
Version:        1.0.9
Release:        8%{?dist}
Summary:        Hibernation setup utility for Amazon EC2

License:        Apache-2.0
URL:            https://github.com/aws/amazon-%{name}
Source0:        https://github.com/aws/%{project}/archive/v%{version}/%{name}-%{version}.tar.gz

# Ensure swapon with maximum priority before hibernation
# Upstream Patch: https://github.com/aws/amazon-ec2-hibinit-agent/pull/49)
Patch1:         0001-swapon-with-maximum-priority-before-hibernation.patch
Patch2:         0002-rhel-fix-swapoff-breaks-hibernate-process.patch

BuildArch:  noarch

BuildRequires: make
BuildRequires: systemd-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: selinux-policy
BuildRequires: selinux-policy-devel

%{?selinux_requires}
Requires: acpid 
Requires: grubby 
Requires: systemd 
Requires: tuned

%description
An EC2 agent that creates a setup for instance hibernation

%prep
%autosetup -p1 -n %{project}-%{version}
# Fix build with setuptools 62.1
# https://github.com/aws/amazon-ec2-hibinit-agent/issues/24
sed -i "20i packages=[]," setup.py
 
%build
%py3_build

# Makefile generates pp.bz2 from .tt file. 
# Generating tt file https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/selinux_users_and_administrators_guide/security-enhanced_linux-the-sepolicy-suite-sepolicy_generate
make -C %{_builddir}/%{project}-%{version}/packaging/rhel/ec2hibernatepolicy

%install
%py3_install

mkdir -p %{buildroot}%{python3_sitelib}
mkdir -p "%{buildroot}%{_unitdir}"
mkdir -p %{buildroot}%{_sysconfdir}/acpi/events 
mkdir -p %{buildroot}%{_sharedstatedir}/hibinit-agent
mkdir -p %{buildroot}%{_sysconfdir}/acpi/actions

install -p -m 644 "%{_builddir}/%{project}-%{version}/hibinit-agent.service" %{buildroot}%{_unitdir}
install -p -m 644 "%{_builddir}/%{project}-%{version}/acpid.sleep.conf" %{buildroot}%{_sysconfdir}/acpi/events/sleepconf

mkdir -p %{buildroot}%{_prefix}/lib/systemd/logind.conf.d
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system-sleep

install -p -m 644 "%{_builddir}/%{project}-%{version}/etc/hibinit-config.cfg" %{buildroot}/%{_sysconfdir}/hibinit-config.cfg
install -p -m 644 "%{_builddir}/%{project}-%{version}/packaging/rhel/00-hibinit-agent.conf" %{buildroot}%{_prefix}/lib/systemd/logind.conf.d/00-hibinit-agent.conf
install -p -m 755 "%{_builddir}/%{project}-%{version}/packaging/rhel/acpid.sleep.sh" %{buildroot}%{_sysconfdir}/acpi/actions/sleep.sh
install -p -m 755 "%{_builddir}/%{project}-%{version}/packaging/rhel/sleep-handler.sh" %{buildroot}%{_prefix}/lib/systemd/system-sleep/sleep-handler.sh

#Disable transparent huge page
mkdir -p  %{buildroot}%{_sysconfdir}/tuned/nothp_profile
install -p -m 644 "%{_builddir}/%{project}-%{version}/packaging/rhel/tuned.conf" %{buildroot}%{_sysconfdir}/tuned/nothp_profile/tuned.conf

# Install policy modules
%_format MODULES $x.pp.bz2
install -d %{buildroot}%{_datadir}/selinux/packages
install -m 0644 %{_builddir}/%{project}-%{version}/packaging/rhel/ec2hibernatepolicy/$MODULES \
        %{buildroot}%{_datadir}/selinux/packages


%files
%doc README.md
%license LICENSE.txt

%config(noreplace) %{_sysconfdir}/hibinit-config.cfg
%{_unitdir}/hibinit-agent.service
%{_bindir}/hibinit-agent
%config(noreplace) %{_sysconfdir}/acpi/events/sleepconf
%config(noreplace) %{_sysconfdir}/acpi/actions/sleep.sh
%{python3_sitelib}/ec2_hibinit_agent-*.egg-info/
%dir %{_sharedstatedir}/hibinit-agent
%ghost %attr(0600,root,root) %{_sharedstatedir}/hibinit-agent/hibernation-enabled

%dir %{_prefix}/lib/systemd/logind.conf.d
%dir %{_prefix}/lib/systemd/system-sleep

%dir %{_sysconfdir}/tuned/nothp_profile
%config(noreplace) %{_sysconfdir}/tuned/nothp_profile/tuned.conf

%{_prefix}/lib/systemd/system-sleep/sleep-handler.sh
%{_prefix}/lib/systemd/logind.conf.d/00-hibinit-agent.conf
%attr(0644,root,root) %{_datadir}/selinux/packages/*.pp.bz2

%pre
%selinux_relabel_pre -s %{selinuxtype}

%post
%systemd_post hibinit-agent.service

#
# Install all modules in a single transaction
#
%_format MODULES %{_datadir}/selinux/packages/$x.pp.bz2
%selinux_modules_install -s %{selinuxtype} $MODULES

#
# Disable THP by switching to nothp_profile profile
#
tuned-adm profile nothp_profile


%preun
%systemd_preun hibinit-agent.service


%postun
%systemd_postun_with_restart hibinit-agent.service

#
# Enable THP
#
tuned-adm profile virtual-guest

# https://fedoraproject.org/wiki/SELinux/IndependentPolicy
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} $MODULES
fi


%posttrans
%selinux_relabel_post -s %{selinuxtype}

%changelog
* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jun 03 2025 Python Maint <python-maint@redhat.com> - 1.0.9-7
- Rebuilt for Python 3.14

* Tue Mar 18 2025 Frank Liang <xiliang@redhat.com> - 1.0.9-6
- Include upstream Patch to fix swapoff breaks hibernate process

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Nov 08 2024 Dominik Wombacher <dominik@wombacher.cc> - 1.0.9-4
- Include upstream Patch to ensure swapon with maximum priority before hibernation
- Resolves rhbz#2322884

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.0.9-2
- Rebuilt for Python 3.13

* Sun Jun 02 2024 Packit <hello@packit.dev> - 1.0.9-1
- Update to version 1.0.9

* Mon Apr 8 2024 Dominik Wombacher <dominik@wombacher.cc> - 1.0.8-1
- Update to 1.0.8
- migrated to SPDX license

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 1.0.5-2
- Rebuilt for Python 3.12

* Tue Apr 25 2023 David Duncan <<davdunc@amazon.com>> - 1.0.5-1
- Ensure we swapon the hibinit swapfile with the highest priority

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 21 2022 Lumír Balhar <lbalhar@redhat.com> - 1.0.4-5
- Fix compatibility with newer setuptools

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 1.0.4-4
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 01 2021 David Duncan <davdunc@amazon.com> - 1.0.4-1
- Update to v1.0.4

* Sat Jun 05 2021 Python Maint <python-maint@redhat.com> - 1.0.3-8
- Rebuilt for Python 3.10

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.0.3-7
- Rebuilt for Python 3.10

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.3-6
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 21 17:27:18 UTC 2021 David Duncan <davdunc@amazon.com> - 1.0.3-4
- Add BuildRequires: make, FESCo issue: #2500

* Tue Nov 03 2020 Mohamed Aboubakr <mabouba@amazon.com> - 1.0.3-3
- Moving selinux folder in packaging directory.
- Use make file to generate .pp.bz2 file

* Fri Oct 02 2020 David Duncan <davdunc@amazon.com> - 1.0.3-2
- Modify Spec for build requirements

* Thu Aug 13 2020 Mohamed Aboubakr <mabouba@amazon.com> - 1.0.3-1
- Support Redhat and Fedora by adding sepolicy
- Ignore handle hibernation in systemd configuration

* Fri Jan 24 2020 Frederick Lefebvre <fredlef@amazon.com> - 1.0.1-2
- Restart the hibinit-agent service on upgrade

* Thu Jan 23 2020 Frederick Lefebvre <fredlef@amazon.com> - 1.0.1-1
- Added IMDSv2 support
- Renamed spec file to match the actual package name

* Fri Jun 14 2019 Anchal Agarwal <anchalag@amazon.com> - 1.0.0-4
- Added hibernation re-try logic in case of hibernation failure

* Wed Nov 07 2018 Matt Dees <mattdees@amazon.com> - 1.0.0-2
- Clean up hibernation configured check

* Wed Oct 31 2018 Anchal Agarwal <anchalag@amazon.com> - 1.0.0-1
- Initial build
