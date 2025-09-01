%global forgeurl https://github.com/ansible-collections/community.internal_test_tools
%bcond tests 1

Name:           ansible-collection-community-internal_test_tools
Version:        0.18.0
%global tag     %{version}
%forgemeta
Release:        %autorelease
Summary:        Internal test tools for other collections

License:        GPL-3.0-or-later
URL:            %{ansible_collection_url community internal_test_tools}
Source:         %{forgesource}
# Not upstreamable. See Ansible Collection Packaging Guidelines.
Patch:          build_ignore.patch

BuildArch:      noarch

BuildRequires:  ansible-packaging
%if %{with tests}
BuildRequires:  ansible-packaging-tests
%endif

%description
The community.library_inventory_filtering_v1 collection includes helpers for
use with other collections that allow inventory plugins to offer common
filtering functionality.


%prep
%autosetup -p1 %{forgesetupargs}
find -type f ! -executable -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +
sed -i 's|^#!/usr/bin/env python|#!%{python3}|' \
    tests/sanity/extra/*.py


%build
%ansible_collection_build


%install
%ansible_collection_install


%check
%ansible_test_unit


%files -f %{ansible_collection_filelist}
%license REUSE.toml
%license CHANGELOG.rst.license
%license COPYING
%license LICENSES
%license changelogs/changelog.yaml.license
%license tests/sanity/extra/*.json.license
%doc CHANGELOG.rst
%doc README.md


%changelog
%autochangelog
