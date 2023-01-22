# remirepo/Fedora spec file for php-laminas-form
#
# Copyright (c) 2015-2022 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    af231c26209fa0684af9e934e8ee5c085eb14cd0
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-form
%global zf_name      zend-form
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Form

%bcond_without       tests

Name:           php-%{gh_project}
Version:        2.17.1
Release:        3%{?dist}
Summary:        %{namespace} Framework %{library} component

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{gh_commit}/%{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
# Tests
%if %{with tests}
BuildRequires:  php(language) >= 5.6
BuildRequires:  php-date
BuildRequires:  php-intl
BuildRequires:  php-mbstring
BuildRequires:  php-pcre
BuildRequires:  php-spl
# Only v3 for build
BuildRequires: (php-autoloader(%{gh_owner}/laminas-hydrator)             >= 3.2     with php-autoloader(%{gh_owner}/laminas-hydrator)             < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-inputfilter)          >= 2.10    with php-autoloader(%{gh_owner}/laminas-inputfilter)          < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.3     with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.1     with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "require-dev": {
#        "doctrine/annotations": "^1.10.4",
#        "laminas/laminas-cache": "^2.9.0",
#        "laminas/laminas-captcha": "^2.9.0",
#        "laminas/laminas-code": "^3.5.0",
#        "laminas/laminas-coding-standard": "^1.0.0",
#        "laminas/laminas-escaper": "^2.6.1",
#        "laminas/laminas-eventmanager": "^3.3.0",
#        "laminas/laminas-filter": "^2.9.4",
#        "laminas/laminas-i18n": "^2.10.3",
#        "laminas/laminas-recaptcha": "^3.2.0",
#        "laminas/laminas-servicemanager": "^3.4.1",
#        "laminas/laminas-session": "^2.9.3",
#        "laminas/laminas-text": "^2.7.1",
#        "laminas/laminas-validator": "^2.13.4",
#        "laminas/laminas-view": "^2.11.4",
#        "phpspec/prophecy-phpunit": "^2.0",
#        "phpunit/phpunit": "^9.4.2"
#        "psalm/plugin-phpunit": "^0.15.1",
#        "vimeo/psalm": "^4.7"
BuildRequires: (php-composer(doctrine/annotations)                       >= 1.10.4  with php-composer(doctrine/annotations)                       < 2)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-cache)                >= 2.9.0   with php-autoloader(%{gh_owner}/laminas-cache)                < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-captcha)              >= 2.9.0   with php-autoloader(%{gh_owner}/laminas-captcha)              < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-code)                 >= 3.5.0   with php-autoloader(%{gh_owner}/laminas-code)                 < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-escaper)              >= 2.6.1   with php-autoloader(%{gh_owner}/laminas-escaper)              < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-eventmanager)         >= 3.3.0   with php-autoloader(%{gh_owner}/laminas-eventmanager)         < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-filter)               >= 2.9.4   with php-autoloader(%{gh_owner}/laminas-filter)               < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-i18n)                 >= 2.10.3  with php-autoloader(%{gh_owner}/laminas-i18n)                 < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.4.1   with php-autoloader(%{gh_owner}/laminas-servicemanager)       < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-session)              >= 2.9.3   with php-autoloader(%{gh_owner}/laminas-session)              < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-text)                 >= 2.7.1   with php-autoloader(%{gh_owner}/laminas-text)                 < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-validator)            >= 2.13.4  with php-autoloader(%{gh_owner}/laminas-validator)            < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-view)                 >= 2.11.4  with php-autoloader(%{gh_owner}/laminas-view)                 < 3)
BuildRequires: (php-composer(phpspec/prophecy-phpunit)                   >= 2.0     with php-composer(phpspec/prophecy-phpunit)                   < 3)
%global phpunit %{_bindir}/phpunit9
BuildRequires:  phpunit9 >= 9.4.2
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "^7.3 || ~8.0.0",
#        "laminas/laminas-hydrator": "^3.2 || ^4.0",
#        "laminas/laminas-inputfilter": "^2.10",
#        "laminas/laminas-stdlib": "^3.3",
#        "laminas/laminas-zendframework-bridge": "^1.1"
Requires:       php(language) >= 7.3
%if ! %{bootstrap}
Requires:      (php-autoloader(%{gh_owner}/laminas-hydrator)             >= 3.2     with php-autoloader(%{gh_owner}/laminas-hydrator)             < 5)
Requires:      (php-autoloader(%{gh_owner}/laminas-inputfilter)          >= 2.10    with php-autoloader(%{gh_owner}/laminas-inputfilter)          < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.3     with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.1     with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# Mandory because of Polyfill
Requires:      (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 2.7.5   with php-autoloader(%{gh_owner}/laminas-servicemanager)       < 4)
# From composer, "suggest": {
#        "laminas/laminas-captcha": "^2.9, required for using CAPTCHA form elements",
#        "laminas/laminas-code": "^3.5, required to use laminas-form annotations support",
#        "laminas/laminas-eventmanager": "^3.3, reuired for laminas-form annotations support",
#        "laminas/laminas-i18n": "^2.10, required when using laminas-form view helpers",
#        "laminas/laminas-recaptcha": "^3.2, in order to use the ReCaptcha form element",
#        "laminas/laminas-servicemanager": "^3.4.1, required to use the form factories or provide services",
#        "laminas/laminas-view": "^2.11.4, required for using the laminas-form view helpers"
%if 0%{?fedora} >= 21 || 0%{?rhel} >= 8
Suggests:       php-autoloader(%{gh_owner}/laminas-captcha)
Suggests:       php-autoloader(%{gh_owner}/laminas-code)
Suggests:       php-autoloader(%{gh_owner}/laminas-eventmanager)
Suggests:       php-autoloader(%{gh_owner}/laminas-i18n)
Suggests:       php-autoloader(%{gh_owner}/laminas-view)
Suggests:       php-autoloader(%{gh_owner}/laminas-recaptcha)
%endif
%endif
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 2.14.3
Requires:       php-date
Requires:       php-intl
Requires:       php-mbstring
Requires:       php-pcre
Requires:       php-spl

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 2.14.4
Provides:       php-zendframework-%{zf_name}              = %{version}
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
The %{namespace}\Form is intended primarily as a bridge between your domain models
and the View Layer. It composes a thin layer of objects representing form
elements, an InputFilter, and a small number of methods for binding data to
and from the form and attached objects.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
: Create autoloader
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::optional([
    '%{php_home}/%{namespace}/Captcha/autoload.php',
    '%{php_home}/%{namespace}/Code/autoload.php',
    '%{php_home}/%{namespace}/EventManager/autoload.php',
    '%{php_home}/%{namespace}/I18n/autoload.php',
    '%{php_home}/%{namespace}/View/autoload.php',
    '%{php_home}/%{namespace}/ReCaptcha/autoload.php',
]);
# Polyfill must be loaded after ServiceManager
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/InputFilter/autoload.php',
    [
        '%{php_home}/%{namespace}/Hydrator4/autoload.php',
        '%{php_home}/%{namespace}/Hydrator3/autoload.php',
    ],
    '%{php_home}/%{namespace}/Stdlib/autoload.php',
    '%{php_home}/%{namespace}/ServiceManager/autoload.php',
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
%if %{with tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{php_home}/%{namespace}/Hydrator3/autoload.php';
require_once '%{buildroot}%{php_home}/%{namespace}/%{library}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{namespace}Test\\%{library}\\', dirname(__DIR__) . '/test');
\Fedora\Autoloader\Dependencies::required([
     dirname(__DIR__) . '/test/_autoload.php',
    '%{php_home}/Prophecy/PhpUnit/autoload.php',
    '%{php_home}/%{namespace}/Cache/autoload.php',
    '%{php_home}/%{namespace}/Escaper/autoload.php',
    '%{php_home}/%{namespace}/Filter/autoload.php',
    '%{php_home}/%{namespace}/Session/autoload.php',
    '%{php_home}/%{namespace}/Text/autoload.php',
    '%{php_home}/%{namespace}/Validator/autoload.php',
]);
EOF


: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend/%{library}/autoload.php";
exit (class_exists("\\Zend\\%{library}\\Factory") ? 0 : 1);
'

# May fail on local build when laminas-form is installed

: upstream test suite
ret=0
for cmdarg in "php %{phpunit}" php73 php74 php80; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit9} -d memory_limit=1G || ret=1
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
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.17.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Feb  1 2022 Remi Collet <remi@remirepo.net> - 2.17.1-1
- update to 2.17.1

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.17.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue May 25 2021 Remi Collet <remi@remirepo.net> - 2.17.0-1
- update to 2.17.0

* Wed Apr  7 2021 Remi Collet <remi@remirepo.net> - 2.16.3-1
- update to 2.16.3 (no change)

* Tue Mar 23 2021 Remi Collet <remi@remirepo.net> - 2.16.2-1
- update to 2.16.2 (no change)

* Mon Mar 22 2021 Remi Collet <remi@remirepo.net> - 2.16.1-1
- update to 2.16.1

* Fri Mar 19 2021 Remi Collet <remi@remirepo.net> - 2.16.0-1
- update to 2.16.0
- raise dependency on PHP 7.3
- raise dependency on laminas-hydrator 3.2
- raise dependency on laminas-inputfilter 2.10
- raise dependency on laminas-stdlib 3.3
- raise dependency on laminas-zendframework-bridge 1.1
- switch to phpunit9

* Thu Mar 18 2021 Remi Collet <remi@remirepo.net> - 2.15.1-1
- update to 2.15.1
- temporarily disable test suite with PHP 8

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 15 2020 Remi Collet <remi@remirepo.net> - 2.15.0-1
- update to 2.15.0

* Tue Jun 23 2020 Remi Collet <remi@remirepo.net> - 2.14.6-1
- update to 2.14.6

* Mon Mar 30 2020 Remi Collet <remi@remirepo.net> - 2.14.5-1
- update to 2.14.5 (no change)

* Thu Mar 19 2020 Remi Collet <remi@remirepo.net> - 2.14.4-1
- update to 2.14.4

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Remi Collet <remi@remirepo.net> - 2.12.0-2
- allow laminas-hydrator v3

* Wed Jan 15 2020 Remi Collet <remi@remirepo.net> - 2.12.0-1
- switch to Laminas
- add patch for PHP 7.4 from
  https://github.com/laminas/laminas-form/pull/55

* Fri Oct  4 2019 Remi Collet <remi@remirepo.net> - 2.14.3-1
- update to 2.14.3
- drop patch merged upstream

* Fri Oct  4 2019 Remi Collet <remi@remirepo.net> - 2.14.2-1
- update to 2.14.2
- add patch for PHP 7.4 from
  https://github.com/zendframework/zend-form/pull/235

* Wed Feb 27 2019 Remi Collet <remi@remirepo.net> - 2.14.1-1
- update to 2.14.1

* Tue Jan  8 2019 Remi Collet <remi@remirepo.net> - 2.14.0-1
- update to 2.14.0
- raise dependency on zend-stdlib 3.2.1

* Wed Dec 12 2018 Remi Collet <remi@remirepo.net> - 2.13.0-1
- update to 2.13.0
- allow zend-hydrator 3
- use range dependencies

* Wed May 23 2018 Remi Collet <remi@remirepo.net> - 2.12.0-2
- update to 2.12.0

* Tue Dec 12 2017 Remi Collet <remi@remirepo.net> - 2.11.0-3
- zend-servicemanager is mandatory

* Tue Dec 12 2017 Remi Collet <remi@remirepo.net> - 2.11.0-2
- switch from zend-loader to fedora/autoloader

* Thu Dec  7 2017 Remi Collet <remi@remirepo.net> - 2.11.0-1
- Update to 2.11.0
- temporarily switch back to phpunit v5
- raise dependency on zend-inputfilter 2.8
- raise dependency on zend-session 2.8.1

* Tue Oct 24 2017 Remi Collet <remi@remirepo.net> - 2.10.2-3
- fix FTBFS from Koschei, add patch for PHP 7.2 from
  https://github.com/zendframework/zend-form/pull/171

* Mon May 22 2017 Remi Collet <remi@remirepo.net> - 2.10.2-1
- Update to 2.10.2

* Thu Apr 27 2017 Remi Collet <remi@remirepo.net> - 2.10.1-1
- Update to 2.10.1
- raise minimum php version to 5.6
- use phpunit6 on F26+

* Thu Mar  2 2017 Remi Collet <remi@remirepo.net> - 2.10.0-1
- update to 2.10.0
- raise dependency on zend-captcha 2.7.1

* Fri Sep 23 2016 Remi Collet <remi@fedoraproject.org> - 2.9.2-1
- update to 2.9.2

* Thu Sep 15 2016 Remi Collet <remi@fedoraproject.org> - 2.9.1-1
- update to 2.9.1

* Fri Jun 10 2016 Remi Collet <remi@fedoraproject.org> - 2.9.0-1
- update to 2.9.0

* Wed May  4 2016 Remi Collet <remi@fedoraproject.org> - 2.8.3-1
- update to 2.8.3

* Mon May  2 2016 Remi Collet <remi@fedoraproject.org> - 2.8.2-1
- update to 2.8.2
- raise dependency on zend-loader >= 2.5.1-3

* Sun May  1 2016 Remi Collet <remi@fedoraproject.org> - 2.8.1-1
- update to 2.8.1

* Fri Apr  8 2016 Remi Collet <remi@fedoraproject.org> - 2.8.0-1
- update to 2.8.0

* Tue Feb 23 2016 Remi Collet <remi@fedoraproject.org> - 2.7.0-1
- update to 2.7.0
- raise dependency on zend-inputfilter >= 2.6
- raise dependency on zend-hydrator >= 1.1

* Thu Jan 28 2016 Remi Collet <remi@fedoraproject.org> - 2.6.0-1
- update to 2.6.0
- raise dependency on zend-stdlib ~2.7
- add dependency on zend-hydrator ~1.0

* Wed Sep 23 2015 Remi Collet <remi@fedoraproject.org> - 2.5.3-1
- update to 2.5.3

* Thu Sep 10 2015 Remi Collet <remi@fedoraproject.org> - 2.5.2-1
- update to 2.5.2
- raise minimum php version to 5.5

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.1-1
- initial package
