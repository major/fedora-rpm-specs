%global desc %{expand:
Helper scripts for the Resalloc server (mostly used by Copr build system)
for maintaining VMs in IBM Cloud (starting, stopping, cleaning orphans, etc.).
}

Name:           resalloc-ibm-cloud
Version:        1.0
Release:        1%{?dist}
Summary:        Resource allocator scripts for IBM cloud

License:        GPL-2.0-or-later
URL:            https://github.com/fedora-copr/%{name}
Source0:        %{url}/archive/refs/tags/%{name}-%{version}.tar.gz


BuildArch:      noarch

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
%{_bindir}/resalloc-ibm-cloud-list-vms
%{_bindir}/resalloc-ibm-cloud-vm


%changelog
* Tue Sep 26 2023 Jiri Kyjovsky 1.0-1
- Use setuptools instead of poetry
- spec: use SPDX lincese and drop build requires due to generic reqs

* Mon Sep 18 2023 Jiri Kyjovsky <j1.kyjovsky@gmail.com> 0.99-2
- use SPDX license and drop buildrequires

* Mon Sep 04 2023 Pavel Raiskup <praiskup@redhat.com> 0.99-1
- package && release with tito

* Wed Jan 18 2023 Jiri Kyjovsky <j1.kyjovsky@gmail.com>
- Initial package.
