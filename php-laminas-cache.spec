# remirepo/Fedora spec file for php-laminas-cache
#
# Copyright (c) 2015-2021 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without tests

# When buid without laminas-session
%global bootstrap    0
%global gh_commit    775cf8815cfd5a654f9b7b341ebaf28e72aa457d
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-cache
%global zf_name      zend-cache
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Cache

# Adapter tests
%global gh_test_commit            2a1f1606fbb57f4641aab5c93eb161606eafc4aa
%global gh_test_version           1.1.1
%global gh_test_short             %(c=%{gh_test_commit}; echo ${c:0:7})
# APC adapter
%global gh_apc_commit             8b375d994f6e67534f6ae6e995249e706faa30c1
%global gh_apc_version            1.0.1
%global gh_apc_short              %(c=%{gh_apc_commit}; echo ${c:0:7})
# APCu adapter
%global gh_apcu_commit            e182aab739d6b03992a9915cc3c7019391a94548
%global gh_apcu_version           1.1.0
%global gh_apcu_short             %(c=%{gh_apcu_commit}; echo ${c:0:7})
# Blackhole adapter
%global gh_blackhole_commit       4af1053efd81785a292c2a9442871c075700345a
%global gh_blackhole_version      1.2.1
%global gh_blackhole_short        %(c=%{gh_blackhole_commit}; echo ${c:0:7})
# Dba adapter
%global gh_dba_commit             ad968d3d8a0350af8e6717be58bb96e5a9e77f3b
%global gh_dba_version            1.0.1
%global gh_dba_short              %(c=%{gh_dba_commit}; echo ${c:0:7})
# ExtMongodb adapter
%global gh_ext_mongodb_commit     5810c3ffb442527b8b3429b0d29dce1ddabc92f2
%global gh_ext_mongodb_version    1.1.0
%global gh_ext_mongodb_short      %(c=%{gh_ext_mongodb_commit}; echo ${c:0:7})
# Filesystem adapter
%global gh_filesystem_commit      76fc488c3fa0ad442e4e70f807305c940d1bdcbc
%global gh_filesystem_version     1.1.1
%global gh_filesystem_short       %(c=%{gh_filesystem_commit}; echo ${c:0:7})
# Memcache adapter
%global gh_memcache_commit        1d2a74e300a0fd0b8d0e0cb4e379a173ccad0088
%global gh_memcache_version       1.1.0
%global gh_memcache_short         %(c=%{gh_memcache_commit}; echo ${c:0:7})
# Memcached adapter
%global gh_memcached_commit       f5d35cc2ef6264c76021bcc798569182103baa91
%global gh_memcached_version      1.1.0
%global gh_memcached_short        %(c=%{gh_memcached_commit}; echo ${c:0:7})
# Memory adapter
%global gh_memory_commit          02c7a4a1118bbd47d1c0f0bfe1e8b140af79d2bd
%global gh_memory_version         1.1.0
%global gh_memory_short           %(c=%{gh_memory_commit}; echo ${c:0:7})
# Mongodb adapter
%global gh_mongodb_commit         ef4aa396b55533b8eb3e1d4126c39a78a22e49a6
%global gh_mongodb_version        1.0.1
%global gh_mongodb_short          %(c=%{gh_mongodb_commit}; echo ${c:0:7})
# Redis adapter
%global gh_redis_commit           de8a63d4a0ef1ccead401eb7fb6d75b57fa3f9ee
%global gh_redis_version          1.2.0
%global gh_redis_short            %(c=%{gh_redis_commit}; echo ${c:0:7})
# Session adapter
%global gh_session_commit         74a275056cfca2300eb9a67cd1d917f7066b4113
%global gh_session_version        1.1.0
%global gh_session_short          %(c=%{gh_session_commit}; echo ${c:0:7})
# wincache adapter - Windows only
%global gh_wincache_commit        0f54599c5d9aff11b01adadd2742097f923170ba
%global gh_wincache_version       1.0.1
%global gh_wincache_short         %(c=%{gh_wincache_commit}; echo ${c:0:7})
# xcache adapter - PHP 5 only
%global gh_xcache_commit          24049557aa796ec7527bcc8032ed68346232b219
%global gh_xcache_version         1.0.1
%global gh_xcache_short           %(c=%{gh_xcache_commit}; echo ${c:0:7})
# zend-server adapter
%global gh_zend_server_commit     8d0b0d219a048a92472d89a5e527990f3ea2decc
%global gh_zend_server_version    1.0.1
%global gh_zend_server_short      %(c=%{gh_zend_server_commit}; echo ${c:0:7})


Name:           php-%{gh_project}
Version:        2.11.3
Release:        5%{?dist}
Summary:        %{namespace} Framework %{library} component

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
# Adapter tests
Source100:      %{name}-storage-adapter-test-%{gh_test_version}-%{gh_test_short}.tgz
# Adapters
Source101:      %{name}-storage-adapter-apc-%{gh_apc_version}-%{gh_apc_short}.tgz
Source102:      %{name}-storage-adapter-apcu-%{gh_apcu_version}-%{gh_apcu_short}.tgz
Source103:      %{name}-storage-adapter-blackhole-%{gh_blackhole_version}-%{gh_blackhole_short}.tgz
Source104:      %{name}-storage-adapter-dba-%{gh_dba_version}-%{gh_dba_short}.tgz
Source105:      %{name}-storage-adapter-ext-mongodb-%{gh_ext_mongodb_version}-%{gh_ext_mongodb_short}.tgz
Source106:      %{name}-storage-adapter-filesystem-%{gh_filesystem_version}-%{gh_filesystem_short}.tgz
Source107:      %{name}-storage-adapter-memcache-%{gh_memcache_version}-%{gh_memcache_short}.tgz
Source108:      %{name}-storage-adapter-memcached-%{gh_memcached_version}-%{gh_memcached_short}.tgz
Source109:      %{name}-storage-adapter-memory-%{gh_memory_version}-%{gh_memory_short}.tgz
Source110:      %{name}-storage-adapter-mongodb-%{gh_mongodb_version}-%{gh_mongodb_short}.tgz
Source111:      %{name}-storage-adapter-redis-%{gh_redis_version}-%{gh_redis_short}.tgz
Source112:      %{name}-storage-adapter-session-%{gh_session_version}-%{gh_session_short}.tgz
Source113:      %{name}-storage-adapter-wincache-%{gh_wincache_version}-%{gh_wincache_short}.tgz
Source114:      %{name}-storage-adapter-xcache-%{gh_xcache_version}-%{gh_xcache_short}.tgz
Source115:      %{name}-storage-adapter-zend-server-%{gh_zend_server_version}-%{gh_zend_server_short}.tgz

BuildArch:      noarch
# Tests
%if %{with tests}
BuildRequires:  php(language) >= 7.3
BuildRequires:  php-reflection
BuildRequires:  php-date
BuildRequires:  php-dba
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires: (php-autoloader(%{gh_owner}/laminas-eventmanager)         >= 3.3   with php-autoloader(%{gh_owner}/laminas-eventmanager)         < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.6   with php-autoloader(%{gh_owner}/laminas-servicemanager)       < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.3   with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0   with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
BuildRequires: (php-composer(psr/cache)                                  >= 1.0   with php-composer(psr/cache)                                  < 2)
BuildRequires: (php-composer(psr/simple-cache)                           >= 1.0   with php-composer(psr/simple-cache)                           < 2)
# From composer, "require-dev": {
#        "laminas/laminas-coding-standard": "~1.0.0",
#        "laminas/laminas-serializer": "^2.6",
#        "laminas/laminas-session": "^2.7.4",
#        "phpbench/phpbench": "^1.0.0-alpha8",
#        "phpspec/prophecy-phpunit": "^2.0",
#        "phpunit/phpunit": "^9.5"
# From laminas/laminas-cache-storage-adapter-test composer, "require": {
#        "cache/integration-tests": "^0.17",
#        "phpunit/phpunit": "^9.5"
BuildRequires: (php-composer(cache/integration-tests)                    >= 0.17  with php-composer(cache/integration-tests)                    < 1)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-serializer)           >= 2.6   with php-autoloader(%{gh_owner}/laminas-serializer)           < 3)
BuildRequires: (php-composer(phpspec/prophecy-phpunit)                   >= 2.0    with php-composer(phpspec/prophecy-phpunit)                   < 3)
%if ! %{bootstrap}
BuildRequires: (php-autoloader(%{gh_owner}/laminas-session)              >= 2.7.4 with php-autoloader(%{gh_owner}/laminas-session)              < 3)
%endif
%global phpunit %{_bindir}/phpunit9
BuildRequires:  phpunit9 >= 9.5
# Autoloader
BuildRequires:  php-fedora-autoloader-devel
%endif

# From composer, "require": {
#        "php": "^7.3 || ~8.0.0",
#        "laminas/laminas-eventmanager": "^3.3",
#        "laminas/laminas-servicemanager": "^3.6",
#        "laminas/laminas-stdlib": "^3.3",
#        "laminas/laminas-zendframework-bridge": "^1.0",
#        "psr/cache": "^1.0",
#        "psr/simple-cache": "^1.0"
Requires:       php(language) >= 5.6
Requires:      (php-autoloader(%{gh_owner}/laminas-eventmanager)         >= 3.3   with php-autoloader(%{gh_owner}/laminas-eventmanager)         < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.6   with php-autoloader(%{gh_owner}/laminas-servicemanager)       < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.3   with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0   with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
Requires:      (php-composer(psr/cache)                                  >= 1.0   with php-composer(psr/cache)                                  < 2)
Requires:      (php-composer(psr/simple-cache)                           >= 1.0   with php-composer(psr/simple-cache)                           < 2)
# From composer, "suggest": {
#        "laminas/laminas-serializer": "Laminas\\Serializer component"
Recommends:     php-composer(%{gh_owner}/laminas-serializer)
# From adapters
Recommends:     php-composer(%{gh_owner}/laminas-session)
Suggests:       php-apcu
Suggests:       php-dba
Suggests:       php-memcache
Suggests:       php-memcached
Suggests:       php-redis
Suggests:       php-composer(mongodb/mongodb)
# From phpcompatinfo report for version 2.9.0
Requires:       php-reflection
Requires:       php-date
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 2.9.1
Provides:       php-zendframework-%{zf_name}              = %{version}
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}
Provides:       php-composer(psr/cache-implementation)        = 1.0
Provides:       php-composer(psr/simple-cache-implementation) = 1.0
# Adapters
Provides:       php-composer(%{gh_owner}/laminas-cache-storage-adapter-apc)         = %{gh_apc_version}
Provides:       php-composer(%{gh_owner}/laminas-cache-storage-adapter-apcu)        = %{gh_apcu_version}
Provides:       php-composer(%{gh_owner}/laminas-cache-storage-adapter-blackhole)   = %{gh_blackhole_version}
Provides:       php-composer(%{gh_owner}/laminas-cache-storage-adapter-dba)         = %{gh_dba_version}
Provides:       php-composer(%{gh_owner}/laminas-cache-storage-adapter-ext-mongodb) = %{gh_ext_mongodb_version}
Provides:       php-composer(%{gh_owner}/laminas-cache-storage-adapter-filesystem)  = %{gh_filesystem_version}
Provides:       php-composer(%{gh_owner}/laminas-cache-storage-adapter-memcache)    = %{gh_memcache_version}
Provides:       php-composer(%{gh_owner}/laminas-cache-storage-adapter-memcached)   = %{gh_memcached_version}
Provides:       php-composer(%{gh_owner}/laminas-cache-storage-adapter-memory)      = %{gh_memory_version}
Provides:       php-composer(%{gh_owner}/laminas-cache-storage-adapter-mongodb)     = %{gh_mongodb_version}
Provides:       php-composer(%{gh_owner}/laminas-cache-storage-adapter-redis)       = %{gh_redis_version}
Provides:       php-composer(%{gh_owner}/laminas-cache-storage-adapter-session)     = %{gh_session_version}
Provides:       php-composer(%{gh_owner}/laminas-cache-storage-adapter-wincache)    = %{gh_wincache_version}
Provides:       php-composer(%{gh_owner}/laminas-cache-storage-adapter-xcache)      = %{gh_xcache_version}
Provides:       php-composer(%{gh_owner}/laminas-cache-storage-adapter-zend-server) = %{gh_zend_server_version}


%description
%{namespace}\Cache provides a general cache system for PHP.
The %{namespace}\Cache component is able to cache different patterns
(class, object, output, etc) using different storage adapters
(DB, File, Memcache, etc).

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit} -a100 -a101 -a102 -a103 -a104 -a105 -a106 -a107 -a108 -a109 -a110 -a111 -a112 -a113 -a114 -a115

mv LICENSE.md LICENSE

mv autoload/*.php src
for i in apc apcu blackhole dba ext-mongodb filesystem memcache memcached memory mongodb redis session wincache xcache zend-server
do
  pushd laminas-cache-storage-adapter-$i-*
    mv src/* ../src/Storage/Adapter
    [ -f CHANGELOG.md ] && mv CHANGELOG.md ../CHANGELOG-$i.md
    mv LICENSE.md ../LICENSE-$i
    mv composer.json ../composer-$i.json
    case $i in
       ext-mongodb|memcache|memcached|mongodb|redis)
         # skip test requiring a running server
         ;;
       dba|zend-server)
         # skip test no ready for PHPUnit 9
         ;;
%if %{bootstrap}
       session)
         ;;
%endif
       *)
         mv test  ../test/Storage/Adapter/$i
         ;;
    esac
  popd
done

mv laminas-cache-storage-adapter-test-*/src/* test/Storage/Adapter/


%build
: Create autoloader
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/Psr/Cache/autoload.php',
    '%{php_home}/Psr/SimpleCache/autoload.php',
    '%{php_home}/%{namespace}/Stdlib/autoload.php',
    '%{php_home}/%{namespace}/ServiceManager/autoload.php',
    '%{php_home}/%{namespace}/EventManager/autoload.php',
    __DIR__ . '/patternPluginManagerPolyfill.php',
]);
\Fedora\Autoloader\Dependencies::optional([
    '%{php_home}/%{namespace}/Serializer/autoload.php',
    '%{php_home}/%{namespace}/Session/autoload.php',
    '%{php_home}/MongoDB/autoload.php',
]);
EOF

cat << 'EOF' | tee zf.php
<?php
require_once '%{php_home}/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/ZendFrameworkBridge/autoload.php',
    dirname(dirname(__DIR__)) . '/%{namespace}/%{library}/autoload.php',
]);
EOF


%install
: Laminas library
mkdir -p   %{buildroot}%{php_home}/%{namespace}/
cp -pr src %{buildroot}%{php_home}/%{namespace}/%{library}

: Zend equiv
mkdir -p      %{buildroot}%{php_home}/Zend/%{library}
cp -pr zf.php %{buildroot}%{php_home}/Zend/%{library}/autoload.php


%check
%if %{with tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{php_home}/%{namespace}/%{library}/autoload.php';
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/Cache/IntegrationTests/autoload.php',
    '%{php_home}/Prophecy/PhpUnit/autoload.php',
]);
\Fedora\Autoloader\Autoload::addPsr4('%{namespace}Test\\%{library}\\', dirname(__DIR__) . '/test');
EOF

# Try to slowdown tests with erratic results
sed -e '/unlinkDelay/s/5000/50000/' \
    -e '/usleep/s/1000/10000/' \
    -i test/Storage/Adapter/filesystem/unit/FilesystemTest.php

# Fix for PHPUnit (some requires v7, some v9)
find test/ -type f \
  -exec sed \
      -e 's/function setUp()$/function setUp(): void/' \
      -e 's/function tearDown()$/function tearDown(): void/' \
      -i {} \;

: upstream test suite
ret=0
# TODO php80
for cmdarg in "php %{phpunit}" php73 php74 php80; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit9} || ret=1
  fi
done

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend/%{library}/autoload.php";
exit (class_exists("\\Zend\\%{library}\\StorageFactory") ? 0 : 1);
'

exit $ret
%else
: Test suite disabled
%endif


%files
%license LICENSE*
%doc *.md
%doc composer*.json
%{php_home}/Zend/%{library}
%{php_home}/%{namespace}/%{library}


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul  9 2021 Remi Collet <remi@remirepo.net> - 2.11.3-1
- update to 2.11.3 (no change)

* Fri Jun  4 2021 Remi Collet <remi@remirepo.net> - 2.11.2-1
- update to 2.11.2
- update laminas-cache-storage-adapter-redis to 1.2.0

* Fri May  7 2021 Remi Collet <remi@remirepo.net> - 2.11.1-1
- update laminas-cache-storage-adapter-ext-mongodb to 1.1.0

* Tue May  4 2021 Remi Collet <remi@remirepo.net> - 2.11.1-1
- update to 2.11.1
- update laminas-cache-storage-adapter-apcu to 1.1.0

* Mon May  3 2021 Remi Collet <remi@remirepo.net> - 2.11.0-2
- update laminas-cache-storage-adapter-blackhole to 1.2.1
- update laminas-cache-storage-adapter-memcache to 1.1.0

* Mon May  3 2021 Remi Collet <remi@remirepo.net> - 2.11.0-1
- update to 2.11.0
- update laminas-cache-storage-adapter-redis to 1.1.0
- update laminas-cache-storage-adapter-session to 1.1.0
- raise dependency on PHP 7.3
- raise dependency on laminas-eventmanager 3.3
- raise dependency on laminas-servicemanager 3.6
- raise dependency on laminas-stdlib 3.3
- switch to phpunit9

* Thu Apr 29 2021 Remi Collet <remi@remirepo.net> - 2.10.2-1
- update to 2.10.2
- update laminas-cache-storage-adapter-filesystem to 1.1.1
- update laminas-cache-storage-adapter-memcached to 1.1.0
- update laminas-cache-storage-adapter-memory to 1.1.0
- update laminas-cache-storage-adapter-test to 1.1.1

* Fri Feb 26 2021 Remi Collet <remi@remirepo.net> - 2.10.1-1
- update to 2.10.1
- update laminas-cache-storage-adapter-backhole to 1.1.1 (no change)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 2021 Remi Collet <remi@remirepo.net> - 2.10.0-2
- update laminas-cache-storage-adapter-filesystem to 1.1.0 (no change)

* Mon Nov  9 2020 Remi Collet <remi@remirepo.net> - 2.10.0-1
- update to 2.10.0
- bundle all cache storage adapters

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Remi Collet <remi@remirepo.net> - 2.9.0-2
- cleanup

* Wed Jan  8 2020 Remi Collet <remi@remirepo.net> - 2.9.0-1
- switch to Laminas
- boostrap build without laminas-session

* Fri Aug 30 2019 Remi Collet <remi@remirepo.net> - 2.9.0-1
- update to 2.9.0
- raise dependency on zend-stdlib 3.2.1

* Thu Aug 29 2019 Remi Collet <remi@remirepo.net> - 2.8.3-2
- update to 2.8.3

* Sun Nov 25 2018 Remi Collet <remi@remirepo.net> - 2.8.2-4
- fix autoloader for psr/cache and psr/simple-cache

* Wed May  2 2018 Remi Collet <remi@remirepo.net> - 2.8.2-2
- update to 2.8.2

* Thu Apr 26 2018 Remi Collet <remi@remirepo.net> - 2.8.1-2
- update to 2.8.1

* Thu Apr 26 2018 Remi Collet <remi@remirepo.net> - 2.8.0-4
- add optional dependency on mongodb/mongodb

* Thu Apr 26 2018 Remi Collet <remi@remirepo.net> - 2.8.0-2
- update to 2.8.0
- raise dependency on PHP 5.6
- add dependency on psr/cache
- add dependency on psr/simple-cache
- raise dependency on zend-eventmanager 3.2
- raise dependency on zend-servicemanager 3.3
- raise dependency on zend-stdlib 3.1
- use range dependencies (F27+)
- switch to phpunit6 or phpunit7

* Fri Nov 24 2017 Remi Collet <remi@remirepo.net> - 2.7.2-6
- switch from zend-loader to fedora/autoloader

* Tue Nov 14 2017 Remi Collet <remi@fedoraproject.org> - 2.7.2-5
- try to slowdown tests with erratic result (FTBFS)

* Tue Oct 31 2017 Remi Collet <remi@fedoraproject.org> - 2.7.2-4
- fix FTBFS from Koschei, add upstream patch for PHP 7.2

* Fri Dec 16 2016 Remi Collet <remi@fedoraproject.org> - 2.7.2-1
- update to 2.7.2

* Fri May 13 2016 Remi Collet <remi@fedoraproject.org> - 2.7.1-1
- update to 2.7.1

* Wed Apr 13 2016 Remi Collet <remi@fedoraproject.org> - 2.7.0-1
- update to 2.7.0

* Sat Feb 13 2016 Remi Collet <remi@fedoraproject.org> - 2.6.1-1
- update to 2.6.1

* Fri Feb 12 2016 Remi Collet <remi@fedoraproject.org> - 2.6.0-1
- update to 2.6.0
- raise dependency on zend-stdlib >= 2.7
- raise dependency on zend-servicemanager >= 2.7.5
- raise dependency on zend-eventmanager >= 2.6.2

* Wed Sep 16 2015 Remi Collet <remi@fedoraproject.org> - 2.5.3-1
- update to 2.5.3
- zend-serializer is    optional

* Thu Aug  6 2015 Remi Collet <remi@fedoraproject.org> - 2.5.2-2
- add missing obsoletes

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.2-1
- initial package
