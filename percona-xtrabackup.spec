%global pxbu_major_minor 80

%define _lto_cflags %{nil}

Summary: Online backup for InnoDB/XtraDB in MySQL, Percona Server and MariaDB
Name: percona-xtrabackup
Version: 8.0.29_22
Release: 1%{?dist}
License: GPLv2 and Boost and MIT and Python
URL: http://www.percona.com/software/percona-xtrabackup/
# Real name is 8.0.29-22 ...
Source: https://github.com/percona/%{name}/archive/refs/tags/%{name}-8.0.29_22.tar.gz
# This is bad - we should use the system boost-devel package!
Source1: boost_1_77_0.tar.bz2
# Note the extras/ directory contains a whole lot of bundles libraries
#      that are statically linked :(
Provides: xtrabackup >= 2.0.0
Provides: %{name}-%{pxbu_major_minor}
Obsoletes: xtrabackup < 2.0.0
BuildRequires: libaio-devel
BuildRequires: libgcrypt-devel
BuildRequires: automake
BuildRequires: cmake >= 2.6.3
BuildRequires: patch
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: libtool
BuildRequires: make
BuildRequires: bison
BuildRequires: ncurses-devel
# upstream does not yet support openssl 3.0
BuildRequires: openssl1.1-devel
BuildRequires: perl-generators
BuildRequires: procps
BuildRequires: python3-sphinx
BuildRequires: python3-devel
BuildRequires: libcurl-devel
BuildRequires: libev-devel
BuildRequires: vim-common
BuildRequires: /usr/bin/pathfix.py
Requires: perl(DBD::mysql)
Requires: libcurl
Requires: libev

%description
Online backup for InnoDB/XtraDB in MySQL, MariaDB and Percona Server.

%package test
Summary: Test suite for Percona Xtrabackup
Provides: %{name}-test-%{pxbu_major_minor}
Requires: %{name}
Requires: /usr/bin/mysql
Requires: %{name}%{?_isa} = %{version}-%{release}

%description test
This package contains the test suite for Percona Xtrabackup

%prep
%setup -qn %{name}-8.0.29-22
mkdir -p %{_build}/../libboost
cp %SOURCE1 %{_build}/../libboost/
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" . ./storage/innobase/xtrabackup/test/subunit2junitxml

%build
%cmake -DWITH_BOOST=libboost -DBUILD_CONFIG=xtrabackup_release \
  -DCMAKE_INSTALL_PREFIX=%{_prefix} -DWITH_SSL=system -DINSTALL_MANDIR=%{_mandir} -DWITH_MAN_PAGES=1 \
  -DINSTALL_MYSQLTESTDIR=%{_datadir}/percona-xtrabackup-test-%{pxbu_major_minor} \
  -DINSTALL_PLUGINDIR="%{_lib}/xtrabackup/plugin" -DFORCE_INSOURCE_BUILD=1

%cmake_build

%install
%cmake_install
rm -rf %{buildroot}/usr/docs/INFO_SRC
rm -rf %{buildroot}/usr/lib/private/libprotobuf*
rm -rf %{buildroot}/usr/lib/libmysqlservices.a
rm -rf %{buildroot}/%{_libdir}/libmysqlservices.a
rm -rf %{buildroot}/%{_mandir}/man8
rm -rf %{buildroot}/%{_mandir}/man1/c*
rm -rf %{buildroot}/%{_mandir}/man1/m*
rm -rf %{buildroot}/%{_mandir}/man1/i*
rm -rf %{buildroot}/%{_mandir}/man1/l*
rm -rf %{buildroot}/%{_mandir}/man1/p*
rm -rf %{buildroot}/%{_mandir}/man1/z*
rm -rf %{buildroot}/%{_libdir}/private
rm -rf %{buildroot}/%{_libdir}/debug/usr/lib64/xtrabackup/plugin
rm -rf %{buildroot}/usr/lib/private/icudt69l/
rm -rf %{buildroot}/usr/include/*kmip*
rm -rf %{buildroot}/usr/lib/*kmip*.a

%files
%{_bindir}/xtrabackup
%{_bindir}/xbstream
%{_bindir}/xbcrypt
%{_bindir}/xbcloud
%{_bindir}/xbcloud_osenv
%doc README.md XB_VERSION
%license LICENSE
%{_mandir}/man1/xtrabackup.1.gz
%{_mandir}/man1/xbstream.1.gz
%{_mandir}/man1/xbcrypt.1.gz
%{_libdir}/xtrabackup/plugin/keyring_file.so
%{_libdir}/xtrabackup/plugin/keyring_vault.so
%{_libdir}/xtrabackup/plugin/component_keyring_file.so
%{_libdir}/xtrabackup/plugin/component_keyring_kmip.so
%{_libdir}/xtrabackup/plugin/component_keyring_kms.so

%files -n percona-xtrabackup-test
%{_datadir}/percona-xtrabackup-test-%{pxbu_major_minor}

%changelog
* Mon Aug 22 2022 Paul Wouters <pwouters@redhat.com> - 8.0.29_22-1
- Update to 8.0.29-22
- Resolves: rhbz#1989019 F35FailsToInstall: percona-xtrabackup, percona-xtrabackup-test
- Build using openssl-1, upstrema does not support openssl 3.0 yet.
- Update builtin booster version to required version (this is bad, should use system boost-devel)
- Cleanup newly added and installed libkmip devel files

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.25_17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.25_17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 8.0.25_17-2
- Rebuilt with OpenSSL 3.0.0

* Sat Jul 31 2021 Sven Lankes <sven@lank.es> - 8.0.25_17-1
- rebase to latest upstream release

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 13 2020 Sven Lankes <sven@lank.es> - 8.0.14-1
- Rebase to new upstream release

* Thu Oct 01 2020 Petr Pisar <ppisar@redhat.com> - 2.3.6-21
- Adapt to new CMake macros (bug #1865206)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-20
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Mar 06 2020 Peter MacKinnon <pmackinn@redhat.com> - 2.3.6-18
- Fixes #1799854

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Carl George <carl@george.computer> - 2.3.6-16
- Remove dependency on python2 rhbz#1738052

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Peter MacKinnon <pmackinn@redhat.com> - 2.3.6-14
- Fixes #1730231

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 2.3.6-12
- Rebuilt for libcrypt.so.2 (#1666033)

* Fri Jan 04 2019 Björn Esser <besser82@fedoraproject.org> - 2.3.6-11
- Add patch to use explicit shebangs, fixes FTBFS for Fedora 30
- Add patch to fix -fpermissive, fixes FTBFS for Fedora 30
- Apply proper buildflags
- Modernize spec-file

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.3.6-9
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 2.3.6-7
- Rebuilt for switch to libxcrypt

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 17 2017 Peter MacKinnon <pmackinn@redhat.com> - 2.3.6-3
- Adjustments for GCC 7

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 18 2017 Peter MacKinnon <pmackinn@redhat.com> - 2.3.6-1
- Updated to 2.3.6
- Fixes CVE-2016-6225

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 3 2015 Peter MacKinnon <pmackinn@redhat.com> - 2.2.9-3
- Add an extra provides for version 2.2

* Tue Sep 1 2015 Peter MacKinnon <pmackinn@redhat.com> - 2.2.9-2
- Spec changes from Fedora review

* Fri Jun 12 2015 Peter MacKinnon <pmackinn@redhat.com> - 2.2.9-1
- Updated to 2.2.9 (mariadb 5.5 compatible)

* Thu Oct 31 2013 Stewart Smith <stewart@flamingspork.com> - 2.1.5-1
- Update packaging for Percona XtraBackup 2.1.5 release

* Mon Sep 27 2010 Aleksandr Kuzminsky
- Version 1.4

* Wed Jun 30 2010 Aleksandr Kuzminsky
- Version 1.3 ported on Percona Server 11

* Thu Mar 11 2010 Aleksandr Kuzminsky
- Ported to MySQL 5.1 with InnoDB plugin

* Fri Mar 13 2009 Vadim Tkachenko
- initial release
