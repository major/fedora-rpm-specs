# remirepo/Fedora spec file for php-laminas-recaptcha
#
# Copyright (c) 2015-2022 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    64c72f1f941c15df07b4ab0985b2f7cc1d492ba9
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-recaptcha
%global zf_name      zendservice-recaptcha
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      ReCaptcha
%global with_tests   0%{!?_without_tests:1}

Name:           php-%{gh_project}
Version:        3.5.0
Release:        1%{?dist}
Summary:        %{namespace} Framework %{library} component

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{gh_commit}/%{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
# Tests
%if %{with_tests}
BuildRequires:  php(language) >= 8.0
BuildRequires:  php-json
BuildRequires: (php-autoloader(%{gh_owner}/laminas-http)                 >= 2.15   with php-autoloader(%{gh_owner}/laminas-http)                 < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.10.1 with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.1    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer.json, "require-dev": {
#        "laminas/laminas-coding-standard": "~2.4.0",
#        "laminas/laminas-config": "^3.7",
#        "laminas/laminas-validator": "^2.15",
#        "phpunit/phpunit": "^9.5.26",
#        "psalm/plugin-phpunit": "^0.18.0",
#        "vimeo/psalm": "^4.29.0"
BuildRequires: (php-autoloader(%{gh_owner}/laminas-config)               >= 3.7    with php-autoloader(%{gh_owner}/laminas-config)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-validator)            >= 2.15   with php-autoloader(%{gh_owner}/laminas-validator)            < 3)
%global phpunit %{_bindir}/phpunit9
BuildRequires:  phpunit9 >= 9.5.26
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "~8.0.0 || ~8.1.0 || ~8.2.0",
#        "ext-json": "*",
#        "laminas/laminas-http": "^2.15",
#        "laminas/laminas-stdlib": "^3.10.1"
Requires:       php(language) >= 8.0
Requires:       php-json
Requires:      (php-autoloader(%{gh_owner}/laminas-http)                 >= 2.15   with php-autoloader(%{gh_owner}/laminas-http)                 < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.10.1 with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.1    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "suggest": {
#        "laminas/laminas-validator": "~2.0, if using ReCaptcha's Mailhide API"
Suggests:       php-autoloader(%{gh_owner}/laminas-validator)
# Autoloader
Requires:       php-composer(fedora/autoloader)

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 3.2.1
Provides:       php-zendframework-%{zf_name}              = %{version}
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
%{summary}.

OOP wrapper for the ReCaptcha web service.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
: Create autoloader
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/Http/autoload.php',
    '%{php_home}/%{namespace}/Stdlib/autoload.php',
]);
\Fedora\Autoloader\Dependencies::optional([
    '%{php_home}/%{namespace}/Validator/autoload.php',
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
mkdir -p      %{buildroot}%{php_home}/ZendService/%{library}
cp -pr zf.php %{buildroot}%{php_home}/ZendService/%{library}/autoload.php


%check
%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{php_home}/%{namespace}/%{library}/autoload.php';
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/Config3/autoload.php',
    '%{php_home}/%{namespace}/Validator/autoload.php',
]);
\Fedora\Autoloader\Autoload::addPsr4('%{namespace}Test\\%{library}\\', dirname(__DIR__) . '/test');
EOF

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/ZendService/%{library}/autoload.php";
exit (class_exists("\\ZendService\\%{library}\\ReCaptcha") ? 0 : 1);
'

: upstream test suite
ret=0
for cmdarg in "php %{phpunit}" php80 php81 php82; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit9} --exclude online --verbose || ret=1
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
%dir %{php_home}/ZendService
     %{php_home}/ZendService/%{library}
     %{php_home}/%{namespace}/%{library}


%changelog
* Fri Nov 18 2022 Remi Collet <remi@remirepo.net> - 3.5.0-1
- update to 3.5.0
- raise dependency on PHP 8.0
- drop dependency on laminas-json

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 29 2021 Remi Collet <remi@remirepo.net> - 3.4.0-1
- update to 3.4.0
- keep compatibility using laminas-zendframework-bridge
  as this is only used using compat autolader
- raise dependency on laminas-http 2.15
- raise dependency on laminas-json 3.3
- raise dependency on laminas-stdlib 3.6

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Apr 20 2021 Remi Collet <remi@remirepo.net> - 3.3.0-1
- update to 3.3.0
- raise dependency on PHP 7.3
- raise dependency on laminas-http 2.14
- raise dependency on laminas-json 3.2
- raise dependency on laminas-stdlib 3.3
- raise dependency on laminas-zendframework-bridge 1.1

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 2020 Remi Collet <remi@remirepo.net> - 3.2.0-1
- switch to Laminas

* Fri Feb  8 2019 Remi Collet <remi@remirepo.net> - 3.2.0-1
- update to 3.2.0
- add dependency on zend-stdlib 3.2.1

* Mon May 14 2018 Remi Collet <remi@remirepo.net> - 3.1.0-2
- update to 3.1.0
- use range dependencies on F27+
- switch to phpunit6 or phpunit7

* Mon Dec 11 2017 Remi Collet <remi@remirepo.net> - 3.0.0-6
- fix virtual provide

* Sat Dec  9 2017 Remi Collet <remi@remirepo.net> - 3.0.0-5
- switch from zend-loader to fedora/autoloader

* Thu Mar  2 2017 Remi Collet <remi@fedoraproject.org> - 3.0.0-3
- add patch to skip online tests, from
  https://github.com/zendframework/ZendService_ReCaptcha/pull/12

* Fri Feb 24 2017 Remi Collet <remi@fedoraproject.org> - 3.0.0-2
- rewrite autoloader as framework extension

* Mon Feb 20 2017 Remi Collet <remi@fedoraproject.org> - 3.0.0-1
- update to 3.0.0

* Thu Aug  6 2015 Remi Collet <remi@fedoraproject.org> - 2.0.1-1
- initial package
