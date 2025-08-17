%global srcname virtualbmc

Name: python-%{srcname}
Version: 3.2.0
Release: 5%{?dist}
Summary: A virtual BMC for controlling virtual machines using IPMI commands
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License: Apache-2.0
URL: https://opendev.org/openstack/virtualbmc
Source0: https://tarballs.opendev.org/openstack/%{srcname}/%{srcname}-%{version}.tar.gz
Source1: 60-vbmcd.rules
Source2: vbmcd.service
Source3: vbmcd.sysusers
BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: systemd-rpm-macros
BuildRequires: git
# Documentation
BuildRequires: python3-sphinx
BuildRequires: python3-openstackdocstheme
# Tests
BuildRequires: python3-stestr
BuildRequires: python3-libvirt
BuildRequires: python3-pyghmi
BuildRequires: python3-zmq
BuildRequires: python3-oslotest
BuildRequires: python3-autopage

%description
A virtual BMC for controlling virtual machines using IPMI commands.

%package -n python3-%{srcname}
Summary: A virtual BMC for controlling virtual machines using IPMI commands
Suggests: python3-%{srcname}-doc

%description -n python3-%{srcname}
A virtual BMC for controlling virtual machines using IPMI commands.

%package -n python3-%{srcname}-tests
Summary: VirtualBMC tests
Requires: python3-%{srcname} = %{version}-%{release}

%description -n python3-%{srcname}-tests
Tests for VirtualBMC.

%package -n python3-%{srcname}-doc
Summary: VirtualBMC documentation

%description -n python3-%{srcname}-doc
Documentation for VirtualBMC.

%prep
%autosetup -n %{srcname}-%{version} -S git

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
# generate html docs
sphinx-build-3 -W -b html doc/source doc/build/html
# remove the sphinx-build-3 leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%pyproject_install
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/polkit-1/rules.d/60-vbmcd.rules
install -p -D -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/vbmcd.service
install -p -D -m 0644 %{SOURCE3} %{buildroot}%{_sysusersdir}/vbmcd.conf
install -d -m 750 %{buildroot}%{_sharedstatedir}/vbmcd

%check
PYTHON=%{__python3} stestr run

%post -n python3-%{srcname}
%systemd_post vbmcd.service

%preun -n python3-%{srcname}
%systemd_preun vbmcd.service

%postun -n python3-%{srcname}
%systemd_postun_with_restart vbmcd.service

%files -n python3-%{srcname}
%license LICENSE
%{_bindir}/vbmcd
%{_bindir}/vbmc
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-*.dist-info
%exclude %{python3_sitelib}/%{srcname}/tests
%{_datadir}/polkit-1/rules.d/60-vbmcd.rules
%{_unitdir}/vbmcd.service
%{_sysusersdir}/vbmcd.conf
%dir %attr(750, vbmcd, vbmcd) %{_sharedstatedir}/vbmcd

%files -n python3-%{srcname}-tests
%license LICENSE
%{python3_sitelib}/%{srcname}/tests

%files -n python3-%{srcname}-doc
%license LICENSE
%doc AUTHORS README.rst HACKING.rst CONTRIBUTING.rst ChangeLog
%doc doc/build/html

%changelog
* Fri Aug 15 2025 Python Maint <python-maint@redhat.com> - 3.2.0-5
- Rebuilt for Python 3.14.0rc2 bytecode

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

%autochangelog
