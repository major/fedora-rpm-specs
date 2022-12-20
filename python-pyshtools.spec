%global srcname pyshtools

%if 0%{?fedora} || 0%{?rhel} >= 9
%global blaslib flexiblas
%else
%global blaslib openblas
%endif

Name:           python-%{srcname}
Version:        4.10.1
Release:        %autorelease
Summary:        Tools for working with spherical harmonics

License:        BSD
URL:            https://shtools.github.io/SHTOOLS/
Source0:        %pypi_source
# https://github.com/numpy/numpy/issues/20941
Patch:          0001-Add-default-include-path-for-FFTW.patch
# We don't need these requirements as Cartopy is already built.
Patch:          0002-Remove-cartopy-build-time-dependencies.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:  gcc
BuildRequires:  gcc-gfortran
BuildRequires:  fftw3-devel
BuildRequires:  %{blaslib}-devel
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-f2py

%description
pysthools is a Python library that can be used to perform spherical
harmonic transforms and reconstructions, multitaper spectral analyses on
the sphere, expansions of functions into Slepian bases, and standard
operations on global gravitational and magnetic field data.


%package -n     python3-%{srcname}
Summary:        %{summary}
Recommends:     python3-%{srcname}-cartopy
Recommends:     python3-%{srcname}-ducc

%description -n python3-%{srcname}
pysthools is a Python library that can be used to perform spherical
harmonic transforms and reconstructions, multitaper spectral analyses on
the sphere, expansions of functions into Slepian bases, and standard
operations on global gravitational and magnetic field data.


%pyproject_extras_subpkg -n python3-%{srcname} cartopy ducc


%prep
%autosetup -n %{srcname}-%{version}

# Don't make f2py silent.
sed -i -e '/f2py_options/d' setup.py

%generate_buildrequires
%pyproject_buildrequires -r -x cartopy,ducc

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
export MPLBACKEND=Agg
export PYTHONPATH=%{buildroot}%{python3_sitearch}
make -C examples/python -f Makefile no-timing PYTHON=%{python3}

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
