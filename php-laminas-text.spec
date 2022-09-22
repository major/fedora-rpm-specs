# remirepo/Fedora spec file for php-laminas-text
#
# Copyright (c) 2015-2021 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    8879e75d03e09b0d6787e6680cfa255afd4645a7
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-text
%global zf_name      zend-text
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Text
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}
Version:        2.9.0
Release:        4%{?dist}
Summary:        %{namespace} Framework %{library} component

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{gh_commit}/%{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
# Tests
%if %{with_tests}
BuildRequires:  php(language) >= 7.3
BuildRequires:  php-ctype
BuildRequires:  php-pcre
BuildRequires:  php-spl
# From composer, "require-dev": {
#        "laminas/laminas-coding-standard": "~1.0.0",
#        "phpunit/phpunit": "^9.3"
BuildRequires: (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.4    with php-autoloader(%{gh_owner}/laminas-servicemanager)       < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.6    with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
%global phpunit %{_bindir}/phpunit9
BuildRequires:  phpunit9 >= 9.3
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "^7.3 || ~8.0.0 || ~8.1.0",
#        "laminas/laminas-servicemanager": "^3.4",
#        "laminas/laminas-stdlib": "^3.6"
Requires:       php(language) >= 7.3
%if ! %{bootstrap}
Requires:      (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.4    with php-autoloader(%{gh_owner}/laminas-servicemanager)       < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.6    with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
%endif
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 2.7.1
Requires:       php-ctype
Requires:       php-pcre
Requires:       php-spl

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 2.7.2
Provides:       php-zendframework-%{zf_name}              = %{version}
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
%{namespace}\Text is a component to work on text strings.
It contains the subcomponents:

* %{namespace}\Text\Figlet that enables developers to create a so called FIGlet
  text. A FIGlet text is a string, which is represented as ASCII art. FIGlets
  use a special font format, called FLT (FigLet Font). By default, one standard
  font is shipped with %{namespace}\Text\Figlet, but you can download
  additional fonts here

* %{namespace}\Text\Table to create text based tables on the fly with different
  decorators. This can be helpful, if you either want to send structured data
  in text emails, which are used to have mono-spaced fonts, or to display table
  information in a CLI application. %{namespace}\Text\Table supports multi-line
  columns, colspan and align as well.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
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
exit (class_exists("\\Zend\\%{library}\\MultiByte") ? 0 : 1);
'

: upstream test suite
ret=0
for cmdarg in "php %{phpunit}" php73 php74 php80 php81; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit9} \
      --filter '^((?!(testWordWrapTriggersDeprecatedError|testStrPadTriggersDeprecatedError)).)*$' \
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
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Nov 10 2021 Remi Collet <remi@remirepo.net> - 2.9.0-2
- ignore tests for deprecation

* Fri Sep  3 2021 Remi Collet <remi@remirepo.net> - 2.9.0-1
- update to 2.9.0
- raise dependency on zend-stdlib >= 3.6
- keep compatibility using laminas-zendframework-bridge
  as this is only used using compat autolader

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 25 2021 Remi Collet <remi@remirepo.net> - 2.8.1-1
- update to 2.8.1 (no change)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov  2 2020 Remi Collet <remi@remirepo.net> - 2.8.0-1
- update to 2.8.0 (no change)
- raise dependency on PHP 7.3
- raise dependency on laminas-servicemanager 3.4
- raise dependency on zend-stdlib >= 3.1
- switch to phpunit9

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 25 2020 Remi Collet <remi@remirepo.net> - 2.7.1-2
- fix Package obsoletes itself #1792401

* Fri Jan 10 2020 Remi Collet <remi@remirepo.net> - 2.7.1-1
- switch to Laminas

* Thu Oct 17 2019 Remi Collet <remi@remirepo.net> - 2.7.1-1
- update to 2.7.1

* Thu May  3 2018 Remi Collet <remi@remirepo.net> - 2.7.0-2
- update to 2.7.0
- raise dependency on PHP 5.6
- use range dependencies on F27+
- switch to phpunit6 or phpunit7

* Thu Dec  7 2017 Remi Collet <remi@remirepo.net> - 2.6.0-4
- switch from zend-loader to fedora/autoloader

* Fri Feb 12 2016 Remi Collet <remi@fedoraproject.org> - 2.6.0-1
- update to 2.6.0
- raise dependency on PHP >= 5.5
- raise dependency on zend-stdlib >= 2.7
- raise dependency on zend-servicemanager >= 2.7.5

* Thu Aug  6 2015 Remi Collet <remi@fedoraproject.org> - 2.5.1-2
- fix description

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.1-1
- initial package
