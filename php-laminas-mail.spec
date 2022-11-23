# remirepo/Fedora spec file for php-laminas-mail
#
# Copyright (c) 2015-2022 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%bcond_without tests

%global gh_commit    0516586f6bf4d47f855cbef040870ac3a324a9a8
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-mail
%global zf_name      zend-mail
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Mail

Name:           php-%{gh_project}
Version:        2.20.0
Release:        1%{?dist}
Summary:        %{namespace} Framework %{library} component

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{gh_commit}/%{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
# Tests
%if %{with tests}
BuildRequires:  php(language) >= 8.0
BuildRequires:  php-ctype
BuildRequires:  php-date
BuildRequires:  php-iconv
BuildRequires:  php-intl
BuildRequires:  php-mbstring
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires: (php-autoloader(%{gh_owner}/laminas-loader)               >= 2.8.0  with php-autoloader(%{gh_owner}/laminas-loader)               < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-mime)                 >= 2.10   with php-autoloader(%{gh_owner}/laminas-mime)                 < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.11.0 with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-validator)            >= 2.23.0 with php-autoloader(%{gh_owner}/laminas-validator)            < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
BuildRequires: (php-composer(webmozart/assert)                           >= 1.11.0 with php-composer(webmozart/assert)                           < 2)
# From composer, "require-dev": {
#        "laminas/laminas-coding-standard": "~2.4.0",
#        "laminas/laminas-crypt": "^3.9.0",
#        "laminas/laminas-db": "^2.15.0",
#        "laminas/laminas-servicemanager": "^3.19",
#        "phpunit/phpunit": "^9.5.25",
#        "psalm/plugin-phpunit": "^0.18.0",
#        "symfony/process": "^6.0.11",
#        "vimeo/psalm": "^4.29"
BuildRequires: (php-autoloader(%{gh_owner}/laminas-crypt)                >= 3.9.0  with php-autoloader(%{gh_owner}/laminas-crypt)                < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-db)                   >= 2.15.0 with php-autoloader(%{gh_owner}/laminas-db)                   < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.19   with php-autoloader(%{gh_owner}/laminas-servicemanager)       < 4)
# ignore min version
BuildRequires: (php-composer(symfony/process)                            >= 4      with php-composer(symfony/process)                            < 6)
BuildRequires:  phpunit9 >= 9.5.25
%global phpunit %{_bindir}/phpunit9
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "~8.0.0 || ~8.1.0 || ~8.2.0",
#        "ext-iconv": "*",
#        "laminas/laminas-loader": "^2.8.0",
#        "laminas/laminas-mime": "^2.10.0",
#        "laminas/laminas-stdlib": "^3.11.0",
#        "laminas/laminas-validator": "^2.23.0",
#        "symfony/polyfill-mbstring": "^1.162.0",
#        "webmozart/assert": "^1.11",
#        "symfony/polyfill-intl-idn": "^1.26.0"
Requires:       php(language) >= 8.0
Requires:       php-iconv
Requires:       php-mbstring
Requires:      (php-autoloader(%{gh_owner}/laminas-loader)               >= 2.8.0  with php-autoloader(%{gh_owner}/laminas-loader)               < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-mime)                 >= 2.10   with php-autoloader(%{gh_owner}/laminas-mime)                 < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.11.0 with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-validator)            >= 2.23.0 with php-autoloader(%{gh_owner}/laminas-validator)            < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
Requires:      (php-composer(webmozart/assert)                           >= 1.11.0 with php-composer(webmozart/assert)                           < 2)
# From composer, "suggest": {
#        "laminas/laminas-crypt": "Crammd5 support in SMTP Auth",
#        "laminas/laminas-servicemanager": "^2.7.10 || ^3.3.1 when using SMTP to deliver messages"
Suggests:       php-autoloader(%{gh_owner}/laminas-crypt)
Suggests:       php-autoloader(%{gh_owner}/laminas-servicemanager)
# From phpcompatinfo report
Recommends:     php-imap
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 2.16.0
Requires:       php-ctype
Requires:       php-date
Requires:       php-intl
Requires:       php-pcre
Requires:       php-spl

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 2.10.1
Provides:       php-zendframework-%{zf_name}              = %{version}
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
%{namespace}\Mail provides generalized functionality to compose and send both text
and MIME-compliant multipart email messages. Mail can be sent with %{namespace}\Mail
via the Mail\Transport\Sendmail, Mail\Transport\Smtp or the
Mail\Transport\File transport. Of course, you can also implement your own
transport by implementing the Mail\Transport\TransportInterface.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
: Create autoloader
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/Loader/autoload.php',
    '%{php_home}/%{namespace}/Mime/autoload.php',
    '%{php_home}/%{namespace}/Stdlib/autoload.php',
    '%{php_home}/%{namespace}/Validator/autoload.php',
    '%{php_home}/Webmozart/Assert/autoload.php',
]);
\Fedora\Autoloader\Dependencies::optional([
    '%{php_home}/%{namespace}/ServiceManager/autoload.php',
    '%{php_home}/%{namespace}/Crypt/autoload.php',
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
require_once '%{buildroot}%{php_home}/%{namespace}/%{library}/autoload.php';
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/Crypt/autoload.php',
    '%{php_home}/%{namespace}/Db/autoload.php',
    [
        '%{php_home}/Symfony5/Component/Process/autoload.php',
        '%{php_home}/Symfony4/Component/Process/autoload.php',
    ],
]);
\Fedora\Autoloader\Autoload::addPsr4('%{namespace}Test\\%{library}\\', dirname(__DIR__) . '/test');
EOF

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend/%{library}/autoload.php";
exit (class_exists("\\Zend\\%{library}\\Message") ? 0 : 1);
'

: upstream test suite
# testCanUseTraversableAsSpec use Composer\\InstalledVersions
ret=0
for cmdarg in "php %{phpunit}" php80 php81 php82; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit9} \
      --filter '^((?!(testCanUseTraversableAsSpec)).)*$' \
      || ret=1
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
* Mon Nov 21 2022 Remi Collet <remi@remirepo.net> - 2.20.0-1
- update to 2.20.0

* Mon Oct 17 2022 Remi Collet <remi@remirepo.net> - 2.19.0-1
- update to 2.19.0

* Tue Sep 20 2022 Remi Collet <remi@remirepo.net> - 2.18.0-1
- update to 2.18.0
- raise dependency on laminas-mime 2.10

* Mon Aug  8 2022 Remi Collet <remi@remirepo.net> - 2.17.0-1
- update to 2.17.0
- raise dependency on laminas-stdlib 3.11.0
- raise dependency on laminas-validator 2.23.0
- raise dependency on webmozart/assert 1.11.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 24 2022 Remi Collet <remi@remirepo.net> - 2.16.0-1
- update to 2.16.0
- drop dependency on true/punycode
- add dependency on intl extension

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Sep 24 2021 Remi Collet <remi@remirepo.net> - 2.15.1-1
- update to 2.15.1
- keep compatibility using laminas-zendframework-bridge
  as this is only used using compat autolader
- raise dependency on laminas-loader 2.8
- raise dependency on laminas-mime 2.9.1
- raise dependency on laminas-stdlib 3.6
- raise dependency on laminas-validator 2.15
- add dependency on webmozart/assert

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 20 2021 Remi Collet <remi@remirepo.net> - 2.14.1-1
- update to 2.14.1

* Thu Mar 18 2021 Remi Collet <remi@remirepo.net> - 2.14.0-1
- update to 2.14.0

* Mon Feb 15 2021 Remi Collet <remi@remirepo.net> - 2.13.1-1
- update to 2.13.1
- drop patch merged upstream
- add dependency on mbstring extension

* Wed Jan 27 2021 Remi Collet <remi@remirepo.net> - 2.13.0-1
- update to 2.13.0
- raise dependency on PHP 7.3
- add patch for PHP 8 from
  https://github.com/laminas/laminas-mail/pull/134
- switch to phpunit9

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan  6 2021 Remi Collet <remi@remirepo.net> - 2.12.5-1
- update to 2.12.5

* Thu Aug 13 2020 Remi Collet <remi@remirepo.net> - 2.12.3-1
- update to 2.12.3

* Tue Aug 11 2020 Remi Collet <remi@remirepo.net> - 2.12.2-1
- update to 2.12.2
- raise dependency on PHP 7.1

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul  1 2020 Remi Collet <remi@remirepo.net> - 2.11.0-1
- update to 2.11.0

* Wed Apr 22 2020 Remi Collet <remi@remirepo.net> - 2.10.1-1
- update to 2.10.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Remi Collet <remi@remirepo.net> - 2.10.0-2
- cleanup

* Thu Jan  9 2020 Remi Collet <remi@remirepo.net> - 2.10.0-1
- switch to Laminas

* Wed Oct  9 2019 Remi Collet <remi@remirepo.net> - 2.10.0-6
- add patch for PHP 7.4 from
  https://github.com/zendframework/zend-mail/pull/244

* Thu Jun  7 2018 Remi Collet <remi@remirepo.net> - 2.10.0-2
- update to 2.10.0
- lower dependency on PHP 5.6
- raise dependency on zend-validator 2.10.2
- add dependency on true/punycode
- switch to phpunit7

* Fri Mar  2 2018 Remi Collet <remi@remirepo.net> - 2.9.0-1
- Update to 2.9.0
- raise dependency on PHP 7.1
- raise dependency on zend-validator 2.10.2
- always use phpunit6
- use range dependencies on F27+

* Tue Dec 12 2017 Remi Collet <remi@remirepo.net> - 2.8.0-4
- switch from zend-loader to fedora/autoloader
- fix FTBFS from Koschei, ignore 1 test, reported as
  https://github.com/zendframework/zend-mail/issues/183

* Fri Oct 20 2017 Remi Collet <remi@remirepo.net> - 2.8.0-3
- fix FTBFS from Koschei
- add patch for latest PHPUnit from
  https://github.com/zendframework/zend-mail/pull/174

* Fri Jun  9 2017 Remi Collet <remi@remirepo.net> - 2.8.0-1
- Update to 2.8.0
- raise dependency on PHP 5.6
- use phpunit6 on F26+

* Wed Apr 12 2017 Remi Collet <remi@fedoraproject.org> - 2.7.3-2
- add upstream patch to fix FTBFS (from Koschei)
  https://github.com/zendframework/zend-mail/issues/136

* Wed Feb 15 2017 Remi Collet <remi@fedoraproject.org> - 2.7.3-1
- update to 2.7.3

* Wed Dec 21 2016 Remi Collet <remi@fedoraproject.org> - 2.7.2-1
- update to 2.7.2

* Wed May 11 2016 Remi Collet <remi@fedoraproject.org> - 2.7.1-1
- update to 2.7.1

* Tue Apr 12 2016 Remi Collet <remi@fedoraproject.org> - 2.7.0-1
- update to 2.7.0
- zend-crypt is now optional

* Thu Feb 25 2016 Remi Collet <remi@fedoraproject.org> - 2.6.1-1
- update to 2.6.1

* Fri Feb 19 2016 Remi Collet <remi@fedoraproject.org> - 2.6.0-1
- update to 2.6.0
- raise dependency on zend-crypt >= 2.6
- raise dependency on zend-stdlib >= 2.7
- raise dependency on zend-validator >= 2.6

* Fri Sep 11 2015 Remi Collet <remi@fedoraproject.org> - 2.5.2-1
- update to 2.5.2
- raise minimum PHP version to 5.5

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.1-1
- initial package
