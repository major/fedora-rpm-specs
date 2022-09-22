# remirepo/fedora spec file for php-ramsey-collection
#
# Copyright (c) 2020-2021 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without tests

# Github
%global gh_commit    cccc74ee5e328031b15640b51056ee8d3bb66c0a
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     ramsey
%global gh_project   collection
# Packagist
%global pk_vendor    %{gh_owner}
%global pk_name      %{gh_project}
# Namespace
%global ns_vendor    Ramsey
%global ns_project   Collection

Name:           php-%{pk_vendor}-%{pk_name}
Version:        1.2.2
Release:        3%{?dist}
Summary:        Library for representing and manipulating collections

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
# Create git snapshot as tests are excluded from official tarball
Source1:        makesrc.sh

BuildArch:      noarch

BuildRequires:  php(language) >= 7.3
BuildRequires:  php-date
BuildRequires:  php-spl
# From composer.json, "require-dev": {
#        "captainhook/captainhook": "^5.3",
#        "dealerdirect/phpcodesniffer-composer-installer": "^0.7.0",
#        "ergebnis/composer-normalize": "^2.6",
#        "fakerphp/faker": "^1.5",
#        "hamcrest/hamcrest-php": "^2",
#        "jangregor/phpstan-prophecy": "^0.8",,
#        "mockery/mockery": "^1.3",
#        "phpspec/prophecy-phpunit": "^2.0",
#        "phpstan/extension-installer": "^1",
#        "phpstan/phpstan": "^0.12.32",
#        "phpstan/phpstan-mockery": "^0.12.5",
#        "phpstan/phpstan-phpunit": "^0.12.11",
#        "phpunit/phpunit": "^8.5 || ^9",
#        "psy/psysh": "^0.10.4",
#        "slevomat/coding-standard": "^6.3",
#        "squizlabs/php_codesniffer": "^3.5",
#        "vimeo/psalm": "^4.4"
%if %{with tests}
BuildRequires:  phpunit9
%global phpunit %{_bindir}/phpunit9
BuildRequires: (php-composer(symfony/polyfill-php81)   >= 1.23  with php-composer(symfony/polyfill-php81)   < 2)
BuildRequires: (php-composer(fzaninotto/faker)         >= 1.5   with php-composer(fzaninotto/faker)         < 2)
BuildRequires: (php-composer(hamcrest/hamcrest-php)    >= 2     with php-composer(hamcrest/hamcrest-php)    < 3)
BuildRequires: (php-composer(mockery/mockery)          >= 1.3   with php-composer(mockery/mockery)          < 2)
BuildRequires: (php-composer(phpspec/prophecy-phpunit) >= 2.0   with php-composer(phpspec/prophecy-phpunit) < 3)
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require": {
#        "php": "^7.3 || ^8",
#        "symfony/polyfill-php81": "^1.23"
Requires:       php(language) >= 7.3
Requires:      (php-composer(symfony/polyfill-php81)   >= 1.23  with php-composer(symfony/polyfill-php81)   < 2)
# From phpcompatifo report for 1.1.1
Requires:       php-spl

# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_name}) = %{version}


%description
ramsey/collection is a PHP library for representing and manipulating
collections. Much inspiration for this library comes from the Java
Collections Framework.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
: Create classmap autoloader
phpab \
  --template fedora \
  --output src/autoload.php \
  src
cat << 'EOF' | tee -a src/autoload.php

\Fedora\Autoloader\Dependencies::required([
    '%{_datadir}/php/Symfony/Polyfill/autoload.php',
]);
EOF


%install
mkdir -p   %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr src %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}


%check
%if %{with tests}
: Generate a simple autoloader
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
// Installed library
require '%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Ramsey\\Console\\', dirname(__DIR__) . '/resources/console');
\Fedora\Autoloader\Autoload::addPsr4('Ramsey\\Collection\\Test\\', dirname(__DIR__) . '/tests');
\Fedora\Autoloader\Autoload::addPsr4('Ramsey\\Test\\Generics\\', dirname(__DIR__) . '/tests/generics');
\Fedora\Autoloader\Dependencies::required([
    '%{_datadir}/php/Faker/autoload.php',
    '%{_datadir}/php/Hamcrest2/autoload.php',
    '%{_datadir}/php/Mockery1/autoload.php',
    '%{_datadir}/php/Prophecy/PhpUnit/autoload.php',
]);
EOF

: Run upstream test suite
ret=0
for cmdarg in "php %{phpunit}" php73 php74 php80 php81; do
  if which $cmdarg; then
   set $cmdarg
   $1 ${2:- %{_bindir}/phpunit9} \
     --no-coverage \
     --verbose || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif

%files
%license LICENSE
%doc *.md
%doc composer.json
%{_datadir}/php/%{ns_vendor}


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 11 2021 Remi Collet <remi@remirepo.net> - 1.2.2-1
- update to 1.2.2

* Fri Aug  6 2021 Remi Collet <remi@remirepo.net> - 1.2.1-1
- update to 1.2.1
- raise dependency on PHP 7.3
- add dependency on symfony/polyfill-php81

* Fri Jul 30 2021 Remi Collet <remi@remirepo.net> - 1.1.4-1
- update to 1.1.4

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Remi Collet <remi@remirepo.net> - 1.1.3-1
- update to 1.1.3

* Thu Jan 21 2021 Remi Collet <remi@remirepo.net> - 1.1.2-1
- update to 1.1.2
- switch to phpunit9

* Thu Oct  1 2020 Remi Collet <remi@remirepo.net> - 1.1.1-1
- initial package
