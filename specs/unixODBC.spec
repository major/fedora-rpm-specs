%bcond   gui_related_parts 1

Name:    unixODBC
Version: 2.3.14
Release: 5%{?dist}

# See README: Programs are GPL, libraries are LGPL
# News Server library (Drivers/nn/yyparse.c) is GPLv3+
# (but that one is not compiled nor shipped)
License: GPL-2.0-or-later AND LGPL-2.1-or-later

Summary: A complete ODBC driver manager for Linux
URL:     http://www.unixODBC.org/

Source:  http://www.unixODBC.org/%{name}-%{version}.tar.gz
Source1: odbcinst.ini

Patch8:  so-version-bump.patch
Patch9:  keep-typedefs.patch

BuildRequires: make automake autoconf libtool libtool-ltdl-devel bison flex
BuildRequires: readline-devel
BuildRequires: multilib-rpm-config

Conflicts: iodbc

Suggests: mariadb-connector-odbc
Suggests: mysql-connector-odbc
Suggests: postgresql-odbc
Suggests: unixODBC-gui-qt

%description
Install unixODBC if you want to access databases through ODBC.
You will also need the mariadb-connector-odbc package if you want to access
a MySQL or MariaDB database, and/or the postgresql-odbc package for PostgreSQL.

%package devel
Summary: Development files for programs which will use the unixODBC library
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The unixODBC package can be used to access databases through ODBC
drivers. If you want to develop programs that will access data through
ODBC, you need to install this package.


%prep
%setup -q
%patch -P8 -p1 -b .soname-bump
%patch -P9 -p1

autoreconf -vfi

%build
%configure \
  --with-gnu-ld=yes \
  --enable-threads=yes \
  --enable-drivers=no \
%if %{with gui_related_parts}
  --enable-driver-config=yes
%else
  --enable-driver-config=no
%endif

# Get rid of the rpaths
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build


%install
%make_install

install -m644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}
%multilib_fix_c_header --file %{_includedir}/unixODBC/unixodbc_conf.h

# Directory for ODBC connector/driver plugins
mkdir $RPM_BUILD_ROOT%{_libdir}/odbc

# copy text driver documentation into main doc directory
# currently disabled because upstream no longer includes text driver
# mkdir -p doc/Drivers/txt
# cp -pr Drivers/txt/doc/* doc/Drivers/txt

# don't want to install doc Makefiles as docs
find doc -name 'Makefile*' | xargs rm

# we do not want to ship static libraries
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a

# remove unpackaged files from the buildroot
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/libltdl.*
rm -rf $RPM_BUILD_ROOT%{_datadir}/libtool

# initialize lists of .so files
find $RPM_BUILD_ROOT%{_libdir} -name "*.so.*" | sed "s|^$RPM_BUILD_ROOT||" > base-so-list
find $RPM_BUILD_ROOT%{_libdir} -name "*.so"   | sed "s|^$RPM_BUILD_ROOT||" > devel-so-list


%files -f base-so-list
%license COPYING
%doc README AUTHORS ChangeLog
%if %{with gui_related_parts}
%doc doc
%endif

%config(noreplace) %{_sysconfdir}/odbc*

%{_bindir}/odbcinst
%{_bindir}/isql
%{_bindir}/dltest
%{_bindir}/iusql
%{_bindir}/odbc_config
%{_bindir}/slencheck
%{_mandir}/man*/*
# ODBC connector/driver plugins are placed here
%dir %{_libdir}/odbc

%files devel -f devel-so-list
%{_includedir}/*
%_libdir/pkgconfig/*.pc


%changelog
%autochangelog
