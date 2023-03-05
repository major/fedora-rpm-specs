%global collection_namespace community
%global collection_name libvirt

# Only run tests where test deps are available
%if 0%{?fedora}
%bcond_without     tests
%else
%bcond_with        tests
%endif

Name:           ansible-collection-%{collection_namespace}-%{collection_name}
Version:        1.2.0
Release:        3%{?dist}
Summary:        Manages virtual machines supported by libvirt
License:        GPL-3.0-or-later
URL:            %{ansible_collection_url}
Source:         https://github.com/ansible-collections/community.libvirt/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  ansible-packaging
# The new ansible-core, specifically, is required for the 'build_ignore:' patch
# and ansible-test to work properly; hence we cannot rely on ansible-packaging,
# which might pull in ansible 2.9
BuildRequires:  ansible-core
%if %{with tests}
Buildrequires:  python3-devel
BuildRequires:  /usr/bin/ansible-test
%endif

%description
%{summary}.

%prep
%setup -q -n community.libvirt-%{version}

# Exclude some files from being installed
cat << 'EOF' >> galaxy.yml
build_ignore:
- .azure-pipelines
- .package_note-%{name}*
- .pyproject-builddir
- .gitignore
- tests
EOF

# Drop shellbangs from python files
find -type f ! -executable -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +

%generate_buildrequires
%if %{with tests}
%pyproject_buildrequires -N %{python3_sitelib}/ansible_test/_data/requirements/units.txt
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
ansible-test units --python-interpreter %{__python3} --local
popd
%endif

%files
%license COPYING
%doc CHANGELOG.rst CONTRIBUTING.md README.md
%{ansible_collection_files}

%changelog
* Fri Mar  3 2023 Paul Howarth <paul@city-fan.org> - 1.2.0-3
- Use SPDX-format license tag

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Aug  5 2022 Paul Howarth <paul@city-fan.org> - 1.2.0-1
- Update to 1.2.0
  - libvirt: Add extra guest information to inventory (GH#113)
  - libvirt: Replace the calls to listDomainsID() and listDefinedDomains() with
    listAllDomains() in find_vm() (GH#117)
  - virt_net: Fix modify function, which was not idempotent, depending on
    whether the network was active (GH#107)
  - virt_pool: It crashed out if pool didn't contain a target path; fix allows
    this not to be set (GH#129)

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 17 2022 Paul Howarth <paul@city-fan.org> - 1.1.0-3
- Add COPYING as a %%license file
- Unconditionally use dynamic buildrequires to ensure expansion of
  %%{ansible_collection_url} in SRPM

* Mon May 16 2022 Paul Howarth <paul@city-fan.org> - 1.1.0-2
- Incorporate feedback from package review (#2086299)
  - Add %%check section to run unit tests
  - Handle file exclusions using galaxy.yml
  - Generate test dependencies dynamically
- Manually specify URL: tag for EPEL-9 compatibility

* Sun May 15 2022 Paul Howarth <paul@city-fan.org> - 1.1.0-1
- Update to 1.1.0
  - Replace deprecated 'distutils.spawn.find_executable' with Ansible's
    'get_bin_path' in '_search_executable' function

* Wed May 11 2022 Paul Howarth <paul@city-fan.org> - 1.0.2-1
- Initial package
