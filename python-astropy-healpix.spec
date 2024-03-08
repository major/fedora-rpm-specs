%global srcname astropy-healpix
%global modname astropy_healpix

Name:           python-%{srcname}
Version:        1.0.2
Release:        %autorelease
Summary:        HEALPix for Astropy

License:        BSD-3-Clause
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        %{pypi_source astropy_healpix}
# https://github.com/astropy/astropy-healpix/issues/183
# https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1026012
# https://salsa.debian.org/debian-astro-team/astropy-healpix/-/blob/master/debian/patches/Temporarily-disable-tests-that-fail-due-to-limited-FP-pre.patch
Patch0:         astropy_healpix-0.7-disable-FP-limited-test.patch

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
#
BuildRequires:  %{py3_dist pytest-astropy}
# BuildRequires for tests, healpy only available on 64 bit architectures,
# thus these tests are skipped on 32 bit
%ifnarch %{ix86} %{arm}
BuildRequires:  %{py3_dist healpy}
%endif

%description
This is a BSD-licensed Python package for HEALPix, which is based on the C
HEALPix code written by Dustin Lang originally in astrometry.net, and was
added here with a Cython wrapper and expanded with a Python interface.


%package -n python3-%{srcname}
Summary: %{summary}

%description -n python3-%{srcname}
%{description}

%prep
%autosetup -n %{modname}-%{version} -p1

# Remove egg files from source
rm -r %{modname}.egg-info

%generate_buildrequires
%pyproject_buildrequires 

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

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.md
%doc README.rst

%changelog
%autochangelog
