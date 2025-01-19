Name:           lua-sql
Version:        2.5.0
Release:        13%{?dist}
Summary:        Database connectivity for the Lua programming language

License:        MIT
URL:            https://keplerproject.github.io/luasql/
Source0:        https://github.com/keplerproject/luasql/archive/%{version}.tar.gz#/luasql-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  lua-devel >= 5.1
BuildRequires:  pkgconfig
BuildRequires:  sqlite-devel >= 3.0
BuildRequires:  mariadb-connector-c-devel openssl-devel
BuildRequires:  libpq-devel
BuildRequires: make

Requires:       lua-sql-mysql%{?_isa} = %{version}-%{release}
Requires:       lua-sql-postgresql%{?_isa} = %{version}-%{release}
Requires:       lua-sql-sqlite%{?_isa} = %{version}-%{release}

%description
LuaSQL is a simple interface from Lua to a DBMS. This package of LuaSQL
supports MySQL, SQLite and PostgreSQL databases. You can execute arbitrary SQL
statements and it allows for retrieving results in a row-by-row cursor fashion.


%package doc
Summary:        Documentation for LuaSQL
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description doc
LuaSQL is a simple interface from Lua to a DBMS. This package contains the
documentation for LuaSQL.


%package sqlite
Summary:        SQLite database connectivity for the Lua programming language

%description sqlite
LuaSQL is a simple interface from Lua to a DBMS. This package provides access
to SQLite databases.


%package mysql
Summary:        MySQL database connectivity for the Lua programming language

%description mysql
LuaSQL is a simple interface from Lua to a DBMS. This package provides access
to MySQL databases.


%package postgresql
Summary:        PostgreSQL database connectivity for the Lua programming language

%description postgresql
LuaSQL is a simple interface from Lua to a DBMS. This package provides access
to PostgreSQL databases.


%prep
%autosetup -n luasql-%{version} -p1


%build
make %{?_smp_mflags} sqlite3 PREFIX=%{_prefix} DRIVER_INCS_sqlite3="`pkg-config --cflags sqlite3`" DRIVER_LIBS_sqlite3="`pkg-config --libs sqlite3`" DEFS="%{optflags} -fPIC -std=c99 -DLUA_COMPAT_APIINTCASTS"
make %{?_smp_mflags} postgres PREFIX=%{_prefix} DRIVER_INCS_postgres="" DRIVER_LIBS_postgres="-lpq" DEFS="%{optflags} -fPIC -std=c99 -DLUA_COMPAT_APIINTCASTS" WARN=
make %{?_smp_mflags} mysql PREFIX=%{_prefix} DRIVER_INCS_mysql="`mysql_config --include`" DRIVER_LIBS_mysql="`mysql_config --libs`" DEFS="%{optflags} -fPIC -std=c99 -DLUA_COMPAT_APIINTCASTS"


%install
make install PREFIX=$RPM_BUILD_ROOT%{_prefix} LUA_LIBDIR=$RPM_BUILD_ROOT%{lua_libdir} LUA_DIR=$RPM_BUILD_ROOT%{lua_pkgdir} T=sqlite3
make install PREFIX=$RPM_BUILD_ROOT%{_prefix} LUA_LIBDIR=$RPM_BUILD_ROOT%{lua_libdir} LUA_DIR=$RPM_BUILD_ROOT%{lua_pkgdir} T=postgres
make install PREFIX=$RPM_BUILD_ROOT%{_prefix} LUA_LIBDIR=$RPM_BUILD_ROOT%{lua_libdir} LUA_DIR=$RPM_BUILD_ROOT%{lua_pkgdir} T=mysql


%files
%license doc/us/license.html doc/us/doc.css doc/us/luasql.png
%doc README

%files doc
%doc doc/us/*

%files mysql
%dir %{lua_libdir}/luasql
%{lua_libdir}/luasql/mysql.so

%files postgresql
%dir %{lua_libdir}/luasql
%{lua_libdir}/luasql/postgres.so

%files sqlite
%dir %{lua_libdir}/luasql
%{lua_libdir}/luasql/sqlite3.so


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Feb 08 2021 Pavel Raiskup <praiskup@redhat.com> - 2.5.0-4
- rebuild for libpq ABI fix rhbz#1908268

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 27 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 2.5.0-2
- Use standard Lua macros

* Tue Aug 25 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 2.5.0-1
- Update to 2.5.0
- Ensure base package ships license file

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Tim Niemueller <tim@niemueller.de> - 2.3.5-7
- Depend on MariaDB package (bz #1493688)
- BR gcc

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.3.5-6
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Mon Jul 31 2017 Florian Weimer <fweimer@redhat.com> - 2.3.5-3
- Rebuild with binutils fix for ppc64le (#1475636)
- Fix build failure with MariaDB

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Adam Williamson <awilliam@redhat.com> - 2.3.5-1
- New release 2.3.5
- Rebuild against MariaDB 10.2

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 16 2015 Tom Callaway <spot@fedoraproject.org> - 2.3.0-5
- rebuild for lua 5.3

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 13 2013 Tom Callaway <spot@fedoraproject.org> - 2.3.0-1
- update to 2.3.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Mar 23 2011 Dan Horák <dan@danny.cz> - 2.2.0-2
- rebuilt for mysql 5.5.10 (soname bump in libmysqlclient)

* Tue Mar 22 2011 Tim Niemueller <tim@niemueller.de> - 2.2.0-1
- Upgrade to latest stable release 2.2.0
- Rebuilt for MySQL 5.5
- Added patch for F-14 and up

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 23 2009 Tim Niemueller <tim@niemueller.de> - 2.1.1-5
- Rebuilt for MySQL 5.1

* Tue Apr 08 2008 Tim Niemueller <tim@niemueller.de> - 2.1.1-4
- Main package is now pure meta package to pull in everything else, README
  moved to doc sub-package.

* Sat Apr 05 2008 Tim Niemueller <tim@niemueller.de> - 2.1.1-3
- Do not use pg_config and mysql_config, they are not good for what you think
  they should be used for, cf. #440673

* Fri Apr 04 2008 Tim Niemueller <tim@niemueller.de> - 2.1.1-2
- Fixed lua-sql-postgres requires
- Own %%{lualibdir}/luasql directory in all sub-packages

* Fri Apr 04 2008 Tim Niemueller <tim@niemueller.de> - 2.1.1-1
- Initial package

