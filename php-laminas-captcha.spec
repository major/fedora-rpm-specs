# remirepo/Fedora spec file for php-laminas-captcha
#
# Copyright (c) 2015-2023 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    8623619b1b634ba3672f91a9fb610deffec9c932
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-captcha
%global zf_name      zend-captcha
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Captcha
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}
Version:        2.16.0
Release:        1%{?dist}
Summary:        %{namespace} Framework %{library} component

License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{gh_commit}/%{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
# Tests
%if %{with_tests}
BuildRequires:  php(language) >= 8.0
BuildRequires:  php-date
BuildRequires:  php-gd
BuildRequires:  php-spl
BuildRequires: (php-autoloader(%{gh_owner}/laminas-math)                 >= 2.7     with php-autoloader(%{gh_owner}/laminas-math)                 < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-recaptcha)            >= 3.4.0   with php-autoloader(%{gh_owner}/laminas-recaptcha)            < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-session)              >= 2.12    with php-autoloader(%{gh_owner}/laminas-session)              < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.10.1  with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-text)                 >= 2.9.0   with php-autoloader(%{gh_owner}/laminas-text)                 < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-validator)            >= 2.19.0  with php-autoloader(%{gh_owner}/laminas-validator)            < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.1     with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "require-dev": {
#        "ext-gd": "*",
#        "laminas/laminas-coding-standard": "~2.4.0",
#        "phpunit/phpunit": "^9.5.26",
#        "psalm/plugin-phpunit": "^0.18.4",
#        "vimeo/psalm": "^5.1"
BuildRequires:  php-gd
%global phpunit %{_bindir}/phpunit9
BuildRequires:  phpunit9 >= 9.5.26
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "~8.0.0 || ~8.1.0 || ~8.2.0",
#        "laminas/laminas-math": "^2.7 || ^3.0",
#        "laminas/laminas-recaptcha": "^3.4.0",
#        "laminas/laminas-session": "^2.12",
#        "laminas/laminas-stdlib": "^3.10.1",
#        "laminas/laminas-text": "^2.9.0",
#        "laminas/laminas-validator": "^2.19.0"
Requires:       php(language) >= 8.0
%if ! %{bootstrap}
Requires:      (php-autoloader(%{gh_owner}/laminas-math)                 >= 2.7     with php-autoloader(%{gh_owner}/laminas-math)                 < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-recaptcha)            >= 3.4.0   with php-autoloader(%{gh_owner}/laminas-recaptcha)            < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-session)              >= 2.12    with php-autoloader(%{gh_owner}/laminas-session)              < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.10.1  with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-text)                 >= 2.9.0   with php-autoloader(%{gh_owner}/laminas-text)                 < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-validator)            >= 2.19.0  with php-autoloader(%{gh_owner}/laminas-validator)            < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.1     with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "suggest": {
#        "laminas/laminas-i18n-resources": "Translations of captcha messages",
Suggests:       php-autoloader(%{gh_owner}/laminas-i18n-resources)
%endif
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 2.9.0
Requires:       php-date
Requires:       php-gd
Requires:       php-spl

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 2.9.1
Provides:       php-zendframework-%{zf_name}              = %{version}
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
%{namespace}\Captcha component is able to manage “Completely Automated Public
Turing test to tell Computers and Humans Apart” (CAPTCHA); it is used
as a challenge-response to ensure that the individual submitting
information is a human and not an automated process. Typically, a captcha
is used with form submissions where authenticated users are not necessary,
but you want to prevent spam submissions.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
: Generate autoloader
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/Math/autoload.php',
    '%{php_home}/%{namespace}/ReCaptcha/autoload.php',
    '%{php_home}/%{namespace}/Session/autoload.php',
    '%{php_home}/%{namespace}/Stdlib/autoload.php',
    '%{php_home}/%{namespace}/Text/autoload.php',
    '%{php_home}/%{namespace}/Validator/autoload.php',
]);
\Fedora\Autoloader\Dependencies::optional([
    '%{php_home}/%{namespace}/I18n/Translator/autoload.php',
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
%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{php_home}/%{namespace}/%{library}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{namespace}Test\\%{library}\\', dirname(__DIR__) . '/test');
EOF

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend/%{library}/autoload.php";
exit (class_exists("\\Zend\\%{library}\\Image") ? 0 : 1);
'

# No TESTS_LAMINAS_CAPTCHA_RECAPTCHA_SUPPORT as online
# and skip online tests: testValidationForDifferentElementNametest, testValidationForResponseElementName

: upstream test suite
ret=0
for cmdarg in "php %{phpunit}" php80 php81 php82; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit9} \
      --filter '^((?!(testValidationForDifferentElementName|testValidationForResponseElementName)).)*$' \
      --verbose || ret=1
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
* Tue Jan  3 2023 Remi Collet <remi@remirepo.net> - 2.16.0-1
- update to 2.16.0

* Wed Nov 16 2022 Remi Collet <remi@remirepo.net> - 2.15.0-1
- update to 2.15.0
- raise dependency on PHP 8.0

* Tue Nov 15 2022 Remi Collet <remi@remirepo.net> - 2.14.0-1
- update to 2.14.0 (no change)

* Mon Jul 25 2022 Remi Collet <remi@remirepo.net> - 2.13.0-1
- update to 2.13.0
- raise dependency on PHP 7.4
- raise dependency on laminas-recaptcha 3.4.0
- raise dependency on laminas-stdlib 3.10.1
- raise dependency on laminas-text 2.9.0
- raise dependency on laminas-validator 2.19.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Apr  7 2022 Remi Collet <remi@remirepo.net> - 2.12.0-1
- update to 2.12.0 (no change)
- add mandatory dependencies on recaptcha, session, text and validator

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 14 2021 Remi Collet <remi@remirepo.net> - 2.11.0-2
- rebuild

* Mon Oct  4 2021 Remi Collet <remi@remirepo.net> - 2.11.0-1
- update to 2.11.0
- keep compatibility using laminas-zendframework-bridge
  as this is only used using compat autolader
- raise dependency on laminas-stdlib 3.6

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Mar 18 2021 Remi Collet <remi@remirepo.net> - 2.10.0-1
- update to 2.10.0
- raise dependency on laminas-stdlib 3.3
- raise dependency on laminas-zendframework-bridge 1.1
- switch to phpunit9

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 14 2020 Remi Collet <remi@remirepo.net> - 2.9.0-1
- switch to Laminas

* Tue Jun 18 2019 Remi Collet <remi@remirepo.net> - 2.9.0-1
- update to 2.9.0 (no change)
- raise dependency on zend-stdlib 3.2.1

* Thu Apr 26 2018 Remi Collet <remi@remirepo.net> - 2.8.0-2
- update to 2.8.0
- raise dependency on zend-math 2.7
- raise dependency on zend-stdlib 2.7.7
- switch to phpunit6 or phpunit7
- use range dependencies on F27+

* Mon Dec 11 2017 Remi Collet <remi@remirepo.net> - 2.7.1-3
- switch from zend-loader to fedora/autoloader

* Thu Feb 23 2017 Remi Collet <remi@fedoraproject.org> - 2.7.1-1
- update to 2.7.1

* Mon Feb 20 2017 Remi Collet <remi@fedoraproject.org> - 2.7.0-1
- update to 2.7.0

* Wed Jun 22 2016 Remi Collet <remi@fedoraproject.org> - 2.6.0-1
- update to 2.6.0
- raise dependency on PHP 5.6

* Tue Feb 23 2016 Remi Collet <remi@fedoraproject.org> - 2.5.4-1
- update to 2.5.4
- raise dependency on zend-math >= 2.6
- raise dependency on zend-stdlib >= 2.7

* Tue Feb 23 2016 Remi Collet <remi@fedoraproject.org> - 2.5.3-1
- update to 2.5.3

* Wed Nov 25 2015 Remi Collet <remi@fedoraproject.org> - 2.5.2-1
- update to 2.5.2
- raise dependency on PHP 5.5

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.1-1
- initial package
