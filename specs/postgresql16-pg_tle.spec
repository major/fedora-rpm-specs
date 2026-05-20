%{!?postgresql_default:%global postgresql_default 0}

%global sname pg_tle
%global pgversion 16
%global pgconfig %{_bindir}/pg_server_config
Name:           postgresql%{pgversion}-%{sname}
Version:        1.5.2
Release:        %autorelease
Summary:        Framework for building and installing trusted language PostgreSQL extensions
License:        Apache-2.0
URL:            https://github.com/aws/%{sname}
Source0:        https://github.com/aws/%{sname}/archive/v%{version}/%{sname}-%{version}.tar.gz

%if %?postgresql_default
%global pkgname %{sname}
%package -n %{pkgname}
Summary: Framework for building and installing trusted language PostgreSQL extensions
%else
%global pkgname %name
%endif

BuildRequires:	gcc
BuildRequires:	flex
BuildRequires:	make
BuildRequires:	postgresql%{pgversion}-server-devel >= 16
Requires:	postgresql%{pgversion}-server >= 16

%global precise_version %{?epoch:%epoch:}%version-%release
%if %?postgresql_default
Provides: postgresql-%{sname} = %precise_version
Provides: %name = %precise_version
%endif
Provides: %{pkgname}%{?_isa} = %precise_version
Provides: %{pkgname} = %precise_version
Provides: %{sname}-any
Conflicts: %{sname}-any

%description
Trusted Language Extensions (pg_tle) is an open-source development kit for
building and deploying PostgreSQL extensions without requiring access to
the underlying file system.

%if %?postgresql_default
%description -n %{pkgname}
Trusted Language Extensions (pg_tle) is an open-source development kit for
building and deploying PostgreSQL extensions without requiring access to
the underlying file system.
%endif

%prep
%autosetup -n %{sname}-%{version}

%build
%make_build PG_CONFIG=%{pgconfig}

%install
%make_install PG_CONFIG=%{pgconfig}

%files
%license LICENSE
%doc README.md
%{_libdir}/pgsql/%{sname}.so
%{_datadir}/pgsql/extension/%{sname}.control
%{_datadir}/pgsql/extension/%{sname}--*.sql

%changelog
%autochangelog
