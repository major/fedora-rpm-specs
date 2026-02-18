%global collection_namespace community
%global collection_name libvirt

# Only run tests where test deps are available
%if 0%{?fedora} || 0%{?rhel} >= 9
%bcond_without     tests
%else
%bcond_with        tests
%endif

Name:           ansible-collection-%{collection_namespace}-%{collection_name}
Version:        2.1.0
Release:        1%{?dist}
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
BuildRequires:  coreutils
BuildRequires:  findutils
%if %{with tests}
BuildRequires:  glibc-langpack-en
Buildrequires:  python3-devel
BuildRequires:  ansible-packaging-tests
%endif

%description
%{summary}.

%prep
%setup -q -n community.libvirt-%{version}

# Exclude some files from being installed
cat << 'EOF' >> galaxy.yml
build_ignore:
- .azure-pipelines
- .github
- .gitignore
- .package_note-%{name}*
- .pyproject-builddir
- changelogs/fragments/.keep
- tests
EOF

# Drop shellbangs from python files
find -type f ! -executable -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +

%build
%ansible_collection_build

%install
%ansible_collection_install

%check
%if %{with tests}
%ansible_test_unit
%endif

%files
%license COPYING
%doc CHANGELOG.rst CONTRIBUTING.md README.md
%{ansible_collection_files}

%changelog
* Mon Feb 16 2026 Paul Howarth <paul@city-fan.org> - 2.1.0-1
- Update to 2.1.0 (rhbz#2440142)
  - This is a minor release of the community.libvirt collection
  - virt_install:
    - Added support for memoryBacking source type configuration, including
      memfd for shared memory (GH#228)
    - Added support for primary value attribute (_value or value) in dynamic
      dict options that require a primary value alongside additional attributes
    - Enhanced cloud_init configuration handling for sub-options (meta-data,
      user-data and network-config) to support both string and dictionary inputs
    - Refactored common virt-install functionality into module_utils and
      doc_fragments to enable code reuse between modules
    - Fixed cloud_init configuration handling for meta-data, user-data and
      network-config
    - Fixed the dict-based options handling for events, resource and sysinfo
      options
  - virt_volume:
    - New return key/value pairs 'Type', 'Capacity' and 'Allocation' were added
      to command 'list_volumes' (GH#187)
    - Added ability to resize volumes if defined capacity is different; if
      volume already exists and defined capacity in XML differs, a resize is
      attempted
  - New module community.libvirt.virt_cloud_instance: Provision new virtual
    machines from cloud images via libvirt

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Jul 21 2025 Paul Howarth <paul@city-fan.org> - 2.0.0-1
- Update to 2.0.0 (rhbz#2382300)
  - This is a major release of the community.libvirt collection
  - Many changes for virt_volume: see CHANGELOG.rst for details
  - New module community.libvirt.virt_install to provision new virtual machines
    using the virt-install tool

* Mon May 26 2025 Paul Howarth <paul@city-fan.org> - 1.4.0-1
- Update to 1.4.0 (rhbz#2368572)
  - virt: implement basic check mode functionality (GH#98)
  - virt: implement the gathering of Dom UUIDs (GH#187)
  - virt: implement the gathering of Dom interface names and MAC addresses
    (GH#189)
  - virt: implement the removal of volumes for a Dom (GH#177)
  - New module community.libvirt.virt_volume: manage libvirt volumes inside a
    storage pool

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Dec 17 2024 Paul Howarth <paul@city-fan.org> - 1.3.1-1
- Update to 1.3.1 (rhbz#2332772)
  - libvirt_lxc: add configuration for libvirt_lxc_noseclabel

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan  12 2024 Maxwell G <maxwell@gtmx.me> - 1.3.0-2
- Depend on ansible-packaging-tests and remove python3-mock dep

* Tue Sep 26 2023 Paul Howarth <paul@city-fan.org> - 1.3.0-1
- Update to 1.3.0
  - virt: add 'mutate_flags' parameter to enable XML mutation (add UUID, MAC
    addresses from existing domain) (GH#142)
  - virt: support '--diff' for 'define' command (GH#142)
  - libvirt_qemu: connection plugin threw a warning about an improperly
    configured remote target; fix adds 'inventory_hostname' to
    'options.remote_addr.vars' (GH#147)
  - libvirt_qemu: fix encoding errors on Windows guests for non-ASCII return
    values (GH#157)
  - virt: fix virt module to undefine a domain with nvram, managed_save,
    snapshot_metadata or checkpoints_metadata (GH#40)
  - virt_pool: replace discouraged function 'listVolumes' with 'listAllVolumes'
    to fix potential race conditions (GH#135)
  - virt_pool: replace discouraged functions 'listStoragePools' and
    'listDefinedStoragePools' with 'listAllStoragePools' to fix potential race
    conditions (GH#134)

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

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
