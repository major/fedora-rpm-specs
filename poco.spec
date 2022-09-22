%global _bundled_pcre2_version 10.40
# read from libversion
%global libversion 92

%global cmake_build_dir cmake-build
%global cmake_debug_dir cmake-debug

# build without tests on s390 (runs out of memory during linking due the 2 GB address space)
%ifnarch s390
%bcond_without tests
%endif

%bcond_without samples

# mongodb still available only on little endian arches
%ifarch aarch64 %{arm} %{ix86} x86_64 ppc64le
%bcond_without mongodb
%endif

%if 0%{?fedora} > 27
%global mysql_devel_pkg mariadb-connector-c-devel
%global mysql_lib_dir %{_libdir}/mariadb
%else
%global mysql_devel_pkg mysql-devel
%global mysql_lib_dir %{_libdir}/mysql
%endif

Name:             poco
Version:          1.12.2
Release:          %autorelease
Summary:          C++ class libraries for network-centric applications

License:          Boost
URL:              https://pocoproject.org

Source0:          https://github.com/pocoproject/%{name}/archive/%{name}-%{version}-release.tar.gz#/%{name}-%{version}.tar.gz

# Disable the tests that will fail under Koji (mostly network)
Patch0:           0001-Disable-tests-that-fail-in-koji.patch
# Fix XML compilation due to new methods being guarded by XML_DTD
Patch1:           define-xml-dtd.patch

BuildRequires:    make
BuildRequires:    cmake
BuildRequires:    gcc-c++
BuildRequires:    openssl-devel
BuildRequires:    libiodbc-devel
BuildRequires:    %{mysql_devel_pkg}
BuildRequires:    zlib-devel
BuildRequires:    pcre2-devel
BuildRequires:    sqlite-devel
BuildRequires:    expat-devel
BuildRequires:    libtool-ltdl-devel

# We build poco to unbundle as much as possible, but unfortunately, it uses
# some internal functions of pcre so there are a few files from pcre that are
# still bundled.  See https://github.com/pocoproject/poco/issues/120.
Provides:         bundled(pcre2) = %{_bundled_pcre2_version}

%description
The POCO C++ Libraries (POCO stands for POrtable COmponents) 
are open source C++ class libraries that simplify and accelerate the 
development of network-centric, portable applications in C++. The 
POCO C++ Libraries are built strictly on standard ANSI/ISO C++, 
including the standard library.

%prep
%autosetup -p1 -n %{name}-%{name}-%{version}-release

# Fix libdir for Fedora
/bin/sed -i.orig -e 's|$(INSTALLDIR)/lib\b|$(INSTALLDIR)/%{_lib}|g' Makefile
# Disable rpath
/bin/sed -i.orig -e 's|SHAREDOPT_LINK  = -Wl,-rpath,$(LIBPATH)|SHAREDOPT_LINK  =|g' build/config/Linux
/bin/sed -i.orig -e 's|"Poco/zlib.h"|<zlib.h>|g' Zip/src/ZipStream.cpp
/bin/sed -i.orig -e 's|#endif|#define POCO_UNBUNDLED 1\n\n#endif|g' Foundation/include/Poco/Config.h
cmp build/config/Linux{,.orig} && exit 1

rm -v Foundation/src/MSG00001.bin
rm -v Foundation/include/Poco/zconf.h
rm -v Foundation/include/Poco/zlib.h
rm -v Foundation/src/adler32.c
rm -v Foundation/src/compress.c
rm -v Foundation/src/crc32.c
rm -v Foundation/src/crc32.h
rm -v Foundation/src/deflate.c
rm -v Foundation/src/deflate.h
rm -v Foundation/src/gzguts.h
rm -v PDF/src/gzio.c
rm -v Foundation/src/infback.c
rm -v Foundation/src/inffast.c
rm -v Foundation/src/inffast.h
rm -v Foundation/src/inffixed.h
rm -v Foundation/src/inflate.c
rm -v Foundation/src/inflate.h
rm -v Foundation/src/inftrees.c
rm -v Foundation/src/inftrees.h
rm -v Foundation/src/trees.c
rm -v Foundation/src/trees.h
rm -v Foundation/src/zconf.h
rm -v Foundation/src/zlib.h
rm -v Foundation/src/zutil.c
rm -v Foundation/src/zutil.h

# PCRE files that can't be removed due to still being used in
#   Foundation/src/Unicode.cpp:
mv -v Foundation/src/pcre2_{config.h,internal.h,ucp.h,intmodedep.h,ucptables.c,tables.c,ucd.c} .
rm -v Foundation/src/pcre2*
mv -v pcre2_* Foundation/src

rm -v Data/SQLite/src/sqlite3.h
rm -v Data/SQLite/src/sqlite3.c
rm -v XML/include/Poco/XML/expat.h
rm -v XML/include/Poco/XML/expat_external.h
rm -v XML/src/ascii.h
rm -v XML/src/asciitab.h
rm -v XML/src/expat_config.h
rm -v XML/src/iasciitab.h
rm -v XML/src/internal.h
rm -v XML/src/latin1tab.h
rm -v XML/src/nametab.h
rm -v XML/src/utf8tab.h
rm -v XML/src/xmlparse.cpp
rm -v XML/src/xmlrole.c
rm -v XML/src/xmlrole.h
rm -v XML/src/xmltok.c
rm -v XML/src/xmltok.h
rm -v XML/src/xmltok_impl.c
rm -v XML/src/xmltok_impl.h
rm -v XML/src/xmltok_ns.c

%build
%if %{with tests}
  %global poco_tests -DENABLE_TESTS=ON
%endif
%if %{without samples}
  %global poco_samples --no-samples
%endif
%if %{without mongodb}
  %global poco_mongodb -DENABLE_MONGODB=OFF
%endif
%cmake -DPOCO_UNBUNDLED=ON %{?poco_tests} %{?poco_mongodb} -DENABLE_REDIS=OFF -DODBC_INCLUDE_DIR=%{_includedir}/libiodbc -B %{cmake_build_dir}
%make_build -C %{cmake_build_dir}
%cmake -DPOCO_UNBUNDLED=ON %{?poco_tests} %{?poco_mongodb} -DENABLE_REDIS=OFF -DODBC_INCLUDE_DIR=%{_includedir}/libiodbc -DCMAKE_BUILD_TYPE=Debug -B %{cmake_debug_dir}
%make_build -C %{cmake_debug_dir}

%install
%make_install -C %{cmake_debug_dir}
%make_install -C %{cmake_build_dir}
# conflict with arc
rm -v %{buildroot}%{_bindir}/arc

%check
%if %{with tests}
export POCO_BASE="$(pwd)"
pushd %{cmake_build_dir}
%ifarch s390x
# NetSSL test timed out on s390x
ctest -V %{?_smp_mflags} -E "MongoDB|Redis|DataMySQL|DataODBC|NetSSL"
%else
ctest -V %{?_smp_mflags} -E "MongoDB|Redis|DataMySQL|DataODBC"
%endif
popd
%endif

# -----------------------------------------------------------------------------
%package          foundation
Summary:          The Foundation POCO component

%description foundation
This package contains the Foundation component of POCO. (POCO is a set 
of C++ class libraries for network-centric applications.)
%files foundation
%license LICENSE
%{_libdir}/libPocoFoundation.so.%{libversion}


# -----------------------------------------------------------------------------
%package          xml
Summary:          The XML POCO component

%description xml
This package contains the XML component of POCO. (POCO is a set of C++ 
class libraries for network-centric applications.)
%files xml
%{_libdir}/libPocoXML.so.%{libversion}

# -----------------------------------------------------------------------------
%package          util
Summary:          The Util POCO component

%description util
This package contains the Util component of POCO. (POCO is a set of C++ 
class libraries for network-centric applications.)
%files util
%{_libdir}/libPocoUtil.so.%{libversion}

# -----------------------------------------------------------------------------
%package          net
Summary:          The Net POCO component

%description net
This package contains the Net component of POCO. (POCO is a set of C++ 
class libraries for network-centric applications.)
%files net
%{_libdir}/libPocoNet.so.%{libversion}

# -----------------------------------------------------------------------------
%package          crypto
Summary:          The Crypto POCO component

%description crypto
This package contains the Crypto component of POCO. (POCO is a set of 
C++ class libraries for network-centric applications.)
%files crypto
%{_libdir}/libPocoCrypto.so.%{libversion}

# -----------------------------------------------------------------------------
%package          netssl
Summary:          The NetSSL POCO component

%description netssl
This package contains the NetSSL component of POCO. (POCO is a set of 
C++ class libraries for network-centric applications.)
%files netssl
%{_libdir}/libPocoNetSSL.so.%{libversion}

# -----------------------------------------------------------------------------
%package          data
Summary:          The Data POCO component

%description data
This package contains the Data component of POCO. (POCO is a set of 
C++ class libraries for network-centric applications.)
%files data
%{_libdir}/libPocoData.so.%{libversion}

# -----------------------------------------------------------------------------
%package          sqlite
Summary:          The Data/SQLite POCO component

%description sqlite
This package contains the Data/SQLite component of POCO. (POCO is a set 
of C++ class libraries for network-centric applications.)
%files sqlite
%{_libdir}/libPocoDataSQLite.so.%{libversion}

# -----------------------------------------------------------------------------
%package          odbc
Summary:          The Data/ODBC POCO component

%description odbc
This package contains the Data/ODBC component of POCO. (POCO is a set 
of C++ class libraries for network-centric applications.)
%files odbc
%{_libdir}/libPocoDataODBC.so.%{libversion}

# -----------------------------------------------------------------------------
%package          mysql
Summary:          The Data/MySQL POCO component

%description mysql
This package contains the Data/MySQL component of POCO. (POCO is a set 
of C++ class libraries for network-centric applications.)
%files mysql
%{_libdir}/libPocoDataMySQL.so.%{libversion}

# -----------------------------------------------------------------------------
%package          zip
Summary:          The Zip POCO component

%description zip
This package contains the Zip component of POCO. (POCO is a set of C++ 
class libraries for network-centric applications.)
%files zip
%{_libdir}/libPocoZip.so.%{libversion}

# -----------------------------------------------------------------------------
%package          json
Summary:          The JSON POCO component

%description json
This package contains the JSON component of POCO. (POCO is a set of C++
class libraries for network-centric applications.)
%files json
%{_libdir}/libPocoJSON.so.%{libversion}

# -----------------------------------------------------------------------------
%if %{with mongodb}
%package          mongodb
Summary:          The MongoDB POCO component

%description mongodb
This package contains the MongoDB component of POCO. (POCO is a set of C++
class libraries for network-centric applications.)
%files mongodb
%{_libdir}/libPocoMongoDB.so.%{libversion}
%endif

# -----------------------------------------------------------------------------
%package          pagecompiler
Summary:          The PageCompiler POCO component

%description pagecompiler
This package contains the PageCompiler component of POCO. (POCO is a 
set of C++ class libraries for network-centric applications.)
%files pagecompiler
%{_bindir}/cpspc
%{_bindir}/f2cpsp

# -----------------------------------------------------------------------------
%package          encodings
Summary:          The Encodings POCO component

%description encodings
This package contains the Encodings component of POCO. (POCO is a set of C++
class libraries for network-centric applications.)
%files encodings
%{_libdir}/libPocoEncodings.so.%{libversion}

# -----------------------------------------------------------------------------
%package          jwt
Summary:          The JWT POCO component

%description jwt
This package contains the JWT component of POCO. (POCO is a set of C++
class libraries for network-centric applications.)
%files jwt
%{_libdir}/libPocoJWT.so.%{libversion}

# -----------------------------------------------------------------------------
%package          activerecord
Summary:          The ActiveRecord POCO component

%description activerecord
This package contains the ActiveRecord component of POCO. (POCO is a set of C++
class libraries for network-centric applications.)
%files activerecord
%{_libdir}/libPocoActiveRecord.so.%{libversion}

# -----------------------------------------------------------------------------
%package          prometheus
Summary:          The Prometheus POCO component

%description prometheus
This package contains the Prometheus component of POCO. (POCO is a set of C++
class libraries for network-centric applications.)

%files prometheus
%{_libdir}/libPocoPrometheus.so.%{libversion}

# -----------------------------------------------------------------------------
%package          debug
Summary:          Debug builds of the POCO libraries

%description debug
This package contains the debug builds of the POCO libraries for 
application testing purposes.
%files debug
%{_libdir}/libPocoFoundationd.so.%{libversion}
%{_libdir}/libPocoXMLd.so.%{libversion}
%{_libdir}/libPocoUtild.so.%{libversion}
%{_libdir}/libPocoNetd.so.%{libversion}
%{_libdir}/libPocoCryptod.so.%{libversion}
%{_libdir}/libPocoNetSSLd.so.%{libversion}
%{_libdir}/libPocoDatad.so.%{libversion}
%{_libdir}/libPocoDataSQLited.so.%{libversion}
%{_libdir}/libPocoDataODBCd.so.%{libversion}
%{_libdir}/libPocoDataMySQLd.so.%{libversion}
%{_libdir}/libPocoZipd.so.%{libversion}
%{_libdir}/libPocoJSONd.so.%{libversion}
%if %{with mongodb}
%{_libdir}/libPocoMongoDBd.so.%{libversion}
%endif
%{_libdir}/libPocoEncodingsd.so.%{libversion}
%{_libdir}/libPocoJWTd.so.%{libversion}
%{_libdir}/libPocoActiveRecordd.so.%{libversion}
%{_libdir}/libPocoPrometheusd.so.%{libversion}

# -----------------------------------------------------------------------------
%package          devel
Summary:          Headers for developing programs that will use POCO

Requires:         poco-debug%{?_isa} = %{version}-%{release}
Requires:         poco-foundation%{?_isa} = %{version}-%{release}
Requires:         poco-xml%{?_isa} = %{version}-%{release}
Requires:         poco-util%{?_isa} = %{version}-%{release}
Requires:         poco-net%{?_isa} = %{version}-%{release}
Requires:         poco-crypto%{?_isa} = %{version}-%{release}
Requires:         poco-netssl%{?_isa} = %{version}-%{release}
Requires:         poco-data%{?_isa} = %{version}-%{release}
Requires:         poco-sqlite%{?_isa} = %{version}-%{release}
Requires:         poco-odbc%{?_isa} = %{version}-%{release}
Requires:         poco-mysql%{?_isa} = %{version}-%{release}
Requires:         poco-zip%{?_isa} = %{version}-%{release}
Requires:         poco-json%{?_isa} = %{version}-%{release}
%if %{with mongodb}
Requires:         poco-mongodb%{?_isa} = %{version}-%{release}
%endif
Requires:         poco-pagecompiler%{?_isa} = %{version}-%{release}
Requires:         poco-encodings%{?_isa} = %{version}-%{release}
Requires:         poco-jwt%{?_isa} = %{version}-%{release}
Requires:         poco-activerecord%{?_isa} = %{version}-%{release}

Requires:         zlib-devel
Requires:         pcre2-devel
Requires:         expat-devel
Requires:         openssl-devel

%description devel
The POCO C++ Libraries (POCO stands for POrtable COmponents) 
are open source C++ class libraries that simplify and accelerate the 
development of network-centric, portable applications in C++. The 
POCO C++ Libraries are built strictly on standard ANSI/ISO C++, 
including the standard library.

This package contains the header files needed for developing 
POCO applications.

%files devel
%doc CHANGELOG CODE_OF_CONDUCT.md CONTRIBUTING.md CONTRIBUTORS README*
%{_includedir}/Poco
%{_libdir}/libPocoFoundation.so
%{_libdir}/libPocoFoundationd.so
%{_libdir}/libPocoXML.so
%{_libdir}/libPocoXMLd.so
%{_libdir}/libPocoUtil.so
%{_libdir}/libPocoUtild.so
%{_libdir}/libPocoNet.so
%{_libdir}/libPocoNetd.so
%{_libdir}/libPocoCrypto.so
%{_libdir}/libPocoCryptod.so
%{_libdir}/libPocoNetSSL.so
%{_libdir}/libPocoNetSSLd.so
%{_libdir}/libPocoData.so
%{_libdir}/libPocoDatad.so
%{_libdir}/libPocoDataSQLite.so
%{_libdir}/libPocoDataSQLited.so
%{_libdir}/libPocoDataODBC.so
%{_libdir}/libPocoDataODBCd.so
%{_libdir}/libPocoDataMySQL.so
%{_libdir}/libPocoDataMySQLd.so
%{_libdir}/libPocoZip.so
%{_libdir}/libPocoZipd.so
%{_libdir}/libPocoJSON.so
%{_libdir}/libPocoJSONd.so
%if %{with mongodb}
%{_libdir}/libPocoMongoDB.so
%{_libdir}/libPocoMongoDBd.so
%endif
%{_libdir}/libPocoEncodings.so
%{_libdir}/libPocoEncodingsd.so
%{_libdir}/libPocoJWT.so
%{_libdir}/libPocoJWTd.so
%{_libdir}/libPocoActiveRecord.so
%{_libdir}/libPocoActiveRecordd.so
%{_libdir}/libPocoPrometheus.so
%{_libdir}/libPocoPrometheusd.so
%{_libdir}/cmake/Poco

# -----------------------------------------------------------------------------
%package          doc
Summary:          The POCO API reference documentation

%description doc
The POCO C++ Libraries (POCO stands for POrtable COmponents) 
are open source C++ class libraries that simplify and accelerate the 
development of network-centric, portable applications in C++. The 
POCO C++ Libraries are built strictly on standard ANSI/ISO C++, 
including the standard library.

This is the complete POCO class library reference documentation in 
HTML format.

%files doc
%doc README NEWS LICENSE CONTRIBUTORS CHANGELOG doc/*

%changelog
%autochangelog
