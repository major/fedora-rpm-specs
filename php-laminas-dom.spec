# remirepo/Fedora spec file for php-laminas-dom
#
# Copyright (c) 2015-2022 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    8cc95ab8843edce65c2b0e77d8f811daff3e4295
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-dom
%global zf_name      zend-dom
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Dom
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}
Version:        2.12.1
Release:        2%{?dist}
Summary:        Laminas Framework %{library} component

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{gh_commit}/%{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
# Tests
%if %{with_tests}
BuildRequires:  php(language) >= 7.4
BuildRequires:  php-dom
BuildRequires:  php-libxml
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.1 with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
BuildRequires:  php-pcre
BuildRequires:  php-spl
# From composer, "require-dev": {
#        "laminas/laminas-coding-standard": "^2.1.4",
#        "phpunit/phpunit": "^9.5.10"
%global phpunit %{_bindir}/phpunit9
BuildRequires:  phpunit9 >= 9.5.10
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "^7.4 || ~8.0.0 || ~8.1.0",
#        "ext-dom": "*",
#        "ext-libxml": "*"
Requires:       php(language) >= 7.4
Requires:       php-dom
Requires:       php-libxml
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.1 with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From phpcompatinfo report for version 2.7.2
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 2.7.3
Provides:       php-zendframework-%{zf_name}              = %{version}
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
The %{gh_project} component provides tools for working with DOM documents and
structures. Currently, we offer Laminas\Dom\Query, which provides a unified
interface for querying DOM documents utilizing both XPath and CSS selectors.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
: Create autoloader
phpab --template fedora --output src/autoload.php src

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

: upstream test suite
ret=0
for cmdarg in "php %{phpunit}" php74 php80 php81 php82; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit9} --verbose || ret=1
  fi
done

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend/%{library}/autoload.php";
exit (class_exists("\\Zend\\%{library}\\Query") ? 0 : 1);
'

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
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun  9 2022 Remi Collet <remi@remirepo.net> - 2.12.1-1
- update to 2.12.1

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 14 2021 Remi Collet <remi@remirepo.net> - 2.12.0-1
- update to 2.12.0
- raise dependency on PHP 7.4

* Mon Dec 13 2021 Remi Collet <remi@remirepo.net> - 2.9.0-1
- update to 2.9.0
- keep compatibility using laminas-zendframework-bridge
  as this is only used using compat autolader

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 12 2021 Remi Collet <remi@remirepo.net> - 2.8.0-1
- update to 2.8.0
- raise dependency on PHP 7.3
- raise dependency on laminas-zendframework-bridge 1.1
- switch to phpunit9

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Remi Collet <remi@remirepo.net> - 2.7.2-2
- cleanup

* Wed Jan  8 2020 Remi Collet <remi@remirepo.net> - 2.7.2-1
- switch to Laminas

* Tue Jun 18 2019 Remi Collet <remi@remirepo.net> - 2.7.2-1
- update to 2.7.2 (no change)

* Wed Apr 11 2018 Remi Collet <remi@remirepo.net> - 2.7.1-1
- update to 2.7.1

* Fri Mar 30 2018 Remi Collet <remi@remirepo.net> - 2.7.0-1
- update to 2.7.0
- raise dependency on PHP 5.6
- use phpunit6

* Tue Dec  5 2017 Remi Collet <remi@remirepo.net> - 2.6.0-5
- switch from zend-loader to fedora/autoloader

* Thu Jan 28 2016 Remi Collet <remi@fedoraproject.org> - 2.6.0-1
- update to 2.6.0
- raise min php version to 5.5

* Thu Aug  6 2015 Remi Collet <remi@fedoraproject.org> - 2.5.1-2
- fix description

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.1-1
- initial package
