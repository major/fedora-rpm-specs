Name:           netcdf-cxx
Version:        4.2
Release:        %autorelease
Summary:        Legacy netCDF C++ library

# Automatically converted from old format: NetCDF - review is highly recommended.
License:        BSD-3-Clause
URL:            http://www.unidata.ucar.edu/software/netcdf/
Source0:        ftp://ftp.unidata.ucar.edu/pub/netcdf/netcdf-cxx-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  netcdf-devel

%description
Legacy netCDF C++ library.  This library is provided for backward
compatibility only. New C++ development should be done with the netCDF
CXX4 C++ library.


%package devel
Summary:        Development files legacy netCDF C++ library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       netcdf-devel%{?_isa}

%description devel
This package contains the legacy netCDF C++ library header files and shared
devel library.


%package static
Summary:        Static libraries for legacy netCDF C++ library
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description static
This package contains the netCDF static libraries.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=${RPM_BUILD_ROOT}
/bin/rm ${RPM_BUILD_ROOT}%{_libdir}/*.la
/bin/rm ${RPM_BUILD_ROOT}%{_infodir}/dir


%check
make check


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc COPYRIGHT cxx/README
%{_libdir}/libnetcdf_c++.so.*

%files devel
%doc examples man4/%{name}.pdf
%{_includedir}/ncvalues.h
%{_includedir}/netcdf.hh
%{_includedir}/netcdfcpp.h
%{_libdir}/libnetcdf_c++.so
%{_infodir}/%{name}.info*

%files static
%{_libdir}/libnetcdf_c++.a


%changelog
%autochangelog
