%global dracut_modname 97walinuxagent

Name:           WALinuxAgent
Version:        2.15.0.1
Release:        %autorelease
Summary:        The Microsoft Azure Linux Agent

License:        Apache-2.0
URL:            https://github.com/Azure/%{name}
Source0:        https://github.com/Azure/%{name}/archive/v%{version}.tar.gz
Source1:        module-setup.sh

Patch1:         0001-waagent.service-set-ConditionVirtualization-microsof.patch

BuildArch:      noarch

BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-setuptools
BuildRequires:  python3-distro
BuildRequires:  python3-crypt-r

Requires:       %name-udev = %version-%release
%if 0%{?fedora}
Requires:       ntfsprogs
%endif
Requires:       openssh
Requires:       openssh-server
Requires:       openssl
Requires:       parted
# We need to manually require this for now since upstream
# still uses crypt (removed in Python 3.13)
Requires:       python3-crypt-r
Requires:       iptables
Requires:       logrotate

BuildRequires:   systemd
Requires(post):  systemd
Requires(preun): systemd
Requires(postun): systemd

%description
The Microsoft Azure Linux Agent supports the provisioning and running of Linux
VMs in the Microsoft Azure cloud. This package should be installed on Linux disk
images that are built to run in the Microsoft Azure environment.

%package udev
Summary:        Udev rules for Microsoft Azure

%description udev
Udev rules specific to Microsoft Azure Virtual Machines.

%prep
%autosetup -n %{name}-%{version} -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files azurelinuxagent

# Prune files the setup.py installs, but that we don't want.
#
# While the setup.py does try to install configuration files,
# it doesn't place them where we need them so we install them
# explicitly later.
rm -rf %{buildroot}/%{python3_sitelib}/{usr,etc}
rm -rf %{buildroot}/%{python3_sitelib}/tests
rm -rf %{buildroot}/%{python3_sitelib}/__main__.py
rm -rf %{buildroot}/%{python3_sitelib}/__pycache__/__main__*.py*
rm -f %{buildroot}%{_sbindir}/waagent2.0

mkdir -p -m 0700 %{buildroot}%{_sharedstatedir}/waagent
mkdir -p %{buildroot}%{_localstatedir}/log
touch %{buildroot}%{_localstatedir}/log/waagent.log

# Install configuration and systemd files for the agent
install -m0644 -D --target-directory=%{buildroot}%{_sysconfdir}/ config/waagent.conf
install -m0644 -D --target-directory=%{buildroot}%{_unitdir}/ init/*.slice
install -m0755 -D bin/waagent %{buildroot}%{_sbindir}/waagent
install -m0644 -D init/redhat/waagent.service %{buildroot}%{_unitdir}/
install -m0644 -D config/waagent.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

# Install -udev related files
install -m0644 -D --target-directory=%{buildroot}%{_udevrulesdir}/ config/*.rules
install -m0755 -D --target-directory=%{buildroot}%{_prefix}/lib/dracut/modules.d/%{dracut_modname}/ %{SOURCE1}

sed -i 's,#!/usr/bin/env python,#!/usr/bin/python3,' %{buildroot}%{_sbindir}/waagent
sed -i 's,/usr/bin/python ,/usr/bin/python3 ,' %{buildroot}%{_unitdir}/waagent.service
# Other commonly-used tools can handle formatting resource disks (cloud-init, azure-vm-utils) so
# by default, let's have WALinuxAgent not do that.
sed -i 's,ResourceDisk.Format=y,ResourceDisk.Format=n,' %{buildroot}%{_sysconfdir}/waagent.conf


%post
%systemd_post waagent.service

%preun
%systemd_preun waagent.service

%postun
%systemd_postun_with_restart waagent.service

%files -f %{pyproject_files}
%doc LICENSE.txt NOTICE README.md
%ghost %{_localstatedir}/log/waagent.log
%dir %attr(0700, root, root) %{_sharedstatedir}/waagent
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{_sysconfdir}/waagent.conf
%{_sbindir}/waagent
%{_unitdir}/waagent.service
%{_unitdir}/azure.slice
%{_unitdir}/azure-vmextensions.slice

%files udev
%{_udevrulesdir}/*.rules
%{_prefix}/lib/dracut/modules.d/%{dracut_modname}/*.sh


%changelog
%autochangelog
