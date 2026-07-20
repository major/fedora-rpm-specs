Name:           wgrib
Version:        1.8.5
Release:        %autorelease
Summary:        Manipulate, inventory and decode GRIB files

License:        LicenseRef-Fedora-Public-Domain
URL:            https://www.cpc.ncep.noaa.gov/products/wesley/wgrib.html
Source0:        https://ftp.cpc.ncep.noaa.gov/wd51we/wgrib/wgrib.c.v%{version}
Source1:        https://ftp.cpc.ncep.noaa.gov/wd51we/wgrib/Changes
Source2:        https://ftp.cpc.ncep.noaa.gov/wd51we/wgrib/NOTICE
Source3:        https://ftp.cpc.ncep.noaa.gov/wd51we/wgrib/double_prec.txt
Source4:        https://ftp.cpc.ncep.noaa.gov/wd51we/wgrib/formats.txt
Source5:        https://ftp.cpc.ncep.noaa.gov/wd51we/wgrib/formats_update.txt
Source6:        https://ftp.cpc.ncep.noaa.gov/wd51we/wgrib/grib2ieee.txt
Source7:        https://ftp.cpc.ncep.noaa.gov/wd51we/wgrib/misc.txt
Source8:        https://ftp.cpc.ncep.noaa.gov/wd51we/wgrib/porting.txt
Source9:        https://ftp.cpc.ncep.noaa.gov/wd51we/wgrib/usertables.txt
Source10:       https://ftp.cpc.ncep.noaa.gov/wd51we/wgrib/tricks.wgrib
Source11:       https://ftp.cpc.ncep.noaa.gov/wd51we/wgrib/land.grb
Source12:       https://ftp.cpc.ncep.noaa.gov/wd51we/wgrib/testbin.c
Source13:       https://ftp.cpc.ncep.noaa.gov/wd51we/wgrib/testbin.f
Source14:       testbin.out
# Include <stdlib.h> and set int return for main() for C99 compliance
Patch0:         wgrib-c99.patch
BuildRequires:  gcc
ExcludeArch:    %{ix86}


%description
WGRIB is a program to manipulate, inventory and decode GRIB files.


%prep
%setup -q -c -T
cp %SOURCE0 wgrib.c
cp %SOURCE1 .
cp %SOURCE2 .
cp %SOURCE3 .
cp %SOURCE4 .
cp %SOURCE5 .
cp %SOURCE6 .
cp %SOURCE7 .
cp %SOURCE8 .
cp %SOURCE9 .
cp %SOURCE10 .
cp %SOURCE11 .
cp %SOURCE12 .
cp %SOURCE13 .
%patch -P0 -p0 -b .c99


%build
gcc %{build_cflags} %{build_ldflags} -o wgrib wgrib.c


%install
install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -m 755 wgrib $RPM_BUILD_ROOT%{_bindir}/


%check
./wgrib land.grb -d 1
gcc %{build_cflags} %{build_ldflags} -o testbin testbin.c -lm
./testbin > testbin.out && diff %SOURCE14 testbin.out



%files
%doc Changes *.txt tricks.wgrib testbin.[cf] land.grb
%{_bindir}/wgrib


%changelog
%autochangelog
