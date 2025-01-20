# remirepo/fedora spec file for php-mongodb
#
# Copyright (c) 2015-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

# disabled for https://fedoraproject.org/wiki/Changes/MongoDB_Removal
%bcond_with          tests

%global gh_commit    75da9ea3b63d97b05e0e8648d8c09a17bc54c0b6
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     mongodb
%global gh_project   mongo-php-library
%global psr0         MongoDB

%global upstream_version 1.20.0
#global upstream_prever  alpha1
#global upstream_lower   alpha1

%global ext_version      1.20.0

Name:           php-%{gh_owner}
Version:        %{upstream_version}%{?upstream_prever:~%{upstream_lower}}
Release:        2%{?dist}
Summary:        MongoDB driver library

License:        Apache-2.0
URL:            https://github.com/%{gh_owner}/%{gh_project}
# use git snapshot to retrieve full sources with tests
Source0:        %{name}-%{upstream_version}%{?upstream_prever}-%{gh_short}.tgz
Source1:        makesrc.sh

# Get rid of composer-runtime-api
Patch0:         %{name}-rpm.patch

BuildArch:      noarch
BuildRequires:  php(language) >= 8.1
BuildRequires:  php-cli
BuildRequires:  php-reflection
BuildRequires:  php-date
BuildRequires:  php-dom
BuildRequires:  php-hash
BuildRequires:  php-json
BuildRequires:  php-spl
BuildRequires: (php-composer(psr/log)                >= 1.1.4 with php-composer(psr/log)                < 4)
%if %{with tests}
BuildRequires:  mongodb-server >= 2.4
BuildRequires:  php-pecl(mongodb) >= %{ext_version}
# From composer.json, "require-dev": {
#        "doctrine/coding-standard": "^12.0",
#        "rector/rector": "^0.19",
#        "squizlabs/php_codesniffer": "^3.7",
#        "symfony/phpunit-bridge": "^5.2",
#        "vimeo/psalm": "^5.13"
%global phpunit %{_bindir}/phpunit9
BuildRequires:  %{phpunit}
%endif
# For autoloader
BuildRequires:  php-composer(fedora/autoloader)

# From composer.json, "require": {
#        "php": "^7.4 || ^8.0"
#        "ext-hash": "*",
#        "ext-json": "*",
#        "ext-mongodb": "^1.18.0",
#        "composer-runtime-api": "^2.0",
#        "symfony/polyfill-php73": "^1.27",
#        "psr/log": "^1.1.4|^2|^3",
#        "symfony/polyfill-php80": "^1.27",
#        "symfony/polyfill-php81": "^1.27"
Requires:       php(language) >= 8.1
Requires:       php-hash
Requires:       php-json
Requires:       php-pecl(mongodb) >= %{ext_version}
Requires:      (php-composer(psr/log)                >= 1.1.4 with php-composer(psr/log)                < 4)
# From phpcompatinfo report for 1.8.0
Requires:       php-reflection
Requires:       php-date
Requires:       php-spl
# For autoloader
Requires:       php-composer(fedora/autoloader)

# Composer
Provides:       php-composer(%{gh_owner}/%{gh_owner}) = %{version}%{?prever}


%description
This library provides a high-level abstraction around the lower-level drivers
for PHP and HHVM (i.e. the mongodb extension).

While the extension provides a limited API for executing commands, queries,
and write operations, this library implements an API similar to that of the
legacy PHP driver. It contains abstractions for client, database, and
collection objects, and provides methods for CRUD operations and common
commands (e.g. index and collection management).

Autoloader: %{_datadir}/php/%{psr0}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

cat << 'EOF'  | tee src/autoload.php
<?php
/* Autoloader for mongodb/mongodb and its dependencies */

require_once '%{_datadir}/php/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('MongoDB\\', __DIR__);
require_once __DIR__. '/functions.php';
\Fedora\Autoloader\Dependencies::required([
    [
        '%{_datadir}/php/Psr/Log3/autoload.php',
        '%{_datadir}/php/Psr/Log2/autoload.php',
        '%{_datadir}/php/Psr/Log/autoload.php',
    ],
]);
EOF

# Get rid of jean85/pretty-package-versions
%patch -P0 -p1 -b .rpm
sed -e 's/@VERSION@/%{upstream_version}%{?upstream_prever:-%{upstream_lower}}/' -i src/Client.php
find src -name \*.rpm -delete
grep -F '%{upstream_version}' src/Client.php


%build
# Nothing


%install
mkdir -p   %{buildroot}%{_datadir}/php
cp -pr src %{buildroot}%{_datadir}/php/%{psr0}


%check
: Check autoloader
php -r '
require_once "%{buildroot}%{_datadir}/php/%{psr0}/autoload.php";
exit (class_exists("%{psr0}\\Client") ? 0 : 1);
'

%if %{with tests}
: Run a server
mkdir dbtest

: Choose a port to allow parallel build
port=$(php -r 'echo (27010+PHP_INT_SIZE+%{?fedora}%{?rhel});')

mongod \
  --journal \
  --logpath     $PWD/server.log \
  --pidfilepath $PWD/server.pid \
  --dbpath      $PWD/dbtest \
  --port        $port \
  --smallfiles \
  --fork

sed -e "s/27017/$port/" phpunit.xml.dist >phpunit.xml
cat << 'EOF' | tee tests/bootstrap.php
<?php
// Library
require_once '%{buildroot}%{_datadir}/php/%{psr0}/autoload.php';
// Test suite
\Fedora\Autoloader\Autoload::addPsr4('MongoDB\\Tests\\', __DIR__);
require_once __DIR__ . '/PHPUnit/Functions.php
EOF

: Run the test suite
ret=0
for cmdarg in "php %{phpunit}" php80 php81 php82; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit9} --verbose || ret=1
  fi
done

: Cleanup
[ -s server.pid ] && kill $(cat server.pid)

exit $ret
%else
: Test suite disabled
%endif


%files
%license LICENSE
%doc composer.json
%doc *.md
%{_datadir}/php/%{psr0}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 25 2024 Remi Collet <remi@remirepo.net> - 1.20.0-1
- update to 1.20.0
- drop docs
- raise dependency on mongodb extension version 1.20

* Mon Sep  9 2024 Remi Collet <remi@remirepo.net> - 1.19.1-3
- drop dependency on symfony/polyfill

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 14 2024 Remi Collet <remi@remirepo.net> - 1.19.1-1
- update to 1.19.1 (no change)

* Tue May 14 2024 Remi Collet <remi@remirepo.net> - 1.19.0-1
- update to 1.19.0

* Thu Mar 28 2024 Remi Collet <remi@remirepo.net> - 1.18.0-1
- update to 1.18.0
- raise dependency on mongodb extension version 1.18

* Tue Mar 19 2024 Remi Collet <remi@remirepo.net> - 1.17.1-1
- update to 1.17.1

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 15 2023 Remi Collet <remi@remirepo.net> - 1.17.0-1
- update to 1.17.0
- raise dependency on PHP 7.2
- raise dependency on mongodb extension version 1.17
- add dependency on psr/log

* Thu Sep 28 2023 Remi Collet <remi@remirepo.net> - 1.16.1-1
- update to 1.16.1

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 22 2023 Remi Collet <remi@remirepo.net> - 1.16.0-1
- update to 1.16.0
- raise dependency on mongodb extension version 1.16
- raise dependency on symfony/polyfill 1.27

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 23 2022 Remi Collet <remi@remirepo.net> - 1.15.0-1
- update to 1.15.0
- raise dependency on mongodb extension version 1.15

* Fri Sep 16 2022 Remi Collet <remi@remirepo.net> - 1.13.1-1
- update to 1.13.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Remi Collet <remi@remirepo.net> - 1.13.0-1
- update to 1.13.0
- raise dependency on mongodb extension version 1.14

* Thu Mar 24 2022 Remi Collet <remi@remirepo.net> - 1.12.0-1
- update to 1.12.0
- raise dependency on mongodb extension version 1.13

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 15 2021 Remi Collet <remi@remirepo.net> - 1.11.0-1
- update to 1.11.0
- raise dependency on PHP 7.2
- raise dependency on mongodb extension version 1.12

* Wed Dec  8 2021 Remi Collet <remi@remirepo.net> - 1.10.1-1
- update to 1.10.1

* Tue Nov  2 2021 Remi Collet <remi@remirepo.net> - 1.10.0-1
- update to 1.10.0
- raise dependency on mongodb extension version 1.11

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul 14 2021 Remi Collet <remi@remirepo.net> - 1.9.0-1
- update to 1.9.0
- raise dependency on PHP 7.1
- raise dependency on mongodb extension version 1.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 25 2020 Remi Collet <remi@remirepo.net> - 1.8.0-1
- update to 1.8.0
- raise dependency on mongodb extension 1.8.1
- add dependency on symfony/polyfill-php80

* Fri Nov  6 2020 Remi Collet <remi@remirepo.net> - 1.7.2-1
- update to 1.7.2

* Mon Oct 12 2020 Remi Collet <remi@remirepo.net> - 1.7.1-1
- update to 1.7.1

* Mon Aug 10 2020 Remi Collet <remi@remirepo.net> - 1.7.0-1
- update to 1.7.0
- raise dependency on PHP 7.0
- raise dependency on mongodb extension 1.8

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb  5 2020 Remi Collet <remi@remirepo.net> - 1.6.0-1
- update to 1.6.0
- raise dependency on mongodb extension 1.7

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 14 2020 Remi Collet <remi@remirepo.net> - 1.5.2-1
- update to 1.5.2

* Thu Nov 14 2019 Remi Collet <remi@remirepo.net> - 1.5.1-1
- update to 1.5.1

* Mon Sep  9 2019 Remi Collet <remi@remirepo.net> - 1.5.0-1
- update to 1.5.0
- raise dependency on PHP 5.6
- raise dependency on mongodb extension 1.6

* Mon Aug 19 2019 Remi Collet <remi@remirepo.net> - 1.4.3-1
- update to 1.4.3

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb  5 2019 Remi Collet <remi@remirepo.net> - 1.4.2-3
- disable test suite and so mongodb-server build dependency
  for https://fedoraproject.org/wiki/Changes/MongoDB_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 24 2018 Remi Collet <remi@remirepo.net> - 1.4.2-1
- update to 1.4.2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Remi Collet <remi@remirepo.net> - 1.4.1-1
- update to 1.4.1

* Thu Jun 28 2018 Remi Collet <remi@remirepo.net> - 1.4.0-1
- update to 1.4.0
- raise dependency on mongodb extension 1.5.0

* Fri Apr 20 2018 Remi Collet <remi@remirepo.net> - 1.3.2-1
- update to 1.3.2

* Wed Apr  4 2018 Remi Collet <remi@remirepo.net> - 1.3.1-1
- update to 1.3.1

* Fri Feb  9 2018 Remi Collet <remi@remirepo.net> - 1.3.0-1
- Update to 1.3.0
- raise dependency on mongodb extension 1.4.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 14 2017 Remi Collet <remi@remirepo.net> - 1.2.0-1
- Update to 1.2.0
- raise dependency on PHP 5.5
- raise dependency on mongodb extension 1.3.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun May 14 2017 Remi Collet <remi@remirepo.net> - 1.1.2-2
- ensure fedora/autoloader is used

* Fri Feb 17 2017 Remi Collet <remi@remirepo.net> - 1.1.2-1
- update to 1.1.2

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 19 2017 Remi Collet <remi@fedoraproject.org> - 1.1.1-1
- update to 1.1.1

* Wed Dec  7 2016 Remi Collet <remi@fedoraproject.org> - 1.1.0-1
- update to 1.1.0
- raise dependency on php-pecl-mongodb 1.2.0
- switch to fedora/autoloader

* Tue Dec  6 2016 Remi Collet <remi@fedoraproject.org> - 1.0.4-1
- update to 1.0.4

* Tue Sep 27 2016 Remi Collet <remi@fedoraproject.org> - 1.0.3-1
- update to 1.0.3

* Thu Jul 28 2016 Remi Collet <remi@fedoraproject.org> - 1.0.2-2
- only run upstream test suite when build --with tests

* Thu Mar 31 2016 Remi Collet <remi@fedoraproject.org> - 1.0.2-1
- update to 1.0.2

* Sat Mar  5 2016 Remi Collet <remi@fedoraproject.org> - 1.0.1-1
- update to 1.0.1

* Fri Jan 22 2016 Remi Collet <remi@fedoraproject.org> - 1.0.0-1
- update to 1.0.0

* Mon Jan  4 2016 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.4.beta2
- update to 1.0.0beta2
- raise dependency on pecl/mongodb ^1.1.1
- run test suite with both PHP 5 and 7 when available

* Tue Nov  3 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.3.beta1
- update to 1.0.0beta1

* Mon Nov  2 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.2.20151102gita3c0b97
- git snapshot

* Sat Oct 31 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.1.alpha1
- initial package
