# remirepo/Fedora spec file for php-laminas-code4
#
# Copyright (c) 2015-2022 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    0337d9265bc2e6376babad8c511500821620cb30
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-code
%global zf_name      zend-code
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Code
%global major        4
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}%{major}
Version:        4.7.0
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
BuildRequires:  php-pcre
BuildRequires:  php-reflection
BuildRequires:  php-spl
BuildRequires:  php-tokenizer
# From composer, "require-dev": {
#        "ext-phar": "*",
#        "doctrine/annotations": "^1.13.2",
#        "laminas/laminas-coding-standard": "^2.3.0",
#        "laminas/laminas-stdlib": "^3.6.1",
#        "phpunit/phpunit": "^9.5.10",
#        "psalm/plugin-phpunit": "^0.16.1",
#        "vimeo/psalm": "^4.13.1"
BuildRequires: (php-composer(doctrine/annotations)                     >= 1.13.2 with php-composer(doctrine/annotations)                    < 2)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)             >= 3.6.1  with php-autoloader(%{gh_owner}/laminas-stdlib)            < 4)
BuildRequires:  phpunit9 >= 9.5.10
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "php": ">=7.4, <8.2"
Requires:       php(language) >= 7.4
%if ! %{bootstrap}
# From composer, "suggest": {
#         "doctrine/annotations": "Doctrine\\Common\\Annotations >=1.0 for annotation features",
#         "laminas/laminas-stdlib": "Laminas\\Stdlib component"
Suggests:       php-composer(doctrine/annotations)
Suggests:       php-autoloader(%{gh_owner}/laminas-stdlib)
# Autoloader
Requires:       php-composer(fedora/autoloader)
%endif
# From phpcompatinfo report for version 3.4.1
Requires:       php-pcre
Requires:       php-reflection
Requires:       php-spl
Requires:       php-tokenizer

Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}


%description
%{gh_project} provides facilities to generate arbitrary code using
an object-oriented interface, both to create new code as well as to update
existing code. While the current implementation is limited to generating
PHP code, you can easily extend the base class in order to provide code
generation for other tasks: JavaScript, configuration files, apache vhosts,
etc.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
: Create autoloader
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::optional([
    '%{php_home}/Doctrine/Common/Annotations/autoload.php',
    '%{php_home}/%{namespace}/Stdlib/autoload.php',
    __DIR__ . '/polyfill/ReflectionEnumPolyfill.php',
]);
EOF


%install
: Laminas library
mkdir -p        %{buildroot}%{php_home}/%{namespace}/
cp -pr src      %{buildroot}%{php_home}/%{namespace}/%{library}%{major}
cp -pr polyfill %{buildroot}%{php_home}/%{namespace}/%{library}%{major}/polyfill


%check
%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{php_home}/%{namespace}/%{library}%{major}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{namespace}Test\\%{library}\\', dirname(__DIR__) . '/test');
EOF

ret=0
for cmd in php php74 php80 php81 php82; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit9 --verbose || ret=1
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
%{php_home}/%{namespace}/%{library}%{major}


%changelog
* Tue Sep 20 2022 Remi Collet <remi@remirepo.net> - 4.7.0-1
- update to 4.7.0

* Mon Aug  1 2022 Remi Collet <remi@remirepo.net> - 4.6.0-1
- update to 4.6.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun  9 2022 Remi Collet <remi@remirepo.net> - 4.5.2-1
- update to 4.5.2

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 20 2021 Remi Collet <remi@remirepo.net> - 4.5.1-1
- update to 4.5.1

* Tue Dec  7 2021 Remi Collet <remi@remirepo.net> - 4.5.0-1
- update to 4.5.0

* Thu Sep 23 2021 Remi Collet <remi@remirepo.net> - 4.4.3-1
- update to 4.4.3

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 12 2021 Remi Collet <remi@remirepo.net> - 4.4.2-1
- update to 4.4.2

* Fri Jul  9 2021 Remi Collet <remi@remirepo.net> - 4.4.1-1
- update to 4.4.1

* Fri Jun 18 2021 Remi Collet <remi@remirepo.net> - 4.4.0-1
- update to 4.4.0
- drop dependency on laminas-eventmanager

* Mon May 17 2021 Remi Collet <remi@remirepo.net> - 4.3.0-1
- update to 4.3.0

* Mon May 10 2021 Remi Collet <remi@remirepo.net> - 4.2.2-1
- update to 4.2.2

* Wed Apr 28 2021 Remi Collet <remi@remirepo.net> - 4.2.1-1
- update to 4.2.1

* Thu Apr 15 2021 Remi Collet <remi@remirepo.net> - 4.2.0-1
- update to 4.2.0

* Mon Mar 29 2021 Remi Collet <remi@remirepo.net> - 4.1.0-1
- update to 4.1.0

* Thu Jan  7 2021 Remi Collet <remi@remirepo.net> - 4.0.0-1
- update to 4.0.0
- rename to php-laminas-code4
- install in /usr/share/php/Zend/Code4
- raise dependency on PHP 7.4
- drop zendframework compatibility layer

* Tue Dec  1 2020 Remi Collet <remi@remirepo.net> - 3.5.1-1
- update to 3.5.1 (no change)

* Thu Nov 12 2020 Remi Collet <remi@remirepo.net> - 3.5.0-1
- update to 3.5.0
- raise dependency on PHP 7.3
- raise dependency on laminas-eventmanager 3.3
- raise dependency on laminas-zendframework-bridge 1..1
- switch to phpunit9

* Fri Jan 17 2020 Remi Collet <remi@remirepo.net> - 3.4.1-2
- cleanup

* Tue Jan  7 2020 Remi Collet <remi@remirepo.net> - 3.4.1-1
- switch to Laminas

* Wed Dec 11 2019 Remi Collet <remi@remirepo.net> - 3.4.1-1
- update to 3.4.1

* Mon Oct  7 2019 Remi Collet <remi@remirepo.net> - 3.4.0-1
- update to 3.4.0
- drop patch merged upstream
- use phpunit8

* Mon Sep  2 2019 Remi Collet <remi@remirepo.net> - 3.3.2-2
- update to 3.3.2
- use phpunit7
- use range dependencies
- add patch for PHP 7.4 from
  https://github.com/zendframework/zend-code/pull/172

* Mon Aug 20 2018 Remi Collet <remi@remirepo.net> - 3.3.1-1
- update to 3.3.1

* Tue Nov 28 2017 Remi Collet <remi@remirepo.net> - 3.3.0-2
- switch from zend-loader to fedora/autoloader

* Sat Oct 21 2017 Remi Collet <remi@remirepo.net> - 3.3.0-1
- Update to 3.3.0

* Fri Aug  4 2017 Remi Collet <remi@remirepo.net> - 3.2.0-1
- Update to 3.2.0
- raise dependency on PHP 7.1
- switch to phpunit6

* Tue Oct 25 2016 Remi Collet <remi@fedoraproject.org> - 3.1.0-1
- update to 3.1.0
- raise dependency on PHP 5.6

* Fri Jul  1 2016 Remi Collet <remi@fedoraproject.org> - 3.0.4-1
- update to 3.0.4

* Wed Jun 29 2016 Remi Collet <remi@fedoraproject.org> - 3.0.3-2
- add patch for ocramius/proxy-manager
  https://github.com/zendframework/zend-code/pull/80

* Wed Jun 29 2016 Remi Collet <remi@fedoraproject.org> - 3.0.3-1
- update to 3.0.0 for ZendFramework 3

* Thu Apr 21 2016 Remi Collet <remi@fedoraproject.org> - 2.6.3-1
- update to 2.6.3

* Thu Jan 28 2016 Remi Collet <remi@fedoraproject.org> - 2.6.2-1
- update to 2.6.2
- dependency on doctrine/annotations instrad of doctrine/common
- raise dependency on zend-stdlib ~2.7
- raise dependency on zend-eventmanager ~2.6

* Thu Nov 19 2015 Remi Collet <remi@fedoraproject.org> - 2.5.3-1
- update to 2.5.3
- run test suite with both PHP 5 and 7 when available

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.2-1
- initial package
- open https://github.com/zendframework/zend-code/pull/5
  avoid using 'vendor' path
