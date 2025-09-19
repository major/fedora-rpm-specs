%global catch_version 2.13.10
%global cli11_version 2.4.2
%global fmt_version 11.0.2
%global libosmium_version 2.20.0
%global protozero_version 1.7.1

Name:           osm2pgsql
Version:        2.2.0
Release:        %autorelease
Summary:        Import map data from OpenStreetMap to a PostgreSQL database

License:        GPL-2.0-or-later
URL:            https://osm2pgsql.org/
Source0:        https://github.com/osm2pgsql-dev/osm2pgsql/archive/%{version}/%{name}-%{version}.tar.gz

ExcludeArch:    %{ix86}

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  libtool
BuildRequires:  boost-devel
BuildRequires:  bzip2-devel
BuildRequires:  catch2-devel >= %{catch_version}
BuildRequires:  catch2-static >= %{catch_version}
BuildRequires:  cli11-devel >= %{cli11_version}
BuildRequires:  cli11-static >= %{cli11_version}
BuildRequires:  expat-devel
BuildRequires:  fmt-devel >= %{fmt_version}
BuildRequires:  json-devel
BuildRequires:  libosmium-devel >= %{libosmium_version}
BuildRequires:  libpq-devel
BuildRequires:  libxml2-devel
BuildRequires:  lua-devel
BuildRequires:  proj-devel
BuildRequires:  protozero-devel >= %{protozero_version}
BuildRequires:  protozero-static >= %{protozero_version}
BuildRequires:  zlib-devel
BuildRequires:  postgresql
BuildRequires:  postgresql-contrib
BuildRequires:  postgresql-test-rpm-macros
BuildRequires:  postgis
BuildRequires:  python3
BuildRequires:  python3-behave
BuildRequires:  python3-osmium
BuildRequires:  python3-psycopg2

%description
Provides a tool for loading OpenStreetMap data into a PostgreSQL / PostGIS
database suitable for applications like rendering into a map, geocoding with
Nominatim, or general analysis.

%prep
%autosetup -p1
rm -rf contrib
mkdir -p contrib/catch2
ln -sf /usr/include/catch2 contrib/catch2/include

%build
%cmake \
  -DEXTERNAL_CLI11=ON \
  -DEXTERNAL_FMT=ON \
  -DEXTERNAL_LIBOSMIUM=ON \
  -DEXTERNAL_PROTOZERO=ON \
  -DBUILD_TESTS=ON \
%cmake_build

%install
%cmake_install

%check
PGTESTS_LOCALE="C.UTF-8" %postgresql_tests_run
echo "local all all trust" > datadir/pg_hba.conf
psql -c "SELECT pg_reload_conf()" postgres
mkdir tablespacetest
psql -c "CREATE TABLESPACE tablespacetest LOCATION '$PWD/tablespacetest'" postgres
LANG="C.UTF-8" %ctest -j1

%files
%doc AUTHORS CONTRIBUTING.md README.md
%license COPYING
%{_mandir}/man1//%{name}*.1*
%{_bindir}/%{name}*
%{_datadir}/%{name}/

%changelog
%autochangelog
