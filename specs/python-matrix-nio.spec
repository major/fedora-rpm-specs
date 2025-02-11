Name:           python-matrix-nio
Version:        0.25.2
Release:        %autorelease
Summary:        A Matrix client library

# ASL:
# matrix_nio-0.21.2//nio/crypto/attachments.py: Apache License 2.0
# matrix_nio-0.21.2//nio/crypto/key_export.py: Apache License 2.0
# matrix_nio-0.21.2//nio/store/database.py: Apache License 2.0
# matrix_nio-0.21.2//nio/store/models.py: Apache License 2.0

# All other files: ISC

License:        ISC and Apache-2.0
URL:            https://pypi.python.org/pypi/matrix-nio
Source0:        %{pypi_source matrix_nio}

BuildArch:      noarch

%global _description %{expand:
nio is a multilayered Matrix client library. The underlying base layer doesn't
do any network IO on its own, but on top of that is a full fledged
batteries-included asyncio layer using aiohttp. File IO is only done if you
enable end-to-end encryption (E2EE).}

%description %_description

%package -n python3-matrix-nio
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-toml
BuildRequires:  python3-logbook

%description -n python3-matrix-nio %_description

%prep
%autosetup -n matrix_nio-%{version}
# Update BRs
sed \
    -e 's/"aiohttp-socks.*"/"aiohttp-socks"/' \
    -e 's/"aiofiles.*"/"aiofiles"/' \
    -e 's/"cachetools.*"/"cachetools"/' \
    -e 's/"h11.*"/"h11"/' \
    -e 's/"h2.*"/"h2"/' \
    -e 's/"pycryptodome.*"/"pycryptodomex"/' \
    -e 's/"jsonschema.*"/"jsonschema"/' \
    -i pyproject.toml

# Remove backup file
rm -fv nio/events/room_events.py.orig

# use cryptodomex instead of crypto
# https://bugzilla.redhat.com/show_bug.cgi?id=2061832
find . -name "*.py" -exec sed -i 's/^from Crypto/from Cryptodome/'  '{}' \;


%generate_buildrequires
%pyproject_buildrequires -x e2e

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files nio

%check
%pyproject_check_import

%files -n python3-matrix-nio  -f %{pyproject_files}
%license LICENSE.md
%doc README.md

%changelog
%autochangelog
