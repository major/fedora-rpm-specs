%global srcname fitsio
%global sum A full featured python library to read from and write to FITS files


Name:           python-%{srcname}
Version:        1.2.5
Release:        %autorelease
Summary:        %{sum}

License:        GPL-2.0-only
URL:            https://github.com/esheldon/fitsio
Source0:        %{pypi_source}

# General
BuildRequires:  cfitsio-devel
BuildRequires:  zlib-devel
BuildRequires:  gcc
# Python 3
BuildRequires:  python3-devel

%global _description %{expand:
This is a python extension written in c and python. Data are read 
into numerical python arrays.}


%description %_description

%package -n python3-%{srcname}
Summary:        %{sum}
BuildRequires: %{py3_dist pytest}
Requires: %{py3_dist pytest}

%description -n python3-%{srcname} %_description

%prep
FITSIO_USE_SYSTEM_FITSIO=""
export FITSIO_USE_SYSTEM_FITSIO
FITSIO_SYSTEM_FITSIO_INCLUDEDIR="%{_includedir}/cfitsio"
export FITSIO_SYSTEM_FITSIO_INCLUDEDIR
FITSIO_SYSTEM_FITSIO_LIBDIR="%{_libdir}"
export FITSIO_SYSTEM_FITSIO_LIBDIR
%autosetup -p1 -n %{srcname}-%{version}

# Remove egg files from source
rm -r %{srcname}.egg-info
# Remove bundled cfitsio, to be sure we are not using it
rm -rf cfitsio-*

%generate_buildrequires
%pyproject_buildrequires


%build
FITSIO_USE_SYSTEM_FITSIO=""
export FITSIO_USE_SYSTEM_FITSIO
FITSIO_SYSTEM_FITSIO_INCLUDEDIR="%{_includedir}/cfitsio"
export FITSIO_SYSTEM_FITSIO_INCLUDEDIR
FITSIO_SYSTEM_FITSIO_LIBDIR="%{_libdir}"
export FITSIO_SYSTEM_FITSIO_LIBDIR
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files fitsio


%check
pushd %{buildroot}/%{python3_sitearch}
  %pytest fitsio
  rm -rf .pytest_cache
popd


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.txt
%doc README.md


%changelog
%autochangelog
