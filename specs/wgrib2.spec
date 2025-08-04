%global commit 2c9bfe3c1132e8c97d54b92987532276ba80c4fd

Name:           wgrib2
Version:        3.7.0
Release:        %autorelease
Summary:        Manipulate, inventory and decode GRIB2 files

# most files are public domain, geo.c and Netcdf.c are GPL+, gribtab.c is GPLv2+
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://www.cpc.ncep.noaa.gov/products/wesley/wgrib2/
Source0:        https://github.com/NOAA-EMC/wgrib2/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  g2clib-devel >= 2.0
BuildRequires:  hdf5-devel
BuildRequires:  libaec-devel
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  netcdf-devel
BuildRequires:  cmake(OpenJPEG)
BuildRequires:  zlib-devel
ExcludeArch:    %{ix86}

%description
Wgrib2 is a swiss army knife for grib2 files. You can use it inventory or
extract data. You can do basic database operations and other nifty things.


%package devel
Summary:        Development files for wgrib2

%description devel
Development files for wgrib2.


%prep
%autosetup -p1 -n %{name}-%{version}


%build
export CFLAGS="$RPM_OPT_FLAGS -I%{_includedir}/mysql -std=gnu17"
export LDFLAGS="-lmysqlclient"
%cmake -DCMAKE_INSTALL_Fortran_MODULES=%{_fmoddir} \
  -DENABLE_DOCS=ON \
  -DUSE_NETCDF=ON \
  -DUSE_MYSQL=ON \
  -DUSE_OPENMP=ON \
  -DUSE_G2CLIB=ON \
  -DUSE_AEC=ON \
  -DMAKE_FTN_API=ON \
  -DUSE_OPENJPEG=ON
%cmake_build


%install
%cmake_install


%files
%doc README.md wgrib2/LICENSE-wgrib2
%{_bindir}/wgrib2

%files devel
%{_includedir}/wgrib2.h
%{_includedir}/wgrib2_api.h
%{_includedir}/wgrib2_meta.h
%{_fmoddir}/wgrib2api.mod
%{_fmoddir}/wgrib2lowapi.mod
%{_libdir}/cmake/wgrib2/
%{_libdir}/libwgrib2.so
%{_libdir}/libwgrib2_ftn_api.so


%changelog
%autochangelog
