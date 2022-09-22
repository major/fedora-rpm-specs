#
# Fedora spec file for php-twig-extensions
#
# Copyright (c) 2014-2019 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     twigphp
%global github_name      Twig-extensions
%global github_version   1.5.4
%global github_commit    57873c8b0c1be51caa47df2cdb824490beb16202

%global composer_vendor  twig
%global composer_project extensions

# "symfony/translation": "^2.7|^3.4"
%global symfony_min_ver  2.7.1
%global symfony_max_ver  4.0
# "twig/twig": "^1.27|^2.0"
%global twig_min_ver     1.27
%global twig_max_ver     3.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       10%{?dist}
Summary:       Twig extensions

License:       MIT
URL:           http://twig-extensions.readthedocs.io/
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Tests
%if %{with_tests}
BuildRequires: php-composer(phpunit/phpunit)
## composer.json
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-composer(symfony/translation) >= %{symfony_min_ver} with php-composer(symfony/translation) <  %{symfony_max_ver})
BuildRequires: (php-composer(twig/twig)           >= %{twig_min_ver}    with php-composer(twig/twig)           <  %{twig_max_ver})
%else
BuildRequires: php-composer(symfony/translation) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/translation) >= %{symfony_min_ver}
BuildRequires: php-composer(twig/twig) <  2
BuildRequires: php-composer(twig/twig) >= %{twig_min_ver}
%endif
## phpcompatinfo (computed from version 1.5.2)
BuildRequires: php(language) >= 5.3.0
BuildRequires: php-date
BuildRequires: php-mbstring
BuildRequires: php-pcre
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:     (php-composer(twig/twig)           >= %{twig_min_ver}    with php-composer(twig/twig)           <  %{twig_max_ver})
# composer.json: optional
Requires:     (php-composer(symfony/translation) >= %{symfony_min_ver} with php-composer(symfony/translation) <  %{symfony_max_ver})
%else
# v2 to not pull PHP 7
Requires:      php-composer(twig/twig) <  2
Requires:      php-composer(twig/twig) >= %{twig_min_ver}
Requires:      php-composer(symfony/translation) >= %{symfony_min_ver}
Requires:      php-composer(symfony/translation) <  %{symfony_max_ver}
%endif
# phpcompatinfo (computed from version 1.5.2)
Requires:      php(language) >= 5.3.0
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Common additional features for Twig that do not directly belong in core Twig.

Autoloader: %{phpdir}/Twig/Extensions/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}

: Create autoloader
cat <<'AUTOLOAD' | tee lib/Twig/Extensions/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr0('Twig_Extensions_', dirname(dirname(__DIR__)));
\Fedora\Autoloader\Autoload::addPsr4('Twig\\Extensions\\', __DIR__);

\Fedora\Autoloader\Dependencies::required(array(
    array(
        '%{phpdir}/Twig2/autoload.php',
        '%{phpdir}/Twig/autoload.php',
    ),
    array(
        '%{phpdir}/Symfony3/Component/Translation/autoload.php',
        '%{phpdir}/Symfony/Component/Translation/autoload.php',
    ),
));
AUTOLOAD


%build
# Empty build section, nothing required


%install
mkdir -p %{buildroot}%{phpdir}
cp -rp lib/* %{buildroot}%{phpdir}/
cp -rp src/* %{buildroot}%{phpdir}/Twig/Extensions/


%check
%if %{with_tests}
# under investigation
sed -e 's/testLocalizedDateFilterWithDateTimeZone/SKIPtestLocalizedDateFilterWithDateTimeZone/' \
    -i test/Twig/Tests/Extension/IntlTest.php

if php -r '
require_once "%{buildroot}%{phpdir}/Twig/Extensions/autoload.php";
exit(class_exists("Twig\\Error\\RuntimeError") ? 0 : 1);
'
then
    grep -r --files-with-matches --null 'Twig_Error_Runtime' \
        | xargs -0 sed -i 's#Twig_Error_Runtime#Twig\\\\Error\\\\RuntimeError#g'
fi

if php -r '
require_once "%{buildroot}%{phpdir}/Twig/Extensions/autoload.php";
exit(class_exists("Twig\\Error\\SyntaxError") ? 0 : 1);
'
then
    grep -r --files-with-matches --null 'Twig_Error_Syntax' \
        | xargs -0 sed -i 's#Twig_Error_Syntax#Twig\\\\Error\\\\SyntaxError#g'
fi


: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in "" %{?rhel:php55 php56} php70 php71 php72 php73; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose \
            --bootstrap %{buildroot}%{phpdir}/Twig/Extensions/autoload.php \
            || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc README.rst
%doc composer.json
%doc doc
%{phpdir}/Twig/Extensions


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep 14 2019 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.5.4-4
- Fix FTBFS (RHBZ #1736436)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec  7 2018 Remi Collet <remi@remirepo.net> - 1.5.4-1
- update to 1.5.4

* Mon Nov 26 2018 Remi Collet <remi@remirepo.net> - 1.5.3-1
- update to 1.5.3

* Tue Sep  4 2018 Remi Collet <remi@remirepo.net> - 1.5.2-1
- update to 1.5.2 (no change)
- use range dependencies
- raise dependency on symfony/translation 2.7.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 09 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.5.1-1
- Update to 1.5.1 (RHBZ #1456812)
- Add max version constraints to BuildRequires
- Switch autoloader to php-composer(fedora/autoloader)
- Add Symfony Translation to autoloader
- Test with SCLs if available

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan  6 2017 Remi Collet <remi@fedoraproject.org> - 1.4.1-2
- use Twig 2 when installed

* Wed Oct 26 2016 Remi Collet <remi@fedoraproject.org> - 1.4.1-1
- update to 1.4.1

* Tue Oct  4 2016 Remi Collet <remi@fedoraproject.org> - 1.4.0-2
- add upstream patch for test suite with twig 1.26

* Sun Sep 25 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.4.0-1
- Updated to 1.4.0 (RHBZ #1378643)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov  2 2015 Remi Collet <remi@fedoraproject.org> - 1.3.0-3
- drop patch, BC fixed in twig

* Mon Nov  2 2015 Remi Collet <remi@fedoraproject.org> - 1.3.0-2
- add patch for newer twig (thanks Koschei)

* Mon Oct 12 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.3.0-1
- Updated to 1.3.0 (RHBZ #1256169)
- "php-phpunit-PHPUnit" build dependency changed to "php-composer(phpunit/phpunit)"
- "twig/twig" dependency version changed from "~1.12" to "~1.20|~2.0"

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Nov 13 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.0-2
- Conditional %%{?dist}
- Removed color turn off and default timezone for phpunit
- Removed "%%dir %%{phpdir}/Twig" from %%files

* Sun Nov 02 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.0-1
- Initial package
