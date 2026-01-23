# For fastmcp: disks, keyring, memory
# For tests: pydantic, elasticsearch
%global extras disk,elasticsearch,keyring,memory,pydantic

Name:           python-py-key-value
Version:        0.3.0
Release:        %autorelease
Summary:        Key-Value Store Project
License:        Apache-2.0
BuildArch:      noarch
URL:            https://github.com/strawgate/py-key-value
Source:         %{url}/archive/%{version}/py-key-value-%{version}.tar.gz

# Downstream-only dependency adjustments
Patch:          0001-Fedora-dependency-adjustments.patch

BuildRequires:  python3-devel

%global _description %{expand:
This library provides a pluggable interface for key-value stores with support
for multiple backends, TTL handling, type safety, and extensible wrappers.}


%description %_description


%package -n python3-py-key-value-shared
Summary:        Shared Key-Value


%description -n python3-py-key-value-shared %_description

This package provides the key_value.shared importable module.


%package -n python3-py-key-value-aio
Summary:        Async Key-Value


%description -n python3-py-key-value-aio %_description

This package provides the key_value.aio importable module.


# The upstream monorepo also includes a key_value.sync module, but that is
# described as "under development".  For now we'll leave that out, but it can
# be added later as another subpackage if needed.


%pyproject_extras_subpkg -n python3-py-key-value-aio -i %{python3_sitelib}/py_key_value_aio-%{version}.dist-info %{gsub %{extras} %{quote:,} %{quote: }}


%prep
%autosetup -p 1 -n py-key-value-%{version}


%generate_buildrequires
# The use of cd over pushd/popd here in this section is intentional.
# pushd/popd outputs the directory stack to stdout, but every stdout line of
# %%generate_buildrequires is treated as a build requirement.  Using pushd/popd
# will result in a somewhat obscure error about dependency tokens.
cd key-value/key-value-shared-test
%pyproject_buildrequires -g dev

cd ../key-value-shared
%pyproject_buildrequires

# key-value-aio depends on key-value-shared, which will cause a self-bootstrap
# loop if we don't filter it out here.  See rhbz#2427769 for more details, and
# rhbz#2386906 for a potential long-term replacement approach.
cd ../key-value-aio
(
%pyproject_buildrequires -x %{extras}
) | grep -vE '\bpy-key-value-shared\b'


%build
cd key-value/key-value-shared-test
%pyproject_wheel

cd ../key-value-shared
%pyproject_wheel

cd ../key-value-aio
%pyproject_wheel


%install
cd key-value/key-value-shared-test
%pyproject_install

cd ../key-value-shared
%pyproject_install

cd ../key-value-aio
%pyproject_install

# %%pyproject_save_files doesn't support multiple wheels, so we'll skip it and
# use a direct file list.


%check
cd key-value/key-value-shared
%pytest

cd ../key-value-aio
# Ignore tests that have missing dependencies, require a docker socket, or only
# run on Windows.
%pytest \
    --ignore tests/stores/duckdb \
    --ignore tests/stores/dynamodb \
    --ignore tests/stores/filetree \
    --ignore tests/stores/memcached \
    --ignore tests/stores/mongodb \
    --ignore tests/stores/redis \
    --ignore tests/stores/rocksdb \
    --ignore tests/stores/valkey \
    --ignore tests/stores/vault \
    --ignore tests/stores/windows_registry


%files -n python3-py-key-value-shared
%license LICENSE
%dir %{python3_sitelib}/key_value
%{python3_sitelib}/key_value/shared
%{python3_sitelib}/py_key_value_shared-%{version}.dist-info
%exclude %{python3_sitelib}/key_value/shared_test
%exclude %{python3_sitelib}/py_key_value_shared_test-%{version}.dist-info


%files -n python3-py-key-value-aio
# We don't need to duplicate the license here, because this subpackage requires
# py-key-value-shared which has the license, similar to a libs/devel split.
%{python3_sitelib}/key_value/aio
%{python3_sitelib}/py_key_value_aio-%{version}.dist-info


%changelog
%autochangelog
