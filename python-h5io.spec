Name:           python-h5io
Version:        0.1.7
Release:        %autorelease
Summary:        Read and write simple Python objects using HDF5

# The entire source is BSD-3-Clause, except:
#   CC0-1.0: versioneer.py and the _version.py it generates; while CC0-1.0 is
#            not allowed for code, these fall under the exception for code
#            present in Fedora prior to 2022-08-01:
# https://gitlab.com/fedora/legal/fedora-license-data/-/issues/91#note_1151947383
#            When upstream updates to versioneer 0.24 or later, this will
#            change to Unlicense.
License:        BSD-3-Clause AND CC0-1.0
URL:            https://github.com/h5io/h5io
Source0:        %{url}/archive/h5io-%{version}/h5io-h5io-%{version}.tar.gz
# Part of https://github.com/h5io/h5io/pull/57
# Part of https://github.com/h5io/h5io/pull/57/commits/a926916a95a1bcd219da953922e8f729843f69ee
# Modified the above commit to apply cleanly
# Rebased on 0.1.7
# numpy 1.24 removes np.bool, use system bool type
Patch:          python-h5io-a926916a-numpy-1_24-compat.patch

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
