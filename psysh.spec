#
# Fedora spec file for psysh
#
# Copyright (c) 2016-2022 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     bobthecow
%global github_name      psysh
%global github_version   0.11.8
%global github_commit    f455acf3645262ae389b10e9beba0c358aa6994e

%global composer_vendor  psy
%global composer_project psysh

# "php": "^8.0 || ^7.0.8"
%global php_min_ver 7.0.8
# "nikic/php-parser": "^4.0 || ^3.1"
#     NOTE: Forcing minimum version 4
%global php_parser_min_ver 4.0
%global php_parser_max_ver 5.0
# "symfony/console": "^6.0 || ^5.0 || ^4.0 || ^3.4"
# "symfony/var-dumper": "^6.0 || ^5.0 || ^4.0 || ^3.4"
%global symfony_min_ver 3.4
%global symfony_max_ver 7.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

# Range dependencies supported?
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
%global with_range_dependencies 1
%else
%global with_range_dependencies 0
%endif

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          psysh
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       A runtime developer console, interactive debugger and REPL for PHP

License:       MIT
URL:           https://psysh.org

# GitHub export does not include tests
# Run psysh-get-source.sh to create full source
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

# Update bin script to use generated autoloader
Patch0:        %{name}-bin-autoload.patch

BuildArch:     noarch
# Tests
%if %{with_tests}
BuildRequires: php-cli
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: phpunit9
%if %{with_range_dependencies}
BuildRequires: (php-composer(nikic/php-parser) >= %{php_parser_min_ver} with php-composer(nikic/php-parser) < %{php_parser_max_ver})
BuildRequires: (php-composer(symfony/console) >= %{symfony_min_ver} with php-composer(symfony/console) < %{symfony_max_ver})
BuildRequires: (php-composer(symfony/var-dumper) >= %{symfony_min_ver} with php-composer(symfony/var-dumper) < %{symfony_max_ver})
%else
BuildRequires: php-composer(nikic/php-parser) <  %{php_parser_max_ver}
BuildRequires: php-composer(nikic/php-parser) >= %{php_parser_min_ver}
BuildRequires: php-symfony3-console
BuildRequires: php-symfony3-var-dumper
%endif
BuildRequires: php-json
BuildRequires: php-tokenizer
## composer.json: optional
BuildRequires: php-pcntl
BuildRequires: php-posix
BuildRequires: php-readline
BuildRequires: php-sqlite3
## phpcompatinfo (computed from version 0.11.8)
BuildRequires: php-date
BuildRequires: php-dom
BuildRequires: php-pcre
BuildRequires: php-pdo
BuildRequires: php-reflection
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

Requires:      php-cli
# composer.json
Requires:      php(language) >= %{php_min_ver}
%if %{with_range_dependencies}
Requires:      (php-composer(nikic/php-parser) >= %{php_parser_min_ver} with php-composer(nikic/php-parser) < %{php_parser_max_ver})
Requires:      (php-composer(symfony/console) >= %{symfony_min_ver} with php-composer(symfony/console) < %{symfony_max_ver})
Requires:      (php-composer(symfony/var-dumper) >= %{symfony_min_ver} with php-composer(symfony/var-dumper) < %{symfony_max_ver})
%else
Requires:      php-composer(nikic/php-parser) <  %{php_parser_max_ver}
Requires:      php-composer(nikic/php-parser) >= %{php_parser_min_ver}
Requires:      php-symfony3-console
Requires:      php-symfony3-var-dumper
%endif
Requires:      php-json
Requires:      php-tokenizer
# composer.json: optional
Requires:      php-pcntl
Requires:      php-posix
Requires:      php-readline
Requires:      php-sqlite3
# phpcompatinfo (computed from version 0.11.8)
Requires:      php-date
Requires:      php-pcre
Requires:      php-pdo
Requires:      php-reflection
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Standard "php-{COMPOSER_VENDOR}-{COMPOSER_PROJECT}" naming
Provides:      php-%{composer_vendor}-%{composer_project} = %{version}-%{release}
# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
%{summary}.

Autoloader: %{phpdir}/Psy/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}

: Update bin script to use generated autoloader
%patch0 -p1
sed 's#__PHPDIR__#%{phpdir}#' -i bin/psysh


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Psy\\', __DIR__);
require_once __DIR__.'/functions.php';

\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/PhpParser4/autoload.php',
    [
        '%{phpdir}/Symfony6/Component/Console/autoload.php',
        '%{phpdir}/Symfony5/Component/Console/autoload.php',
        '%{phpdir}/Symfony4/Component/Console/autoload.php',
        '%{phpdir}/Symfony3/Component/Console/autoload.php',
        '%{phpdir}/Symfony/Component/Console/autoload.php',
    ],
    [
        '%{phpdir}/Symfony6/Component/VarDumper/autoload.php',
        '%{phpdir}/Symfony5/Component/VarDumper/autoload.php',
        '%{phpdir}/Symfony4/Component/VarDumper/autoload.php',
        '%{phpdir}/Symfony3/Component/VarDumper/autoload.php',
        '%{phpdir}/Symfony/Component/VarDumper/autoload.php',
    ],
]);
AUTOLOAD


%install
: Library
mkdir -p %{buildroot}%{phpdir}
cp -rp src %{buildroot}%{phpdir}/Psy

: Bin
mkdir -p %{buildroot}%{_bindir}
install -pm 0755 bin/psysh %{buildroot}%{_bindir}/


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require '%{buildroot}%{phpdir}/Psy/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Psy\\Test\\', __DIR__.'/test');
BOOTSTRAP

: Skip tests known to fail
sed 's/function testFilesAndDirectories/function SKIP_testFilesAndDirectories/' \
    -i test/ConfigurationTest.php

: Skip tests known to fail in a mock env
sed 's/function testFormat/function SKIP_testFormat/' \
    -i test/Formatter/CodeFormatterTest.php
sed 's/function testWriteReturnValue/function SKIP_testWriteReturnValue/' \
    -i test/ShellTest.php
sed 's/function testMoreUnclosedStatements/function SKIP_testMoreUnclosedStatements/' \
    -i test/CodeCleanerTest.php
sed 's/function testEnumerateUserFunctions/function SKIP_testEnumerateUserFunctions/' \
    -i test/Command/ListCommand/FunctionEnumeratorTest.php
sed 's/function testEnumerate/function SKIP_testEnumerate/' \
    -i test/Command/ListCommand/GlobalVariableEnumeratorTest.php
sed 's/function testEnumerateEnumerates/function SKIP_testEnumerateEnumerates/' \
    -i test/Command/ListCommand/VariableEnumeratorTest.php
sed 's/function testEnumerateAllEnumeratesEvenMore/function SKIP_testEnumerateAllEnumeratesEvenMore/' \
    -i test/Command/ListCommand/VariableEnumeratorTest.php
: Skip test failing with php 7.3
sed -e 's/function testConfigurationFromInput/function SKIP_testConfigurationFromInput/' \
    -e 's/function testConfigurationFromInputSpecificity/function SKIP_testConfigurationFromInputSpecificity/' \
    -e 's/function testConfigurationFromInputVerbosityLevels/function SKIP_testConfigurationFromInputVerbosityLevels/' \
    -e 's/function testConfigurationFromInputShortOptions/function SKIP_testConfigurationFromInputShortOptions/' \
    -i test/ConfigurationTest.php


: Drop unneeded test as readline is always there
rm test/Readline/HoaConsoleTest.php

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit9)
for PHP_EXEC in "" php73 php74 php80 php81 php82; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose --bootstrap bootstrap.php \
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
%{phpdir}/Psy
%{_bindir}/psysh


%changelog
* Thu Oct 06 2022 Shawn Iwinski <shawn@iwin.ski> - 0.11.8-1
- Update to 0.11.8 (RHBZ #2012727)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed May 26 2021 Remi Collet <remi@remirepo.net> - 0.10.8-1
- update to 0.10.8
- drop dependency on dnoegel/php-xdg-base-dir
- switch to phpunit9

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Aug 16 2020 Shawn Iwinski <shawn@iwin.ski> - 0.10.4-1
- Update to 0.10.4 (RHBZ #1782258)
- Fix FTBFS (RHBZ #1865260)
- Conditionally use range dependencies
- Conditionally drop Symfony 2 interoperability
- Force "nikic/php-parser" minimum version 4

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 01 2019 Shawn Iwinski <shawn@iwin.ski> - 0.9.11-1
- Update to 0.9.11 (RHBZ #1529814)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 13 2017 Shawn Iwinski <shawn@iwin.ski> - 0.8.16-1
- Update to 0.8.16 (RHBZ #1468827)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 25 2017 Shawn Iwinski <shawn@iwin.ski> - 0.8.8-1
- Update to 0.8.8 (RHBZ #1464772)

* Fri Jun 23 2017 Shawn Iwinski <shawn@iwin.ski> - 0.8.7-1
- Update to 0.8.7 (RHBZ #1450707)
- Fix autoloader for PHP < 5.4

* Sat Apr 08 2017 Shawn Iwinski <shawn@iwin.ski> - 0.8.3-1
- Update to 0.8.3 (RHBZ #1433813)
- Allow Symfony 3

* Sat Mar 04 2017 2017 Shawn Iwinski <shawn@iwin.ski> - 0.8.2-1
- Update to 0.8.2 (RHBZ #1413429)
- Test with SCLs if available

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Dec 11 2016 Shawn Iwinski <shawn@iwin.ski> - 0.8.0-1
- Update to 0.8.0 (RHBZ #1403040)
- Switch autoloader from php-composer(symfony/class-loader) to
  php-composer(fedora/autoloader)

* Wed Jul 20 2016 Shawn Iwinski <shawn@iwin.ski> - 0.7.2-2
- Add explicit php-cli dependency (bin script uses "#!/usr/bin/env php")

* Fri Jul 15 2016 Shawn Iwinski <shawn@iwin.ski> - 0.7.2-1
- Initial package
