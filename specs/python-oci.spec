%bcond_without  tests

%global         reponame    oci-python-sdk
%global         srcname     oci

Name:           python-%{srcname}
Version:        2.190.0
Release:        %autorelease
Summary:        Oracle Cloud Infrastructure SDK for Python

License:        UPL-1.0
URL:            https://github.com/oracle/oci-python-sdk
Source0:        %{url}/archive/v%{version}/%{reponame}-%{version}.tar.gz

# Upstream tries to import a non-existent 'vcr_mods' module.
# https://github.com/oracle/oci-python-sdk/pull/253
Patch0:         https://patch-diff.githubusercontent.com/raw/oracle/oci-python-sdk/pull/253.patch

BuildArch:      noarch

BuildRequires:  python3-devel

# Upstream imports crc32c unconditionally in oci.object_storage but does not
# declare it in pyproject.toml, so it is neither pulled by
# %%pyproject_buildrequires nor auto-generated as a runtime dependency.
# oci/object_storage/transfer/internal/additional_checksum.py imports crc32c.
BuildRequires:  python3dist(crc32c)

# Upstream imports six unconditionally but does not declare it in pyproject.toml,
# so it is not pulled into build requirements or generated runtime requirements.
BuildRequires:  python3dist(six)

%if %{with tests}
BuildRequires:  python3dist(docstring-parser)
BuildRequires:  python3dist(pydantic)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(rich)
BuildRequires:  python3dist(vcrpy)
%endif

%global _description %{expand:
This is the Python SDK for Oracle Cloud Infrastructure. }

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

# Undeclared upstream dependency (imported in oci.object_storage). See the
# BuildRequires comment above.
Requires:       python3dist(crc32c)
Requires:       python3dist(six)

%description -n python3-%{srcname} %{_description}

%prep
%autosetup -n %{reponame}-%{version} -p1

# Remove upper limits and pinned dependencies.
sed -i -e 's/,[<= ]\+[0-9\.]\+//' -e 's/==/>=/' pyproject.toml

# Fedora has no python-pkcs11 package and nothing provides
# python3dist(python-pkcs11). Upstream treats it as an optional dependency:
# the import is wrapped in try/except in oci/auth/signers/__init__.py, so
# the SDK imports and works without it. Only the PKCS#11 signers are
# unavailable until python-pkcs11 is packaged in Fedora.
sed -i '/python-pkcs11/d' pyproject.toml

# Compatibility with pytest 7.4.0
# reported upstream: https://github.com/oracle/oci-python-sdk/issues/565
sed -i 's/--config-file/--config-file-path/' tests/conftest.py

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
# oci.auth.signers.pkcs11_signer imports the unpackaged python-pkcs11 module.
%pyproject_check_import -e 'oci.addons.*' -e 'oci.auth.signers.pkcs11_signer'

%if %{with tests}
%pytest tests/autogentest tests/unit tests/integ
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.txt THIRD_PARTY_LICENSES.txt THIRD_PARTY_LICENSES_DEV.txt
%doc CHANGELOG.rst CONTRIBUTING.rst README.rst README-development.rst


%changelog
%autochangelog
