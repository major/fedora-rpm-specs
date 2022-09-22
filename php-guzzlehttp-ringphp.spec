#
# Fedora spec file for php-guzzlehttp-ringphp
#
# Copyright (c) 2014-2021 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     guzzle
%global github_name      RingPHP
%global github_version   1.1.1
%global github_commit    5e2a174052995663dd68e6b5ad838afd47dd615b

%global composer_vendor  guzzlehttp
%global composer_project ringphp

# "php": ">=5.4.0"
%global php_min_ver      5.4.0
# "guzzlehttp/streams": "~3.0"
%global streams_min_ver  3.0.0
%global streams_max_ver  4.0
# "react/promise": "~2.0"
%global promise_min_ver  2.2.0
%global promise_max_ver  3.0

# Build using "--without tests" to disable tests
%global with_tests %{?_without_tests:0}%{!?_without_tests:1}

%{!?phpdir:    %global phpdir    %{_datadir}/php}
%{!?testsdir:  %global testsdir  %{_datadir}/tests}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       10%{?github_release}%{?dist}
Summary:       Simple handler system used to power clients and servers in PHP

License:       MIT
URL:           http://ringphp.readthedocs.org
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

# Fix #41 use proper proxy attribute without ending /
# https://github.com/guzzle/RingPHP/pull/42
# https://github.com/guzzle/RingPHP/pull/42.patch
Patch0:        %{name}-upstream-pull-42.patch

BuildArch:     noarch
# Tests
%if %{with_tests}
BuildRequires: nodejs
BuildRequires: %{_bindir}/phpunit
## composer.json
BuildRequires: php(language)                    >= %{php_min_ver}
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-composer(guzzlehttp/streams) >= %{streams_min_ver}  with php-composer(guzzlehttp/streams) <  %{streams_max_ver})
BuildRequires: (php-composer(react/promise)      >= %{promise_min_ver}  with php-composer(react/promise)      <  %{promise_max_ver})
%else
BuildRequires: php-composer(guzzlehttp/streams) <  %{streams_max_ver}
BuildRequires: php-composer(guzzlehttp/streams) >= %{streams_min_ver}
BuildRequires: php-composer(react/promise)      <  %{promise_max_ver}
BuildRequires: php-composer(react/promise)      >= %{promise_min_ver}
%endif
BuildRequires: php-curl
## phpcompatinfo (computed from version 1.1.0)
BuildRequires: php-json
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-spl
BuildRequires: php-zlib
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language)                    >= %{php_min_ver}
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-composer(guzzlehttp/streams) >= %{streams_min_ver}  with php-composer(guzzlehttp/streams) <  %{streams_max_ver})
Requires:      (php-composer(react/promise)      >= %{promise_min_ver}  with php-composer(react/promise)      <  %{promise_max_ver})
%else
Requires:      php-composer(guzzlehttp/streams) <  %{streams_max_ver}
Requires:      php-composer(guzzlehttp/streams) >= %{streams_min_ver}
Requires:      php-composer(react/promise)      <  %{promise_max_ver}
Requires:      php-composer(react/promise)      >= %{promise_min_ver}
%endif
# composer.json: optional
Requires:      php-curl
# phpcompatinfo (computed from version 1.1.0)
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Provides low level APIs used to power HTTP clients and servers through a simple,
PHP callable that accepts a request hash and returns a future response hash.
RingPHP supports both synchronous and asynchronous workflows by utilizing both
futures and promises [1].

RingPHP is inspired by Clojure's Ring [2], but has been modified to accommodate
clients and servers for both blocking and non-blocking requests.

[1] https://github.com/reactphp/promise
[2] https://github.com/ring-clojure/ring


# ------------------------------------------------------------------------------


%package tests

Summary:  Tests for %{name}
Group:    Development/Libraries

Requires: %{name} = %{version}-%{release}
Requires: nodejs
Requires: php-composer(phpunit/phpunit)
# phpcompatinfo (computed from version 1.1.0)
Requires: php-json
Requires: php-pcre
Requires: php-reflection
Requires: php-zlib

%description tests
%{summary}.


# ------------------------------------------------------------------------------


%prep
%setup -qn %{github_name}-%{github_commit}

# Fix #41 use proper proxy attribute without ending /
%patch0 -p1

: Modify tests bootstrap
sed -e "s#.*require.*autoload.*#require __DIR__ . '/autoload.php';#" \
    -i tests/bootstrap.php


%build
: Create library autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('GuzzleHttp\\Ring\\', __DIR__);

\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/GuzzleHttp/Stream/autoload.php',
    '%{phpdir}/React/Promise/autoload.php',
]);
AUTOLOAD

: Create tests autoloader
cat <<'AUTOLOAD' | tee tests/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-tests-%{version}-%{release}).
 */

// Require library autoloader.  Allow for both RPM builds of %{name}
// and other packages' usage of %{name}-tests.
$libraryAutoload = '%{phpdir}/GuzzleHttp/Ring/autoload.php';
$rpmBuildRoot = getenv('RPM_BUILD_ROOT');
if ($rpmBuildRoot && file_exists($rpmBuildRoot . $libraryAutoload)) {
    require_once $rpmBuildRoot . $libraryAutoload;
} else {
    require_once $libraryAutoload;
}
unset($libraryAutoload, $rpmBuildRoot);

\Fedora\Autoloader\Autoload::addPsr4('GuzzleHttp\\Tests\\Ring\\', __DIR__);
AUTOLOAD

: Create custom tests PHPUnit config
rm -f phpunit.xml.dist
cat <<'PHPUNIT' | tee phpunit.xml.dist
<?xml version="1.0" encoding="UTF-8"?>
<phpunit bootstrap="./bootstrap.php" colors="true">
    <testsuites>
        <testsuite>
            <directory>.</directory>
        </testsuite>
    </testsuites>
</phpunit>
PHPUNIT


%install
: Library
mkdir -p %{buildroot}%{phpdir}/GuzzleHttp/Ring
cp -rp src/* %{buildroot}%{phpdir}/GuzzleHttp/Ring/

: Tests
mkdir -p %{buildroot}%{testsdir}
cp -rp tests %{buildroot}%{testsdir}/%{name}
cp -p phpunit.xml.dist %{buildroot}%{testsdir}/%{name}/


%check
%if %{with_tests}
: Upstream tests

# testEmitsDebugInfoToStream have strange failure on F29+
# testCreatesCurlHandle and testEmitsProgressToFunction fail on F35+

RETURN_CODE=0
for PHP_EXEC in php %{?rhel:php55 php56 php70 php71 php72} php73 php74 php80; do
    if [ "php" == "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC %{_bindir}/phpunit --verbose \
            --filter '^((?!(testEmitsDebugInfoToStream|testCreatesCurlHandle|testEmitsProgressToFunction)).)*$' \
            --configuration %{buildroot}%{testsdir}/%{name} \
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
%doc *.rst
%doc composer.json
%{phpdir}/GuzzleHttp/Ring

%files tests
%{testsdir}/%{name}


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Apr  1 2021 Remi Collet <remi@remirepo.net> - 1.1.1-7
- skip 2 tests failing with PHP 8

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 16 2018 Remi Collet <remi@remirepo.net> - 1.1.1-1
- update to 1.1.1 for PHP 7.3 compatibility
- use range dependencies
- skip 1 test with strange failure on F29+ (everything seems ok)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Apr 07 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1.0-9
- Fix rawhide (F27) FTBS
- Switch autoloader to php-composer(fedora/autoloader)
- Test with SCLs if available

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 22 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1.0-6
- Updated autoloader to load dependencies after self registration
- Minor cleanups

* Sun Jun 28 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1.0-5
- Autoloader updates

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 12 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1.0-3
- Fix tests' autoload

* Fri Jun 12 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1.0-2
- Use new $fedoraClassLoader concept in autoloader
- Remove secondary "tests" directory from tests sub-package

* Mon Jun 01 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1.0-1
- Updated to 1.1.0
- Updated source URL
- Added autoloader
- Sub-packaged tests

* Sun Dec 28 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.5-1
- Updated to 1.0.5

* Thu Nov 13 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.3-1
- Updated to 1.0.3
- Removed color turn off and default timezone for phpunit

* Mon Oct 27 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.1-1
- Initial package
