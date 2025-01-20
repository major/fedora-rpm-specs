# remirepo/fedora spec file for php-netresearch-jsonmapper
#
# Copyright (c) 2017-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without       tests

%global gh_commit    8e76efb98ee8b6afc54687045e1b8dba55ac76e5
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     cweiske
%global gh_project   jsonmapper

%global pk_vendor    netresearch
%global pk_project   jsonmapper

%global php_home     %{_datadir}/php

Name:           php-%{pk_vendor}-%{pk_project}4
Version:        4.5.0
Release:        2%{?dist}
Summary:        Map nested JSON structures onto PHP classes, version 4

License:        OSL-3.0
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
# Git snapshot with tests
Source1:        makesrc.sh

BuildArch:      noarch
%if %{with tests}
# For tests
BuildRequires:  php(language) >= 7.1
BuildRequires:  php-date
BuildRequires:  php-json
BuildRequires:  php-pcre
BuildRequires:  php-reflection
BuildRequires:  php-spl
# From composer.json, "require-dev": {
#        "phpunit/phpunit": "~7.5 || ~8.0 || ~9.0 || ~10.0",
#        "squizlabs/php_codesniffer": "~3.5"
%global phpunit %{_bindir}/phpunit10
BuildRequires: phpunit10
# Required by autoloader
BuildRequires:  php-fedora-autoloader-devel
%endif

# From composer.json, "require": {
#        "php": ">=7.1",
#        "ext-spl": "*",
#        "ext-json": "*",
#        "ext-pcre": "*",
#        "ext-reflection": "*"
Requires:       php(language) >= 7.1
Requires:       php-spl
Requires:       php-json
Requires:       php-pcre
Requires:       php-reflection
# From phpcompatinfo report for version 4.4.0
# none
# Required by autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
Takes data retrieved from a JSON web service and converts them into nested
object and arrays - using your own model classes.

Starting from a base object, it maps JSON data on class properties, converting
them into the correct simple types or objects.

It's a bit like the native SOAP parameter mapping PHP's SoapClient gives you,
but for JSON. It does not rely on any schema, only your PHP class definitions.

Type detection works by parsing @var docblock annotations of class properties,
as well as type hints in setter methods.

You do not have to modify your model classes by adding JSON specific code;
it works automatically by parsing already-existing docblocks.

Autoloader: %{php_home}/%{pk_vendor}/%{pk_project}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
phpab --template fedora --output src/autoload.php src


%install
: Library
mkdir -p   %{buildroot}%{php_home}/%{pk_vendor}
cp -pr src %{buildroot}%{php_home}/%{pk_vendor}/%{pk_project}


%check
%if %{with tests}
mkdir vendor
phpab --template fedora --output vendor/autoload.php tests
cat << 'EOF' | tee -a vendor/autoload.php
require_once "%{buildroot}%{php_home}/%{pk_vendor}/%{pk_project}/autoload.php";
EOF

: Run upstream test suite
ret=0
for cmd in "php %{phpunit}" php81 php82 php83 php84; do
  if which $cmd; then
    set $cmd
    $1 ${2:-%{_bindir}/phpunit10} \
      --no-coverage \
      . || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif


%files
%license LICENSE
%doc composer.json
%doc ChangeLog README.rst
%dir %{php_home}/%{pk_vendor}
     %{php_home}/%{pk_vendor}/%{pk_project}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep  9 2024 Remi Collet <remi@remirepo.net> - 4.5.0-1
- update to 4.5.0
- rename to php-netresearch-jsonmapper4 (compat package)

* Wed Jan 31 2024 Remi Collet <remi@remirepo.net> - 4.4.1-1
- update to 4.4.1

* Mon Jan 29 2024 Remi Collet <remi@remirepo.net> - 4.4.0-1
- update to 4.4.0

* Tue Apr 11 2023 Remi Collet <remi@remirepo.net> - 4.2.0-1
- update to 4.2.0

* Fri Dec  9 2022 Remi Collet <remi@remirepo.net> - 4.1.0-1
- update to 4.1.0

* Mon Jun 28 2021 Remi Collet <remi@remirepo.net> - 4.0.0-1
- update to 4.0.0
- raise dependency on PHP 7.1
- switch to phpunit9

* Tue Nov  3 2020 Remi Collet <remi@remirepo.net> - 3.1.1-1
- update to 3.1.1

* Mon Aug 17 2020 Remi Collet <remi@remirepo.net> - 3.1.0-1
- update to 3.1.0

* Tue Aug 11 2020 Remi Collet <remi@remirepo.net> - 3.0.0-1
- update to 3.0.0

* Fri Apr 17 2020 Remi Collet <remi@remirepo.net> - 2.1.0-1
- update to 2.1.0

* Sat Mar 14 2020 Remi Collet <remi@remirepo.net> - 2.0.0-1
- update to 2.0.0
- switch to phpunit7

* Mon Aug 19 2019 Remi Collet <remi@remirepo.net> - 1.6.0-1
- update to 1.6.0
- drop patch merged upstream

* Thu Aug  8 2019 Remi Collet <remi@remirepo.net> - 1.5.2-1
- update to 1.5.2
- add patch for PHP 7.4 from
  https://github.com/cweiske/jsonmapper/pull/131

* Tue Jul  9 2019 Remi Collet <remi@remirepo.net> - 1.5.1-1
- update to 1.5.1

* Mon Jul  8 2019 Remi Collet <remi@remirepo.net> - 1.5.0-1
- update to 1.5.0

* Mon Jan 22 2018 Remi Collet <remi@remirepo.net> - 1.4.0-1
- Update to 1.4.0
- use phpunit6 on F26+
- sources from git snapshot

* Sat Oct 21 2017 Remi Collet <remi@remirepo.net> - 1.3.0-1
- initial package, version 1.3.0
