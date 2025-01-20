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
%global gh_commit    a4b48764bfbb8f3a6a4d1aeb1a35bb5e9ecac4a5
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
Version:        2.0.0
Release:        7%{?dist}
Summary:        Library for representing and manipulating collections

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
# Create git snapshot as tests are excluded from official tarball
Source1:        makesrc.sh

BuildArch:      noarch

BuildRequires:  php(language) >= 8.1
BuildRequires:  php-date
BuildRequires:  php-spl
# From composer.json, "require-dev": {
#        "captainhook/plugin-composer": "^5.3",
#        "ergebnis/composer-normalize": "^2.28.3",
#        "fakerphp/faker": "^1.21",
#        "hamcrest/hamcrest-php": "^2.0",
#        "jangregor/phpstan-prophecy": "^1.0",
#        "mockery/mockery": "^1.5",
#        "php-parallel-lint/php-console-highlighter": "^1.0",
#        "php-parallel-lint/php-parallel-lint": "^1.3",
#        "phpcsstandards/phpcsutils": "^1.0.0-rc1",
#        "phpspec/prophecy-phpunit": "^2.0",
#        "phpstan/extension-installer": "^1.2",
#        "phpstan/phpstan": "^1.9",
#        "phpstan/phpstan-mockery": "^1.1",
#        "phpstan/phpstan-phpunit": "^1.3",
#        "phpunit/phpunit": "^9.5",
#        "psalm/plugin-mockery": "^1.1",
#        "psalm/plugin-phpunit": "^0.18.4",
#        "ramsey/coding-standard": "^2.0.3",
#        "ramsey/conventional-commits": "^1.3",
#        "vimeo/psalm": "^5.4"
%if %{with tests}
BuildRequires:  phpunit9 >= 9.5
%global phpunit %{_bindir}/phpunit9
BuildRequires: (php-composer(fzaninotto/faker)         >= 1.5   with php-composer(fzaninotto/faker)         < 2)
BuildRequires: (php-composer(hamcrest/hamcrest-php)    >= 2     with php-composer(hamcrest/hamcrest-php)    < 3)
BuildRequires: (php-composer(mockery/mockery)          >= 1.5   with php-composer(mockery/mockery)          < 2)
BuildRequires: (php-composer(phpspec/prophecy-phpunit) >= 2.0   with php-composer(phpspec/prophecy-phpunit) < 3)
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require": {
#        "php": "^8.1",
Requires:       php(language) >= 8.1
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

: ignore PHPStan tests
find tests -type f -exec grep PHPStan {} \; -delete -print

: Run upstream test suite
ret=0
for cmdarg in "php %{phpunit}" php81 php82; do
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
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan  2 2023 Remi Collet <remi@remirepo.net> - 2.0.0-1
- update to 2.0.0
- raise dependency on PHP 8.1

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
