Name:           ansible-collection-mdellweg-filters
Version:        0.0.3
Release:        1%{?dist}
Summary:        An Ansible collection of random filters I missed at some point

License:        GPL-3.0-or-later
URL:            %{ansible_collection_url mdellweg filters}
Source:         https://github.com/mdellweg/ansible_filters/archive/v%{version}/mdwellweg.filters-%{version}.tar.gz
# build_ignore development files, tests, and docs
Patch:          build_ignore.patch

BuildArch:      noarch

BuildRequires:  ansible-packaging

%description
%{summary}.


%prep
%autosetup -p1 -n ansible_filters-%{version}


%build
%ansible_collection_build


%install
%ansible_collection_install


%check
echo 'localhost ansible_connection=local' >hosts.ini
export \
    ANSIBLE_COLLECTIONS_PATH=%{buildroot}%{ansible_collections_dir} \
    ANSIBLE_INVENTORY=hosts.ini
ansible-playbook $(find tests/playbooks/*.yaml -not -name 'jq.yaml')



%files -f %{ansible_collection_filelist}
%license LICENSE
%doc README.md


%changelog
* Tue Jul 11 2023 Maxwell G <maxwell@gtmx.me> - 0.0.3-1
- Initial package. Fixes rhbz#2222129.
