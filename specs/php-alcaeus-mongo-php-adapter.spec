# remirepo/fedora spec file for php-alcaeus-mongo-php-adapter
#
# Copyright (c) 2016-2023 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

# disabled for https://fedoraproject.org/wiki/Changes/MongoDB_Removal
%bcond_with          tests

%global gh_commit    561496fca4989dc728ed3dda50331aacae62ee9c
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     alcaeus
%global gh_project   mongo-php-adapter
%global ns_vendor    Alcaeus


Name:           php-%{gh_owner}-%{gh_project}
Version:        1.2.5
Release:        5%{?dist}
Summary:        Mongo PHP Adapter

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}%{?prever}-%{?gh_short}.tar.gz

BuildArch:      noarch
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  php(language) >= 5.6
%if %{with tests}
BuildRequires:  php-ctype
BuildRequires:  php-hash
BuildRequires:  php-composer(mongodb/mongodb) >= 1.0.1
BuildRequires:  php-reflection
BuildRequires:  php-date
BuildRequires:  php-json
BuildRequires:  php-mbstring
BuildRequires:  php-pcre
BuildRequires:  php-spl
# from composer.json, require-dev": {
#        "phpunit/phpunit": "^5.7.27 || ^6.0 || ^7.0",
#        "squizlabs/php_codesniffer": "^3.2"
BuildRequires:  mongodb-server >= 3.4
BuildRequires:  phpunit7
%endif

# From composer.json, "require": {
#        "php": "^5.6 || ^7.0 || ^8.0",
#        "ext-ctype": "*",
#        "ext-hash": "*",
#        "ext-mongodb": "^1.2.0",
#        "mongodb/mongodb": "^1.0.1"
Requires:       php(language) >= 5.6
Requires:       php-ctype
Requires:       php-hash
Requires:       php-pecl(mongodb) >= 1.2.0
Requires:       php-composer(mongodb/mongodb) >= 1.0.1
# From phpcompatinfo report for 1.1.7
Requires:       php-reflection
Requires:       php-date
Requires:       php-json
Requires:       php-mbstring
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

# Composer
Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-composer(ext-mongo) = 1.6.14


%description
The Mongo PHP Adapter is a userland library designed to act as an
adapter between applications relying on ext-mongo and the new driver
(ext-mongodb).

It provides the API of ext-mongo built on top of mongo-php-library,
thus being compatible with PHP 7.

Autoloader: %{_datadir}/php/%{ns_vendor}/MongoDbAdapter/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}
mv lib/Mongo  lib/%{ns_vendor}/Mongo


%build
: Create a classmap autoloader
%{_bindir}/phpab \
    --template fedora \
    --output lib/%{ns_vendor}/MongoDbAdapter/autoload.php \
             lib/%{ns_vendor}

cat << 'EOF' | tee -a lib/%{ns_vendor}/MongoDbAdapter/autoload.php

\Fedora\Autoloader\Dependencies::required(array(
    dirname(__DIR__) . '/Mongo/functions.php',
    '%{_datadir}/php/MongoDB/autoload.php',
));
EOF


%install
mkdir -p   %{buildroot}%{_datadir}/php
cp -pr lib/%{ns_vendor} %{buildroot}%{_datadir}/php/%{ns_vendor}


%check
%if %{with tests}
cat << 'EOF' | tee bs.php
<?php
require '%{buildroot}%{_datadir}/php/%{ns_vendor}/MongoDbAdapter/autoload.php';
require 'tests/%{ns_vendor}/MongoDbAdapter/TestCase.php';
EOF

: Run a server
mkdir dbtest
mongod \
  --journal \
  --logpath     $PWD/server.log \
  --pidfilepath $PWD/server.pid \
  --dbpath      $PWD/dbtest \
  --fork   || : skip test as server cant start

if [ ! -s server.pid ] ; then
  exit 0
fi

: Run the test suite
%{_bindir}/phpunit7 --bootstrap bs.php || ret=1

: Cleanup
kill $(cat server.pid)
sleep 1

exit $ret
%else
: Test suite disabled
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc composer.json
%doc *.md
%{_datadir}/php/%{ns_vendor}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 29 2023 Remi Collet <remi@remirepo.net> - 1.2.5-1
- update to 1.2.5

* Wed Oct  4 2023 Remi Collet <remi@remirepo.net> - 1.2.4-1
- update to 1.2.4

* Fri Jul 21 2023 Remi Collet <remi@remirepo.net> - 1.2.3-1
- update to 1.2.3

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Feb  7 2022 Remi Collet <remi@remirepo.net> - 1.2.2-1
- update to 1.2.2

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul  9 2021 Remi Collet <remi@remirepo.net> - 1.2.1-1
- update to 1.2.1

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 12 2020 Remi Collet <remi@remirepo.net> - 1.2.0-1
- update to 1.2.0

* Mon Nov  2 2020 Remi Collet <remi@remirepo.net> - 1.1.13-1
- update to 1.1.13

* Mon Oct 19 2020 Remi Collet <remi@remirepo.net> - 1.1.12-1
- update to 1.1.12

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Remi Collet <remi@remirepo.net> - 1.1.11-1
- update to 1.1.11

* Thu Nov  7 2019 Remi Collet <remi@remirepo.net> - 1.1.10-1
- update to 1.1.10

* Thu Aug  8 2019 Remi Collet <remi@remirepo.net> - 1.1.9-1
- update to 1.1.9

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 15 2019 Remi Collet <remi@remirepo.net> - 1.1.8-1
- update to 1.1.8

* Mon Apr  8 2019 Remi Collet <remi@remirepo.net> - 1.1.7-1
- update to 1.1.7

* Fri Feb  8 2019 Remi Collet <remi@remirepo.net> - 1.1.6-1
- update to 1.1.6
- drop patch merged upstream

* Tue Feb  5 2019 Remi Collet <remi@remirepo.net> - 1.1.5-5
- disable test suite and so mongodb-server build dependency
  for https://fedoraproject.org/wiki/Changes/MongoDB_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul  9 2018 Remi Collet <remi@remirepo.net> - 1.1.5-2
- add upstream for ext-mongodb 1.5

* Tue Mar  6 2018 Remi Collet <remi@remirepo.net> - 1.1.5-1
- Update to 1.1.5
- switch to phpunit7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Remi Collet <remi@remirepo.net> - 1.1.4-1
- Update to 1.1.4

* Sun Sep 24 2017 Remi Collet <remi@remirepo.net> - 1.1.3-1
- Update to 1.1.3

* Sat Aug  5 2017 Remi Collet <remi@remirepo.net> - 1.1.2-1
- Update to 1.1.2

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Remi Collet <remi@remirepo.net> - 1.1.1-1
- Update to 1.1.1

* Sun May 14 2017 Remi Collet <remi@remirepo.net> - 1.1.0-1
- Update to 1.1.0
- raise dependency on PHP >= 5.6
- add dependency on pecl/mongodb >= 1.2.0
- only run test with MongoDB 3.4

* Thu Apr 27 2017 Remi Collet <remi@remirepo.net> - 1.0.11-1
- Update to 1.0.11
- add patch from https://github.com/alcaeus/mongo-php-adapter/pull/167

* Thu Mar 30 2017 Remi Collet <remi@remirepo.net> - 1.0.10-1
- Update to 1.0.10

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 29 2017 Remi Collet <remi@fedoraproject.org> - 1.0.9-1
- update to 1.0.9
- switch to fedora autoloader

* Thu Jan 12 2017 Remi Collet <remi@fedoraproject.org> - 1.0.8-1
- update to 1.0.8

* Tue Dec 20 2016 Remi Collet <remi@fedoraproject.org> - 1.0.7-1
- update to 1.0.7

* Fri Oct  7 2016 Remi Collet <remi@fedoraproject.org> - 1.0.6-1
- update to 1.0.6

* Thu Jul 28 2016 Remi Collet <remi@fedoraproject.org> - 1.0.5-2
- only run upstream test suite when build --with tests

* Mon Jul  4 2016 Remi Collet <remi@fedoraproject.org> - 1.0.5-1
- update to 1.0.5

* Wed Jun 22 2016 Remi Collet <remi@fedoraproject.org> - 1.0.4-1
- update to 1.0.4

* Wed Jun 15 2016 Remi Collet <remi@fedoraproject.org> - 1.0.3-1
- initial package

