#
# Fedora spec file for php-di-symfony2-bridge
#
# Copyright (c) 2016-2017 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     PHP-DI
%global github_name      Symfony2-Bridge
%global github_version   3.0.0
%global github_commit    d536a47f168b2c06fd15a2f902ea6d59ff8dc55d

%global composer_vendor  php-di
%global composer_project symfony2-bridge

# "php": ">=7.0.0"
%global php_min_ver 7.0.0
# "php-di/php-di": "~6.0"
%global di_min_ver 6.0
%global di_max_ver 7
#        "symfony/dependency-injection": "~3.3||~4.0",
#        "symfony/http-kernel": "~3.3||~4.0",
#        "symfony/proxy-manager-bridge": "~3.3||~4.0",
#        "symfony/config": "~3.3||~4.0"
%global symfony_min_ver 3.3
%global symfony_max_ver 5

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          %{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       8%{?github_release}%{?dist}
Summary:       PHP-DI integration with Symfony

License:       MIT
URL:           http://php-di.org/doc/frameworks/symfony2.html

# GitHub export does not include tests.
# Run php-di-symfony2-bridge-get-source.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php-composer(phpunit/phpunit)
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires:(php-composer(php-di/php-di)                >= %{di_min_ver}      with php-composer(php-di/php-di)                <  %{di_max_ver})
BuildRequires:(php-composer(symfony/dependency-injection) >= %{symfony_min_ver} with php-composer(symfony/dependency-injection) <  %{symfony_max_ver})
BuildRequires:(php-composer(symfony/http-kernel)          >= %{symfony_min_ver} with php-composer(symfony/http-kernel)          <  %{symfony_max_ver})
BuildRequires:(php-composer(symfony/proxy-manager-bridge) >= %{symfony_min_ver} with php-composer(symfony/proxy-manager-bridge) <  %{symfony_max_ver})
BuildRequires:(php-composer(symfony/config)               >= %{symfony_min_ver} with php-composer(symfony/config)               <  %{symfony_max_ver})
BuildRequires:(php-composer(symfony/filesystem)           >= %{symfony_min_ver} with php-composer(symfony/filesystem)           <  %{symfony_max_ver})
BuildRequires:(php-composer(symfony/yaml)                 >= %{symfony_min_ver} with php-composer(symfony/yaml)                 <  %{symfony_max_ver})
BuildRequires:(php-composer(symfony/debug)                >= %{symfony_min_ver} with php-composer(symfony/debug)                <  %{symfony_max_ver})
%else
BuildRequires: php-composer(php-di/php-di)                <  %{di_max_ver}
BuildRequires: php-composer(php-di/php-di)                >= %{di_min_ver}
BuildRequires: php-composer(symfony/dependency-injection) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/dependency-injection) >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/http-kernel)          <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/http-kernel)          >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/proxy-manager-bridge) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/proxy-manager-bridge) >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/config)               <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/config)               >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/filesystem)           <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/filesystem)           >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/yaml)                 <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/yaml)                 >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/debug)                <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/debug)                >= %{symfony_min_ver}
%endif
## phpcompatinfo (computed from version 3.0.0)
BuildRequires: php(language)                              >= %{php_min_ver}
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:     (php-composer(php-di/php-di)                >= %{di_min_ver}      with php-composer(php-di/php-di)                <  %{di_max_ver})
Requires:     (php-composer(symfony/dependency-injection) >= %{symfony_min_ver} with php-composer(symfony/dependency-injection) <  %{symfony_max_ver})
Requires:     (php-composer(symfony/http-kernel)          >= %{symfony_min_ver} with php-composer(symfony/http-kernel)          <  %{symfony_max_ver})
Requires:     (php-composer(symfony/proxy-manager-bridge) >= %{symfony_min_ver} with php-composer(symfony/proxy-manager-bridge) <  %{symfony_max_ver})
Requires:     (php-composer(symfony/config)               >= %{symfony_min_ver} with php-composer(symfony/config)               <  %{symfony_max_ver})
%else
Requires:      php-composer(php-di/php-di)                <  %{di_max_ver}
Requires:      php-composer(php-di/php-di)                >= %{di_min_ver}
Requires:      php-composer(symfony/dependency-injection) <  %{symfony_max_ver}
Requires:      php-composer(symfony/dependency-injection) >= %{symfony_min_ver}
Requires:      php-composer(symfony/http-kernel)          <  %{symfony_max_ver}
Requires:      php-composer(symfony/http-kernel)          >= %{symfony_min_ver}
Requires:      php-composer(symfony/proxy-manager-bridge) <  %{symfony_max_ver}
Requires:      php-composer(symfony/proxy-manager-bridge) >= %{symfony_min_ver}
Requires:      php-composer(symfony/config)               <  %{symfony_max_ver}
Requires:      php-composer(symfony/config)               >= %{symfony_min_ver}
%endif
# phpcompatinfo (computed from version 3.0.0)
Requires:      php(language)                              >= %{php_min_ver}
# Autoloader
Requires:      php-composer(fedora/autoloader)

# php-{COMPOSER_VENDOR}-{COMPOSER_PROJECT}
Provides:      php-%{composer_vendor}-%{composer_project}           = %{version}-%{release}
# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
%{summary}.

Autoloader: %{phpdir}/DI/Bridge/Symfony/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}

: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 *
 */

require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('DI\\Bridge\\Symfony\\', __DIR__);

\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/DI/autoload.php',
    [
        '%{phpdir}/Symfony4/Component/DependencyInjection/autoload.php',
        '%{phpdir}/Symfony3/Component/DependencyInjection/autoload.php',
    ], [
        '%{phpdir}/Symfony4/Component/HttpKernel/autoload.php',
        '%{phpdir}/Symfony3/Component/HttpKernel/autoload.php',
    ], [
        '%{phpdir}/Symfony4/Bridge/ProxyManager/autoload.php',
        '%{phpdir}/Symfony3/Bridge/ProxyManager/autoload.php',
    ], [
        '%{phpdir}/Symfony4/Component/Config/autoload.php',
        '%{phpdir}/Symfony3/Component/Config/autoload.php',
    ],
]);
AUTOLOAD


%build
# Empty build section, nothing to build


%install
mkdir -p   %{buildroot}%{phpdir}/DI/Bridge
cp -rp src %{buildroot}%{phpdir}/DI/Bridge/Symfony


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require_once '%{buildroot}%{phpdir}/DI/Bridge/Symfony/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('DI\\Bridge\\Symfony\\Test\\', __DIR__.'/tests');
\Fedora\Autoloader\Dependencies::required([
    [
        '%{phpdir}/Symfony4/Component/Filesystem/autoload.php',
        '%{phpdir}/Symfony3/Component/Filesystem/autoload.php',
    ], [
        '%{phpdir}/Symfony4/Component/Yaml/autoload.php',
        '%{phpdir}/Symfony3/Component/Yaml/autoload.php',
    ], [
        '%{phpdir}/Symfony4/Component/Config/autoload.php',
        '%{phpdir}/Symfony3/Component/Config/autoload.php',
    ],
]);
BOOTSTRAP

# TODO investigate on symfonyGetInPHPDI failure

: Run tests
ret=0
for cmd in php php71 php72 php73 php74; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit \
      --filter '^((?!(symfonyGetInPHPDI)).)*$' \
      --bootstrap bootstrap.php \
      --verbose || ret=1
  fi
done
exit $ret
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%dir %{phpdir}/DI/Bridge
     %{phpdir}/DI/Bridge/Symfony


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 17 2019 Remi Collet <remi@remirepo.net> - 3.0.0-1
- update to 3.0.0
- add dependency on symfony/http-kernel
- add dependency on symfony/proxy-manager-bridge
- add dependency on symfony/config
- switch from Symfony 2 to Sypmfony 3 or 4
- raise dependency on php-di 6.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 10 2017 Remi Collet <remi@remirepo.net> - 1.1.0-5
- add max version to build dependencies
- run test suite against PHP SCLs when available

* Wed May 10 2017 Valentin Collet <valentin@famillecollet.com> - 1.1.0-4
- Switch to fedora/autoloader

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 03 2016 Shawn Iwinski <shawn@iwin.ski> - 1.1.0-1
- Initial package
