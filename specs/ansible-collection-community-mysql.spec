%if %{defined fedora}
%bcond_without tests
%else
%bcond_with tests
%endif

Name:           ansible-collection-community-mysql
Version:        3.12.0
Release:        %autorelease
Summary:        MySQL collection for Ansible

# All files are GPL-3.0-or-later except:
# PSF-2.0:      plugins/module_utils/_version.py
# BSD-2-Clause: plugins/module_utils/user.py
# BSD-2-Clause: plugins/module_utils/mysql.py
# BSD-2-Clause: plugins/module_utils/database.py
License:        GPL-3.0-or-later AND PSF-2.0 AND BSD-2-Clause
URL:            %{ansible_collection_url community mysql}
Source:         https://github.com/ansible-collections/community.mysql/archive/%{version}/%{name}-%{version}.tar.gz
# Patch galaxy.yml to exclude unnecessary files from the built collection.
# This is a downstream only patch.
Patch:          build_ignore.patch

BuildRequires:  ansible-packaging
%if %{with tests}
BuildRequires:  ansible-packaging-tests
%endif

BuildArch:      noarch

%description
%{summary}.

%prep
%autosetup -n community.mysql-%{version}
find -type f ! -executable -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +

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
