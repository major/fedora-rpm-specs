#
# Fedora spec file for php-goutte
#
# Copyright (c) 2014-2019 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner    FriendsOfPHP
%global github_name     Goutte
%global github_version  3.2.3
%global github_commit   3f0eaf0a40181359470651f1565b3e07e3dd31b8

%global composer_vendor  fabpot
%global composer_project goutte

# "php": ">=5.5.0"
%global php_min_ver 5.5.0
# "guzzlehttp/guzzle": "^6.0"
%global guzzle_min_ver 6.0
%global guzzle_max_ver 7.0
# "symfony/browser-kit": ~2.1|~3.0|~4.0
# "symfony/css-selector": ~2.1|~3.0|~4.0
# "symfony/dom-crawler": ~2.1|~3.0|~4.0
#     NOTE: Min version not 2.1 because autoloader required
%global symfony_min_ver 2.7.1
%global symfony_max_ver 5.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-goutte
Version:       %{github_version}
Release:       8%{?github_release}%{?dist}
Summary:       A simple PHP web scraper

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Tests
%if %{with_tests}
BuildRequires: php-composer(phpunit/phpunit)
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-composer(guzzlehttp/guzzle) >= %{guzzle_min_ver} with php-composer(guzzlehttp/guzzle) < %{guzzle_max_ver})
BuildRequires: (php-composer(symfony/browser-kit) >= %{symfony_min_ver} with php-composer(symfony/browser-kit) < %{symfony_max_ver})
BuildRequires: (php-composer(symfony/css-selector) >= %{symfony_min_ver} with php-composer(symfony/css-selector) < %{symfony_max_ver})
BuildRequires: (php-composer(symfony/dom-crawler) >= %{symfony_min_ver} with php-composer(symfony/dom-crawler) < %{symfony_max_ver})
%else
BuildRequires: php-composer(guzzlehttp/guzzle) <  %{guzzle_max_ver}
BuildRequires: php-composer(guzzlehttp/guzzle) >= %{guzzle_min_ver}
BuildRequires: php-composer(symfony/browser-kit) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/browser-kit) >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/css-selector) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/css-selector) >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/dom-crawler) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/dom-crawler) >= %{symfony_min_ver}
%endif
## phpcompatinfo (computed from version 3.2.3)
BuildRequires: php-reflection
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-composer(guzzlehttp/guzzle) >= %{guzzle_min_ver} with php-composer(guzzlehttp/guzzle) < %{guzzle_max_ver})
Requires:      (php-composer(symfony/browser-kit) >= %{symfony_min_ver} with php-composer(symfony/browser-kit) < %{symfony_max_ver})
Requires:      (php-composer(symfony/css-selector) >= %{symfony_min_ver} with php-composer(symfony/css-selector) < %{symfony_max_ver})
Requires:      (php-composer(symfony/dom-crawler) >= %{symfony_min_ver} with php-composer(symfony/dom-crawler) < %{symfony_max_ver})
%else
Requires:      php-composer(guzzlehttp/guzzle) <  %{guzzle_max_ver}
Requires:      php-composer(guzzlehttp/guzzle) >= %{guzzle_min_ver}
Requires:      php-composer(symfony/browser-kit) <  %{symfony_max_ver}
Requires:      php-composer(symfony/browser-kit) >= %{symfony_min_ver}
Requires:      php-composer(symfony/css-selector) <  %{symfony_max_ver}
Requires:      php-composer(symfony/css-selector) >= %{symfony_min_ver}
Requires:      php-composer(symfony/dom-crawler) <  %{symfony_max_ver}
Requires:      php-composer(symfony/dom-crawler) >= %{symfony_min_ver}
%endif
# phpcompatinfo (computed from version 3.2.3)
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Standard "php-{COMPOSER_VENDOR}-{COMPOSER_PROJECT}" naming
Provides:      php-%{composer_vendor}-%{composer_project} = %{version}-%{release}
# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Goutte is a screen scraping and web crawling library for PHP.

Goutte provides a nice API to crawl websites and extract data
from the HTML/XML responses.

Autoloader: %{phpdir}/Goutte/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
cat <<'AUTOLOAD' | tee Goutte/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Goutte\\', __DIR__);

\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/GuzzleHttp6/autoload.php',
    [
        '%{phpdir}/Symfony4/Component/BrowserKit/autoload.php',
        '%{phpdir}/Symfony3/Component/BrowserKit/autoload.php',
        '%{phpdir}/Symfony/Component/BrowserKit/autoload.php',
    ],
    [
        '%{phpdir}/Symfony4/Component/CssSelector/autoload.php',
        '%{phpdir}/Symfony3/Component/CssSelector/autoload.php',
        '%{phpdir}/Symfony/Component/CssSelector/autoload.php',
    ],
    [
        '%{phpdir}/Symfony4/Component/DomCrawler/autoload.php',
        '%{phpdir}/Symfony3/Component/DomCrawler/autoload.php',
        '%{phpdir}/Symfony/Component/DomCrawler/autoload.php',
    ],
]);
AUTOLOAD


%install
mkdir -p %{buildroot}/%{phpdir}/Goutte
cp -p Goutte/{autoload,Client}.php %{buildroot}/%{phpdir}/Goutte/


%check
%if %{with_tests}
: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in "" php56 php70 php71 php72 php73 php74; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose \
            --bootstrap %{buildroot}/%{phpdir}/Goutte/autoload.php \
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
%doc *.rst
%doc composer.json
%{phpdir}/Goutte


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 16 2019 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.2.3-1
- Update to 3.2.3 (RHBZ #1596940)
- Add range version dependencies for Fedora >= 27 || RHEL >= 8

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 13 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.2.2-1
- Update to 3.2.2 (RHBZ #1409941)
- Allow Symfony 4
- Remove patch

* Thu Sep 21 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.2.0-4
- Add max versions to BuildRequires
- Allow Symfony 3
- Modify tests

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 30 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.2.0-1
- Updated to 3.2.0 (RHBZ #1395456)
- Use php-composer(fedora/autoloader)
- Run upstream tests with SCLs if they are available

* Sat Jul 09 2016 Shawn Iwinski <shawn@iwin.ski> - 3.1.2-1
- Update to 3.1.2 (RHBZ #1100719, 1289798)

* Sun Jun 12 2016 Shawn Iwinski <shawn@iwin.ski> - 2.0.4-1
- Update to 2.0.4

* Mon Mar 28 2016 Shawn Iwinski <shawn@iwin.ski> - 1.0.7-3
- Fixed Guzzle min version for autoloader
- Added "php-{COMPOSER_VENDOR}-{COMPOSER_PROJECT}" virtual provide
- Added library version value and autoloader check

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 23 2015 Shawn Iwinski <shawn@iwin.ski> - 1.0.7-1
- Updated to 1.0.7
- Added spec file license header
- php-composer(*) dependencies
- Added php-composer(fabpot/goutte) virtual provide
- Added autoloader

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 16 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.6-1
- Updated to 1.0.6

* Wed Feb 19 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.5-1
- Updated to 1.0.5
- Conditional release dist
- Fixed %%files

* Mon Jan 27 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.3-1.20140118gite83f8f9
- Initial package
