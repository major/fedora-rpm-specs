#
# Fedora spec file for php-doctrine-common
#
# Copyright (c) 2013-2021 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     doctrine
%global github_name      common
%global github_version   2.13.3
%global github_commit    f3812c026e557892c34ef37f6ab808a6b567da7f

%global composer_vendor  doctrine
%global composer_project common

# "php": "^7.1 || ^8.0"
%global php_min_ver 7.1
# "doctrine/annotations": "^1.0"
#     NOTE: Min version not 1.0 because autoloader required
%global doctrine_annotations_min_ver 1.2.6
%global doctrine_annotations_max_ver 2.0
# "doctrine/cache": "^1.0"
#     NOTE: Min version not 1.0 because autoloader required
%global doctrine_cache_min_ver 1.4.1
%global doctrine_cache_max_ver 2.0
# "doctrine/collections": "^1.0"
#     NOTE: Min version not 1.0 because autoloader required
%global doctrine_collections_min_ver 1.3.0
%global doctrine_collections_max_ver 2.0
# "doctrine/inflector": "^1.0"
#     NOTE: Min version not 1.0 because autoloader required
%global doctrine_inflector_min_ver 1.0.1
%global doctrine_inflector_max_ver 2.0
# "doctrine/lexer": "^1.0"
#     NOTE: Min version not 1.0 because autoloader required
%global doctrine_lexer_min_ver 1.0.1
%global doctrine_lexer_max_ver 2.0
# "doctrine/event-manager": "^1.0"
%global doctrine_event_min_ver 1.0
%global doctrine_event_max_ver 2
# "doctrine/reflection": "^1.0"
%global doctrine_refl_min_ver 1.0
%global doctrine_refl_max_ver 2
# "doctrine/persistence": "^1.3.3"
%global doctrine_pers_min_ver 1.3.3
%global doctrine_pers_max_ver 2

# Build using "--with tests" to enable tests
%bcond_with tests

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Epoch:         1
Version:       %{github_version}
Release:       12%{?dist}
Summary:       Common library for Doctrine projects

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests.
# Run php-doctrine-common-get-source.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

# Minimal fix for PHP 8
Patch0:        %{name}-php8.patch

BuildArch:     noarch
# Library version value check
BuildRequires: php-cli
# Tests
%if %{with tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: (php-composer(doctrine/annotations) >= %{doctrine_annotations_min_ver} with php-composer(doctrine/annotations) < %{doctrine_annotations_max_ver})
BuildRequires: (php-composer(doctrine/cache) >= %{doctrine_cache_min_ver} with php-composer(doctrine/cache) < %{doctrine_cache_max_ver})
BuildRequires: (php-composer(doctrine/collections) >= %{doctrine_collections_min_ver} with php-composer(doctrine/collections) < %{doctrine_collections_max_ver})
BuildRequires: (php-composer(doctrine/inflector) >= %{doctrine_inflector_min_ver} with php-composer(doctrine/inflector) < %{doctrine_inflector_max_ver})
BuildRequires: (php-composer(doctrine/lexer) >= %{doctrine_lexer_min_ver} with php-composer(doctrine/lexer) < %{doctrine_lexer_max_ver})
BuildRequires: (php-composer(doctrine/event-manager) >= %{doctrine_event_min_ver} with php-composer(doctrine/event-manager) < %{doctrine_event_max_ver})
BuildRequires: (php-composer(doctrine/reflection) >= %{doctrine_refl_min_ver} with php-composer(doctrine/reflection) < %{doctrine_refl_max_ver})
BuildRequires: (php-composer(doctrine/persistence) >= %{doctrine_pers_min_ver} with php-composer(doctrine/persistence) < %{doctrine_pers_max_ver})
BuildRequires: phpunit7
## phpcompatinfo (computed from version 2.8.1)
BuildRequires: php-date
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-spl
BuildRequires: php-tokenizer
# Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      (php-composer(doctrine/annotations) >= %{doctrine_annotations_min_ver} with php-composer(doctrine/annotations) < %{doctrine_annotations_max_ver})
Requires:      (php-composer(doctrine/cache) >= %{doctrine_cache_min_ver} with php-composer(doctrine/cache) < %{doctrine_cache_max_ver})
Requires:      (php-composer(doctrine/collections) >= %{doctrine_collections_min_ver} with php-composer(doctrine/collections) < %{doctrine_collections_max_ver})
Requires:      (php-composer(doctrine/inflector) >= %{doctrine_inflector_min_ver} with php-composer(doctrine/inflector) < %{doctrine_inflector_max_ver})
Requires:      (php-composer(doctrine/lexer) >= %{doctrine_lexer_min_ver} with php-composer(doctrine/lexer) < %{doctrine_lexer_max_ver})
Requires:      (php-composer(doctrine/event-manager) >= %{doctrine_event_min_ver} with php-composer(doctrine/event-manager) < %{doctrine_event_max_ver})
Requires:      (php-composer(doctrine/reflection) >= %{doctrine_refl_min_ver} with php-composer(doctrine/reflection) < %{doctrine_refl_max_ver})
Requires:      (php-composer(doctrine/persistence) >= %{doctrine_pers_min_ver} with php-composer(doctrine/persistence) < %{doctrine_pers_max_ver})
# phpcompatinfo (computed from version 2.8.1)
Requires:      php-pcre
Requires:      php-reflection
Requires:      php-spl
Requires:      php-tokenizer
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}
# PEAR
Provides:      php-pear(pear.doctrine-project.org/DoctrineCommon) = %{version}
# Rename
Obsoletes:     php-doctrine-DoctrineCommon < %{version}
Provides:      php-doctrine-DoctrineCommon = %{version}

%description
The Doctrine Common project is a library that provides extensions to core PHP
functionality.

Autoloader: %{phpdir}/Doctrine/Common/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}
%patch0 -p1 -b .php8

sed -e 's/2.12.0-DEV/%{version}/' -i lib/Doctrine/Common/Version.php


%build
: Create autoloader
cat <<'AUTOLOAD' | tee lib/Doctrine/Common/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Doctrine\\Common\\', __DIR__);

\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/Doctrine/Common/Annotations/autoload.php',
    '%{phpdir}/Doctrine/Common/Cache/autoload.php',
    '%{phpdir}/Doctrine/Common/Collections/autoload.php',
    '%{phpdir}/Doctrine/Common/Inflector/autoload.php',
    '%{phpdir}/Doctrine/Common/Lexer/autoload.php',
    '%{phpdir}/Doctrine/Common/EventManager/autoload.php',
    '%{phpdir}/Doctrine/Common/Reflection/autoload.php',
    '%{phpdir}/Doctrine/Common/Persistence/autoload.php',
));
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}
cp -rp lib/* %{buildroot}%{phpdir}/


%check
: Library version value check
%{_bindir}/php -r '
    require_once "%{buildroot}%{phpdir}/Doctrine/Common/Version.php";
    $version = \Doctrine\Common\Version::VERSION;
    echo "Version $version (expected %{version})\n";
    exit(version_compare("%{version}", "$version", "=") ? 0 : 1);
'

%if %{with tests}
: Modify tests init
sed "s#require.*autoload.*#require_once '%{buildroot}%{phpdir}/Doctrine/Common/autoload.php';#" \
     -i tests/Doctrine/Tests/TestInit.php


: Upstream tests
RETURN_CODE=0
for PHP_EXEC in "" php73 php74 php80; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC %{_bindir}/phpunit7 --verbose || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif


%files
%license LICENSE
%doc *.md
%doc UPGRADE*
%doc composer.json
%{phpdir}/Doctrine/Common/*.php
%{phpdir}/Doctrine/Common/Proxy
%{phpdir}/Doctrine/Common/Util


%changelog
* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.13.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.13.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.13.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Feb 07 2023 Shawn Iwinski <shawn.iwinski@gmail.com> - 1:2.13.3-9
- Disable tests by default
- FTBFS (RHBZ #2046813)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.13.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.13.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.13.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.13.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Mar 31 2021 Remi Collet <remi@remirepo.net> - 2.13.3-4
- add minimal patch to fix test suite for PHP 8

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.13.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.13.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun  8 2020 Remi Collet <remi@remirepo.net> - 2.13.3-1
- update to 2.13.3

* Tue Jun  2 2020 Remi Collet <remi@remirepo.net> - 2.13.2-1
- update to 2.13.2

* Tue May 26 2020 Remi Collet <remi@remirepo.net> - 2.13.1-1
- update to 2.13.1

* Fri May 15 2020 Remi Collet <remi@remirepo.net> - 2.13.0-1
- update to 2.13.0
- raise dependency on doctrine/persistence 1.3.3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 2020 Remi Collet <remi@remirepo.net> - 2.12.0-1
- update to 2.12.0

* Tue Sep 10 2019 Remi Collet <remi@remirepo.net> - 2.11.0-1
- update to 2.11.0
- switch to phpunit7

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 22 2018 Remi Collet <remi@remirepo.net> - 2.10.0-1
- update to 2.10.0
- raise dependency on doctrine/persistence 1.1

* Thu Oct 18 2018 Remi Collet <remi@remirepo.net> - 2.9.0-1
- update to 2.9.0
- switch to phpunit6
- add dependency on doctrine/event-manager
- add dependency on doctrine/reflection
- add dependency on doctrine/persistence

* Wed Oct 17 2018 Remi Collet <remi@remirepo.net> - 2.8.1-1
- update to 2.8.1
- raise dependency on PHP 7.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 23 2018 Shawn Iwinski <shawn.iwinski@gmail.com> - 1:2.7.3-2
- Fix PHP dependency version for downgrade

* Sun Apr 22 2018 Shawn Iwinski <shawn.iwinski@gmail.com> - 1:2.7.3-1
- Downgraded to 2.7.3 (i.e. latest version less than 2.8 which is required by
  php-doctrine-dbal-2.5.12)

* Sun Apr 22 2018 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.8.1-1
- Updated to 2.8.1 (RHBZ #1258673)
- Update get source script to save source in same directory
- Add range version dependencies for Fedora >= 27 || RHEL >= 8
- Add composer.json to repo

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 09 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.7.2-1
- Updated to 2.7.2 (RHBZ #1258673)

* Fri May 12 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.5.3-3
- Switch autoloader to php-composer(fedora/autoloader)
- Add max versions to build dependencies
- Test with SCLs if available

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul 22 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.5.3-1
- Updated to 2.5.3 (RHBZ #1347924 / CVE-2015-5723)
- Added library version value check

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jun 27 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.5.0-1
- Updated to 2.5.0 (RHBZ #1209683)
- Added autoloader
- %%license usage

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 20 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.4.2-3
- Added php-composer(%%{composer_vendor}/%%{composer_project}) virtual provide
- Added option to build without tests ("--without tests")
- Updated dependencies to use php-composer virtual provides

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.4.2-1
- Updated to 2.4.2 (BZ #1100718)

* Sat Jan 04 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.4.1-2
- Conditional %%{?dist}
- Removed php-channel-doctrine obsolete

* Fri Dec 27 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.4.1-1
- Initial package
