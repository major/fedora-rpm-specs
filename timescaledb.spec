%global core_name timescale

Name:           %{core_name}db
Version:        2.10.1
Release:        1%{?dist}
Summary:        Open-source time-series database powered by PostgreSQL

License:        ASL 2.0
URL:            http://www.%{core_name}.com
Source0:        https://github.com/%{core_name}/%{name}/archive/refs/tags/%{version}.tar.gz

%if 0%{?fedora} >= 30 || 0%{?epel} >= 8
BuildRequires:  cmake gcc openssl-devel postgresql-server-devel
%else
BuildRequires:  cmake gcc openssl-devel postgresql-devel
%endif

%{?postgresql_module_requires}

%description
TimescaleDB is an open-source database designed to make SQL scalable for
time-series data.  It is engineered up from PostgreSQL, providing automatic
partitioning across time and space (partitioning key), as well as full SQL
support.


%prep
%autosetup -n %{name}-%{version}
# Remove tsl directory containing sources licensed under Timescale license
rm -rf tsl


%build
%if 0%{?fedora} >= 30 || 0%{?epel} >= 8
%cmake -DPROJECT_INSTALL_METHOD=fedora -DREGRESS_CHECKS=OFF -DAPACHE_ONLY=1 -DPG_CONFIG=%_bindir/pg_server_config
%else
%cmake -DPROJECT_INSTALL_METHOD=fedora -DREGRESS_CHECKS=OFF -DAPACHE_ONLY=1 -DPG_CONFIG=%_bindir/pg_config
%endif
%cmake_build


%install
%cmake_install


%files
%license LICENSE-APACHE
%doc README.md
%{_libdir}/pgsql/%{name}-%{version}.so
%{_libdir}/pgsql/%{name}.so
%{_datadir}/pgsql/extension/%{name}--*%{version}.sql
%{_datadir}/pgsql/extension/%{name}.control


%changelog
* Fri Mar 17 2023 Ondrej Sloup <osloup@redhat.com> -  2.10.1-1
- Rebase to the latest upstream version (rhbz#2178347)

* Sun Feb 26 2023 Ondrej Sloup <osloup@redhat.com> -  2.10.0-1
- Rebase to the latest upstream version (rhbz#2167977)

* Fri Feb 10 2023 Ondrej Sloup <osloup@redhat.com> -  2.9.3-1
- Rebase to the latest upstream version (rhbz#771255)

* Fri Jan 27 2023 Ondrej Sloup <osloup@redhat.com> -  2.9.2-1
- Rebase to the latest upstream version (rhbz#2164282)

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Ondrej Sloup <osloup@redhat.com> - 2.9.1-1
- Rebase to the latest upstream version (rhbz#2156187)

* Fri Dec 23 2022 Ondrej Sloup <osloup@redhat.com> - 2.9.0-1
- Rebase to the latest upstream version (rhbz#2155326)

* Wed Nov 16 2022 Ondřej Sloup <osloup@redhat.com> - 2.8.1-2
- Rebuild for new PostgreSQL 15

* Thu Sep 01 2022 Ondrej Sloup <osloup@redhat.com> - 2.8.0-1
- Rebase to the latest upstream version (rhbz#2123172)

* Tue Jul 26 2022 Ondrej Sloup <osloup@redhat.com> - 2.7.2-1
- Rebase to the latest upstream version (rhbz#2110891)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 1 2022 Ondrej Sloup <osloup@redhat.com> - 2.7.0-1
- Use autosetup
- Change source links to Github
- Rebase to the latest upstream version (rhbz#1989589)

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 06 2022 Filip Januš <fjanus@redhat.com> - 2.5.1-2
- Update to postgresql 14

* Mon Jan 03 2022 Filip Januš <fjanus@redhat.com> - 2.5.1-1
- Update to 2.5.1 - add support for Postgresql 14

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 2.3.1-4
- Rebuilt with OpenSSL 3.0.0

* Mon Jul 26 2021 Filip Januš <fjanus@redhat.com> - 2.3.1-3
- Remove libpq-devel requirement - postgresql-server-devel uses
  postgresql-private-devel instead of libpq-devel

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 09 2021 Patrik Novotný <panovotn@redhat.com> - 2.3.1-1
- Rebase to upstream release 2.3.1

* Wed Jun 09 2021 Patrik Novotný <panovotn@redhat.com> - 2.3.0-1
- Rebase to upstream release 2.3.0

* Wed Apr 14 2021 Patrik Novotný <panovotn@redhat.com> - 2.1.1-1
- Rebase to upstream release 2.1.1

* Tue Feb 23 2021 Patrik Novotný <panovotn@redhat.com> - 2.1.0-1
- Rebase to upstream release 2.1.0
- Adds PostgreSQL 13 support

* Mon Feb 08 2021 Pavel Raiskup <praiskup@redhat.com> - 1.7.4-3
- rebuild for libpq ABI fix rhbz#1908268

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 15 2020 Patrik Novotný <panovotn@redhat.com> - 1.7.4-1
- Rebase to upstream release 1.7.4

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Patrik Novotný <panovotn@redhat.com> - 1.7.1-1
- New upstream release 1.7.1

* Fri Apr 17 2020 Patrik Novotný <panovotn@redhat.com> - 1.7.0-1
- New upstream release 1.7.0

* Tue Mar 24 2020 Patrik Novotný <panovotn@redhat.com> - 1.6.1-2
- New upstream release 1.6.1

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 25 2019 Patrik Novotný <panovotn@redhat.com> - 1.5.1-1
- New upstream release 1.5.1

* Fri Nov 01 2019 Patrik Novotný <panovotn@redhat.com> - 1.5.0-1
- New upstream release 1.5.0

* Fri Sep 13 2019 Patrik Novotný <panovotn@redhat.com> - 1.4.2-1
- New upstream release 1.4.2

* Tue Aug 20 2019 Patrik Novotný <panovotn@redhat.com> - 1.4.1-1
- New upstream release: 1.4.1

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 03 2019 Patrik Novotný <panovotn@redhat.com> - 1.3.2-1
- New upstream release: 1.3.2

* Wed Jun 12 2019 Patrik Novotný <panovotn@redhat.com> - 1.3.1-1
- New upstream release: 1.3.1

* Tue May 07 2019 Patrik Novotný <panovotn@redhat.com> - 1.3.0-1
- New upstream version: 1.3.0

* Tue Mar 26 2019 Patrik Novotný <panovotn@redhat.com> - 1.2.2-2
- Add PROJECT_INSTALL_METHOD build flag for upstream telemetry

* Thu Mar 21 2019 Patrik Novotný <panovotn@redhat.com> - 1.2.2-1
- Rebase to usptream version 1.2.2

* Thu Jan 31 2019 Patrik Novotný <panovotn@redhat.com> - 1.2.0-1
- Update to upstream release 1.2.0

* Thu Jan 03 2019 Patrik Novotný <panovotn@redhat.com> - 1.1.0
- Update to upstream release 1.1.0

* Wed Sep 19 2018 panovotn@redhat.com - 0.12.0-1
- Upstream update to 0.12.0

* Wed Sep 05 2018 praiskup@redhat.com - 0.11.0-2
- rebuild against postgresql-server-devel (rhbz#1618698)

* Thu Aug  9 2018 Patrik Novotný <panovotn@redhat.com> - 0.11.0-1
- An upstream update to 0.11.0

* Tue Aug  7 2018 Patrik Novotný <panovotn@redhat.com> - 0.10.1-1
- Initial build
