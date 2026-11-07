Name:           python-h5io
Version:        0.2.6
Release:        %autorelease
Summary:        Read and write simple Python objects using HDF5

License:        BSD-3-Clause
URL:            https://github.com/h5io/h5io
Source:         %{url}/archive/h5io-%{version}/h5io-h5io-%{version}.tar.gz

BuildArch:      noarch

# README.rst: ``scipy`` is required for sparse matrix IO support.
BuildRequires:  python3dist(scipy)

BuildRequires:  python3dist(pytest)
# Enables an additional integration test
BuildRequires:  python3dist(tables)

%global common_description %{expand:
h5io is a package designed to facilitate saving some standard Python objects
into the forward-compatible HDF5 format. It is a higher-level package than
h5py.}

%description %{common_description}


%package -n python3-h5io
Summary:        %{summary}

# README.rst: ``scipy`` is required for sparse matrix IO support.
Recommends:     python%{python3_version}dist(scipy)

%description -n python3-h5io %{common_description}


%prep
%autosetup -n h5io-h5io-%{version} -p1

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i 's/--cov[^[:blank:]"=]*(=[^[:blank:]"]*)?//g' pyproject.toml

# Normally, vcs_versioning should be an indirect dependency via setuptools_scm.
# Upstream depends on it directly solely to avoid version 2.0.1. The problem is
# that vcs_versioning was introduced relatively recently, and Fedora releases
# with older setuptools_scm versions (before F45) do not have vcs_versioning.
# The sensible solution is to remove the direct dependency.
%pyproject_patch_dependency vcs_versioning:ignore


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l h5io


%check
%pytest --verbose


%files -n python3-h5io -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
