Name:           netcdf4-python
Version:        1.7.5
Release:        %autorelease
Summary:        Python/numpy interface to netCDF

License:        MIT
URL:            https://github.com/Unidata/netcdf4-python
Source0:        https://github.com/Unidata/netcdf4-python/archive/refs/tags/v%{version}rel/%{name}-%{version}.tar.gz
# No rpath for library
# https://github.com/Unidata/netcdf4-python/issues/138
Patch0:         netcdf4-python-norpath.patch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  netcdf-devel
Requires:       python%{python3_pkgversion}-netcdf4 = %{version}-%{release}

%description
netCDF version 4 has many features not found in earlier versions of the
library and is implemented on top of HDF5. This module can read and write
files in both the new netCDF 4 and the old netCDF 3 format, and can create
files that are readable by HDF5 clients. The API modeled after
Scientific.IO.NetCDF, and should be familiar to users of that module.

Most new features of netCDF 4 are implemented, such as multiple unlimited
dimensions, groups and zlib data compression. All the new numeric data types
(such as 64 bit and unsigned integer types) are implemented. Compound and
variable length (vlen) data types are supported, but the enum and opaque data
types are not. Mixtures of compound and vlen data types (compound types
containing vlens, and vlens containing compound types) are not supported.


%package -n python%{python3_pkgversion}-netcdf4
Summary:        Python/numpy interface to netCDF

%description -n python%{python3_pkgversion}-netcdf4
netCDF version 4 has many features not found in earlier versions of the
library and is implemented on top of HDF5. This module can read and write
files in both the new netCDF 4 and the old netCDF 3 format, and can create
files that are readable by HDF5 clients. The API modeled after
Scientific.IO.NetCDF, and should be familiar to users of that module.

Most new features of netCDF 4 are implemented, such as multiple unlimited
dimensions, groups and zlib data compression. All the new numeric data types
(such as 64 bit and unsigned integer types) are implemented. Compound and
variable length (vlen) data types are supported, but the enum and opaque data
types are not. Mixtures of compound and vlen data types (compound types
containing vlens, and vlens containing compound types) are not supported.


%prep
%autosetup -p1 -n %{name}-%{version}rel


%generate_buildrequires
%pyproject_buildrequires -g test


%build
# Set to get libs from ncconfig to avoid directly linking to -lhdf5
export USE_NCCONFIG=1
# This causes the plugins to be duplicated into the python package
# https://github.com/Unidata/netcdf4-python/issues/1263
#export NETCDF_PLUGIN_DIR=%%{_libdir}/hdf5/plugin
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l netCDF4

 
%check
cd test
export NO_NET=1
%ifarch s390x
# FAIL: runTest (tst_compoundvar.VariablesTestCase) -> assert (cmptype4 == dtype4a) # data type should be aligned
# https://github.com/Unidata/netcdf4-python/issues/1124
PYTHONPATH=$(echo ../build/lib.linux-*) %{__python3} run_all.py || :
%else
PYTHONPATH=$(echo ../build/lib.linux-*) %{__python3} run_all.py
%endif


%files
%license LICENSE
%{_bindir}/nc3tonc4
%{_bindir}/nc4tonc3
%{_bindir}/ncinfo


%files -n python%{python3_pkgversion}-netcdf4 -f %{pyproject_files}
%doc Changelog docs examples README.md


%changelog
%autochangelog
