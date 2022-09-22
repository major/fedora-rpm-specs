#
# Fedora spec file for php-behat-mink
#
# Copyright (c) 2015-2020 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     minkphp
%global github_name      Mink
%global github_version   1.8.1
%global github_commit    07c6a9fe3fa98c2de074b25d9ed26c22904e3887

%global composer_vendor  behat
%global composer_project mink

%global testsuite_github_owner  minkphp
%global testsuite_github_name   driver-testsuite
%global testsuite_github_commit 9ce01154e5331640d2a4f2b9791baf19bb0f4a5d

%if 0%{?fedora} >= 32 || 0%{?rhel} >= 8
%global with_symfony2 0
%else
%global with_symfony2 1
%endif

# "php": ">=5.3.1"
%global php_min_ver 5.3.1
# "symfony/css-selector": "^2.7|^3.0|^4.0|^5.0"
%if %{with_symfony2}
#     NOTE: Min version not 2.7 because autoloader required
%global symfony_min_ver 2.7.1
%else
%global symfony_min_ver 3.0
%endif
%global symfony_max_ver 6.0

# PHPUnit
%if 0%{?fedora} >= 28
%global phpunit_require phpunit7
%global phpunit_exec    phpunit7
%else
%global phpunit_require php-composer(phpunit/phpunit)
%global phpunit_exec    phpunit
%endif

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
Release:       6%{?dist}
Summary:       Browser controller/emulator abstraction for PHP

License:       MIT
URL:           http://mink.behat.org/

# GitHub export does not include tests
# Run php-behat-mink-get-source.sh to create full source
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh
# Test suite
Source2:       https://github.com/%{testsuite_github_owner}/%{testsuite_github_name}/archive/%{testsuite_github_commit}/%{name}-testsuite-%{testsuite_github_commit}.tar.gz

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: %{phpunit_require}
%if %{with_range_dependencies}
BuildRequires: (php-composer(symfony/css-selector) >= %{symfony_min_ver} with php-composer(symfony/css-selector) < %{symfony_max_ver})
%else
BuildRequires: php-composer(symfony/css-selector) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/css-selector) >= %{symfony_min_ver}
%endif
## phpcompatinfo (computed from version 1.8.1)
BuildRequires: php-dom
BuildRequires: php-mbstring
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-spl
### Test suite (computed from commit 9ce01154e5331640d2a4f2b9791baf19bb0f4a5d)
BuildRequires: php-date
BuildRequires: php-gd
BuildRequires: php-json
BuildRequires: php-session
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
%if %{with_range_dependencies}
Requires:      (php-composer(symfony/css-selector) >= %{symfony_min_ver} with php-composer(symfony/css-selector) < %{symfony_max_ver})
%else
Requires:      php-composer(symfony/css-selector) >= %{symfony_min_ver}
Requires:      php-composer(symfony/css-selector) <  %{symfony_max_ver}
%endif
# phpcompatinfo (computed from version 1.8.1)
Requires:      php-mbstring
Requires:      php-pcre
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

# Obsolete test suite sub-package
Obsoletes:     %{name}-driver-testsuite < %{version}-%{release}

%description
One of the most important parts in the web is a browser. Browser is the window
through which web users interact with web applications and other users. Users
are always talking with web applications through browsers.

So, in order to test that our web application behaves correctly, we need a way
to simulate this interaction between the browser and the web application in our
tests. We need a Mink.

Mink is an open source browser controller/emulator for web applications,
written in PHP.

Read Mink at a Glance [1] to learn more about Mink and why you need it.

Autoloader: %{phpdir}/Behat/Mink/autoload.php

[1] http://mink.behat.org/en/latest/at-a-glance.html


%prep
%setup -qn %{github_name}-%{github_commit} -a 2


%build
: Create library autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Behat\\Mink\\', __DIR__);

\Fedora\Autoloader\Dependencies::required(array(
    array(
        '%{phpdir}/Symfony5/Component/CssSelector/autoload.php',
        '%{phpdir}/Symfony4/Component/CssSelector/autoload.php',
        '%{phpdir}/Symfony3/Component/CssSelector/autoload.php',
%if %{with_symfony2}
        '%{phpdir}/Symfony/Component/CssSelector/autoload.php',
%endif
    ),
));
AUTOLOAD


%install
: Library
mkdir -p  %{buildroot}%{phpdir}/Behat
cp -pr src %{buildroot}%{phpdir}/Behat/Mink


%check
%if %{with_tests}
: Setup driver testsuite
mkdir -p vendor/mink
ln -s ../../driver-testsuite-%{testsuite_github_commit} vendor/mink/driver-testsuite

: Create mock Composer autoloader
cat <<'AUTOLOAD' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{phpdir}/Behat/Mink/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Behat\\Mink\\Tests\\', dirname(__DIR__).'/tests');

\Fedora\Autoloader\Autoload::addPsr4('Behat\\Mink\\Tests\\Driver\\Util\\', __DIR__.'/mink/driver-testsuite/src');
\Fedora\Autoloader\Autoload::addPsr4('Behat\\Mink\\Tests\\Driver\\', __DIR__.'/mink/driver-testsuite/tests');
AUTOLOAD

: Remove SymfonyTestsListener
sed \
    -e '/SymfonyTestsListener/d' \
    -e '/listeners>/d' \
    phpunit.xml.dist > phpunit.xml

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which %{phpunit_exec})
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
%dir %{phpdir}/Behat
     %{phpdir}/Behat/Mink


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 17 2020 Shawn Iwinski <shawn@iwin.ski> - 1.8.1-1
- Update to 1.8.1 (RHBZ #1812690)
- Obsolete test suite sub-package
- Testsuite as source to ensure proper version/commit
- Conditionally use range dependencies
- Conditionally drop Symfony 2 interoperability
- Conditionally use PHPUnit 7

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 22 2017 Shawn Iwinski <shawn@iwin.ski> - 1.7.1-5
- Fix autoloader for Symfony 3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri May 12 2017 Shawn Iwinski <shawn@iwin.ski> - 1.7.1-3
- Switch autoloader to php-composer(fedora/autoloader)
- Add max versions to build dependencies
- Test with SCLs if available

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Aug 09 2016 Shawn Iwinski <shawn@iwin.ski> - 1.7.1-1
- Updated to 1.7.1 (RHBZ #1314987)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 25 2015 Shawn Iwinski <shawn@iwin.ski> - 1.7.0-1
- Initial package
