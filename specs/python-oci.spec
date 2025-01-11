%bcond_without  tests

%global         reponame    oci-python-sdk
%global         srcname     oci

Name:           python-%{srcname}
Version:        2.141.1
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

%if %{with tests}
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(vcrpy)
%endif

%global _description %{expand:
This is the Python SDK for Oracle Cloud Infrastructure. }

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}

%prep
%autosetup -n %{reponame}-%{version} -p1

# Remove upper limits and pinned dependencies.
sed -i -e 's/,[<= ]\+[0-9\.]\+//' -e 's/==/>=/' setup.py

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
%pyproject_check_import

%if %{with tests}
%pytest tests/autogentest tests/unit tests/integ
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.txt THIRD_PARTY_LICENSES.txt THIRD_PARTY_LICENSES_DEV.txt
%doc CHANGELOG.rst CONTRIBUTING.rst README.rst README-development.rst


%changelog
%autochangelog
