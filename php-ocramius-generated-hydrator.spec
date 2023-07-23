#
# Fedora spec file for php-ocramius-generated-hydrator
#
# Copyright (c) 2014-2021 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     Ocramius
%global github_name      GeneratedHydrator
%global github_version   4.1.0
%global github_commit    e1d2919b31631195f3f45a2dfcf84812daa15384

%global composer_vendor  ocramius
%global composer_project generated-hydrator

# "php": "^7.4.7"
%global php_min_ver 7.4.7
# "nikic/php-parser": "^4.10.4"
%global php_parser_min_ver 4.10.4
%global php_parser_max_ver 5
# "ocramius/code-generator-utils": "^1.1.0"
%global ocramius_cgu_min_ver 1.1.0
%global ocramius_cgu_max_ver 2
# "laminas/laminas-hydrator": "^3.1.1"
%global laminas_hydrator_min_ver 3.1.1
%global laminas_hydrator_max_ver 4

# Build using "--without tests" to disable tests
%bcond_without tests

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       5%{?github_release}%{?dist}
Summary:       An object hydrator

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
%if %{with tests}
# composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: phpunit9
BuildRequires: (php-composer(laminas/laminas-hydrator) >= %{laminas_hydrator_min_ver} with php-composer(laminas/laminas-hydrator) < %{laminas_hydrator_max_ver})
BuildRequires: (php-composer(nikic/php-parser) >= %{php_parser_min_ver} with php-composer(nikic/php-parser) < %{php_parser_max_ver})
BuildRequires: (php-composer(ocramius/code-generator-utils) >= %{ocramius_cgu_min_ver} with php-composer(ocramius/code-generator-utils) < %{ocramius_cgu_max_ver})
# phpcompatinfo (computed from version 4.1.0)
BuildRequires: php-date
BuildRequires: php-reflection
BuildRequires: php-spl
%endif
# Autoloader
BuildRequires: php-composer(fedora/autoloader)

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      (php-composer(laminas/laminas-hydrator) >= %{laminas_hydrator_min_ver} with php-composer(laminas/laminas-hydrator) < %{laminas_hydrator_max_ver})
Requires:      (php-composer(nikic/php-parser) >= %{php_parser_min_ver} with php-composer(nikic/php-parser) < %{php_parser_max_ver})
Requires:      (php-composer(ocramius/code-generator-utils) >= %{ocramius_cgu_min_ver} with php-composer(ocramius/code-generator-utils) < %{ocramius_cgu_max_ver})
# phpcompatinfo (computed from version 4.1.0)
Requires:      php-reflection
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
GeneratedHydrator is a library about high performance transition of data from
arrays to objects and from objects to arrays.

Autoloader: %{phpdir}/GeneratedHydrator/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/GeneratedHydrator/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('GeneratedHydrator\\', __DIR__);

\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/CodeGenerationUtils/autoload.php',
    '%{phpdir}/Laminas/Hydrator3/autoload.php',
    '%{phpdir}/PhpParser4/autoload.php',
]);
AUTOLOAD


%install

mkdir -p %{buildroot}%{phpdir}
cp -rp src/GeneratedHydrator %{buildroot}%{phpdir}/


%check
%if %{with tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require '%{buildroot}%{phpdir}/GeneratedHydrator/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('GeneratedHydratorTest\\', __DIR__.'/tests/GeneratedHydratorTest');
\Fedora\Autoloader\Autoload::addPsr4('GeneratedHydratorTestAsset\\', __DIR__.'/tests/GeneratedHydratorTestAsset');
BOOTSTRAP

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit9)
for PHP_EXEC in php php80 php81; do
    if [ "php" == "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose --bootstrap bootstrap.php \
            || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif


%files
%license LICENSE
%doc *.md
%doc composer.json
%{phpdir}/GeneratedHydrator


%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Sep 18 2021 Shawn Iwinski <shawn.iwinski@gmail.com> - 4.1.0-1
- Update to 4.1.0 (RHBZ #1685279)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Mar 24 2021 Remi Collet <remi@remirepo.net> - 2.2.0-5
- disable tests

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 29 2019 Remi Collet <remi@remirepo.net> - 2.2.0-1
- update to 2.2.0
- use zendframework/zend-hydrator autoloader instead of framework one
- switch to phpunit6

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 29 2018 Remi Collet <remi@fedoraproject.org> - 2.1.0-5
- use range dependencies and fix FTBFS

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug  7 2017 Remi Collet <remi@fedoraproject.org> - 2.1.0-2
- clean autoloader

* Sat Aug 05 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.1.0-1
- Update to 2.1.0 (RHBZ #1473994)
- Switch autoloader to php-composer(fedora/autoloader)
- Test with SCLs if available

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Remi Collet <remi@fedoraproject.org> - 2.0.0-2
- explicit dependency on php-nikic-php-parser, fix FTBFS from Koschei

* Wed Nov 30 2016 Remi Collet <remi@fedoraproject.org> - 2.0.0-1
- update to 2.0.0
- drop dependency on zendframework/zend-stdlib
- raise dependency on php ~7.0
- raise dependency on nikic/php-parser ~2.0
- raise dependency on ocramius/code-generator-utils 0.4.*
- add dependency on zendframework/zend-hydrator

* Wed Oct 12 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.0-1
- Update to 1.2.0
- Add autoloader

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 25 2015 Remi Collet <remi@fedoraproject.org> - 1.1.1-1
- update to 1.1.1 (no change)
- raise nikic/php-parser max version

* Mon Oct 27 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1.0-1
- Initial package
