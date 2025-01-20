Summary: Spherical data types, functions, and operators for PostgreSQL
Name: pgsphere
Version: 1.4.1
Release: 6%{?dist}
License: BSD-3-Clause

Source0: https://github.com/postgrespro/%{name}/archive/refs/tags/%{version}.tar.gz
URL: https://github.com/postgrespro/pgsphere/

BuildRequires: make
BuildRequires: gcc
BuildRequires: postgresql-server-devel
BuildRequires: clang-devel
BuildRequires: llvm-devel
BuildRequires: healpix-c++-devel
BuildRequires: zlib-devel
Requires(pre):	postgresql-server

%description
pgSphere is a server side module for PostgreSQL. It contains methods for 
working with spherical coordinates and objects. It also supports indexing of 
spherical objects.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%make_build 

%install
%make_install

%files
%doc %{_datadir}/doc/pgsql/extension/README.pg_sphere
%license %{_datadir}/doc/pgsql/extension/COPYRIGHT.pg_sphere
%{_libdir}/pgsql/pg_sphere*
%{_datadir}/pgsql/extension/pg_sphere*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 11 2023 Ondrej Sloup <osloup@redhat.com> - 1.4.1-2
- Remove macro %%{?postgresql_module_requires}

* Mon Dec 11 2023 Ondrej Sloup <osloup@redhat.com> - 1.4.1-1
- Rebase to the latest upstream version
- Change upstream to https://github.com/postgrespro/pgsphere/
- Update license to SPDX format (BSD-3-Clause)
- Remove merged patches

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 16 2022 Ondřej Sloup <osloup@redhat.com> - 1.1.1-36
- Rebuild for new PostgreSQL 15

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 06 2022 Filip Januš <fjanus@redhat.com> - 1.1.1-33
- Rebuild for Postgresql 14

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 14 2021 Patrik Novotný <panovotn@redhat.com> - 1.1.1-31
- Add compatibility for llvm enabled postgresql

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar 18 2020 Sergio Pascual <sergiopr at fedoraproject.org> 1.1.1-28
- Rebuild for PostgreSQL 12 (rhbz#1813525)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 18 2018 Petr Kubat <pkubat@redhat.com> - 1.1.1-24
- rebuild for PostgreSQL 11

* Wed Sep 05 2018 Pavel Raiskup <praiskup@redhat.com> - 1.1.1-23
- rebuild against postgresql-server-devel (rhbz#1618698)

* Tue Jul 17 2018 Christian Dersch <lupinix@fedoraproject.org> - 1.1.1-22
- BuildRequires: gcc

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct 07 2017 Pavel Raiskup <praiskup@redhat.com> - 1.1.1-19
- rebuild for PostgreSQL 10

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 10 2016 Pavel Raiskup <praiskup@redhat.com> - 1.1.1-15
- bump: build in rawhide done too early

* Mon Oct 10 2016 Petr Kubat <pkubat@redhat.com> - 1.1.1-14
- Rebuild for PostgreSQL 9.6.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 08 2016 Pavel Kajaba <pkajaba@redhat.com> - 1.1.1-12
- Rebuild for PostgreSQL 9.5 (rhbz#1296584)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 12 2015 Pavel Raiskup <praiskup@redhat.com> - 1.1.1-10
- rebuild for PostgreSQL 9.4

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Sep 18 2013 Sergio Pascual <sergiopr at fedoraproject.org> 1.1.1-7
- Patch to build with psql 9.3

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jun 30 2011 Sergio Pascual <sergiopr at fedoraproject.org> 1.1.1-2
- Fix source url
- Directory in datadir included

* Tue Jan 11 2011 Sergio Pascual <sergiopr at fedoraproject.org> 1.1.1-1
- Initial spec file
