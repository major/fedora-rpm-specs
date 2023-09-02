Name:           python-h5io
Version:        0.1.9
Release:        %autorelease
Summary:        Read and write simple Python objects using HDF5

License:        BSD-3-Clause
URL:            https://github.com/h5io/h5io
Source:         %{url}/archive/h5io-%{version}/h5io-h5io-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

# README.rst: ``scipy`` is required for sparse matrix IO support.
BuildRequires:  python3dist(scipy)

BuildRequires:  python3dist(pytest)

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
sed -r -i 's/--cov[^[:blank:]=]*=[^[:blank:]]*//g' setup.cfg


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files h5io


%check
%pytest -v


%files -n python3-h5io -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
