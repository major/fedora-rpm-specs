# For deep debugging we need to build binaries with extra debug info
%bcond debug 0



Name:           mariadb-connector-odbc
Version:        3.2.6
Release:        3%{?with_debug:.debug}%{?dist}
Summary:        The MariaDB Native Client library (ODBC driver)
License:        LGPL-2.1-or-later
Source:         https://archive.mariadb.org/connector-odbc-%{version}/%{name}-%{version}-src.tar.gz
Url:            https://mariadb.org/en/
# Online documentation can be found at: https://mariadb.com/kb/en/library/mariadb-connector-odbc/

Patch1: gcc-15.patch
Patch2: upstream_125389a471ba12a244029801786cc459cf930e65.patch

BuildRequires:  cmake unixODBC-devel gcc-c++
BuildRequires:  mariadb-connector-c-devel >= 3.4.5

%description
MariaDB Connector/ODBC is a standardized, LGPL licensed database driver using
the industry standard Open Database Connectivity (ODBC) API. It supports ODBC
Standard 3.5, can be used as a drop-in replacement for MySQL Connector/ODBC,
and it supports both Unicode and ANSI modes.

%package        devel
Summary:        Development files for the %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
Header files for %{name} that make developing projects with
this connector easier.


%prep
%setup -q -n %{name}-%{version}-src
%patch -P1 -p1
%patch -P2 -p1

sed -i -e "s|/usr/include/mariadb|$(pkg-config --variable=includedir libmariadb)|" CMakeLists.txt


%build

%cmake \
       -DCMAKE_BUILD_TYPE="%{?with_debug:Debug}%{!?with_debug:RelWithDebInfo}" \
       -DMARIADB_LINK_DYNAMIC="$(pkg-config --variable=libdir libmariadb)/libmariadb.so" \
       \
       -DINSTALL_LAYOUT=%{!?flatpak:RPM}%{?flatpak:DEFAULT} \
       -DINSTALL_LIBDIR="%{_lib}" \
       -DINSTALL_LIB_SUFFIX="%{_lib}" \
       -DINSTALL_DOCDIR="%{_defaultdocdir}/%{name}" \
       -DINSTALL_LICENSEDIR="%{_defaultlicensedir}/%{name}" \
       \
       -DCMAKE_C_FLAGS_DEBUG="-O0 -g" \
       -DCMAKE_CXX_FLAGS_DEBUG="-O0 -g" \
       \
       -DCMAKE_SKIP_RPATH=YES \
       -DCMAKE_SKIP_INSTALL_RPATH=YES

cmake -B %_vpath_builddir -N -LAH

%cmake_build



%install
%cmake_install



%files
%license COPYING
%doc     README

# This is unixODBC plugin. It resides directly in %%{_libdir} to be consistent with the rest of unixODBC plugins. Since it is plugin, it doesn´t need to be versioned.
%{_libdir}/libmaodbc.so

# Example configuration file for UnixODBC
%{_pkgdocdir}/maodbc.ini

%files    devel
%dir %{_includedir}/mariadb/
%{_includedir}/mariadb/sqlmariadb.h

# Pkgconfig
%{_libdir}/pkgconfig/libmaodbc.pc

%changelog
%autochangelog
