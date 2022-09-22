#
# Fedora spec file for php-PhpOption
#
# Copyright (c) 2013-2022 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     schmittjoh
%global github_name      php-option
%global github_version   1.8.1
%global github_commit    eab7a0df01fe2344d172bff4cd6dbd3f8b84ad15

%global composer_vendor  phpoption
%global composer_project phpoption

# "php": "^7.0 || ^8.0"
%global php_min_ver      7.0

# PHPUnit
%global phpunit_require phpunit9
%global phpunit_exec    phpunit9

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-PhpOption
Version:       %{github_version}
Release:       2%{?dist}
Summary:       Option type for PHP

License:       ASL 2.0
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests.
# Run php-PhpOption-get-source.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
BuildRequires: %{phpunit_require}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
## phpcompatinfo (computed from version 1.7.5)
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 1.7.5)
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Standard "php-{COMPOSER_VENDOR}-{COMPOSER_PROJECT}" naming
Provides:      php-%{composer_vendor}-%{composer_project} = %{version}-%{release}
Provides:      php-%{composer_vendor} = %{version}-%{release}
# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
An Option type for PHP.

The Option type is intended for cases where you sometimes might return a value
(typically an object), and sometimes you might return a base value (typically
null) depending on arguments, or other runtime factors.

Often times, you forget to handle the case where a base value should be
returned. Not intentionally of course, but maybe you did not account for all
possible states of the system; or maybe you indeed covered all cases, then time
goes on, code is refactored, some of these your checks might become invalid, or
incomplete. Suddenly, without noticing, the base value case is not handled
anymore. As a result, you might sometimes get fatal PHP errors telling you that
you called a method on a non-object; users might see blank pages, or worse.

On one hand, the Option type forces a developer to consciously think about both
cases (returning a value, or returning a base value). That in itself will
already make your code more robust. On the other hand, the Option type also
allows the API developer to provide more concise API methods, and empowers the
API user in how he consumes these methods.

Autoloader: %{phpdir}/PhpOption/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/PhpOption/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('PhpOption\\', __DIR__);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}
cp -rp src/PhpOption %{buildroot}%{phpdir}/


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require '%{buildroot}%{phpdir}/PhpOption/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('PhpOption\\Tests\\', __DIR__.'/tests/PhpOption/Tests/');
BOOTSTRAP

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which %{phpunit_exec})
for PHP_EXEC in "" php74 php80 php81; do
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
%doc composer.json
%{phpdir}/PhpOption


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Mar 21 2022 Remi Collet <remi@remirepo.net> - 1.8.1-1
- update to 1.8.1

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 17 2020 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.7.5-1
- Update to 1.7.5 (RHBZ #1782417)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 01 2019 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.6.0-1
- Update to 1.6.0 (RHBZ #1771062)
-
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 07 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.5.0-3
- Bump release for rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.5.0-1
- Updated to 1.5.0
- Switched autoloader to php-composer(fedora/autoloader)
- Test with SCLs if available

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jul 11 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.4.0-4
- Added spec license
- Added autoloader
- Added standard "php-{COMPOSER_VENDOR}-{COMPOSER_PROJECT}" naming provides
- Added php-composer(phpoption/phpoption) provide
- %%license usage

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 12 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.4.0-1
- Updated to 1.4.0 (BZ #1055299)

* Sat Sep 28 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.3.0-1
- Updated to 1.3.0
- Other minor updates

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Mar 30 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.0-1
- Updated to version 1.2.0
- Removed tests sub-package

* Tue Jan 22 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1.0-1
- Initial package
