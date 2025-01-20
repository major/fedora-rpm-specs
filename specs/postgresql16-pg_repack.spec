%{!?postgresql_default:%global postgresql_default 1}

%global majorname pg_repack
%global pgversion 16
Name:           postgresql%{pgversion}-%{majorname}
Version:        1.4.8
Release:        10%{?dist}
Summary:        Reorganize tables in PostgreSQL databases without any locks

License:        BSD-3-Clause
URL:            http://reorg.github.io/%{majorname}/
Source0:        https://github.com/reorg/%{majorname}/archive/ver_%{version}.tar.gz

%if %?postgresql_default
%global pkgname %{majorname}
%package -n %{pkgname}
Summary: Reorganize tables in PostgreSQL databases without any locks
%else
%global pkgname %name
%endif

BuildRequires: make
BuildRequires:  gcc, openssl-devel, lz4-devel
BuildRequires:  postgresql-server-devel >= 16, postgresql-server-devel < 17
BuildRequires:  postgresql-server >= 16, postgresql-server < 17
BuildRequires:  postgresql-static >= 16, postgresql-static < 17
BuildRequires:  readline-devel, zlib-devel
BuildRequires:  python3-docutils
Requires(pre): postgresql-server >= 16, postgresql-server < 17

%global precise_version %{?epoch:%epoch:}%version-%release
Provides: %{pkgname} = %precise_version
%if %?postgresql_default
Provides: postgresql-%{majorname} = %precise_version
Provides: %name = %precise_version
%endif
Provides: %{pkgname}%{?_isa} = %precise_version
Provides: %{majorname}-any
Conflicts: %{majorname}-any

%description
pg_repack is a PostgreSQL extension which lets you remove
bloat from tables and indexes, and optionally
restore the physical order of clustered indexes.
Unlike CLUSTER and VACUUM FULL it works online,
without holding an exclusive lock on the processed tables during processing.
pg_repack is efficient to boot,
with performance comparable to using CLUSTER directly.

Please check the documentation (in the doc directory or online)
for installation and usage instructions.

%description -n %{pkgname}
pg_repack is a PostgreSQL extension which lets you remove
bloat from tables and indexes, and optionally
restore the physical order of clustered indexes.
Unlike CLUSTER and VACUUM FULL it works online,
without holding an exclusive lock on the processed tables during processing.
pg_repack is efficient to boot,
with performance comparable to using CLUSTER directly.

Please check the documentation (in the doc directory or online)
for installation and usage instructions.

%prep
%setup -n %{majorname}-ver_%{version} -q


%build

make %{?_smp_mflags}
cd doc
make


%install
%make_install

%files -n %{pkgname}
%{_bindir}/%{majorname}
%{_libdir}/pgsql/%{majorname}.so
%if 0%{?postgresql_server_llvmjit}
%{_libdir}/pgsql/bitcode/%{majorname}.index.bc
%{_libdir}/pgsql/bitcode/%{majorname}/pgut/pgut-spi.bc
%{_libdir}/pgsql/bitcode/%{majorname}/repack.bc
%endif
%{_datadir}/pgsql/extension/%{majorname}.control
%{_datadir}/pgsql/extension/%{majorname}--%{version}.sql

%license COPYRIGHT

%doc README.rst
%doc doc/%{majorname}.html
%doc doc/%{majorname}.rst
%doc doc/%{majorname}_jp.html
%doc doc/%{majorname}_jp.rst
%doc doc/release.html
%doc doc/release.rst


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 16 2024 Filip Janus <fjanus@redhat.com> - 1.4.8-9
- Add provide postgresqlVERSION-pg_repack

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Dec 06 2023 Filip Janus <fjanus@redhat.com> - 1.4.8-5
- Add postgresql_default macro to be able to decide which version of extension
  is the default one in the repository

* Mon Apr 24 2023 Filip Januš <fjanus@redhat.com> - 1.4.8-4
- Build without modules

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 16 2022 Ondřej Sloup <osloup@redhat.com> - 1.4.8-2
- Rebuild for new PostgreSQL 15

* Tue Oct 25 2022 Ondrej Sloup <osloup@redhat.com> - 1.4.8-1
-  Rebase to the latest upstream version
-  PostgreSQL 15 support

* Wed Aug 3 2022 Filip Janus <fjanus@redhat.com> - 1.4.7-3
- add lz4-devel

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Mar 16 2022 Filip Janus <fjanus@redhat.com> - 1.4.7-1
- Update to 1.4.7

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 06 2022 Filip Januš <fjanus@redhat.com> - 1.4.6-5
- Rebuild for Postgresql 14

* Fri Jul 30 2021 Filip Januš <fjanus@redhat.com> - 1.4.6-4
- Remove requirements after postgresql architecture
  change(usage of private libpq)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Apr 22 2021 Honza Horak <hhorak@redhat.com> - 1.4.6-2
- Build jit based on what postgresql server does

* Thu Jan 28 2021 Patrik Novotný <panovotn@redhat.com> - 1.4.6-1
- Rebase to upstream release 1.4.6

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Aug 21 2019 Filip Januš <fjanus@redhat.com> 1.4.5-1
- Initial packaging
