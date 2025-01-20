%{!?postgresql_default:%global postgresql_default 1}

%global majorname pgaudit
%global pgversion 16
Name:		postgresql%{pgversion}-%{majorname}
Version:	16.0
Release:	7%{?dist}
Summary:	PostgreSQL Audit Extension

License:	PostgreSQL
URL:		http://pgaudit.org

Source0:	https://github.com/%{majorname}/%{majorname}/archive/%{version}/%{majorname}-%{version}.tar.gz

%if %?postgresql_default
%global pkgname %{majorname}
%package -n %{pkgname}
Summary: PostgreSQL Audit Extension
%else
%global pkgname %name
%endif

BuildRequires: make
BuildRequires:	gcc
BuildRequires:	postgresql-server-devel >= 16, postgresql-server-devel < 17
BuildRequires:	openssl-devel

Requires(pre): postgresql-server >= 16, postgresql-server < 17

%global precise_version %{?epoch:%epoch:}%version-%release
Provides: %{pkgname} = %precise_version
%if %?postgresql_default
Provides: %name = %precise_version
Provides: postgresql-%{majorname} = %precise_version
%endif
Provides: %{pkgname}%{?_isa} = %precise_version
Provides: %{majorname}-any
Conflicts: %{majorname}-any

%description
The PostgreSQL Audit extension (pgaudit) provides detailed session
and/or object audit logging via the standard PostgreSQL logging
facility.

The goal of the PostgreSQL Audit extension (pgaudit) is to provide
PostgreSQL users with capability to produce audit logs often required to
comply with government, financial, or ISO certifications.

An audit is an official inspection of an individual's or organization's
accounts, typically by an independent body. The information gathered by
the PostgreSQL Audit extension (pgaudit) is properly called an audit
trail or audit log. The term audit log is used in this documentation.

%description -n %{pkgname}
The PostgreSQL Audit extension (pgaudit) provides detailed session
and/or object audit logging via the standard PostgreSQL logging
facility.

The goal of the PostgreSQL Audit extension (pgaudit) is to provide
PostgreSQL users with capability to produce audit logs often required to
comply with government, financial, or ISO certifications.

An audit is an official inspection of an individual's or organization's
accounts, typically by an independent body. The information gathered by
the PostgreSQL Audit extension (pgaudit) is properly called an audit
trail or audit log. The term audit log is used in this documentation.

%prep
%setup -q -n %{majorname}-%{version}


%build
%make_build USE_PGXS=1 PG_CONFIG=/usr/bin/pg_server_config


%install
%make_install USE_PGXS=1 PG_CONFIG=/usr/bin/pg_server_config


%files -n %{pkgname}
%doc README.md
%license LICENSE
%{_libdir}/pgsql/%{majorname}.so
%if 0%{?postgresql_server_llvmjit}
%{_libdir}/pgsql/bitcode/%{majorname}.index.bc
%{_libdir}/pgsql/bitcode/%{majorname}/%{majorname}.bc
%endif
%{_datadir}/pgsql/extension/%{majorname}--1*.sql
%{_datadir}/pgsql/extension/%{majorname}.control


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 16.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 16 2024 Filip Janus <fjanus@redhat.com> - 16.0-6
- Add provide postgresqlVERSION-pgaudit

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 16.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 16.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 11 2023 Filip Janus <fjanus@redhat.com> - 16.0-2
- Add macro postgresql_default to be able set up default version in distro
- Add symbop pgaudit-any

* Tue Nov 28 2023 Filip Janus <fjanus@redhat.com> - 16.0-1
- Update to 16.0

* Tue Nov 28 2023 Filip Janus <fjanus@redhat.com> - 1.7.0-6
- Initial import of demodularized version

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 16 2022 Ondřej Sloup <osloup@redhat.com> - 1.7.0-3
- Rebuild for new PostgreSQL 15

* Mon Oct 17 2022 Ondrej Sloup <osloup@redhat.com> - 1.7.0-2
- Allow PostgreSQL server 15 build requirement

* Wed Oct 12 2022 Ondrej Sloup <osloup@redhat.com> - 1.7.0-1
- Add pgaudit sql 1.7 removed 1.6.2 and 1.6.1-1.6.2
- Rebase to the latest upstream version

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 10 2022 Ondrej Sloup <osloup@redhat.com> - 1.6.2-1
- Add pgaudit sql 1.6.2 and 1.6.1-1.6.2, removed 1.6.1
- Rebase to the latest upstream version

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 06 2022 Filip Januš <fjanus@redhat.com> - 1.6.1-2
- Update to postgresql 14

* Wed Jan 05 2022 Filip Januš <fjanus@redhat.com> - 1.6.1-1
- Update to v1.6.1

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Apr 16 2021 Honza Horak <hhorak@redhat.com> - 1.5.0-3
- Make llvmjit features optional, follow what is enabled in postgresql

* Mon Feb 08 2021 Pavel Raiskup <praiskup@redhat.com> - 1.5.0-2
- rebuild for libpq ABI fix rhbz#1908268

* Fri Feb  5 2021 Honza Horak <hhorak@redhat.com> - 1.5.0-1
- Update to 1.5.0 for PostgreSQL 13 support

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Mar 13 2020 Devrim Gündüz <devrim@gunduz.org> - 1.4.0-1
- Update to 1.4.0 for PostgreSQL 12 support

* Sun Mar 08 2020 Patrik Novotný <panovotn@redhat.com> - 1.3.0-5
- Rebuild for PostgreSQL 12

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 18 2018 Petr Kubat <pkubat@redhat.com> - 1.3.0-1
- rebase to latest upstream release

* Wed Sep 05 2018 Pavel Raiskup <praiskup@redhat.com> - 1.2.0-4
- rebuild against postgresql-server-devel (rhbz#1618698)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 20 2017 - Filip Čáp <ficap@redhat.com> 1.2.0-1
- Initial RPM packaging for Fedora
- Based on Devrim Gündüz's packaging for PostgreSQL RPM Repo

* Thu Oct 27 2016 - Devrim Gündüz <devrim@gunduz.org> 1.0.0-1
- Update to 1.0.0

* Fri Oct 21 2016 - Devrim Gündüz <devrim@gunduz.org> 0.0.4-1
- Initial RPM packaging for PostgreSQL RPM Repository
