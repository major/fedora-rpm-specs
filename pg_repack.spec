Name:           pg_repack
Version:        1.4.8
Release:        4%{?dist}
Summary:        Reorganize tables in PostgreSQL databases without any locks

License:        BSD-3-Clause
URL:            http://reorg.github.io/%{name}/
Source0:        https://github.com/reorg/%{name}/archive/ver_%{version}.tar.gz

BuildRequires: make
BuildRequires:  postgresql, gcc, openssl-devel, postgresql-server
BuildRequires:  postgresql-server-devel, lz4-devel
BuildRequires:  readline-devel, zlib-devel, postgresql-static
BuildRequires:  python3-docutils
%{?postgresql_module_requires}

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
%prep
%setup -n %{name}-ver_%{version} -q


%build

make %{?_smp_mflags}
cd doc
make


%install
%make_install

%files
%{_bindir}/%{name}
%{_libdir}/pgsql/%{name}.so
%if 0%{?postgresql_server_llvmjit}
%{_libdir}/pgsql/bitcode/%{name}.index.bc
%{_libdir}/pgsql/bitcode/%{name}/pgut/pgut-spi.bc
%{_libdir}/pgsql/bitcode/%{name}/repack.bc
%endif
%{_datadir}/pgsql/extension/%{name}.control
%{_datadir}/pgsql/extension/%{name}--%{version}.sql

%license COPYRIGHT

%doc README.rst
%doc doc/%{name}.html
%doc doc/%{name}.rst
%doc doc/%{name}_jp.html
%doc doc/%{name}_jp.rst
%doc doc/release.html
%doc doc/release.rst


%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

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
