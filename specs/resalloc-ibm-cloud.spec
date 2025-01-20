%global desc %{expand:
Helper scripts for the Resalloc server (mostly used by Copr build system)
for maintaining VMs in IBM Cloud (starting, stopping, cleaning orphans, etc.).
}

Name:           resalloc-ibm-cloud
Version:        3.0
Release:        2%{?dist}
Summary:        Resource allocator scripts for IBM cloud

License:        GPL-2.0-or-later
URL:            https://github.com/fedora-copr/%{name}
Source0:        %{url}/archive/refs/tags/%{name}-%{version}.tar.gz


BuildArch:      noarch

Requires:       resalloc-helpers
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros


%description
%{desc}


%prep
%autosetup -n %{name}-%{version}


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files resalloc_ibm_cloud


%files -n %{name} -f %{pyproject_files}
%license LICENSE
%doc README.md
%_mandir/man1/resalloc-ibm-cloud*1*
%{_bindir}/resalloc-ibm-cloud-list-deleting-vms
%{_bindir}/resalloc-ibm-cloud-list-deleting-volumes
%{_bindir}/resalloc-ibm-cloud-list-vms
%{_bindir}/resalloc-ibm-cloud-vm


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jan 11 2025 Pavel Raiskup <praiskup@redhat.com> 3.0-1
- Log the instance create request content
- Allow specifying a list of Floating IPs
- Drop executable bits from PYTHONPATH scripts

* Tue Dec 17 2024 Jiri Kyjovsky <j1.kyjovsky@gmail.com> 2.3-1
- Add functionality for tagging resource by its crn (j1.kyjovsky@gmail.com)
- Add option for specifying resource group (j1.kyjovsky@gmail.com)

* Tue Oct 01 2024 Jiri Kyjovsky <j1.kyjovsky@gmail.com> 2.2-1
- Allow dynamic spefifying of volume size

* Wed Feb 28 2024 Pavel Raiskup <praiskup@redhat.com> 2.1-1
- The wait-for-ssh script was moved to resalloc-helpers
- releng: release to all active Fedora releases

* Tue Jan 16 2024 Pavel Raiskup <praiskup@redhat.com>
- don't try to remove attached volumes
- give the ansible-playbook utility a blocking stdin

* Wed Nov 08 2023 Pavel Raiskup <praiskup@redhat.com> 1.2-1
- Automatically remove leftover Floating IPs
- Fail early for too-long resource names

* Mon Oct 16 2023 Pavel Raiskup <praiskup@redhat.com> 1.1-1
- Simplify the get_service() helper
- list-deleting-volumes: new helper for customer case reporting
- fix manpage contents
- provide subnets ids directly to the tool via argument (j1.kyjovsky@gmail.com)
- specify ibm cloud zone instead of hardcoded API url (j1.kyjovsky@gmail.com)
- add option to use instance's private IP to connect to it (j1.kyjovsky@gmail.com)

* Tue Sep 26 2023 Jiri Kyjovsky 1.0-1
- Use setuptools instead of poetry
- spec: use SPDX lincese and drop build requires due to generic reqs

* Mon Sep 18 2023 Jiri Kyjovsky <j1.kyjovsky@gmail.com> 0.99-2
- use SPDX license and drop buildrequires

* Mon Sep 04 2023 Pavel Raiskup <praiskup@redhat.com> 0.99-1
- package && release with tito

* Wed Jan 18 2023 Jiri Kyjovsky <j1.kyjovsky@gmail.com>
- Initial package.
