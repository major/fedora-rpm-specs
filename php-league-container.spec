#
# Fedora spec file for php-league-container
#
# Copyright (c) 2016-2021 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     thephpleague
%global github_name      container
%global github_version   3.4.1
%global github_commit    84ecbc2dbecc31bd23faf759a0e329ee49abddbd

%global composer_vendor  league
%global composer_project container

# "php": "^7.0"
%global php_min_ver 7.0
# "psr/container": "^1.0.0"
%global psr_container_min_ver 1.0
%global psr_container_max_ver 2

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       4%{?github_release}%{?dist}
Summary:       A fast and intuitive dependency injection container

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
BuildRequires: phpunit8
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-composer(psr/container) >= %{psr_container_min_ver} with php-composer(psr/container) < %{psr_container_max_ver})
%else
BuildRequires: php-composer(psr/container) >= %{psr_container_min_ver}
BuildRequires: php-composer(psr/container) <  %{psr_container_max_ver}
%endif
## phpcompatinfo (computed from version 3.2.2)
BuildRequires: php-reflection
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-composer(psr/container) >= %{psr_container_min_ver} with php-composer(psr/container) < %{psr_container_max_ver})
%else
Requires:      php-composer(psr/container) >= %{psr_container_min_ver}
Requires:      php-composer(psr/container) <  %{psr_container_max_ver}
%endif
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

Autoloader: %{phpdir}/League/Container/autoload.php


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
    '%{phpdir}/Psr/Container/autoload.php',
]);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/League
cp -rp src %{buildroot}%{phpdir}/League/Container


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require '%{buildroot}%{phpdir}/League/Container/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('League\\Container\\Test\\', __DIR__.'/tests');
BOOTSTRAP

: cleanup for phpunit8/9
sed -e '/log/d' -i phpunit.xml

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit8)
for PHP_EXEC in php php73 php74 php80; do
    if [ "php" = "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --bootstrap bootstrap.php --verbose || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE.md
%doc CHANGELOG.md
%doc composer.json
%doc CONTRIBUTING.md
%doc README.md
%dir %{phpdir}/League
     %{phpdir}/League/Container


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul  9 2021 Remi Collet <remi@remirepo.net> - 3.4.1-1
- update to 3.4.1
- revert allow psr/container v2

* Wed Mar 17 2021 Remi Collet <remi@remirepo.net> - 3.3.5-1
- update to 3.3.5
- switch to phpunit8
- allow psr/container v2

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 16 2019 Shawn Iwinski <shawn@iwin.ski> - 3.2.2-1
- Update to 3.2.2 (RHBZ #1607388)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 20 2017 Shawn Iwinski <shawn@iwin.ski> - 2.4.1-1
- Update to 2.4.1
- Switch autoloader to fedora/autoloader
- Test with SCLs if available

* Tue Aug 09 2016 Shawn Iwinski <shawn@iwin.ski> - 2.2.0-1
- Initial package
