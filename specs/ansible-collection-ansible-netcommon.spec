%global _docdir_fmt %{name}

Name:           ansible-collection-ansible-netcommon
Version:        6.1.3
Release:        2%{?dist}
Summary:        Ansible Network Collection for Common Code

# All files are licensed under GPL-3.0-or-later except:
# rg --pcre2 -g '!tests/sanity/extra/licenses.py' 'SPDX-License-Identifier: (?!GPL-3\.0-or-later)' | sort | sed 's|^|# |'
#
# plugins/module_utils/cli_parser/cli_parserbase.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/cli_parser/cli_parsertemplate.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/network/common/config.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/network/common/netconf.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/network/common/network.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/network/common/network_template.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/network/common/parsing.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/network/common/resource_module.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/network/common/rm_base/network_template.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/network/common/rm_base/resource_module_base.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/network/common/rm_base/resource_module.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/network/common/utils.py:# SPDX-License-Identifier: BSD-2-Clause
# plugins/module_utils/network/restconf/restconf.py:# SPDX-License-Identifier: BSD-2-Clause
License:        GPL-3.0-or-later AND BSD-2-Clause
URL:            %{ansible_collection_url ansible netcommon}
Source:         https://github.com/ansible-collections/ansible.netcommon/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ansible-packaging
BuildRequires:  %{py3_dist pyyaml}

BuildArch:      noarch

%global _description %{expand:
The Ansible ansible.netcommon collection includes common content to help
automate the management of network, security, and cloud devices. This includes
connection plugins, such as network_cli, httpapi, and netconf.}

%description %_description

%package        doc
Summary:        %{summary} - Docs

%description    doc %_description

This subpackage provides documentation for ansible-collection-ansible-netcommon.

%prep
%autosetup -n ansible.netcommon-%{version} -p1
find -type f ! -executable -type f -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +

# Patch galaxy.yml to exclude unnecessary files from the built collection.
# This is a downstream only patch.
%{python3} - <<EOF
import yaml

build_ignores = """
- .pre-commit-config.yaml
- .gitignore
- .yamllint
- .github
- .flake8
- .isort.cfg
- .prettierignore
- tests
- changelogs/fragments/
- requirements.txt
- test-requirements.txt
- tox.ini
# We install these files with %%doc/%%license. We don't want them duplicated.
- CHANGELOG.rst
- README.md
- LICENSE
- LICENSES
- docs
"""
ignores = yaml.safe_load(build_ignores)
with open("galaxy.yml") as fp:
    data = yaml.safe_load(fp)
data.setdefault("build_ignore", []).extend(ignores)
with open("galaxy.yml", "w") as fp2:
    yaml.safe_dump(data, fp2)
EOF

%build
%ansible_collection_build

%install
%ansible_collection_install

%files -f %{ansible_collection_filelist}
%license LICENSE LICENSES/
%doc README.md CHANGELOG.rst

%files doc
%license LICENSE
%doc docs

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Orion Poplawski <orion@nwra.com> - 6.1.3-1
- Update to 6.1.3

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Dec 01 2023 Maxwell G <maxwell@gtmx.me> - 6.0.0-1
- Update to 6.0.0.

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 04 2022 Maxwell G <gotmax@e.email> - 4.1.0-1
- Update to 4.1.0. Fixes rhbz#2139971.

* Wed Oct 19 2022 Maxwell G <gotmax@e.email> - 4.0.0-1
- Update to 4.0.0. Fixes rhbz#2124745.

* Sat Aug 27 2022 Maxwell G <gotmax@e.email> - 3.1.0-1
- Update to 3.1.0. Fixes rhbz#2089526.

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Oct 13 2021 Sagi Shnaidman <sshnaidm@redhat.com> - 2.2.0-2
- Use ansible or ansible-core as BuildRequires

* Thu Jul 22 2021 Sagi Shnaidman <sshnaidm@redhat.com> - 2.2.0-1
- Update to 2.2.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 04 2021 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.5.0-1
- Update to 1.5.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 16 2021 Kevin Fenzi <kevin@scrye.com> - 1.4.1-2
- Rebuild for new ansible-generator and allow to be used with ansible-base-2.10.x

* Tue Dec 29 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.4.1-1
- Update to 1.4.1

* Sat Aug 08 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.1.2-1
- Initial package
