# remirepo/Fedora spec file for php-laminas-view
#
# Copyright (c) 2015-2022 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    7c5a85fbdf6df06549279c14a46b841cfcd01e06
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-view
%global zf_name      zend-view
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      View
%global with_tests   0%{!?_without_tests:1}

Name:           php-%{gh_project}
Version:        2.25.1
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
BuildRequires:  php-reflection
BuildRequires:  php-date
BuildRequires:  php-dom
BuildRequires:  php-filter
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires: (php-autoloader(%{gh_owner}/laminas-escaper)              >= 2.5     with php-autoloader(%{gh_owner}/laminas-escaper)              < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-eventmanager)         >= 3.4     with php-autoloader(%{gh_owner}/laminas-eventmanager)         < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-json)                 >= 3.3     with php-autoloader(%{gh_owner}/laminas-json)                 < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-loader)               >= 2.5     with php-autoloader(%{gh_owner}/laminas-loader)               < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.14.0  with php-autoloader(%{gh_owner}/laminas-servicemanager)       < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.10.1  with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
BuildRequires: (php-composer(psr/container)                              >= 1       with php-composer(psr/container)                              < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0     with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "require-dev": {
#        "laminas/laminas-authentication": "^2.13",
#        "laminas/laminas-coding-standard": "~2.4.0",
#        "laminas/laminas-console": "^2.8",
#        "laminas/laminas-feed": "^2.19",
#        "laminas/laminas-filter": "^2.25",
#        "laminas/laminas-http": "^2.17",
#        "laminas/laminas-i18n": "^2.19",
#        "laminas/laminas-modulemanager": "^2.14",
#        "laminas/laminas-mvc": "^3.5",
#        "laminas/laminas-mvc-i18n": "^1.6",
#        "laminas/laminas-mvc-plugin-flashmessenger": "^1.9",
#        "laminas/laminas-navigation": "^2.16",
#        "laminas/laminas-paginator": "^2.15",
#        "laminas/laminas-permissions-acl": "^2.12",
#        "laminas/laminas-router": "^3.10",
#        "laminas/laminas-uri": "^2.10",
#        "phpunit/phpunit": "^9.5.26",
#        "psalm/plugin-phpunit": "^0.18.3",
#        "vimeo/psalm": "^4.30"
BuildRequires: (php-autoloader(%{gh_owner}/laminas-authentication)       >= 2.13    with php-autoloader(%{gh_owner}/laminas-authentication)       < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-console)              >= 2.8     with php-autoloader(%{gh_owner}/laminas-console)              < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-feed)                 >= 2.19    with php-autoloader(%{gh_owner}/laminas-feed)                 < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-filter)               >= 2.25    with php-autoloader(%{gh_owner}/laminas-filter)               < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-http)                 >= 2.17    with php-autoloader(%{gh_owner}/laminas-http)                 < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-i18n)                 >= 2.19    with php-autoloader(%{gh_owner}/laminas-i18n)                 < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-modulemanager)        >= 2.14    with php-autoloader(%{gh_owner}/laminas-modulemanager)        < 3)
%if ! %{bootstrap}
BuildRequires: (php-autoloader(%{gh_owner}/laminas-mvc)                  >= 3.5     with php-autoloader(%{gh_owner}/laminas-mvc)                  < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-mvc-i18n)             >= 1.6     with php-autoloader(%{gh_owner}/laminas-mvc-i18n)             < 2)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-mvc-plugin-flashmessenger) >= 1.9 with php-autoloader(%{gh_owner}/laminas-mvc-plugin-flashmessenger) < 2)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-navigation)           >= 2.16    with php-autoloader(%{gh_owner}/laminas-navigation)           < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-paginator)            >= 2.15    with php-autoloader(%{gh_owner}/laminas-paginator)            < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-permissions-acl)      >= 2.12    with php-autoloader(%{gh_owner}/laminas-permissions-acl)      < 3)
%endif
BuildRequires: (php-autoloader(%{gh_owner}/laminas-router)               >= 3.10    with php-autoloader(%{gh_owner}/laminas-router)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-uri)                  >= 2.10    with php-autoloader(%{gh_owner}/laminas-uri)                  < 3)
BuildRequires:  phpunit9 >= 9.5.26
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "~8.0.0 || ~8.1.0 || ~8.2.0",
#        "ext-dom": "*",
#        "ext-filter": "*",
#        "ext-json": "*",
#        "laminas/laminas-escaper": "^2.5",
#        "laminas/laminas-eventmanager": "^3.4",
#        "laminas/laminas-json": "^3.3",
#        "laminas/laminas-loader": "^2.5",
#        "laminas/laminas-servicemanager": "^3.14.0",
#        "laminas/laminas-stdlib": "^3.10.1",
#        "psr/container": "^1 || ^2"
Requires:       php(language) >= 8.0
Requires:       php-dom
Requires:       php-filter
Requires:       php-json
Requires:      (php-autoloader(%{gh_owner}/laminas-escaper)              >= 2.5     with php-autoloader(%{gh_owner}/laminas-escaper)              < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-eventmanager)         >= 3.4     with php-autoloader(%{gh_owner}/laminas-eventmanager)         < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-json)                 >= 3.3     with php-autoloader(%{gh_owner}/laminas-json)                 < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-loader)               >= 2.5     with php-autoloader(%{gh_owner}/laminas-loader)               < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.14.0  with php-autoloader(%{gh_owner}/laminas-servicemanager)       < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.10.1  with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
Requires:      (php-composer(psr/container)                              >= 1       with php-composer(psr/container)                              < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0     with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "suggest": {
#        "laminas/laminas-authentication": "Laminas\\Authentication component",
#        "laminas/laminas-feed": "Laminas\\Feed component",
#        "laminas/laminas-filter": "Laminas\\Filter component",
#        "laminas/laminas-http": "Laminas\\Http component",
#        "laminas/laminas-i18n": "Laminas\\I18n component",
#        "laminas/laminas-mvc": "Laminas\\Mvc component",
#        "laminas/laminas-mvc-plugin-flashmessenger": "laminas-mvc-plugin-flashmessenger component, if you want to use the FlashMessenger view helper with laminas-mvc versions 3 and up",
#        "laminas/laminas-navigation": "Laminas\\Navigation component",
#        "laminas/laminas-paginator": "Laminas\\Paginator component",
#        "laminas/laminas-permissions-acl": "Laminas\\Permissions\\Acl component",
#        "laminas/laminas-uri": "Laminas\\Uri component"
Suggests:       php-composer(%{gh_owner}/laminas-authentication)
Suggests:       php-composer(%{gh_owner}/laminas-feed)
Suggests:       php-composer(%{gh_owner}/laminas-filter)
Suggests:       php-composer(%{gh_owner}/laminas-http)
Suggests:       php-composer(%{gh_owner}/laminas-i18n)
Suggests:       php-composer(%{gh_owner}/laminas-mvc)
Suggests:       php-composer(%{gh_owner}/laminas-mvc-plugin-flashmessenger)
Suggests:       php-composer(%{gh_owner}/laminas-navigation)
Suggests:       php-composer(%{gh_owner}/laminas-paginator)
Suggests:       php-composer(%{gh_owner}/laminas-permissions-acl)
Suggests:       php-composer(%{gh_owner}/laminas-uri)
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 2.11.4
Requires:       php-cli
Requires:       php-reflection
Requires:       php-date
Requires:       php-pcre
Requires:       php-spl

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 2.11.5
Provides:       php-zendframework-%{zf_name}              = %{version}
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
%{namespace}\View provides the “View” layer of Zend Framework 2’s MVC system.
It is a multi-tiered system allowing a variety of mechanisms for extension,
substitution, and more.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
: Create autoloader
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/ServiceManager/autoload.php',
    [
        '%{php_home}/Psr/Container2/autoload.php',
        '%{php_home}/Psr/Container/autoload.php',
    ],
    '%{php_home}/%{namespace}/Escaper/autoload.php',
    '%{php_home}/%{namespace}/EventManager/autoload.php',
    '%{php_home}/%{namespace}/Loader/autoload.php',
    '%{php_home}/%{namespace}/Stdlib/autoload.php',
]);
\Fedora\Autoloader\Dependencies::optional([
    '%{php_home}/%{namespace}/Authentication/autoload.php',
    '%{php_home}/%{namespace}/Feed/autoload.php',
    '%{php_home}/%{namespace}/Filter/autoload.php',
    '%{php_home}/%{namespace}/Http/autoload.php',
    '%{php_home}/%{namespace}/I18n/autoload.php',
    '%{php_home}/%{namespace}/Json/autoload.php',
    '%{php_home}/%{namespace}/Mvc/autoload.php',
    '%{php_home}/%{namespace}/Navigation/autoload.php',
    '%{php_home}/%{namespace}/Paginator/autoload.php',
    '%{php_home}/%{namespace}/Permissions/Acl/autoload.php',
    '%{php_home}/%{namespace}/Uri/autoload.php',
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
 
# From composer.json,     "bin": [
#        "bin/templatemap_generator.php"
for i in bin/templatemap_generator.php
do   install -Dpm 755 $i %{buildroot}%{_bindir}/%{gh_owner}_$(basename $i .php)
done


%check
%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{php_home}/%{namespace}/%{library}/autoload.php';
\Fedora\Autoloader\Dependencies::optional([
    '%{php_home}/%{namespace}/Console/autoload.php',
    '%{php_home}/%{namespace}/ModuleManager/autoload.php',
    '%{php_home}/%{namespace}/Mvc/I18n/autoload.php',
    '%{php_home}/%{namespace}/Mvc/Plugin/FlashMessenger/autoload.php',
    '%{php_home}/%{namespace}/Router/autoload.php',
]);
\Fedora\Autoloader\Autoload::addPsr4('%{namespace}Test\\%{library}\\', dirname(__DIR__) . '/test');
EOF

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend/%{library}/autoload.php";
exit (class_exists("\\Zend\\%{library}\\View") ? 0 : 1);
'

%if %{bootstrap}
rm -r test/Helper*
%endif

: upstream test suite
ret=0
for cmd in php php80 php81 php82; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit9 \
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
%{_bindir}/%{gh_owner}_templatemap_generator


%changelog
* Wed Dec 21 2022 Remi Collet <remi@remirepo.net> - 2.25.1-1
- update to 2.25.1 (no change)

* Mon Nov  7 2022 Remi Collet <remi@remirepo.net> - 2.25.0-1
- update to 2.25.0 (no change)

* Wed Oct 12 2022 Remi Collet <remi@remirepo.net> - 2.24.0-1
- update to 2.24.0
- raise dependency on PHP 8.0

* Tue Sep 20 2022 Remi Collet <remi@remirepo.net> - 2.23.0-1
- update to 2.23.0

* Thu Aug 18 2022 Remi Collet <remi@remirepo.net> - 2.22.1-1
- update to 2.22.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Remi Collet <remi@remirepo.net> - 2.22.0-1
- update to 2.22.0

* Mon Jul 11 2022 Remi Collet <remi@remirepo.net> - 2.21.0-1
- update to 2.21.0
- raise dependency on laminas-servicemanager 3.14.0
- raise dependency on laminas-stdlib 3.10.1

* Thu Jun 23 2022 Remi Collet <remi@remirepo.net> - 2.20.0-2
- drop dependency on container-interop/container-interop
  replaced by servicemanager >= 3.12

* Wed Mar 30 2022 Remi Collet <remi@remirepo.net> - 2.20.0-1
- update to 2.20.0
- add dependency on laminas-escaper, laminas-servicemanager,
  container-interop/container-interop and psr/container

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 13 2022 Remi Collet <remi@remirepo.net> - 2.19.1-1
- update to 2.19.1 (no change)

* Tue Jan 11 2022 Remi Collet <remi@remirepo.net> - 2.19.0-1
- update to 2.19.0

* Mon Jan 10 2022 Remi Collet <remi@remirepo.net> - 2.18.0-1
- update to 2.18.0
- raise dependency on PHP 7.4

* Mon Jan  3 2022 Remi Collet <remi@remirepo.net> - 2.16.0-1
- update to 2.16.0

* Mon Dec 20 2021 Remi Collet <remi@remirepo.net> - 2.15.0-1
- update to 2.15.0

* Wed Nov 17 2021 Remi Collet <remi@remirepo.net> - 2.14.2-1
- update to 2.14.2

* Thu Oct 14 2021 Remi Collet <remi@remirepo.net> - 2.14.1-1
- update to 2.14.1

* Wed Oct 13 2021 Remi Collet <remi@remirepo.net> - 2.14.0-1
- update to 2.14.0

* Wed Oct 13 2021 Remi Collet <remi@remirepo.net> - 2.13.1-1
- update to 2.13.1
- keep compatibility using laminas-zendframework-bridge
  as this is only used using compat autolader
- raise dependency on laminas-eventmanager 3.4
- raise dependency on laminas-json 3.3
- raise dependency on laminas-stdlib 3.6

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan  7 2021 Remi Collet <remi@remirepo.net> - 2.12.0-1
- update to 2.12.0
- raise dependency on PHP 7.3
- raise dependency on laminas-stdlib 3.2.1
- switch to phpunit9

* Wed Dec 16 2020 Remi Collet <remi@remirepo.net> - 2.11.5-1
- update to 2.11.5
- switch to phpunit7

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 15 2020 Remi Collet <remi@remirepo.net> - 2.11.4-1
- switch to Laminas

* Thu Dec  5 2019 Remi Collet <remi@remirepo.net> - 2.11.4-1
- update to 2.11.4

* Sun Oct 13 2019 Remi Collet <remi@remirepo.net> - 2.11.3-1
- update to 2.11.3
- drop patches merged upstream

* Fri Oct 11 2019 Remi Collet <remi@remirepo.net> - 2.11.2-3
- add patches for PHP 7.4 from
  https://github.com/zendframework/zend-view/pull/192
  https://github.com/zendframework/zend-view/pull/195

* Wed Feb 20 2019 Remi Collet <remi@remirepo.net> - 2.11.2-1
- update to 2.11.2

* Tue Dec 11 2018 Remi Collet <remi@remirepo.net> - 2.11.1-1
- update to 2.11.1
- add mandatory dependency on zendframework/zend-json
- add optional dependency on zendframework/zend-mvc-plugin-flashmessenger
- raise dependency on zendframework/zend-mvc 2.7.14
- use range dependencies

* Thu Dec  6 2018 Remi Collet <remi@remirepo.net> - 2.10.0-4
- cleanup for EL-8

* Thu Jan 18 2018 Remi Collet <remi@remirepo.net> - 2.10.0-1
- Update to 2.10.0
- only use phpunit6

* Tue Dec 12 2017 Remi Collet <remi@remirepo.net> - 2.9.0-3
- switch from zend-loader to fedora/autoloader

* Tue Mar 21 2017 Remi Collet <remi@remirepo.net> - 2.9.0-1
- Update to 2.9.0
- raise dependency on PHP 5.6
- use phpunit6 on F26+

* Tue Mar 21 2017 Remi Collet <remi@remirepo.net> - 2.8.2-1
- Update to 2.8.2

* Tue Feb 21 2017 Remi Collet <remi@fedoraproject.org> - 2.8.1-2
- add missing BR, fix FTBFS #1424088

* Fri Jul  1 2016 Remi Collet <remi@fedoraproject.org> - 2.8.1-1
- version 2.8.1

* Wed Jun 22 2016 Remi Collet <remi@fedoraproject.org> - 2.8.0-1
- version 2.8.0
- add zf_templatemap_generator (dropped from zf2)

* Thu May 12 2016 Remi Collet <remi@fedoraproject.org> - 2.7.0-1
- version 2.7.0

* Tue Apr 19 2016 Remi Collet <remi@fedoraproject.org> - 2.6.7-1
- version 2.6.7

* Mon Mar 21 2016 Remi Collet <remi@fedoraproject.org> - 2.6.5-1
- version 2.6.5

* Mon Mar 21 2016 Remi Collet <remi@fedoraproject.org> - 2.6.4-2
- add patch for zend-navigation issue, see:
  https://github.com/zendframework/zend-navigation/issues/23

* Thu Mar  3 2016 Remi Collet <remi@fedoraproject.org> - 2.6.4-1
- version 2.6.4

* Tue Feb 23 2016 Remi Collet <remi@fedoraproject.org> - 2.6.3-1
- version 2.6.3

* Fri Feb 19 2016 Remi Collet <remi@fedoraproject.org> - 2.6.2-1
- version 2.6.2

* Thu Feb 18 2016 Remi Collet <remi@fedoraproject.org> - 2.6.1-1
- version 2.6.1

* Thu Feb 18 2016 Remi Collet <remi@fedoraproject.org> - 2.6.0-1
- version 2.6.0
- raise dependency on zend-eventmanager >= 2.6.2
- raise dependency on zend-stdlib >= 2.7

* Wed Jan 20 2016 Remi Collet <remi@fedoraproject.org> - 2.5.3-1
- version 2.5.3

* Thu Aug  6 2015 Remi Collet <remi@fedoraproject.org> - 2.5.2-1
- version 2.5.2

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.1-1
- initial package
