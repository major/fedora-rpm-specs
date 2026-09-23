%if %{defined fedora}
%bcond tests 1
%else
%bcond tests 0
%endif

Name:           ansible-collection-ansible-mariadb
Version:        6.0.2
Release:        %autorelease
Summary:        MariaDB collection for Ansible

# All files are GPL-3.0-or-later except:
# PSF-2.0:      plugins/module_utils/_version.py
# BSD-2-Clause: plugins/module_utils/user.py
# BSD-2-Clause: plugins/module_utils/mysql.py
# BSD-2-Clause: plugins/module_utils/database.py
License:        GPL-3.0-or-later AND PSF-2.0 AND BSD-2-Clause
URL:            %{ansible_collection_url ansible mariadb}
Source:         https://github.com/ansible-collections/ansible.mariadb/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ansible-packaging
%if %{with tests}
BuildRequires:  ansible-packaging-tests
%endif

BuildArch:      noarch

%description
MariaDB collection for Ansible.

This collection was cloned from the ansible.mysql collection to allow its
contributors and maintainers to focus on MariaDB-related automation
development. MySQL is NOT supported by the ansible.mariadb collection!


%prep
%autosetup -n ansible.mariadb-%{version}
find -type f ! -executable -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +
# Remove zero length file
rm -r changelogs/fragments

%build
%ansible_collection_build

%install
%ansible_collection_install

%if %{with tests}
%check
%ansible_test_unit
%endif

%files -f %{ansible_collection_filelist}
%license COPYING PSF-license.txt simplified_bsd.txt CONTRIBUTORS
%doc README.md CHANGELOG.rst

%changelog
%autochangelog
