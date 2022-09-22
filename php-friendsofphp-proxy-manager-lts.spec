# remirepo/fedora spec file for php-friendsofphp-proxy-manager-lts
#
# Copyright (c) 2021-2022 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%global github_owner     FriendsOfPHP
%global github_name      proxy-manager-lts
%global github_version   1.0.12
%global github_commit    8419f0158715b30d4b99a5bd37c6a39671994ad7
%global github_short     %(c=%{github_commit}; echo ${c:0:7})
%global major            %nil

%global ns_project       ProxyManager

%global composer_vendor  friendsofphp
%global composer_project proxy-manager-lts

# Build using "--without tests" to disable tests
%bcond_without tests

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}%{major}
Version:       %{github_version}
Release:       2%{?github_release}%{?dist}
Summary:       OOP proxy wrappers utilities

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{name}-%{github_version}-%{github_short}.tgz
Source1:       makesrc.sh

BuildArch:     noarch
# As we use phpunit9
BuildRequires: php(language) >= 7.3
%if %{with tests}
BuildRequires: php-reflection
BuildRequires: php-pcre
BuildRequires: php-spl
BuildRequires:(php-composer(laminas/laminas-code) >= 4       with php-composer(laminas/laminas-code) <  5)
BuildRequires:(php-composer(symfony/filesystem)   >= 4.4.17  with php-composer(symfony/filesystem)   <  7)
## composer.json (require-dev)
#        "ext-phar":                     "*",
#        "symfony/phpunit-bridge":       "^5.4|^6.0"
%global phpunit %{_bindir}/phpunit9
BuildRequires:  %{phpunit}
%endif
## Autoloader
BuildRequires: php-fedora-autoloader-devel

# composer.json
#        "php":                       ">=7.1",
#        "laminas/laminas-code":      "~3.4.1|^4.0",
#        "symfony/filesystem":        "^4.4.17|^5.0|^6.0"
Requires:      php(language) >= 7.1
# prefer v4 required for PHP 8, better with PHP 7.4
Requires:     (php-composer(laminas/laminas-code) >= 4.0     with php-composer(laminas/laminas-code) <  5)
Requires:     (php-composer(symfony/filesystem)   >= 4.4.17  with php-composer(symfony/filesystem)   <  7)
# phpcompatinfo (computed from version 1.0.3)
Requires:      php-reflection
Requires:      php-pcre
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
This package is a fork of the excellent ocramius/proxy-manager library
that adds long term support for a wider range of PHP versions.

Unless they're caused by this very fork, please report issues and submit
new features to the origin library.

This fork:

* maintains compatibility with PHP >=7.1;
  supporting new versions of PHP is considered as a bugfix;
* won't bump the minimum supported version of PHP in a minor release;
* does not depend on Composer 2, thus can be used with Composer 1 if
  you need more time to migrate;
* uses a versioning policy that is friendly to progressive migrations
  while providing the latest improvements from the origin lib.

Autoloader: %{phpdir}/%{github_owner}/%{ns_project}%{major}/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
phpab --template fedora \
      --output src/autoload.php \
      src

cat <<'AUTOLOAD' | tee -a src/autoload.php

if (PHP_VERSION_ID < 70400) {
    $code = '%{phpdir}/Laminas/Code/autoload.php';
} else if (PHP_VERSION_ID < 80000) {
    $code = [
        '%{phpdir}/Laminas/Code4/autoload.php',
        '%{phpdir}/Laminas/Code/autoload.php',
    ];
} else {
    $code = '%{phpdir}/Laminas/Code4/autoload.php';
}
\Fedora\Autoloader\Dependencies::required([
    $code,
    [
        '%{phpdir}/Symfony6/Component/Filesystem/autoload.php',
        '%{phpdir}/Symfony5/Component/Filesystem/autoload.php',
        '%{phpdir}/Symfony4/Component/Filesystem/autoload.php',
    ],
]);
AUTOLOAD


%install
# fake "vendor" directory to avoid conflict with real ocramius library
mkdir -p %{buildroot}%{phpdir}/%{github_owner}/
cp -rp src %{buildroot}%{phpdir}/%{github_owner}/%{ns_project}%{major}


%check
%if %{with tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once "%{buildroot}%{phpdir}/%{github_owner}/%{ns_project}%{major}/autoload.php";
\Fedora\Autoloader\Autoload::addPsr4('ProxyManagerTest\\',      dirname(__DIR__) . "/tests/ProxyManagerTest");
\Fedora\Autoloader\Autoload::addPsr4('ProxyManagerTestAsset\\', dirname(__DIR__) . "/tests/ProxyManagerTestAsset");
\Fedora\Autoloader\Autoload::addPsr4('Laminas\\Server\\',       dirname(__DIR__) . "/tests/Stubbed/Laminas/Server");
EOF


: Upstream tests
ret=0
for cmdarg in "php %{phpunit}" php74 php80 php81; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit9} \
      --filter '^((?!(testCodeGeneration)).)*$' \
      --verbose || ret=1
  fi
done
exit $ret
%else
: Tests skipped
%endif


%files
%license LICENSE
%doc README.md
%doc composer.json
%dir %{phpdir}/%{github_owner}
     %{phpdir}/%{github_owner}/%{ns_project}%{major}


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu May  5 2022 Remi Collet <remi@remirepo.net> - 1.0.12-1
- update to 1.0.12

* Wed May  4 2022 Remi Collet <remi@remirepo.net> - 1.0.11-1
- update to 1.0.11

* Mon May  2 2022 Remi Collet <remi@remirepo.net> - 1.0.10-1
- update to 1.0.10

* Thu Mar  3 2022 Remi Collet <remi@remirepo.net> - 1.0.7-1
- update to 1.0.7

* Mon Feb 28 2022 Remi Collet <remi@remirepo.net> - 1.0.6-1
- update to 1.0.6

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue May 25 2021 Remi Collet <remi@remirepo.net> - 1.0.5-1
- update to 1.0.5

* Thu May 20 2021 Remi Collet <remi@remirepo.net> - 1.0.4-1
- update to 1.0.4

* Thu Jan 28 2021 Remi Collet <remi@remirepo.net> - 1.0.3-2
- fix description and summary

* Thu Jan 28 2021 Remi Collet <remi@remirepo.net> - 1.0.3-1
- Initial package
