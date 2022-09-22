#
# Fedora spec file for php-cilex1
#
# Copyright (c) 2017-2019 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     Cilex
%global github_name      Cilex
%global github_version   1.1.0
%global github_commit    7acd965a609a56d0345e8b6071c261fbdb926cb5

%global composer_vendor  cilex
%global composer_project cilex

# cilex/cilex: "cilex/console-service-provider": "1.*"
# Bundled: php-composer(cilex/console-service-provider)
%global cilex_console_service_provider_github_version 1.0.0
%global cilex_console_service_provider_github_commit  25ee3d1875243d38e1a3448ff94bdf944f70d24e

# cilex/cilex: "php": ">=5.3.3"
# cilex/console-service-provider: "php": ">=5.3.3"
%global php_min_ver 5.3.3
# cilex/cilex: "monolog/monolog": ">=1.0.0"
%global monolog_min_ver 1.0.0
%global monolog_max_ver 2.0
# cilex/cilex: "pimple/pimple": "~1.0"
# cilex/console-service-provider: "pimple/pimple": "1.*@dev"
%global pimple_min_ver 1.0
%global pimple_max_ver 2.0
# cilex/cilex: "symfony/finder": "~2.1"
# cilex/cilex: "symfony/process": "~2.1"
# cilex/cilex: "symfony/validator": ">=1.0.0"
# cilex/cilex: "symfony/validator": "~2.1"
# cilex/cilex: "symfony/yaml": ">=1.0.0"
# cilex/console-service-provider: "symfony/console": "~2.1"
#     NOTE: Min version not 2.1 because autoloader required.
%global symfony_min_ver %{?el6:2.3.31}%{!?el6:2.7.1}
%global symfony_max_ver 3.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_project}1
Version:       %{github_version}
Release:       14%{?github_release}%{?dist}
Summary:       PHP micro-framework for Command line tools

# License file request for cilex/console-service-provider:
# https://github.com/Cilex/console-service-provider/issues/11
License:       MIT
URL:           http://cilex.github.io/
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

# Bundled: php-composer(cilex/console-service-provider)
Source1:       https://github.com/%{github_owner}/console-service-provider/archive/%{cilex_console_service_provider_github_commit}/%{name}-console-service-provider-%{cilex_console_service_provider_github_version}-%{cilex_console_service_provider_github_commit}.tar.gz

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
BuildRequires: php-composer(pimple/pimple) <  %{pimple_max_ver}
BuildRequires: php-composer(pimple/pimple) >= %{pimple_min_ver}
BuildRequires: php-composer(symfony/console) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/console) >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/finder) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/finder) >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/process) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/process) >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/validator) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/validator) >= %{symfony_min_ver}
## phpcompatinfo (computed from version 1.1.0 / cilex/console-service-provider 1.0.0)
BuildRequires: php-json
BuildRequires: php-pcre
BuildRequires: php-simplexml
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-composer(pimple/pimple) <  %{pimple_max_ver}
Requires:      php-composer(pimple/pimple) >= %{pimple_min_ver}
Requires:      php-composer(symfony/console) <  %{symfony_max_ver}
Requires:      php-composer(symfony/console) >= %{symfony_min_ver}
Requires:      php-composer(symfony/finder) <  %{symfony_max_ver}
Requires:      php-composer(symfony/finder) >= %{symfony_min_ver}
Requires:      php-composer(symfony/process) <  %{symfony_max_ver}
Requires:      php-composer(symfony/process) >= %{symfony_min_ver}
# phpcompatinfo (computed from version 1.1.0 / cilex/console-service-provider 1.0.0)
Requires:      php-json
Requires:      php-pcre
Requires:      php-simplexml
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Weak dependencies
%if 0%{?fedora} >= 21 || 0%{?rhel} >= 8
Suggests:      php-composer(monolog/monolog)
Suggests:      php-composer(symfony/validator)
Suggests:      php-composer(symfony/yaml)
%endif

# Standard "php-{COMPOSER_VENDOR}-{COMPOSER_PROJECT}" naming
Provides:      php-%{composer_vendor}-%{composer_project}1 = %{version}-%{release}
# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

# Bundled: php-composer(cilex/console-service-provider)
Provides:      bundled(php-cilex-console-service-provider) = %{cilex_console_service_provider_github_version}
Provides:      php-composer(cilex/console-service-provider) = %{cilex_console_service_provider_github_version}

%description
Cilex provides the means to build anything from small script collections to
complete command line applications.

Cilex aims to be:
* extensible, Cilex leverages Service Providers to add basic functionality,
  such as dealing with configuration files
* easy to use, an application and a series of commands; you don't need anything
  more to get started.
* Testable, Cilex leverages the Dependency Injection Container Pimple and the
  Symfony2 Console Component; which makes it easy to test your application.

Autoloader: %{phpdir}/Cilex1/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit} -a 1

: Remove unneeded file
rm -f src/Cilex/Compiler.php

: Docs and licenses
mkdir -p .rpm/{docs,licenses}
mv *.md composer.json .rpm/docs/
mv LICENSE .rpm/licenses/
# Bundled: php-composer(cilex/console-service-provider)
mkdir .rpm/docs/console-service-provider
mv \
    console-service-provider-%{cilex_console_service_provider_github_commit}/{*.md,composer.json} \
    .rpm/docs/console-service-provider/


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/Cilex/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Cilex\\', __DIR__);

\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/Pimple1/autoload.php',
    '%{phpdir}/Symfony/Component/Console/autoload.php',
    '%{phpdir}/Symfony/Component/Finder/autoload.php',
    '%{phpdir}/Symfony/Component/Process/autoload.php',
));

\Fedora\Autoloader\Dependencies::optional(array(
    '%{phpdir}/Monolog/autoload.php',
    '%{phpdir}/Symfony/Component/Validator/autoload.php',
    '%{phpdir}/Symfony/Component/Yaml/autoload.php',
));
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}
cp -rp src/Cilex %{buildroot}%{phpdir}/Cilex1

# Bundled: php-composer(cilex/console-service-provider)
cp -rp \
    console-service-provider-%{cilex_console_service_provider_github_commit}/src/Cilex/Provider/Console \
    %{buildroot}%{phpdir}/Cilex1/Provider/


%check
%if %{with_tests}
: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in php %{?rhel:php54 php55 php56} php70 php71 php72 php73; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose \
            --bootstrap %{buildroot}%{phpdir}/Cilex1/autoload.php \
            || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license .rpm/licenses/*
%doc .rpm/docs/*
%{phpdir}/Cilex1


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 26 2019 Remi Collet <remi@remirepo.net> - 1.1.0-7
- cleanup for EL-8

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 12 2017 Shawn Iwinski <shawn@iwin.ski> - 1.1.0-2
- Add link to upstream cilex/console-service-provider license file request
- Remove php-tokenizer dependency
- Add php-composer(cilex/console-service-provider) provides

* Sun Jun 04 2017 Shawn Iwinski <shawn@iwin.ski> - 1.1.0-1
- Initial package
