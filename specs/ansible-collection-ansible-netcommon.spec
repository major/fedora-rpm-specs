%global _docdir_fmt %{name}

Name:           ansible-collection-ansible-netcommon
Version:        7.1.0
Release:        %autorelease
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
%autochangelog
