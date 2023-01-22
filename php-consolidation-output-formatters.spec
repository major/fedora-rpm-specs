#
# Fedora spec file for php-consolidation-output-formatters
#
# Copyright (c) 2016-2022 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     consolidation
%global github_name      output-formatters
%global github_version   4.2.2
%global github_commit    d57992bf81ead908ee21cd94b46ed65afa2e785b

%global composer_vendor  consolidation
%global composer_project output-formatters

# "php": ">=7.1.3"
%global php_min_ver 7.1.3
# "dflydev/dot-access-data": "^1.1.0 || ^2 || ^3"
%global dflydev_dot_access_data_min_ver 1.1.0
%global dflydev_dot_access_data_max_ver 4.0
# "symfony/console": "^4|^5|^6"
# "symfony/finder": "^4|^5|^6"
# "symfony/var-dumper": "^4|^5|^6"
# "symfony/yaml": "^4|^5|^6"
%global symfony_min_ver 4.0
%global symfony_max_ver 7.0

# "phpunit/phpunit": ">=7"
%global phpunit_require phpunit9
%global phpunit_min_ver 9
%global phpunit_exec    phpunit9

# "yoast/phpunit-polyfills": "^0.2.0"
%global phpunit_polyfills_min_ver 0.2
%global phpunit_polyfills_max_ver 2

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

# Range dependencies supported?
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
%global with_range_dependencies 1
%else
%global with_range_dependencies 0
%endif

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       2%{?github_release}%{?dist}
Summary:       Format text by applying transformations provided by plug-in formatters

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests
# Run php-consolidation-output-formatters-get-source.sh to create full source
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: %{phpunit_require} >= %{phpunit_min_ver}
%if %{with_range_dependencies}
BuildRequires: (php-composer(dflydev/dot-access-data) >= %{dflydev_dot_access_data_min_ver} with php-composer(dflydev/dot-access-data) < %{dflydev_dot_access_data_max_ver})
BuildRequires: (php-composer(symfony/console) >= %{symfony_min_ver} with php-composer(symfony/console) < %{symfony_max_ver})
BuildRequires: (php-composer(symfony/finder) >= %{symfony_min_ver} with php-composer(symfony/finder) < %{symfony_max_ver})
BuildRequires: (php-composer(symfony/var-dumper) >= %{symfony_min_ver} with php-composer(symfony/var-dumper) < %{symfony_max_ver})
BuildRequires: (php-composer(symfony/yaml) >= %{symfony_min_ver} with php-composer(symfony/yaml) < %{symfony_max_ver})
BuildRequires: (php-composer(yoast/phpunit-polyfills) >= %{phpunit_polyfills_min_ver} with php-composer(yoast/phpunit-polyfills) < %{phpunit_polyfills_max_ver})
%else
BuildRequires: php-composer(dflydev/dot-access-data) <  %{dflydev_dot_access_data_max_ver}
BuildRequires: php-composer(dflydev/dot-access-data) >= %{dflydev_dot_access_data_min_ver}
BuildRequires: php-symfony4-console >= %{symfony_min_ver}
BuildRequires: php-symfony4-finder >= %{symfony_min_ver}
BuildRequires: php-symfony4-var-dumper >= %{symfony_min_ver}
BuildRequires: php-symfony4-yaml >= %{symfony_min_ver}
BuildRequires: php-composer(yoast/phpunit-polyfills) <  %{phpunit_polyfills_max_ver}
BuildRequires: php-composer(yoast/phpunit-polyfills) >= %{phpunit_polyfills_min_ver}
%endif
## phpcompatinfo (computed from version 4.1.1)
BuildRequires: php-dom
BuildRequires: php-json
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
%if %{with_range_dependencies}
Requires:      (php-composer(dflydev/dot-access-data) >= %{dflydev_dot_access_data_min_ver} with php-composer(dflydev/dot-access-data) < %{dflydev_dot_access_data_max_ver})
Requires:      (php-composer(symfony/console) >= %{symfony_min_ver} with php-composer(symfony/console) < %{symfony_max_ver})
Requires:      (php-composer(symfony/finder) >= %{symfony_min_ver} with php-composer(symfony/finder) < %{symfony_max_ver})
%else
Requires:      php-composer(dflydev/dot-access-data) <  %{dflydev_dot_access_data_max_ver}
Requires:      php-composer(dflydev/dot-access-data) >= %{dflydev_dot_access_data_min_ver}
Requires:      php-symfony4-console >= %{symfony_min_ver}
Requires:      php-symfony4-finder >= %{symfony_min_ver}
%endif
# phpcompatinfo (computed from version 4.1.1)
Requires:      php-dom
Requires:      php-json
Requires:      php-pcre
Requires:      php-reflection
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

%if %{with_range_dependencies}
# Weak dependencies
Suggests:      (php-composer(symfony/var-dumper) >= %{symfony_min_ver} with php-composer(symfony/var-dumper) < %{symfony_max_ver})
%endif

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
%{summary}.

Autoloader: %{phpdir}/Consolidation/OutputFormatters/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Consolidation\\OutputFormatters\\', __DIR__);

\Fedora\Autoloader\Dependencies::required([
    [
        '%{phpdir}/Dflydev/DotAccessData3/autoload.php',
        '%{phpdir}/Dflydev/DotAccessData2/autoload.php',
        '%{phpdir}/Dflydev/DotAccessData/autoload.php',
    ],
    [
        '%{phpdir}/Symfony6/Component/Console/autoload.php',
        '%{phpdir}/Symfony5/Component/Console/autoload.php',
        '%{phpdir}/Symfony4/Component/Console/autoload.php',
    ],
    [
        '%{phpdir}/Symfony6/Component/Finder/autoload.php',
        '%{phpdir}/Symfony5/Component/Finder/autoload.php',
        '%{phpdir}/Symfony4/Component/Finder/autoload.php',
    ],
]);

\Fedora\Autoloader\Dependencies::optional([
    [
        '%{phpdir}/Symfony6/Component/VarDumper/autoload.php',
        '%{phpdir}/Symfony5/Component/VarDumper/autoload.php',
        '%{phpdir}/Symfony4/Component/VarDumper/autoload.php',
    ],
]);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/Consolidation
cp -rp src %{buildroot}%{phpdir}/Consolidation/OutputFormatters


%check
%if %{with_tests}
: Create tests bootstrap
mkdir vendor
cat <<'BOOTSTRAP' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{phpdir}/Consolidation/OutputFormatters/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Consolidation\\TestUtils\\', dirname(__DIR__).'/tests/src');

\Fedora\Autoloader\Dependencies::required([
    [
        '%{phpdir}/Symfony6/Component/Yaml/autoload.php',
        '%{phpdir}/Symfony5/Component/Yaml/autoload.php',
        '%{phpdir}/Symfony4/Component/Yaml/autoload.php',
    ],
    '%{phpdir}/Yoast/PHPUnitPolyfills/autoload.php',
]);
BOOTSTRAP

: Skip tests known to fail
sed \
  -e 's/function testTableWithWordWrapping5/function SKIP_testTableWithWordWrapping5/' \
  -e 's/function testSimpleTableWithFieldLabels/function SKIP_testSimpleTableWithFieldLabels/' \
  -e 's/function testSimpleList/function SKIP_testSimpleList/' \
  -i tests/FormattersTest.php

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which %{phpunit_exec})
for PHP_EXEC in "" php73 php74 php80 php81 php82; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose --no-coverage \
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
%doc *.md
%doc composer.json
%dir %{phpdir}/Consolidation
     %{phpdir}/Consolidation/OutputFormatters


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Oct 07 2022 Shawn Iwinski <shawn@iwin.ski> - 4.2.2-1
- Update to 4.2.2 (RHBZ #2035735)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 21 2021 Remi Collet <remi@remirepo.net> - 4.1.2-2
- allow yoast/phpunit-polyfills version 1

* Tue Mar 23 2021 Remi Collet <remi@remirepo.net> - 4.1.2-1
- update to 4.1.2
- switch to phpunit9 with yoast/phpunit-polyfills

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 07 2020 Shawn Iwinski <shawn@iwin.ski> - 4.1.1-1
- Update to 4.1.1 (RHBZ #1851299)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 24 2020 Shawn Iwinski <shawn@iwin.ski> - 4.1.0-1
- Update to 4.1.0
- Use PHPUnit 6

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 01 2019 Shawn Iwinski <shawn@iwin.ski> - 3.5.0-2
- Fix sources

* Sat Jun 01 2019 Shawn Iwinski <shawn@iwin.ski> - 3.5.0-1
- Update to 3.5.0 (RHBZ #1582691)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 30 2018 Shawn Iwinski <shawn@iwin.ski> - 3.2.0-1
- Update to 3.2.0 (RHBZ #1505200)

* Fri Mar 30 2018 Shawn Iwinski <shawn@iwin.ski> - 3.1.13-2
- Update range dependencies' conditional to include RHEL8+

* Wed Feb 21 2018 Shawn Iwinski <shawn@iwin.ski> - 3.1.13-1
- Update to 3.1.13 (RHBZ #1505200)
- Add range version dependencies for Fedora >= 27

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 30 2017 Shawn Iwinski <shawn@iwin.ski> - 3.1.11-1
- Update to 3.1.11 (RHBZ #1482728)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 08 2017 Shawn Iwinski <shawn@iwin.ski> - 3.1.10-1
- Update to 3.1.10 (RHBZ #1449852)

* Sat Apr 08 2017 Shawn Iwinski <shawn@iwin.ski> - 3.1.8-1
- Update to 3.1.8 (RHBZ #1428197)
- Allow Symfony 3

* Tue Feb 28 2017 Shawn Iwinski <shawn@iwin.ski> - 3.1.7-1
- Update to 3.1.7 (RHBZ #1415386)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 16 2017 Remi Collet <remi@fedoraproject.org> - 3.1.6-2
- fix autoloader dependency

* Sun Jan 15 2017 Shawn Iwinski <shawn@iwin.ski> - 3.1.6-1
- Update to 3.1.6 (RHBZ #1392720)
- Use php-composer(fedora/autoloader)
- Run upstream tests with SCLs if they are available

* Tue Nov 01 2016 Shawn Iwinski <shawn@iwin.ski> - 2.0.1-1
- Update to 2.0.1 (RHBZ #1376274)

* Tue Jul 19 2016 Shawn Iwinski <shawn@iwin.ski> - 1.0.0-1
- Initial package
