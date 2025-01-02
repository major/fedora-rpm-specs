%bcond tests %{undefined rhel}

Name:           ansible-collection-dellemc-openmanage
Version:        9.10.0
Release:        %autorelease
Summary:        Dell OpenManage collection for Ansible

# All file ares GPL-3.0-only except for:
# plugins/module_utils/dellemc_idrac.py: BSD 2-Clause License
# plugins/module_utils/idrac_redfish.py: BSD 2-Clause License
# plugins/module_utils/ome.py: BSD 2-Clause License
# plugins/module_utils/redfish.py: BSD 2-Clause License
# plugins/module_utils/session_utils.py: BSD 2-Clause License
# plugins/module_utils/utils.py: BSD 2-Clause License
# Clarification requested upstream at https://github.com/dell/dellemc-openmanage-ansible-modules/issues/754
License:        GPL-3.0-only AND BSD-2-Clause

URL:            %{ansible_collection_url dellemc openmanage}
Source0:        https://github.com/dell/dellemc-openmanage-ansible-modules/releases/download/v%{version}/dellemc-openmanage-%{version}.tar.gz
Source1:        https://github.com/dell/dellemc-openmanage-ansible-modules/releases/download/v%{version}/dellemc-openmanage-%{version}.tar.gz.sign
# https://linux.dell.com/files/pgp_pubkeys/0x1285491434D8786F.asc
Source2:        gpgkey-42550ABD1E80D7C1BC0BAD851285491434D8786F.gpg

# File is missing from signed archive, but is required for RPM Macros
# https://github.com/dell/dellemc-openmanage-ansible-modules/issues/674
Source3:        https://raw.githubusercontent.com/dell/dellemc-openmanage-ansible-modules/v%{version}/galaxy.yml

# build_ignore development files, tests, and docs, downstream only
Patch:          build_ignore.patch

BuildArch:      noarch

BuildRequires:  gnupg2
BuildRequires:  ansible-packaging
%if %{with tests}
BuildRequires:  ansible-packaging-tests
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(mock)
%endif

# From bindep.txt
Requires:       xorriso
Requires:       syslinux
Requires:       isomd5sum
Requires:       wget

# From requirements.txt
Requires:       python3dist(omsdk)
Requires:       python3dist(netaddr)

%description
%{summary}.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -N -c -n dellemc-openmanage-%{version}
cp '%{SOURCE3}' galaxy.yml
%autopatch

# Remove shebangs on non-executable files
find -type f ! -executable -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +

# Remove empty files
find . -type f -empty ! -name __init__.py -print -delete


%if %{with tests}
%generate_buildrequires
%pyproject_buildrequires -N requirements.txt
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
%license LICENSE
%doc README.md CHANGELOG.rst docs/*


%changelog
%autochangelog
