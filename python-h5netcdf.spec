%bcond_without check

%global srcname h5netcdf

Name: python-%{srcname}
Version: 1.2.0
Release: %autorelease
Summary: Python interface for the netCDF4 file-format in HDF5 files
License: BSD

URL: https://h5netcdf.org/
Source0: %{pypi_source}

BuildArch: noarch
BuildRequires:  python3-devel

%global _description %{expand:
A Python interface for the netCDF4 file-format that reads and writes 
local or remote HDF5 files directly via h5py or h5pyd, without relying 
on the Unidata netCDF library.}     

%description %_description

%package -n python3-%{srcname}
Summary: %{summary}

%description -n python3-%{srcname}
%_description

%prep
%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
# Testing
%if %{with check}
%pyproject_buildrequires -x test
%else
%pyproject_buildrequires 
%endif

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files h5netcdf

%check
%if %{with check}
%pytest
%else
%pyproject_check_import -e '*.test*'
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst AUTHORS.txt

%changelog
%autochangelog

