#
# Fedora spec file for php-SymfonyCmfRouting
#
# Copyright (c) 2013-2016 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     symfony-cmf
%global github_name      routing
%global github_version   1.4.1
%global github_commit    fb1e7f85ff8c6866238b7e73a490a0a0243ae8ac

%global composer_vendor  symfony-cmf
%global composer_project routing

# "php": "^5.3.9|^7.0"
%global php_min_ver     5.3.9
# "symfony/config": "^2.2|3.*"
# "symfony/dependency-injection": "^2.0.5|3.*"
# "symfony/event-dispatcher": "^2.1|3.*"
# "symfony/http-kernel": "^2.2|3.*"
# "symfony/routing": "^2.2|3.*"
## NOTE: Min version not 2.2 because autoloaders required
%global symfony_min_ver 2.7.1
%global symfony_max_ver 4.0
# "psr/log": "1.*"
## NOTE: Min version not 1.0 because autoloader required
%global psr_log_min_ver 1.0.1
%global psr_log_max_ver 2.0

# Build using "--without tests" to disable tests
%global with_tests  0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-SymfonyCmfRouting
Version:       %{github_version}
Release:       11%{?dist}
Summary:       Extends the Symfony2 routing component for dynamic routes and chaining

License:       MIT
URL:           http://symfony.com/doc/master/cmf/book/routing.html
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Tests
%if %{with_tests}
BuildRequires: php-composer(phpunit/phpunit)
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(psr/log) <  %{psr_log_max_ver}
BuildRequires: php-composer(psr/log) >= %{psr_log_min_ver}
BuildRequires: php-composer(symfony/config) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/config) >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/dependency-injection) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/dependency-injection) >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/event-dispatcher) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/event-dispatcher) >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/http-kernel) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/http-kernel) >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/routing) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/routing) >= %{symfony_min_ver}
## phpcompatinfo (computed from version 1.4.1)
BuildRequires: php-pcre
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-composer(psr/log) >= %{psr_log_min_ver}
Requires:      php-composer(psr/log) <  %{psr_log_max_ver}
Requires:      php-composer(symfony/http-kernel) >= %{symfony_min_ver}
Requires:      php-composer(symfony/http-kernel) <  %{symfony_max_ver}
Requires:      php-composer(symfony/routing) >= %{symfony_min_ver}
Requires:      php-composer(symfony/routing) <  %{symfony_max_ver}
# phpcompatinfo (computed from version 1.4.1)
Requires:      php-pcre
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# composer.json: optional
%if 0%{?fedora} > 21
Suggests:      php-composer(symfony/event-dispatcher)
%endif

# php-{COMPOSER_VENDOR}-{COMPOSER_PROJECT}
Provides:      php-%{composer_vendor}-%{composer_project}           = %{version}-%{release}
# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
The Symfony CMF Routing component extends the Symfony2 core routing component.
It provides:
* A ChainRouter to run several routers in parallel
* A DynamicRouter that can load routes from any database and can generate
      additional information in the route match

Even though it has Symfony in its name, the Routing component does not need the
full Symfony2 Framework and can be used in standalone projects.

Autoloader: %{phpdir}/Symfony/Cmf/Component/Routing/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
cat <<'AUTOLOAD' | tee autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Symfony\\Cmf\\Component\\Routing\\', __DIR__);

\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/Psr/Log/autoload.php',
    array(
        '%{phpdir}/Symfony3/Component/HttpKernel/autoload.php',
        '%{phpdir}/Symfony/Component/HttpKernel/autoload.php',
    ),
    array(
        '%{phpdir}/Symfony3/Component/Routing/autoload.php',
        '%{phpdir}/Symfony/Component/Routing/autoload.php',
    ),
));

\Fedora\Autoloader\Dependencies::optional(array(
    array(
        '%{phpdir}/Symfony3/Component/EventDispatcher/autoload.php',
        '%{phpdir}/Symfony/Component/EventDispatcher/autoload.php',
    ),
));
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/Symfony/Cmf/Component/Routing
cp -rp * %{buildroot}%{phpdir}/Symfony/Cmf/Component/Routing/


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php

require_once '%{buildroot}%{phpdir}/Symfony/Cmf/Component/Routing/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4(
    'Symfony\\Cmf\\Component\\Routing\\Test\\',
    '%{buildroot}%{phpdir}/Symfony/Cmf/Component/Routing/Test'
);

\Fedora\Autoloader\Autoload::addPsr4(
    'Symfony\\Cmf\\Component\\Routing\\Tests\\',
    '%{buildroot}%{phpdir}/Symfony/Cmf/Component/Routing/Tests'
);

\Fedora\Autoloader\Dependencies::required(array(
    array(
        '%{phpdir}/Symfony3/Component/Config/autoload.php',
        '%{phpdir}/Symfony/Component/Config/autoload.php',
    ),
    array(
        '%{phpdir}/Symfony3/Component/DependencyInjection/autoload.php',
        '%{phpdir}/Symfony/Component/DependencyInjection/autoload.php',
    ),
));
BOOTSTRAP

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in "" %{?rhel:php54 php55} php56 php70 php71 php72; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose --bootstrap bootstrap.php || RETURN_CODE=1
     fi
 done
exit $RETURN_CODE
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc CHANGELOG.md
%doc README.md
%doc composer.json
%dir %{phpdir}/Symfony/Cmf
%dir %{phpdir}/Symfony/Cmf/Component
     %{phpdir}/Symfony/Cmf/Component/Routing
%exclude %{phpdir}/Symfony/Cmf/Component/Routing/LICENSE
%exclude %{phpdir}/Symfony/Cmf/Component/Routing/*.md
%exclude %{phpdir}/Symfony/Cmf/Component/Routing/composer.json
%exclude %{phpdir}/Symfony/Cmf/Component/Routing/phpunit.xml.dist
%exclude %{phpdir}/Symfony/Cmf/Component/Routing/Test*


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 22 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.4.1-1
- Update to 1.4.1
- Allow Symfony 3
- Add max versions to BuildRequires
- Switch autloader to fedora/autoloader

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov 03 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.4.0-1
- Updated to 1.4.0 (RHBZ #1297159)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.3.0-4
- Added autoloader dependency to build requires

* Wed Jan 20 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.3.0-3
- php-composer(*) virtual provide dependencies instead of direct package names
- Dropped max version build dependencies
- Increased Symfony min version from 2.2 to 2.3.31/2.7.3 for autoloaders
- Added "php-{COMPOSER_VENDOR}-{COMPOSER_PROJECT}" ("php-symfony-cmf-routing")
  virtual provide
- Suggest php-composer(symfony/event-dispatcher) instead of require
- Added autoloader

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Nov 13 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.3.0-1
- Updated to 1.3.0 (BZ #1096125)

* Mon Oct 20 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.0-1
- Updated to 1.2.0 (BZ #1096125)
- Enabled tests by default
- Updated URL, description, dependencies, %%check, and %%files
- Added "php-composer(symfony-cmf/routing)" virtual provide
- %%license usage

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Oct 30 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.1.0-1
- Updated to 1.1.0 (BZ #962129)
- Updated required pkg versions, required pkgs, summary, URL, and description
- php-common -> php(language)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 08 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.1-1
- Updated to version 1.0.1 (BZ #958188)
- Added php-pear(pear.symfony.com/HttpFoundation) require
- Only run tests with "--with tests" option
- Remove phpunit.xml.dist from packaging since tests themselves are not included

* Sat Mar 09 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.0-0.3.alpha4.20130306git4706313
- Added additional commits (snapshot) beyond tagged version 1.0.0-alpha4 which
  include several Symfony 2.2 fixes

* Tue Mar 05 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.0-0.2.alpha4.20130121git92ee467
- Added globals symfony_min_ver and symfony_max_ver
- Removed tests sub-package

* Thu Jan 31 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.0-0.1.alpha4.20130121git92ee467
- Initial package
