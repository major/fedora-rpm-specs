# remirepo/Fedora spec file for stratigility
#
# Copyright (c) 2016-2021 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    cc6f48fd9cedb446debe9c4a1710b31ff7e6a62d
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-stratigility
%global zf_name      zend-stratigility
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Stratigility
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}
Version:        2.2.2p2
Release:        8%{?dist}
Summary:        Middleware for PHP

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{gh_commit}/%{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
# Tests
BuildRequires:  php(language) >= 5.6
BuildRequires: (php-autoloader(%{gh_owner}/laminas-escaper)              >= 2.3    with php-autoloader(%{gh_owner}/laminas-escaper)              < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
BuildRequires: (php-composer(psr/http-message)                           >= 1.0    with php-composer(psr/http-message)                           < 2)
# From composer, "require-dev": {
#        "laminas/laminas-coding-standard": "~1.0.0",
#        "laminas/laminas-diactoros": "^1.0",
#        "malukenho/docheader": "^0.1.5",
#        "phpunit/phpunit": "^5.7.22 || ^6.4.1"
BuildRequires: (php-autoloader(%{gh_owner}/laminas-diactoros)            >= 1.0   with php-autoloader(%{gh_owner}/laminas-diactoros)             < 2)
BuildRequires:  php-composer(http-interop/http-middleware)               >= 0.5
BuildRequires:  php-composer(webimpress/http-middleware-compatibility)   >= 0.1.4
BuildRequires:  php-pcre
BuildRequires:  php-reflection
BuildRequires:  php-spl
%if %{with_tests}
BuildRequires:  phpunit7
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "^5.6 || ^7.0",
#        "laminas/laminas-escaper": "^2.3",
#        "laminas/laminas-zendframework-bridge": "^1.0",
#        "psr/http-message": "^1.0",
#        "webimpress/http-middleware-compatibility": "^0.1.4"
Requires:       php(language) >= 5.6
Requires:      (php-autoloader(%{gh_owner}/laminas-escaper)              >= 2.3    with php-autoloader(%{gh_owner}/laminas-escaper)              < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
Requires:      (php-composer(psr/http-message)                           >= 1.0    with php-composer(psr/http-message)                           < 2)
Requires:       php-composer(http-interop/http-middleware)               >= 0.5
Requires:       php-composer(webimpress/http-middleware-compatibility) >= 0.1.4
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 2.2.2
Requires:       php-reflection
Requires:       php-spl

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 2.2.2p1
Provides:       php-zendframework-%{zf_name}              = %{version}
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
From "Strata", Latin for "layer", and "agility".

Stratigility is a port of Sencha Connect to PHP.
It allows you to create and dispatch middleware pipelines.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE

%build
: Create autoloader
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/Psr/Http/Message/autoload.php',
    '%{php_home}/%{namespace}/Escaper/autoload.php',
    '%{php_home}/webimpress/http-middleware-compatibility/autoload.php',
    __DIR__ . "/functions/double-pass-middleware.php",
    __DIR__ . "/functions/middleware.php",
    __DIR__ . "/functions/path.php",
    __DIR__ . "/functions/double-pass-middleware.legacy.php",
    __DIR__ . "/functions/middleware.legacy.php",
    __DIR__ . "/functions/path.legacy.php",
]);
\Fedora\Autoloader\Dependencies::optional([
    '%{php_home}/%{namespace}/Diactoros/autoload.php',
]);
EOF

cat << 'EOF' | tee zf.php
<?php
require_once '%{php_home}/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/ZendFrameworkBridge/autoload.php',
    dirname(dirname(__DIR__)) . '/%{namespace}/%{library}/autoload.php',
]);
EOF


%install
: Laminas library
mkdir -p   %{buildroot}%{php_home}/%{namespace}/
cp -pr src %{buildroot}%{php_home}/%{namespace}/%{library}

: Zend equiv
mkdir -p      %{buildroot}%{php_home}/Zend/%{library}
cp -pr zf.php %{buildroot}%{php_home}/Zend/%{library}/autoload.php


%check
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{php_home}/%{namespace}/%{library}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{namespace}Test\\%{library}\\', dirname(__DIR__) . '/test');
EOF

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend/%{library}/autoload.php";
exit (class_exists("\\Zend\\%{library}\\Route") ? 0 : 1);
'

%if %{with_tests}
: upstream test suite
ret=0
for cmd in php php73 php74 php80; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit7 || ret=1
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
%{php_home}/Zend/%{library}
%{php_home}/%{namespace}/%{library}


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2p2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2p2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2p2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2p2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Mar 25 2021 Remi Collet <remi@remirepo.net> - 2.2.2p2-4
- switch to phpunit7

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2p2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2p2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 30 2020 Remi Collet <remi@remirepo.net> - 2.2.2p2-1
- update to 2.2.2p2 (no change)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2p1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 10 2020 Remi Collet <remi@remirepo.net> - 2.2.2p1-1
- switch to Laminas
- update to 2.2.2p1
- raise dependency on http-interop/http-middleware 0.5
- add dependency on webimpress/http-middleware-compatibility

* Thu Dec  6 2018 Remi Collet <remi@remirepo.net> - 1.3.3-7
- use range dependencies
- temporarily disable test suite

* Sat Dec  9 2017 Remi Collet <remi@remirepo.net> - 1.3.3-4
- switch from zend-loader to fedora/autoloader

* Tue Jan 24 2017 Remi Collet <remi@fedoraproject.org> - 1.3.3-1
- update to 1.3.3

* Fri Jan  6 2017 Remi Collet <remi@fedoraproject.org> - 1.3.2-1
- update to 1.3.2

* Fri Nov 11 2016 Remi Collet <remi@fedoraproject.org> - 1.3.1-1
- update to 1.3.1

* Thu Nov 10 2016 Remi Collet <remi@fedoraproject.org> - 1.3.0-1
- update to 1.3.0
- raise dependency on PHP 5.6
- add dependency on http-interop/http-middleware

* Sat Jul  2 2016 Remi Collet <remi@fedoraproject.org> - 1.2.1-2
- drop autoloader, rely on zend-loader >= 2.5.1-4

* Wed Jun 29 2016 Remi Collet <remi@fedoraproject.org> - 1.2.1-1
- initial package
