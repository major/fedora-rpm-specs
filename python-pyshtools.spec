%global srcname pyshtools

%if 0%{?fedora} || 0%{?rhel} >= 9
%global blaslib flexiblas
%else
%global blaslib openblas
%endif

Name:           python-%{srcname}
Version:        4.11.10
Release:        %autorelease
Summary:        Tools for working with spherical harmonics

License:        BSD-3-Clause
URL:            https://shtools.github.io/SHTOOLS/
Source0:        %pypi_source %{srcname}
# https://github.com/SHTOOLS/SHTOOLS/pull/448
Patch:          0001-Remove-cartopy-build-time-dependencies.patch
# We don't need oldest-supported-numpy as NumPy is always built for "this" Python.
Patch:          0002-Use-normal-numpy-as-build-dependency.patch
# https://github.com/SHTOOLS/SHTOOLS/commit/f76fd884910829350e23beebdece9c38484b1ed1
Patch:          0003-Add-jupyter-to-build-system.requires.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  fftw3-devel
BuildRequires:  %{blaslib}-devel
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-f2py

# Runtime dependencies (we can't use automatic build requires due to build issues).
BuildRequires:  python3dist(scipy) >= 0.14
BuildRequires:  python3dist(matplotlib) >= 3.3
BuildRequires:  python3dist(astropy) >= 4
BuildRequires:  python3dist(xarray)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(pooch) >= 1.1
BuildRequires:  python3dist(tqdm)

# Optional dependencies.
BuildRequires:  python3dist(cartopy) >= 0.18
BuildRequires:  python3dist(ducc0) >= 0.15

%description
pysthools is a Python library that can be used to perform spherical
harmonic transforms and reconstructions, multitaper spectral analyses on
the sphere, expansions of functions into Slepian bases, and standard
operations on global gravitational and magnetic field data.


%package -n     python3-%{srcname}
Summary:        %{summary}
Recommends:     python3-%{srcname}+cartopy
Recommends:     python3-%{srcname}+ducc

%description -n python3-%{srcname}
pysthools is a Python library that can be used to perform spherical
harmonic transforms and reconstructions, multitaper spectral analyses on
the sphere, expansions of functions into Slepian bases, and standard
operations on global gravitational and magnetic field data.


%pyproject_extras_subpkg -n python3-%{srcname} cartopy ducc


%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -R

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel -Csetup-args=-Dblas=%{blaslib} -Csetup-args=-Dlapack=%{blaslib}

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
export MPLBACKEND=Agg %py3_test_envvars
make -C examples/python -f Makefile no-timing PYTHON=%{python3}

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
