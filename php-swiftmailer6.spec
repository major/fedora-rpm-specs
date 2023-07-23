# remirepo/fedora spec file for php-swiftmailer6
#
# Copyright (c) 2016-2021 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please preserve changelog entries
#

%bcond_without       tests

%global gh_commit    8a5d5072dca8f48460fce2f4131fcc495eec654c
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     swiftmailer
%global gh_project   swiftmailer
# don't change major version used in package name
%global major        6
%global php_home     %{_datadir}/php

Name:           php-%{gh_project}%{major}
Version:        6.3.0
Release:        5%{?dist}
Summary:        Free Feature-rich PHP Mailer

License:        MIT
URL:            https://swiftmailer.symfony.com/
# git snapshot to retrieve test suite
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
%if %{with tests}
BuildRequires:  php(language) >= 7.0.0
BuildRequires: (php-composer(egulias/email-validator) >= 2.0  with php-composer(egulias/email-validator) <  4)
BuildRequires:  php-intl
BuildRequires:  php-reflection
BuildRequires:  php-simplexml
BuildRequires:  php-bcmath
BuildRequires:  php-date
BuildRequires:  php-filter
BuildRequires:  php-hash
BuildRequires:  php-iconv
BuildRequires:  php-mbstring
BuildRequires:  php-mhash
BuildRequires:  php-openssl
BuildRequires:  php-pcre
BuildRequires:  php-spl
# From composer.json, "require-dev": {
#        "mockery/mockery": "^1.0",
#        "symfony/phpunit-bridge": "^4.4|^5.4	"
BuildRequires: (php-composer(mockery/mockery)        >= 1.0    with php-composer(mockery/mockery)        < 2)
#BuildRequires:(php-composer(symfony/phpunit-bridge) >= 4.4    with php-composer(symfony/phpunit-bridge) < 5)
%global phpunit %{_bindir}/phpunit9
BuildRequires:  %{phpunit}
%endif
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require": {
#        "php": ">=7.0.0",
#        "egulias/email-validator": "^2.0|^3.1",
#        "symfony/polyfill-iconv": "^1.0",
#        "symfony/polyfill-mbstring": "^1.0",
#        "symfony/polyfill-intl-idn": "^1.10"
Requires:       php(language) >= 7.0.0
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-composer(egulias/email-validator) >= 2.0  with php-composer(egulias/email-validator) <  4)
%endif
# From composer.json,     "suggest": {
#        "ext-intl": "Needed to support internationalized email addresses"
Requires:       php-intl
# from phpcompatinfo report on version 6.2.0
Requires:       php-reflection
Requires:       php-simplexml
Requires:       php-bcmath
Requires:       php-date
Requires:       php-filter
Requires:       php-hash
Requires:       php-iconv
Requires:       php-mbstring
Requires:       php-mhash
Requires:       php-openssl
Requires:       php-pcre
Requires:       php-spl

Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}


%description
Swift Mailer integrates into any web app written in PHP, offering a 
flexible and elegant object-oriented approach to sending emails with 
a multitude of features.

Autoloader: %{php_home}/Swift%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

cat << 'EOF' | tee lib/autoload.php
<?php
/* Autoloader for %{name} and its' dependencies */
if (file_exists('%{php_home}/Egulias/EmailValidator3/autoload.php')) {
   require_once '%{php_home}/Egulias/EmailValidator3/autoload.php';
} else {
   require_once '%{php_home}/Egulias/EmailValidator2/autoload.php';
}
require_once __DIR__ . '/swift_required.php';
EOF


%build
# Empty build section, most likely nothing required.


%install
mkdir -p                   %{buildroot}/%{php_home}/Swift%{major}
cp -p  lib/*.php           %{buildroot}/%{php_home}/Swift%{major}/
cp -pr lib/classes         %{buildroot}/%{php_home}/Swift%{major}/
cp -pr lib/dependency_maps %{buildroot}/%{php_home}/Swift%{major}/


%check
%if %{with tests}
: Use installed tree and autoloader
mkdir vendor
%{_bindir}/phpab --format fedora --output vendor/autoload.php tests
cat << 'EOF' | tee -a vendor/autoload.php
require_once '%{buildroot}/%{php_home}/Swift%{major}/autoload.php';
require_once '%{php_home}/Mockery1/autoload.php';
//require_once '%{php_home}/Symfony4/Bridge/PhpUnit/autoload.php';
EOF

: Avoid duplicated classes
find tests -name \*.php -exec sed -e '/swift_required/d' -i {} \;

TMPDIR=$(mktemp -d $PWD/rpmtests-XXXXXXXX)
cat << EOF | tee tests/acceptance.conf.php
<?php
define('SWIFT_TMP_DIR', '$TMPDIR');
EOF

: for phpunit8/9
find tests -name \*.php \
  -exec sed \
    -e 's/assertMatchesRegularExpression/assertRegExp/' \
    -e 's/assertDoesNotMatchRegularExpression/assertNotRegExp/' \
    -e 's/function setUp()/function setUp():void/' \
    -e 's/function tearDown()/function tearDown():void/' \
    -i {} \;

: get rid of symfony/phpunit-bridge
sed -e '/listener/d' phpunit.xml.dist > phpunit.xml

: Run upstream test suite
ret=0
for cmdarg in "php %{phpunit}" php73 php74 php80 php81; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit9} \
      --filter '^((?!(testLMv1Generator)).)*$' \
      --exclude smoke \
      --verbose || ret=1
  fi
done
rm -r $TMPDIR
exit $ret
%endif


%files
%license LICENSE
%doc CHANGES README.md
%doc doc
%doc composer.json
%{php_home}/Swift%{major}


%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 19 2021 Remi Collet <remi@remirepo.net> - 6.3.0-1
- update to 6.3.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar  9 2021 Remi Collet <remi@remirepo.net> - 6.2.7-1
- update to 6.2.7
- allow egulias/email-validator v3

* Fri Mar  5 2021 Remi Collet <remi@remirepo.net> - 6.2.6-1
- update to 6.2.6

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 12 2021 Remi Collet <remi@remirepo.net> - 6.2.5-1
- update to 6.2.5

* Wed Dec  9 2020 Remi Collet <remi@remirepo.net> - 6.2.4-1
- update to 6.2.4
- sources from git snapshot
- switch to phpunit9 and php-mockery

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 24 2020 Remi Collet <remi@remirepo.net> - 6.2.3-3
- disable test suite where mockery < 1 is broken

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Remi Collet <remi@remirepo.net> - 6.2.3-1
- update to 6.2.3

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 23 2019 Remi Collet <remi@remirepo.net> - 6.2.1-1
- update to 6.2.1

* Mon Mar 11 2019 Remi Collet <remi@remirepo.net> - 6.2.0-1
- update to 6.2.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 11 2018 Remi Collet <remi@remirepo.net> - 6.1.3-1
- update to 6.1.3

* Fri Jul 13 2018 Remi Collet <remi@remirepo.net> - 6.1.2-1
- update to 6.1.2

* Wed Jul  4 2018 Remi Collet <remi@remirepo.net> - 6.1.1-1
- update to 6.1.1

* Tue Jul  3 2018 Remi Collet <remi@remirepo.net> - 6.1.0-1
- update to 6.1.0
- add dependency on intl extension
- use range dependencies

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct  4 2017 Remi Collet <remi@remirepo.net> - 6.0.2-1
- Update to 6.0.2
- rename to php-swiftmailer6
- raise dependency on PHP 7.0
- add dependency on egulias/email-validator 2.0
- use phpunit6 for test suite

* Wed Oct  4 2017 Remi Collet <remi@remirepo.net> - 5.4.8-3
- drop unneeded dependency on php-mcrypt

* Wed May 10 2017 Remi Collet <remi@remirepo.net> - 5.4.8-1
- Update to 5.4.8

* Fri Apr 21 2017 Remi Collet <remi@remirepo.net> - 5.4.7-1
- Update to 5.4.7

* Mon Feb 13 2017 Remi Collet <remi@fedoraproject.org> - 5.4.6-1
- update to 5.4.6

* Thu Dec 29 2016 Remi Collet <remi@fedoraproject.org> - 5.4.5-1
- update to 5.4.5
- fix Remote Code Execution CVE-2016-10074

* Thu Nov 24 2016 Remi Collet <remi@fedoraproject.org> - 5.4.4-1
- update to 5.4.4

* Fri Jul  8 2016 Remi Collet <remi@fedoraproject.org> - 5.4.3-1
- update to 5.4.3
- drop patch merged upstream

* Tue Jun 14 2016 Remi Collet <remi@fedoraproject.org> - 5.4.2-2
- add patch to allow mockery 0.9.x
  open https://github.com/swiftmailer/swiftmailer/pull/769

* Mon May  2 2016 Remi Collet <remi@fedoraproject.org> - 5.4.2-1
- update to 5.4.2

* Fri Mar 25 2016 Remi Collet <remi@fedoraproject.org> - 5.4.1-2
- rebuild for remi repository

* Fri Oct 16 2015 Remi Collet <remi@fedoraproject.org> - 5.4.1-1
- initial rpm, version 5.4.1
- sources from github, pear channel is dead

