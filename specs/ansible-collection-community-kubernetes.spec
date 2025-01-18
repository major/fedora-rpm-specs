%global collection_namespace community
%global collection_name kubernetes

Name:           ansible-collection-%{collection_namespace}-%{collection_name}
Version:        2.0.1
Release:        11%{?dist}
Summary:        Kubernetes Collection for Ansible

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            %{ansible_collection_url}
Source:         https://github.com/ansible-collections/community.kubernetes/archive/%{version}/%{name}-%{version}.tar.gz

# See message in %%description.
Provides:       deprecated()

BuildRequires:  ansible-packaging

BuildArch:      noarch

%description
%{summary}.
This collection has been deprecated in favor of
ansible-collection-kubernetes-core. Users should change their collection names
from `community.kubernetes.X` to `kubernetes.core.X` and replace this package
with ansible-collection-kubernetes-core.


%prep
%autosetup -n %{collection_namespace}.%{collection_name}-%{version}
rm -vr .github .yamllint codecov.yml setup.cfg
find -type f ! -executable -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +
find -type f -name '.gitignore' -print -delete

%build
%ansible_collection_build

%install
%ansible_collection_install

%files
%license LICENSE
%doc README.md CHANGELOG.rst
%{ansible_collection_files}

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 2.0.1-10
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 20 2022 Maxwell G <gotmax@e.email> - 2.0.1-3
- Add deprecation warning.
- Mark package as deprecated().

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 03 2021 Kevin Fenzi <kevin@scrye.com> - 2.0.1-1
- Update to 2.0.1. Fixes rhbz#2028314

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 16 2021 Kevin Fenzi <kevin@scrye.com> - 1.1.1-3
- Rebuild against new ansible-generator and allow to be used by ansible-base-2.10.x

* Tue Dec 29 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.1.1-2
- Drop unneeded dependency

* Tue Dec 29 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.1.1-1
- Update to 1.1.1

* Sun Aug 09 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.0.0-1
- Initial package
