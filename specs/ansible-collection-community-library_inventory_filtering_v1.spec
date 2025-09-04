%global forgeurl https://github.com/ansible-collections/community.library_inventory_filtering
%bcond tests 1

Name:           ansible-collection-community-library_inventory_filtering_v1
Version:        1.1.1
%global tag     %{version}
%forgemeta
Release:        %autorelease
Summary:        Library collection with helpers for inventory plugins

License:        GPL-3.0-or-later
URL:            %{ansible_collection_url community library_inventory_filtering_v1}
Source:         %{forgesource}
# Not upstreamable
Patch:          0001-galaxy.yml-add-unnecessary-files-to-build_ignore.patch

BuildArch:      noarch

BuildRequires:  ansible-packaging
%if %{with tests}
# 1-15 adds support for %%ansible_test_unit's -c flag
BuildRequires:  ansible-packaging-tests >= 1-15
BuildRequires:  ansible-collection(community.internal_test_tools)
%endif

%description
The community.library_inventory_filtering_v1 collection includes helpers for
use with other collections that allow inventory plugins to offer common
filtering functionality.


%prep
%autosetup -p1 %{forgesetupargs}
find -type f ! -executable -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +


%build
%ansible_collection_build


%install
%ansible_collection_install


%check
%if %{with tests}
%ansible_test_unit -c community.internal_test_tools
%endif


%files -f %{ansible_collection_filelist}
%license REUSE.toml
%license CHANGELOG.*.license
%license COPYING
%license LICENSES
%license changelogs/changelog.yaml.license
%doc CHANGELOG.{md,rst}
%doc README.md


%changelog
%autochangelog
