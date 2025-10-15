%global srcname cftime

Name:           python-%{srcname}
Version:        1.6.5
Release:        %autorelease
Summary:        Time-handling functionality from netcdf4-python

# calendar calculation routines in _cftime.pyx derived from calcalcs.c by David
# W. Pierce with GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
# Automatically converted from old format: MIT and GPLv3 - review is highly recommended.
License:        LicenseRef-Callaway-MIT AND GPL-3.0-only
URL:            https://pypi.python.org/pypi/cftime
Source0:        %{pypi_source}

BuildRequires:  gcc

%description
Time-handling functionality from netcdf4-python.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
# For tests
BuildRequires:  python%{python3_pkgversion}-pytest

%description -n python%{python3_pkgversion}-%{srcname}
Time-handling functionality from netcdf4-python.

%prep
%autosetup -n %{srcname}-%{version}
sed -i -e '/--cov/d' setup.cfg

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
%pytest -v

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
