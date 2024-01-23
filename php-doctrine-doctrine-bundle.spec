#
# Fedora spec file for php-doctrine-doctrine-bundle
#
# Copyright (c) 2015-2020 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     doctrine
%global github_name      DoctrineBundle
%global github_version   1.12.13
%global github_commit    85460b85edd8f61a16ad311e7ffc5d255d3c937c

%global composer_vendor  doctrine
%global composer_project doctrine-bundle

# "php": "^7.1 || ^8.0"
%global php_min_ver 7.1
# "doctrine/dbal": "^2.5.12|^3.0"
%global dbal_min_ver 2.5.12
%global dbal_max_ver 4
# "doctrine/doctrine-cache-bundle": "~1.2"
%global cache_bundle_min_ver 1.2
%global cache_bundle_max_ver 2.0
# "doctrine/persistence": "^1.3.3",
%global persistence_min_ver 1.3.3
%global persistence_max_ver 2
# "doctrine/orm": "~2.6"
%global orm_min_ver 2.6
%global orm_max_ver 3.0
# "jdorn/sql-formatter": "^1.2.16"
%global sql_formatter_min_ver 1.2.16
%global sql_formatter_max_ver 2.0
# "symfony/cache": "^3.4.30|^4.3.3",
# "symfony/config": "^3.4.30|^4.3.3",
# "symfony/console": "^3.4.30|^4.3.3"
# "symfony/dependency-injection": "^3.4.30|^4.3.3"
# "symfony/doctrine-bridge": "^3.4.30|^4.3.3"
# "symfony/framework-bundle": "^3.4.30|^4.3.3"
# "symfony/cache": "^3.4.30|^4.3.3",
# "symfony/property-info": "^3.4.30|^4.3.3"
# "symfony/proxy-manager-bridge": "^3.4|^4|^5",
# "symfony/twig-bridge": "^3.4|^4.1",
# "symfony/validator": "^3.4.30|^4.3.3"
# "symfony/web-profiler-bundle": "^3.4.30|^4.3.3"
# "symfony/yaml": "^3.4.30|^4.3.3"
%global symfony_min_ver 3.4
%global symfony_max_ver 5
%global symfony_br_ver 4.3.3
# "symfony/service-contracts": "^1.1.1|^2.0",
# TODO v2 is not yet packaged
%global contracts_min_ver 1.1.1
%global contracts_max_ver 2
# "twig/twig": "~1.34|~2.12"
%global twig_min_ver 1.34
%if 0%{?fedora} >= 26 || 0%{?rhel} >= 8
%global twig_max_ver 3
%else
%global twig_max_ver 2
%endif
# "ocramius/proxy-manager": "^2.1",
%global proxy_manager_min_ver 2.1
%global proxy_manager_max_ver 3

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       9%{?dist}
Summary:       Symfony Bundle for Doctrine

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

Patch0:        %{name}-vendor.patch

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language)                                >= %{php_min_ver}
BuildRequires: php-theseer-autoload
BuildRequires:(php-composer(doctrine/dbal)                  >= %{dbal_min_ver}          with php-composer(doctrine/dbal)                  < %{dbal_max_ver})
BuildRequires:(php-composer(doctrine/doctrine-cache-bundle) >= %{cache_bundle_min_ver}  with php-composer(doctrine/doctrine-cache-bundle) < %{cache_bundle_max_ver})
BuildRequires:(php-composer(doctrine/orm)                   >= %{orm_min_ver}           with php-composer(doctrine/orm)                   < %{orm_max_ver})
BuildRequires:(php-composer(doctrine/persistence)           >= %{persistence_min_ver}   with php-composer(doctrine/persistence)           < %{persistence_max_ver})
BuildRequires:(php-composer(jdorn/sql-formatter)            >= %{sql_formatter_min_ver} with php-composer(jdorn/sql-formatter)            < %{sql_formatter_max_ver})
BuildRequires:(php-composer(symfony/service-contracts)      >= %{contracts_min_ver}     with php-composer(symfony/service-contracts)      < %{contracts_max_ver})
BuildRequires:(php-composer(ocramius/proxy-manager)         >= %{proxy_manager_min_ver} with php-composer(ocramius/proxy-manager)         < %{proxy_manager_max_ver})
BuildRequires:(php-composer(twig/twig)                      >= %{twig_min_ver}          with php-composer(twig/twig)                      < %{twig_max_ver})
# ensure same version of all components is used
# "require"
BuildRequires: php-symfony4-cache                 >= %{symfony_br_ver}
BuildRequires: php-symfony4-config                >= %{symfony_br_ver}
BuildRequires: php-symfony4-console               >= %{symfony_br_ver}
BuildRequires: php-symfony4-dependency-injection  >= %{symfony_br_ver}
BuildRequires: php-symfony4-doctrine-bridge       >= %{symfony_br_ver}
BuildRequires: php-symfony4-framework-bundle      >= %{symfony_br_ver}
# "require-dev"
BuildRequires: php-symfony4-property-info         >= %{symfony_br_ver}
BuildRequires: php-symfony4-proxy-manager-bridge  >= %{symfony_br_ver}
BuildRequires: php-symfony4-twig-bridge           >= %{symfony_br_ver}
BuildRequires: php-symfony4-validator             >= %{symfony_br_ver}
BuildRequires: php-symfony4-web-profiler-bundle   >= %{symfony_br_ver}
BuildRequires: php-symfony4-yaml                  >= %{symfony_br_ver}
BuildRequires: phpunit7 >= 7.5
## phpcompatinfo (computed from version 1.11.0)
BuildRequires: php-dom
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language)                                >= %{php_min_ver}
Requires:     (php-composer(doctrine/dbal)                  >= %{dbal_min_ver}          with php-composer(doctrine/dbal)                  <  %{dbal_max_ver})
Requires:     (php-composer(doctrine/doctrine-cache-bundle) >= %{cache_bundle_min_ver}  with php-composer(doctrine/doctrine-cache-bundle) <  %{cache_bundle_max_ver})
Requires:     (php-composer(doctrine/persistence)           >= %{persistence_min_ver}   with php-composer(doctrine/persistence)           <  %{persistence_max_ver})
Requires:     (php-composer(jdorn/sql-formatter)            >= %{sql_formatter_min_ver} with php-composer(jdorn/sql-formatter)            <  %{sql_formatter_max_ver})
Requires:     (php-composer(symfony/cache)                  >= %{symfony_min_ver}       with php-composer(symfony/cache)                  <  %{symfony_max_ver})
Requires:     (php-composer(symfony/config)                 >= %{symfony_min_ver}       with php-composer(symfony/config)                 <  %{symfony_max_ver})
Requires:     (php-composer(symfony/console)                >= %{symfony_min_ver}       with php-composer(symfony/console)                <  %{symfony_max_ver})
Requires:     (php-composer(symfony/service-contracts)      >= %{contracts_min_ver}     with php-composer(symfony/service-contracts)      <  %{contracts_max_ver})
Requires:     (php-composer(symfony/dependency-injection)   >= %{symfony_min_ver}       with php-composer(symfony/dependency-injection)   <  %{symfony_max_ver})
Requires:     (php-composer(symfony/doctrine-bridge)        >= %{symfony_min_ver}       with php-composer(symfony/doctrine-bridge)        <  %{symfony_max_ver})
Requires:     (php-composer(symfony/framework-bundle)       >= %{symfony_min_ver}       with php-composer(symfony/framework-bundle)       <  %{symfony_max_ver})
# phpcompatinfo (computed from version 1.11.0)
Requires:      php-pcre
Requires:      php-reflection
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

# Weak dependencies
Suggests:      php-composer(doctrine/orm)
Suggests:      php-composer(symfony/web-profiler-bundle)
Suggests:      php-composer(twig/twig)

%description
Doctrine DBAL & ORM Bundle for the Symfony Framework.

Autoloader: %{phpdir}/Doctrine/Bundle/DoctrineBundle/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}
%patch0 -p1 -b .rpm

find . -name \*.rpm -delete -print

: Licenses and docs
mkdir -p .rpm/{docs,licenses}
mv *.md composer.* .rpm/docs
mkdir -p .rpm/docs/Resources
mv Resources/doc .rpm/docs/Resources/
mv LICENSE .rpm/licenses


%build
: Create autoloader
cat <<'AUTOLOAD' | tee autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Doctrine\\Bundle\\DoctrineBundle\\', __DIR__);

\Fedora\Autoloader\Dependencies::required([
    [
        '%{phpdir}/Symfony4/Bridge/Doctrine/autoload.php',
        '%{phpdir}/Symfony3/Bridge/Doctrine/autoload.php',
    ], [
        '%{phpdir}/Symfony4/Bundle/FrameworkBundle/autoload.php',
        '%{phpdir}/Symfony3/Bundle/FrameworkBundle/autoload.php',
    ], [
        '%{phpdir}/Symfony4/Component/Cache/autoload.php',
        '%{phpdir}/Symfony3/Component/Cache/autoload.php',
    ], [
        '%{phpdir}/Symfony4/Component/Config/autoload.php',
        '%{phpdir}/Symfony3/Component/Config/autoload.php',
    ], [
        '%{phpdir}/Symfony4/Component/Console/autoload.php',
        '%{phpdir}/Symfony3/Component/Console/autoload.php',
    ], [
        '%{phpdir}/Symfony4/Component/DependencyInjection/autoload.php',
        '%{phpdir}/Symfony3/Component/DependencyInjection/autoload.php',
    ],
    '%{phpdir}/Doctrine/Bundle/DoctrineCacheBundle/autoload.php',
    [
        '%{phpdir}/Doctrine/DBAL3/autoload.php',
        '%{phpdir}/Doctrine/DBAL/autoload.php',
    ],
    '%{phpdir}/Doctrine/Persistence/autoload.php',
    '%{phpdir}/jdorn-sql-formatter/autoload.php',
    '%{phpdir}/Symfony/Contracts/autoload.php',
]);

\Fedora\Autoloader\Dependencies::optional([
    '%{phpdir}/Doctrine/ORM/autoload.php',
    [
        '%{phpdir}/Symfony4/Bundle/WebProfilerBundle/autoload.php',
        '%{phpdir}/Symfony3/Bundle/WebProfilerBundle/autoload.php',
    ], [
        '%{phpdir}/Twig2/autoload.php',
        '%{phpdir}/Twig/autoload.php',
    ],
]);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/Doctrine/Bundle/DoctrineBundle
cp -pr * %{buildroot}%{phpdir}/Doctrine/Bundle/DoctrineBundle/


%check
%if %{with_tests}
phpab -o bs.php Tests/DependencyInjection
cat << 'EOF' | tee -a bs.php
require '%{buildroot}%{phpdir}/Doctrine/Bundle/DoctrineBundle/autoload.php';
\Fedora\Autoloader\Dependencies::required([
    [
        '%{phpdir}/Twig2/autoload.php',
        '%{phpdir}/Twig/autoload.php',
    ],
    '%{phpdir}/Symfony4/Component/PropertyInfo/autoload.php',
    '%{phpdir}/Symfony4/Component/Validator/autoload.php',
    '%{phpdir}/Symfony4/Component/Yaml/autoload.php',
    '%{phpdir}/Symfony4/Bridge/ProxyManager/autoload.php',
    '%{phpdir}/Symfony4/Bridge/Twig/autoload.php',
    '%{phpdir}/ProxyManager/autoload.php',
]);
EOF

sed -e '/listener/d' phpunit.xml.dist >phpunit.xml

: Skip tests known to fail
rm -f Tests/ConnectionFactoryTest.php
sed \
    -e 's/function testExecuteXmlWithBundle/function SKIP_testExecuteXmlWithBundle/' \
    -e 's/function testExecuteAnnotationsWithBundle/function SKIP_testExecuteAnnotationsWithBundle/' \
    -e 's/function testExecuteThrowsExceptionWithNamespaceAndNoPath/function SKIP_testExecuteThrowsExceptionWithNamespaceAndNoPath/' \
    -e 's/function testExecuteXmlWithNamespace/function SKIP_testExecuteXmlWithNamespace/' \
    -e 's/function testExecuteAnnotationsWithNamespace/function SKIP_testExecuteAnnotationsWithNamespace/' \
    -i Tests/Command/ImportMappingDoctrineCommandTest.php
sed 's/function testContainer/function SKIP_testContainer/' \
    -i Tests/ContainerTest.php
sed 's/function testIdentityMapsStayConsistentAfterReset/function SKIP_testIdentityMapsStayConsistentAfterReset/' \
    -i Tests/RegistryTest.php
sed 's/function testDbalSchemaFilterNewConfig/function SKIP_testDbalSchemaFilterNewConfig/' \
    -i Tests/DependencyInjection/AbstractDoctrineExtensionTest.php


: Upstream tests with SCLs if available
RETURN_CODE=0
for SCL in php php72 php73 php74 php80 php81 php82; do
    if which $SCL; then
        $SCL %{_bindir}/phpunit7 \
            --filter '^((?!(testBacktraceLogged|testRender)).)*$' \
            --bootstrap bs.php \
            --verbose || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif


%files
%license .rpm/licenses/*
%doc .rpm/docs/*
%{phpdir}/Doctrine/Bundle/DoctrineBundle
%exclude %{phpdir}/Doctrine/Bundle/DoctrineBundle/phpunit.*
%exclude %{phpdir}/Doctrine/Bundle/DoctrineBundle/Tests


%changelog
* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.13-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Oct 12 2022 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.12.13-6
- Skip tests known to fail to fix FTBFS

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec  8 2020 Remi Collet <remi@remirepo.net> - 1.12.13-1
- update to 1.12.13
- allow doctrine/dbal v3

* Thu Nov 12 2020 Remi Collet <remi@remirepo.net> - 1.12.12-1
- update to 1.12.12

* Mon Nov  9 2020 Remi Collet <remi@remirepo.net> - 1.12.11-1
- update to 1.12.11

* Tue May 26 2020 Remi Collet <remi@remirepo.net> - 1.12.10-2
- fix dependency and FTBFS #1863698

* Tue May 26 2020 Remi Collet <remi@remirepo.net> - 1.12.10-1
- update to 1.12.10

* Thu Apr 23 2020 Remi Collet <remi@remirepo.net> - 1.12.8-1
- update to 1.12.8

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Remi Collet <remi@remirepo.net> - 1.12.7-1
- update to 1.12.7

* Fri Jan  3 2020 Remi Collet <remi@remirepo.net> - 1.12.6-1
- update to 1.12.6
- add dependency on doctrine/persistence
- add dependency on symfony/service-contracts
- add build dependency on ocramius/proxy-manager

* Thu Nov 28 2019 Remi Collet <remi@remirepo.net> - 1.12.2-1
- update to 1.12.2

* Thu Nov 28 2019 Remi Collet <remi@remirepo.net> - 1.12.1-1
- update to 1.12.1
- add dependency on symfony/cache
- add dependency on symfony/config
- raise build dependency on Symfony 4.3.3

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun  4 2019 Remi Collet <remi@remirepo.net> - 1.11.2-1
- update to 1.11.2

* Tue May 14 2019 Remi Collet <remi@remirepo.net> - 1.11.1-1
- update to 1.11.1

* Mon May 13 2019 Remi Collet <remi@remirepo.net> - 1.11.0-1
- update to 1.11.0
- raise dependency on PHP 7.1
- raise dependency on symfony 3.4
- use phpunit7

* Fri Feb  8 2019 Remi Collet <remi@remirepo.net> - 1.10.2-1
- update to 1.10.2

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan  8 2019 Remi Collet <remi@remirepo.net> - 1.10.1-1
- update to 1.10.1
- prefer symfony 4

* Wed Oct 17 2018 Remi Collet <remi@remirepo.net> - 1.9.1-1
- update to 1.9.1
- raise dependency on doctrine/dbal 2.5.12
- raise dependency on jdorn/sql-formatter 1.2.16

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 10 2017 Remi Collet <remi@remirepo.net> - 1.6.13-1
- Update to 1.6.13
- fix autoloader to allow symfony 2, 3 and 4
- ensure we use same version of all component at build time
- raise dependency on doctrine/doctrine-cache-bundle 1.2
- raise dependency on twig/twig 1.12

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 04 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.6.7-1
- Updated to 1.6.7 (RHBZ #1416390)
- Removed optional dependencies' conflicts
- Changed autoloader to use short array format

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan  8 2017 Remi Collet <remi@fedoraproject.org> - 1.6.6-1
- update to 1.6.6
- allow twig 2
- don't allow symfony 3 (autoloader not ready)
- raise dependency on PHP 5.5.9

* Fri Dec 30 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.6.4-1
- Updated to 1.6.4 (RHBZ #1279827)
- Use php-composer(fedora/autoloader)
- Run upstream tests with SCLs if they are available
- Set Resources/doc as %%doc

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 05 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.5.2-1
- Updated to 1.5.2 (RHBZ #1253092 / CVE-2015-5723)
- Updated autoloader to load dependencies after self registration

* Fri Jun 26 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.5.0-3
- Autoloader updates

* Tue Jun 16 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.5.0-2
- Fixed dependencies
- Added optional dependency version conflicts

* Thu Jun 11 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.5.0-1
- Initial package
