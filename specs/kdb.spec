%undefine __cmake_in_source_build
# koffice version to Obsolete
%global koffice_ver 3:2.3.70

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
# some known failures, ping upstream
%global tests 1
%endif

Name:    kdb
Summary: Database Connectivity and Creation Framework
Version: 3.2.0
Release: 22%{?dist}

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+

Url:     https://community.kde.org/KDb
Source0: http://download.kde.org/stable/%{name}/src/%{name}-%{version}.tar.xz

## upstream patches
Patch1: 0001-cmake-find-PostgreSQL-12.patch
Patch2: 0002-PgSQL-driver-fix-build-with-PostgreSQL-12.patch
Patch3: 0003-Autotests-Fix-QCOMPARE-for-QString-const-char-and-QB.patch
Patch4: 0004-TRIVIAL-Move-Q_REQUIRED_RESULT-to-correct-place.patch
Patch7: 0007-Take-all-args-to-kdbfeaturestest-before-the-driver.patch
Patch8: 0008-Expand-feature-test-for-buffered-cursors.patch
Patch9: 0009-Escape-table-name-in-when-building-a-select-statemen.patch
Patch10: 0010-Improve-a-bit-parse-error-diagnosis.patch
Patch12: 0012-Update-README.md-add-github-note-and-donation.patch
Patch13: 0013-cmake-find-PostgreSQL-13.patch
Patch17: 0017-Find-also-Python3-with-find_package-PythonInterp.patch
Patch20: 0020-Fix-build-with-newer-Qt.patch
Patch22: 0022-cmake-find-PostgreSQL-14.patch
Patch30: 0030-Fix-build-with-GCC-12-standard-attributes-in-middle-.patch

## upstreamable patches
# fix/santitize KDb3.pc dependencies
Patch100: kdb-3.2.0-pkgconfig.patch
# https://invent.kde.org/libraries/kdb/-/merge_requests/11
Patch1001: 1001-gcc-12-inline.patch

BuildRequires: gcc-c++

BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros
BuildRequires: cmake(KF5CoreAddons)

BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Xml)

BuildRequires: libicu-devel
BuildRequires: python3

# drivers
%if (0%{?rhel} && 0%{?rhel} < 8 )
BuildRequires: mariadb-devel
%else
BuildRequires: mariadb-connector-c-devel
%endif
# postgresql-private-devel introduced in f35+ with pgsql-13.4 and Conflicts: libpq-devel
%if 0%{?fedora} > 34 || 0%{?rhel} > 8
BuildRequires: postgresql-private-devel >= 13.4
%else
BuildRequires: libpq-devel
%endif
# this shouldn't be needed, but the build system configuration seems to
# mistakenly detect server-related headers
BuildRequires: postgresql-server-devel
BuildRequires: pkgconfig(sqlite3)

# autodeps
BuildRequires: cmake
BuildRequires: pkgconfig

%if 0%{?tests}
BuildRequires: cmake(Qt5Test)
%endif

Obsoletes: calligra-kexi-driver-sybase < 3.0.0
Obsoletes: calligra-kexi-driver-xbase < 3.0.0

%description
A database connectivity and creation framework for various database vendors.


%package devel
Summary: Developer files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: cmake(KF5CoreAddons)
%description devel
%{summary}.

%package  driver-mysql
Summary:  Mysql driver for %{name}
Obsoletes: koffice-kexi-driver-mysql < %{koffice_ver}
Obsoletes: calligra-kexi-driver-mysql < 3.0.0
Provides:  calligra-kexi-driver-mysql = %{version}-%{release}
Requires: %{name} = %{version}-%{release}
Supplements: (%{name} and mariadb-server)
%description driver-mysql
%{summary}.

%package  driver-postgresql
Summary:  Postgresql driver for %{name}
Obsoletes: koffice-kexi-driver-pgsql < %{koffice_ver}
Obsoletes: calligra-kexi-driver-pgsql < 2.3.86-2
Provides:  calligra-kexi-driver-pgsql = %{version}-%{release}
Obsoletes: calligra-kexi-driver-postgresql < 3.0.0
Provides:  calligra-kexi-driver-postgresql = %{version}-%{release}
Requires: %{name} = %{version}-%{release}
Supplements: (%{name} and postgresql-server)
%description driver-postgresql
%{summary}.


%prep
%autosetup -p1


%build
%cmake_kf5 \
  -Wno-dev \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{?!tests:OFF} \
  -DPYTHON_EXECUTABLE:PATH="%{__python3}"

%cmake_build


%install
%cmake_install

%find_lang_kf5 kdb_qt
%find_lang_kf5 kdb_mysqldriver_qt
%find_lang_kf5 kdb_postgresqldriver_qt
%find_lang_kf5 kdb_sqlitedriver_qt
cat kdb_sqlitedriver_qt.lang >> kdb_qt.lang


%check
## tests have known failures, TODO: consult upstream
## assumes cmake files are installed on system (not buildroot)
#The following tests FAILED:
#         11 - HeadersTest (Failed)
%if 0%{?tests}
%ctest ||:
%endif


%ldconfig_scriptlets

%files -f kdb_qt.lang
%license COPYING.LIB
%{_libdir}/libKDb3.so.4*
%{_bindir}/kdb3_sqlite3_dump
%dir %{_qt5_plugindir}/kdb3/
# sqlite driver included in base (for now)
%{_qt5_plugindir}/kdb3/kdb_sqlitedriver.so
%{_qt5_plugindir}/kdb3/sqlite3/

%files driver-mysql -f kdb_mysqldriver_qt.lang
%{_qt5_plugindir}/kdb3/kdb_mysqldriver.so

%files driver-postgresql -f kdb_postgresqldriver_qt.lang
%{_qt5_plugindir}/kdb3/kdb_postgresqldriver.so

%files devel
%{_includedir}/KDb3/
%{_libdir}/libKDb3.so
%{_libdir}/cmake/KDb3/
%{_libdir}/pkgconfig/KDb3.pc
%{_kf5_archdatadir}/mkspecs/modules/qt_KDb3.pri


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 3.2.0-21
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Feb 02 2024 Pete Walter <pwalter@fedoraproject.org> - 3.2.0-19
- Fix FTBFS (rhbz#2261270)

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 František Zatloukal <fzatlouk@redhat.com> - 3.2.0-15
- Rebuilt for ICU 73.2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 31 2022 Pete Walter <pwalter@fedoraproject.org> - 3.2.0-13
- Rebuild for ICU 72

* Wed Nov 16 2022 Ondřej Sloup <osloup@redhat.com> - 3.2.0-12
- Rebuild for new PostgreSQL 15

* Mon Aug 01 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 3.2.0-11
- Rebuilt for ICU 71.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 06 2022 Filip Januš <fjanus@redhat.com> - 3.2.0-8
- Rebuild for Postgresql 14

* Wed Sep 15 2021 Filip Januš <fjanus@redhat.com> - 3.2.0-7
- replace libpq-devel by postgresql-private-devel

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 20 2021 Pete Walter <pwalter@fedoraproject.org> - 3.2.0-5
- Rebuild for ICU 69

* Mon Feb 08 2021 Pavel Raiskup <praiskup@redhat.com> - 3.2.0-4
- rebuild for libpq ABI fix rhbz#1908268

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Rex Dieter <rdieter@fedoraproject.org> - 3.2.0-1
- 3.2.0

* Mon Jun 22 2020 Rex Dieter <rdieter@fedoraproject.org> - 3.1.0-12
- BR: python3

* Fri Jan 31 2020 Petr Viktorin <pviktori@redhat.com> - 3.1.0-11
- Require the Python interpreter directly

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 01 2019 Pete Walter <pwalter@fedoraproject.org> - 3.1.0-9
- Rebuild for ICU 65

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Pete Walter <pwalter@fedoraproject.org> - 3.1.0-6
- Rebuild for ICU 63

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 3.1.0-4
- Rebuild for ICU 62

* Mon Apr 30 2018 Pete Walter <pwalter@fedoraproject.org> - 3.1.0-3
- Rebuild for ICU 61.1

* Thu Mar 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.1.0-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sun Mar 11 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.1.0-1
- 3.1.0
- use Supplements for -driver subpkgs

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.94-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.0.94-1
- 3.0.94

* Thu Nov 30 2017 Pete Walter <pwalter@fedoraproject.org> - 3.0.2-4
- Rebuild for ICU 60.1

* Tue Oct 10 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.2-3
- use mariadb-connector-c-devel on f28+ (#1494227)

* Fri Aug 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.2-2
- fix/santize pkgconfig deps

* Fri Aug 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.2-1
- 3.0.2 (includes translations)

* Mon Aug 07 2017 Björn Esser <besser82@fedoraproject.org> - 3.0.1-5
- Rebuilt for AutoReq cmake-filesystem

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.1-2
- rebuild (mariadb)

* Wed Apr 12 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.1-0.1
- first try
