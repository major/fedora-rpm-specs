# remirepo/fedora spec file for php-league-container4
#
# Copyright (c) 2016-2024 Shawn Iwinski <shawn@iwin.ski>
#                         Remi Collet <remi@remirepo.net>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     thephpleague
%global github_name      container
%global github_version   4.2.4
%global github_commit    7ea728b013b9a156c409c6f0fc3624071b742dec

%global major            4

%global composer_vendor  league
%global composer_project container

# "php": "^7.2 || ^8.0"
%global php_min_ver 7.2
# "psr/container": "^1.1 || ^2.0"
%global psr_container_min_ver 1.1
%global psr_container_max_ver 3

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}%{major}
Version:       %{github_version}
Release:       2%{?github_release}%{?dist}
Summary:       A fast and intuitive dependency injection container version %{major}

License:       MIT
URL:           http://container.thephpleague.com/

# GitHub export does not include tests.
# Run php-league-container-get-source.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: phpunit8 >= 8.5.17
BuildRequires: (php-composer(psr/container) >= %{psr_container_min_ver} with php-composer(psr/container) < %{psr_container_max_ver})
## phpcompatinfo (computed from version 3.2.2)
BuildRequires: php-reflection
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      (php-composer(psr/container) >= %{psr_container_min_ver} with php-composer(psr/container) < %{psr_container_max_ver})
# phpcompatinfo (computed from version 3.3.5)
Requires:      php-reflection
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}
Provides:      php-composer(psr/container-implementation) =  1.0

%description
A small but powerful dependency injection container that allows you to decouple
components in your application in order to write clean and testable code.

Autoloader: %{phpdir}/League/Container%{major}/autoload.php


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

\Fedora\Autoloader\Autoload::addPsr4('League\\Container\\', __DIR__);

\Fedora\Autoloader\Dependencies::required([
    [
        '%{phpdir}/Psr/Container2/autoload.php',
        '%{phpdir}/Psr/Container/autoload.php',
    ]
]);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/League
cp -rp src %{buildroot}%{phpdir}/League/Container%{major}


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require '%{buildroot}%{phpdir}/League/Container%{major}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('League\\Container\\Test\\', __DIR__.'/tests');
require __DIR__ . '/tests/Asset/function.php';
BOOTSTRAP

: cleanup for phpunit8/9
sed -e '/log/d' -i phpunit.xml

: Upstream tests
RETURN_CODE=0
# TODO PHP 8.1, Call to undefined method ReflectionUnionType::getName()
PHPUNIT=$(which phpunit8)
for PHP_EXEC in php php81 php82 php83 php84; do
    if which $PHP_EXEC; then
        FILTER="--filter '^((?!(testResolverResolvesArgumentsViaReflection|testResolverThrowsExceptionWhenReflectionDoesNotResolve)).)*\$'"
        $PHP_EXEC $PHPUNIT $FILTER \
            --bootstrap bootstrap.php \
            --verbose || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif


%files
%license LICENSE.md
%doc CHANGELOG.md
%doc composer.json
%doc CONTRIBUTING.md
%doc README.md
%dir %{phpdir}/League
     %{phpdir}/League/Container%{major}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Nov 12 2024 Remi Collet <remi@remirepo.net> - 4.2.4-1
- update to 4.2.4

* Wed Oct 23 2024 Remi Collet <remi@remirepo.net> - 4.2.3-1
- update to 4.2.3

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Mar 13 2024 Remi Collet <remi@remirepo.net> - 4.2.2-1
- update to 4.2.2

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 16 2021 Remi Collet <remi@remirepo.net> - 4.2.0-1
- update to 4.2.0
- allow psr/container 1.1

* Fri Jul  9 2021 Remi Collet <remi@remirepo.net> - 3.4.1-1
- update to 4.1.2
- rename to php-league-container4
- install in /usr/share/php/League/Container4
- raise dependency on PHP 7.2
- raise dependency on psr/container 2.0.0

* Fri Jul  9 2021 Remi Collet <remi@remirepo.net> - 3.4.1-1
- update to 3.4.1
- revert allow psr/container v2

* Wed Mar 17 2021 Remi Collet <remi@remirepo.net> - 3.3.5-1
- update to 3.3.5
- switch to phpunit8
- allow psr/container v2

* Sun Jun 16 2019 Shawn Iwinski <shawn@iwin.ski> - 3.2.2-1
- Update to 3.2.2 (RHBZ #1607388)

* Sun Aug 20 2017 Shawn Iwinski <shawn@iwin.ski> - 2.4.1-1
- Update to 2.4.1
- Switch autoloader to fedora/autoloader
- Test with SCLs if available

* Tue Aug 09 2016 Shawn Iwinski <shawn@iwin.ski> - 2.2.0-1
- Initial package
