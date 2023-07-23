#
# Fedora spec file for php-guzzlehttp-guzzle6
#
# Copyright (c) 2015-2022 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     guzzle
%global github_name      guzzle
%global github_version   6.5.8
%global github_commit    a52f0440530b54fa079ce76e8c5d196a42cad981

%global composer_vendor  guzzlehttp
%global composer_project guzzle

# "php": ">=5.5"
%global php_min_ver      5.5.0
# "guzzlehttp/promises": "^1.0"
%global promises_min_ver 1.0
%global promises_max_ver 2.0
# "guzzlehttp/psr7": "^1.9"
%global psr7_min_ver     1.9
%global psr7_max_ver     2.0
# "psr/log": "^1.1"
%global psr_log_min_ver  1.1
%global psr_log_max_ver  2.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

# Range dependencies supported?
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
%global with_range_dependencies 1
%else
%global with_range_dependencies 0
%endif

%{!?phpdir:    %global phpdir    %{_datadir}/php}
%{!?testsdir:  %global testsdir  %{_datadir}/tests}

Name:          php-%{composer_vendor}-%{composer_project}6
Version:       %{github_version}
Release:       4%{?github_release}%{?dist}
Summary:       PHP HTTP client library

License:       MIT
URL:           http://guzzlephp.org

# GitHub export does not include tests.
# Run php-guzzlehttp-guzzle6.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Library version value and autoloader check
BuildRequires: php-cli
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
%if %{with_range_dependencies}
BuildRequires: (php-composer(guzzlehttp/promises) >= %{promises_min_ver} with php-composer(guzzlehttp/promises) < %{promises_max_ver})
BuildRequires: (php-composer(guzzlehttp/psr7) >= %{psr7_min_ver} with php-composer(guzzlehttp/psr7) < %{psr7_max_ver})
BuildRequires: (php-composer(psr/log) >= %{psr_log_min_ver} with php-composer(psr/log) < %{psr_log_max_ver})
%else
BuildRequires: php-composer(guzzlehttp/promises) <  %{promises_max_ver}
BuildRequires: php-composer(guzzlehttp/promises) >= %{promises_min_ver}
BuildRequires: php-composer(guzzlehttp/psr7) <  %{psr7_max_ver}
BuildRequires: php-composer(guzzlehttp/psr7) >= %{psr7_min_ver}
BuildRequires: php-composer(psr/log) <  %{psr_log_max_ver}
BuildRequires: php-composer(psr/log) >= %{psr_log_min_ver}
%endif
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
# Tests
%if %{with_tests}
BuildRequires: nodejs
## composer.json
BuildRequires: php-curl
BuildRequires: php-json
BuildRequires: phpunit7
## phpcompatinfo (computed from version 6.5.2)
BuildRequires: php-date
BuildRequires: php-filter
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-spl
BuildRequires: php-zlib
# to avoid symfony/polyfill-intl-idn
BuildRequires: php-intl
%endif

Requires:      ca-certificates
# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-json
# composer.json: optional
Requires:      php-intl
%if %{with_range_dependencies}
# composer.json
Requires:      (php-composer(guzzlehttp/promises) >= %{promises_min_ver} with php-composer(guzzlehttp/promises) < %{promises_max_ver})
Requires:      (php-composer(guzzlehttp/psr7) >= %{psr7_min_ver} with php-composer(guzzlehttp/psr7) < %{psr7_max_ver})
# composer.json: optional
Requires:      (php-composer(psr/log) >= %{psr_log_min_ver} with php-composer(psr/log) < %{psr_log_max_ver})
%else
# composer.json
Requires:      php-composer(guzzlehttp/promises) <  %{promises_max_ver}
Requires:      php-composer(guzzlehttp/promises) >= %{promises_min_ver}
Requires:      php-composer(guzzlehttp/psr7) <  %{psr7_max_ver}
Requires:      php-composer(guzzlehttp/psr7) >= %{psr7_min_ver}
# composer.json: optional
Requires:      php-composer(psr/log) <  %{psr_log_max_ver}
Requires:      php-composer(psr/log) >= %{psr_log_min_ver}
%endif
# phpcompatinfo (computed from version 6.5.2)
Requires:      php-curl
Requires:      php-date
Requires:      php-filter
Requires:      php-pcre
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Guzzle is a PHP HTTP client that makes it easy to send HTTP requests and trivial
to integrate with web services.

* Simple interface for building query strings, POST requests, streaming large
  uploads, streaming large downloads, using HTTP cookies, uploading JSON data,
  etc...
* Can send both synchronous and asynchronous requests using the same interface.
* Uses PSR-7 interfaces for requests, responses, and streams. This allows you
  to utilize other PSR-7 compatible libraries with Guzzle.
* Abstracts away the underlying HTTP transport, allowing you to write
  environment and transport agnostic code; i.e., no hard dependency on cURL,
  PHP streams, sockets, or non-blocking event loops.
* Middleware system allows you to augment and compose client behavior.

Autoloader: %{phpdir}/GuzzleHttp6/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create common autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('GuzzleHttp\\', __DIR__);

\Fedora\Autoloader\Dependencies::required([
    __DIR__.'/functions_include.php',
    '%{phpdir}/GuzzleHttp/Promise/autoload.php',
    '%{phpdir}/GuzzleHttp/Psr7/autoload.php',
    '%{phpdir}/Psr/Log/autoload.php',
]);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}
cp -pr src %{buildroot}%{phpdir}/GuzzleHttp6


%check
: Autoloader check
%{_bindir}/php -r '
    require_once "%{buildroot}%{phpdir}/GuzzleHttp6/autoload.php";
    exit(interface_exists("\\GuzzleHttp\\ClientInterface") ? 0 : 1);
'

%if %{with_tests}
: Create mock Composer autoloader
mkdir vendor
cat <<'AUTOLOAD' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{phpdir}/GuzzleHttp6/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('GuzzleHttp\\Tests\\', __DIR__.'/tests');
AUTOLOAD

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit7)
for PHP_EXEC in php php74 php80 php81 php82; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then

        VER=$($PHP_EXEC -r 'echo PHP_VERSION_ID;')
        FILTER="testDescribesType|testInvokesOnStatsOnError|testAddsCookiesWithEmptyPathFromResponse|testCreatesExceptionWithoutPrintableBody"
        if [ $VER -ge 80000 ]; then
          # CurlHandle Object instead of resource
          FILTER="$FILTER|testEmitsProgressToFunction|testCreatesCurlHandle"
        fi

        $PHP_EXEC $PHPUNIT \
          --filter "^((?!($FILTER)).)*$" \
          --verbose || RETURN_CODE=1
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
%{phpdir}/GuzzleHttp6


%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 22 2022 Remi Collet <remi@remirepo.net> - 6.5.8-1
- update to 6.5.8
- raise dependency on guzzlehttp/psr7 1.9

* Mon Jun 13 2022 Remi Collet <remi@remirepo.net> - 6.5.7-1
- update to 6.5.7

* Mon May 30 2022 Remi Collet <remi@remirepo.net> - 6.5.6-1
- update to 6.5.6

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Apr  1 2021 Remi Collet <remi@remirepo.net> - 6.5.5-1
- update to 6.5.5

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 26 2019 Shawn Iwinski <shawn@iwin.ski> - 6.5.2-1
- Update to 6.5.2 (RHBZ #1764727)
- Remove version check and only do autoloader check b/c
  `\GuzzleHttp\ClientInterface::VERSION` is
  `@deprecated Will be removed in Guzzle 7.0.0`

* Tue Dec 17 2019 Shawn Iwinski <shawn@iwin.ski> - 6.5.0-1
- Update to 6.5.0 (RHBZ #1764727)
- Use PHPUnit 7

* Sun Sep 08 2019 Shawn Iwinski <shawn@iwin.ski> - 6.3.3-6
- Fix FTBFS (RHBZ #1736433)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Remi Collet <remi@remirepo.net> - 6.3.3-3
- skip 1 failed test

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 23 2018 Shawn Iwinski <shawn@iwin.ski> - 6.3.3-1
- Update to 6.3.3 (RHBZ #1560991)
- Update get source script to save source in same directory
- Add range version dependencies for Fedora >= 27 || RHEL >= 8
- Add composer.json to repo

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Shawn Iwinski <shawn@iwin.ski> - 6.3.0-3
- Fix %%check to fail when upstream tests fail

* Wed Jul 05 2017 Shawn Iwinski <shawn@iwin.ski> - 6.3.0-2
- Add patch to fix version
- Add check for version and run whether tests are skipped or not

* Fri Jun 23 2017 Shawn Iwinski <shawn@iwin.ski> - 6.3.0-1
- Update to 6.3.0 (RHBZ #1464283)
- Remove patch

* Fri Apr 07 2017 Shawn Iwinski <shawn@iwin.ski> - 6.2.3-1
- Update to 6.2.3
- Fix rawhide (F27) FTBS
- Add max versions to BuildRequires
- Switch autoloader to php-composer(fedora/autoloader)
- Test with SCLs if available

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Oct 09 2016 Shawn Iwinski <shawn@iwin.ski> - 6.2.2-1
- Update to 6.2.2 (RHBZ #1383050)

* Mon Jul 18 2016 Shawn Iwinski <shawn@iwin.ski> - 6.2.1-1
- Update to 6.2.1 (RHBZ #1357582 / CVE-2016-5385)
- Removed "Fix failing test" patch

* Sun May 29 2016 Shawn Iwinski <shawn@iwin.ski> - 6.2.0-3
- Fix failing test

* Fri Apr 08 2016 Shawn Iwinski <shawn@iwin.ski> - 6.2.0-2
- Prepend PSR-4 autoloader (fixes dual-install issue with
  php-guzzlehttp-guzzle when other packages register PSR-0
  autoloader first usually with include path failover)

* Sun Mar 27 2016 Shawn Iwinski <shawn@iwin.ski> - 6.2.0-1
- Updated to 6.2.0 (RHBZ #1319960)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Shawn Iwinski <shawn@iwin.ski> - 6.1.1-2
- Added min version of autoloader dependency
- Fix directory ownership

* Sun Dec 06 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 6.1.1-1
- Renamed from php-guzzlehttp-guzzle to php-guzzlehttp-guzzle6 for
  dual-install of version 5 and version 6
- Updated to 6.1.1

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
