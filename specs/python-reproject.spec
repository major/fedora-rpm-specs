%global srcname reproject
%global sum Reproject astronomical images

Name:           python-%{srcname}
Version:        0.15.0
Release:        %autorelease
Summary:        %{sum}

License:        BSD-3-Clause
URL:            https://reproject.readthedocs.io/
Source0:        %{pypi_source}

# Backport upstream patch which removes the upper Cython version bound
# https://github.com/astropy/reproject/commit/27aee71380bbdd29fefec6f0319d5b21bbc590d5
#Patch:          fix-cython-pin.patch

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
%ifarch aarch64
%pyproject_check_import -e '*.test*'
%else
# https://github.com/astropy/reproject/issues/552
pushd %{buildroot}/%{python3_sitearch}
  %pytest \
   --deselect "reproject/interpolation/tests/test_core.py::test_reproject_parallel_broadcasting" \
   reproject
popd
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc CHANGES.md README.rst

%changelog
%autochangelog
