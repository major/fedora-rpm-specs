#
# Fedora spec file for php-PhpCollection
#
# Copyright (c) 2013-2021 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner      schmittjoh
%global github_name       php-collection
%global github_version    0.6.0
%global github_commit     56d18c8c2c0400f2838703246ac7de919a605763

%global composer_vendor   phpcollection
%global composer_project  phpcollection

# "phpoption/phpoption": "1.*"
#     NOTE: min version not 1.0 because autoloader required
%global phpoption_min_ver 1.5.0
%global phpoption_max_ver 2.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-PhpCollection
Version:       %{github_version}
Release:       2%{?dist}
Summary:       General purpose collection library for PHP

Group:         Development/Libraries
License:       ASL 2.0
URL:           http://jmsyst.com/libs/%{github_name}

# GitHub export contains non-allowable licened documentation.
# Run php-PhpCollection-get-source.sh to create allowable source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
BuildRequires: phpunit9
## composer.json
BuildRequires:(php-composer(phpoption/phpoption) >= %{phpoption_min_ver} with php-composer(phpoption/phpoption) <  %{phpoption_max_ver})
## phpcompatinfo (computed from version 0.5.0)
BuildRequires: php(language) >= 5.4.0
BuildRequires: php-date
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:     (php-composer(phpoption/phpoption) >= %{phpoption_min_ver} with php-composer(phpoption/phpoption) <  %{phpoption_max_ver})
# phpcompatinfo (computed from version 0.5.0)
Requires:      php(language) >= 5.4.0
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Standard "php-{COMPOSER_VENDOR}-{COMPOSER_PROJECT}" naming
Provides:      php-%{composer_vendor}-%{composer_project} = %{version}-%{release}
Provides:      php-%{composer_vendor} = %{version}-%{release}
# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
This library adds basic collections for PHP.

Collections can be seen as more specialized arrays for which certain contracts
are guaranteed.

Supported Collections:
* Sequences
** Keys: numerical, consequentially increasing, no gaps
** Values: anything, duplicates allowed
** Classes: Sequence, SortedSequence
* Maps
** Keys: strings or objects, duplicate keys not allowed
** Values: anything, duplicates allowed
** Classes: Map, ObjectMap (not yet implemented)
* Sets (not yet implemented)
** Keys: not meaningful
** Values: anything, each value must be unique (===)
** Classes: Set

General Characteristics:
* Collections are mutable (new elements may be added, existing elements may be
  modified or removed). Specialized immutable versions may be added in the
  future though.
* Equality comparison between elements are always performed using the shallow
  comparison operator (===).
* Sorting algorithms are unstable, that means the order for equal elements is
  undefined (the default, and only PHP behavior).

Autoloader: %{phpdir}/PhpCollection/autoload.php


%prep
%setup -q -n %{github_name}-%{github_commit}


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/PhpCollection/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('PhpCollection\\', __DIR__);

\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/PhpOption/autoload.php',
));
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}
cp -rp src/PhpCollection %{buildroot}%{phpdir}/


%check
%if %{with_tests}
: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit9)
for PHP_EXEC in "" php74 php80 php81; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose \
            --bootstrap %{buildroot}%{phpdir}/PhpCollection/autoload.php \
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
%{phpdir}/PhpCollection


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Mar 21 2022 Remi Collet <remi@remirepo.net> - 0.6.0-1
- update to 0.6.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 07 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.5.0-4
- Bump release for rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 11 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.5.0-1
- Updated to 0.5.0
- Switched autoloader to php-composer(fedora/autoloader)
- Test with SCLs if available

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jul 12 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.4.0-4
- Added spec license
- New source script %%{name}-get-source.sh instead of %%{name}-strip.sh
- Added autoloader
- Added standard "php-{COMPOSER_VENDOR}-{COMPOSER_PROJECT}" naming provides
- Added php-composer(phpcollection/phpcollection) provide
- %%license usage

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 21 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.4.0-1
- Updated to 0.4.0 (BZ #1078754)

* Mon Dec 30 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.3.1-1
- Updated to 0.3.1 (BZ #1045915)
- Spec cleanup

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.3.0-1
- Updated to 0.3.0 (BZ #985339)

* Mon Mar 18 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.2.0-2
- Added %%{name}-strip.sh as Source1

* Sat Mar 16 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.2.0-1
- Updated to version 0.2.0
- Added phpoption_max_ver global
- Bad licensed files stripped from source
- php-common => php(language)
- Removed tests sub-package

* Wed Jan 23 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.1.0-1
- Initial package
