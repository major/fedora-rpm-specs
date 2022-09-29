# remirepo/fedora spec file for php-doctrine-common3
#
# Copyright (c) 2013-2022 Shawn Iwinski, Remi Collet
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     doctrine
%global github_name      common
%global github_version   3.4.1
%global github_commit    616d5fca274ea66b969cdebbbfd1dc33a87d461b
%global major            3

%global composer_vendor  doctrine
%global composer_project common

%global ns_vendor        Doctrine
%global ns_project       Common

# "php": "^7.1 || ^8.0"
%global php_min_ver 7.1
# "doctrine/persistence": "^2.0 || ^3.0"
%global doctrine_pers_min_ver 2.0
%global doctrine_pers_max_ver 4
# "doctrine/collections": "^1",
%global doctrine_coll_min_ver 1
%global doctrine_coll_max_ver 2

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}%{major}
Epoch:         1
Version:       %{github_version}
Release:       1%{?dist}
Summary:       Common library for Doctrine projects version %{major}

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests.
# Run php-doctrine-common-get-source.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       makesrc.sh

BuildArch:     noarch
# Library version value check
BuildRequires: php-cli
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: (php-composer(doctrine/persistence) >= %{doctrine_pers_min_ver} with php-composer(doctrine/persistence) < %{doctrine_pers_max_ver})
BuildRequires: (php-composer(doctrine/collections) >= %{doctrine_coll_min_ver} with php-composer(doctrine/collections) < %{doctrine_coll_max_ver})
%global phpunit %{_bindir}/phpunit9
BuildRequires: phpunit9 >= 9.0
## phpcompatinfo (computed from version 3.0.0)
BuildRequires: php-reflection
BuildRequires: php-date
BuildRequires: php-pcre
BuildRequires: php-spl
%endif
# Autoloader
BuildRequires: php-fedora-autoloader-devel

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      (php-composer(doctrine/persistence) >= %{doctrine_pers_min_ver} with php-composer(doctrine/persistence) < %{doctrine_pers_max_ver})
# phpcompatinfo (computed from version 3.0.0)
Requires:      php-reflection
Requires:      php-pcre
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}


%description
The Doctrine Common project is a library that provides extensions to core PHP
functionality.

Autoloader: %{phpdir}/%{ns_vendor}/%{ns_project}%{major}/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
phpab --template fedora \
      --output src/autoload.php \
      src

cat <<'AUTOLOAD' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    [
        '%{phpdir}/%{ns_vendor}/Persistence3/autoload.php',
        '%{phpdir}/%{ns_vendor}/Persistence2/autoload.php',
    ],
]);
AUTOLOAD


%install
mkdir -p   %{buildroot}%{phpdir}/%{ns_vendor}
cp -rp src %{buildroot}%{phpdir}/%{ns_vendor}/%{ns_project}%{major}


%check
%if %{with_tests}
cat << 'AUTOLOAD' | tee bs.php
<?php
require_once '%{buildroot}%{phpdir}/%{ns_vendor}/%{ns_project}%{major}/autoload.php';
\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/%{ns_vendor}/Common/Collections/autoload.php',
]);
\Fedora\Autoloader\Autoload::addPsr4('Doctrine\\Tests\\', __DIR__ . '/tests');
AUTOLOAD

: Upstream tests
RETURN_CODE=0
for CMDARG in "php %{phpunit}" php74 php80 php81 php82; do
    if which $CMDARG; then
        set $CMDARG
        $1 ${2:-%{_bindir}/phpunit9} \
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
%doc UPGRADE*
%doc composer.json
%{phpdir}/%{ns_vendor}/%{ns_project}%{major}


%changelog
* Tue Sep 27 2022 Remi Collet <remi@remirepo.net> - 3.4.1-1
- update to 3.4.1

* Fri Sep  9 2022 Remi Collet <remi@remirepo.net> - 3.4.0-1
- update to 3.4.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Apr 19 2022 Remi Collet <remi@remirepo.net> - 3.3.0-1
- update to 3.3.0
- allow doctrine/persistence v3

* Wed Feb  2 2022 Remi Collet <remi@remirepo.net> - 3.2.2-1
- update to 3.2.2

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan  3 2022 Remi Collet <remi@remirepo.net> - 3.2.1-1
- update to 3.2.1

* Wed Oct 20 2021 Remi Collet <remi@remirepo.net> - 3.2.0-1
- update to 3.2.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Apr  6 2021 Remi Collet <remi@remirepo.net> - 3.1.2-1
- update to 3.1.2

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 21 2021 Remi Collet <remi@remirepo.net> - 3.1.1-1
- update to 3.1.1

* Tue Dec  8 2020 Remi Collet <remi@remirepo.net> - 3.1.0-1
- update to 3.1.0
- switch to phpunit9

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun  8 2020 Remi Collet <remi@remirepo.net> - 3.0.2-1
- update to 3.0.2

* Tue Jun  2 2020 Remi Collet <remi@remirepo.net> - 3.0.1-1
- update to 3.0.1

* Tue May 26 2020 Remi Collet <remi@remirepo.net> - 3.0.0-1
- update to 3.0.0
- rename to php-doctrine-common3
- move to /usr/share/php/Doctrine/Common3
- raise dependency on doctrine/persistence 2.0
- drop dependency on doctrine/inflector, doctrine/cache, doctrine/collections,
  doctrine/lexer, doctrine/annotations, doctrine/event-manager and
  and doctrine/reflection

* Tue May 26 2020 Remi Collet <remi@remirepo.net> - 2.13.1-1
- update to 2.13.1

* Fri May 15 2020 Remi Collet <remi@remirepo.net> - 2.13.0-1
- update to 2.13.0
- raise dependency on doctrine/persistence 1.3.3

* Mon Jan 13 2020 Remi Collet <remi@remirepo.net> - 2.12.0-1
- update to 2.12.0

* Tue Sep 10 2019 Remi Collet <remi@remirepo.net> - 2.11.0-1
- update to 2.11.0
- switch to phpunit7

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

* Sun Jul 09 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.7.2-1
- Updated to 2.7.2 (RHBZ #1258673)

* Fri May 12 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.5.3-3
- Switch autoloader to php-composer(fedora/autoloader)
- Add max versions to build dependencies
- Test with SCLs if available

* Fri Jul 22 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.5.3-1
- Updated to 2.5.3 (RHBZ #1347924 / CVE-2015-5723)
- Added library version value check

* Sat Jun 27 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.5.0-1
- Updated to 2.5.0 (RHBZ #1209683)
- Added autoloader
- %%license usage

* Fri Jun 20 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.4.2-3
- Added php-composer(%%{composer_vendor}/%%{composer_project}) virtual provide
- Added option to build without tests ("--without tests")
- Updated dependencies to use php-composer virtual provides

* Mon May 26 2014 Remi Collet <rpms@famillecollet.com> 2.4.2-1
- backport 2.4.2 for remi repo

* Fri May 23 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.4.2-1
- Updated to 2.4.2 (BZ #1100718)

* Sat Jan 11 2014 Remi Collet <rpms@famillecollet.com> 2.4.1-2
- backport for remi repo

* Sat Jan 04 2014 Shawn Iwinski <shawn.iwinski@gmail.com> 2.4.1-2
- Conditional %%{?dist}
- Removed php-channel-doctrine obsolete

* Fri Dec 27 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 2.4.1-1
- Initial package
