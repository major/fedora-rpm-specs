# remirepo/fedora spec file for php-mock2
#
# Copyright (c) 2016-2022 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    9a55bd8ba40e6da2e97a866121d2c69dedd4952b
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     php-mock
%global gh_project   php-mock
%global with_tests   0%{!?_without_tests:1}
%global major        2

Name:           php-mock%{major}
Version:        2.3.1
Release:        2%{?dist}
Summary:        PHP-Mock can mock built-in PHP functions

License:        WTFPL
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
BuildRequires:  php(language) >= 5.6
%if %{with_tests}
# from composer.json, "require-dev": {
#        "phpunit/phpunit": "^5.7 || ^6.5 || ^7.5 || ^8.0 || ^9.0",
#        "squizlabs/php_codesniffer": "^3.5"
BuildRequires: (php-composer(phpunit/php-text-template) >= 1   with php-composer(phpunit/php-text-template) < 3)
BuildRequires: phpunit9
%global phpunit %{_bindir}/phpunit9
%endif
# For autoloader
BuildRequires: php-composer(fedora/autoloader)

# from composer.json, "require": {
#        "php": "^5.6 || ^7.0 || ^8.0",
#        "phpunit/php-text-template": "^1"
Requires:       php(language) >= 5.6
Requires:      (php-composer(phpunit/php-text-template) >= 1   with php-composer(phpunit/php-text-template) < 3)
# From phpcompatinfo report from version 2.0.0
Requires:       php-date
Requires:       php-reflection
Requires:       php-spl
# For autoloader
Requires:       php-composer(fedora/autoloader)
# from composer.json, "suggest": {
#       "php-mock/php-mock-phpunit": "Allows integration into PHPUnit testcase with the trait PHPMock."
Suggests:       php-composer(php-mock/php-mock-phpunit)

Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}


%description
PHP-Mock can mock built-in PHP functions (e.g. time()).
PHP-Mock relies on PHP's namespace fallback policy.
No further extension is needed.

Autoloader: %{_datadir}/php/phpmock%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

: Prepare the layout
mv tests/autoload.php testload.php
mkdir -p rpm/tests rpm/php
mv classes rpm/php/phpmock%{major}
mv tests   rpm/tests/phpmock%{major}

: Create autoloader
cat << 'AUTOLOAD' | tee rpm/php/phpmock%{major}/autoload.php
<?php
/* Autoloader for %{name} and its dependencies */
require_once '%{_datadir}/php/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('phpmock\\', __DIR__);
\Fedora\Autoloader\Autoload::addPsr4('phpmock\\', dirname(dirname(__DIR__)) . '/tests/phpmock%{major}');
\Fedora\Autoloader\Dependencies::required([
    [
        '%{_datadir}/php/SebastianBergmann/Template2/autoload.php',
        '%{_datadir}/php/Text/Template/Autoload.php',
    ]
]);
AUTOLOAD
grep -v '<?php' autoload.php >>rpm/php/phpmock%{major}/autoload.php
grep -v '<?php' testload.php >>rpm/php/phpmock%{major}/autoload.php

ln -s ../../php/phpmock%{major}/autoload.php rpm/tests/phpmock%{major}/autoload.php

: Fix autoloader path
sed -e 's:../autoload.php:autoload.php:' \
    -i rpm/tests/phpmock2/AbstractMockTest.php&


%build
# Nothing


%install
# Library
mkdir -p         %{buildroot}%{_datadir}
cp -pr rpm/php   %{buildroot}%{_datadir}/php
cp -pr rpm/tests %{buildroot}%{_datadir}/tests


%check
%if %{with_tests}
ret=0
# testDefiningAfterCallingUnqualified and testEnable may fail locally (ok in mock)

for cmdarg in "php %{phpunit}" php74 php80 php81;do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit9} \
      --filter '^((?!(testDefiningAfterCallingUnqualified|testEnable)).)*$' \
      --bootstrap %{buildroot}%{_datadir}/tests/phpmock2/autoload.php --verbose rpm/tests || ret=1
  fi
done
exit $ret
%else
: bootstrap build with test suite disabled
%endif


%files
%license LICENSE
%doc composer.json
%doc *.md
%{_datadir}/php/phpmock%{major}
%{_datadir}/tests/phpmock%{major}


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Feb  8 2022 Remi Collet <remi@remirepo.net> - 2.3.1-1
- update to 2.3.1

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 14 2020 Remi Collet <remi@remirepo.net> - 2.3.0-1
- update to 2.3.0
- switch to phpunit9

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 20 2020 Remi Collet <remi@remirepo.net> - 2.2.2-1
- update to 2.2.2

* Mon Feb 10 2020 Remi Collet <remi@remirepo.net> - 2.2.1-1
- update to 2.2.1
- allow phpunit9 and phpunit/php-text-template v2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun  6 2019 Remi Collet <remi@remirepo.net> - 2.1.2-1
- update to 2.1.2

* Mon Apr  8 2019 Remi Collet <remi@remirepo.net> - 2.1.1-1
- update to 2.1.1

* Thu Mar  7 2019 Remi Collet <remi@remirepo.net> - 2.1.0-2
- update to 2.1.0
- single autoloader

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 23 2018 Remi Collet <remi@remirepo.net> - 2.0.0-2
- use range dependencies on F27+

* Tue Dec  5 2017 Remi Collet <remi@remirepo.net> - 2.0.0-1
- rename to php-mock2
- Update to 2.0.0
- raise dependency on PHP 5.6

* Thu May 11 2017 Remi Collet <remi@remirepo.net> - 1.0.1-4
- switch to fedora/autoloader

* Mon Feb 22 2016 Remi Collet <remi@fedoraproject.org> - 1.0.1-2
- Fix: license is WTFPL, from review #1306968

* Fri Feb 12 2016 Remi Collet <remi@fedoraproject.org> - 1.0.1-1
- initial package
