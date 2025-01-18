%global collection_namespace kubernetes
%global collection_name core
%global forgeurl https://github.com/ansible-collections/%{collection_namespace}.%{collection_name}

# Only run tests where %%generate_buildrequires and test deps are available.
%if 0%{?fedora} || 0%{?rhel} >= 9
%bcond_without     tests
%else
%bcond_with        tests
%endif


Name:           ansible-collection-%{collection_namespace}-%{collection_name}
Version:        2.3.2
%global tag     %{version}
%forgemeta
Release:        10%{?dist}
Summary:        Ansible content for working with Kubernetes and OpenShift clusters

# All files are GPL-3.0-or-later (GPLv3+) except:
# ./plugins/module_utils/apply.py: Apache License 2.0
# ./plugins/module_utils/copy.py: Apache License 2.0
# ./plugins/module_utils/exceptions.py: Apache License 2.0
# ./plugins/module_utils/hashes.py: Apache License 2.0
# ./plugins/module_utils/k8sdynamicclient.py: Apache License 2.0
# ./plugins/module_utils/selector.py: Apache License 2.0
# ./plugins/module_utils/client/discovery.py: Apache License 2.0
# ./plugins/module_utils/client/resource.py: Apache License 2.0
# ./plugins/module_utils/_version.py: PSF-2.0

# SPDX-License-Identifier: GPL-3.0-or-later AND Apache-2.0 AND PSF-2.0
# Automatically converted from old format: GPLv3+ and ASL 2.0 and Python - review is highly recommended.
License:        GPL-3.0-or-later AND Apache-2.0 AND LicenseRef-Callaway-Python
URL:            %{ansible_collection_url}
Source0:        %{forgesource}

BuildArch:      noarch

# Needed for %%pyroject_buildrequires
Buildrequires:  python3-devel

BuildRequires:  ansible-packaging
# The new ansible-core, specifically, is required for the `build_ignore:` patch and ansible-test to work properly.
# Therefore, we cannot rely on ansible-packaging which might pull in ansible 2.9.
BuildRequires:  ansible-core
%if %{with tests}
BuildRequires:  ansible-packaging-tests
%endif

%global _description %{expand:
%{name} provides the %{collection_namespace}.%{collection_name} (formerly known as community.kubernetes) Ansible collection.

The collection includes a variety of Ansible content to help automate the management of applications in Kubernetes and OpenShift clusters, as well as the provisioning and maintenance of clusters themselves.}


%description
%wordwrap -v _description


%prep
%forgeautosetup -p1
find -type f ! -executable -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +
# Exclude some files from being installed
cat << EOF >> galaxy.yml
  - .github
  - .package_note-%{name}*
  - .pyproject-builddir
  - .gitignore
  - .yamllint
  - setup.cfg
  - codecov.yml
  - tox.ini
  - Makefile
  - tests
# These files are installed into /usr/share/doc and /usr/share/license.
# We don't want to duplicate them in %%{ansible_collection_files}.
  - LICENSE
  - PSF-license.txt
  - README.md
  - CONTRIBUTING.md
  - CHANGELOG.rst
  - docs
EOF


%if %{with tests}
%generate_buildrequires
%pyproject_buildrequires -N tests/unit/requirements.txt
%endif


%build
%ansible_collection_build


%install
%ansible_collection_install


%check
%if %{with tests}
mkdir -p ../ansible_collections/%{collection_namespace}
cp -a $(pwd) ../ansible_collections/%{collection_namespace}/%{collection_name}
pushd ../ansible_collections/%{collection_namespace}/%{collection_name}
ansible-test units --python-interpreter %{python3} --local
popd
%endif


%files
%license LICENSE PSF-license.txt
%doc README.md CHANGELOG.rst CONTRIBUTING.md docs
%{ansible_collection_files}


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 2.3.2-9
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 12 2024 Maxwell G <maxwell@gtmx.me> - 2.3.2-5
- Depend on ansible-packaging-tests and remove python3-mock dep

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Maxwell G <gotmax@e.email> - 2.3.2-1
- Initial package. Closes rhbz#2096448.
- Fix ansible-collection-community-kubernetes FTI (rhbz#2031305).
