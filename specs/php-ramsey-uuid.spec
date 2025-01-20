# remirepo/fedora spec file for php-ramsey-uuid
#
# Copyright (c) 2020-2023 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without tests

# Github
%global gh_commit    91039bc1faa45ba123c4328958e620d382ec7088
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     ramsey
%global gh_project   uuid
# Packagist
%global pk_vendor    %{gh_owner}
%global pk_name      %{gh_project}
# Namespace
%global ns_vendor    Ramsey
%global ns_project   Uuid

Name:           php-%{pk_vendor}-%{pk_name}
Version:        4.7.6
Release:        3%{?dist}
Summary:        Library for generating and working with UUIDs

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
# Create git snapshot as tests are excluded from official tarball
Source1:        makesrc.sh

BuildArch:      noarch

BuildRequires:  php(language) >= 8.0
BuildRequires:  php-date
BuildRequires:  php-hash
BuildRequires:  php-json
BuildRequires:  php-pcre
BuildRequires:  php-spl
# From composer.json, "require-dev": {
#        "captainhook/captainhook": "^5.10",
#        "captainhook/plugin-composer": "^5.3",
#        "dealerdirect/phpcodesniffer-composer-installer": "^0.7.0",
#        "doctrine/annotations": "^1.8",
#        "ergebnis/composer-normalize": "^2.15",
#        "mockery/mockery": "^1.3",
#        "paragonie/random-lib": "^2",
#        "php-mock/php-mock": "^2.2",
#        "php-mock/php-mock-mockery": "^1.3",
#        "php-parallel-lint/php-parallel-lint": "^1.1",
#        "phpbench/phpbench": "^1.0",
#        "phpstan/extension-installer": "^1.0",
#        "phpstan/phpstan": "^0.12",
#        "phpstan/phpstan-mockery": "^0.12",
#        "phpstan/phpstan-phpunit": "^0.12",
#        "phpunit/phpunit": "^8.5 || ^9",
#        "slevomat/coding-standard": "^7.0",
#        "squizlabs/php_codesniffer": "^3.5",
#        "vimeo/psalm": "^4.9"
%if %{with tests}
BuildRequires: (php-composer(brick/math)             >= 0.8.8 with php-composer(brick/math)             < 1)
BuildRequires: (php-composer(ramsey/collection)      >= 1.2   with php-composer(ramsey/collection)      < 3)
BuildRequires: (php-composer(mockery/mockery)        >= 1.3   with php-composer(mockery/mockery)        < 2)
BuildRequires: (php-composer(php-mock/php-mock)      >= 2.2   with php-composer(php-mock/php-mock)      < 3)
BuildRequires:  phpunit9
%global phpunit %{_bindir}/phpunit9
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require": {
#        "php": "^8.0",
#        "ext-json": "*",
#        "brick/math": "^0.8.8 || ^0.9 || ^0.10 || ^0.11 || ^0.12",
#        "ramsey/collection": "^1.2 || ^2.0",
Requires:       php(language) >= 8.0
Requires:       php-json
Requires:      (php-composer(brick/math)        >= 0.8.8     with php-composer(brick/math)             < 1)
Requires:      (php-composer(ramsey/collection) >= 1.2       with php-composer(ramsey/collection)      < 3)
# From phpcompatifo report for 4.6.0
Requires:       php-date
Requires:       php-hash
Requires:       php-pcre
Requires:       php-spl

# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_name}) = %{version}


%description
ramsey/uuid is a PHP library for generating and working with universally
unique identifiers (UUIDs).

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
    '%{_datadir}/php/Brick/Math/autoload.php',
    '%{_datadir}/php/Ramsey/Collection/autoload.php',
    __DIR__ . '/functions.php',
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
\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\%{ns_project}\\Test\\', dirname(__DIR__) . '/tests');
\Fedora\Autoloader\Dependencies::required([
    '%{_datadir}/php/Mockery1/autoload.php',
    '%{_datadir}/tests/phpmock2/autoload.php',
]);
EOF

: Ignore tests using missing mocking libraries
find tests -type f -exec grep -Eq '(PHPMockery|Aspec|Moontoast)' {} \; -delete -print

: Ignore tests
# testSerializationOfNodeProviderCollection: erratic result on Koji
FILTER="--filter '^((?!(testSerializationOfNodeProviderCollection)).)*$'"
: Test failing with recent depdencies
rm tests/Generator/RandomLibAdapterTest.php

: Run upstream test suite
ret=0
for cmdarg in "php %{?phpunit}" php81 php82 php83; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit9} \
      --no-coverage \
      --verbose $FILTER || ret=1
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
%{_datadir}/php/%{ns_vendor}/%{ns_project}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu May  2 2024 Remi Collet <remi@remirepo.net> - 4.7.6-1
- update to 4.7.6

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov  8 2023 Remi Collet <remi@remirepo.net> - 4.7.5-1
- update to 4.7.5

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Apr 19 2023 Remi Collet <remi@remirepo.net> - 4.7.4-1
- update to 4.7.4

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 13 2023 Remi Collet <remi@remirepo.net> - 4.7.3-1
- update to 4.7.3

* Mon Jan  2 2023 Remi Collet <remi@remirepo.net> - 4.7.1-1
- update to 4.7.1
- allow ramsey/collection 2

* Tue Dec 20 2022 Remi Collet <remi@remirepo.net> - 4.7.0-1
- update to 4.7.0
- raise dependency on ramsey/collection 1.2

* Mon Nov  7 2022 Remi Collet <remi@remirepo.net> - 4.6.0-1
- update to 4.6.0

* Fri Sep 16 2022 Remi Collet <remi@remirepo.net> - 4.5.1-1
- update to 4.5.1

* Thu Sep 15 2022 Remi Collet <remi@remirepo.net> - 4.5.0-1
- update to 4.5.0
- raise dependency on  brick/math 0.8.8

* Mon Aug  8 2022 Remi Collet <remi@remirepo.net> - 4.4.0-1
- update to 4.4.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 20 2022 Remi Collet <remi@remirepo.net> - 4.3.1-2
- allow brick/math 0.10

* Mon Mar 28 2022 Remi Collet <remi@remirepo.net> - 4.3.1-1
- update to 4.3.1
- raise dependency on PHP 8.0
- drop dependency on php-symfony-polyfill

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Sep 27 2021 Remi Collet <remi@remirepo.net> - 4.2.3-1
- update to 4.2.3
- add dependency on php-symfony-polyfill

* Wed Aug 11 2021 Remi Collet <remi@remirepo.net> - 4.2.1-1
- update to 4.2.1

* Mon Aug  9 2021 Remi Collet <remi@remirepo.net> - 4.2.0-1
- update to 4.2.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jan 29 2021 Remi Collet <remi@remirepo.net> - 4.1.1-3
- ignore 2 tests and fix FTBFS

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov  6 2020 Remi Collet <remi@remirepo.net> - 4.1.1-2
- add patch for PHP 8 from merged PR
  https://github.com/ramsey/uuid/pull/352
- switch to phpunit9
  https://github.com/ramsey/uuid/pull/350
- ignore 1 test with erratic result from review #1884542

* Fri Oct  2 2020 Remi Collet <remi@remirepo.net> - 4.1.1-1
- initial package
