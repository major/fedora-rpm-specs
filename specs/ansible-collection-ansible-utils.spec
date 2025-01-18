%global collection_namespace ansible
%global collection_name utils

Name:           ansible-collection-%{collection_namespace}-%{collection_name}
Version:        5.0.0
Release:        2%{?dist}
Summary:        Ansible Network Collection for Common Code

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            %{ansible_collection_url}
Source:         https://github.com/ansible-collections/ansible.utils/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ansible-packaging

BuildArch:      noarch

%description
%{summary}.

%prep
%autosetup -n ansible.utils-%{version}
sed -i -e '/version:/s/null/%{version}/' galaxy.yml
find -type f ! -executable -type f -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +
rm -fvr tests/integration tests/unit bindep.txt .pre-commit-config.yaml .yamllint changelogs/fragments/.keep
find -type f -name '.gitignore' -print -delete

%build
%ansible_collection_build

%install
%ansible_collection_install

%files
%license LICENSE
%doc README.md
%{ansible_collection_files}

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Orion Poplawski <orion@nwra.com> - 5.0.0-1
- Update to 5.0.0

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 4.0.0-3
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Mar 28 2024 Orion Poplawski <orion@nwra.com> - 4.0.0-1
- Update to 4.0.0

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Dec 01 2023 Maxwell G <maxwell@gtmx.me> - 3.0.0-1
- Update to 3.0.0. Fixes rhbz#2139973.

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jan 31 2023 Orion Poplawski <orion@nwra.com> - 2.9.0-1
- Update to 2.9.0

* Tue Jan 31 2023 Orion Poplawski <orion@nwra.com> - 2.8.0-1
- Update to 2.8.0

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 23 2022 Orion Poplawski <orion@nwra.com> - 2.6.1-1
- Update to 2.6.1

* Sat Jan 29 2022 Maxwell G <gotmax@e.email> - 2.3.0-5
- Switch to ansible-packaging.

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 14 2021 Sagi Shnaidman <sshnaidm@redhat.com> - 2.3.0-3
- Use ansible or ansible-core as BuildRequires

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 06 2021 Sagi Shnaidman <sshnaidm@redhat.com> - 2.3.0-1
- Initial package

