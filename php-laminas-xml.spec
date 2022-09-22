# remirepo/Fedora spec file for php-laminas-xml
#
# Copyright (c) 2015-2021 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    dcadeefdb6d7ed6b39d772b47e3845003d6ea60f
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-xml
%global zf_name      zendxml
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Xml
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}
Version:        1.4.0
Release:        3%{?dist}
Summary:        Laminas Framework %{library} component

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{gh_commit}/%{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
# Tests
%if %{with_tests}
BuildRequires:  php(language) >= 7.3
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0 with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
BuildRequires:  php-simplexml
BuildRequires:  php-dom
BuildRequires:  php-libxml
BuildRequires:  php-pcre
# From composer, "require-dev": {
#        "laminas/laminas-coding-standard": "~1.0.0",
#        "squizlabs/php_codesniffer": "3.6.1 as 2.9999999.9999999",
#        "phpunit/phpunit": "^9.5.8",
#        "ext-iconv": "*"
BuildRequires:  phpunit9 >= 9.5.8
BuildRequires:  php-iconv
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "^7.3 || ~8.0.0 || ~8.1.0",
#        "ext-dom": "*",
#        "ext-simplexml": "*"
Requires:       php(language) >= 7.3
Requires:       php-dom
Requires:       php-simplexml
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0 with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From phpcompatinfo report for version 1.3.0
Requires:       php-libxml
Requires:       php-pcre
# Autoloader
Requires:       php-composer(fedora/autoloader)

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 1.2.1
Provides:       php-zendframework-%{zf_name}              = %{version}
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
An utility component for XML usage and best practices in PHP.


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
: Create autoloader
phpab --template fedora --output src/autoload.php src

# Notice ZendXml instead of Zend/Xml
cat << 'EOF' | tee zf.php
<?php
require_once '%{php_home}/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/ZendFrameworkBridge/autoload.php',
    dirname(__DIR__) . '/%{namespace}/%{library}/autoload.php',
]);
EOF


%install
: Laminas library
mkdir -p   %{buildroot}%{php_home}/%{namespace}/
cp -pr src %{buildroot}%{php_home}/%{namespace}/%{library}

: Zend equiv
mkdir -p      %{buildroot}%{php_home}/Zend%{library}
cp -pr zf.php %{buildroot}%{php_home}/Zend%{library}/autoload.php


%check
%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{php_home}/%{namespace}/%{library}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{namespace}Test\\%{library}\\', dirname(__DIR__) . '/test');
EOF

: upstream test suite
ret=0
for cmd in php php74 php80 php81; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit9 --verbose || ret=1
  fi
done

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend%{library}/autoload.php";
exit (class_exists("\\Zend%{library}\\Security") ? 0 : 1);
'

exit $ret
%else
: Test suite disabled
%endif


%files
%license LICENSE
%doc *.md
%doc composer.json
%{php_home}/Zend%{library}
%{php_home}/%{namespace}/%{library}


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 30 2021 Remi Collet <remi@remirepo.net> - 1.4.0-1
- update to 1.4.0
- keep compatibility using laminas-zendframework-bridge
  as this is only used using compat autolader

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 25 2021 Remi Collet <remi@remirepo.net> - 1.3.1-1
- update to 1.3.1 (no change)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 19 2020 Remi Collet <remi@remirepo.net> - 1.3.0-1
- update to 1.3.0
- raise dependency on PHP 7.3
- switch to phpunit9

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Remi Collet <remi@remirepo.net> - 1.2.0-2
- cleanup

* Wed Jan  8 2020 Remi Collet <remi@remirepo.net> - 1.2.0-1
- switch to Laminas

* Wed Jan 23 2019 Remi Collet <remi@remirepo.net> - 1.2.0-1
- update to 1.2.0

* Thu May  3 2018 Remi Collet <remi@remirepo.net> - 1.1.0-1
- update to 1.1.0

* Wed Dec  6 2017 Remi Collet <remi@remirepo.net> - 1.0.2-5
- switch from zend-loader to fedora/autoloader

* Sat Jun 11 2016 Shawn Iwinski <shawn@iwin.ski> - 1.0.2-2
- Allow F22 / EPEL7 / EPEL6 (ZF 2.4)

* Fri Feb  5 2016 Remi Collet <remi@fedoraproject.org> - 1.0.2-1
- update to 1.0.2

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 1.0.1-1
- initial package
