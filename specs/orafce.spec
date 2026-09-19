Name:		orafce
Version:	4.16.10
Release:	%autorelease
Summary:	Implementation of some Oracle functions into PostgreSQL
License:	0BSD
URL:		https://github.com/orafce/orafce
Source:		%{url}/archive/VERSION_%{gsub %{version} %%. _}.tar.gz

Requires(pre): postgresql-server

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	clang-devel llvm-devel
BuildRequires:	postgresql-server-devel openssl-devel krb5-devel bison flex


%description
The goal of this project is implementation some functions from Oracle database.
Some date functions (next_day, last_day, trunc, round, ...) are implemented
now. Functionality was verified on Oracle 10g and module is useful
for production work.


%prep
%setup -q -n %{name}-VERSION_%{gsub %{version} %%. _}


%build
%make_build USE_PGXS=1 PG_CONFIG=/usr/bin/pg_server_config


%install
%make_install USE_PGXS=1 PG_CONFIG=/usr/bin/pg_server_config


%files
%license COPYRIGHT.orafce
%doc INSTALL.orafce README.asciidoc
%{_libdir}/pgsql/
%{_datadir}/pgsql/
%exclude %{_docdir}/pgsql/


%changelog
%autochangelog
