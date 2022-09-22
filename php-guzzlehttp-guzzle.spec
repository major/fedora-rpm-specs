#
# Fedora spec file for php-guzzlehttp-guzzle
#
# Copyright (c) 2014-2021 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     guzzle
%global github_name      guzzle
%global github_version   5.3.4
%global github_commit    b87eda7a7162f95574032da17e9323c9899cb6b2

%global composer_vendor  guzzlehttp
%global composer_project guzzle

# "php": ">=5.4.0"
%global php_min_ver 5.4.0
# "guzzlehttp/ringphp": "^1.1"
#     Note: Min version not "1.1" because autoloader required
%global ring_min_ver 1.1.1
%global ring_max_ver 2.0
# "react/promise": "^2.2"
%global react_promise_min_ver 2.2
%global react_promise_max_ver 3.0

# Build using "--without tests" to disable tests
%bcond_without tests

%{!?phpdir:    %global phpdir    %{_datadir}/php}
%{!?testsdir:  %global testsdir  %{_datadir}/tests}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       8%{?github_release}%{?dist}
Summary:       PHP HTTP client and webservice framework

License:       MIT
URL:           http://guzzlephp.org

# GitHub export does not include tests.
# Run php-guzzlehttp-guzzle.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with tests}
BuildRequires: nodejs
BuildRequires: php-composer(phpunit/phpunit)
BuildRequires: php-guzzlehttp-ringphp-tests
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-composer(guzzlehttp/ringphp) >= %{ring_min_ver} with php-composer(guzzlehttp/ringphp) < %{ring_max_ver})
BuildRequires: (php-composer(react/promise) >= %{react_promise_min_ver} with php-composer(react/promise) < %{react_promise_max_ver})
%else
BuildRequires: php-composer(guzzlehttp/ringphp) <  %{ring_max_ver}
BuildRequires: php-composer(guzzlehttp/ringphp) >= %{ring_min_ver}
BuildRequires: php-composer(react/promise) <  %{react_promise_max_ver}
BuildRequires: php-composer(react/promise) >= %{react_promise_min_ver}
%endif
## phpcompatinfo (computed from version 5.3.2)
BuildRequires: php-curl
BuildRequires: php-date
BuildRequires: php-filter
BuildRequires: php-json
BuildRequires: php-libxml
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-simplexml
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

Requires:      ca-certificates
# composer.json
Requires:      php(language) >= %{php_min_ver}
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-composer(guzzlehttp/ringphp) >= %{ring_min_ver} with php-composer(guzzlehttp/ringphp) < %{ring_max_ver})
Requires:      (php-composer(react/promise) >= %{react_promise_min_ver} with php-composer(react/promise) < %{react_promise_max_ver})
%else
Requires:      php-composer(guzzlehttp/ringphp) >= %{ring_min_ver}
Requires:      php-composer(guzzlehttp/ringphp) <  %{ring_max_ver}
Requires:      php-composer(react/promise) <  %{react_promise_max_ver}
Requires:      php-composer(react/promise) >= %{react_promise_min_ver}
%endif
# phpcompatinfo (computed from version 5.3.2)
Requires:      php-curl
Requires:      php-date
Requires:      php-filter
Requires:      php-json
Requires:      php-libxml
Requires:      php-pcre
Requires:      php-simplexml
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Guzzle is a PHP HTTP client that makes it easy to work with HTTP/1.1 and takes
the pain out of consuming web services.

* Pluggable HTTP adapters that can send requests serially or in parallel
* Doesn't require cURL, but uses cURL by default
* Streams data for both uploads and downloads
* Provides event hooks & plugins for cookies, caching, logging, OAuth, mocks,
  etc
* Keep-Alive & connection pooling
* SSL Verification
* Automatic decompression of response bodies
* Streaming multipart file uploads
* Connection timeouts

Autoloader: %{phpdir}/GuzzleHttp/autoload.php


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

\Fedora\Autoloader\Autoload::addPsr4('GuzzleHttp\\', __DIR__);

\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/GuzzleHttp/Ring/autoload.php',
    '%{phpdir}/React/Promise/autoload.php',
));
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}
cp -pr src %{buildroot}%{phpdir}/GuzzleHttp


%check
%if %{with tests}
: Create tests autoloader
cat <<'AUTOLOAD' | tee tests/autoload.php
<?php
require '%{buildroot}%{phpdir}/GuzzleHttp/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('GuzzleHttp\\Tests', __DIR__);
AUTOLOAD

: Modify tests bootstrap
sed -e "s#.*require.*autoload.*#require __DIR__ . '/autoload.php';#" \
    -e "s#.*require.*Server.php.*#require '%{testsdir}/php-guzzlehttp-ringphp/autoload.php';#" \
    -i tests/bootstrap.php

: Skip tests known to fail
sed 's/function testEnsuresResponseIsPresentAfterSending/function SKIP_testEnsuresResponseIsPresentAfterSending/' \
    -i tests/ClientTest.php

: Skip flakey test in mock/rpmbuild environment
sed 's/function testCookiesAreExtractedFromRedirectResponses/function SKIP_testCookiesAreExtractedFromRedirectResponses/' \
    -i tests/Subscriber/CookieTest.php

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in "" %{?rhel:php55 php56 php70 php71 php72 php73 php74} php80 php81; do
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
%{phpdir}/GuzzleHttp/*


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Sep 18 2021 Shawn Iwinski <shawn.iwinski@gmail.com> - 5.3.4-6
- Fix "FTBFS in Fedora rawhide/f35" (RHBZ #1987816)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 01 2019 Shawn Iwinski <shawn.iwinski@gmail.com> - 5.3.4-1
- Update to 5.3.4 (RHBZ #1766925)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 16 2018 Remi Collet <remi@remirepo.net> - 5.3.3-1
- update to 5.3.3 for PHP 7.3 compatibility

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 23 2018 Remi Collet <remi@remirepo.net> - 5.3.2-2
- fix dependencies

* Sun Apr 22 2018 Shawn Iwinski <shawn.iwinski@gmail.com> - 5.3.2-1
- Update to 5.3.2 (RHBZ #1534517)
- Update get source script to save source in same directory
- Add range version dependencies for Fedora >= 27 || RHEL >= 8
- Add composer.json to repo
- Remove test skips

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun May 14 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 5.3.1-3
- Switch autoloader to php-composer(fedora/autoloader)
- Add max versions to build dependencies
- Test with SCLs if available

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jul 18 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 5.3.1-1
- Update to 5.3.1 (RHBZ #1350616 / RHBZ #1357580 / CVE-2016-5385)
- Add "get source" script

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 22 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 5.3.0-4
- Updated autoloader to load dependencies after self registration
- Minor cleanups

* Sun Jun 28 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 5.3.0-3
- Autoloader updates

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 14 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 5.3.0-1
- Updated to 5.3.0 (BZ #1140134)
- Added autoloader
- Re-added tests

* Sun Feb 08 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 5.1.0-1
- Updated to 5.1.0 (BZ #1140134)
- CA cert no longer bundled (see
  https://github.com/guzzle/guzzle/blob/5.1.0/docs/clients.rst#verify)
- No tests because dependency package does not provide required test file

* Mon Jan 12 2015 Remi Collet <remi@fedoraproject.org> - 4.1.8-3
- Upstream patch for PHP behavior change, thanks Koschei

* Tue Aug 26 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 4.1.8-2
- Fix test suite when previous version installed

* Sat Aug 23 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 4.1.8-1
- Updated to 4.1.8 (BZ #1126611)

* Wed Jul 30 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 4.1.4-1
- Updated to 4.1.4 (BZ #1124226)
- Added %%license usage

* Sun Jun 29 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 4.1.2-1
- Updated to 4.1.2

* Fri Jun 06 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 4.1.0-1
- Updated to 4.1.0
- Require php-composer virtual provides instead of direct pkgs
- Added php-PsrLog and nodejs build requires
- Added php-composer(%%{composer_vendor}/%%{composer_project}) virtual provide
- Added option to build without tests

* Fri May 23 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 4.0.2-1
- Initial package
