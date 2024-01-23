#
# Fedora spec file for php-symfony-psr-http-message-bridge
#
# Copyright (c) 2015-2020 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     symfony
%global github_name      psr-http-message-bridge
%global github_version   1.3.0
%global github_commit    9d3e80d54d9ae747ad573cad796e8e247df7b796

%global composer_vendor  symfony
%global composer_project psr-http-message-bridge

# "php": "^7.1"
%global php_min_ver 7.1
# "nyholm/psr7": "^1.1"
%global nyholm_psr7_min_ver 1.1
%global nyholm_psr7_max_ver 2.0
# "psr/http-message": "^1.0"
%global psr_http_message_min_ver 1.0
%global psr_http_message_max_ver 2.0
# "symfony/http-foundation": "^4.4 || ^5.0"
%global symfony_min_ver 4.4
%global symfony_max_ver 6.0
# "zendframework/zend-diactoros": "^1.4.1 || ^2.0"
%global zend_diactoros_min_ver 1.4.1
%global zend_diactoros_max_ver 3.0

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
Release:       9%{?github_release}%{?dist}
Summary:       Symfony PSR HTTP message bridge

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Tests
%if %{with_tests}
BuildRequires: phpunit8
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
%if %{with_range_dependencies}
BuildRequires: (php-composer(nyholm/psr7) >= %{nyholm_psr7_min_ver} with php-composer(nyholm/psr7) < %{nyholm_psr7_max_ver})
BuildRequires: (php-composer(psr/http-message) >= %{psr_http_message_min_ver} with php-composer(psr/http-message) < %{psr_http_message_max_ver})
BuildRequires: (php-composer(symfony/http-foundation) >= %{symfony_min_ver} with php-composer(symfony/http-foundation) < %{symfony_max_ver})
BuildRequires: (php-composer(zendframework/zend-diactoros) >= %{zend_diactoros_min_ver} with php-composer(zendframework/zend-diactoros) < %{zend_diactoros_max_ver})
%else
BuildRequires: php-composer(nyholm/psr7) <  %{nyholm_psr7_max_ver}
BuildRequires: php-composer(nyholm/psr7) >= %{nyholm_psr7_min_ver}
BuildRequires: php-composer(psr/http-message) <  %{psr_http_message_max_ver}
BuildRequires: php-composer(psr/http-message) >= %{psr_http_message_min_ver}
BuildRequires: php-composer(symfony/http-foundation) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/http-foundation) >= %{symfony_min_ver}
BuildRequires: php-composer(zendframework/zend-diactoros) <  %{zend_diactoros_max_ver}
BuildRequires: php-composer(zendframework/zend-diactoros) >= %{zend_diactoros_min_ver}
%endif
## phpcompatinfo (computed from version 1.1.2)
BuildRequires: php-date
BuildRequires: php-reflection
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
%if %{with_range_dependencies}
Requires:      (php-composer(psr/http-message) >= %{psr_http_message_min_ver} with php-composer(psr/http-message) < %{psr_http_message_max_ver})
Requires:      (php-composer(symfony/http-foundation) >= %{symfony_min_ver} with php-composer(symfony/http-foundation) < %{symfony_max_ver})
%else
Requires:      php-composer(psr/http-message) <  %{psr_http_message_max_ver}
Requires:      php-composer(psr/http-message) >= %{psr_http_message_min_ver}
Requires:      php-composer(symfony/http-foundation) <  %{symfony_max_ver}
Requires:      php-composer(symfony/http-foundation) >= %{symfony_min_ver}
%endif
# phpcompatinfo (computed from version 1.1.2)
Requires:      php-date
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Weak dependencies
## composer.json
Suggests:      php-composer(nyholm/psr7)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Provides integration for PSR7.

Autoloader: %{phpdir}/Symfony/Bridge/PsrHttpMessage/autoload.php


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

\Fedora\Autoloader\Autoload::addPsr4('Symfony\\Bridge\\PsrHttpMessage\\', __DIR__);

\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/Psr/Http/Message/autoload.php',
    [
        '%{phpdir}/Symfony5/Component/HttpFoundation/autoload.php',
        '%{phpdir}/Symfony4/Component/HttpFoundation/autoload.php',
    ],
]);

\Fedora\Autoloader\Dependencies::optional([
    '%{phpdir}/Nyholm/Psr7/autoload.php',
]);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/Symfony/Bridge/PsrHttpMessage
cp -rp *.php Factory Tests %{buildroot}%{phpdir}/Symfony/Bridge/PsrHttpMessage/


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee -a bootstrap.php
<?php
require_once '%{buildroot}%{phpdir}/Symfony/Bridge/PsrHttpMessage/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Symfony\\Bridge\\PsrHttpMessage\\Tests\\', __DIR__.'/Tests');

\Fedora\Autoloader\Dependencies::required([
    [
        '%{phpdir}/Zend/Diactoros2/autoload.php',
        '%{phpdir}/Zend/Diactoros/autoload.php',
    ],
]);

/*
if (!class_exists('PHPUnit\\Framework\\TestCase')) {
    class_alias('PHPUnit_Framework_TestCase', 'PHPUnit\\Framework\\TestCase');
}
*/
BOOTSTRAP

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit8)
for PHP_EXEC in "" php72 php73 php74; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose --bootstrap bootstrap.php \
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
%{phpdir}/Symfony/Bridge/PsrHttpMessage
%exclude %{phpdir}/Symfony/Bridge/PsrHttpMessage/Tests


%changelog
* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 08 2020 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.3.0-1
- Update to 1.3.0 (RHBZ #1687504)
- Use PHPUnit 8

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 15 2019 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1.2-1
- Update to 1.1.2
- Remove php-composer(zendframework/zend-diactoros) interoperability (no longer
  suggested in composer.json)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr 22 2018 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.2-2
- Fix el6 tests

* Sun Apr 22 2018 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.2-1
- Update to 1.0.2 (RHBZ #1528620)
- Add range version dependencies for Fedora >= 27 || RHEL >= 8
- Add composer.json to repo
- Remove tests' patch

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 21 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.0-3
- Allow Symfony 3
- Modify tests
- Apply patch to fix test suite with !el6 and zendframework/zend-diactoros

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Apr 15 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.0-1
- Update to 1.0.0 (RHBZ #1370802)
- Add max versions to BuildRequires
- Switch autoloader to php-composer(fedora/autoloader)
- Test with SCLs if available

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Aug 02 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.2-2
- Fixed dependency versions
- Added php-composer(zendframework/zend-diactoros) build dependency for tests
  (excluding el6)
- Autoloader update
- Fixed %%files

* Wed Jul 08 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.2-1
- Initial package
