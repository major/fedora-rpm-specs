%bcond tests 1
# Excluded extras:
# - docs: build-time documentation group
# - aerospike, chdb, duckdb, dynamodb, firestore, memcached, rocksdb, s3,
#   valkey, vault: dependencies not yet packaged in Fedora
%global extras azure-tables,disk,elasticsearch,filetree,keyring,keyring-linux,memory,mongodb,opensearch,postgresql,pydantic,redis,vault,wrappers-encryption

Name:           python-py-key-value-aio
Version:        0.4.6
Release:        %autorelease
Summary:        Async Key-Value Store - A pluggable interface for KV Stores

License:        Apache-2.0
URL:            https://github.com/strawgate/py-key-value
Source:         %{url}/archive/%{version}/py-key-value-aio-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  tomcli


%if %{with tests}
BuildRequires:  python3-dirty-equals
BuildRequires:  python3-inline-snapshot
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio
BuildRequires:  python3-pytest-xdist
%endif

%global _description %{expand:
py-key-value-aio provides a pluggable, type-safe asynchronous interface for
key-value stores. It enables applications and frameworks to interact with
multiple storage backends (including in-memory, disk, OS secret stores, and
distributed databases such as Redis, Valkey, DynamoDB, and MongoDB) through a
unified protocol.

Key features include automatic TTL expiration, logical collections and
namespaces, type-safe adapters (such as Pydantic and dataclasses), and
stackable wrappers for caching, compression, encryption, retries, and
statistics tracking.}

%description %_description

%package -n     python3-py-key-value-aio
Summary:        %{summary}

%description -n python3-py-key-value-aio %_description

%pyproject_extras_subpkg -n python3-py-key-value-aio %{extras}


%prep
%autosetup -p1 -n py-key-value-%{version}
# Relax upper version bound on uv_build to allow building with >= 0.12
tomcli set pyproject.toml arrays replace -t regex_search build-system.requires '(uv_build\b[^,]*),\s*<0\.12' '\1'

# At runtime, dropping types-hvac causes no issues at all
tomcli set pyproject.toml arrays delitem 'project.optional-dependencies.vault' '^types-hvac\b.*'


%generate_buildrequires
%pyproject_buildrequires -x %{extras}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l key_value


%check
# Skip import checks for unpackaged optional backends
%pyproject_check_import -e 'key_value.aio.stores.aerospike*' -e 'key_value.aio.stores.chdb*' -e 'key_value.aio.stores.duckdb*' -e 'key_value.aio.stores.dynamodb*' -e 'key_value.aio.stores.firestore*' -e 'key_value.aio.stores.memcached*' -e 'key_value.aio.stores.rocksdb*' -e 'key_value.aio.stores.s3*' -e 'key_value.aio.stores.valkey*' -e 'key_value.aio.stores.windows_registry*'


%if %{with tests}
pytest_opts=(
    # Skip test for the extra dependencies we do not package
    --ignore="tests/stores/aerospike"
    --ignore="tests/stores/chdb"
    --ignore="tests/stores/duckdb"
    --ignore="tests/stores/dynamodb"
    --ignore="tests/stores/firestore"
    --ignore="tests/stores/memcached"
    --ignore="tests/stores/rocksdb"
    --ignore="tests/stores/s3"
    --ignore="tests/stores/valkey"
    --ignore="tests/stores/windows_registry"

    # Skip test that relies on testcontainers which can't be run in the Koji/mock build environments
    --ignore="tests/stores/azure_tables"
    --ignore="tests/stores/elasticsearch"
    --ignore="tests/stores/mongodb"
    --ignore="tests/stores/opensearch"
    --ignore="tests/stores/postgresql"
    --ignore="tests/stores/redis"
    --ignore="tests/stores/valkey"
    --ignore="tests/stores/vault"
)
%pytest "${pytest_opts[@]}"
%endif


%files -n python3-py-key-value-aio -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
