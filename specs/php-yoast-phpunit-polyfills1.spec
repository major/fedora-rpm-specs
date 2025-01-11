# remirepo/fedora spec file for php-yoast-phpunit-polyfills
#
# SPDX-FileCopyrightText:  Copyright 2020-2025 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please preserve changelog entries
#
# Github
%global gh_commit    0b31ce834facf03b8b44b6587e65b3cf1d7cfb94
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     Yoast
%global gh_project   PHPUnit-Polyfills
# Packagist
%global pk_vendor    yoast
%global pk_project   phpunit-polyfills
# Namespace
%global ns_vendor    Yoast
%global ns_project   PHPUnitPolyfills
# don't change major version used in package name
%global major        %nil
%bcond_without       tests
%global php_home     %{_datadir}/php

Name:           php-%{pk_vendor}-%{pk_project}1
Version:        1.1.3
Release:        1%{?dist}
Summary:        Set of polyfills for changed PHPUnit functionality, version 1

License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
# git snapshot to get upstream test suite
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
%if %{with tests}
BuildRequires:  php(language) >= 5.4
BuildRequires:  php-reflection
# From composer.json, "require-dev": {
#        "yoast/yoastcs": "^2.3.0"
BuildRequires:  phpunit9
BuildRequires:  phpunit8
%endif
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require": {
#        "php": ">=5.4",
#        "phpunit/phpunit": "^4.8.36 || ^5.7.21 || ^6.0 || ^7.0 || ^8.0 || ^9.0"
Requires:       php(language) >= 5.4
# from phpcompatinfo report on version 0.2.0
Requires:       php-reflection
Conflicts:      php-%{pk_vendor}-%{pk_project} < 2

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
Set of polyfills for changed PHPUnit functionality to allow for creating
PHPUnit cross-version compatible tests.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

# Fix for RPM layout
sed -e 's:src/::' phpunitpolyfills-autoload.php > src/autoload.php


%build
# Empty build section, most likely nothing required.


%install
mkdir -p        %{buildroot}/%{php_home}/%{ns_vendor}
cp -pr src      %{buildroot}/%{php_home}/%{ns_vendor}/%{ns_project}%{major}


%check
%if %{with tests}
: Use installed tree and autoloader
mkdir vendor
cat << 'EOF' | tee -a vendor/autoload.php
<?php
require_once '%{php_home}/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Yoast\\PHPUnitPolyfills\\Tests\\', dirname(__DIR__) . '/tests');
require_once '%{buildroot}/%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php';
EOF

: Run upstream test suite
ret=0
if [ -x %{_bindir}/phpunit7 ]; then
    %{_bindir}/phpunit7 --no-coverage || ret=1
fi
if [ -x %{_bindir}/phpunit8 ]; then
  for cmd in php php81 php82 php83; do
    if which $cmd; then
      $cmd %{_bindir}/phpunit8 --no-coverage || ret=1
    fi
  done
fi
if [ -x %{_bindir}/phpunit9 ]; then
  for cmd in php php81 php82 php83 php84; do
    if which $cmd; then
      $cmd %{_bindir}/phpunit9 --no-coverage || ret=1
    fi
  done
fi

exit $ret
%endif


%files
%license LICENSE
%doc *.md
%doc composer.json
%{php_home}/%{ns_vendor}


%changelog
* Thu Jan  9 2025 Remi Collet <remi@remirepo.net> - 1.1.3-1
- update to 1.1.3
- re-license spec file to CECILL-2.1

* Mon Sep  9 2024 Remi Collet <remi@remirepo.net> - 1.1.2-1
- update to 1.1.2

* Fri Aug 30 2024 Remi Collet <remi@remirepo.net> - 1.1.1-1
- rename to php-yoast-phpunit-polyfills1 (compat package)

* Tue Apr  9 2024 Remi Collet <remi@remirepo.net> - 1.1.1-1
- update to 1.1.1

* Fri Mar 31 2023 Remi Collet <remi@remirepo.net> - 1.0.5-1
- update to 1.0.5

* Wed Nov 16 2022 Remi Collet <remi@remirepo.net> - 1.0.4-1
- update to 1.0.4

* Tue Nov 23 2021 Remi Collet <remi@remirepo.net> - 1.0.3-1
- update to 1.0.3

* Mon Oct  4 2021 Remi Collet <remi@remirepo.net> - 1.0.2-1
- update to 1.0.2

* Tue Aug 10 2021 Remi Collet <remi@remirepo.net> - 1.0.1-1
- update to 1.0.1

* Mon Jun 21 2021 Remi Collet <remi@remirepo.net> - 1.0.0-1
- update to 1.0.0

* Wed Mar 10 2021 Remi Collet <remi@remirepo.net> - 0.2.0-2
- reduce build matrix

* Thu Nov 26 2020 Remi Collet <remi@remirepo.net> - 0.2.0-1
- initial rpm
