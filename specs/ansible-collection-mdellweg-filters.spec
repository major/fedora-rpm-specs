Name:           ansible-collection-mdellweg-filters
Version:        0.0.6
Release:        2%{?dist}
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
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Sep 28 2024 Maxwell G <maxwell@gtmx.me> - 0.0.6-1
- Update to 0.0.6. Fixes rhbz#2296369.

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Maxwell G <maxwell@gtmx.me> - 0.0.3-1
- Initial package. Fixes rhbz#2222129.
