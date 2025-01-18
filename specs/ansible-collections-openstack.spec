%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%{?dlrn: %global tarsources ansible-collections-openstack.cloud}
%{!?dlrn: %global tarsources ansible-collections-openstack}

Name:           ansible-collections-openstack
Version:        2.2.0
Release:        3%{?dist}
Summary:        Openstack Ansible collections
License:        GPL-3.0-or-later
URL:            https://opendev.org/openstack/ansible-collections-openstack
Source0:        https://github.com/openstack/%{name}/archive/refs/tags/%{version}.tar.gz
BuildArch:      noarch
# (amoralej) We can remove this patch when we move to next release after 2.2.0
%if %{lua:print(rpm.vercmp(rpm.expand("%{version}"), '2.2.0'));} <= 0
Patch0:         0001-Disable-auto-discovery-for-setuptools.patch
%endif

BuildRequires:  git-core
BuildRequires:  python3-pbr
BuildRequires:  python3-devel

%if 0%{?rhel}
Requires:       openstack-ansible-core
%else
Requires:       ansible-core
%endif
Requires:       python3-openstacksdk >= 0.13.0

%description
Openstack Ansible collections

%prep
%autosetup -n %{tarsources}-%{upstream_version} -S git

%build
%py3_build

%install
export PBR_VERSION=%{version}
export SKIP_PIP_INSTALL=1
%py3_install

%files

%doc README.md
%license COPYING
%{python3_sitelib}/ansible_collections_openstack.cloud-*.egg-info
%{_datadir}/ansible/collections/ansible_collections/openstack/cloud/

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Oct 28 2024 Joel Capitao <jcapitao@redhat.com> 2.2.0-2
- Require ansible-core in Fedora

* Tue Oct 08 2024 Joel Capitao <jcapitao@redhat.com> 2.2.0-1
- Update to upstream version 2.2.0

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 2.1.0-6
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 14 2023 Alfredo Moralejo <amoralej@redhat.com> - 2.1.0-1
- Update to 2.1.0

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.2.ed36d82git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 23 2022 Alfredo Moralejo <amoralej@redhat.com> - 2.0.0-0.1.ed36d82git
- Update to pre-2.0.0 commit (ed36d82a0c60a841d2f30c61a50d60531481b2cc)

* Tue Aug 02 2022 Joel Capitao <jcapitao@redhat.com> - 1.7.1-4.938abd0git
- Take advantage of ansible-packaging

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-3.938abd0git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.7.1-2.938abd0git
- Rebuilt for Python 3.11

* Thu May 19 2022 Joel Capitao <jcapitao@redhat.com> 1.7.1-1.938abd0git
- Update to upstream version 1.7.1

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.3.0-3
- Rebuilt for Python 3.10

* Thu Apr 08 2021 Sagi Shnaidman <sshnaidm@redhat.com> 1.3.0-2
- RPM package fixes

* Mon Apr 05 2021 Sagi Shnaidman <sshnaidm@redhat.com> 1.3.0-1
- Initial package


