# remirepo/Fedora spec file for php-laminas-escaper
#
# Copyright (c) 2015-2022 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    ee7a4c37bf3d0e8c03635d5bddb5bb3184ead490
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-escaper
%global zf_name      zend-escaper
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Escaper
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}
Version:        2.12.0
Release:        1%{?dist}
Summary:        Laminas Framework %{library} component

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{gh_commit}/%{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
# Tests
%if %{with_tests}
BuildRequires:  php(language) >= 7.4
BuildRequires: (php-composer(%{gh_owner}/laminas-zendframework-bridge) >= 1.0 with php-composer(%{gh_owner}/laminas-zendframework-bridge) < 2)
BuildRequires:  php-ctype
BuildRequires:  php-iconv
BuildRequires:  php-mbstring
BuildRequires:  php-pcre
BuildRequires:  php-spl
# From composer, "require-dev": {
#        "infection/infection": "^0.26.6",
#        "laminas/laminas-coding-standard": "~2.4.0",
#        "maglnet/composer-require-checker": "^3.8.0",
#        "phpunit/phpunit": "^9.5.18",
#        "psalm/plugin-phpunit": "^0.17.0",
#        "vimeo/psalm": "^4.22.0"
%global phpunit %{_bindir}/phpunit9
BuildRequires:  phpunit9 >= 9.5
# Autoloader
BuildRequires:  php-fedora-autoloader-devel
%endif

# From composer, "require": {
#        "php": "^7.4 || ~8.0.0 || ~8.1.0 || ~8.2.0",
#        "ext-ctype": "*",
#        "ext-mbstring": "*"
Requires:       php(language) >= 7.4
Requires:       php-ctype
Requires:       php-mbstring
Requires:      (php-composer(%{gh_owner}/laminas-zendframework-bridge) >= 1.0 with php-composer(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From phpcompatinfo report for version 2.6.1
Requires:       php-iconv
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 2.6.2
Provides:       php-zendframework-%{zf_name}              = %{version}
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
The OWASP Top 10 web security risks study lists Cross-Site Scripting (XSS)
in second place. PHP’s sole functionality against XSS is limited to two
functions of which one is commonly misapplied. Thus, the %{gh_project}
component was written. It offers developers a way to escape output and defend
from XSS and related vulnerabilities by introducing contextual escaping based
on peer-reviewed rules.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
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
    $1 ${2:-%{_bindir}/phpunit8} --verbose || ret=1
  fi
done

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend/%{library}/autoload.php";
exit (class_exists("\\Zend\\%{library}\\%{library}") ? 0 : 1);
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
* Mon Oct 10 2022 Remi Collet <remi@remirepo.net> - 2.12.0-1
- update to 2.12.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Mar  9 2022 Remi Collet <remi@remirepo.net> - 2.10.0-1
- update to 2.10.0
- raise dependency on PHP 7.4

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Sep  3 2021 Remi Collet <remi@remirepo.net> - 2.9.0-1
- update to 2.9.0 (no change)
- keep compatibility using laminas-zendframework-bridge
  as this is only used using compat autolader

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 28 2021 Remi Collet <remi@remirepo.net> - 2.8.0-1
- update to 2.8.0

* Fri Jun 25 2021 Remi Collet <remi@remirepo.net> - 2.7.1-1
- update to 2.7.1

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 18 2020 Remi Collet <remi@remirepo.net> - 2.7.0-1
- update to 2.7.0 (no change)
- raise dependency on PHP 7.3
- switch to phpunit9

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Remi Collet <remi@remirepo.net> - 2.6.1-2
- cleanup

* Mon Jan  6 2020 Remi Collet <remi@remirepo.net> - 2.6.1-1
- switch to Laminas

* Fri Sep  6 2019 Remi Collet <remi@remirepo.net> - 2.6.1-1
- update to 2.6.1 (no change)

* Thu Apr 26 2018 Remi Collet <remi@remirepo.net> - 2.6.0-1
- update to 2.6.0
- raise dependency on PHP 5.6
- switch to phpunit7 on F27+

* Thu Nov 23 2017 Remi Collet <remi@remirepo.net> - 2.5.2-4
- switch from zend-loader to fedora/autoloader

* Fri Jul  1 2016 Remi Collet <remi@fedoraproject.org> - 2.5.2-1
- update to 2.5.2
- raise dependency on PHP 5.5

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.1-1
- initial package
