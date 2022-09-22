#
# Fedora spec file for php-Metadata
#
# Copyright (c) 2013-2020 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     schmittjoh
%global github_name      metadata
%global github_version   1.7.0
%global github_commit    e5854ab1aa643623dc64adde718a8eec32b957a8

%global composer_vendor  jms
%global composer_project metadata

# "php": ">=5.3.0"
%global php_min_ver 5.3.0
# "doctrine/cache" : "~1.0"
#     NOTE: min version not 1.0 because autoloader required
%global doctrine_cache_min_ver 1.4.1
%global doctrine_cache_max_ver 2.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-Metadata
Version:       %{github_version}
Release:       5%{?github_release}%{?dist}
Summary:       Class/method/property metadata management in PHP

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Tests
%if %{with_tests}
BuildRequires: php-composer(phpunit/phpunit)
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
## phpcompatinfo (computed from version 1.7.0)
BuildRequires: php-date
BuildRequires: php-reflection
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 1.7.0)
Requires:      php-date
Requires:      php-reflection
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

%if 0%{?fedora} >= 21 || 0%{?rhel} >= 8
# phpcompatinfo (computed from version 1.6.0)
Suggests:      php-composer(doctrine/cache)
Suggests:      php-composer(psr/cache)
Suggests:      php-composer(symfony/dependency-injection)
%endif

# Standard "php-{COMPOSER_VENDOR}-{COMPOSER_PROJECT}" naming
Provides:      php-%{composer_vendor}-%{composer_project} = %{version}-%{release}
# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
This library provides some commonly needed base classes for managing metadata
for classes, methods and properties. The metadata can come from many different
sources (annotations, YAML/XML/PHP configuration files).

The metadata classes are used to abstract away that source and provide a common
interface for all of them.

Autoloader: %{phpdir}/Metadata/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/Metadata/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Metadata\\', __DIR__);

\Fedora\Autoloader\Dependencies::optional(array(
    '%{phpdir}/Doctrine/Common/Cache/autoload.php',
    '%{phpdir}/Psr/Cache/autoload.php',
    '%{phpdir}/Symfony/Component/DependencyInjection/autoload.php',
));
AUTOLOAD



%install
mkdir -p %{buildroot}%{phpdir}
cp -rp src/Metadata %{buildroot}%{phpdir}/


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require_once '%{buildroot}%{phpdir}/Metadata/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Metadata\\Tests\\', __DIR__.'/tests/Metadata/Tests');
BOOTSTRAP

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in "" %{?rhel:php54 php55} php56 php70 php71 php72 php73 php74; do
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
%doc *.md
%doc *.rst
%doc composer.json
%{phpdir}/Metadata


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 17 2020 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.7.0-1
- Update to 1.7.0
- Change license from ASL 2.0 to MIT

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 07 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.6.0-4
- Bump release for rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.6.0-1
- Updated to 1.6.0
- Switched autoloader to php-composer(fedora/autoloader)
- Test with SCLs if available

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jul 11 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.5.1-3
- Added autoloader
- Added standard "php-{COMPOSER_VENDOR}-{COMPOSER_PROJECT}" naming provides

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jul 19 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.5.1-1
- Updated to 1.5.1 (BZ #1119425)
- Added "php-composer(jms/metadata)" virtual provide
- Added option to build without tests ("--without tests")

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 30 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.5.0-2
- Updated dependencies to match newly available pkgs
  -- php-pear(pear.doctrine-project.org/DoctrineCommon) => php-doctrine-cache
     (cache separated out from common)
  -- php-pear(pear.symfony.com/DependencyInjection) => php-symfony-dependencyinjection
- Doctrine cache required instead of just build requirement

* Fri Nov 15 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.5.0-1
- Updated to 1.5.0 (BZ #1001125)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Mar 30 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.3.0-1
- Updated to version 1.3.0 (BZ #929410)
- Removed tests sub-package

* Wed Jan 23 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1.1-1
- Initial package
