#
# Fedora spec file for php-behat-mink-browserkit-driver
#
# Copyright (c) 2015-2020 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     minkphp
%global github_name      MinkBrowserKitDriver
%global github_version   1.3.4
%global github_commit    e3b90840022ebcd544c7b394a3c9597ae242cbee

%global composer_vendor  behat
%global composer_project mink-browserkit-driver

%global testsuite_github_owner  minkphp
%global testsuite_github_name   driver-testsuite
%global testsuite_github_commit 9ce01154e5331640d2a4f2b9791baf19bb0f4a5d

%if 0%{?fedora} >= 32 || 0%{?rhel} >= 8
%global with_symfony2 0
%else
%global with_symfony2 1
%endif

# "php": ">=5.3.6"
%global php_min_ver 5.3.6
# "behat/mink": "^1.7.1@dev"
%global mink_min_ver 1.7.1
%global mink_max_ver 2.0
# "symfony/browser-kit": "~2.3|~3.0|~4.0"
# "symfony/dom-crawler": "~2.3|~3.0|~4.0"
# "symfony/http-kernel": "~2.3|~3.0|~4.0"
%if %{with_symfony2}
#     NOTE: Min version not 2.3 because autoloader required
%global symfony_min_ver %{?el6:2.3.31}%{!?el6:2.7.1}
%else
%global symfony_min_ver 3.0
%endif
%global symfony_max_ver 5.0

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
Release:       9%{?dist}
Summary:       Symfony BrowserKit driver for Mink framework

License:       MIT
URL:           http://mink.behat.org/en/latest/drivers/browserkit.html
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz
# Test suite
Source1:       https://github.com/%{testsuite_github_owner}/%{testsuite_github_name}/archive/%{testsuite_github_commit}/%{name}-testsuite-%{testsuite_github_commit}.tar.gz

BuildArch:     noarch
# Tests
%if %{with_tests}
BuildRequires: php-composer(phpunit/phpunit)
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
%if %{with_range_dependencies}
BuildRequires: (php-composer(behat/mink) >= %{mink_min_ver} with php-composer(behat/mink) < %{mink_max_ver})
BuildRequires: (php-composer(symfony/browser-kit) >= %{symfony_min_ver} with php-composer(symfony/browser-kit) < %{symfony_max_ver})
BuildRequires: (php-composer(symfony/dom-crawler) >= %{symfony_min_ver} with php-composer(symfony/dom-crawler) < %{symfony_max_ver})
BuildRequires: (php-composer(symfony/http-kernel) >= %{symfony_min_ver} with php-composer(symfony/http-kernel) < %{symfony_max_ver})
%else
BuildRequires: php-composer(behat/mink) <  %{mink_max_ver}
BuildRequires: php-composer(behat/mink) >= %{mink_min_ver}
BuildRequires: php-composer(symfony/browser-kit) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/browser-kit) >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/dom-crawler) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/dom-crawler) >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/http-kernel) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/http-kernel) >= %{symfony_min_ver}
%endif
## phpcompatinfo (computed from version 1.3.4)
BuildRequires: php-pcre
BuildRequires: php-reflection
### Test suite (computed from commit 9ce01154e5331640d2a4f2b9791baf19bb0f4a5d)
BuildRequires: php-date
BuildRequires: php-gd
BuildRequires: php-json
BuildRequires: php-session
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
%if %{with_range_dependencies}
Requires:      (php-composer(behat/mink) >= %{mink_min_ver} with php-composer(behat/mink) < %{mink_max_ver})
Requires:      (php-composer(symfony/browser-kit) >= %{symfony_min_ver} with php-composer(symfony/browser-kit) < %{symfony_max_ver})
Requires:      (php-composer(symfony/dom-crawler) >= %{symfony_min_ver} with php-composer(symfony/dom-crawler) < %{symfony_max_ver})
%else
Requires:      php-composer(behat/mink) <  %{mink_max_ver}
Requires:      php-composer(behat/mink) >= %{mink_min_ver}
Requires:      php-composer(symfony/browser-kit) <  %{symfony_max_ver}
Requires:      php-composer(symfony/browser-kit) >= %{symfony_min_ver}
Requires:      php-composer(symfony/dom-crawler) <  %{symfony_max_ver}
Requires:      php-composer(symfony/dom-crawler) >= %{symfony_min_ver}
%endif
# phpcompatinfo (computed from version 1.3.4)
Requires:      php-pcre
Requires:      php-reflection
# Autoloader
BuildRequires: php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
BrowserKitDriver provides a bridge for the Symfony BrowserKit [1] component.
BrowserKit is a browser emulator provided by the Symfony project [2].

Autoloader: %{phpdir}/Behat/Mink/Driver/autoload-browserkit.php

[1] http://symfony.com/components/BrowserKit
[2] http://symfony.com/


%prep
%setup -qn %{github_name}-%{github_commit} -a 1


%build
: Create library autoloader
cat <<'AUTOLOAD' | tee src/autoload-browserkit.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Behat\\Mink\\Driver\\', __DIR__);

\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/Behat/Mink/autoload.php',
    array(
        '%{phpdir}/Symfony4/Component/BrowserKit/autoload.php',
        '%{phpdir}/Symfony3/Component/BrowserKit/autoload.php',
%if %{with_symfony2}
        '%{phpdir}/Symfony/Component/BrowserKit/autoload.php',
%endif
    ),
    array(
        '%{phpdir}/Symfony4/Component/DomCrawler/autoload.php',
        '%{phpdir}/Symfony3/Component/DomCrawler/autoload.php',
%if %{with_symfony2}
        '%{phpdir}/Symfony/Component/DomCrawler/autoload.php',
%endif
    ),
));
AUTOLOAD


%install
mkdir -p  %{buildroot}%{phpdir}/Behat/Mink/Driver
cp -pr src/* %{buildroot}%{phpdir}/Behat/Mink/Driver/


%check
%if %{with_tests}
: Setup driver testsuite
mkdir -p vendor/mink
ln -s ../../driver-testsuite-%{testsuite_github_commit} vendor/mink/driver-testsuite

: Create mock Composer autoloader
cat <<'BOOTSTRAP' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{phpdir}/Behat/Mink/Driver/autoload-browserkit.php';

\Fedora\Autoloader\Autoload::addPsr4('Behat\\Mink\\Tests\\Driver\\', dirname(__DIR__).'/tests');

\Fedora\Autoloader\Autoload::addPsr4('Behat\\Mink\\Tests\\Driver\\Util\\', __DIR__.'/mink/driver-testsuite/src');
\Fedora\Autoloader\Autoload::addPsr4('Behat\\Mink\\Tests\\Driver\\', __DIR__.'/mink/driver-testsuite/tests');

\Fedora\Autoloader\Dependencies::required(array(
    array(
        '%{phpdir}/Symfony4/Component/HttpKernel/autoload.php',
        '%{phpdir}/Symfony3/Component/HttpKernel/autoload.php',
%if %{with_symfony2}
        '%{phpdir}/Symfony/Component/HttpKernel/autoload.php',
%endif
    ),
));
BOOTSTRAP

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in "" %{?rhel:php54 php55} php56 php70 php71 php72 php73 php74; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose || RETURN_CODE=1
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
%{phpdir}/Behat/Mink/Driver/autoload-browserkit.php
%{phpdir}/Behat/Mink/Driver/BrowserKitDriver.php


%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 17 2020 Shawn Iwinski <shawn@iwin.ski> - 1.3.4-2
- Conditional Symfony 2 or not
- Fix autoloader for PHP < 5.4
- Add test suite BuildRequires

* Tue Mar 17 2020 Shawn Iwinski <shawn@iwin.ski> - 1.3.4-1
- Update to 1.3.4 (RHBZ #1574132)
- Testsuite as source to ensure proper version/commit
- Conditionally use range dependencies
- Drop Symfony 2 interoperability

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri May 12 2017 Shawn Iwinski <shawn@iwin.ski> - 1.3.2-3
- Switch autoloader to php-composer(fedora/autoloader)
- Add max versions to build dependencies
- Test with SCLs if available

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Aug 09 2016 Shawn Iwinski <shawn@iwin.ski> - 1.3.2-1
- Updated to 1.3.2 (RHBZ #1300118)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 25 2015 Shawn Iwinski <shawn@iwin.ski> - 1.3.0-1
- Initial package
