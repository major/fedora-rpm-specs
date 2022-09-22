#
# Fedora spec file for php-consolidation-log
#
# Copyright (c) 2016-2021 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     consolidation
%global github_name      log
%global github_version   2.0.2
%global github_commit    82a2aaaa621a7b976e50a745a8d249d5085ee2b1

%global composer_vendor  consolidation
%global composer_project log

# "php": ">=7.1.3"
%global php_min_ver 7.1.3
# "psr/log": "^1.0"
#     NOTE: Min version not 1.0 because autoloader required
%global psr_log_min_ver 1.0.1
%global psr_log_max_ver 2.0
# "symfony/console": "^4|^5"
%global symfony_min_ver 4.0
%global symfony_max_ver 6.0

# "phpunit/phpunit": ">=7.5.20"
%global phpunit_require phpunit9
%global phpunit_min_ver 9
%global phpunit_exec    phpunit9
# "yoast/phpunit-polyfills": "^0.2.0"
%global polyfills_min_ver 0.2
%global polyfills_max_ver 2

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

# Range dependencies supported?
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
%global with_range_dependencies 1
%else
%global with_range_dependencies 0
%endif

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       5%{?github_release}%{?dist}
Summary:       Improved PSR-3 / Psr\\Log logger based on Symfony Console components

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: %{phpunit_require} >= %{phpunit_min_ver}
%if %{with_range_dependencies}
BuildRequires: (php-composer(psr/log) >= %{psr_log_min_ver} with php-composer(psr/log) < %{psr_log_max_ver})
BuildRequires: (php-composer(symfony/console) >= %{symfony_min_ver} with php-composer(symfony/console) < %{symfony_max_ver})
BuildRequires: (php-composer(yoast/phpunit-polyfills) >= %{polyfills_min_ver} with php-composer(yoast/phpunit-polyfills) < %{polyfills_max_ver})
%else
BuildRequires: php-composer(psr/log) <  %{psr_log_max_ver}
BuildRequires: php-composer(psr/log) >= %{psr_log_min_ver}
BuildRequires: php-symfony4-console  >= %{symfony_min_ver}
BuildRequires: php-composer(yoast/phpunit-polyfills) <  %{polyfills_max_ver}
BuildRequires: php-composer(yoast/phpunit-polyfills) >= %{polyfills_min_ver}
%endif
## phpcompatinfo (computed from version 2.0.1)
BuildRequires: php-pcre
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
%if %{with_range_dependencies}
Requires:      (php-composer(psr/log) >= %{psr_log_min_ver} with php-composer(psr/log) < %{psr_log_max_ver})
Requires:      (php-composer(symfony/console) >= %{symfony_min_ver} with php-composer(symfony/console) < %{symfony_max_ver})
%else
Requires:      php-composer(psr/log) <  %{psr_log_max_ver}
Requires:      php-composer(psr/log) >= %{psr_log_min_ver}
Requires:      php-symfony4-console  >= %{symfony_min_ver}
%endif
# phpcompatinfo (computed from version 2.0.1)
## none
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Consolidation\Log provides a Psr-3 compatible logger that provides styled log
output to the standard error (stderr) stream. By default, styling is provided
by the SymfonyStyle class from the Symfony Console component; however,
alternative stylers may be provided if desired.

Autoloader: %{phpdir}/Consolidation/Log/autoload.php


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

\Fedora\Autoloader\Autoload::addPsr4('Consolidation\\Log\\', __DIR__);

\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/Psr/Log/autoload.php',
    [
        '%{phpdir}/Symfony5/Component/Console/autoload.php',
        '%{phpdir}/Symfony4/Component/Console/autoload.php',
    ],
]);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/Consolidation
cp -rp src %{buildroot}%{phpdir}/Consolidation/Log


%check
%if %{with_tests}
: Create tests bootstrap
mkdir vendor
cat <<'BOOTSTRAP' | tee vendor/autoload.php
<?php
require '%{buildroot}%{phpdir}/Consolidation/Log/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Consolidation\\TestUtils\\', dirname(__DIR__).'/tests/src');

\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/Yoast/PHPUnitPolyfills/autoload.php',
]);
BOOTSTRAP

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which %{phpunit_exec})
for PHP_EXEC in "" php73 php74 php80; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose --no-coverage \
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
%dir %{phpdir}/Consolidation
     %{phpdir}/Consolidation/Log


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 21 2021 Remi Collet <remi@remirepo.net> - 2.0.2-2
- allow yoast/phpunit-polyfills version 1

* Tue Mar 23 2021 Remi Collet <remi@remirepo.net> - 2.0.2-1
- update to 2.0.2
- switch to phpunit9 with yoast/phpunit-polyfills

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 07 2020 Shawn Iwinski <shawn@iwin.ski> - 2.0.1-1
- Update to 2.0.1 (RHBZ #1850810)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 24 2020 Shawn Iwinski <shawn@iwin.ski> - 2.0.0-1
- Update to 2.0.0
- Use PHPUnit 6

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 01 2019 Shawn Iwinski <shawn@iwin.ski> - 1.1.1-1
- Update to 1.1.1 (RHBZ #1582690)
- Add range version dependencies for Fedora >= 27 || RHEL >= 8

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 20 2017 Shawn Iwinski <shawn@iwin.ski> - 1.0.3-2
- Add max versions to BuildRequires
- Switch autoloader to fedora/autoloader
- Test with SCLs if available

* Tue Aug 09 2016 Shawn Iwinski <shawn@iwin.ski> - 1.0.3-1
- Initial package
