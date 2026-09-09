%global pypi_name astropy-healpix
%global srcname astropy_healpix
%global modname astropy_healpix

Name:           python-%{pypi_name}
Version:        2.0.1
Release:        %autorelease
Summary:        HEALPix for Astropy

License:        BSD-3-Clause
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        %{pypi_source %{srcname}}
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:  gcc
BuildRequires:  python3-devel

%global _description %{expand:
This is a BSD-licensed Python package for HEALPix, which is based on the C
HEALPix code written by Dustin Lang originally in astrometry.net, and was
added here with a Cython wrapper and expanded with a Python interface.}

%description %_description


%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{srcname}-%{version} -p1

# Remove egg files from source
rm -r %{modname}.egg-info

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname}

%check
export PYTEST_ADDOPTS='-p no:cacheprovider'
pushd %{buildroot}/%{python3_sitearch}
%pytest \
%ifarch aarch64
--deselect "astropy_healpix/tests/test_healpy.py::test_ang2pix" \
--deselect "astropy_healpix/tests/test_healpy.py::test_ring2nest" \
--deselect "astropy_healpix/tests/test_healpy.py::test_interp_weights" \
--deselect "astropy_healpix/tests/test_healpy.py::test_ang2vec" \
%endif
%ifarch riscv64
--deselect "astropy_healpix/tests/test_healpy.py::test_pix2ang" \
--deselect "astropy_healpix/tests/test_healpy.py::test_pix2vec" \
--deselect "astropy_healpix/tests/test_healpy.py::test_ang2vec" \
%endif
%ifarch s390x
--deselect "astropy_healpix/tests/test_healpy.py::test_ang2vec" \
%endif
%{modname}

# Hypothesis tests creates some files in sitearch... we remove them now
rm -rf .hypothesis
popd

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE.md
%doc README.rst

%changelog
%autochangelog
