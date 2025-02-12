%{!?postgresql_default:%global postgresql_default 1}

%global pname vector
%global sname pgvector
%global pgversion 16

%ifarch ppc64 ppc64le s390 s390x armv7hl
	%{!?llvm:%global llvm 0}
%else
	%{!?llvm:%global llvm 0}
%endif

Name:		postgresql%{pgversion}-%{sname}
Version:	0.6.2
Release:	4%{?dist}
Summary:	Open-source vector similarity search for Postgres
License:	PostgreSQL
URL:		https://github.com/%{sname}/%{sname}/
Source0:	https://github.com/%{sname}/%{sname}/archive/refs/tags/v%{version}.tar.gz

%if %?postgresql_default
%global pkgname %{sname}
%package -n %{pkgname}
Summary: Open-source vector similarity search for Postgres
%else
%global pkgname %name
%endif

BuildRequires:	make gcc
BuildRequires:	postgresql%{pgversion}-server-devel
Requires:	postgresql%{pgversion}-server

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
Open-source vector similarity search for Postgres. Supports L2 distance,
inner product, and cosine distance

%description -n %{pkgname}
Open-source vector similarity search for Postgres. Supports L2 distance,
inner product, and cosine distance

%if %llvm
%package -n %{pkgname}-llvmjit
Summary:	Just-in-time compilation support for pgvector
Requires:	%{pkgname}%{?_isa} = %precise_version
Requires:	llvm => 13.0

%description -n %{pkgname}-llvmjit
This packages provides JIT support for pgvector
%endif

%prep
%setup -q -n %{sname}-%{version}

%build
%make_build %{?_smp_mflags} OPTFLAGS=""

%install
%make_install

#Remove header file, we don't need it right now:
%{__rm} %{buildroot}/%{_includedir}/pgsql/server/extension/%{pname}/%{pname}.h

%files -n %{pkgname}
%doc README.md
%license LICENSE
%{_libdir}/pgsql/%{pname}.so
%{_datadir}/pgsql/extension//%{pname}.control
%{_datadir}/pgsql/extension/%{pname}*sql
%if %llvm
%files -n %{pkgname}-llvmjit
%{_libdir}/pgsql/bitcode/%{pname}*.bc
%{_libdir}/pgsql/bitcode/%{pname}/src/*.bc
%endif

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jan 09 2025 Filip Janus <fjanus@redhat.com> - 0.6.2-3
- Portable build 
- Resolves: rhbz2329849

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Mar 25 2024 Filip Janus <fjanus@redhat.com> - 0.6.2-1
- Initial packaging

