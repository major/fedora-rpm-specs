#
# Fedora spec file for php-doctrine-doctrine-bundle2
#
# Copyright (c) 2015-2022 Shawn Iwinski <shawn.iwinski@gmail.com>
#                         Remi Collet <remi@fedoraproject.org>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     doctrine
%global github_name      DoctrineBundle
%global github_version   2.7.1
%global github_commit    a2dcad48741c9d12fd6040398cf075025030096e
%global major            2

%global composer_vendor  doctrine
%global composer_project doctrine-bundle

# "php": "^7.1 || ^8.0"
%global php_min_ver 7.1
#        "doctrine/annotations": "^1",
%global annotations_min_ver 1
%global annotations_max_ver 2
# "psr/log": "^1.1.4|^2.0|^3.0",
%global psr_log_min_ver 1.1.4
%global psr_log_max_ver 4
# "doctrine/cache": "^1.11|^2.0"
%global cache_min_ver 1.11
%global cache_max_ver 3
# "doctrine/dbal": "^2.13.1|^3.3.2"
%global dbal_min_ver 2.13.1
%global dbal_max_ver 4
# "doctrine/persistence": "^2.2|^3",
%global persistence_min_ver 2.2
%global persistence_max_ver 4
# "doctrine/orm": "~2.11 || ^3.0"
%global orm_min_ver 2.11
%global orm_max_ver 4
# "doctrine/sql-formatter": "^1.0.1"
%global sql_formatter_min_ver 1.0.1
%global sql_formatter_max_ver 2.0
# "symfony/cache": "^4.4|^5.4|^6.0",
# "symfony/config": "^4.4.3|^5.4|^6.0",
# "symfony/console": "^4.4|^5.4|^6.0"
# "symfony/dependency-injection": "^4.4.18|^5.4|^6.0"
# "symfony/doctrine-bridge": "^4.4.22|^5.4|^6.0"
# "symfony/framework-bundle": "^4.4|^5.4|^6.0"
# "symfony/property-info": "^4.4|^5.4|^6.0"
# "symfony/proxy-manager-bridge": "^4.4|^5.4|^6.0"
# "symfony/twig-bridge": "^4.4|^5.4|^6.0",
# "symfony/validator": "^4.4|^5.4|^6.0"
# "symfony/web-profiler-bundle": "^4.4|^5.4|^6.0"
# "symfony/yaml": "^4.4|^5.4|^6.0"
%global symfony_min_ver 4.4.22
%global symfony_max_ver 7
%global symfony_br_ver  %{symfony_min_ver}
# "symfony/service-contracts": "^1.1.1|^2.0|^3",
# "symfony/deprecation-contracts": "^2.1|^3",
%global contracts_min_ver 2.1
%global contracts_max_ver 4
# "twig/twig": "^1.34|^2.12|^3.0"
%global twig_min_ver 1.34
%if 0%{?fedora} >= 26 || 0%{?rhel} >= 8
%global twig_max_ver 4
%else
%global twig_max_ver 2
%endif
# "friendsofphp/proxy-manager-lts": "^1.0",
%global proxy_manager_min_ver 1.0
%global proxy_manager_max_ver 2

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}%{major}
Version:       %{github_version}
Release:       1%{?dist}
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
BuildRequires:(php-composer(doctrine/annotations)           >= %{annotations_min_ver}   with php-composer(doctrine/annotations)           < %{annotations_max_ver})
BuildRequires:(php-composer(doctrine/cache)                 >= %{cache_min_ver}         with php-composer(doctrine/cache)                 < %{cache_max_ver})
BuildRequires:(php-composer(doctrine/dbal)                  >= %{dbal_min_ver}          with php-composer(doctrine/dbal)                  < %{dbal_max_ver})
BuildRequires:(php-composer(doctrine/orm)                   >= %{orm_min_ver}           with php-composer(doctrine/orm)                   < %{orm_max_ver})
BuildRequires:(php-composer(doctrine/persistence)           >= %{persistence_min_ver}   with php-composer(doctrine/persistence)           < %{persistence_max_ver})
BuildRequires:(php-composer(doctrine/sql-formatter)         >= %{sql_formatter_min_ver} with php-composer(doctrine/sql-formatter)         < %{sql_formatter_max_ver})
BuildRequires:(php-composer(psr/log)                        >= %{psr_log_min_ver}       with php-composer(psr/log)                        < %{psr_log_max_ver})
BuildRequires:(php-composer(symfony/deprecation-contracts)  >= %{contracts_min_ver}     with php-composer(symfony/deprecation-contracts)  < %{contracts_max_ver})
BuildRequires:(php-composer(symfony/service-contracts)      >= %{contracts_min_ver}     with php-composer(symfony/service-contracts)      < %{contracts_max_ver})
BuildRequires:(php-composer(friendsofphp/proxy-manager-lts) >= %{proxy_manager_min_ver} with php-composer(friendsofphp/proxy-manager-lts) < %{proxy_manager_max_ver})
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
%if 0%{?fedora} >= 31 || 0%{?rhel} >= 9
%global phpunit %{_bindir}/phpunit9
BuildRequires: phpunit9 >= 9.3
%else
%global phpunit %{_bindir}/phpunit8
BuildRequires: phpunit8 >= 8.0
%endif
## phpcompatinfo (computed from version 2.0.0)
BuildRequires: php-dom
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language)                                >= %{php_min_ver}
Requires:     (php-composer(doctrine/annotations)           >= %{annotations_min_ver}   with php-composer(doctrine/annotations)           < %{annotations_max_ver})
Requires:     (php-composer(doctrine/cache)                 >= %{cache_min_ver}         with php-composer(doctrine/cache)                 < %{cache_max_ver})
Requires:     (php-composer(doctrine/dbal)                  >= %{dbal_min_ver}          with php-composer(doctrine/dbal)                  <  %{dbal_max_ver})
Requires:     (php-composer(doctrine/persistence)           >= %{persistence_min_ver}   with php-composer(doctrine/persistence)           <  %{persistence_max_ver})
Requires:     (php-composer(doctrine/sql-formatter)         >= %{sql_formatter_min_ver} with php-composer(doctrine/sql-formatter)         <  %{sql_formatter_max_ver})
Requires:     (php-composer(symfony/cache)                  >= %{symfony_min_ver}       with php-composer(symfony/cache)                  <  %{symfony_max_ver})
Requires:     (php-composer(symfony/config)                 >= %{symfony_min_ver}       with php-composer(symfony/config)                 <  %{symfony_max_ver})
Requires:     (php-composer(symfony/console)                >= %{symfony_min_ver}       with php-composer(symfony/console)                <  %{symfony_max_ver})
Requires:     (php-composer(symfony/deprecation-contracts)  >= %{contracts_min_ver}     with php-composer(symfony/deprecation-contracts)  <  %{contracts_max_ver})
Requires:     (php-composer(symfony/service-contracts)      >= %{contracts_min_ver}     with php-composer(symfony/service-contracts)      <  %{contracts_max_ver})
Requires:     (php-composer(symfony/dependency-injection)   >= %{symfony_min_ver}       with php-composer(symfony/dependency-injection)   <  %{symfony_max_ver})
Requires:     (php-composer(symfony/doctrine-bridge)        >= %{symfony_min_ver}       with php-composer(symfony/doctrine-bridge)        <  %{symfony_max_ver})
Requires:     (php-composer(symfony/framework-bundle)       >= %{symfony_min_ver}       with php-composer(symfony/framework-bundle)       <  %{symfony_max_ver})
# phpcompatinfo (computed from version 2.0.0)
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
Suggests:      php-pdo

%description
Doctrine DBAL & ORM Bundle for the Symfony Framework.

Autoloader: %{phpdir}/Doctrine/Bundle/DoctrineBundle%{major}/autoload.php


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

\Fedora\Autoloader\Dependencies::optional([
    [
        '%{phpdir}/Doctrine/ORM3/autoload.php',
        '%{phpdir}/Doctrine/ORM/autoload.php',
    ], [
        '%{phpdir}/Symfony6/Bundle/WebProfilerBundle/autoload.php',
        '%{phpdir}/Symfony5/Bundle/WebProfilerBundle/autoload.php',
        '%{phpdir}/Symfony4/Bundle/WebProfilerBundle/autoload.php',
    ], [
        '%{phpdir}/Twig3/autoload.php',
        '%{phpdir}/Twig2/autoload.php',
        '%{phpdir}/Twig/autoload.php',
    ],
]);
\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/Doctrine/Common/Annotations/autoload.php',
    [
        '%{phpdir}/Doctrine/Common/Cache2/autoload.php',
        '%{phpdir}/Doctrine/Common/Cache/autoload.php',
    ], [
        '%{phpdir}/Doctrine/DBAL3/autoload.php',
        '%{phpdir}/Doctrine/DBAL/autoload.php',
    ], [
        '%{phpdir}/Doctrine/Persistence3/autoload.php',
        '%{phpdir}/Doctrine/Persistence2/autoload.php',
    ],
    '%{phpdir}/Doctrine/SqlFormatter/autoload.php',
    [
        '%{phpdir}/Symfony/Contracts3/autoload.php',
        '%{phpdir}/Symfony/Contracts2/autoload.php',
    ],[
        '%{phpdir}/Symfony6/Bridge/Doctrine/autoload.php',
        '%{phpdir}/Symfony5/Bridge/Doctrine/autoload.php',
        '%{phpdir}/Symfony4/Bridge/Doctrine/autoload.php',
    ], [
        '%{phpdir}/Symfony6/Bundle/FrameworkBundle/autoload.php',
        '%{phpdir}/Symfony5/Bundle/FrameworkBundle/autoload.php',
        '%{phpdir}/Symfony4/Bundle/FrameworkBundle/autoload.php',
    ], [
        '%{phpdir}/Symfony6/Component/Cache/autoload.php',
        '%{phpdir}/Symfony5/Component/Cache/autoload.php',
        '%{phpdir}/Symfony4/Component/Cache/autoload.php',
    ], [
        '%{phpdir}/Symfony6/Component/Config/autoload.php',
        '%{phpdir}/Symfony5/Component/Config/autoload.php',
        '%{phpdir}/Symfony4/Component/Config/autoload.php',
    ], [
        '%{phpdir}/Symfony6/Component/Console/autoload.php',
        '%{phpdir}/Symfony5/Component/Console/autoload.php',
        '%{phpdir}/Symfony4/Component/Console/autoload.php',
    ], [
        '%{phpdir}/Symfony6/Component/DependencyInjection/autoload.php',
        '%{phpdir}/Symfony5/Component/DependencyInjection/autoload.php',
        '%{phpdir}/Symfony4/Component/DependencyInjection/autoload.php',
]]);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/Doctrine/Bundle/DoctrineBundle%{major}
cp -pr * %{buildroot}%{phpdir}/Doctrine/Bundle/DoctrineBundle%{major}/


%check
%if %{with_tests}
phpab -o bs.php Tests/DependencyInjection
cat << 'EOF' | tee -a bs.php
require '%{buildroot}%{phpdir}/Doctrine/Bundle/DoctrineBundle%{major}/autoload.php';
\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/Symfony4/Component/PropertyInfo/autoload.php',
    '%{phpdir}/Symfony4/Component/Validator/autoload.php',
    '%{phpdir}/Symfony4/Component/Yaml/autoload.php',
    '%{phpdir}/Symfony4/Bridge/ProxyManager/autoload.php',
    '%{phpdir}/Symfony4/Bridge/Twig/autoload.php',
    '%{phpdir}/FriendsOfPHP/ProxyManager/autoload.php',
    [
        '%{phpdir}/Psr/Log3/autoload.php',
        '%{phpdir}/Psr/Log2/autoload.php',
        '%{phpdir}/Psr/Log/autoload.php',
    ],
]);
EOF

: Skip symfony/phpunit-bridge usage
sed -e '/listener/d' phpunit.xml.dist >phpunit.xml
rm Tests/DependencyInjection/Compiler/CacheCompatibilityPassTest.php

: Upstream tests with SCLs if available
RETURN_CODE=0
for CMDARG in "php %{phpunit}" php74 php80 php81 php82; do
    if which $CMDARG; then
        set $CMDARG
        $1 ${2:-%{_bindir}/phpunit9} \
%if 0%{?rhel} == 7
            --filter '^((?!(testBacktraceLogged|testExecuteXmlWithBundle|testExecuteAnnotationsWithBundle|testExecuteXmlWithNamespace|testExecuteAnnotationsWithNamespace)).)*$' \
%else
            --filter '^((?!(testBacktraceLogged)).)*$' \
%endif
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
%dir     %{phpdir}/Doctrine/Bundle
         %{phpdir}/Doctrine/Bundle/DoctrineBundle%{major}
%exclude %{phpdir}/Doctrine/Bundle/DoctrineBundle%{major}/phpunit.*
%exclude %{phpdir}/Doctrine/Bundle/DoctrineBundle%{major}/Tests


%changelog
* Tue Nov  8 2022 Remi Collet <remi@remirepo.net> - 2.7.1-1
- update to 2.7.1
- raise dependency on Symfony 4.4.22

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Remi Collet <remi@remirepo.net> - 2.7.0-1
- update to 2.7.0

* Mon Apr 25 2022 Remi Collet <remi@remirepo.net> - 2.6.3-1
- update to 2.6.3
- allow doctrine/persistence v3

* Mon Apr 11 2022 Remi Collet <remi@remirepo.net> - 2.6.2-1
- update to 2.6.2

* Mon Apr  4 2022 Remi Collet <remi@remirepo.net> - 2.6.1-1
- update to 2.6.1

* Wed Mar 30 2022 Remi Collet <remi@remirepo.net> - 2.6.0-1
- update to 2.6.0

* Mon Mar  7 2022 Remi Collet <remi@remirepo.net> - 2.5.7-1
- update to 2.5.7

* Tue Feb 15 2022 Remi Collet <remi@remirepo.net> - 2.5.6-1
- update to 2.5.6

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan  6 2022 Remi Collet <remi@remirepo.net> - 2.5.5-1
- update to 2.5.5

* Mon Jan  3 2022 Remi Collet <remi@remirepo.net> - 2.5.4-1
- update to 2.5.4
- allow doctrin/orm 3

* Thu Dec  2 2021 Remi Collet <remi@remirepo.net> - 2.5.2-1
- update to 2.5.2
- allow symfony/contracts 3

* Tue Nov 30 2021 Remi Collet <remi@remirepo.net> - 2.5.1-1
- update to 2.5.1

* Mon Nov 22 2021 Remi Collet <remi@remirepo.net> - 2.5.0-1
- update to 2.5.0
- raise dependency on doctrine/dbal 2.13.1
- raise dependency on dbal doctrine/persistence 2.2

* Mon Oct  4 2021 Remi Collet <remi@remirepo.net> - 2.4.3-1
- update to 2.4.3
- add dependency on doctrine/annotations

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun  7 2021 Remi Collet <remi@remirepo.net> - 2.4.2-1
- update to 2.4.2

* Wed Jun  2 2021 Remi Collet <remi@remirepo.net> - 2.4.1-1
- update to 2.4.1
- add dependency on doctrine/cache
- raise dependency on doctrine/orm 2.9
- allow symfony 5 and 6
- switch to symfony/contracts 2

* Mon May 10 2021 Remi Collet <remi@remirepo.net> - 2.3.2-1
- update to 2.3.2

* Tue Apr  6 2021 Remi Collet <remi@remirepo.net> - 2.3.1-1
- update to 2.3.1

* Mon Mar 29 2021 Remi Collet <remi@remirepo.net> - 2.3.0-1
- update to 2.3.0

* Wed Feb 10 2021 Remi Collet <remi@remirepo.net> - 2.2.3-1
- update to 2.2.3
- switch from ocramius/proxy-manager to friendsofphp/proxy-manager-lts

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec  8 2020 Remi Collet <remi@remirepo.net> - 2.2.2-2
- load ORM autoloader first to ensure proper DBAL version is used

* Tue Dec  8 2020 Remi Collet <remi@remirepo.net> - 2.2.2-1
- update to 2.2.2

* Thu Nov 12 2020 Remi Collet <remi@remirepo.net> - 2.2.1-1
- update to 2.2.1

* Mon Nov  9 2020 Remi Collet <remi@remirepo.net> - 2.2.0-1
- update to 2.2.0
- allow twig version 3
- switch to phpunit9

* Tue Aug 25 2020 Remi Collet <remi@remirepo.net> - 2.1.2-1
- update to 2.1.2

* Tue Aug 25 2020 Remi Collet <remi@remirepo.net> - 2.1.1-1
- update to 2.1.1
- allow doctrine/dbal 3.0
- allow doctrine/persistence 2.0

* Tue May 26 2020 Remi Collet <remi@remirepo.net> - 2.1.0-
- fix dependency and FTBFS #1863700

* Tue May 26 2020 Remi Collet <remi@remirepo.net> - 2.1.0-1
- update to 2.1.0
- switch from jdorn/sql-formatter to doctrine/sql-formatter

* Thu Apr 23 2020 Remi Collet <remi@remirepo.net> - 2.0.8-1
- update to 2.0.8

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Remi Collet <remi@remirepo.net> - 2.0.7-1
- update to 2.0.7

* Fri Jan  3 2020 Remi Collet <remi@remirepo.net> - 2.0.6-1
- update to 2.0.6
- add dependency on doctrine/persistence
- add dependency on symfony/service-contracts
- add build dependency on ocramius/proxy-manager

* Thu Nov 28 2019 Remi Collet <remi@remirepo.net> - 2.0.2-1
- update to 2.0.2
- add dependency on symfony/cache

* Thu Nov 21 2019 Remi Collet <remi@remirepo.net> - 2.0.0-1
- update to 2.0.0
- rename to php-doctrine-doctrine-bundle2
- move to /usr/share/php/Doctrine/Bundle/DoctrineBundle2
- raise dependency on doctrine/dbal 2.9.0
- raise dependency on Symfony 4.3.3
- drop dependency on doctrine/doctrine-cache-bundle

* Wed Nov 20 2019 Remi Collet <remi@remirepo.net> - 1.12.0-1
- update to 1.12.0
- add dependency on symfony/config
- raise build dependency on Symfony 4.3.3

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

* Tue Jan  8 2019 Remi Collet <remi@remirepo.net> - 1.10.1-1
- update to 1.10.1
- prefer symfony 4

* Wed Oct 17 2018 Remi Collet <remi@remirepo.net> - 1.9.1-1
- update to 1.9.1
- raise dependency on doctrine/dbal 2.5.12
- raise dependency on jdorn/sql-formatter 1.2.16

* Fri Nov 10 2017 Remi Collet <remi@remirepo.net> - 1.6.13-1
- Update to 1.6.13
- fix autoloader to allow symfony 2, 3 and 4
- ensure we use same version of all component at build time
- raise dependency on doctrine/doctrine-cache-bundle 1.2
- raise dependency on twig/twig 1.12

* Sat Mar 04 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.6.7-1
- Updated to 1.6.7 (RHBZ #1416390)
- Removed optional dependencies' conflicts
- Changed autoloader to use short array format

* Sun Jan  8 2017 Remi Collet <remi@fedoraproject.org> - 1.6.6-1
- update to 1.6.6
- allow twig 2
- don't allow symfony 3 (autoloader not ready)
- raise dependency on PHP 5.5.9

* Fri Jan  6 2017 Remi Collet <remi@fedoraproject.org> - 1.6.4-2
- drop conflict with twig 2
- ensure twig 1 is used during the build

* Fri Dec 30 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.6.4-1
- Updated to 1.6.4 (RHBZ #1279827)
- Use php-composer(fedora/autoloader)
- Run upstream tests with SCLs if they are available
- Set Resources/doc as %%doc

* Sat Sep 05 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.5.2-1
- Updated to 1.5.2 (RHBZ #1253092 / CVE-2015-5723)
- Updated autoloader to load dependencies after self registration

* Sat Jun 27 2015 Remi Collet <remi@remirepo.net> - 1.5.0-3
- backport for remi repo

* Fri Jun 26 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.5.0-3
- Autoloader updates

* Tue Jun 16 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.5.0-2
- Fixed dependencies
- Added optional dependency version conflicts

* Thu Jun 11 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.5.0-1
- Initial package
