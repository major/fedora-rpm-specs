Summary:	'top' for PostgreSQL process
Name:		pg_top
Version:	4.1.2
Release:	%autorelease
License:	BSD-3-Clause
Source:		https://gitlab.com/pg_top/pg_top/-/archive/v%{version}/pg_top-v%{version}.tar.bz2
URL:		https://pg_top.gitlab.io/
BuildRequires:	cmake
BuildRequires:	elfutils-libelf-devel
BuildRequires:	gcc
BuildRequires:	libbsd-devel
BuildRequires:	libpq-devel
BuildRequires:	readline-devel
BuildRequires:	/usr/bin/rst2man
Requires:	postgresql-server

%description
pg_top is 'top' for PostgreSQL processes. See running queries, 
query plans, issued locks, and table and index statistics.

%prep
%autosetup -n %{name}-v%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%{_mandir}/man1/%{name}*
%{_bindir}/%{name}
%doc HISTORY.rst README.rst TODO Y2K
%license LICENSE

%changelog
%autochangelog
