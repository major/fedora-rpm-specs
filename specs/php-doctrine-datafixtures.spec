#
# Fedora spec file for php-doctrine-datafixtures
#
# Copyright (c) 2013-2023 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     doctrine
%global github_name      data-fixtures
%global github_version   1.6.5
%global github_commit    e6b97f557942ea17564bbc30ae3ebc9bd2209363
%global github_short     %(c=%{github_commit}; echo ${c:0:7})

%global composer_vendor  doctrine
%global composer_project data-fixtures

# "php": "^7.2 || ^8.0"
%global php_min_ver 7.2
# "doctrine/orm": "^2.12"
%global doctrine_orm_min_ver 2.12
%global doctrine_orm_max_ver 3.0
# "doctrine/dbal": "^2.13 || ^3.0"
%global doctrine_dbal_min_ver 2.13
%global doctrine_dbal_max_ver 4
# "doctrine/persistence": "^1.3.3|^2.0|^3.0"
%global doctrine_pers_min_ver 1.3.3
%global doctrine_pers_max_ver 4
# "doctrine/deprecations": "^1.0",
%global doctrine_dep_min_ver 1.0
%global doctrine_dep_max_ver 2

# Build using "--without tests" to disable tests
%bcond_without tests

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-datafixtures
Version:       %{github_version}
Release:       6%{?dist}
Summary:       Data Fixtures for all Doctrine Object Managers

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
# Use git snapshot with tests
Source0:       %{name}-%{github_version}-%{github_short}.tgz
Source1:       makesrc.sh

BuildArch:     noarch
# Tests
%if %{with tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-sqlite3
BuildRequires:(php-composer(doctrine/orm)    >= %{doctrine_orm_min_ver}    with php-composer(doctrine/orm)    < %{doctrine_orm_max_ver})
BuildRequires:(php-composer(doctrine/dbal)   >= %{doctrine_dbal_min_ver}   with php-composer(doctrine/dbal)   < %{doctrine_dbal_max_ver})
BuildRequires:(php-composer(doctrine/deprecations) >= %{doctrine_dep_min_ver}   with php-composer(doctrine/deprecations) < %{doctrine_dep_max_ver})
BuildRequires:(php-composer(doctrine/persistence) >= %{doctrine_pers_min_ver}   with php-composer(doctrine/persistence) < %{doctrine_pers_max_ver})
# missing doctrine/mongodb-odm ^1.3.0 || ^2.0.0
BuildRequires: php-symfony4-cache
BuildRequires: phpunit9
## phpcompatinfo (computed from version 1.0.2)
BuildRequires: php-json
BuildRequires: php-reflection
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:     (php-composer(doctrine/deprecations) >= %{doctrine_dep_min_ver}   with php-composer(doctrine/deprecations) < %{doctrine_dep_max_ver})
Requires:     (php-composer(doctrine/persistence) >= %{doctrine_pers_min_ver}   with php-composer(doctrine/persistence) < %{doctrine_pers_max_ver})
# composer.json: optional and deprecated
Suggests:      php-composer(alcaeus/mongo-php-adapter)
# missing option doctrine/mongodb-odm
# phpcompatinfo (computed from version 1.0.2)
Requires:      php-json
Requires:      php-reflection
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Standard "php-{COMPOSER_VENDOR}-{COMPOSER_PROJECT}" naming
Provides:      php-%{composer_vendor}-%{composer_project} = %{version}-%{release}
# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
This extension aims to provide a simple way to manage and execute the loading
of data fixtures for the Doctrine ORM or ODM.

Autoloader: %{phpdir}/Doctrine/Common/DataFixtures/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Doctrine\\Common\\DataFixtures\\', __DIR__);

\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/Doctrine/Deprecations/autoload.php',
    [
        '%{phpdir}/Doctrine/Persistence3/autoload.php',
        '%{phpdir}/Doctrine/Persistence2/autoload.php',
        '%{phpdir}/Doctrine/Persistence/autoload.php',
    ]
]);

\Fedora\Autoloader\Dependencies::optional([
    '%{phpdir}/Doctrine/ORM/autoload.php',
    '%{phpdir}/Alcaeus/MongoDbAdapter/autoload.php',
]);
AUTOLOAD


%install
mkdir -p   %{buildroot}%{phpdir}/Doctrine/Common
cp -rp src %{buildroot}%{phpdir}/Doctrine/Common/DataFixtures


%check
%if %{with tests}
: Create tests bootstrap
cat << 'BOOTSTRAP' | tee bootstrap.php
<?php
require_once '%{buildroot}%{phpdir}/Doctrine/Common/DataFixtures/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Doctrine\\Tests\\', __DIR__.'/tests');
\Fedora\Autoloader\Dependencies::required([
    [
        '%{phpdir}/Doctrine/DBAL3/autoload.php',
        '%{phpdir}/Doctrine/DBAL/autoload.php',
    ],
    '%{phpdir}/Symfony4/Component/Cache/autoload.php',
]);
BOOTSTRAP

: ignore as doctrine/phpcr-odm not available
rm tests/Common/DataFixtures/Executor/PHPCRExecutorTest.php

: Upstream tests
RETURN_CODE=0
for PHP_EXEC in "" php80 php81 php82; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC %{_bindir}/phpunit9 --verbose --bootstrap bootstrap.php \
            || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif


%files
%license LICENSE
%doc *.md
%doc composer.json
%{phpdir}/Doctrine/Common/DataFixtures


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr  7 2023 Remi Collet <remi@remirepo.net> - 1.6.5-1
- update to 1.6.5
- add dependency on doctrine/deprecations

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan  9 2023 Remi Collet <remi@remirepo.net> - 1.6.3-1
- update to 1.6.3

* Fri Jan  6 2023 Remi Collet <remi@remirepo.net> - 1.6.2-1
- update to 1.6.2

* Tue Jan  3 2023 Remi Collet <remi@remirepo.net> - 1.6.1-1
- update to 1.6.1
- drop dependency on doctrine/common

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Apr 20 2022 Remi Collet <remi@remirepo.net> - 1.5.3-1
- update to 1.5.3 (no change)
- allow doctrine/persistence v3
- switch to phpunit9

* Fri Jan 21 2022 Remi Collet <remi@remirepo.net> - 1.5.2-1
- update to 1.5.2
- drop patch merged upstream

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct  5 2021 Remi Collet <remi@remirepo.net> - 1.5.1-1
- update to 1.5.1
- add patch for test suite with doctrine/dbal v3 from
  https://github.com/doctrine/data-fixtures/pull/370

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 25 2021 Remi Collet <remi@remirepo.net> - 1.5.0-1
- update to 1.5.0

* Tue Sep  1 2020 Remi Collet <remi@remirepo.net> - 1.4.4-1
- update to 1.4.4
- raise dependency on doctrine/common 2.13 and allow v3
- allow doctrine/persistence v2

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Remi Collet <remi@remirepo.net> - 1.4.3-1
- update to 1.4.3 (no change)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Remi Collet <remi@remirepo.net> - 1.4.2-1
- update to 1.4.2

* Tue Jan 14 2020 Remi Collet <remi@remirepo.net> - 1.4.1-1
- update to 1.4.1
- add dependency on doctrine/persistence 1.3.3

* Wed Nov 13 2019 Remi Collet <remi@remirepo.net> - 1.4.0-1
- update to 1.4.0
- raise dependency on PHP 7.2
- raise dependency on doctrine/common 2.11

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 11 2019 Remi Collet <remi@remirepo.net> - 1.3.2-1
- update to 1.3.2
- sources from git snapshot because of .gitattributes

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Remi Collet <remi@remirepo.net> - 1.3.1-1
- update to 1.3.1
- raise dependencies on PHP 7.1
- use range dependencies
- doctrine/orm is optional
- add optional dependency on alcaeus/mongo-php-adapter

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri May 12 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.2-5
- Switch autoloader to php-composer(fedora/autoloader)
- Add max versions to build dependencies
- Test with SCLs if available

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jul 31 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.2-1
- Updated/fixed php-composer(doctrine/*) dependencies min version for autoloaders
- Modified autoloader

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jul 03 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.2-1
- Updated to 1.0.2 (RHBZ #1206860)
- Added standard "php-{COMPOSER_VENDOR}-{COMPOSER_PROJECT}" naming provides
- Added autoloader
- %%license usage

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 21 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.0-4
- Added php-composer(%%{composer_vendor}/%%{composer_project}) virtual provide
- Added option to build without tests ("--without tests")
- Updated Doctrine dependencies to use php-composer virtual provides

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Jan 05 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.0-2
- Use non-PEAR Doctrine pkgs
- Conditional %%{?dist}

* Fri Dec 20 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.0-1
- Initial package
