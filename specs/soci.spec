#
##
# Default values are %%{?with_empty} %%{?with_sqlite3} %%{?with_mysql}
#                    %%{?with_postgresql} %%{?with_odbc} %%{!?with_oracle}
# Note that, for Oracle, when enabled, the following options should
# also be given:
# --with-oracle-include=/opt/oracle/app/oracle/product/11.1.0/db_1/rdbms/public
# --with-oracle-lib=/opt/oracle/app/oracle/product/11.1.0/db_1/lib
# If the macros are defined, redefine them with the correct compilation flags.
%bcond empty 1
%bcond sqlite3 1
%bcond mysql 1
%bcond postgresql 1
%bcond odbc 1
%bcond oracle 0
%bcond tests 1

%global _default_oracle_dir /opt/oracle/app/oracle/product/11.1.0/db_1
%{!?_with_oracle_incdir: %define _with_oracle_incdir --with-oracle-include=%{_default_oracle_dir}/rdbms/public}
%{!?_with_oracle_libdir: %define _with_oracle_libdir --with-oracle-lib=%{_default_oracle_dir}/lib}
#
##
#
Name:           soci
Version:        4.1.2
%global ups_ver 4.1.2
Release:        %autorelease
Summary:        The database access library for C++ programmers
License:        BSL-1.0
URL:            https://github.com/SOCI/%{name}
Source0:        %{url}/archive/v%{ups_ver}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  dos2unix
BuildRequires:  gcc gcc-c++
BuildRequires:  cmake
BuildRequires:  boost-devel

%description
%{name} is a C++ database access library that provides the
illusion of embedding SQL in regular C++ code, staying entirely within
the C++ standard.


%{?with_empty:%package        empty
Summary:        Empty back-end for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    empty
This package contains the Empty back-end for %{name}, i.e.,
dynamic library specific to the Empty database. If you would like to
use %{name} in your programs with an empty database, you will need to
install %{name}-empty.}

%{?with_sqlite3:%package        sqlite3
Summary:        SQLite3 back-end for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
BuildRequires:  sqlite-devel

%description    sqlite3
This package contains the SQLite3 back-end for %{name}, i.e.,
dynamic library specific to the SQLite3 database. If you would like to
use %{name} in your programs with SQLite3, you will need to
install %{name}-sqlite3.}

%{?with_mysql:%package        mysql
Summary:        MySQL back-end for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
BuildRequires:  mariadb-connector-c-devel

%description    mysql
This package contains the MySQL back-end for %{name}, i.e.,
dynamic library specific to the MySQL database. If you would like to
use %{name} in your programs with MySQL, you will need to
install %{name}-mysql.}

%{?with_postgresql:%package        postgresql
Summary:        PostGreSQL back-end for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
BuildRequires:  libpq-devel

%description    postgresql
This package contains the PostGreSQL back-end for %{name}, i.e.,
dynamic library specific to the PostGreSQL database. If you would like
to use %{name} in your programs with PostGreSQL, you will need to
install %{name}-postgresql.}

%{?with_odbc:%package        odbc
Summary:        ODBC back-end for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
BuildRequires:  unixODBC-devel

%description    odbc
This package contains the ODBC back-end for %{name}, i.e.,
dynamic library specific to the ODBC connectors. If you would like to
use %{name} in your programs with ODBC, you will need to
install %{name}-odbc.}

%{?with_oracle:%package        oracle
Summary:        Oracle back-end for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    oracle
This package contains the Oracle back-end for %{name}, i.e.,
dynamic library specific to the Oracle database. If you would like to
use %{name} in your programs with Oracle, you will need to install
%{name}-oracle.}


%package        devel
Summary:        Header files, libraries and development documentation for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
This package contains the header files, dynamic libraries and
development documentation for %{name}. If you would like to develop
programs using %{name}, you will need to install %{name}-devel.

%{?with_empty:%package        empty-devel
Summary:        Empty back-end for %{name}
Requires:       %{name}-devel = %{version}-%{release}
Requires:       %{name}-empty = %{version}-%{release}

%description    empty-devel
This package contains the Empty back-end for %{name}, i.e., header
files and dynamic libraries specific to an empty database. If you
would like to develop programs using %{name} and an empty database,
you will need to install %{name}-empty.}

%{?with_sqlite3:%package        sqlite3-devel
Summary:        SQLite3 back-end for %{name}
Requires:       %{name}-devel = %{version}-%{release}
Requires:       %{name}-sqlite3 = %{version}-%{release}
Requires:       sqlite-devel

%description    sqlite3-devel
This package contains the SQLite3 back-end for %{name}, i.e., header
files and dynamic libraries specific to the SQLite3 database. If you
would like to develop programs using %{name} and SQLite3, you will need
to install %{name}-sqlite3.}

%{?with_mysql:%package        mysql-devel
Summary:        MySQL back-end for %{name}
Requires:       %{name}-devel = %{version}-%{release}
Requires:       %{name}-mysql = %{version}-%{release}
Requires:       mariadb-connector-c-devel

%description    mysql-devel
This package contains the MySQL back-end for %{name}, i.e., header
files and dynamic libraries specific to the MySQL database. If you
would like to develop programs using %{name} and MySQL, you will need
to install %{name}-mysql.}

%{?with_postgresql:%package        postgresql-devel
Summary:        PostGreSQL back-end for %{name}
Requires:       %{name}-devel = %{version}-%{release}
Requires:       %{name}-postgresql = %{version}-%{release}
Requires:       libpq-devel

%description    postgresql-devel
This package contains the PostGreSQL back-end for %{name}, i.e., header
files and dynamic libraries specific to the PostGreSQL database. If
you would like to develop programs using %{name} and PostGreSQL, you
will need to install %{name}-postgresql.}

%{?with_odbc:%package        odbc-devel
Summary:        ODBC back-end for %{name}
Requires:       %{name}-devel = %{version}-%{release}
Requires:       %{name}-odbc = %{version}-%{release}
Requires:       unixODBC-devel

%description    odbc-devel
This package contains the Odbc back-end for %{name}, i.e., header
files and dynamic libraries specific to the Odbc database. If you
would like to develop programs using %{name} and Odbc, you will need
to install %{name}-odbc.}

%{?with_oracle:%package        oracle-devel
Summary:        Oracle back-end for %{name}
Requires:       %{name}-devel = %{version}-%{release}
Requires:       %{name}-oracle = %{version}-%{release}

%description    oracle-devel
This package contains the Oracle back-end for %{name}, i.e., header
files and dynamic libraries specific to the Oracle database. If you
would like to develop programs using %{name} and Oracle, you will need
to install %{name}-oracle.}


%package        doc
Summary:        HTML documentation for the %{name} library
BuildArch:      noarch
#BuildRequires:  tex(latex)
#BuildRequires:  doxygen, ghostscript

%description    doc
This package contains the documentation in the HTML format of the %{name}
library. The documentation is the same as at the %{name} web page.


%prep
%setup -q -n %{name}-%{ups_ver}

# Rename change-log and license file, so that they comply with
# packaging standard
mv README.md README
mv CHANGES ChangeLog
mv LICENSE_1_0.txt COPYING
echo "2025-03-30:" > NEWS
echo "- Version 4.1.0" >> NEWS
echo "- See the ChangeLog file for more details." >> NEWS
# Remove the spurious executable permission
chmod a-x AUTHORS README ChangeLog COPYING NEWS
# Unix ends of line
dos2unix AUTHORS README ChangeLog COPYING NEWS

%build
# Support for building tests.
%define soci_testflags -DBUILD_TESTS="NONE"
%if %{with tests}
%define soci_testflags -DSOCI_TEST=ON -DSOCI_EMPTY_TEST_CONNSTR="dummy" -DSOCI_SQLITE3_TEST_CONNSTR="test.db" -DSOCI_POSTGRESQL_TEST_CONNSTR:STRING="dbname=soci_test" -DSOCI_MYSQL_TEST_CONNSTR:STRING="db=soci_test user=mloskot password=pantera"
%endif

%cmake \
 -DSOCI_EMPTY=%{?with_empty:ON}%{!?with_empty:OFF} \
 -DSOCI_SQLITE3=%{?with_sqlite3:ON}%{!?with_sqlite3:OFF} \
 -DSOCI_POSTGRESQL=%{?with_postgresql:ON}%{!?with_postgresql:OFF} \
 -DSOCI_MYSQL=%{?with_mysql:ON}%{!?with_mysql:OFF} \
 -DSOCI_ODBC=%{?with_odbc:ON}%{!?with_odbc:OFF} \
 -DSOCI_ORACLE=%{?with_oracle:ON %{?_with_oracle_incdir} %{?_with_oracle_libdir}}%{!?with_oracle:OFF} \
 %{soci_testflags}
%cmake_build

%install
%cmake_install

# The SOCI libraries are now released in a non-standard location
mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d
#echo "%%{_libdir}/%%{name}" > %%{buildroot}%%{_sysconfdir}/ld.so.conf.d/%%{name}64.conf

# CMake helpers
mkdir -p %{buildroot}%{_datadir}/%{name}
mv -f %{buildroot}%{_libdir}/cmake %{buildroot}%{_datadir}/%{name}/CMake

# Remove unpackaged files from the buildroot
rm -f %{buildroot}%{_libdir}/*.a

%if %{with tests}
%check
%{ctest --exclude-regex 'soci_(odbc|mysql|postgresql)_test'}
%endif


%files
%doc AUTHORS ChangeLog COPYING NEWS README
#%%{_sysconfdir}/ld.so.conf.d/%%{name}64.conf
%{_libdir}/lib%{name}_core.so.*

%{?with_empty:%files empty
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/lib%{name}_empty.so.*}

%{?with_sqlite3:%files sqlite3
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/lib%{name}_sqlite3.so.*}

%{?with_mysql:%files mysql
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/lib%{name}_mysql.so.*}

%{?with_postgresql:%files postgresql
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/lib%{name}_postgresql.so.*}

%{?with_odbc:%files odbc
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/lib%{name}_odbc.so.*}

%{?with_oracle:%files oracle
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/lib%{name}_oracle.so.*}


%files devel
%doc AUTHORS ChangeLog COPYING NEWS README
%dir %{_includedir}/%{name}/
%{_includedir}/%{name}/*.h
%{_libdir}/lib%{name}_core.so
%{_datadir}/%{name}/CMake

%{?with_empty:%files empty-devel
%doc AUTHORS ChangeLog COPYING NEWS README
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/empty/
%{_libdir}/lib%{name}_empty.so}

%{?with_sqlite3:%files sqlite3-devel
%doc AUTHORS ChangeLog COPYING NEWS README
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/sqlite3/
%{_libdir}/lib%{name}_sqlite3.so}

%{?with_mysql:%files mysql-devel
%doc AUTHORS ChangeLog COPYING NEWS README
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/mysql
%{_libdir}/lib%{name}_mysql.so}

%{?with_postgresql:%files postgresql-devel
%doc AUTHORS ChangeLog COPYING NEWS README
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/postgresql
%{_libdir}/lib%{name}_postgresql.so}

%{?with_odbc:%files odbc-devel
%doc AUTHORS ChangeLog COPYING NEWS README
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/odbc/
%{_libdir}/lib%{name}_odbc.so}

%{?with_oracle:%files oracle-devel
%doc AUTHORS ChangeLog COPYING NEWS README
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/oracle
%{_libdir}/lib%{name}_oracle.so}


%files doc
%doc AUTHORS ChangeLog NEWS README
%license COPYING

%changelog
%autochangelog

