# This is the PostgreSQL Global Development Group Official RPMset spec file,
# or a derivative thereof.

# This spec file and ancillary files are licensed in accordance with
# The PostgreSQL license.

# In this file you can find the default build package list macros.
# These can be overridden by defining on the rpm command line:
# rpm --define 'packagename 1' .... to force the package to build.
# rpm --define 'packagename 0' .... to force the package NOT to build.
# The base package, the libs package, the devel package, and the server package
# always get built.

%{!?test:%global test 1}
%{!?llvmjit:%global llvmjit 0}
%{!?external_libpq:%global external_libpq 0}
%{!?upgrade:%global upgrade 1}
%{!?plpython3:%global plpython3 1}
%{!?pltcl:%global pltcl 0}
%{!?plperl:%global plperl 1}
%{!?ssl:%global ssl 1}
%{!?icu:%global icu 1}
%{!?kerberos:%global kerberos 1}
%{!?ldap:%global ldap 1}
%{!?nls:%global nls 1}
%{!?uuid:%global uuid 1}
%{!?xml:%global xml 1}
%{!?pam:%global pam 1}
%{!?sdt:%global sdt 1}
%{!?selinux:%global selinux 1}
%{!?runselftest:%global runselftest 1}
%{!?pgaudit:%global pgaudit 1}
%{!?pg_repack:%global pg_repack 1}
%{!?pgvector:%global pgvector 1}
%{!?decoderbufs:%global decoderbufs 0}
%{!?postgresql_default:%global postgresql_default 0}

%global majorname postgresql
%global majorversion 19

# By default, patch(1) creates backup files when chunks apply with offsets.
# Turn that off to ensure such files don't get included in RPMs.
%global _default_patch_flags --no-backup-if-mismatch

# https://fedoraproject.org/wiki/Packaging:Guidelines#Packaging_of_Additional_RPM_Macros
%global macrosdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)

# Don't create note file, added package_note_flags to linker by redhat-rpm-config
# will cause issue during extension build because it'll be inherited.
%undefine _package_note_file

Summary: PostgreSQL client programs
Name: %{majorname}%{majorversion}
Version: 19beta1
Release: 3%{?dist}

# The PostgreSQL license is very similar to other MIT licenses, but the OSI
# recognizes it as an independent license, so we do as well.
License: PostgreSQL
Url: http://www.postgresql.org/

# This SRPM includes copies of the previous major releases, which are needed for
# in-place upgrade of an old database.  In most cases it will not be critical
# that this be kept up with the latest minor release of the previous series;
# but update when bugs affecting pg_dump output are fixed.
%global prevmajorversion 18
%global prevversion %{prevmajorversion}.3
%global prev_prefix %{_libdir}/pgsql/postgresql-%{prevmajorversion}
%global precise_version %{?epoch:%epoch:}%version-%release

%global setup_version 8.12

%global service_name postgresql.service

Source0: https://ftp.postgresql.org/pub/source/v%{version}/postgresql-%{version}.tar.bz2
Source3: https://ftp.postgresql.org/pub/source/v%{prevversion}/postgresql-%{prevversion}.tar.bz2
Source4: Makefile.regress
Source9: postgresql.tmpfiles.d
Source10: postgresql.pam
Source11: postgresql-bashprofile


# git: https://github.com/devexp-db/postgresql-setup
Source12: https://github.com/devexp-db/postgresql-setup/releases/download/v%{setup_version}/postgresql-setup-%{setup_version}.tar.gz

# Those here are just to enforce packagers check that the tarball was downloaded
# correctly.  Also, this allows us check that packagers-only tarballs do not
# differ with publicly released ones.
Source16: https://ftp.postgresql.org/pub/source/v%{version}/postgresql-%{version}.tar.bz2.sha256
Source17: https://ftp.postgresql.org/pub/source/v%{prevversion}/postgresql-%{prevversion}.tar.bz2.sha256

# pgaudit extension - using main branch until pgaudit 19.0 is released
# Latest released version is 18.0 (for PG18), main branch targets PG19
Source20: https://github.com/pgaudit/pgaudit/archive/refs/heads/main.tar.gz#/pgaudit-main.tar.gz

# pg_repack extension
Source21: https://github.com/reorg/pg_repack/archive/refs/tags/ver_1.5.3.tar.gz#/pg_repack-1.5.3.tar.gz

# pgvector extension
Source22: https://github.com/pgvector/pgvector/archive/refs/tags/v0.8.3.tar.gz#/pgvector-0.8.3.tar.gz

# postgres-decoderbufs extension
Source23: https://github.com/debezium/postgres-decoderbufs/archive/refs/tags/v3.5.2.Final.tar.gz#/postgres-decoderbufs-3.5.2.tar.gz

# Fix pgaudit compilation with PostgreSQL 19 (VARSIZE_ANY_EXHDR API change)
Patch20: pgaudit-pg19-compat.patch
# Enable in-tree builds for PGXS-based extensions
Patch21: pg_repack-intree-build.patch
Patch22: pgvector-intree-build.patch
Patch23: decoderbufs-intree-build.patch

# Comments for these patches are in the patch files.
Patch1: rpm-pgsql.patch
Patch2: postgresql-logging.patch
Patch5: postgresql-var-run-socket.patch
Patch8: postgresql-external-libpq.patch
Patch9: postgresql-server-pg_config.patch
# Upstream bug #16971: https://www.postgresql.org/message-id/16971-5d004d34742a3d35%40postgresql.org
# rhbz#1940964
Patch10: postgresql-datalayout-mismatch-on-s390.patch
Patch12: postgresql-no-libecpg.patch
Patch13: postgresql-default-ssl-config.patch

# This macro is used for package names in the files section
%if %?postgresql_default
%global pkgname %{majorname}
%package -n %{pkgname}
Summary: PostgreSQL client programs
%else
%global pkgname %{majorname}%{majorversion}
%endif

BuildRequires: make
BuildRequires: lz4-devel
BuildRequires: libzstd-devel
BuildRequires: gcc
BuildRequires: perl(ExtUtils::MakeMaker) glibc-devel bison flex gawk
BuildRequires: perl(ExtUtils::Embed), perl-devel
BuildRequires: perl(Opcode)
BuildRequires: perl-FindBin
%if 0%{?fedora} || 0%{?rhel} > 7
BuildRequires: perl-generators
%endif
BuildRequires: readline-devel zlib-devel
BuildRequires: systemd systemd-devel util-linux
%{!?rhel:BuildRequires: multilib-rpm-config}
%if %external_libpq
BuildRequires: libpq-devel >= %version
%endif
BuildRequires: docbook-style-xsl

# postgresql-setup build requires
BuildRequires: m4 elinks docbook-utils help2man

%if %plpython3
BuildRequires: python3-devel
%endif

%if %pltcl
BuildRequires: tcl-devel
%endif

%if %ssl
BuildRequires: openssl-devel
%endif

%if %kerberos
BuildRequires: krb5-devel
%endif

%if %ldap
BuildRequires: openldap-devel
%endif

%if %nls
BuildRequires: gettext >= 0.10.35
%endif

%if %uuid
BuildRequires: uuid-devel
%endif

%if %xml
BuildRequires: libxml2-devel libxslt-devel
%endif

%if %pam
BuildRequires: pam-devel
%endif

%if %sdt
BuildRequires: systemtap-sdt-devel
BuildRequires: systemtap-sdt-dtrace
%endif

%if %selinux
BuildRequires: libselinux-devel
%endif

%if %icu
BuildRequires:	libicu-devel
%endif

%if %decoderbufs
BuildRequires: protobuf-c-devel
%endif

%if %?postgresql_default
%define postgresqlXX_if_default() %{expand:\
Provides: postgresql%{majorversion}%{?1:-%{1}} = %precise_version\
Provides: postgresql%{majorversion}%{?1:-%{1}}%{?_isa} = %precise_version\
Obsoletes: postgresql%{majorversion}%{?1:-%{1}}\
}
%else
%define postgresqlXX_if_default() %{nil}
%endif

%define conflict_with_other_streams() %{expand:\
Provides: %{majorname}%{?1:-%{1}}-any\
Conflicts: %{majorname}%{?1:-%{1}}-any\
}

%define virtual_conflicts_and_provides() %{expand:\
%conflict_with_other_streams %{**}\
%postgresqlXX_if_default %{**}\
}

Provides: %{pkgname} = %precise_version
Provides: %{pkgname}%{?_isa} = %precise_version

%virtual_conflicts_and_provides

# https://bugzilla.redhat.com/1464368
# and do not provide pkgconfig RPM provides (RHBZ#1980992) and #2121696
%global __provides_exclude_from %{_libdir}/(pgsql|pkgconfig)

%description
PostgreSQL is an advanced Object-Relational database management system (DBMS).
The base postgresql package contains the client programs that you'll need to
access a PostgreSQL DBMS server, as well as HTML documentation for the whole
system.  These client programs can be located on the same machine as the
PostgreSQL server, or on a remote machine that accesses a PostgreSQL server
over a network connection.  The PostgreSQL server can be found in the
postgresql-server sub-package.

%description -n %{pkgname}
PostgreSQL is an advanced Object-Relational database management system (DBMS).
The base postgresql package contains the client programs that you'll need to
access a PostgreSQL DBMS server, as well as HTML documentation for the whole
system.  These client programs can be located on the same machine as the
PostgreSQL server, or on a remote machine that accesses a PostgreSQL server
over a network connection.  The PostgreSQL server can be found in the
postgresql-server sub-package.


%if ! %external_libpq
%package -n %{pkgname}-private-libs
Summary: The shared libraries required only for this build of PostgreSQL server
Group: Applications/Databases
# for /sbin/ldconfig
Requires(post): glibc
Requires(postun): glibc
Provides: %{pkgname}-private-libs = %precise_version
Provides: %{pkgname}-private-libs%{?_isa} = %precise_version

%virtual_conflicts_and_provides private-libs

%description -n %{pkgname}-private-libs
The postgresql-private-libs package provides the shared libraries for this
build of PostgreSQL server and plugins build with this version of server.
For shared libraries used by client packages that need to connect to a
PostgreSQL server, install libpq package instead.


%package -n %{pkgname}-private-devel
Summary: PostgreSQL development header files for this build of PostgreSQL server
Group: Development/Libraries
Requires: %{pkgname}-private-libs%{?_isa} = %precise_version
# Conflict is desired here, a user must pick one or another
Conflicts: libpq-devel
Provides: %{pkgname}-devel = %precise_version
Provides: %{pkgname}-devel%{?_isa} = %precise_version

%virtual_conflicts_and_provides private-devel

%description -n %{pkgname}-private-devel
The postgresql-private-devel package contains the header files and libraries
needed to compile C or C++ applications which will directly interact
with a PostgreSQL database management server.
You need to install this package if you want to develop applications which
will interact with a PostgreSQL server.
%endif


%package -n %{pkgname}-server
Summary: The programs needed to create and run a PostgreSQL server
Requires: %{pkgname}%{?_isa} = %precise_version
# We require this to be present for %%{_prefix}/lib/tmpfiles.d
Requires: systemd
# Make sure it's there when scriptlets run, too
%{?systemd_requires}
# We require this to be present for /usr/sbin/runuser when using --initdb (rhbz#2071437)
Requires: util-linux
# postgresql setup requires runuser from util-linux package
BuildRequires: util-linux
# Packages which provide postgresql plugins should build-require
# postgresql-server-devel and require
# postgresql-server(:MODULE_COMPAT_%%{postgresql_major}).
# This will automatically guard against incompatible server & plugin
# installation (#1008939, #1007840)
Provides: %{pkgname}-server(:MODULE_COMPAT_%{majorversion})
Provides: bundled(postgresql-setup) = %setup_version
Provides: %{pkgname}-server = %precise_version
Provides: %{pkgname}-server%{?_isa} = %precise_version
# Provide symbol regardless version. This symbol is present in every single
# postgresql stream

%virtual_conflicts_and_provides server

%description -n %{pkgname}-server
PostgreSQL is an advanced Object-Relational database management system (DBMS).
The postgresql-server package contains the programs needed to create
and run a PostgreSQL server, which will in turn allow you to create
and maintain PostgreSQL databases.


%package -n %{pkgname}-docs
Summary: Extra documentation for PostgreSQL
Requires: %{pkgname}%{?_isa} = %precise_version
Provides: %{pkgname}-doc = %precise_version
Provides: %{pkgname}-docs = %precise_version

%virtual_conflicts_and_provides docs

%description -n %{pkgname}-docs
The postgresql-docs package contains some additional documentation for
PostgreSQL.  Currently, this includes the main documentation in PDF format
and source files for the PostgreSQL tutorial.


%package -n %{pkgname}-contrib
Summary: Extension modules distributed with PostgreSQL
Requires: %{pkgname}%{?_isa} = %precise_version
Provides: %{pkgname}-contrib = %precise_version
Provides: %{pkgname}-contrib%{?_isa} = %precise_version

%virtual_conflicts_and_provides contrib

%description -n %{pkgname}-contrib
The postgresql-contrib package contains various extension modules that are
included in the PostgreSQL distribution.


%package -n %{pkgname}-server-devel
Summary: PostgreSQL development header files and libraries
%if %icu
Requires:	libicu-devel
%endif
%if %kerberos
Requires: krb5-devel
%endif
%if %llvmjit
Requires: clang-devel llvm-devel
%endif
%if %external_libpq
# Some extensions require libpq
# Do not make them care about whether server uses private or system-wide
# libpq, simply let the server pull the correct one
Requires: libpq-devel
%else
Requires: %{pkgname}-private-devel
%endif
Provides: %{pkgname}-server-devel = %precise_version
Provides: %{pkgname}-server-devel%{?_isa} = %precise_version

%virtual_conflicts_and_provides server-devel

%description -n %{pkgname}-server-devel
The postgresql-server-devel package contains the header files and configuration
needed to compile PostgreSQL server extension.

%package -n %{pkgname}-test-rpm-macros
Summary: Convenience RPM macros for build-time testing against PostgreSQL server
Requires: %{pkgname}-server = %precise_version
BuildArch: noarch
Provides: %{pkgname}-test-rpm-macros = %precise_version

%conflict_with_other_streams test-rpm-macros

%description -n %{pkgname}-test-rpm-macros
This package is meant to be added as BuildRequires: dependency of other packages
that want to run build-time testsuite against running PostgreSQL server.


%package -n %{pkgname}-static
Summary: Statically linked PostgreSQL libraries
Requires: %{pkgname}-server-devel%{?_isa} = %precise_version
Provides: %{pkgname}-static = %precise_version
Provides: %{pkgname}-static%{?_isa} = %precise_version

%virtual_conflicts_and_provides static

%description -n %{pkgname}-static
Statically linked PostgreSQL libraries that do not have dynamically linked
counterparts.


%if %upgrade
%package -n %{pkgname}-upgrade
Summary: Support for upgrading from the previous major release of PostgreSQL
Requires: %{pkgname}-server%{?_isa} = %precise_version
Provides: bundled(postgresql-server) = %prevversion
Provides: %{pkgname}-upgrade = %precise_version
Provides: %{pkgname}-upgrade%{?_isa} = %precise_version

%virtual_conflicts_and_provides upgrade

%description -n %{pkgname}-upgrade
The postgresql-upgrade package contains the pg_upgrade utility and supporting
files needed for upgrading a PostgreSQL database from the previous major
version of PostgreSQL (version %{prevmajorversion}).


%package -n %{pkgname}-upgrade-devel
Summary: Support for build of extensions required for upgrade process
Requires: %{pkgname}-upgrade%{?_isa} = %precise_version
Provides: %{pkgname}-upgrade-devel = %precise_version
Provides: %{pkgname}-upgrade-devel%{?_isa} = %precise_version

%virtual_conflicts_and_provides upgrade-devel

%description -n %{pkgname}-upgrade-devel
The postgresql-devel package contains the header files and libraries
needed to compile C or C++ applications which are necessary in upgrade
process.
%endif


%if %plperl
%package -n %{pkgname}-plperl
Summary: The Perl procedural language for PostgreSQL
Requires: %{pkgname}-server%{?_isa} = %precise_version
Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
%if %runselftest
BuildRequires: perl(Opcode)
BuildRequires: perl(Data::Dumper)
%endif
Provides: %{pkgname}-plperl = %precise_version
Provides: %{pkgname}-plperl%{?_isa} = %precise_version

%virtual_conflicts_and_provides plperl

%description -n %{pkgname}-plperl
The postgresql-plperl package contains the PL/Perl procedural language,
which is an extension to the PostgreSQL database server.
Install this if you want to write database functions in Perl.
%endif


%if %plpython3
%package -n %{pkgname}-plpython3
Summary: The Python3 procedural language for PostgreSQL
Requires: %{pkgname}-server%{?_isa} = %precise_version
Provides: %{pkgname}-plpython3 = %precise_version
Provides: %{pkgname}-plpython3%{?_isa} = %precise_version

%virtual_conflicts_and_provides plpython3

%description -n %{pkgname}-plpython3
The postgresql-plpython3 package contains the PL/Python3 procedural language,
which is an extension to the PostgreSQL database server.
Install this if you want to write database functions in Python 3.
%endif


%if %pltcl
%package -n %{pkgname}-pltcl
Summary: The Tcl procedural language for PostgreSQL
Requires: %{pkgname}-server%{?_isa} = %precise_version
Provides: %{pkgname}-pltcl = %precise_version
Provides: %{pkgname}-pltcl%{?_isa} = %precise_version

%virtual_conflicts_and_provides pltcl

%description -n %{pkgname}-pltcl
The postgresql-pltcl package contains the PL/Tcl procedural language,
which is an extension to the PostgreSQL database server.
Install this if you want to write database functions in Tcl.
%endif


%if %test
%package -n %{pkgname}-test
Summary: The test suite distributed with PostgreSQL
Requires: %{pkgname}-server%{?_isa} = %precise_version
Requires: %{pkgname}-server-devel%{?_isa} = %precise_version
Requires: %{pkgname}-contrib%{?_isa} = %precise_version
Provides: %{pkgname}-test = %precise_version
Provides: %{pkgname}-test%{?_isa} = %precise_version

%virtual_conflicts_and_provides test

%description -n %{pkgname}-test
The postgresql-test package contains files needed for various tests for the
PostgreSQL database management system, including regression tests and
benchmarks.
%endif

%if %llvmjit
%package -n %{pkgname}-llvmjit
Summary:	Just-in-time compilation support for PostgreSQL
Requires:	%{pkgname}-server%{?_isa} = %{version}-%{release}
%if 0%{?rhel} && 0%{?rhel} == 7
Requires:	llvm5.0 >= 5.0
%else
Requires:	llvm => 5.0
%endif
Provides:	postgresql-llvmjit >= %{version}-%{release}
Provides: %{pkgname}-llvmjit = %precise_version
Provides: %{pkgname}-llvmjit%{?_isa} = %precise_version

BuildRequires:	llvm-devel >= 5.0 clang-devel >= 5.0

%virtual_conflicts_and_provides llvmjit

%description -n %{pkgname}-llvmjit
The postgresql-llvmjit package contains support for
just-in-time compiling parts of PostgreSQL queries. Using LLVM it
compiles e.g. expressions and tuple deforming into native code, with the
goal of accelerating analytics queries.
%endif

%if %pgaudit
%package -n %{pkgname}-pgaudit
Summary: PostgreSQL Audit Extension
Requires: %{pkgname}-server%{?_isa} = %precise_version
Provides: %{pkgname}-pgaudit = %precise_version
Provides: %{pkgname}-pgaudit%{?_isa} = %precise_version

%virtual_conflicts_and_provides pgaudit

%description -n %{pkgname}-pgaudit
The PostgreSQL Audit extension (pgaudit) provides detailed session
and/or object audit logging via the standard PostgreSQL logging
facility.

The goal of the PostgreSQL Audit extension (pgaudit) is to provide
PostgreSQL users with capability to produce audit logs often required to
comply with government, financial, or ISO certifications.

An audit is an official inspection of an individual's or organization's
accounts, typically by an independent body. The information gathered by
the PostgreSQL Audit extension (pgaudit) is properly called an audit
trail or audit log. The term audit log is used in this documentation.
%endif

%if %pg_repack
%package -n %{pkgname}-pg-repack
Summary: Online table reorganization for PostgreSQL
Requires: %{pkgname}-server%{?_isa} = %precise_version
Provides: %{pkgname}-pg-repack = %precise_version
Provides: %{pkgname}-pg-repack%{?_isa} = %precise_version

%virtual_conflicts_and_provides pg-repack

%description -n %{pkgname}-pg-repack
pg_repack is a PostgreSQL extension which lets you remove bloat from
tables and indexes, and optionally restore the physical order of
clustered indexes. Unlike CLUSTER and VACUUM FULL it works online,
without holding an exclusive lock on the processed tables during
processing.
%endif

%if %pgvector
%package -n %{pkgname}-pgvector
Summary: Open-source vector similarity search for PostgreSQL
Requires: %{pkgname}-server%{?_isa} = %precise_version
Provides: %{pkgname}-pgvector = %precise_version
Provides: %{pkgname}-pgvector%{?_isa} = %precise_version

%virtual_conflicts_and_provides pgvector

%description -n %{pkgname}-pgvector
pgvector is an open-source vector similarity search extension for
PostgreSQL. Store your vectors with the rest of your data. Supports
exact and approximate nearest neighbor search, L2 distance, inner
product, cosine distance, and more.
%endif

%if %decoderbufs
%package -n %{pkgname}-decoderbufs
Summary: PostgreSQL Protocol Buffers logical decoder plugin
Requires: %{pkgname}-server%{?_isa} = %precise_version
Provides: %{pkgname}-decoderbufs = %precise_version
Provides: %{pkgname}-decoderbufs%{?_isa} = %precise_version

%virtual_conflicts_and_provides decoderbufs

%description -n %{pkgname}-decoderbufs
A PostgreSQL logical decoder output plugin to deliver data as
Protocol Buffers messages. Used by Debezium for Change Data Capture.
%endif

%prep
(
  cd "$(dirname "%{SOURCE0}")"
  sha256sum -c %{SOURCE16}
%if %upgrade
  sha256sum -c %{SOURCE17}
%endif
)
%setup -q -a 12 -n postgresql-%{version}
%patch 1 -p1
%patch 2 -p1
%patch 5 -p1
%if %external_libpq
%patch 8 -p1
%else
%patch 12 -p1
%endif
%patch 9 -p1
%patch 10 -p1
%patch 13 -p1


%if ! %external_libpq
%global private_soname private%{majorversion}
find . -type f -name Makefile -exec sed -i -e "s/SO_MAJOR_VERSION=\s\?\([0-9]\+\)/SO_MAJOR_VERSION= %{private_soname}-\1/" {} \;
%endif

%if %upgrade
tar xfj %{SOURCE3}

# libpq from this upgrade-only build is dropped and the libpq from the main
# version is used. Use the same major hack therefore.
%if ! %external_libpq
find postgresql-%{prevversion} -type f -name Makefile -exec sed -i -e "s/SO_MAJOR_VERSION=\s\?\([0-9]\+\)/SO_MAJOR_VERSION= %{private_soname}-\1/" {} \;
%endif

# apply once SOURCE3 is extracted
%endif

# remove .gitignore files to ensure none get into the RPMs (bug #642210)
find . -type f -name .gitignore | xargs rm

# Create a sysusers.d config file
cat > postgresql19.sysusers.conf <<EOF
u postgres 26 'PostgreSQL Server' /var/lib/pgsql /bin/bash
EOF

cat > postgresql19.tmpfiles.conf <<EOF
d /var/lib/pgsql 0700 postgres postgres -
EOF

%if %pgaudit
tar xzf %{SOURCE20}
mv pgaudit-main contrib/pgaudit
pushd contrib/pgaudit
%patch 20 -p1
popd
%endif

%if %pg_repack
tar xzf %{SOURCE21}
mv pg_repack-ver_1.5.3 contrib/pg_repack
pushd contrib/pg_repack
%patch 21 -p1
popd
%endif

%if %pgvector
tar xzf %{SOURCE22}
mv pgvector-0.8.3 contrib/pgvector
pushd contrib/pgvector
%patch 22 -p1
popd
%endif

%if %decoderbufs
tar xzf %{SOURCE23}
mv postgres-decoderbufs-3.5.2.Final contrib/decoderbufs
pushd contrib/decoderbufs
%patch 23 -p1
popd
%endif

%build
# Avoid LTO on armv7hl as it runs out of memory
%ifarch armv7hl s390x
%define _lto_cflags %{nil}
%endif
# fail quickly and obviously if user tries to build as root
%if %runselftest
	if [ x"`id -u`" = x0 ]; then
		echo "postgresql's regression tests fail if run as root."
		echo "If you really need to build the RPM as root, use"
		echo "--define='runselftest 0' to skip the regression tests."
		exit 1
	fi
%endif

# Building postgresql-setup

cd postgresql-setup-%{setup_version}

%configure \
    pgdocdir=%{_pkgdocdir} \
    PGVERSION=%{version} \
    PGMAJORVERSION=%{majorversion} \
    NAME_DEFAULT_PREV_SERVICE=postgresql

make %{?_smp_mflags}
cd ..

# Fiddling with CFLAGS.

CFLAGS="${CFLAGS:-%optflags}"
CFLAGS="$CFLAGS -DOPENSSL_NO_ENGINE -std=c18"
# Strip out -ffast-math from CFLAGS....
CFLAGS=`echo $CFLAGS|xargs -n 1|grep -v ffast-math|xargs -n 100`
export CFLAGS

common_configure_options='
	--disable-rpath
%if %plperl
	--with-perl
%endif
%if %pltcl
	--with-tcl
	--with-tclconfig=/usr/%_lib
%endif
%if %ldap
	--with-ldap
%endif
%if %ssl
	--with-openssl
%endif
%if %pam
	--with-pam
%endif
%if %kerberos
	--with-gssapi
%endif
%if %uuid
	--with-ossp-uuid
%endif
%if %xml
	--with-libxml
	--with-libxslt
%endif
%if %nls
	--enable-nls
%endif
%if %sdt
	--enable-dtrace
%endif
%if %selinux
	--with-selinux
%endif
	--with-system-tzdata=/usr/share/zoneinfo
	--datadir=%_datadir/pgsql
	--with-systemd
	--with-lz4
	--with-zstd
%if %icu
	--with-icu
%endif
%if %llvmjit
	--with-llvm
%endif
%if %plpython3
	--with-python
%endif
'

export PYTHON=/usr/bin/python3

# These configure options must match main build
%configure $common_configure_options

%make_build world

# Have to hack makefile to put correct path into tutorial scripts
sed "s|C=\`pwd\`;|C=%{_libdir}/pgsql/tutorial;|" < src/tutorial/Makefile > src/tutorial/GNUmakefile
make %{?_smp_mflags} -C src/tutorial NO_PGXS=1 all
rm -f src/tutorial/GNUmakefile

# The object files shouldn't be copied to rpm bz#1187514
rm -f src/tutorial/*.o

# run_testsuite WHERE
# -------------------
# Run 'make check' in WHERE path.  When that command fails, return the logs
# given by PostgreSQL build system and set 'test_failure=1'.  This function
# never exits directly nor stops rpmbuild where `set -e` is enabled.
run_testsuite()
{
	make -k -C "$1" MAX_CONNECTIONS=5 check && return 0 || test_failure=1
	(
		set +x
		echo "=== trying to find all regression.diffs files in build directory ==="
		find "$1" -name 'regression.diffs' | \
		while read line; do
			echo "=== make failure: $line ==="
			cat "$line"
		done
	)
}

test_failure=0

%if %runselftest
	run_testsuite "src/test/regress"
	make clean -C "src/test/regress"
	run_testsuite "src/pl"
	run_testsuite "contrib"
%endif

# "assert(ALL_TESTS_OK)"
test "$test_failure" -eq 0

%if %test
	# undo the "make clean" above
	make all -C src/test/regress
%endif

%if %upgrade
	pushd postgresql-%{prevversion}

	# The upgrade build can be pretty stripped-down, but make sure that
	# any options that affect on-disk file layout match the previous
	# major release!

	# The set of built server modules here should ideally create superset
	# of modules we used to ship in %%prevversion (in the installation
	# the user will upgrade from), including *-contrib or *-pl*
	# subpackages.  This increases chances that the upgrade from
	# %%prevversion will work smoothly.

upgrade_configure ()
{
	# Note we intentionally do not use %%configure here, because we *don't* want
	# its ideas about installation paths.

	# The -fno-aggressive-loop-optimizations is hack for #993532
	CFLAGS="$CFLAGS -fno-aggressive-loop-optimizations -DOPENSSL_NO_ENGINE" ./configure \
		--build=%{_build} \
		--host=%{_host} \
		--prefix=%prev_prefix \
		--disable-rpath \
		--with-lz4 \
		--with-zstd \
%if %icu
		--with-icu \
%endif
%if %plperl
		--with-perl \
%endif
%if %pltcl
		--with-tcl \
%endif
%if %ldap
       --with-ldap \
%endif
%if %pam
       --with-pam \
%endif
%if %kerberos
       --with-gssapi \
%endif
%if %uuid
       --with-ossp-uuid \
%endif
%if %xml
       --with-libxml \
       --with-libxslt \
%endif
%if %nls
       --enable-nls \
%endif
%if %sdt
       --enable-dtrace \
%endif
%if %selinux
%if %ssl
       --with-openssl \
%endif
       --with-selinux \
%endif
%if %plpython3
		--with-python \
%endif
		--with-tclconfig=/usr/%_lib \
		--with-system-tzdata=/usr/share/zoneinfo \
		"$@"
}

	upgrade_configure \

	make %{?_smp_mflags} all
	make -C contrib %{?_smp_mflags} all
	popd
# endif upgrade
%endif

%if %pgaudit
%make_build -C contrib/pgaudit
%endif

%if %pg_repack
%make_build -C contrib/pg_repack
%endif

%if %pgvector
%make_build -C contrib/pgvector
%endif

%if %decoderbufs
%make_build -C contrib/decoderbufs
%endif


%install
cd postgresql-setup-%{setup_version}
make install DESTDIR=$RPM_BUILD_ROOT
cd ..

# For some reason, having '%%doc %%{_pkgdocdir}/README.rpm-dist' in %%files
# causes FTBFS (at least on RHEL6), see rhbz#1250006.
mv $RPM_BUILD_ROOT/%{_pkgdocdir}/README.rpm-dist ./

cat > $RPM_BUILD_ROOT%{_sysconfdir}/postgresql-setup/upgrade/postgresql.conf <<EOF
id              postgresql
major           %{prevmajorversion}
data_default    %{_localstatedir}/pgsql/data
package         postgresql-upgrade
engine          %{_libdir}/pgsql/postgresql-%{prevmajorversion}/bin
description     "Upgrade data from system PostgreSQL version (PostgreSQL %{prevmajorversion})"
redhat_sockets_hack no
EOF

make DESTDIR=$RPM_BUILD_ROOT install-world

%if %pgaudit
make -C contrib/pgaudit DESTDIR=$RPM_BUILD_ROOT install
%endif

%if %pg_repack
make -C contrib/pg_repack DESTDIR=$RPM_BUILD_ROOT install
%endif

%if %pgvector
make -C contrib/pgvector DESTDIR=$RPM_BUILD_ROOT install
%endif

%if %decoderbufs
make -C contrib/decoderbufs DESTDIR=$RPM_BUILD_ROOT install
%endif

# We ship pg_config through libpq-devel
mv $RPM_BUILD_ROOT/%_mandir/man1/pg_{,server_}config.1
%if %external_libpq
rm $RPM_BUILD_ROOT/%_includedir/pg_config*.h
rm $RPM_BUILD_ROOT/%_includedir/libpq/libpq-fs.h
rm $RPM_BUILD_ROOT/%_includedir/postgres_ext.h
rm -r $RPM_BUILD_ROOT/%_includedir/pgsql/internal/
%else
ln -s pg_server_config $RPM_BUILD_ROOT/%_bindir/pg_config
rm $RPM_BUILD_ROOT/%{_libdir}/libpq.a
%endif

# make sure these directories exist even if we suppressed all contrib modules
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/pgsql/contrib
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/pgsql/extension

%if %{undefined rhel}
# multilib header hack
for header in \
	%{_includedir}/pgsql/server/pg_config.h
do
%multilib_fix_c_header --file "$header"
done
%endif

install -d -m 755 $RPM_BUILD_ROOT%{_libdir}/pgsql/tutorial
cp -p src/tutorial/* $RPM_BUILD_ROOT%{_libdir}/pgsql/tutorial

%if %pam
install -d $RPM_BUILD_ROOT/etc/pam.d
install -m 644 %{SOURCE10} $RPM_BUILD_ROOT/etc/pam.d/postgresql
%endif

mkdir -p $RPM_BUILD_ROOT%{_tmpfilesdir}
install -m 0644 %{SOURCE9} $RPM_BUILD_ROOT%{_tmpfilesdir}/postgresql.conf

# PGDATA needs removal of group and world permissions due to pg_pwd hole.
install -d -m 700 $RPM_BUILD_ROOT%{?_localstatedir}/lib/pgsql/data

# backups of data go here...
install -d -m 700 $RPM_BUILD_ROOT%{?_localstatedir}/lib/pgsql/backups

# postgres' .bash_profile
install -m 644 %{SOURCE11} $RPM_BUILD_ROOT%{?_localstatedir}/lib/pgsql/.bash_profile

rm $RPM_BUILD_ROOT/%{_datadir}/man/man1/ecpg.1

%if %upgrade
	# Install PostgreSQL 18 for upgrade
	pushd postgresql-%{prevversion}
	make DESTDIR=$RPM_BUILD_ROOT install
	make -C contrib DESTDIR=$RPM_BUILD_ROOT install
	popd

	# remove stuff we don't actually need for upgrade purposes
	pushd $RPM_BUILD_ROOT%{_libdir}/pgsql/postgresql-%{prevmajorversion}
	rm bin/clusterdb
	rm bin/createdb
	rm bin/createuser
	rm bin/dropdb
	rm bin/dropuser
	rm bin/ecpg
	rm bin/initdb
	rm bin/pg_basebackup
	rm bin/pg_dump
	rm bin/pg_dumpall
	rm bin/pg_restore
	rm bin/pgbench
	rm bin/psql
	rm bin/reindexdb
	rm bin/vacuumdb
	rm -rf share/doc
	rm -rf share/man
	rm -rf share/tsearch_data
	rm lib/*.a
	# Drop libpq.  This might need some tweaks once there's
	# soname bump between %%prevversion and %%version.
	rm lib/libpq.so*
	# Drop libraries.
	rm lib/lib{ecpg,ecpg_compat,pgtypes}.so*
	rm share/*.bki
	rm share/*.sample
	rm share/*.sql
	rm share/*.txt
	rm share/extension/*.sql
	rm share/extension/*.control
	popd
	cat <<EOF > $RPM_BUILD_ROOT%macrosdir/macros.postgresql-upgrade
%%postgresql_upgrade_prefix %prev_prefix
EOF
%endif

# Let plugins use the same llvmjit settings as server has
cat <<EOF >> $RPM_BUILD_ROOT%macrosdir/macros.postgresql
%%postgresql_server_llvmjit %llvmjit
EOF

%if %test
	# tests. There are many files included here that are unnecessary,
	# but include them anyway for completeness.  We replace the original
	# Makefiles, however.
	mkdir -p $RPM_BUILD_ROOT%{_libdir}/pgsql/test
	cp -a src/test/regress $RPM_BUILD_ROOT%{_libdir}/pgsql/test
	# pg_regress binary should be only in one subpackage,
	# there will be a symlink from -test to -devel
	rm -f $RPM_BUILD_ROOT%{_libdir}/pgsql/test/regress/pg_regress
	rm -f $RPM_BUILD_ROOT%{_libdir}/pgsql/test/regress/refint.so
	rm -f $RPM_BUILD_ROOT%{_libdir}/pgsql/test/regress/autoinc.so
	ln -sf ../../pgxs/src/test/regress/pg_regress $RPM_BUILD_ROOT%{_libdir}/pgsql/test/regress/pg_regress
	ln -sf ../../autoinc.so $RPM_BUILD_ROOT%{_libdir}/pgsql/test/regress/autoinc.so
	ln -sf ../../refint.so $RPM_BUILD_ROOT%{_libdir}/pgsql/test/regress/refint.so
	pushd  $RPM_BUILD_ROOT%{_libdir}/pgsql/test/regress
	rm -f GNUmakefile Makefile *.o
	chmod 0755 pg_regress regress.so
	popd
	sed 's|@bindir@|%{_bindir}|g' \
		< %{SOURCE4} \
		> $RPM_BUILD_ROOT%{_libdir}/pgsql/test/regress/Makefile
	chmod 0644 $RPM_BUILD_ROOT%{_libdir}/pgsql/test/regress/Makefile
%endif

rm -rf doc/html # HACK! allow 'rpmbuild -bi --short-circuit'
mv $RPM_BUILD_ROOT%{_docdir}/pgsql/html doc
rm -rf $RPM_BUILD_ROOT%{_docdir}/pgsql

# remove files not to be packaged
rm $RPM_BUILD_ROOT%{_libdir}/libpgfeutils.a

%if !%plperl
rm -f $RPM_BUILD_ROOT%{_bindir}/pgsql/hstore_plperl.so
%endif

# no python2, yet installed, remove
rm -f $RPM_BUILD_ROOT%{_datadir}/pgsql/extension/*_plpythonu*
rm -f $RPM_BUILD_ROOT%{_datadir}/pgsql/extension/*_plpython2u*

%if %nls
find_lang_bins ()
{
	lstfile=$1 ; shift
	cp /dev/null "$lstfile"
	for binary; do
		%find_lang "$binary"-%{majorversion}
		cat "$binary"-%{majorversion}.lang >>"$lstfile"
	done
}
find_lang_bins devel.lst pg_server_config
find_lang_bins server.lst \
	initdb pg_basebackup pg_controldata pg_ctl pg_resetwal pg_rewind plpgsql \
	postgres pg_checksums pg_verifybackup pg_combinebackup \
    pg_walsummary
find_lang_bins contrib.lst \
	pg_amcheck pg_archivecleanup pg_test_fsync pg_test_timing pg_waldump \
	postgresql-regress
find_lang_bins main.lst \
	pg_dump pg_upgrade pgscripts psql \
%if ! %external_libpq
libpq%{private_soname}-5
%endif

%if %plperl
find_lang_bins plperl.lst plperl
%endif
%if %plpython3
find_lang_bins plpython3.lst plpython
%endif
%if %pltcl
find_lang_bins pltcl.lst pltcl
%endif
%endif

install -m0644 -D postgresql19.sysusers.conf %{buildroot}%{_sysusersdir}/postgresql19.conf
install -m0644 -D postgresql19.tmpfiles.conf %{buildroot}%{_tmpfilesdir}/postgresql19.conf

%post -n %{pkgname}-server
%systemd_post %service_name


%preun -n %{pkgname}-server
%systemd_preun %service_name


%postun -n %{pkgname}-server
%systemd_postun_with_restart %service_name


%check
%if %runselftest
make -C postgresql-setup-%{setup_version} check
%endif

# FILES sections.
%files -f main.lst -n %{pkgname}
%doc doc/KNOWN_BUGS doc/MISSING_FEATURES doc/TODO
%doc COPYRIGHT HISTORY
%doc README.rpm-dist
%{_bindir}/clusterdb
%{_bindir}/createdb
%{_bindir}/createuser
%{_bindir}/dropdb
%{_bindir}/dropuser
%{_bindir}/pg_dump
%{_bindir}/pg_dumpall
%{_bindir}/pg_isready
%{_bindir}/pg_restore
%{_bindir}/pg_upgrade
%{_bindir}/psql
%{_bindir}/reindexdb
%{_bindir}/vacuumdb
%{_mandir}/man1/clusterdb.*
%{_mandir}/man1/createdb.*
%{_mandir}/man1/createuser.*
%{_mandir}/man1/dropdb.*
%{_mandir}/man1/dropuser.*
%{_mandir}/man1/pg_dump.*
%{_mandir}/man1/pg_dumpall.*
%{_mandir}/man1/pg_isready.*
%{_mandir}/man1/pg_restore.*
%{_mandir}/man1/pg_upgrade.*
%{_mandir}/man1/psql.*
%{_mandir}/man1/reindexdb.*
%{_mandir}/man1/vacuumdb.*
%{_mandir}/man7/*
%if %llvmjit
# Install bitcode directory along with the main package,
# so that extensions can use this dir.
%dir %{_libdir}/pgsql/bitcode
%endif


%if ! %external_libpq
%files -n %{pkgname}-private-libs
%{_libdir}/libpq.so.*
%endif


%files -n %{pkgname}-docs
%doc doc/html
%{_libdir}/pgsql/tutorial/


%files -n %{pkgname}-contrib -f contrib.lst
%doc contrib/spi/*.example
%{_bindir}/oid2name
%{_bindir}/pg_amcheck
%{_bindir}/pg_archivecleanup
%{_bindir}/pg_test_fsync
%{_bindir}/pg_test_timing
%{_bindir}/pg_waldump

%{_bindir}/pg_walsummary
%{_bindir}/pg_combinebackup

%{_bindir}/pgbench
%{_bindir}/vacuumlo
%{_datadir}/pgsql/extension/amcheck*
%{_datadir}/pgsql/extension/autoinc*
%{_datadir}/pgsql/extension/bloom*
%{_datadir}/pgsql/extension/btree_gin*
%{_datadir}/pgsql/extension/btree_gist*
%{_datadir}/pgsql/extension/citext*
%{_datadir}/pgsql/extension/cube*
%{_datadir}/pgsql/extension/dblink*
%{_datadir}/pgsql/extension/dict_int*
%{_datadir}/pgsql/extension/dict_xsyn*
%{_datadir}/pgsql/extension/earthdistance*
%{_datadir}/pgsql/extension/file_fdw*
%{_datadir}/pgsql/extension/fuzzystrmatch*
%{_datadir}/pgsql/extension/hstore*
%{_datadir}/pgsql/extension/insert_username*
%{_datadir}/pgsql/extension/intagg*
%{_datadir}/pgsql/extension/intarray*
%{_datadir}/pgsql/extension/isn*
%if %{plperl}
%{_datadir}/pgsql/extension/jsonb_plperl*
%endif
%if %{plpython3}
%{_datadir}/pgsql/extension/jsonb_plpython3u*
%endif
%{_datadir}/pgsql/extension/lo*
%{_datadir}/pgsql/extension/pg_logicalinspect*
%{_datadir}/pgsql/extension/ltree*
%{_datadir}/pgsql/extension/moddatetime*
%{_datadir}/pgsql/extension/pageinspect*
%{_datadir}/pgsql/extension/pg_buffercache*
%{_datadir}/pgsql/extension/pg_freespacemap*
%{_datadir}/pgsql/extension/pg_prewarm*
%{_datadir}/pgsql/extension/pg_stat_statements*
%{_datadir}/pgsql/extension/pg_surgery*
%{_datadir}/pgsql/extension/pg_trgm*
%{_datadir}/pgsql/extension/pg_visibility*
%{_datadir}/pgsql/extension/pg_walinspect*
%{_datadir}/pgsql/extension/pgcrypto*
%{_datadir}/pgsql/extension/pgrowlocks*
%{_datadir}/pgsql/extension/pgstattuple*
%{_datadir}/pgsql/extension/postgres_fdw*
%{_datadir}/pgsql/extension/refint*
%{_datadir}/pgsql/extension/seg*
%{_datadir}/pgsql/extension/tablefunc*
%{_datadir}/pgsql/extension/tcn*
%{_datadir}/pgsql/extension/tsm_system_rows*
%{_datadir}/pgsql/extension/tsm_system_time*
%{_datadir}/pgsql/extension/unaccent*
%{_libdir}/pgsql/_int.so
%{_libdir}/pgsql/amcheck.so
%{_libdir}/pgsql/auth_delay.so
%{_libdir}/pgsql/auto_explain.so
%{_libdir}/pgsql/autoinc.so
%{_libdir}/pgsql/bloom.so
%{_libdir}/pgsql/btree_gin.so
%{_libdir}/pgsql/btree_gist.so
%{_libdir}/pgsql/citext.so
%{_libdir}/pgsql/cube.so
%{_libdir}/pgsql/dblink.so
%{_libdir}/pgsql/dict_int.so
%{_libdir}/pgsql/dict_xsyn.so
%{_libdir}/pgsql/earthdistance.so
%{_libdir}/pgsql/file_fdw.so
%{_libdir}/pgsql/fuzzystrmatch.so
%{_libdir}/pgsql/hstore.so
%if %plperl
%{_libdir}/pgsql/hstore_plperl.so
%endif
%if %plpython3
%{_libdir}/pgsql/hstore_plpython3.so
%endif
%{_libdir}/pgsql/insert_username.so
%{_libdir}/pgsql/isn.so
%if %plperl
%{_libdir}/pgsql/jsonb_plperl.so
%endif
%if %plpython3
%{_libdir}/pgsql/jsonb_plpython3.so
%endif
%{_libdir}/pgsql/lo.so
%{_libdir}/pgsql/ltree.so
%if %plpython3
%{_libdir}/pgsql/ltree_plpython3.so
%endif
%{_libdir}/pgsql/pg_logicalinspect.so
%{_libdir}/pgsql/pg_overexplain.so
%{_libdir}/pgsql/moddatetime.so
%{_libdir}/pgsql/pageinspect.so
%{_libdir}/pgsql/passwordcheck.so
%{_libdir}/pgsql/pg_buffercache.so
%{_libdir}/pgsql/pg_freespacemap.so
%{_libdir}/pgsql/pg_stat_statements.so
%{_libdir}/pgsql/pg_surgery.so
%{_libdir}/pgsql/pg_trgm.so
%{_libdir}/pgsql/pg_visibility.so
%{_libdir}/pgsql/pg_walinspect.so
%{_libdir}/pgsql/basic_archive.so
%{_libdir}/pgsql/basebackup_to_shell.so
%{_libdir}/pgsql/pgcrypto.so
%{_libdir}/pgsql/pgrowlocks.so
%{_libdir}/pgsql/pgstattuple.so
%{_libdir}/pgsql/postgres_fdw.so
%{_libdir}/pgsql/refint.so
%{_libdir}/pgsql/seg.so
%{_libdir}/pgsql/tablefunc.so
%{_libdir}/pgsql/tcn.so
%{_libdir}/pgsql/test_decoding.so
%{_libdir}/pgsql/tsm_system_rows.so
%{_libdir}/pgsql/tsm_system_time.so
%{_libdir}/pgsql/unaccent.so
%{_libdir}/pgsql/cyrillic.so
%{_libdir}/pgsql/pg_plan_advice.so
%{_libdir}/pgsql/pg_stash_advice.so
%{_libdir}/pgsql/pgrepack.so
%{_datadir}/pgsql/extension/pg_stash_advice*
%{_mandir}/man1/oid2name.*
%{_mandir}/man1/pg_amcheck.*
%{_mandir}/man1/pg_archivecleanup.*
%{_mandir}/man1/pg_recvlogical.*
%{_mandir}/man1/pg_test_fsync.*
%{_mandir}/man1/pg_test_timing.*
%{_mandir}/man1/pg_waldump.*
%{_mandir}/man1/pgbench.*
%{_mandir}/man1/vacuumlo.*
%{_mandir}/man3/dblink*
%if %selinux
%{_datadir}/pgsql/contrib/sepgsql.sql
%{_libdir}/pgsql/sepgsql.so
%endif
%if %ssl
%{_datadir}/pgsql/extension/sslinfo*
%{_libdir}/pgsql/sslinfo.so
%endif
%if %uuid
%{_datadir}/pgsql/extension/uuid-ossp*
%{_libdir}/pgsql/uuid-ossp.so
%endif
%if %xml
%{_datadir}/pgsql/extension/xml2*
%{_libdir}/pgsql/pgxml.so
%endif

%files -n %{pkgname}-server -f server.lst
%{_bindir}/initdb
%{_bindir}/pg_basebackup

%{_bindir}/pg_controldata
%{_bindir}/pg_ctl
%{_bindir}/pg_receivewal
%{_bindir}/pg_recvlogical
%{_bindir}/pg_resetwal
%{_bindir}/pg_rewind
%{_bindir}/pg_checksums
%{_bindir}/pg_verifybackup

%{_bindir}/pg_createsubscriber

%{_bindir}/postgres
%{_bindir}/postgresql-setup
%{_bindir}/postgresql-upgrade
%dir %{_datadir}/pgsql
%{_datadir}/pgsql/*.sample
%dir %{_datadir}/pgsql/contrib
%dir %{_datadir}/pgsql/extension
%{_datadir}/pgsql/extension/plpgsql*
%{_datadir}/pgsql/information_schema.sql
%{_datadir}/pgsql/postgres.bki
%{_datadir}/pgsql/snowball_create.sql
%{_datadir}/pgsql/sql_features.txt
%{_datadir}/pgsql/system_constraints.sql
%{_datadir}/pgsql/system_functions.sql
%{_datadir}/pgsql/system_views.sql
%{_datadir}/pgsql/timezonesets/
%{_datadir}/pgsql/tsearch_data/
%dir %{_datadir}/postgresql-setup
%{_datadir}/postgresql-setup/library.sh
%dir %{_libdir}/pgsql
%{_libdir}/pgsql/*_and_*.so
%{_libdir}/pgsql/dict_snowball.so
%{_libdir}/pgsql/euc2004_sjis2004.so
%{_libdir}/pgsql/libpqwalreceiver.so
%{_libdir}/pgsql/pg_prewarm.so
%{_libdir}/pgsql/pgoutput.so
%{_libdir}/pgsql/plpgsql.so
%dir %{_usr}/libexec/initscripts/legacy-actions/postgresql
%{_usr}/libexec/initscripts/legacy-actions/postgresql/*
%{_libexecdir}/postgresql-check-db-dir
%dir %{_sysconfdir}/postgresql-setup
%dir %{_sysconfdir}/postgresql-setup/upgrade
%config %{_sysconfdir}/postgresql-setup/upgrade/*.conf
%{_mandir}/man1/initdb.*
%{_mandir}/man1/pg_basebackup.*
%{_mandir}/man1/pg_controldata.*
%{_mandir}/man1/pg_ctl.*
%{_mandir}/man1/pg_receivewal.*
%{_mandir}/man1/pg_resetwal.*
%{_mandir}/man1/pg_rewind.*
%{_mandir}/man1/pg_checksums.*
%{_mandir}/man1/pg_verifybackup.*
%{_mandir}/man1/postgres.*
%{_mandir}/man1/postgresql-new-systemd-unit.*
%{_mandir}/man1/postgresql-setup.*
%{_mandir}/man1/postgresql-upgrade.*

%{_mandir}/man1/pg_walsummary.*
%{_mandir}/man1/pg_combinebackup.*
%{_mandir}/man1/pg_createsubscriber.*

%{_sbindir}/postgresql-new-systemd-unit
%{_tmpfilesdir}/postgresql.conf
%{_unitdir}/*postgresql*.service
%attr(700,postgres,postgres) %dir %{?_localstatedir}/lib/pgsql
%attr(644,postgres,postgres) %config(noreplace) %{?_localstatedir}/lib/pgsql/.bash_profile
%attr(700,postgres,postgres) %dir %{?_localstatedir}/lib/pgsql/backups
%attr(700,postgres,postgres) %dir %{?_localstatedir}/lib/pgsql/data
%ghost %attr(755,postgres,postgres) %dir %{_rundir}/postgresql
%if %pam
%config(noreplace) /etc/pam.d/postgresql
%endif
%{_sysusersdir}/postgresql19.conf
%{_tmpfilesdir}/postgresql19.conf

%files -n %{pkgname}-server-devel -f devel.lst
%{_bindir}/pg_server_config
%dir %{_datadir}/pgsql
%{_datadir}/pgsql/errcodes.txt
%dir %{_includedir}/pgsql
%{_includedir}/pgsql/server
%{_libdir}/pgsql/pgxs/
%{_mandir}/man1/pg_server_config.*
%{_mandir}/man3/SPI_*
%{macrosdir}/macros.postgresql


%if ! %external_libpq
%files -n %{pkgname}-private-devel
%{_bindir}/pg_config
%{_includedir}/libpq-events.h
%{_includedir}/libpq-fe.h
%{_includedir}/postgres_ext.h
%{_includedir}/pgsql/internal/*.h
%{_includedir}/pgsql/internal/libpq/pqcomm.h

%{_includedir}/pgsql/internal/libpq/protocol.h

%{_includedir}/libpq/*.h
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libpq.so
%{_includedir}/pg_config*.h
%endif


%files -n %{pkgname}-test-rpm-macros
%{_datadir}/postgresql-setup/postgresql_pkg_tests.sh
%{macrosdir}/macros.postgresql-test


%files -n %{pkgname}-static
%{_libdir}/libpgcommon.a
%{_libdir}/libpgport.a
%{_libdir}/libpgcommon_shlib.a
%{_libdir}/libpgport_shlib.a


%if %upgrade
%files -n %{pkgname}-upgrade
%{_libdir}/pgsql/postgresql-%{prevmajorversion}/bin
%exclude %{_libdir}/pgsql/postgresql-%{prevmajorversion}/bin/pg_config
%{_libdir}/pgsql/postgresql-%{prevmajorversion}/lib
%exclude %{_libdir}/pgsql/postgresql-%{prevmajorversion}/lib/pgxs
%exclude %{_libdir}/pgsql/postgresql-%{prevmajorversion}/lib/pkgconfig
%{_libdir}/pgsql/postgresql-%{prevmajorversion}/share


%files -n %{pkgname}-upgrade-devel
%{_libdir}/pgsql/postgresql-%{prevmajorversion}/bin/pg_config
%{_libdir}/pgsql/postgresql-%{prevmajorversion}/include
%{_libdir}/pgsql/postgresql-%{prevmajorversion}/lib/pkgconfig
%{_libdir}/pgsql/postgresql-%{prevmajorversion}/lib/pgxs
%{macrosdir}/macros.postgresql-upgrade
%endif

%if %llvmjit
%files -n %{pkgname}-llvmjit
%defattr(-,root,root)
%{_libdir}/pgsql/bitcode/*
%{_libdir}/pgsql/llvmjit.so
%{_libdir}/pgsql/llvmjit_types.bc
%endif

%if %plperl
%files -n %{pkgname}-plperl -f plperl.lst
%{_datadir}/pgsql/extension/bool_plperl*
%{_datadir}/pgsql/extension/plperl*
%{_libdir}/pgsql/bool_plperl.so
%{_libdir}/pgsql/plperl.so
%endif


%if %pltcl
%files -n %{pkgname}-pltcl -f pltcl.lst
%{_datadir}/pgsql/extension/pltcl*
%{_libdir}/pgsql/pltcl.so
%endif


%if %plpython3
%files -n %{pkgname}-plpython3 -f plpython3.lst
%{_datadir}/pgsql/extension/plpython3*
%{_libdir}/pgsql/plpython3.so
%endif


%if %test
%files -n %{pkgname}-test
%attr(-,postgres,postgres) %{_libdir}/pgsql/test
%endif


%if %pgaudit
%files -n %{pkgname}-pgaudit
%license contrib/pgaudit/LICENSE
%{_libdir}/pgsql/pgaudit.so
%if 0%{?postgresql_server_llvmjit}
%{_libdir}/pgsql/bitcode/pgaudit.index.bc
%{_libdir}/pgsql/bitcode/pgaudit/pgaudit.bc
%endif
%{_datadir}/pgsql/extension/pgaudit--*.sql
%{_datadir}/pgsql/extension/pgaudit.control
%endif

%if %pg_repack
%files -n %{pkgname}-pg-repack
%license contrib/pg_repack/COPYRIGHT
%{_bindir}/pg_repack
%{_libdir}/pgsql/pg_repack.so
%{_datadir}/pgsql/extension/pg_repack--*.sql
%{_datadir}/pgsql/extension/pg_repack.control
%endif

%if %pgvector
%files -n %{pkgname}-pgvector
%license contrib/pgvector/LICENSE
%{_libdir}/pgsql/vector.so
%{_datadir}/pgsql/extension/vector--*.sql
%{_datadir}/pgsql/extension/vector.control
%{_includedir}/pgsql/server/extension/vector/vector.h
%endif

%if %decoderbufs
%files -n %{pkgname}-decoderbufs
%license contrib/decoderbufs/LICENSE
%{_libdir}/pgsql/decoderbufs.so
%endif


%changelog
* Wed Jul 22 2026 Python Maint <python-maint@redhat.com> - 19beta1-3
- Rebuilt for Python 3.15.0b4 ABI change

* Thu Jul 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 19beta1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Fri Jun 12 2026 Filip Janus <fjanus@redhat.com> - 19beta1-1
- Initial build of postgresql 19 (beta1)
- Based on postgresql18 package
- Integrate pgaudit extension as subpackage
- Support upgrade from PostgreSQL 18 only

