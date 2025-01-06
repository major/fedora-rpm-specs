# This package requires astropy which requires astropy-iers-data
# The loop has to be broken for the bootstrap of a new Python in Fedora
%bcond tests 1

%global upname astropy-iers-data
%global srcname astropy_iers_data

Name: python-%{upname}
Version: 0.2024.12.30.0.33.36
Release: %autorelease
Summary: IERS Earth Rotation and Leap Second tables for the astropy core package
License: BSD-3-Clause

URL: https://github.com/astropy/astropy-iers-data
Source: %{pypi_source %{srcname}}

BuildArch: noarch
BuildRequires:  python3-devel

%global _description %{expand:
This package provides IERS Earth Rotation and Leap Second tables for the
astropy.utils.iers package.

There the following IERS data products are included:

* Bulletin A (IERS_A) is updated weekly and has historical data starting from
  1973 and predictive data for 1 year into the future. It contains Earth
  orientation parameters x/y pole, UT1-UTC and their errors at daily intervals.

* Bulletin B (IERS_B) is updated monthly and has data from 1962 up to the time
  when it is generated. This file contains Earth’s orientation in the IERS
  Reference System including Universal Time, coordinates of the terrestrial
  pole, and celestial pole offsets.

The package also provides leap second data.

Note: This package is not currently meant to be used directly by users, and
only meant to be used from the core Astropy package.}
%description %_description

%package -n python3-%{upname}
Summary: %{summary}

%description -n python3-%{upname}
%_description

%prep
%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-t -x test}

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l astropy_iers_data

%check
%pyproject_check_import
%if %{with tests}
%{tox}
%endif

%files -n python3-%{upname} -f %{pyproject_files}
%doc README.rst 

%changelog
%autochangelog
