%global srcname astroscrappy 
%global common_desc Astro-SCRAPPY is designed to detect cosmic rays in images (numpy arrays).

Name:           python-%{srcname}
Version:        1.2.0
Release:        %autorelease
Summary:        Cosmic Ray Annihilation

License:        BSD-3-Clause
URL:            https://pypi.python.org/pypi/%{srcname}
Source:         %{pypi_source}

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
%autosetup -p1 -n %{srcname}-%{version}

# Fedora doesn't have numpy 2.0 yet
# but tests seem ok to use current version
sed -i pyproject.toml -e 's|"numpy>=2.0.0rc1"|"numpy"|'

%generate_buildrequires
%pyproject_buildrequires -x test


%build
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