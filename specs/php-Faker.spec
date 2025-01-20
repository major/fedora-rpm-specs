#
# Fedora spec file for php-Faker
#
# Copyright (c) 2012-2021 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     fzaninotto
%global github_name      Faker
%global github_version   1.9.2
%global github_commit    848d8125239d7dbf8ab25cb7f054f1a630e68c2e

%global composer_vendor  fzaninotto
%global composer_project faker

# "php": "^5.3.3 || ^7.0"
%global php_min_ver 5.3.3

# Build using "--without tests" to disable tests
%global with_tests  %{?_without_tests:0}%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{github_name}
Version:       %{github_version}
Release:       10%{?dist}
Summary:       A PHP library that generates fake data

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests.
# Run php-Faker-get-source.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

# For PHP 8, not submitted upstream as dead project
Patch0:        %{name}-php8.patch

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
BuildRequires: php-intl
## phpcompatinfo (computed from version 1.9.0)
BuildRequires: php-curl
BuildRequires: php-date
BuildRequires: php-dom
BuildRequires: php-hash
BuildRequires: php-iconv
BuildRequires: php-json
BuildRequires: php-mbstring
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-spl
## Autoloader
BuildRequires: php-fedora-autoloader-devel
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 1.9.0)
Requires:      php-curl
Requires:      php-date
Requires:      php-dom
Requires:      php-hash
Requires:      php-iconv
Requires:      php-json
Requires:      php-mbstring
Requires:      php-pcre
Requires:      php-reflection
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# php-{COMPOSER_VENDOR}-{COMPOSER_PROJECT}
Provides:      php-%{composer_vendor}-%{composer_project} = %{version}-%{release}
# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Faker is a PHP library that generates fake data for you. Whether you need
to bootstrap your database, create good-looking XML documents, fill-in your
persistence to stress test it, or anonymize data taken from a production
service, Faker is for you.

Faker is heavily inspired by Perl's Data::Faker [1], and by Ruby's Faker [2].

Autoloader: %{phpdir}/Faker/autoload.php

Optional:
* CakePHP (http://cakephp.org/)
* Doctrine ORM (php-doctrine-orm)
* Mandango (http://mandango.org/)
* Propel (http://propelorm.org/)

[1] http://search.cpan.org/~jasonk/Data-Faker/
[2] http://faker.rubyforge.org/


%prep
%setup -qn %{github_name}-%{github_commit}
%patch -P0 -p1 -b .php8

: Create autoloader
cat <<'AUTOLOAD' | tee src/Faker/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Faker\\', __DIR__);
AUTOLOAD


%build
# Empty build section, nothing to build


%install
mkdir -p %{buildroot}%{phpdir}
cp -rp src/%{github_name} %{buildroot}%{phpdir}/


%check
%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{phpdir}/Faker/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Faker\\Test\\', dirname(__DIR__).'/test/Faker');

class_alias('PHPUnit_Framework_TestCase', 'PHPUnit\\Framework\\TestCase');
EOF

# Skip flakey test that randomly fails even after patch from
# https://github.com/fzaninotto/Faker/issues/1498 is applied
#
# Faker\Test\Provider\DateTimeTest::testFixedSeedWithMaximumTimestamp
# InvalidArgumentException: Start date must be anterior to end date.
sed 's/function testFixedSeedWithMaximumTimestamp/function SKIP_testFixedSeedWithMaximumTimestamp/' \
    -i test/Faker/Provider/DateTimeTest.php

if php -r 'exit(PHP_INT_SIZE<8 ? 0 : 1);'
then
  # strtotime(): Epoch doesn't fit in a PHP integer
  rm test/Faker/Provider/ro_RO/PersonTest.php
  rm test/Faker/Provider/fi_FI/PersonTest.php
fi

ret=0
for cmd in php php73 php74 php80; do
  if which $cmd; then
    $cmd -d memory_limit=1G %{_bindir}/phpunit --verbose || ret=1
  fi
done
exit $ret
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%{phpdir}/%{github_name}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Mar 26 2021 Remi Collet <remi@remirepo.net> - 1.9.2-1
- update to 1.9.2
- add minimal test for PHP 8

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 17 2019 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.9.0-1
- Update to 1.9.0 (RHBZ #1772493)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 16 2019 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.8.0-1
- Update to 1.8.0 (RHBZ #1481901)

* Thu Feb 14 2019 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.7.1-7
- Fix FTBFS by skipping flakey test (RHBZ #1605437 / RHBZ #1675661)
- Reference patches locally
- Remove invalid phpdoc @return from autoloader

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 28 2017 Remi Collet <remi@remirepo.net> - 1.7.1-3
- run full test suite on all arches
- add patch for 32-bit from
  https://github.com/fzaninotto/Faker/pull/1348
- add patch for big endian from
  https://github.com/fzaninotto/Faker/pull/1365
- fix dependencies

* Fri Nov 10 2017 Remi Collet <remi@remirepo.net> - 1.7.1-2
- fix skip result condition

* Fri Nov 10 2017 Remi Collet <remi@remirepo.net> - 1.7.1-1
- Update to 1.7.1
- fix erratic FTBFS from Koschei
- skip 1 test on BigEndian
  https://github.com/fzaninotto/Faker/issues/1346
- ignore test results on 32-bit
  https://github.com/fzaninotto/Faker/issues/1347

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 16 2017 Remi Collet <remi@remirepo.net> - 1.6.0-1
- update to 1.6.0
- switch to fedora/autoloader

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul  1 2016 Remi Collet <remi@fedoraproject.org> - 1.5.0-6
- fix test suite on 32bits, FTBFS detected by Koschei
  open https://github.com/fzaninotto/Faker/pull/953

* Sat Mar 12 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.5.0-5
- Add standard "php-{COMPOSER_VENDOR}-{COMPOSER_PROJECT}" provides
- Updated autoloader

* Fri Mar 11 2016 Remi Collet <remi@fedoraproject.org> - 1.5.0-4
- skip tests with erratic results in Koschei

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 30 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.5.0-1
- Updated to 1.5.0 (BZ #1226339)
- Packaged autoloader
- %%license usage

* Sun Jun 08 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.4.0-1
- Updated to 1.4.0 (BZ #1105815)
- Added php-composer(fzaninotto/faker) virtual provide
- Made Doctrine pkg optional instead of required
- Added option to build without tests

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Dec 29 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.3.0-1
- Updated to 1.3.0 (BZ #1044436)
- Spec cleanup

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 10 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.0-1
- Updated to 1.2.0 (BZ #972499)
- Added php-mbstring require
- Updates per new Fedora packaging guidelines for Git repos

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Dec 09 2012 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1.0-2
- Added php-pear(pear.doctrine-project.org/DoctrineCommon) require

* Sun Dec 09 2012 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1.0-1
- Initial package
