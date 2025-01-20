%if 0%{?fedora}
%global pg_config PG_CONFIG=%_bindir/pg_server_config
%else
%global pg_config PG_CONFIG=%_bindir/pg_config
%endif

Name:		pg-semver
Version:	0.32.1
Release:	6%{?dist}
Summary:	A semantic version data type for PostgreSQL
License:	PostgreSQL
Url:		https://github.com/theory/pg-semver
Source0:	http://api.pgxn.org/dist/semver/%{version}/semver-%{version}.zip
BuildRequires:	clang
BuildRequires:	gcc
BuildRequires:	llvm
BuildRequires:	make
BuildRequires:	postgresql-server-devel
Requires(pre):	postgresql-server

%description
PostgreSQL server extension implementing data type called "semver".
It's an implementation of the version number format specified by the
Semantic Versioning Specification.

%prep
%autosetup -n semver-%{version}

%build
%make_build CFLAGS="%{optflags}" %pg_config

%install
%make_install CFLAGS="%{optflags}" %pg_config

# remove misplaced documentation file, added via doc
rm -f %{buildroot}%{_docdir}/pgsql/contrib/semver.mmd
rm -f %{buildroot}%{_docdir}/pgsql/extension/semver.mmd


%files
%doc LICENSE README.md doc/semver.mmd
%{_libdir}/pgsql/semver.so
%{_datadir}/pgsql/extension/semver*.sql
%{_datadir}/pgsql/extension/semver.control

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.32.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.32.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.32.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.32.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 11 2023 Ondrej Sloup <osloup@redhat.com> - 0.32.1-2
- Remove macro %%{?postgresql_module_requires}

* Mon Dec 11 2023 Ondrej Sloup <osloup@redhat.com> - 0.32.1-1
- Rebase to the latest upstream version

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 07 2022 Pavel Raiskup <praiskup@redhat.com> - 0.31.0-9
- rebuild for the new PostgreSQL 15

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 06 2022 Filip Januš <fjanus@redhat.com> - 0.31.0-6
- Update to postgresql 14

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Feb 08 2021 Pavel Raiskup <praiskup@redhat.com> - 0.31.0-4
- rebuild for libpq ABI fix rhbz#1908268

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec  1 13:15:24 CET 2020 msuchy <msuchy@redhat.com> - 0.31.0-2
- BR make

* Sun Nov 1 2020 Martin Kutlak <mkfedora@fedoraproject.org> - 0.31.0-1
- Update to 0.31.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.30.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 15 2020 Ernestas Kulik <ekulik@redhat.com> - 0.30.0-2
- Patch extension control file to fix the default version

* Tue May 19 2020 Ernestas Kulik <ekulik@redhat.com> - 0.30.0-1
- Update to 0.30.0

* Tue May 19 2020 Ernestas Kulik <ekulik@redhat.com> - 0.22.0-1
- Update to 0.22.0

* Sun Mar 22 2020 Ernestas Kulik <ekulik@redhat.com> - 0.21.0-1
- Update to 0.21.0
- Change %%setup to %%autosetup
- Update outdated Fedora version checks

* Thu Feb 20 2020 Martin Kutlak <mkutlak@redhat.com> - 0.20.3-5
- Rebuilt against PostgreSQL 12
- spec: Fix missing BR for build with PSQL12
- spec: Fix unpackaged bitcode files

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 18 2019 Pavel Raiskup <praiskup@redhat.com> - 0.20.3-1
- new upstream version (rhbz#1639261)

* Wed Oct 17 2018 Pavel Raiskup <praiskup@redhat.com> - 0.5.0-15
- rebuild against PostgreSQL 11

* Wed Sep 05 2018 Pavel Raiskup <praiskup@redhat.com> - 0.5.0-14
- rebuild against postgresql-server-devel (rhbz#1618698)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 10 2017 Pavel Raiskup <praiskup@redhat.com> - 0.5.0-11
- rebuild for PostgreSQL 10

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 10 2016 Pavel Raiskup <praiskup@redhat.com> - 0.5.0-7
- bump: build in rawhide done too early

* Mon Oct 10 2016 Petr Kubat <pkubat@redhat.com> - 0.5.0-6
- Rebuild for PostgreSQL 9.6.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 08 2016 Pavel Kajaba <pkajaba@redhat.com> - 0.5.0-4
- Rebuild for PostgreSQL 9.5 (rhbz#1296584)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 05 2015 Richard Marko <rmarko@fedoraproject.org> - 0.5.0-2
- Fix issues found by review

* Tue Dec 09 2014 Richard Marko <rmarko@fedoraproject.org> - 0.5.0-1
- Initial packaging.
