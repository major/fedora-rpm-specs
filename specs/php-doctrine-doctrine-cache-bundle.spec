#
# Fedora spec file for php-doctrine-doctrine-cache-bundle
#
# Copyright (c) 2015-2018 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     doctrine
%global github_name      DoctrineCacheBundle
%global github_version   1.4.0
%global github_commit    6bee2f9b339847e8a984427353670bad4e7bdccb
%global github_short     %(c=%{github_commit}; echo ${c:0:7})

%global composer_vendor  doctrine
%global composer_project doctrine-cache-bundle

# "php": "^7.1"
%global php_min_ver 7.1
# "doctrine/cache": "^1.4.2"
%global cache_min_ver 1.4.2
%global cache_max_ver 2.0
# "doctrine/inflector": "~1.0"
%global inflector_min_ver 1.0
%global inflector_max_ver 2.0
# "symfony/doctrine-bridge":  "^3.4|^4.0"
# "symfony/yaml":             "^3.4|^4.0",
# "symfony/validator":        "^3.4|^4.0",
# "symfony/console":          "^3.4|^4.0",
# "symfony/finder":           "^3.4|^4.0",
# "symfony/framework-bundle": "^3.4|^4.0",
%global symfony_min_ver 3.4
%global symfony_max_ver 5
# "symfony/security-acl":     "^2.8",
%global secacl_min_ver 2.8
%global secacl_max_ver 3

# Build using "--with tests" to enable tests
%global with_tests 0%{?_with_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       12%{?dist}
Summary:       Symfony2 Bundle for Doctrine Cache

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{name}-%{github_version}-%{github_short}.tgz
Source1:       makesrc.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-composer(doctrine/cache) >= %{cache_min_ver} with php-composer(doctrine/cache) <  %{cache_max_ver})
BuildRequires: (php-composer(doctrine/inflector) >= %{inflector_min_ver} with php-composer(doctrine/inflector) <  %{inflector_max_ver})
BuildRequires: (php-composer(symfony/security-acl) >= %{secacl_min_ver} with php-composer(symfony/security-acl) <  %{secacl_max_ver})
# ensure we use same version of all components
BuildRequires: php-symfony4-console
BuildRequires: php-symfony4-doctrine-bridge
BuildRequires: php-symfony4-finder
BuildRequires: php-symfony4-framework-bundle
BuildRequires: php-symfony4-validator
BuildRequires: php-symfony4-yaml
%else
BuildRequires: php-doctrine-cache >= %{cache_min_ver}
BuildRequires: php-doctrine-inflector >= %{inflector_min_ver}
BuildRequires: php-symfony-security-acl
BuildRequires: php-symfony4-console
BuildRequires: php-symfony4-doctrine-bridge
BuildRequires: php-symfony4-finder
BuildRequires: php-symfony4-framework-bundle
BuildRequires: php-symfony4-validator
BuildRequires: php-symfony4-yaml
%endif
BuildRequires: phpunit7
%global phpunit %{_bindir}/phpunit7
## phpcompatinfo (computed from version 1.3.4)
BuildRequires: php-hash
BuildRequires: php-reflection
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-composer(doctrine/cache) >= %{cache_min_ver} with php-composer(doctrine/cache) <  %{cache_max_ver})
Requires:      (php-composer(doctrine/inflector) >= %{inflector_min_ver} with php-composer(doctrine/inflector) <  %{inflector_max_ver})
Requires:      (php-composer(symfony/doctrine-bridge) >= %{symfony_min_ver} with php-composer(symfony/doctrine-bridge) <  %{symfony_max_ver})
%else
Requires:      php-doctrine-cache >= %{cache_min_ver}
Requires:      php-doctrine-inflector >= %{inflector_min_ver}
Requires:      php-symfony4-doctrine-bridge >= %{symfony_min_ver}
%endif
# phpcompatinfo (computed from version 1.4.0)
Requires:      php-hash
Requires:      php-reflection
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)
# Weak dependencies
%if 0%{?fedora} >= 21 || 0%{?rhel} >= 8
Suggests:      php-pecl(memcache)
Suggests:      php-pecl(memcached)
Suggests:      php-pecl(mongo)
Suggests:      php-composer(symfony/security-acl)
%endif

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
%{summary}.

Autoloader: %{phpdir}/Doctrine/Bundle/DoctrineCacheBundle/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
cat <<'AUTOLOAD' | tee autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Doctrine\\Bundle\\DoctrineCacheBundle\\', __DIR__);

\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/Doctrine/Common/Cache/autoload.php',
    '%{phpdir}/Doctrine/Common/Inflector/autoload.php',
    [
        (getenv('RPM_SYMFONY_TREE')?:'%{phpdir}/Symfony4') . '/Bridge/Doctrine/autoload.php',
        '%{phpdir}/Symfony3/Bridge/Doctrine/autoload.php',
    ],
]);

\Fedora\Autoloader\Dependencies::optional([
    [
        '%{phpdir}/Symfony/Component/Security/autoload.php',
    ],
]);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/Doctrine/Bundle/DoctrineCacheBundle
cp -pr Acl Command DependencyInjection Resources Tests *.php \
    %{buildroot}%{phpdir}/Doctrine/Bundle/DoctrineCacheBundle/


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require_once '%{buildroot}%{phpdir}/Doctrine/Bundle/DoctrineCacheBundle/autoload.php';

\Fedora\Autoloader\Dependencies::required([
    [
        '%{phpdir}/Symfony4/Bundle/FrameworkBundle/autoload.php',
        '%{phpdir}/Symfony3/Bundle/FrameworkBundle/autoload.php',
    ], [
        '%{phpdir}/Symfony4/Component/Console/autoload.php',
        '%{phpdir}/Symfony3/Component/Console/autoload.php',
    ], [
        '%{phpdir}/Symfony4/Component/Finder/autoload.php',
        '%{phpdir}/Symfony3/Component/Finder/autoload.php',
    ], [
        '%{phpdir}/Symfony4/Component/Validator/autoload.php',
        '%{phpdir}/Symfony3/Component/Validator/autoload.php',
    ], [
        '%{phpdir}/Symfony4/Component/Yaml/autoload.php',
        '%{phpdir}/Symfony3/Component/Yaml/autoload.php',
    ],
]);
BOOTSTRAP

: Modify PHPUnit config
sed -e 's#\./#%{buildroot}%{phpdir}/Doctrine/Bundle/DoctrineCacheBundle/#g' \
    -e 's#>\.<#>%{buildroot}%{phpdir}/Doctrine/Bundle/DoctrineCacheBundle<#' \
    -i phpunit.xml.dist

: Remove tests requiring a server to connect to
pushd %{buildroot}%{phpdir}/Doctrine/Bundle/DoctrineCacheBundle/Tests
    rm -f \
        Functional/Fixtures/config/predis.xml \
        Functional/PredisCacheTest.php
popd

: Upstream tests
RETURN_CODE=0
for cmdarg in "php %{phpunit}" php71 php72 php73 php74; do
    if which $cmdarg; then
        set $cmdarg
        $1 ${2:-%{_bindir}/phpunit7} --verbose --bootstrap bootstrap.php \
            || RETURN_CODE=1
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
%dir %{phpdir}/Doctrine/Bundle
     %{phpdir}/Doctrine/Bundle/DoctrineCacheBundle
%exclude %{phpdir}/Doctrine/Bundle/DoctrineCacheBundle/Tests


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar 25 2020 Remi Collet <remi@remirepo.net> - 1.4.0-1
- update to 1.4.0
- raise dependency on PHP 7.1
- raise dependency on Symfony 3.4

* Sun Feb 23 2020 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.3.5-5
- Disable tests by default (for now) to fix FTBFS (RHBZ #1799868)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov  9 2018 Remi Collet <remi@remirepo.net> - 1.3.5-1
- update to 1.3.5

* Thu Nov  8 2018 Remi Collet <remi@remirepo.net> - 1.3.4-1
- update to 1.3.4 (no change)
- sources from git snapshot
- use phpunit7

* Wed Oct 17 2018 Remi Collet <remi@remirepo.net> - 1.3.3-1
- update to 1.3.3
- switch to Symfony 4 for test suite
- use range dependencies

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 10 2017 Remi Collet <remi@remirepo.net> - 1.3.2-1
- Update to 1.3.2
- fix FTBFS from Koschei
- ensure we use same version of all component at build time
- allow symfony/doctrine-bridge v4

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 31 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.3.0-6
- Fix test failures with Symfony 2.8.21 (see
  https://github.com/doctrine/DoctrineCacheBundle/pull/112)

* Tue May 30 2017 Remi Collet <remi@remirepo.net> - 1.3.0-5
- allow to force Symfony version using RPM_SYMFONY_TREE

* Sun May 14 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.3.0-4
- Fix autoloder for Symfony 3

* Fri May 12 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.3.0-3
- Switch autoloader to php-composer(fedora/autoloader)
- Add max versions to build dependencies
- Test with SCLs if available

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Mar 31 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.3.0-1
- Updated to 1.3.0 (RHBZ #1279828)
- Updated dependency versions for their autoloaders and modified autoloader
  to use those autoloaders

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jun 27 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.1-3
- Updated autoloader with trailing separator

* Tue Jun 16 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.1-2
- Fix dependencies

* Thu Jun 11 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.1-1
- Initial package
