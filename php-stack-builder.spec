#
# Fedora spec file for php-stack-builder
#
# Copyright (c) 2015-2020 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     stackphp
%global github_name      builder
%global github_version   1.0.6
%global github_commit    a4faaa6f532c6086bc66c29e1bc6c29593e1ca7c

%global composer_vendor  stack
%global composer_project builder

# "php": ">=7.2.0"
%global php_min_ver 7.2.0
# "symfony/http-foundation": "~2.1|~3.0|~4.0|~5.0"
# "symfony/http-kernel": "~2.1|~3.0|~4.0|~5.0"
# "symfony/routing": "^5.0"
#     NOTE: Forcing v3+ (i.e. dropping Symfony 2 interoperability)
#     NOTE: Loosening "symfony/routing" version (only a dev dependency and tests pass)
%global symfony_min_ver 3.0
%global symfony_max_ver 6.0

# Build using "--without tests" to disable tests
%global with_tests  %{?_without_tests:0}%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       6%{?github_release}%{?dist}
Summary:       Builder for stack middleware based on HttpKernelInterface

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

Patch0:        %{name}-fix-tests-bootstrap-for-symfony-lt-5.patch

BuildArch:     noarch
# Autoloader
BuildRequires: php-composer(theseer/autoload)
# Tests
%if %{with_tests}
BuildRequires: phpunit8
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: (php-composer(symfony/routing) >= %{symfony_min_ver} with php-composer(symfony/routing) < %{symfony_max_ver})
BuildRequires: (php-composer(symfony/http-foundation) >= %{symfony_min_ver} with php-composer(symfony/http-foundation) < %{symfony_max_ver})
BuildRequires: (php-composer(symfony/http-kernel) >= %{symfony_min_ver} with php-composer(symfony/http-kernel) < %{symfony_max_ver})
## phpcompatinfo (computed from version 1.0.6)
BuildRequires: php-reflection
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      (php-composer(symfony/http-foundation) >= %{symfony_min_ver} with php-composer(symfony/http-foundation) < %{symfony_max_ver})
Requires:      (php-composer(symfony/http-kernel) >= %{symfony_min_ver} with php-composer(symfony/http-kernel) < %{symfony_max_ver})
# phpcompatinfo (computed from version 1.0.6)
Requires:      php-reflection
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Builder for stack middlewares based on HttpKernelInterface.

Stack/Builder is a small library that helps you construct a nested
HttpKernelInterface decorator tree. It models it as a stack of middlewares.

Autoloader: %{phpdir}/Stack/autoload-builder.php


%prep
%setup -qn %{github_name}-%{github_commit}

cp tests/bootstrap.php tests/bootstrap.symfony5.php
%patch0 -p1


%build
: Generate autoloader
%{_bindir}/phpab --nolower --output src/Stack/autoload-builder.php src/Stack

cat <<'AUTOLOAD' | tee -a src/Stack/autoload-builder.php

require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Dependencies::required([
    [
        '%{phpdir}/Symfony5/Component/HttpFoundation/autoload.php',
        '%{phpdir}/Symfony4/Component/HttpFoundation/autoload.php',
        '%{phpdir}/Symfony3/Component/HttpFoundation/autoload.php',
    ],
    [
        '%{phpdir}/Symfony5/Component/HttpKernel/autoload.php',
        '%{phpdir}/Symfony4/Component/HttpKernel/autoload.php',
        '%{phpdir}/Symfony3/Component/HttpKernel/autoload.php',
    ],
]);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}
cp -rp src/Stack %{buildroot}%{phpdir}/


%check
%if %{with_tests}
: Create mock Composer autoloader
mkdir vendor
cat <<'BOOTSTRAP' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{phpdir}/Stack/autoload-builder.php';

\Fedora\Autoloader\Dependencies::required([
    [
        '%{phpdir}/Symfony5/Component/Routing/autoload.php',
        '%{phpdir}/Symfony4/Component/Routing/autoload.php',
        '%{phpdir}/Symfony3/Component/Routing/autoload.php',
    ],
]);
BOOTSTRAP

: If Symfony 5 then use unpatched bootstrap
[ -e "%{phpdir}/Symfony5/Component/HttpKernel/autoload.php" ] \
    && mv tests/bootstrap.symfony5.php tests/bootstrap.php

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit8)
for PHP_EXEC in "" php73 php74; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --testsuite unit --verbose || RETURN_CODE=1
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
%dir %{_datadir}/php/Stack
     %{_datadir}/php/Stack/Builder.php
     %{_datadir}/php/Stack/StackedHttpKernel.php
     %{_datadir}/php/Stack/autoload-builder.php


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 26 2020 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.6-1
- Update to 1.0.6 (RHBZ #1796631)
- Drop Symfony 2 interoperability
- Patch tests boostrap to run with Symfony >=5 and <5
- Use range dependencies
- Use PHPUnit 8

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 13 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.5-1
- Update to 1.0.5 (RHBZ #1514861)
- Fix autoloader for multiple versions of Symfony
- Test with SCLs if available

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jul 24 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.4-1
- Update to 1.0.4 (RHBZ #1342093)
- Update autoloader to use dependencies' autoloaders

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat May 16 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.3-1
- Initial package
