Name:          pgrouting
Version:       3.8.0
Release:       %autorelease
Summary:       Provides routing functionality to PostGIS / PostgreSQL
License:       GPL-2.0-or-later AND BSL-1.0 AND MIT
URL:           https://pgrouting.org
Source:        https://github.com/pgRouting/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires: boost-devel
BuildRequires: boost-graph
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: perl-File-Find
BuildRequires: perl-interpreter
BuildRequires: perl-version
BuildRequires: postgresql-server-devel
Requires:      postgis
Requires:      postgresql-server

%description
pgRouting extends the PostGIS / PostgreSQL geospatial database to provide
geospatial routing functionality.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%cmake -DPOSTGRESQL_PG_CONFIG=%{_bindir}/pg_server_config
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%license BOOST_LICENSE_1_0.txt
%license tools/licences/MIT_license.txt
%license tools/licences/GNU_license.txt
%license tools/licences/CCM_license.txt
%doc CODE_OF_CONDUCT.md NEWS README.md CONTRIBUTING.md
%{_libdir}/pgsql/libpgrouting-%{sub %version 1 3}.so
%{_datadir}/pgsql/extension/pgrouting--*--%{version}.sql
%{_datadir}/pgsql/extension/pgrouting--%{version}.sql
%{_datadir}/pgsql/extension/pgrouting.control

%changelog
%autochangelog
