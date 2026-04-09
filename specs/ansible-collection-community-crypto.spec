%bcond tests %{undefined rhel}

Name:           ansible-collection-community-crypto
Version:        3.1.1
Release:        %autorelease
Summary:        The community.crypto collection for Ansible

# See the LICENSES directory and the summary in the README
License:        GPL-3.0-or-later AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND PSF-2.0
URL:            %{ansible_collection_url community crypto}
Source:         https://github.com/ansible-collections/community.crypto/archive/%{version}/community.crypto-%{version}.tar.gz
# build_ignore development files, tests, and docs
Patch:          build_ignore.patch

BuildArch:      noarch

BuildRequires:  ansible-packaging
%if %{with tests}
BuildRequires:  ansible-packaging-tests
BuildRequires:  pyproject-rpm-macros
%endif

%description
%{summary}.


%prep
%autosetup -p1 -n community.crypto-%{version}
find -type f ! -executable -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +


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
%ansible_test_unit
%endif


%files -f %{ansible_collection_filelist}
%license COPYING LICENSES
%doc README.md CHANGELOG.rst* docs/docsite/rst/


%changelog
%autochangelog
