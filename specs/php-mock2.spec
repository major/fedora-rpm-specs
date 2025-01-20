# remirepo/fedora spec file for php-mock2
#
# SPDX-FileCopyrightText:  Copyright 2016-2024 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#
%global gh_commit    8f58972dce4de5a804dc0459383a11bc651416cf
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_date      2024-12-09
%global gh_owner     php-mock
%global gh_project   php-mock
%global with_tests   0%{!?_without_tests:1}
%global major        2

Name:           php-mock%{major}
Version:        2.5.1
Release:        2%{?dist}
Summary:        PHP-Mock can mock built-in PHP functions

License:        WTFPL
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
# 7.4 because of phpunit9
BuildRequires:  php(language) >= 7.4
%if %{with_tests}
# from composer.json, "require-dev": {
#        "phpunit/phpunit": "^5.7 || ^6.5 || ^7.5 || ^8.0 || ^9.0 || ^10.0|| ^11.0",
#        "squizlabs/php_codesniffer": "^3.5"
BuildRequires: phpunit8
BuildRequires: phpunit9
BuildRequires: phpunit10
# TODO phpunit11 but requires php 8.2
%endif
# For autoloader
BuildRequires: php-composer(fedora/autoloader)

# from composer.json, "require": {
#        "php": "^5.6 || ^7.0 || ^8.0",
#        "phpunit/php-text-template": "^1 || ^2 || ^3 || ^4")
Requires:       php(language) >= 5.6
Requires:      (php-composer(phpunit/php-text-template) >= 1   with php-composer(phpunit/php-text-template) < 5)
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
if (PHP_VERSION_ID >= 80200) {
	$deps = [
        '%{_datadir}/php/SebastianBergmann/Template4/autoload.php',
        '%{_datadir}/php/SebastianBergmann/Template3/autoload.php',
        '%{_datadir}/php/SebastianBergmann/Template2/autoload.php',
        '%{_datadir}/php/Text/Template/Autoload.php',
    ];
} else {
	$deps = [
        '%{_datadir}/php/SebastianBergmann/Template3/autoload.php',
        '%{_datadir}/php/SebastianBergmann/Template2/autoload.php',
        '%{_datadir}/php/Text/Template/Autoload.php',
    ];
}
\Fedora\Autoloader\Dependencies::required([
	$deps,
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

if [ -x %{_bindir}/phpunit8 ]; then
	for cmd in php php80 php81 php82;do
	  if which $cmd; then
		$cmd %{_bindir}/phpunit8 \
		  --filter '^((?!(testDefiningAfterCallingUnqualified|testEnable)).)*$' \
		  --bootstrap %{buildroot}%{_datadir}/tests/phpmock2/autoload.php --verbose rpm/tests || ret=1
	  fi
	done
fi

if [ -x %{_bindir}/phpunit9 ]; then
	for cmd in php php80 php81 php82 php83 php84;do
	  if which $cmd; then
		$cmd %{_bindir}/phpunit9 \
		  --filter '^((?!(testDefiningAfterCallingUnqualified|testEnable)).)*$' \
		  --bootstrap %{buildroot}%{_datadir}/tests/phpmock2/autoload.php --verbose rpm/tests || ret=1
	  fi
	done
fi

if [ -x %{_bindir}/phpunit10 ]; then
	for cmd in php php81 php82 php83 php84;do
	  if which $cmd; then
		$cmd %{_bindir}/phpunit10 \
		  --filter '^((?!(testDefiningAfterCallingUnqualified|testEnable)).)*$' \
		  --bootstrap %{buildroot}%{_datadir}/tests/phpmock2/autoload.php rpm/tests || ret=1
	  fi
	done
fi

if [ -x %{_bindir}/phpunit11 ]; then
	for cmd in php  php82 php83 php84;do
	  if which $cmd; then
		$cmd %{_bindir}/phpunit11 \
		  --filter '^((?!(testDefiningAfterCallingUnqualified|testEnable)).)*$' \
		  --bootstrap %{buildroot}%{_datadir}/tests/phpmock2/autoload.php rpm/tests || ret=1
	  fi
	done
fi
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
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Dec  9 2024 Remi Collet <remi@remirepo.net> - 2.5.1-1
- update to 2.5.1
- re-license spec file to CECILL-2.1

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Feb 12 2024 Remi Collet <remi@remirepo.net> - 2.5.0-1
- update to 2.5.0
- allow phpunit10

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Remi Collet <remi@remirepo.net> - 2.4.1-1
- update to 2.4.1 (no change)

* Mon Feb 13 2023 Remi Collet <remi@remirepo.net> - 2.4.0-1
- update to 2.4.0
- allow phpunit10

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

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
