# remirepo/fedora spec file for php-sabre-event5
#
# Copyright (c) 2013-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without      tests

# Github
%global gh_commit    86d57e305c272898ba3c28e9bd3d65d5464587c2
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sabre-io
%global gh_project   event
# Packagist
%global pk_vendor    sabre
%global pk_project   %{gh_project}
# Namespace
%global ns_vendor    Sabre
%global ns_project   Event
# For RPM
%global major        5

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Summary:        Lightweight library for event-based programming
Version:        5.1.7
Release:        2%{?dist}

URL:            http://sabre.io/event
License:        BSD-3-Clause
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
%if %{with tests}
BuildRequires:  php(language) >= 7.1
BuildRequires:  php-spl
# From composer.json, "require-dev": {
#        "friendsofphp/php-cs-fixer": "~2.17.1",
#        "phpstan/phpstan": "^0.12||^3.63",
#        "phpunit/phpunit" : "^7.5 || ^8.5 || ^9.6"
BuildRequires:  phpunit9 >= 9.6
%global phpunit %{_bindir}/phpunit9
# Autoloader
BuildRequires:  php-composer(fedora/autoloader)
%endif

# From composer.json, "require": {
#        "php": "^7.1 || ^8.0"
Requires:       php(language) >= 7.1
# From phpcompatinfo report for version 5.0.2
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
This library provides the following event-based concepts:

* EventEmitter.
* Promises.
* An event loop.
* Co-routines.

Full documentation can be found on http://sabre.io/event/

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

cat << 'EOF' | tee lib/autoload.php
<?php
/* Autoloader for %{name} and its dependencies */
require_once '/usr/share/php/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Sabre\\Event\\', __DIR__);

if (!function_exists('Sabre\\Event\\coroutine')) {
    require_once __DIR__ . '/coroutine.php';
    require_once __DIR__ . '/Loop/functions.php';
    require_once __DIR__ . '/Promise/functions.php';
}
EOF


%build
# nothing to build


%install
mkdir -p   %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr lib %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}


%check
: Check version
php -r '
require "%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php";
echo  Sabre\Event\Version::VERSION . "\n";
exit (Sabre\Event\Version::VERSION === "%{version}" ? 0 : 1);
'

%if %{with tests}
: Run upstream test suite against installed library
ret=0
for cmdarg in "php %{phpunit}" php81 php82 php83 php84; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit9} \
      --bootstrap=%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
      --configuration tests/phpunit.xml \
      --verbose || ret=1
  fi
done
exit $ret
%else
: Skip upstream test suite
%endif


%files
%license LICENSE
%doc *md
%doc composer.json
%dir %{_datadir}/php/%{ns_vendor}
     %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Remi Collet <remi@remirepo.net> - 5.1.7-1
- update to 5.1.7 (no change, CS only)

* Fri Jul 26 2024 Remi Collet <remi@remirepo.net> - 5.1.6-1
- update to 5.1.6

* Thu Jul 25 2024 Remi Collet <remi@remirepo.net> - 5.1.5-1
- update to 5.1.5

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Nov  4 2021 Remi Collet <remi@remirepo.net> - 5.1.4-1
- update to 5.1.4

* Thu Nov  4 2021 Remi Collet <remi@remirepo.net> - 5.1.3-1
- update to 5.1.3

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct  5 2020 Remi Collet <remi@remirepo.net> - 5.1.2-1
- update to 5.1.2

* Mon Sep 21 2020 Remi Collet <remi@remirepo.net> - 5.1.1-1
- update to 5.1.1
- switch to phpunit9

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb  1 2020 Remi Collet <remi@remirepo.net> - 5.1.0-1
- update to 5.1.0
- raise dependency on PHP 7.1
- switch to phpunit8

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Mar  5 2018 Remi Collet <remi@remirepo.net> - 5.0.3-1
- Update to 5.0.3
- sources from git snapshot

* Sat Oct 21 2017 Remi Collet <remi@remirepo.net> - 5.0.2-1
- rename to php-sabre-event5
- update to 5.0.2
- raise dependency on PHP 7.0

* Sat Oct 29 2016 Remi Collet <remi@fedoraproject.org> - 2.0.2-3
- switch from symfony/class-loader to fedora/autoloader

* Mon Jul 20 2015 Remi Collet <remi@fedoraproject.org> - 2.0.2-1
- update to 2.0.2
- add autoloader

* Fri Jun 13 2014 Remi Collet <remi@fedoraproject.org> - 1.0.1-1
- update to 1.0.1
- add provides php-composer(sabre/event)
- change url to http://sabre.io/event

* Tue Dec 31 2013 Remi Collet <remi@fedoraproject.org> - 1.0.0-1
- Initial packaging
