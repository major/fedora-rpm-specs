%global macrosdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)

Name:           g2clib
Version:        2.3.0
Release:        %autorelease
Summary:        GRIB2 encoder/decoder and search/indexing routines in C

License:        LGPL-3.0-only
URL:            https://github.com/NOAA-EMC/NCEPLIBS-g2c
Source0:        https://github.com/NOAA-EMC/NCEPLIBS-g2c/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  doxygen
BuildRequires:  jasper-devel
BuildRequires:  libaec-devel
BuildRequires:  libpng-devel
ExcludeArch:    %{ix86}

%global g2clib g2c

%description
This library contains "C" decoder/encoder
routines for GRIB edition 2.  The user API for the GRIB2 routines
is described in ASCII file "grib2c.doc".


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
# The cmake target requires the static library to be present
Requires:       %{name}-static = %{version}-%{release}
Requires:       jasper-devel%{?_isa}
Requires:       libpng-devel%{?_isa}

%description    devel
This library contains "C" decoder/encoder
routines for GRIB edition 2.  The user API for the GRIB2 routines
is described in file "grib2c.doc".

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        static
Summary:        Static library for %{name}
Requires:       %{name}-devel = %{version}-%{release}

%description    static
This library contains "C" decoder/encoder
routines for GRIB edition 2.  The user API for the GRIB2 routines
is described in file "grib2c.doc".

The %{name}-static package contains the g2c static library.


%package        utils
Summary:        %{name} utilities
Requires:       %{name} = %{version}-%{release}

%description    utils
The %{name}-utils package contains utilities for g2clib.


%prep
%autosetup -p1 -n NCEPLIBS-g2c-%{version}


%build
%cmake -DENABLE_DOCS=ON \
  -DUSE_AEC=ON \
  -DPTHREADS=ON
%cmake_build


%install
mkdir -p $RPM_BUILD_ROOT%{macrosdir}
echo %%g2clib %g2clib > $RPM_BUILD_ROOT%{macrosdir}/macros.g2clib
%cmake_install


%check
# Tests fail on s390x https://github.com/NOAA-EMC/NCEPLIBS-g2c/issues/586
%ifarch s390x
%ctest --verbose || :
%else
%ctest --verbose
%endif


%files
%license LICENSE.md
%doc README.md
%{_libdir}/lib%{g2clib}.so.0
%{_datadir}/g2c/

%files devel
%{_libdir}/cmake/g2c/
%{_libdir}/lib%{g2clib}.so
%{_includedir}/grib2.h

%files static
%{_libdir}/lib%{g2clib}.a
%{macrosdir}/macros.g2clib

%files utils
%{_bindir}/g2c_compare
%{_bindir}/g2c_degrib2
%{_bindir}/g2c_index


%changelog
%autochangelog
