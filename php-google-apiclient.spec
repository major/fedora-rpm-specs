#
# Fedora spec file for php-google-apiclient
#
# Copyright (c) 2014-2021 Shawn Iwinski <shawn.iwinski@gmail.com>
#                         Adam Williamson <awilliam@redhat.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     google
%global github_name      google-api-php-client
%global github_version   2.10.1
%global github_commit    11871e94006ce7a419bb6124d51b6f9ace3f679b

%global composer_vendor  google
%global composer_project apiclient

# "php": "^5.6|^7.0|^8.0"
%global php_min_ver 5.6
# "cache/filesystem-adapter": "^0.3.2|^1.1"
%global cache_filesystem_adapter_min_ver 0.3.2
%global cache_filesystem_adapter_max_ver 2
# "firebase/php-jwt": "~2.0||~3.0||~4.0||~5.0"
%global firebase_php_jwt_min_ver 2.0
%global firebase_php_jwt_max_ver 6.0
# "google/apiclient-services": "~0.200"
%global google_apiclient_services_min_ver 0.200
%global google_apiclient_services_max_ver 1
# "google/auth": "^1.10"
%global google_auth_min_ver 1.10
%global google_auth_max_ver 2
# "guzzlehttp/guzzle": "~5.3.3||~6.0||~7.0"
#     NOTE: Min version not 5.3.3 to force version 6+
%global guzzlehttp_guzzle_min_ver 6
%global guzzlehttp_guzzle_max_ver 8
# "guzzlehttp/psr7": "^1.2"
%global guzzlehttp_psr7_min_ver 1.2
%global guzzlehttp_psr7_max_ver 2
# "monolog/monolog": "^1.17|^2.0"
%global monolog_min_ver 1.17
%global monolog_max_ver 3
# "phpseclib/phpseclib": "~2.0||^3.0.2"
%global phpseclib_min_ver 2
%global phpseclib_max_ver 4
# "symfony/css-selector": "~2.1"
# "symfony/dom-crawler": "~2.1"
%global symfony_min_ver 2.1
%global symfony_max_ver 3

# Build using "--without tests" to disable tests
%bcond_without tests

# Range dependencies supported?
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
%global with_range_dependencies 1
%else
%global with_range_dependencies 0
%endif

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       3%{?dist}
# Epoch bumped to permit downgrade to 1.1.7 due to breaking change in 1.1.8 from v2 to v3 google API bz#1386167
Epoch:         2
Summary:       Client library for Google APIs

License:       ASL 2.0
URL:           https://developers.google.com/api-client-library/php/

# GitHub export does not include tests
# Run php-google-apiclient-get-source.sh to create full source
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: phpunit8
%if %{with_range_dependencies}
BuildRequires: (php-composer(cache/filesystem-adapter) >= %{cache_filesystem_adapter_min_ver} with php-composer(cache/filesystem-adapter) < %{cache_filesystem_adapter_max_ver})
BuildRequires: (php-composer(firebase/php-jwt) >= %{firebase_php_jwt_min_ver} with php-composer(firebase/php-jwt) < %{firebase_php_jwt_max_ver})
BuildRequires: (php-composer(google/apiclient-services) >= %{google_apiclient_services_min_ver} with php-composer(google/apiclient-services) < %{google_apiclient_services_max_ver})
BuildRequires: (php-composer(google/auth) >= %{google_auth_min_ver} with php-composer(google/auth) < %{google_auth_max_ver})
BuildRequires: (php-composer(guzzlehttp/guzzle) >= %{guzzlehttp_guzzle_min_ver} with php-composer(guzzlehttp/guzzle) < %{guzzlehttp_guzzle_max_ver})
BuildRequires: (php-composer(guzzlehttp/psr7) >= %{guzzlehttp_psr7_min_ver} with php-composer(guzzlehttp/psr7) < %{guzzlehttp_psr7_max_ver})
BuildRequires: (php-composer(monolog/monolog) >= %{monolog_min_ver} with php-composer(monolog/monolog) < %{monolog_max_ver})
BuildRequires: (php-composer(phpseclib/phpseclib) >= %{phpseclib_min_ver} with php-composer(phpseclib/phpseclib) < %{phpseclib_max_ver})
BuildRequires: (php-composer(symfony/css-selector) >= %{symfony_min_ver} with php-composer(symfony/css-selector) < %{symfony_max_ver})
BuildRequires: (php-composer(symfony/dom-crawler) >= %{symfony_min_ver} with php-composer(symfony/dom-crawler) < %{symfony_max_ver})
%else
BuildRequires: php-composer(cache/filesystem-adapter) <  %{cache_filesystem_adapter_max_ver}
BuildRequires: php-composer(cache/filesystem-adapter) >= %{cache_filesystem_adapter_min_ver}
BuildRequires: php-composer(firebase/php-jwt) <  %{firebase_php_jwt_max_ver}
BuildRequires: php-composer(firebase/php-jwt) >= %{firebase_php_jwt_min_ver}
BuildRequires: php-composer(google/apiclient-services) <  %{google_apiclient_services_max_ver}
BuildRequires: php-composer(google/apiclient-services) >= %{google_apiclient_services_min_ver}
BuildRequires: php-composer(google/auth) <  %{google_auth_max_ver}
BuildRequires: php-composer(google/auth) >= %{google_auth_min_ver}
BuildRequires: php-composer(guzzlehttp/guzzle) <  %{guzzlehttp_guzzle_max_ver}
BuildRequires: php-composer(guzzlehttp/guzzle) >= %{guzzlehttp_guzzle_min_ver}
BuildRequires: php-composer(guzzlehttp/psr7) <  %{guzzlehttp_psr7_max_ver}
BuildRequires: php-composer(guzzlehttp/psr7) >= %{guzzlehttp_psr7_min_ver}
BuildRequires: php-composer(monolog/monolog) <  %{monolog_max_ver}
BuildRequires: php-composer(monolog/monolog) >= %{monolog_min_ver}
BuildRequires: php-composer(phpseclib/phpseclib) <  %{phpseclib_max_ver}
BuildRequires: php-composer(phpseclib/phpseclib) >= %{phpseclib_min_ver}
BuildRequires: php-composer(symfony/css-selector) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/css-selector) >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/dom-crawler) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/dom-crawler) >= %{symfony_min_ver}
%endif
## phpcompatinfo (computed from version 2.10.1)
BuildRequires: php-curl
BuildRequires: php-date
BuildRequires: php-filter
BuildRequires: php-json
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-spl
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 2.10.1)
Requires:      php-date
Requires:      php-filter
Requires:      php-json
Requires:      php-pcre
Requires:      php-reflection
Requires:      php-spl

# Weak dependencies
%if 0%{?fedora} >= 21
Suggests:      php-composer(cache/filesystem-adapter)
Suggests:      php-pecl(apcu)
Suggests:      php-pecl(memcache)
Suggests:      php-pecl(memcached)
%endif

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

Obsoletes:     %{name}-examples <= %{version}


%description
Google APIs Client Library for PHP provides access to many Google APIs.
It is designed for PHP client-application developers and offers simple,
flexible, powerful API access.

Autoloader: %{phpdir}/Google/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create Fedora autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Google\\', __DIR__);

\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/Firebase/JWT/autoload.php',
    '%{phpdir}/Google/Auth/autoload.php',
    '%{phpdir}/Google/Service/autoload.php',
    [
        '%{phpdir}/GuzzleHttp7/autoload.php',
        '%{phpdir}/GuzzleHttp6/autoload.php',
    ],
    '%{phpdir}/GuzzleHttp/Psr7/autoload.php',
    [
        '%{phpdir}/Monolog2/autoload.php',
        '%{phpdir}/Monolog/autoload.php',
    ],
    [
        '%{phpdir}/phpseclib3/autoload.php',
        '%{phpdir}/phpseclib/autoload.php',
    ],
]);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/Google
cp -rp src/* %{buildroot}%{phpdir}/Google/


%check
%if %{with tests}
: Mock Composer autoloader
mkdir vendor
cat <<'BOOTSTRAP' | tee vendor/autoload.php
<?php
require '%{buildroot}%{phpdir}/Google/autoload.php';

\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/Cache/Adapter/Filesystem/autoload.php',
    '%{phpdir}/Symfony/Component/CssSelector/autoload.php',
    '%{phpdir}/Symfony/Component/DomCrawler/autoload.php',
]);
BOOTSTRAP

: Skip tests requiring network access
sed -e 's/function testPhpsecConstants/function SKIP_testPhpsecConstants/' \
    -e 's/function testRetrieveCertsFromLocation/function SKIP_testRetrieveCertsFromLocation/' \
    -i tests/Google/AccessToken/VerifyTest.php
sed 's/function testExceptionResponse/function SKIP_testExceptionResponse/' \
    -i tests/Google/Http/RESTTest.php

: Skip tests known to fail
rm -f tests/Google/Task/ComposerTest.php

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit8)
for PHP_EXEC in "" %{?rhel:php70 php71 php72 php73 php74} php80 php81; do
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
%{phpdir}/Google


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Sep 18 2021 Shawn Iwinski <shawn.iwinski@gmail.com> - 2:2.10.1-1
- Update to 2.10.1 (RHBZ #1438295)
- Fix "FTBFS in Fedora rawhide/f35" (RHBZ #1987814)
- Obsolete "examples" sub-package

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.1.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.1.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.1.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.1.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.1.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Oct 18 2016 James Hogarth <james.hogarth@gmail.com> - 2:1.1.7-2
- Missed an %%{epoch} for the examples subpackage

* Tue Oct 18 2016 James Hogarth <james.hogarth@gmail.com> - 2:1.1.7-1
- Downgrade to 1.1.7 (RHBZ #1386167)

* Sun Jul 24 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1.8-1
- Updated to 1.1.8 (RHBZ #1275453)
- Added weak dependencies
- Always ensure unbundled CA cert is referenced

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Oct 11 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1.5-1
- Updated to 1.1.5 (RHBZ #1266282)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 22 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1.4-1
- Updated to 1.1.4 (BZ #1222260)
- Added spec license header
- Removed autoload patch
- Added option to build without tests

* Fri Jan 02 2015 Adam Williamson <awilliam@redhat.com> - 1.1.2-2
- update autoloader relocation patch to match latest upstream submission

* Sat Dec 20 2014 Adam Williamson <awilliam@redhat.com> - 1.1.2-1
- new upstream release 1.1.2
- relocate autoloader to make it work with systemwide installation

* Sat Dec 20 2014 Adam Williamson <awilliam@redhat.com> - 1.0.6-0.3.beta
- use new %%license directory
- add Packagist/Composer provide

* Fri Nov 07 2014 Adam Williamson <awilliam@redhat.com> - 1.0.6-0.2.beta
- apply CA trust store path substitution to Curl as well as Stream

* Fri Nov 07 2014 Adam Williamson <awilliam@redhat.com> - 1.0.6-0.1.beta
- new upstream release 1.0.6-beta

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-0.3.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 19 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.3-0.2.beta
- Backported commit c6949531d2399f81a5e15caf256f156dd68e00e9 for OwnCloud
- Sub-packaged examples

* Sat Feb 08 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.3-0.1.beta
- Initial package
