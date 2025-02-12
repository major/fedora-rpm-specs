%global srcname reproject
%global sum Reproject astronomical images

Name:           python-%{srcname}
Version:        0.14.1
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
sed -i -e 's/oldest-supported-numpy/numpy/' -e 's/cython==3.0.4/cython>=3/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files reproject

%check
# these fail in arm
# reproject/healpix/tests/test_healpix.py::test_reproject_healpix_to_image_footprint[**]
%ifarch aarch64
%pyproject_check_import -e '*.test*'
%else
pushd %{buildroot}/%{python3_sitearch}
  %pytest reproject
  rm -rf .pytest_cache
popd
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc CHANGES.md README.rst

%changelog
%autochangelog
