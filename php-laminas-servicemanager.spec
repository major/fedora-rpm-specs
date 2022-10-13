# remirepo/Fedora spec file for php-laminas-servicemanager
#
# Copyright (c) 2015-2021 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    ed160729bb8721127efdaac799f9a298963345b1
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-servicemanager
%global zf_name      zend-servicemanager
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      ServiceManager
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}
Version:        3.19.0
Release:        1%{?dist}
Summary:        Laminas Framework %{library} component

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{gh_commit}/%{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
# Tests
%if %{with_tests}
BuildRequires:  php(language) >= 8.0
BuildRequires: (php-composer(%{gh_owner}/laminas-zendframework-bridge) >= 1.0   with php-composer(%{gh_owner}/laminas-zendframework-bridge) < 2)
BuildRequires: (php-composer(psr/container)                            >= 1.0   with php-composer(psr/container)                            < 2)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)             >= 3.2.1 with php-autoloader(%{gh_owner}/laminas-stdlib)             < 4)
BuildRequires:  php-reflection
BuildRequires:  php-date
BuildRequires:  php-json
BuildRequires:  php-spl
# From composer, "require-dev": {
#        "composer/package-versions-deprecated": "^1.11.99.5",
#        "laminas/laminas-coding-standard": "~2.4.0",
#        "laminas/laminas-container-config-test": "^0.6",
#        "laminas/laminas-dependency-plugin": "^2.2",
#        "mikey179/vfsstream": "^1.6.11@alpha",
#        "ocramius/proxy-manager": "^2.14.1",
#        "phpbench/phpbench": "^1.2.6",
#        "phpunit/phpunit": "^9.5.25",
#        "psalm/plugin-phpunit": "^0.16.1",
#        "vimeo/psalm": "^4.28"
BuildRequires: (php-composer(mikey179/vfsstream)                >= 1.6.10 with php-composer(mikey179/vfsstream)                < 2)
# ignore minimal version
BuildRequires: (php-composer(ocramius/proxy-manager)            >= 2.2.3 with php-composer(ocramius/proxy-manager)            < 3)
BuildRequires:  phpunit9 >= 9.5.5
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "~8.0.0 || ~8.1.0 || ~8.2.0",
#        "laminas/laminas-stdlib": "^3.2.1",
#        "psr/container": "^1.0"
Requires:       php(language) >= 8.0
Requires:      (php-autoloader(%{gh_owner}/laminas-stdlib)             >= 3.2.1 with php-autoloader(%{gh_owner}/laminas-stdlib)             < 4)
Requires:      (php-composer(%{gh_owner}/laminas-zendframework-bridge) >= 1.0   with php-composer(%{gh_owner}/laminas-zendframework-bridge) < 2)
Requires:      (php-composer(psr/container)                            >= 1.0   with php-composer(psr/container)                            < 2)
# From phpcompatinfo report for version 3.4.0
Requires:       php-reflection
Requires:       php-date
Requires:       php-json
Requires:       php-spl
%if ! %{bootstrap}
# From composer, "suggest": {
#        "laminas/laminas-stdlib": "laminas-stdlib ^2.5 if you wish to use the MergeReplaceKey or MergeRemoveKey features in Config instances",
#        "ocramius/proxy-manager": "ProxyManager ^2.1.1 to handle lazy initialization of services"
%if 0%{?fedora} >= 21 || 0%{?rhel} >= 8
Suggests:       php-composer(ocramius/proxy-manager)
%endif
# Autoloader
Requires:       php-composer(fedora/autoloader)
%endif
# From composer, "conflict": {
#        "ext-psr": "*",
Conflicts:      php-pecl-psr
#endif

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 3.4.1
Provides:       php-zendframework-%{zf_name}              = %{version}
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}
Provides:       php-composer(psr/container-implementation) = 1.0


%description
The Service Locator design pattern is implemented by the %{gh_project}
component. The Service Locator is a service/object locator, tasked with
retrieving other objects.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv src/autoload.php src/_autoload.php
mv LICENSE.md LICENSE


%build
: Create autoloader
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/Psr/Container/autoload.php',
    '%{php_home}/%{namespace}/Stdlib/autoload.php',
    __DIR__ . '/_autoload.php',
]);
\Fedora\Autoloader\Dependencies::optional([
    '%{php_home}/ProxyManager/autoload.php',
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
\Fedora\Autoloader\Autoload::addPsr4('%{namespace}Bench\\%{library}\\', dirname(__DIR__) . '/benchmarks');
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/org/bovigo/vfs/autoload.php',
]);
EOF

# test using laminas/laminas-container-config-test
rm test/ContainerTest.php

ret=0
for cmd in php php80 php81 php82; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit9 --verbose || ret=1
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
* Tue Oct 11 2022 Remi Collet <remi@remirepo.net> - 3.19.0-1
- update to 3.19.0
- raise dependency on PHP 8.0

* Thu Sep 22 2022 Remi Collet <remi@remirepo.net> - 3.17.0-1
- update to 3.17.0

* Thu Jul 28 2022 Remi Collet <remi@remirepo.net> - 3.16.0-1
- update to 3.16.0 (no change)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Remi Collet <remi@remirepo.net> - 3.15.1-1
- update to 3.15.1
- drop support for psr/container version 2

* Tue Jul 19 2022 Remi Collet <remi@remirepo.net> - 3.15.0-1
- update to 3.15.0
- raise dependency on psr/container 1.1 and allow version 2

* Fri Jul  8 2022 Remi Collet <remi@remirepo.net> - 3.14.0-1
- update to 3.14.0

* Wed Jun 29 2022 Remi Collet <remi@remirepo.net> - 3.13.0-1
- update to 3.13.0

* Thu Jun 16 2022 Remi Collet <remi@remirepo.net> - 3.12.0-1
- update to 3.12.0
- drop dependency on container-interop/container-interop
- conflict with psr extension

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec  3 2021 Remi Collet <remi@remirepo.net> - 3.10.0-1
- update to 3.10.0
- keep compatibility using laminas-zendframework-bridge
  as this is only used using compat autolader
- raise dependency on PHP 7.4

* Mon Jul 26 2021 Remi Collet <remi@remirepo.net> - 3.7.0-1
- update to 3.7.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb  3 2021 Remi Collet <remi@remirepo.net> - 3.6.4-1
- update to 3.6.4

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 25 2021 Remi Collet <remi@remirepo.net> - 3.6.3-1
- update to 3.6.3

* Mon Jan 18 2021 Remi Collet <remi@remirepo.net> - 3.6.2-1
- update to 3.6.2

* Mon Jan 11 2021 Remi Collet <remi@remirepo.net> - 3.6.1-1
- update to 3.6.1
- raise dependency on PHP 7.3
- switch to phpunit 9

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 11 2020 Remi Collet <remi@remirepo.net> - 3.4.1-1
- update to 3.4.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Remi Collet <remi@remirepo.net> - 3.4.0-2
- cleanup

* Tue Jan  7 2020 Remi Collet <remi@remirepo.net> - 3.4.0-1
- switch to Laminas
- add fix for PHP 7.4 from
  https://github.com/laminas/laminas-servicemanager/pull/28

* Wed Oct  9 2019 Remi Collet <remi@remirepo.net> - 3.4.0-4
- fix test autoloader

* Tue Jan  8 2019 Remi Collet <remi@remirepo.net> - 3.4.0-1
- update to 3.4.0
- use range dependencies
- raise dependency on zend-stdlib 3.2.1

* Wed Jan 31 2018 Remi Collet <remi@remirepo.net> - 3.3.2-1
- Update to 3.3.2

* Tue Nov 28 2017 Remi Collet <remi@remirepo.net> - 3.3.1-1
- Update to 3.3.1

* Thu Nov 23 2017 Remi Collet <remi@remirepo.net> - 3.3.0-3
- switch from zend-loader to fedora/autoloader

* Thu Mar  2 2017 Remi Collet <remi@fedoraproject.org> - 3.3.0-1
- update to 3.3.0
- raise dependency on container-interop/container-interop 1.2
- add dependency on psr/container 1.0

* Wed Feb 15 2017 Remi Collet <remi@fedoraproject.org> - 3.2.1-1
- update to 3.2.1

* Tue Dec 20 2016 Remi Collet <remi@fedoraproject.org> - 3.2.0-1
- update to 3.2.0
- raise dependency on PHP 5.6
- add dependency on zendframework/zend-stdlib

* Sun Jul 17 2016 Remi Collet <remi@fedoraproject.org> - 3.1.1-1
- update to 3.1.1

* Wed Jun 29 2016 Remi Collet <remi@fedoraproject.org> - 3.1.0-1
- update to 3.1.0 for ZendFramework 3
- add dependencies autoloader

* Thu Apr 28 2016 Remi Collet <remi@fedoraproject.org> - 2.7.6-1
- update to 2.7.6

* Tue Feb  2 2016 Remi Collet <remi@fedoraproject.org> - 2.7.5-1
- update to 2.7.5

* Thu Jan 28 2016 Remi Collet <remi@fedoraproject.org> - 2.7.4-2
- update to 2.7.4
- raise minimal php version to 5.5
- add dependency on container-interop/container-interop ~1.0

* Thu Aug  6 2015 Remi Collet <remi@fedoraproject.org> - 2.5.1-2
- fix description

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.1-1
- initial package
