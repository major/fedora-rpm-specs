%global srcname astroscrappy 
%global common_desc Astro-SCRAPPY is designed to detect cosmic rays in images (numpy arrays).

Name:           python-%{srcname}
Version:        1.1.0
Release:        %autorelease
Summary:        Cosmic Ray Annihilation

License:        BSD-3-Clause
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        %{pypi_source}

BuildRequires:  gcc
ExcludeArch: %{ix86}

%description
%{common_desc}.

%package -n python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel

%description -n python3-%{srcname}
%{common_desc}.

%prep
%autosetup -n %{srcname}-%{version}

# Fedora doesn't have 'oldest-supported-numpy'
sed -i pyproject.toml -e 's|"oldest-supported-numpy"|"numpy"|'

%generate_buildrequires
%pyproject_buildrequires -x test


%build
# Force Cython re-run
echo "cython_version = 'unknown'" > astroscrappy/cython_version.py
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files astroscrappy

%check
%ifnarch s390x
export PYTEST_ADDOPTS='-p no:cacheprovider'
pushd %{buildroot}/%{python3_sitearch}
%pytest astroscrappy
popd
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%license licenses/LICENSE.rst
%doc CHANGES.rst README.rst

%changelog
%autochangelog
