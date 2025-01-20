#
# Fedora spec file for php-doctrine-cache
#
# Copyright (c) 2013-2021 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     doctrine
%global github_name      cache
%global github_version   1.13.0
%global github_commit    56cd022adb5514472cb144c087393c1821911d09

%global composer_vendor  doctrine
%global composer_project cache

# "cache/integration-tests": "dev-master",
%global cache_integration_tests_min_ver 0.17

# "symfony/cache": "^4.4 || ^5.4 || ^6",
# "symfony/var-exporter": "^4.4 || ^5.4 || ^6"
%global symfony_min_ver 4.4
%global symfony_max_ver 7

# "psr/cache": "^1.0 || ^2.0 || ^3.0"
%global psr_cache_min_ver 1.0
%global psr_cache_max_ver 4

# "php": "~7.1 || ^8.0"
%global php_min_ver 7.1

# Build using "--without tests" to disable tests
%bcond_without   tests

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       8%{?dist}
Summary:       Doctrine Cache

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests.
# Run php-doctrine-cache-get-source.sh to create full source.
Source0:       %{name}-%{version}-%{github_commit}.tar.gz
Source9:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: phpunit9 >= 9.5
## phpcompatinfo (computed from version 1.7.1)
BuildRequires: php-date
BuildRequires: php-hash
BuildRequires: php-pecl(igbinary)
BuildRequires: php-reflection
BuildRequires: php-spl
BuildRequires: php-sqlite3
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
BuildRequires:(php-composer(symfony/cache)        >= %{symfony_min_ver}      with php-composer(symfony/cache)        < %{symfony_max_ver})
BuildRequires:(php-composer(symfony/var-exporter) >= %{symfony_min_ver}      with php-composer(symfony/var-exporter) < %{symfony_max_ver})
BuildRequires:(php-composer(psr/cache)            >= %{psr_cache_min_ver}    with php-composer(psr/cache)            < %{psr_cache_max_ver})
BuildRequires: php-composer(cache/integration-tests) >= %{cache_integration_tests_min_ver}
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 1.7.1)
Requires:      php-date
Requires:      php-hash
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)
# Weak dependencies
%if 0%{?fedora} > 21 || 0%{?rhel} >= 8
Suggests:      php-composer(alcaeus/mongo-php-adapter)
Suggests:      php-composer(mongodb/mongodb)
Suggests:      php-composer(predis/predis)
Suggests:      php-pecl(apcu)
Suggests:      php-pecl(igbinary)
Suggests:      php-pecl(memcache)
Suggests:      php-pecl(memcached)
Suggests:      php-pecl(mongo)
Suggests:      php-pecl(redis)
%endif

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

# Extracted from Doctrine Common as of version 2.4
Conflicts:     php-pear(pear.doctrine-project.org/DoctrineCommon) < 2.4

%description
Cache component extracted from the Doctrine Common project.

Autoloader: %{phpdir}/Doctrine/Common/Cache/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}

: Remove files that will never be used
find . -name '*WinCache*' -delete
find . -name '*ZendDataCache*' -delete

: Create autoloader
cat <<'AUTOLOAD' | tee lib/Doctrine/Common/Cache/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Doctrine\\Common\\Cache\\', __DIR__);
\Fedora\Autoloader\Dependencies::optional([
    '/usr/share/php/Alcaeus/MongoDbAdapter/autoload.php',
    '/usr/share/php/MongoDB/autoload.php',
    '/usr/share/pear/Predis/Autoloader.php',
]);
if (class_exists("Predis\\Autoloader")) {
	Predis\Autoloader::register();
}
AUTOLOAD


%build
# Empty build section, nothing required


%install
mkdir -p %{buildroot}%{phpdir}/Doctrine/Common
cp -rp lib/Doctrine/Common/Cache %{buildroot}%{phpdir}/Doctrine/Common/


%check
%if %{with tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require_once '%{buildroot}%{phpdir}/Doctrine/Common/Cache/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Doctrine\\Tests\\', __DIR__.'/tests/Doctrine/Tests');
\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/Cache/IntegrationTests/autoload.php',
    [
        '%{phpdir}/Psr/Cache3/autoload.php',
        '%{phpdir}/Psr/Cache2/autoload.php',
        '%{phpdir}/Psr/Cache/autoload.php',
    ], [
        '%{phpdir}/Symfony6/Component/Cache/autoload.php',
        '%{phpdir}/Symfony5/Component/Cache/autoload.php',
        '%{phpdir}/Symfony4/Component/Cache/autoload.php',
    ], [
        '%{phpdir}/Symfony6/Component/VarExporter/autoload.php',
        '%{phpdir}/Symfony5/Component/VarExporter/autoload.php',
        '%{phpdir}/Symfony4/Component/VarExporter/autoload.php',
	],
]);
BOOTSTRAP

: Skip tests known to fail
rm -f tests/Doctrine/Tests/Common/Cache/ApcCacheTest.php

: Skip tests requiring a server to connect to
rm -f \
    tests/Doctrine/Tests/Common/Cache/Psr6/CacheAdapterTest.php \
    tests/Doctrine/Tests/Common/Cache/CouchbaseCacheTest.php \
    tests/Doctrine/Tests/Common/Cache/CouchbaseBucketCacheTest.php \
    tests/Doctrine/Tests/Common/Cache/ExtMongoDBCacheTest.php \
    tests/Doctrine/Tests/Common/Cache/LegacyMongoDBCacheTest.php \
    tests/Doctrine/Tests/Common/Cache/MemcacheCacheTest.php \
    tests/Doctrine/Tests/Common/Cache/MemcachedCacheTest.php \
    tests/Doctrine/Tests/Common/Cache/PredisCacheTest.php \
    tests/Doctrine/Tests/Common/Cache/RedisCacheTest.php \
    tests/Doctrine/Tests/Common/Cache/XcacheCacheTest.php

: Upstream tests
RETURN_CODE=0
for PHP_EXEC in "" php74 php80 php81 php82; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC %{_bindir}/phpunit9 --bootstrap bootstrap.php \
            --verbose || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%dir %{phpdir}/Doctrine
%dir %{phpdir}/Doctrine/Common
     %{phpdir}/Doctrine/Common/Cache


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 23 2022 Remi Collet <remi@remirepo.net> - 1.13.0-1
- update to 1.13.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 19 2021 Remi Collet <remi@remirepo.net> - 1.12.1-1
- update to 1.12.1
- allow psr/cache v3
- allow Symfony v6

* Tue May 25 2021 Remi Collet <remi@remirepo.net> - 1.11.3-1
- update to 1.11.3

* Tue May 25 2021 Remi Collet <remi@remirepo.net> - 1.11.2-1
- update to 1.11.2

* Wed May 19 2021 Remi Collet <remi@remirepo.net> - 1.11.1-1
- update to 1.11.1

* Fri Apr 23 2021 Remi Collet <remi@remirepo.net> - 1.11.0-1
- update to 1.11.0
- switch to phpunit9
- add build dependency on psr/cache, symfony/cache and cache/integration-tests

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul  8 2020 Remi Collet <remi@remirepo.net> - 1.10.2-1
- update to 1.10.2

* Thu May 28 2020 Remi Collet <remi@remirepo.net> - 1.10.1-1
- update to 1.10.1 (no change)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec  2 2019 Remi Collet <remi@remirepo.net> - 1.10.0-1
- update to 1.10.0

* Mon Nov 18 2019 Remi Collet <remi@remirepo.net> - 1.9.1-1
- update to 1.9.1

* Tue Nov 12 2019 Remi Collet <remi@remirepo.net> - 1.9.0-1
- update to 1.9.0

* Mon Oct 28 2019 Remi Collet <remi@remirepo.net> - 1.8.1-1
- update to 1.8.1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Remi Collet <remi@remirepo.net> - 1.8.0-1
- update to 1.8.0
- manage optional dependencies in autoloader
- switch to phpunit7

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Sep 10 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.7.1-1
- Update to 1.7.1 (RHBZ #1485327)

* Sat Aug 05 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.7.0-1
- Update to 1.7.0 (RHBZ #1473989)
- Add "get source" script
- Test with SCLs if available

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 04 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.6.1-1
- Updated to 1.6.1 (RHBZ #1389915)
- Removed PHP max version dependency
- Switched autoloader from "symfony/class-loader" to "fedora/autoloader"

* Sat Mar 12 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.6.0-1
- Updated to 1.6.0 (RHBZ #1295634)
- Removed "phpunit without assertNotFalse() function" patch since
  this version will never be built for EL6 (b/c of PHP min version
  dependency)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 25 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.5.4-1
- Updated to 1.5.4 (RHBZ #1276019)
- Added "Suggests" weak dependencies

* Sat Sep 05 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.4.2-1
- Updated to 1.4.2 (RHBZ #1258670 / CVE-2015-5723)

* Sat Jun 27 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.4.1-2
- Updated autoloader with trailing separator

* Wed Jun 24 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.4.1-1
- Updated to 1.4.1 (RHBZ #1211817)
- Added autoloader

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 30 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.4.0-1
- Updated to 1.4.0 (BZ #1183598)

* Wed Sep 24 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.3.1-1
- Updated to 1.3.1 (BZ #1142986)
- Tests update
- %%license usage

* Fri Jun 20 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.3.0-4
- Added php-composer(%%{composer_vendor}/%%{composer_project}) virtual provide
- Removed %%{summary_base}
- Added option to build without tests

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 03 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.3.0-2
- Conditional %%{?dist}
- Removed sub-packages
- Skip all tests requiring a server to connect to

* Mon Dec 23 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.3.0-1
- Initial package
