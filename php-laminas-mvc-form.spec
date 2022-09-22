# remirepo/Fedora spec file for php-laminas-mvc-form
#
# Copyright (c) 2016-2021 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    9e03ded7e7605a5b1e34a2f187b14d7fd4f1e44f
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-mvc-form
%global zf_name      zend-mvc-form
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Mvc
%global subproj      Form

Name:           php-%{gh_project}
Version:        1.2.0
Release:        3%{?dist}
Summary:        %{namespace} Framework %{library}/%{subproj} component

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
# For test
BuildRequires:  php-cli
BuildRequires: (php-autoloader(%{gh_owner}/laminas-code)                 >= 3.5.1  with php-autoloader(%{gh_owner}/laminas-code)                 < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-form)                 >= 2.17.0 with php-autoloader(%{gh_owner}/laminas-form)                 < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-i18n)                 >= 2.11.1 with php-autoloader(%{gh_owner}/laminas-i18n)                 < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.2    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)

# From composer, "require": {
#        "php": "^7.3 || ~8.0.0",
#        "laminas/laminas-code": "^3.5.1",
#        "laminas/laminas-form": "^2.17.0",
#        "laminas/laminas-i18n": "^2.11.1"
Requires:       php(language) >= 7.3
Requires:      (php-autoloader(%{gh_owner}/laminas-code)                 >= 3.5.1  with php-autoloader(%{gh_owner}/laminas-code)                 < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-form)                 >= 2.17.0 with php-autoloader(%{gh_owner}/laminas-form)                 < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-i18n)                 >= 2.11.1 with php-autoloader(%{gh_owner}/laminas-i18n)                 < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.2    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# Autoloader
Requires:       php-composer(fedora/autoloader)

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 1.0.1
Provides:       php-zendframework-%{zf_name}              = %{version}
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
%{gh_project} is a metapackage that provides a single package for
installing all packages necessary to fully use laminas-form under laminas-mvc,
including:

* laminas/laminas-code
* laminas/laminas-form
* laminas/laminas-i18n

i18n integration: this package only requires laminas-i18n, and not
laminas-mvc-i18n. This is to allow providing the bare minimum required
to use laminas-form, as its base view helper extends from the base
laminas-i18n view helper. If you want to provide translations for your
form elements, please install laminas-mvc-i18n as well.


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
: Create autoloader
cat << 'EOF' | tee autoload.php
<?php
require_once '/usr/share/php/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/Code/autoload.php',
    '%{php_home}/%{namespace}/Form/autoload.php',
    '%{php_home}/%{namespace}/I18n/autoload.php',
]);
EOF

cat << 'EOF' | tee zf.php
<?php
require_once '%{php_home}/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/ZendFrameworkBridge/autoload.php',
    dirname(dirname(dirname(__DIR__))) . '/%{namespace}/%{library}/%{subproj}/autoload.php',
]);
EOF


%install
: Laminas library
install -Dpm 644 autoload.php %{buildroot}%{php_home}/%{namespace}/%{library}/%{subproj}/autoload.php
 
: Zend equiv
install -Dpm 644 zf.php %{buildroot}%{php_home}/Zend/%{library}/%{subproj}/autoload.php


%check
: Ensure autoloader works
php -r '
require "%{buildroot}%{php_home}/%{namespace}/%{library}/%{subproj}/autoload.php";
exit (class_exists("\\%{namespace}\\Form\\Factory") ? 0 : 1);
'

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend/%{library}/%{subproj}/autoload.php";
exit (class_exists("\\Zend\\Form\\Factory") ? 0 : 1);
'


%files
%license LICENSE
%doc *.md
%doc composer.json
%dir %{php_home}/Zend/%{library}
     %{php_home}/Zend/%{library}/%{subproj}
%dir %{php_home}/%{namespace}/%{library}
     %{php_home}/%{namespace}/%{library}/%{subproj}


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 11 2021 Remi Collet <remi@remirepo.net> - 1.2.0-1
- update to 1.2.0 (no change)
- keep compatibility using laminas-zendframework-bridge
  as this is only used using compat autolader

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May  3 2021 Remi Collet <remi@remirepo.net> - 1.1.0-1
- update to 1.1.0
- raise dependency on PHP 7.3
- raise dependency on laminas-code 3.5
- raise dependency on laminas-form 2.16
- raise dependency on laminas-i18n 2.11
- raise dependency on laminas-zendframework-bridge 1.2

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 15 2020 Remi Collet <remi@remirepo.net> - 1.0.0-1
- switch to Laminas
- use range dependencies

* Tue Dec 12 2017 Remi Collet <remi@remirepo.net> - 1.0.0-5
- switch from zend-loader to fedora/autoloader

* Tue Jul 26 2016 Remi Collet <remi@fedoraproject.org> - 1.0.0-2
- fix summary

* Wed Jun 29 2016 Remi Collet <remi@fedoraproject.org> - 1.0.0-1
- initial package

