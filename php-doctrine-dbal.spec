#
# Fedora spec file for php-doctrine-dbal
#
# Copyright (c) 2013-2022 Shawn Iwinski <shawn.iwinski@gmail.com>
#                         Adam Williamson <awilliam@redhat.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

# Build using "--without tests" to disable tests
%bcond_without tests

%global github_owner     doctrine
%global github_name      dbal
%global github_version   2.13.9
%global github_commit    c480849ca3ad6706a39c970cdfe6888fa8a058b8

%global composer_vendor  doctrine
%global composer_project dbal

# "php": "^7.1 || ^8"
%global php_min_ver 7.1
# "doctrine/cache": "^1.0|^2.0"
%global doctrine_cache_min_ver 1.0
%global doctrine_cache_max_ver 3
# "doctrine/event-manager": "^1.0"
%global doctrine_event_min_ver 1.0
%global doctrine_event_max_ver 2
# "doctrine/deprecations": "^0.5.3|^1",
%global doctrine_deprecations_min_ver 0.5.3
%global doctrine_deprecations_max_ver 2
# "symfony/console": "^2.0.5|^3.0|^4.0|^5.0"
%global symfony_console_min_ver 2.0.5
%global symfony_console_max_ver 6
# "symfony/cache": "^4.4"
%global symfony_cache_min_ver 4.4
%global symfony_cache_max_ver 5

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       2%{?github_release}%{?dist}
Summary:       Doctrine Database Abstraction Layer (DBAL)

License:       MIT
URL:           http://www.doctrine-project.org/projects/dbal.html

# Run "php-doctrine-dbal-get-source.sh" to create source
Source0:       %{name}-%{version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

# Update bin script:
# 1) Add she-bang
# 2) Auto-load using Doctrine\Common\ClassLoader
Patch0:        %{name}-bin.patch

BuildArch: noarch
# Tests
%if %{with tests}
BuildRequires: phpunit9 >= 9.5.16
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires:(php-composer(doctrine/cache) >= %{doctrine_cache_min_ver} with php-composer(doctrine/cache) <  %{doctrine_cache_max_ver})
BuildRequires:(php-composer(doctrine/deprecations) >= %{doctrine_deprecations_min_ver} with php-composer(doctrine/deprecations) <  %{doctrine_deprecations_max_ver})
BuildRequires:(php-composer(doctrine/event-manager) >= %{doctrine_event_min_ver} with php-composer(doctrine/event-manager) <  %{doctrine_cache_max_ver})
## composer.json (optional)
BuildRequires:(php-composer(symfony/cache) >= %{symfony_cache_min_ver} with php-composer(symfony/cache) <  %{symfony_cache_max_ver})
BuildRequires:(php-composer(symfony/console) >= %{symfony_console_min_ver} with php-composer(symfony/console) <  %{symfony_console_max_ver})
## phpcompatinfo (computed from version 2.12)
BuildRequires: php-date
BuildRequires: php-json
BuildRequires: php-hash
BuildRequires: php-pcre
BuildRequires: php-pdo
BuildRequires: php-reflection
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:     (php-composer(doctrine/cache) >= %{doctrine_cache_min_ver} with php-composer(doctrine/cache) <  %{doctrine_cache_max_ver})
Requires:     (php-composer(doctrine/deprecations) >= %{doctrine_deprecations_min_ver} with php-composer(doctrine/deprecations) <  %{doctrine_deprecations_max_ver})
Requires:     (php-composer(doctrine/event-manager) >= %{doctrine_event_min_ver} with php-composer(doctrine/event-manager) <  %{doctrine_cache_max_ver})
# composer.json (optional)
Requires:     (php-composer(symfony/console) >= %{symfony_console_min_ver} with php-composer(symfony/console) <  %{symfony_console_max_ver})
Requires:      php-pdo
# phpcompatinfo (computed from version 2.12)
Requires:      php-date
Requires:      php-json
Requires:      php-hash
Requires:      php-pcre
Requires:      php-reflection
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}
# PEAR
Provides:      php-pear(pear.doctrine-project.org/DoctrineDBAL) = %{version}
# Rename
Obsoletes:     php-doctrine-DoctrineDBAL < %{version}
Provides:      php-doctrine-DoctrineDBAL = %{version}

%description
The Doctrine database abstraction & access layer (DBAL) offers a lightweight
and thin runtime layer around a PDO-like API and a lot of additional, horizontal
features like database schema introspection and manipulation through an OO API.

The fact that the Doctrine DBAL abstracts the concrete PDO API away through the
use of interfaces that closely resemble the existing PDO API makes it possible
to implement custom drivers that may use existing native or self-made APIs. For
example, the DBAL ships with a driver for Oracle databases that uses the oci8
extension under the hood.

Autoloader: %{phpdir}/Doctrine/DBAL/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}

: Patch bin script
%patch0 -p1 -b .rpm

: Remove empty file
rm -f lib/Doctrine/DBAL/README.markdown


%build
: Create autoloader
cat <<'AUTOLOAD' | tee lib/Doctrine/DBAL/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

if (!class_exists('Doctrine\\DBAL\\Connection')) {
     \Fedora\Autoloader\Autoload::addPsr4('Doctrine\\DBAL\\', __DIR__);
}

\Fedora\Autoloader\Dependencies::required([
    [
        '%{phpdir}/Doctrine/Common/Cache2/autoload.php',
        '%{phpdir}/Doctrine/Common/Cache/autoload.php',
    ],
    '%{phpdir}/Doctrine/Deprecations/autoload.php',
    '%{phpdir}/Doctrine/Common/EventManager/autoload.php',
]);

\Fedora\Autoloader\Dependencies::optional([
    [
        (getenv('RPM_SYMFONY_TREE')?:'%{phpdir}/Symfony5') . '/Component/Console/autoload.php',
        '%{phpdir}/Symfony4/Component/Console/autoload.php',
        '%{phpdir}/Symfony3/Component/Console/autoload.php',
        '%{phpdir}/Symfony/Component/Console/autoload.php',
    ],
]);
AUTOLOAD


%install
mkdir -p %{buildroot}/%{phpdir}
cp -rp lib/Doctrine %{buildroot}/%{phpdir}/

mkdir -p %{buildroot}/%{_bindir}
install -pm 0755 bin/doctrine-dbal.php %{buildroot}/%{_bindir}/doctrine-dbal


%check
%if %{with tests}
cat > bs.php <<'BOOTSTRAP'
<?php
require_once '%{buildroot}/%{phpdir}/Doctrine/DBAL/autoload.php';
\Fedora\Autoloader\Dependencies::required([
        '%{phpdir}/Symfony4/Component/Cache/autoload.php',
]);
\Fedora\Autoloader\Autoload::addPsr4(
    'Doctrine\\Tests\\',
    __DIR__ . '/tests/Doctrine/Tests'
);
BOOTSTRAP

%if 0%{?rhel} == 7
SKIP="--filter '^((?!(testFetchAllKeyValueWithLimit|testFetchLongBlob)).)*$'"
%else
SKIP="--filter '^((?!(testFetchLongBlob)).)*$'"
%endif

: Upstream tests
RETURN_CODE=0
for PHP_EXEC in php php74 php80 php81; do
    rm -f /tmp/test_nesting.sqlite
    if which $PHP_EXEC; then
        $PHP_EXEC %{_bindir}/phpunit9 \
            $SKIP \
            --bootstrap bs.php \
            --verbose || RETURN_CODE=1
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
%{phpdir}/Doctrine/DBAL
%{_bindir}/doctrine-dbal


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May  3 2022 Remi Collet <remi@remirepo.net> - 2.13.9-1
- update to 2.13.9
- allow doctrine/deprecations 1

* Thu Mar 10 2022 Remi Collet <remi@remirepo.net> - 2.13.8-1
- update to 2.13.8

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan  6 2022 Remi Collet <remi@remirepo.net> - 2.13.7-1
- update to 2.13.7

* Mon Nov 29 2021 Remi Collet <remi@remirepo.net> - 2.13.6-1
- update to 2.13.6

* Mon Nov 15 2021 Remi Collet <remi@remirepo.net> - 2.13.5-1
- update to 2.13.5

* Mon Oct  4 2021 Remi Collet <remi@remirepo.net> - 2.13.4-1
- update to 2.13.4

* Mon Sep 13 2021 Remi Collet <remi@remirepo.net> - 2.13.3-1
- update to 2.13.3

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 23 2021 Remi Collet <remi@remirepo.net> - 2.13.2-1
- update to 2.13.2
- allow doctrine/cache version 2

* Tue Apr 20 2021 Remi Collet <remi@remirepo.net> - 2.13.1-1
- update to 2.13.1

* Tue Mar 30 2021 Remi Collet <remi@remirepo.net> - 2.13.0-1
- update to 2.13.0
- lower dependency on PHP 7.1
- add dependency on doctrine/deprecations

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec  8 2020 Remi Collet <remi@remirepo.net> - 2.12.1-2
- don't register autoloader twice, e.g. by doctrine/dbal v3

* Mon Nov 16 2020 Remi Collet <remi@remirepo.net> - 2.12.1-1
- update to 2.12.1

* Fri Oct 23 2020 Remi Collet <remi@remirepo.net> - 2.12.0-1
- update to 2.12.0

* Wed Oct 21 2020 Remi Collet <remi@remirepo.net> - 2.11.3-1
- update to 2.11.3

* Mon Oct 19 2020 Remi Collet <remi@remirepo.net> - 2.11.2-1
- update to 2.11.2

* Mon Sep 28 2020 Remi Collet <remi@remirepo.net> - 2.11.1-1
- update to 2.11.1

* Mon Sep 21 2020 Remi Collet <remi@remirepo.net> - 2.11.0-1
- update to 2.11.0
- raise dependency on PHP 7.3
- switch to phpunit9

* Mon Sep 14 2020 Remi Collet <remi@remirepo.net> - 2.10.4-1
- update to 2.10.4

* Wed Sep  2 2020 Remi Collet <remi@remirepo.net> - 2.10.3-1
- update to 2.10.3

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Apr 21 2020 Remi Collet <remi@remirepo.net> - 2.10.2-1
- update to 2.10.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan  6 2020 Remi Collet <remi@remirepo.net> - 2.10.1-1
- update to 2.10.1

* Mon Nov  4 2019 Remi Collet <remi@remirepo.net> - 2.10.0-1
- update to 2.10.0
- raise dependencies on PHP 7.2
- switch to phpunit8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan  2 2019 Remi Collet <remi@remirepo.net> - 2.9.2-1
- update to 2.9.2

* Fri Dec 14 2018 Remi Collet <remi@remirepo.net> - 2.9.1-1
- update to 2.9.1

* Mon Dec 10 2018 Remi Collet <remi@remirepo.net> - 2.9.0-1
- update to 2.9.0

* Thu Oct 18 2018 Remi Collet <remi@remirepo.net> - 2.8.0-1
- update to 2.8.0
- drop dependency on doctrine/common
- add dependency on doctrine/cache
- add dependency on doctrine/event-manager
- allow Symfony 4

* Wed Oct 17 2018 Remi Collet <remi@remirepo.net> - 2.7.2-1
- update to 2.7.2
- raise dependencies on PHP 7.1
- use range dependencies
- switch to phpunit7

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 30 2017 Remi Collet <remi@remirepo.net> - 2.5.12-3
- allow to force Symfony version using RPM_SYMFONY_TREE

* Sat Mar 11 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.5.12-1
- Updated to 2.5.12 (RHBZ #1412852)
- Switch autoloader to php-composer(fedora/autoloader)
- Run upstream tests with SCLs if available

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 26 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.5.5-1
- Updated to 2.5.5 (RHBZ #1374891)

* Mon Jun 13 2016 Remi Collet <remi@fedoraproject.org> - 2.5.4-2
- add workaround for test suite with PHPUnit 5.4

* Mon Mar 14 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.5.4-1
- Updated to 2.5.4 (RHBZ #1153987)
- Added autoloader

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jan 14 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.5.1-1
- Updated to 2.5.1 (BZ #1153987)

* Fri Jan 02 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.5.1-0.2.20150101git185b886
- Updated to latest snapshot
- Fixed bin script
- Added tests

* Tue Dec 30 2014 Adam Williamson <awilliam@redhat.com> - 2.5.1-0.1.20141230gitdd4d106
- bump to 2.5 branch (with latest fixes, some of which look big; BZ #1153987)

* Tue Jul 29 2014 Adam Williamson <awilliam@redhat.com> - 2.4.2-6
- really apply the patch

* Tue Jul 29 2014 Adam Williamson <awilliam@redhat.com> - 2.4.2-5
- backport another OwnCloud-related pgsql fix from upstream master

* Fri Jun 20 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.4.2-4
- Added php-composer(%%{composer_vendor}/%%{composer_project}) virtual provide
- Updated Doctrine dependencies to use php-composer virtual provides

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jan 07 2014 Adam Williamson <awilliam@redhat.com> - 2.4.2-2
- primary_index: one OwnCloud patch still isn't in upstream

* Sat Jan 04 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.4.2-1
- Updated to 2.4.2
- Conditional %%{?dist}

* Tue Dec 31 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.4.1-2.20131231gitd08b11c
- Updated to latest snapshot
- Removed patches (pulled into latest snapshot)

* Sun Dec 29 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.4.1-1
- Initial package
