# Force out of source build
%undefine __cmake_in_source_build

# base pkg default to SQLITE now, install -mysql if you want that instead
%global database_backend SQLITE

# trim changelog included in binary rpms
%global _changelog_trimtime %(date +%s -d "1 year ago")

Summary: PIM Storage Service Libraries
Name:    akonadi
Version: 1.13.0
Release: 128%{?dist}

License: LGPL-2.0-or-later
URL:     http://community.kde.org/KDE_PIM/Akonadi 
Source0: http://download.kde.org/stable/akonadi/src/akonadi-%{version}.tar.bz2

## downstream patches
Patch100: akonadi-1.13.0-libs_only.patch

## upstreamable patches

## upstream patches (1.13 branch)
Patch1: 0001-FindSqlite-Use-CMAKE_FLAGS-the-right-way-in-try_comp.patch
Patch2: 0002-Do-not-enter-the-test-directories-if-AKONADI_BUILD_T.patch
Patch3: 0003-STORE-Allow-modifying-items-tags-via-Tag-RID-or-GID.patch
Patch4: 0004-Fix-typo-in-if-condition.patch
Patch5: 0005-Fix-buffer-overflow-in-AKTEST_FAKESERVER_MAIN.patch
Patch6: 0006-Don-t-crash-when-setmntent-returns-NULL.patch
Patch7: 0007-Don-t-call-insert-from-Q_ASSERT-breaks-unit-tests-in.patch
Patch8: 0008-Suppress-unused-variable-warnings-in-release-mode.patch
Patch9: 0009-Test-whether-compiler-supports-all-required-C-11-fea.patch
Patch10: 0010-prevent-starting-a-QTimer-with-a-negative-interval.patch
Patch11: 0011-Convert-some-qDebugs-to-akDebugs.patch
Patch12: 0012-Optimize-Reduce-the-amount-of-allocations-required-t.patch
Patch13: 0013-Intern-entity-strings-for-table-and-column-names.patch
Patch14: 0014-No-semicolon-after-Q_DECLARE_METATYPE.patch
Patch15: 0015-Use-QMutexLocker-instead-of-manual-lock-unlock-calls.patch
Patch16: 0016-Use-an-QAtomicInt-instead-of-a-plain-bool-for-Entity.patch
Patch17: 0017-Optimize-Only-do-one-hash-lookup-to-retrieve-value-f.patch
Patch18: 0018-Optimize-Skip-value-condition-on-invalid-flags.patch
Patch19: 0019-Optimize-queries-Do-not-retrieve-known-key-used-in-t.patch
Patch20: 0020-Avoid-ridiculous-amount-of-SQL-queries-by-caching-Pa.patch
Patch21: 0021-Implement-support-for-CASE.WHEN.THEN-SQL-statements-.patch
Patch22: 0022-Implement-cache-for-CollectionStatistics-to-signific.patch
Patch23: 0023-Always-create-a-new-PartType-when-it-does-not-exist.patch
Patch24: 0024-Fix-compilation-with-strict-iterators.patch
Patch25: 0025-Avoid-repeated-calls-to-PimItem-flags-and-PimItem-ta.patch
Patch26: 0026-Avoid-recursive-collection-listing-in-SearchHelper.patch
Patch27: 0027-Minor-improvements-in-StatisticsCache-as-suggested-b.patch
Patch28: 0028-Extend-imapparser-benchmark-and-keep-static-data-aro.patch
Patch29: 0029-Reduce-the-amount-of-allocations-by-preallocating-a-.patch
Patch30: 0030-Preallocate-a-capacity-of-16-for-the-returned-list.patch

BuildRequires: automoc4
BuildRequires: boost-devel
BuildRequires: cmake >= 2.8.8
BuildRequires: gcc-c++
# for xsltproc
BuildRequires: libxslt
BuildRequires: pkgconfig(QtDBus) pkgconfig(QtSql) pkgconfig(QtXml)
BuildRequires: pkgconfig(shared-mime-info)

%description
%{summary}.

%package devel
Summary: Developer files for %{name}
Conflicts: kf5-akonadi-server-devel
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.


%prep
%autosetup -p1 -n akonadi-%{version}


%build
%cmake -DCMAKE_BUILD_TYPE:STRING="Release"
%cmake_build


%install
%cmake_install

## unpackaged files
rm -fv %{buildroot}%{_datadir}/mime/packages/akonadi-mime.xml


%check
export PKG_CONFIG_PATH=%{buildroot}%{_datadir}/pkgconfig:%{buildroot}%{_libdir}/pkgconfig
test "$(pkg-config --modversion akonadi)" = "%{version}"


%ldconfig_scriptlets

%files
%doc AUTHORS
%license lgpl-license
%{_libdir}/libakonadiprotocolinternals.so.1*

%files devel
%{_includedir}/akonadi/
%{_libdir}/pkgconfig/akonadi.pc
%{_libdir}/libakonadiprotocolinternals.so
%{_libdir}/cmake/Akonadi/
%{_datadir}/dbus-1/interfaces/org.freedesktop.Akonadi.*.xml


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-128
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-127
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-126
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-125
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-124
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 12 2023 Than Ngo <than@redhat.com> - 1.13.0-123
- migrated to SPDX license

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-122
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-121
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-120
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-119
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-118
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-117
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-116
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-115
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-114
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-113
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 1.13.0-112
- Rebuilt for Boost 1.69

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-111
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 20 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.13.0-110
- BR: gcc-c++, use %%ldconfig_scriptlets

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-109
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 1.13.0-108
- Rebuilt for Boost 1.66

* Sun Aug 06 2017 Björn Esser <besser82@fedoraproject.org> - 1.13.0-107
- Rebuilt for AutoReq cmake-filesystem

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-106
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-105
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 18 2017 Jonathan Wakely <jwakely@redhat.com> - 1.13.0-104
- Rebuilt for Boost 1.64

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-103
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-102
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 17 2015 Rex Dieter <rdieter@fedoraproject.org> 1.13.0-101
- -devel: re-enable dbus-1/interfaces, Conflicts: kf5-akonadi-server-devel

* Fri Dec 11 2015 Rex Dieter <rdieter@fedoraproject.org> 1.13.0-100
- for kf5 kdepim world, build libakonadi bits only (omit server and related files)

* Thu Nov 12 2015 Rex Dieter <rdieter@fedoraproject.org> 1.13.0-22
- Recommends: akonadi-mysql

* Sun Aug 30 2015 Jonathan Wakely <jwakely@redhat.com> 1.13.0-21
- Rebuilt for Boost 1.59

* Wed Aug 05 2015 Jonathan Wakely <jwakely@redhat.com> 1.13.0-20
- Rebuilt for Boost 1.58

* Fri Jul 31 2015 Rex Dieter <rdieter@fedoraproject.org> 1.13.0-19
- pull in latest 1.13 branch fixes

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13.0-18
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.13.0-17
- rebuild for Boost 1.58

* Mon Jun 29 2015 Daniel Vrátil <dvratil@redhat.com> - 1.13.0-16
- pull upstream fix for KDE#341884

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 07 2015 Rex Dieter <rdieter@fedoraproject.org> 1.13.0-14
- %%build: explicitly set -DCMAKE_BUILD_TYPE="Release" (-DQT_NO_DEBUG was used already)

* Mon Apr 27 2015 Daniel Vrátil <dvratil@redhat.com> - 1.13.0-13
- Rebuild for boost

* Sun Mar 08 2015 Rex Dieter <rdieter@fedoraproject.org> - 1.13.0-12
- explicit BuildRequires: mariadb-server
- -mysql: Recommends: mariadb-server (f21+, #1199797)

* Sun Mar 08 2015 Rex Dieter <rdieter@fedoraproject.org> 1.13.0-11
- explicitly Requires: mariadb(-sesrver) only as needed (#1199797)

* Wed Feb 18 2015 Rex Dieter <rdieter@fedoraproject.org> 1.13.0-10
- rebuild (gcc5)

* Wed Feb 04 2015 Petr Machata <pmachata@redhat.com> - 1.13.0-9
- Bump for rebuild.

* Sat Jan 31 2015 Rex Dieter <rdieter@fedoraproject.org> 1.13.0-8
- latest 1.13 branch fixes

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 1.13.0-7
- Rebuild for boost 1.57.0

* Thu Jan 08 2015 Rex Dieter <rdieter@fedoraproject.org> 1.13.0-6
- drop el6/cmake hacks

* Fri Oct 31 2014 Rex Dieter <rdieter@fedoraproject.org> 1.13.0-5
- latest 1.13 branch fixes

* Sat Sep 27 2014 Rex Dieter <rdieter@fedoraproject.org> 1.13.0-4
- explicitly Requires: mariadb-server/mysql-server as appropriate

* Mon Sep 15 2014 Rex Dieter <rdieter@fedoraproject.org> 1.13.0-3
- pull in some upstream fixes

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Aug 14 2014 Rex Dieter <rdieter@fedoraproject.org> 1.13.0-1
- 1.13.0

* Mon Aug 04 2014 Rex Dieter <rdieter@fedoraproject.org> 1.12.91-1
- 1.12.91

* Tue Jul 08 2014 Rex Dieter <rdieter@fedoraproject.org> 1.12.1-10
- scriptlet polish

* Thu Jul 03 2014 Rex Dieter <rdieter@fedoraproject.org> 1.12.1-9
- optimized mimeinfo scriptlet

* Mon Jun 09 2014 Rex Dieter <rdieter@fedoraproject.org> 1.12.1-8
- pull in latest 1.12 branch commits

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Petr Machata <pmachata@redhat.com> - 1.12.1-6
- Rebuild for boost 1.55.0

* Tue Apr 22 2014 Daniel Vrátil <dvratil@redhat.com> 1.12.1-5
- backport 1.12.2 patch to fix upgrade from Akonadi < 1.12 for users with invalid entries in DB

* Wed Apr 16 2014 Rex Dieter <rdieter@fedoraproject.org> 1.12.1-4
- backport master/ branch commits to test sqlite backend concurrency support

* Wed Apr 16 2014 Rex Dieter <rdieter@fedoraproject.org> 1.12.1-3
- WITH_SOPRANO=OFF (kde-4.13,fc21+)

* Tue Apr 15 2014 Rex Dieter <rdieter@fedoraproject.org> 1.12.1-2
- drop mysql-global-mobile.conf, it's too minimalistic
- drop Requires: qt4 >= 4.8.5-10 (workaround for psql driver bug had only a small window a long time ago)

* Tue Apr 08 2014 Rex Dieter <rdieter@fedoraproject.org> 1.12.1-1
- 1.12.1

* Wed Mar 26 2014 Rex Dieter <rdieter@fedoraproject.org> 1.12.0-1
- 1.12.0

* Wed Mar 19 2014 Daniel Vrátil <dvratil@redhat.com> 1.11.90-1
- 1.11.90

* Mon Mar 17 2014 Rex Dieter <rdieter@fedoraproject.org> 1.11.80-1
- 1.11.80

* Mon Feb 03 2014 Rex Dieter <rdieter@fedoraproject.org> 1.11.0-2
- rebuild

* Sat Nov 30 2013 Rex Dieter <rdieter@fedoraproject.org> 1.11.0-1
- 1.11.0

* Fri Nov 15 2013 Rex Dieter <rdieter@fedoraproject.org> 1.10.80-1
- 1.10.80

* Mon Oct 07 2013 Daniel Vrátil <dvratil@redhat.com> - 1.10.3-1
- 1.10.3

* Sun Jul 28 2013 Daniel Vrátil <dvratil@redhat.com> - 1.10.2-1
- 1.10.2

* Sat Jul 27 2013 pmachata@redhat.com - 1.10.1-2
- Rebuild for boost 1.54.0

* Thu Jul 25 2013 Rex Dieter <rdieter@fedoraproject.org> 1.10.1-1
- akonadi-1.10.1
- mysql_conf_timestamp 20130607

* Sat Jul 13 2013 Rex Dieter <rdieter@fedoraproject.org> 1.10.0-1
- 1.10.0

* Thu Jun 27 2013 Rex Dieter <rdieter@fedoraproject.org> 1.9.80-1
- 1.9.80

* Wed May 08 2013 Rex Dieter <rdieter@fedoraproject.org> 1.9.2-1
- 1.9.2

* Mon Mar 11 2013 Rex Dieter <rdieter@fedoraproject.org> 1.9.1-3
- revert hard-coding mariadb on f19+

* Sat Mar 02 2013 Rex Dieter <rdieter@fedoraproject.org> 1.9.1-1
- 1.9.1

* Mon Feb 11 2013 Rex Dieter <rdieter@fedoraproject.org> 1.9.0-5
- drop boost patch, qt/moc has workaround now

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.9.0-4
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.9.0-3
- Rebuild for Boost-1.53.0

* Fri Feb 08 2013 Rex Dieter <rdieter@fedoraproject.org> 1.9.0-2
- pull in a few upstream fixes

* Thu Jan 03 2013 Rex Dieter <rdieter@fedoraproject.org> 1.9.0-1
- 1.9.0

* Mon Dec 03 2012 Rex Dieter <rdieter@fedoraproject.org> 1.8.80-1
- 1.8.80

* Tue Oct 16 2012 Rex Dieter <rdieter@fedoraproject.org> 1.8.1-1
- 1.8.1

* Sat Oct 13 2012 Rex Dieter <rdieter@fedoraproject.org> 1.8.0-3
- include a couple upstream patches

* Mon Jul 30 2012 Rex Dieter <rdieter@fedoraproject.org> 1.8.0-2
- rebuild (boost)

* Thu Jul 26 2012 Rex Dieter <rdieter@fedoraproject.org> 1.8.0-1
- 1.8.0

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 25 2012 Rex Dieter <rdieter@fedoraproject.org> 1.7.90-2
- -mysql subpkg

* Mon Jun 25 2012 Rex Dieter <rdieter@fedoraproject.org> 1.7.90-1
- 1.7.90

* Sat Mar 31 2012 Rex Dieter <rdieter@fedoraproject.org> 1.7.2-1
- 1.7.2

* Thu Mar 15 2012 Rex Dieter <rdieter@fedoraproject.org> 1.7.1-2
- New cleanup in "akonadictl fsck"

* Tue Mar 06 2012 Rex Dieter <rdieter@fedoraproject.org> 1.7.1-1
- 1.7.1

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-2
- Rebuilt for c++ ABI breakage

* Tue Jan 24 2012 Rex Dieter <rdieter@fedoraproject.org> 1.7.0-1
- 1.7.0

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.90-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jan 11 2012 Rex Dieter <rdieter@fedoraproject.org> 1.6.90-3
- BR: +postgresql-server, -mysql-devel
- -devel: drop explicit BR: qt4-devel, pulled in via auto-pkgconfig deps

* Sat Dec 31 2011 Rex Dieter <rdieter@fedoraproject.org> 1.6.90-2
- %%check: try harder to make work in mock (using xvfb)
- default to sqlite on 'small' platforms (arm)

* Fri Dec 23 2011 Rex Dieter <rdieter@fedoraproject.org> 1.6.90-1
- 1.6.90

* Sun Nov 20 2011 Rex Dieter <rdieter@fedoraproject.org> 1.6.2-5
- rebuild (boost)

* Thu Oct 27 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> 1.6.2-4
- rebuild against fixed glibc headers in Rawhide

* Wed Oct 19 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> 1.6.2-3
- rebuild against fixed Qt headers in Rawhide

* Sat Oct 15 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> 1.6.2-2.1
- rebuild against known working Qt headers for F16 final

* Thu Oct 13 2011 Rex Dieter <rdieter@fedoraproject.org> 1.6.2-2
- switch back to mysql backend default
- pkgconfig-style deps
- own/ghost /etc/xdg/akonadi/akonadiserverrc

* Tue Oct 04 2011 Rex Dieter <rdieter@fedoraproject.org> 1.6.2-1
- 1.6.2

* Fri Sep 16 2011 Rex Dieter <rdieter@fedoraproject.org> 1.6.1-1
- 1.6.1

* Mon Aug 15 2011 Kalev Lember <kalevlember@gmail.com> 1.6.0-4
- Rebuilt for rpm bug #728707

* Thu Jul 21 2011 Rex Dieter <rdieter@fedoraproject.org> 1.6.0-3
- rebuild (boost)

* Wed Jul 13 2011 Rex Dieter <rdieter@fedoraproject.org> 1.6.0-2
- -DDATABASE_BACKEND=SQLITE 

* Tue Jul 12 2011 Rex Dieter <rdieter@fedoraproject.org> 1.6.0-1
- 1.6.0

* Wed Jun 29 2011 Rex Dieter <rdieter@fedoraproject.org> 1.5.80-2
- drop mysql_config patch, use -mobile.conf instead
- use database_backend macro more

* Thu Jun 02 2011 Jaroslav Reznik <jreznik@redhat.com> 1.5.80-1
- 1.5.80

* Sun May 15 2011 Rex Dieter <rdieter@fedoraproject.org> 1.5.3-1
- 1.5.3

* Tue Apr 05 2011 Rex Dieter <rdieter@fedoraproject.org> 1.5.2-1
- akonadi-1.5.2

* Mon Mar 14 2011 Rex Dieter <rdieter@fedoraproject.org> 1.5.1-1
- akonadi-1.5.1

* Tue Feb 15 2011 Rex Dieter <rdieter@fedoraproject.org> 1.5.0-4
- arch'ify qt4-mysql dep

* Fri Feb 11 2011 Rex Dieter <rdieter@fedoraproject.org> 1.5.0-3.1
- shrinky-dink db on f15 too

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Feb 06 2011 Rex Dieter <rdieter@fedoraproject.org> 1.5.0-2
- rebuild (boost)

* Sat Jan 22 2011 Rex Dieter <rdieter@fedoraproject.org> 1.5.0-1
- akonadi-1.5.0

* Fri Jan 07 2011 Rex Dieter <rdieter@fedoraproject.org> 1.4.95-1
- akonadi-1.4.95

* Fri Jan 07 2011 <rdieter@fedoraproject.org> - 1.4.90-2
- rebuild (mysql)
- %%check: make test should pass 100% now

* Tue Dec 21 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.4.90-1
- akonadi-1.4.90

* Sun Nov 21 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.4.80-1
- akonadi-1.4.80

* Sat Nov 20 2010 Rex Dieter <rdieter@fedoraproject.org> 1.4.54-1.20101120
- akonadi-1.4.54-20101120 snapshot

* Fri Oct 22 2010 Rex Dieter <rdieter@fedoraproject.org> 1.4.1-2
- patch out (paranoid) assert

* Fri Oct 22 2010 Rex Dieter <rdieter@fedoraproject.org> 1.4.1-1
- akonadi-1.4.1

* Tue Oct 19 2010 Rex Dieter <rdieter@fedoraproject.org> 1.4.0-3
- own %%_libdir/akonadi (#644540)

* Sat Oct 09 2010 Rex Dieter <rdieter@fedoraproject.org> 1.4.0-2
- apply mysql_conf patch only for < f15

* Sat Aug 07 2010 Rex Dieter <rdieter@fedoraproject.org> 1.4.0-1
- akonadi-1.4.0

* Thu Aug  5 2010 Tom "spot" Callaway <tcallawa@redhat.com> 1.3.90-3
- rebuild for boost again

* Tue Jul 27 2010 Rex Dieter <rdieter@fedoraproject.org> 1.3.90-2
- rebuild (boost)

* Thu Jul 15 2010 Rex Dieter <rdieter@fedoraproject.org> 1.3.90-1
- akonadi-1.3.90

* Wed Jun 09 2010 Rex Dieter <rdieter@fedoraproject.org> 1.3.85-1
- akonadi-1.3.85

* Wed May 26 2010 Rex Dieter <rdieter@fedoraproject.org> 1.3.80-1
- akonadi-1.3.80

* Sun May 23 2010 Rex Dieter <rdieter@fedoraproject.org> 1.3.60-1.20100523
- akonadi-1.3.60 (20100523 snapshot)

* Tue Mar 30 2010 Rex Dieter <rdieter@fedoraproject.org> 1.3.1-4
- fix typo on qt4 dep

* Tue Mar 30 2010 Rex Dieter <rdieter@fedoraproject.org> 1.3.1-3
- backport mysql_update patch (kde#232702)
- add (versioned) Requires: qt4 ...

* Wed Feb 10 2010 Rex Dieter <rdieter@fedoraproject.org> 1.3.1-2
- mysql_conf_timestamp 20100209 (ie, force a config resync)

* Tue Feb 09 2010 Rex Dieter <rdieter@fedoraproject.org> 1.3.1-1
- akonadi-1.3.1

* Wed Jan 20 2010 Rex Dieter <rdieter@fedoraproject.org> 1.3.0-1
- akonadi-1.3.0

* Tue Jan 19 2010 Rex Dieter <rdieter@fedoraproject.org> 1.2.90-3
- Client applications freeze because of hanging Nepomuk search job (kde#219687)

* Sat Jan 16 2010 Rex Dieter <rdieter@fedoraproject.org> 1.2.90-2
- rebuild (boost)

* Wed Jan 06 2010 Rex Dieter <rdieter@fedoraproject.org> 1.2.90-1
- akonadi-1.2.90

* Mon Dec 07 2009 Rex Dieter <rdieter@fedoraproject.org> 1.2.80-1
- Akonadi 1.2.80
- restore mysql deps

* Sat Nov 21 2009 Ben Boeckel <MathStuf@gmail.com> - 1.2.61-0.1.svn1052261
- Update to SVN snapshot of 1.2.61

* Tue Sep  1 2009 Lukáš Tinkl <ltinkl@redhat.com> - 1.2.1-1
- Akonadi 1.2.1

* Fri Aug 28 2009 Rex Dieter <rdieter@fedoraproject.org> 1.2.0-2.2
- temporarily drop mysql-related bits, to workaround broken rawhide deps

* Tue Aug 25 2009 Karsten Hopp <karsten@redhat.com> 1.2.0-2
- bump and rebuild, as s390x picked up an old boost library

* Thu Jul 30 2009 Lukáš Tinkl <ltinkl@redhat.com> - 1.2.0-1
- Akonadi 1.2.0

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.95-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jun 25 2009 Than Ngo <than@redhat.com> - 1.1.95-1
- 1.1.95

* Wed Jun 03 2009 Rex Dieter <rdieter@fedoraproject.org> 1.1.90-1
- akonadi-1.1.90

* Tue May 26 2009 Rex Dieter <rdieter@fedoraproject.org> 1.1.85-3
- akonadi.pc.cmake: s/AKONADI_LIB_VERSION_STRING/AKONADI_VERSION_STRING/

* Tue May 12 2009 Than Ngo <than@redhat.com> 1.1.85-2
- fix rpm file list

* Wed May 06 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.1.85-1
- akonadi-1.1.85

* Thu Apr 30 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.1.2-1
- akonadi-1.1.2
- optimize scriptlets a bit

* Wed Feb 25 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.1.1-6
- rev startup patch
- BR: cmake >= 2.6.0
- preserve timestamp's on mysql*.conf's

* Tue Feb 24 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.1.1-5
- own %%_sysconfig/akonadi/mysql-local.conf
- startup patch: reset conf only when needed, and clear mysql log file on update

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.1.1-3
- shrink default db initial size a bit (approx 140mb->28mb)
- drop extraneous RPATH-cmake baggage

* Wed Jan 21 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.1.1-1
- 1.1.1

* Sun Jan 04 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.1.0-1
- 1.1.0

* Tue Dec 16 2008 Rex Dieter <rdieter@fedoraproject.org> - 1.0.81-1
- 1.0.81

* Mon Dec 08 2008 Rex Dieter <rdieter@fedoraproject.org> - 1.0.80-3
- restore Requires: mysql-server

* Mon Dec 01 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.0.80-2
- own /usr/share/akonadi and /usr/share/akonadi/agents (#473595)

* Wed Nov 26 2008 Than Ngo <than@redhat.com> -  1.0.80-1
- 1.0.80

* Wed Oct 22 2008 Rex Dieter <rdieter@fedoraproject.org> 1.0.0-4
- drop Requires: mysql-server (for now), mention in %%description

* Wed Jul 30 2008 Rex Dieter <rdieter@fedoraproject.org> 1.0.0-3
- Requires: mysql-server

* Wed Jul 30 2008 Rex Dieter <rdieter@fedoraproject.org> 1.0.0-2
- BR: mysql-server
- Requires: qt4-mysql
- cleanup spec

* Wed Jul 23 2008 Than Ngo <than@redhat.com> -  1.0.0-1
- 1.0.0

* Wed Jun 18 2008 Rex Dieter <rdieter@fedoraproject.org> 0.82.0-1
- akonadi-0.82.0

* Tue Jun  3 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.81.0-0.2.20080526svn812787
- BR automoc, drop automoc hack

* Mon May 26 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.81.0-0.1.20080526svn812787
- update to revision 812787 from KDE SVN (to match KDE 4.1 Beta 1)
- restore builtin automoc4 for now
- update file list, require pkgconfig in -devel (.pc file now included)

* Mon May  5 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.80.0-2
- -devel: remove bogus Requires: pkgconfig

* Sat May  3 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.80.0-1
- first Fedora package
