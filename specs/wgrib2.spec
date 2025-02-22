Name:           wgrib2
Version:        3.1.3
Release:        %autorelease
Summary:        Manipulate, inventory and decode GRIB2 files

# most files are public domain, geo.c and Netcdf.c are GPL+, gribtab.c is GPLv2+
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.cpc.ncep.noaa.gov/products/wesley/wgrib2/
Source0:        http://ftp.cpc.ncep.noaa.gov/wd51we/wgrib2/wgrib2_nolib.tgz.v%{version}
Source1:        config.h
# Disable gctpc for now - bundled library
Patch0:         wgrib2-nogctpc.patch
# support jasper 2
Patch1:         wgrib2-jasper-2.patch
# jasper3 now hides internal encoder / decoder. Use wrapper entry point
# c.f. https://github.com/jasper-software/jasper/commit/5fe57ac5829ec31396e7eaab59a688da014660af
Patch2:         wgrib2-2.0.8-jasper3-use-wrapper-entry-point.patch

BuildRequires:  make
BuildRequires:  g2clib-static
BuildRequires:  hdf5-devel
BuildRequires:  libaec-devel
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  netcdf-devel
BuildRequires:  proj-devel
BuildRequires:  zlib-devel
ExcludeArch:    %{ix86}

%description
Wgrib2 is a swiss army knife for grib2 files. You can use it inventory or
extract data. You can do basic database operations and other nifty things.


%prep
%setup -q -n grib2
%patch -P 0 -p1 -b .nogctpc
%patch -P 1 -p1 -b .jasper2
%patch -P 2 -p1 -b .jasper3

rm wgrib2/fnlist.c
rm -r wgrib2/{Gctpc,gctpc_ll2xy,new_grid_lambertc}.[ch]
cp %SOURCE1 wgrib2/config.h


%build
cd wgrib2
# Fails to build with C23 https://github.com/NOAA-EMC/wgrib2/issues/309
export CFLAGS="-I.. -I%{_includedir}/netcdf -I%{_includedir}/mysql $RPM_OPT_FLAGS -fopenmp -std=gnu17"
export LDFLAGS="-l%{g2clib} -ljasper -lnetcdf -lpng -lmysqlclient -lsz -lz -lm -fopenmp"
%make_build fnlist.c
%make_build


%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install wgrib2/wgrib2 $RPM_BUILD_ROOT%{_bindir}/wgrib2


%files
%doc README wgrib2/LICENSE-wgrib2
%{_bindir}/wgrib2


%changelog
%autochangelog
