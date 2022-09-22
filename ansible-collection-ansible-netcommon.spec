%global _docdir_fmt %{name}
%global collection_namespace ansible
%global collection_name netcommon
# This package does not include any ELF binaries, and we don't want this file
# in the built collection artifact.
%undefine _package_note_file

Name:           ansible-collection-%{collection_namespace}-%{collection_name}
Version:        3.1.0
Release:        1%{?dist}
Summary:        Ansible Network Collection for Common Code

# All files are licensed under GPL-3.0-or-later except:
# licensecheck -r . | grep -vEe "UNKNOWN" -e "GNU General Public License v3.0" | sed 's|^|# |'
#
# ./plugins/module_utils/network/common/config.py: BSD 2-Clause License
# ./plugins/module_utils/network/common/netconf.py: BSD 2-Clause License
# ./plugins/module_utils/network/common/network.py: BSD 2-Clause License
# ./plugins/module_utils/network/common/network_template.py: BSD 2-Clause License
# ./plugins/module_utils/network/common/parsing.py: BSD 2-Clause License
# ./plugins/module_utils/network/common/resource_module.py: BSD 2-Clause License
# ./plugins/module_utils/network/common/utils.py: BSD 2-Clause License
# ./plugins/module_utils/network/restconf/restconf.py: BSD 2-Clause License
# ./plugins/module_utils/network/common/rm_base/network_template.py: BSD 2-Clause License
# ./plugins/module_utils/network/common/rm_base/resource_module.py: BSD 2-Clause License
# ./plugins/module_utils/network/common/rm_base/resource_module_base.py: BSD 2-Clause License
License:        GPL-3.0-or-later AND BSD-2-Clause
URL:            %{ansible_collection_url}
Source:         https://github.com/ansible-collections/ansible.netcommon/archive/%{version}/%{name}-%{version}.tar.gz
# Patch galaxy.yml to exclude unnecessary files from the built collection.
# This is a downstream only patch.
Patch:          0001-build_ignore-unnecessary-files.patch

BuildRequires:  ansible-packaging

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
sed -i -e '/version:/s/null/%{version}/' galaxy.yml
find -type f ! -executable -type f -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +

%build
%ansible_collection_build

%install
%ansible_collection_install

%files
%license LICENSE
%doc README.md CHANGELOG.rst
%{ansible_collection_files}

%files doc
%doc docs
%license LICENSE

%changelog
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
