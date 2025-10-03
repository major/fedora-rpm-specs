%global srcname reproject
%global sum Reproject astronomical images

Name:           python-%{srcname}
Version:        0.16.0
Release:        %autorelease
Summary:        %{sum}

License:        BSD-3-Clause
URL:            https://reproject.readthedocs.io/
Source0:        %{pypi_source}

BuildRequires:  gcc

BuildRequires:  python3-devel

ExcludeArch: %{ix86}

%description
%{sum}.

%package -n python3-%{srcname}
Summary:        %{sum}

%description -n python3-%{srcname}
%{sum}.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files reproject

%check
export PYTEST_ADDOPTS='-p no:cacheprovider'
# these fail in arm
# reproject/healpix/tests/test_healpix.py::test_reproject_healpix_to_image_footprint[**]
# TestHIPSDaskArray uses remote data
%ifarch aarch64
%pyproject_check_import -e '*.test*'
%else
# https://github.com/astropy/reproject/issues/552
pushd %{buildroot}/%{python3_sitearch}
  %pytest \
   --deselect "reproject/interpolation/tests/test_core.py::test_reproject_parallel_broadcasting" \
   --deselect "reproject/hips/tests/test_dask_array.py::TestHIPSDaskArray::test_roundtrip"  \
   --deselect "reproject/hips/tests/test_dask_array.py::TestHIPSDaskArray::test_level_validation" \
   reproject
popd
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc CHANGES.md README.rst

%changelog
%autochangelog
