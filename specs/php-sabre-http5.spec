# remirepo/fedora spec file for php-sabre-http5
#
# Copyright (c) 2013-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without      tests

# Github
%global gh_commit    dedff73f3995578bc942fa4c8484190cac14f139
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sabre-io
%global gh_project   http
# Packagist
%global pk_vendor    sabre
%global pk_project   %{gh_project}
# Namespace
%global ns_vendor    Sabre
%global ns_project   HTTP
%global major        5

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Summary:        Library for dealing with http requests and responses
Version:        5.1.12
Release:        2%{?dist}

URL:            https://github.com/%{gh_owner}/%{gh_project}
License:        BSD-3-Clause
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
%if %{with tests}
BuildRequires:  php(language) >= 7.1
BuildRequires:  php-mbstring
BuildRequires:  php-ctype
BuildRequires: (php-composer(sabre/event) >= 4.0   with php-composer(sabre/event) < 6)
BuildRequires: (php-composer(sabre/uri)   >= 2.0   with php-composer(sabre/uri)   < 3)
# From composer.json, "require-dev" : {
#        "friendsofphp/php-cs-fixer": "~2.17.1||^3.63",
#        "phpstan/phpstan": "^0.12",
#        "phpunit/phpunit" : "^7.5 || ^8.5 || ^9.6"
BuildRequires:  phpunit9 >= 9.6
%global phpunit %{_bindir}/phpunit9
BuildRequires:  php-curl
BuildRequires:  php-date
BuildRequires:  php-hash
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires:  php-xml
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require" : {
#        "php"          : "^7.1 || ^8.0",
#        "ext-mbstring" : "*",
#        "ext-ctype"    : "*",
#        "ext-curl"     : "*",
#        "sabre/event"  : ">=4.0 <6.0",
#        "sabre/uri"    : "~2.0"
Requires:       php(language) >= 7.1
Requires:       php-mbstring
Requires:       php-ctype
Requires:       php-curl
Requires:      (php-composer(sabre/event) >= 4.0   with php-composer(sabre/event) < 6)
Requires:      (php-composer(sabre/uri)   >= 2.0   with php-composer(sabre/uri)   < 3)
# From phpcompatinfo report for version 5.0.0
Requires:       php-date
Requires:       php-hash
Requires:       php-pcre
Requires:       php-spl
Requires:       php-xml
# Autoloader
Requires:       php-composer(fedora/autoloader)

# Was split from php-sabre-dav in version 1.9
Conflicts:      php-sabre-dav < 1.9

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
This library provides a toolkit to make working with the HTTP protocol easier.

Most PHP scripts run within a HTTP request but accessing information about
the HTTP request is cumbersome at least, mainly do to superglobals and the
CGI standard.

There's bad practices, inconsistencies and confusion.
This library is effectively a wrapper around the following PHP constructs:

For Input:
    $_GET
    $_POST
    $_SERVER
    php://input or $HTTP_RAW_POST_DATA.

For output:
    php://output or echo.
    header()

What this library provides, is a Request object, and a Response object.
The objects are extendable and easily mockable.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

phpab -t fedora -o lib/autoload.php lib
cat << 'EOF' | tee -a lib/autoload.php

// Dependencies
\Fedora\Autoloader\Dependencies::required([
    '%{_datadir}/php/Sabre/Event5/autoload.php',
    '%{_datadir}/php/Sabre/Uri2/autoload.php',
]);

// Functions
if (!function_exists('Sabre\\HTTP\\parseDate')) {
    require_once __DIR__ . '/functions.php';
}
EOF


%build
# nothing to build


%install
# Install as a PSR-0 library
mkdir -p %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr lib %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}


%check
: Check version
php -r '
require "%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php";
echo  Sabre\HTTP\Version::VERSION . "\n";
exit (Sabre\HTTP\Version::VERSION === "%{version}" ? 0 : 1);
'

%if %{with tests}

cd tests
ln -sf %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php bootstrap.php

: Start a Development web server
PORT=$(expr 8080 + %{?fedora}%{?rhel})
sed -e "s/localhost:8000/127.0.0.1:$PORT/" -i phpunit.xml
%{_bindir}/php   -S 127.0.0.1:$PORT -t $PWD/www &>web.log &
PHPPID=$!

: Run upstream test suite against installed library
ret=0
for cmdarg in "php %{phpunit}" php81 php82 php83 php84; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit9} --verbose || ret=1
  fi
done

kill $PHPPID || :

exit $ret
%else
: Skip upstream test suite
%endif


%files
%license LICENSE
%doc *md
%doc composer.json
%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Remi Collet <remi@remirepo.net> - 5.1.12-1
- update to 5.1.12 (no change, CS only)

* Fri Jul 26 2024 Remi Collet <remi@remirepo.net> - 5.1.11-1
- update to 5.1.11

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Aug 24 2023 Remi Collet <remi@remirepo.net> - 5.1.10-1
- update to 5.1.10

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 26 2023 Remi Collet <remi@remirepo.net> - 5.1.7-1
- update to 5.1.7

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Remi Collet <remi@remirepo.net> - 5.1.6-1
- update to 5.1.6

* Mon Jul 11 2022 Remi Collet <remi@remirepo.net> - 5.1.5-1
- update to 5.1.5

* Fri Jun 24 2022 Remi Collet <remi@remirepo.net> - 5.1.4-1
- update to 5.1.4

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Nov  4 2021 Remi Collet <remi@remirepo.net> - 5.1.3-1
- update to 5.1.3

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct  5 2020 Remi Collet <remi@remirepo.net> - 5.1.1-1
- update to 5.1.1
- switch to phpunit9

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb  1 2020 Remi Collet <remi@remirepo.net> - 5.1.0-1
- update to 5.1.0
- raise dependency on PHP 7.1
- switch to phpunit8

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 29 2019 Remi Collet <remi@remirepo.net> - 5.0.5-1
- update to 5.0.5

* Thu Oct 10 2019 Remi Collet <remi@remirepo.net> - 5.0.4-1
- update to 5.0.4

* Tue Oct  8 2019 Remi Collet <remi@remirepo.net> - 5.0.3-1
- update to 5.0.3

* Fri Sep 13 2019 Remi Collet <remi@remirepo.net> - 5.0.2-1
- update to 5.0.2
- drop patch merged upstream
- switch to phpunit7

* Tue Aug 20 2019 Remi Collet <remi@remirepo.net> - 5.0.0-4
- add patch for 7.4 from
  https://github.com/sabre-io/http/pull/121

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul  5 2019 Remi Collet <remi@remirepo.net> - 5.0.0-2
- fix autoloader

* Fri Jul  5 2019 Remi Collet <remi@remirepo.net> - 5.0.0-1
- update to 5.0.0
- rename to php-sabre-http5
- move to /usr/share/php/Sabre/HTTP5
- raise dependency on PHP 7
- raise dependency on sabre/event 5.0
- raise dependency on sabre/uri 2.0
- switch to classmap autoloader
- use phpunit 6

* Tue Jun  5 2018 Remi Collet <remi@remirepo.net> - 4.2.4-1
- update to 4.2.4
- use range dependencies on F27+

* Mon Jun 12 2017 Remi Collet <remi@remirepo.net> - 4.2.3-1
- Update to 4.2.3

* Wed Jan  4 2017 Remi Collet <remi@fedoraproject.org> - 4.2.2-1
- update to 4.2.2

* Sat Oct 29 2016 Remi Collet <remi@fedoraproject.org> - 4.2.1-2
- switch from symfony/class-loader to fedora/autoloader

* Fri Mar 11 2016 Remi Collet <remi@fedoraproject.org> - 4.2.1-1
- update to 4.2.1
- add dependency on sabre/uri
- run test suite with both PHP 5 and 7 when available

* Mon Jul 20 2015 Remi Collet <remi@fedoraproject.org> - 3.0.5-1
- update to 3.0.5
- add autoloader

* Wed Jul 16 2014 Remi Collet <remi@fedoraproject.org> - 2.0.4-1
- update to 2.0.4
- composer dependencies

* Tue May  6 2014 Remi Collet <remi@fedoraproject.org> - 2.0.3-1
- update to 2.0.3

* Tue Feb 11 2014 Remi Collet <remi@fedoraproject.org> - 2.0.2-1
- update to 2.0.2

* Sat Jan 11 2014 Remi Collet <remi@fedoraproject.org> - 2.0.1-1
- update to 2.0.1

* Tue Jan  7 2014 Remi Collet <remi@fedoraproject.org> - 2.0.0-0.2.alpha6
- update to 2.0.0alpha6
- add explicit conflicts with php-sabre-dav < 1.9

* Tue Dec 31 2013 Remi Collet <remi@fedoraproject.org> - 2.0.0-0.1.alpha5
- Initial packaging
