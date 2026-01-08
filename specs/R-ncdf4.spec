Name:           R-ncdf4
Version:        %R_rpm_version 1.24
Release:        %autorelease
Summary:        Interface to Unidata netCDF (Version 4 or Earlier) Format Data Files

License:        GPL-3.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel
BuildRequires:  netcdf-devel >= 4.1
BuildRequires:  chrpath

%description
Provides a high-level R interface to data files written using Unidata's netCDF
library (version 4 or earlier), which are binary data files that are portable
across platforms and include metadata information in addition to the data sets.
Using this package, netCDF files (either version 4 or "classic" version 3) can
be opened and data sets read in easily. It is also easy to create new netCDF
dimensions, variables, and files, in either version 3 or 4 format, and
manipulate existing netCDF files.

%prep
%autosetup -c
# Remove license about bundled (but not on Fedora) HDF5.
rm ncdf4/inst/HDF5_COPYING

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

# Fix rpath.
chrpath -d %{buildroot}%{_R_libdir}/ncdf4/libs/ncdf4.so

%check
%R_check

%files -f %{R_files}

%changelog
%autochangelog
