%global	sname	ip4r

Summary:	IPv4/v6 type and IPv4/v6 range index type for PostgreSQL
Name:		postgresql-%{sname}
Version:	2.4.2
Release:	6%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
# Note that the URL is generated, needs to be changed.
Source0:	https://github.com/RhodiumToad/%sname/archive/%version/%name-%version.tar.gz
URL:		https://github.com/RhodiumToad/ip4r


BuildRequires: make
BuildRequires:	gcc
BuildRequires:	clang-devel llvm-devel
BuildRequires:	postgresql-server-devel

Requires(pre): postgresql-server

%description
ip4, ip4r, ip6, ip6r, ipaddress and iprange are types that contain a single
IPv4/IPv6 address and a range of IPv4/IPv6 addresses respectively. They can
be used as a more flexible, indexable version of the cidr type.

%prep
%autosetup -n %{sname}-%{version} -p1


%build
%make_build PG_CONFIG=%_bindir/pg_server_config


%install
%make_install PG_CONFIG=%_bindir/pg_server_config
%{__rm} %{buildroot}/usr/share/doc/pgsql/extension/README.ip4r

# Package into *-devel once it is requested, more info:
# https://github.com/RhodiumToad/ip4r/pull/13
%{__rm} -r %{buildroot}%{_includedir}/pgsql


%files
%doc README.ip4r
%{_datadir}/pgsql/extension/*
%{_libdir}/pgsql/%{sname}.so
%if 0%{?postgresql_server_llvmjit}
%{_libdir}/pgsql/bitcode/%{sname}*.bc
%{_libdir}/pgsql/bitcode/%{sname}/src/*.bc
%endif

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 2.4.2-5
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Dec 05 2023 Filip Janus <fjanus@redhat.com> - 2.4.2-1
- Update to 2.4.2

* Tue Dec 05 2023 Filip Janus <fjanus@redhat.com> - 2.4.1-15
- disable postgresql_module_compat macro

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 16 2022 Ondřej Sloup <osloup@redhat.com> - 2.4.1-12
- Rebuild for new PostgreSQL 15

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 06 2022 Filip Januš <fjanus@redhat.com> - 2.4.1.-9
- Rebuild for Postgresql 14

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Feb 08 2021 Pavel Raiskup <praiskup@redhat.com> - 2.4.1-7
- rebuild for libpq ABI fix

* Fri Jan 15 2021 Patrik Novotný <panovotn@redhat.com> - 2.4.1-6
- Add compatibilty for llvm enabled postgresql

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar 12 2020 Honza Horak <hhorak@redhat.com> - 2.4.1-4
- Add precompiled files into files section

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 2019 Devrim Gündüz <devrim@gunduz.org> - 2.4.1-1
- Update to 2.4.1
- Update description

* Fri Feb 01 2019 Pavel Raiskup <praiskup@redhat.com> - 2.4-1
- the latest upstream release

* Mon Oct 22 2018 Pavel Raiskup <praiskup@redhat.com> - 2.3-1
- rebuild against PostgreSQL 11
- update to new upstream release (rhbz#1641664)

* Wed Sep 05 2018 Pavel Raiskup <praiskup@redhat.com> - 2.0.2-18
- rebuild against postgresql-server-devel (rhbz#1618698)

* Mon Jul 23 2018 Pavel Raiskup <praiskup@redhat.com> - 2.0.2-17
- fix ftbfs (rhbz#1605493)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct 07 2017 Pavel Raiskup <praiskup@redhat.com> - 2.0.2-15
- rebuild for PostgreSQL 10

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 10 2016 Pavel Raiskup <praiskup@redhat.com> - 2.0.2-11
- bump: build in rawhide done too early

* Wed Oct 05 2016 Pavel Raiskup <praiskup@redhat.com> - 2.0.2-10
- rebuild for postgresql 9.6.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 08 2016 Pavel Kajaba <pkajaba@redhat.com> - 2.0.2-8
- Rebuild for PostgreSQL 9.5 (rhbz#1296584)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jan 06 2015 Jozef Mlich <jmlich@redhat.com> - 2.0.2-6
- rebuild because of broken dependency
  requires postgresql-server(:MODULE_COMPAT_9.3)

* Sun Aug 24 2014 Pavel Raiskup <praiskup@redhat.com> - 2.0.2-5
- rebuild as previously the %%postgresql_major was not expanded correctly

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 18 2014 Pavel Raiskup <praiskup@redhat.com> - 2.0.2-2
- make the package dependant on postgresql-server(:MODULE_COMPAT_*) (#1008939)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Pavel Raiskup <praiskup@redhat.com> - 2.0.2-1
- new upstream release

* Wed Sep 18 2013 Pavel Raiskup <praiskup@redhat.com> - 2.0-1
- rebase to the newest upstream version (#1009468)
- fix fedora-review complaints

* Wed Sep 18 2013 Pavel Raiskup <praiskup@redhat.com> - 1.05-8
- Rebuild against PostgreSQL 9.3

* Mon Aug 12 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.05-7
- Use special %%doc to install docs (#994049).

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.05-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.05-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.05-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 19 2010 Devrim GÜNDÜZ <devrim@gunduz.org> - 1.05-1
- Update to 1.05.

* Mon Jul 19 2010 Devrim GÜNDÜZ <devrim@gunduz.org> - 1.03-5
- Rebuilt against PostgreSQL 8.4. Fixes	bz #615715.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec  4 2008 Michael Schwendt <mschwendt@fedoraproject.org> 1.03-2
- Include unowned doc directory.

* Fri Feb 1 2008 - Devrim GUNDUZ <devrim@commandprompt.com> 1.03-1
- Update to 1.03

* Sun Jan 20 2008 - Devrim GUNDUZ <devrim@commandprompt.com> 1.02-1
- Update to 1.02

* Mon Jul 9 2007 - Devrim GUNDUZ <devrim@commandprompt.com> 1.01-2
- Removed unneeded ldconfig calls, per bz review #246747

* Wed Jul 4 2007 - Devrim GUNDUZ <devrim@commandprompt.com> 1.01-1
- Initial RPM packaging for Fedora
