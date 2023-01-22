#
# Fedora spec file for php-google-auth
#
# Copyright (c) 2017-2022 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     google
%global github_name      google-auth-library-php
%global github_version   1.23.0
%global github_commit    8da16102d2cd1bdc128d97f323553df465ee7701

%global composer_vendor  google
%global composer_project auth

# "php": "^7.1||^8.0"
%global php_min_ver 7.1
# "firebase/php-jwt": "^5.5||^6.0"
%global firebase_jwt_min_ver 5.5
%global firebase_jwt_max_ver 7.0
# "guzzlehttp/guzzle": "^6.2.1|^7.0"
%global guzzle_min_ver 6.2.1
%global guzzle_max_ver 8.0
# "guzzlehttp/psr7": "^1.7|^2.0"
#     NOTE: Not currently allowing v2 until we know what it's install directory will be
%global guzzle_psr7_min_ver 1.7
%global guzzle_psr7_max_ver 2.0
# "guzzlehttp/promises": "0.1.1|^1.3"
%global guzzle_promises_min_ver 0.1.1
%global guzzle_promises_max_ver 2.0
# "phpseclib/phpseclib": "^2.0.31"
%global phpseclib_min_ver 2.0.31
%global phpseclib_max_ver 3.0
# "psr/cache": "^1.0|^2.0|^3.0"
%global psr_cache_min_ver 1.0
%global psr_cache_max_ver 4.0
# "psr/http-message": "^1.0"
%global psr_http_message_min_ver 1.0
%global psr_http_message_max_ver 2.0

# "phpunit/phpunit": "^7.5||^8.5"
%global phpunit_require phpunit8
%global phpunit_min_ver 8
%global phpunit_exec    phpunit8

# Build using "--without tests" to disable tests
%bcond_without tests

# Range dependencies supported?
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
%global with_range_dependencies 1
%else
%global with_range_dependencies 0
%endif

# Weak dependencies supported?
%if 0%{?fedora} >= 21 || 0%{?rhel} >= 8
%global with_weak_dependencies 1
%else
%global with_weak_dependencies 0
%endif

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       2%{?github_release}%{?dist}
Summary:       Google Auth Library for PHP

License:       ASL 2.0
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests
# Run php-google-auth-get-source.sh to create full source
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: %{phpunit_require} >= %{phpunit_min_ver}
%if %{with_range_dependencies}
BuildRequires: (php-composer(firebase/php-jwt) >= %{firebase_jwt_min_ver} with php-composer(firebase/php-jwt) < %{firebase_jwt_max_ver})
BuildRequires: (php-composer(guzzlehttp/guzzle) >= %{guzzle_min_ver} with php-composer(guzzlehttp/guzzle) < %{guzzle_max_ver})
BuildRequires: (php-composer(guzzlehttp/promises) >= %{guzzle_promises_min_ver} with php-composer(guzzlehttp/promises) < %{guzzle_promises_max_ver})
BuildRequires: (php-composer(guzzlehttp/psr7) >= %{guzzle_psr7_min_ver} with php-composer(guzzlehttp/psr7) < %{guzzle_psr7_max_ver})
BuildRequires: (php-composer(phpseclib/phpseclib) >= %{phpseclib_min_ver} with php-composer(phpseclib/phpseclib) < %{phpseclib_max_ver})
BuildRequires: (php-composer(psr/cache) >= %{psr_cache_min_ver} with php-composer(psr/cache) < %{psr_cache_max_ver})
BuildRequires: (php-composer(psr/http-message) >= %{psr_http_message_min_ver} with php-composer(psr/http-message) < %{psr_http_message_max_ver})
%else
BuildRequires: php-composer(firebase/php-jwt) <  %{firebase_jwt_max_ver}
BuildRequires: php-composer(firebase/php-jwt) >= %{firebase_jwt_min_ver}
BuildRequires: php-composer(guzzlehttp/guzzle) <  %{guzzle_max_ver}
BuildRequires: php-composer(guzzlehttp/guzzle) >= %{guzzle_min_ver}
BuildRequires: php-composer(guzzlehttp/promises) <  %{guzzle_promises_max_ver}
BuildRequires: php-composer(guzzlehttp/promises) >= %{guzzle_promises_min_ver}
BuildRequires: php-composer(guzzlehttp/psr7) <  %{guzzle_psr7_max_ver}
BuildRequires: php-composer(guzzlehttp/psr7) >= %{guzzle_psr7_min_ver}
BuildRequires: php-composer(phpseclib/phpseclib) <  %{phpseclib_max_ver}
BuildRequires: php-composer(phpseclib/phpseclib) >= %{phpseclib_min_ver}
BuildRequires: php-composer(psr/cache) <  %{psr_cache_max_ver}
BuildRequires: php-composer(psr/cache) >= %{psr_cache_min_ver}
BuildRequires: php-composer(psr/http-message) <  %{psr_http_message_max_ver}
BuildRequires: php-composer(psr/http-message) >= %{psr_http_message_min_ver}
%endif
## phpcompatinfo (computed from version 1.5.1)
BuildRequires: php-date
BuildRequires: php-hash
BuildRequires: php-json
BuildRequires: php-openssl
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:     php(language) >= %{php_min_ver}
%if %{with_range_dependencies}
Requires:     (php-composer(firebase/php-jwt) >= %{firebase_jwt_min_ver} with php-composer(firebase/php-jwt) < %{firebase_jwt_max_ver})
Requires:     (php-composer(guzzlehttp/guzzle) >= %{guzzle_min_ver} with php-composer(guzzlehttp/guzzle) < %{guzzle_max_ver})
Requires:     (php-composer(guzzlehttp/psr7) >= %{guzzle_psr7_min_ver} with php-composer(guzzlehttp/psr7) < %{guzzle_psr7_max_ver})
Requires:     (php-composer(psr/cache) >= %{psr_cache_min_ver} with php-composer(psr/cache) < %{psr_cache_max_ver})
Requires:     (php-composer(psr/http-message) >= %{psr_http_message_min_ver} with php-composer(psr/http-message) < %{psr_http_message_max_ver})
%else
Requires:     php-composer(firebase/php-jwt) <  %{firebase_jwt_max_ver}
Requires:     php-composer(firebase/php-jwt) >= %{firebase_jwt_min_ver}
Requires:     php-composer(guzzlehttp/guzzle) <  %{guzzle_max_ver}
Requires:     php-composer(guzzlehttp/guzzle) >= %{guzzle_min_ver}
Requires:     php-composer(guzzlehttp/psr7) <  %{guzzle_psr7_max_ver}
Requires:     php-composer(guzzlehttp/psr7) >= %{guzzle_psr7_min_ver}
Requires:     php-composer(psr/cache) <  %{psr_cache_max_ver}
Requires:     php-composer(psr/cache) >= %{psr_cache_min_ver}
Requires:     php-composer(psr/http-message) <  %{psr_http_message_max_ver}
Requires:     php-composer(psr/http-message) >= %{psr_http_message_min_ver}
%endif
# phpcompatinfo (computed from version 1.5.1)
Requires:      php-date
Requires:      php-hash
Requires:      php-json
Requires:      php-openssl
Requires:      php-pcre
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Weak dependencies
## composer.json: optional
%if %{with_weak_dependencies}
Suggests:      php-composer(phpseclib/phpseclib)
%endif

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

Conflicts:     php-google-apiclient < 2

%description
This is Google's officially supported PHP client library for using OAuth 2.0
authorization and authentication with Google APIs.

Autoloader: %{phpdir}/Google/Auth/autoload.php


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

\Fedora\Autoloader\Autoload::addPsr4('Google\\Auth\\', __DIR__);

\Fedora\Autoloader\Dependencies::required([
    [
        '%{phpdir}/Firebase/JWT6/autoload.php',
        '%{phpdir}/Firebase/JWT/autoload.php',
    ],
    '%{phpdir}/GuzzleHttp/Psr7/autoload.php',
    [
        '%{phpdir}/GuzzleHttp7/autoload.php',
        '%{phpdir}/GuzzleHttp6/autoload.php',
    ],
    [
        '%{phpdir}/Psr/Cache3/autoload.php',
        '%{phpdir}/Psr/Cache2/autoload.php',
        '%{phpdir}/Psr/Cache/autoload.php',
    ],
    '%{phpdir}/Psr/Http/Message/autoload.php',
]);

\Fedora\Autoloader\Dependencies::optional([
    '%{phpdir}/phpseclib/autoload.php',
]);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/Google
cp -rp src %{buildroot}%{phpdir}/Google/Auth


%check
%if %{with tests}
: Create mock Composer autoloader
mkdir vendor
cat <<'BOOTSTRAP' | tee vendor/autoload.php
<?php

require_once '%{buildroot}%{phpdir}/Google/Auth/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Google\\Auth\\Tests\\', dirname(__DIR__).'/tests');

\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/GuzzleHttp/Promise/autoload.php',
]);
BOOTSTRAP

: Skip test known to fail in mock environment
rm -f tests/AccessTokenTest.php

: Skip test requiring network access
sed 's/function testMakeHttpClient/function SKIP_testMakeHttpClient/'\
    -i tests/FetchAuthTokenTest.php

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which %{phpunit_exec})
for PHP_EXEC in "" %{?rhel:php72 php73 php74} php80 php81 php82; do
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
%dir %{phpdir}/Google
     %{phpdir}/Google/Auth


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.23.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Oct 11 2022 Shawn Iwinski <shawn@iwin.ski> - 1.23.0-1
- Update to 1.23.0 (RHBZ #2068626)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Sep 18 2021 Shawn Iwinski <shawn@iwin.ski> - 1.18.0-1
- Update to 1.18.0 (RHBZ #1742186)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 17 2020 Remi Collet <remi@remirepo.net> - 1.5.1-5
- drop unneeded conflicts to allow installation of php-phpseclib3

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 2019 Shawn Iwinski <shawn@iwin.ski> - 1.5.1-1
- Update to 1.5.1 (RHBZ #1461830)
- Add range version dependencies for Fedora >= 27 || RHEL >= 8

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 11 2017 Shawn Iwinski <shawn@iwin.ski> - 0.11.1-1
- Initial package
