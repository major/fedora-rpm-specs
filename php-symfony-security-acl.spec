#
# Fedora spec file for php-symfony-securiy-acl
#
# Copyright (c) 2016-2019 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     symfony
%global github_name      security-acl
%global github_version   2.8.0
%global github_commit    4a3f7327ad215242c78f6564ad4ea6d2db1b8347

%global composer_vendor  symfony
%global composer_project security-acl

# "php": ">=5.3.9"
%global php_min_ver 5.3.9
# "symfony/phpunit-bridge": "~2.7|~3.0.0"
# "symfony/security-core": "~2.4|~3.0.0"
#     NOTE: Min version not 2.7 because autoloader required
%global symfony_min_ver 2.7.1
%global symfony_max_ver 4.0
# "doctrine/common": "~2.2"
#     NOTE: Min version not 2.2 because autoloader required
%global doctrine_common_min_ver 2.5.0
%global doctrine_common_max_ver 3.0
# "doctrine/dbal": "~2.2"
#     NOTE: Min version not 2.2 because autoloader required
%global doctrine_dbal_min_ver 2.5.4
%global doctrine_dbal_max_ver 3.0
# "psr/log": "~1.0"
#     NOTE: Min version not 1.0 because autoloader required
%global psr_log_min_ver 1.0.1
%global psr_log_max_ver 2.0

# Build using "--with tests" to enable tests
%bcond_with tests

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       17%{?github_release}%{?dist}
Summary:       Symfony Security Component - ACL (Access Control List)

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Tests
%if %{with tests}
## composer.json
BuildRequires: php(language)                       >= %{php_min_ver}
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires:(php-composer(doctrine/common)       >= %{doctrine_common_min_ver} with php-composer(doctrine/common)       <  %{doctrine_common_max_ver})
BuildRequires:(php-composer(doctrine/dbal)         >= %{doctrine_dbal_min_ver}   with php-composer(doctrine/dbal)         <  %{doctrine_dbal_max_ver})
BuildRequires:(php-composer(psr/log)               >= %{psr_log_min_ver}         with php-composer(psr/log)               <  %{psr_log_max_ver})
BuildRequires:(php-composer(symfony/security-core) >= %{symfony_min_ver}         with php-composer(symfony/security-core) <  %{symfony_max_ver})
%else
BuildRequires: php-composer(doctrine/common)       <  %{doctrine_common_max_ver}
BuildRequires: php-composer(doctrine/common)       >= %{doctrine_common_min_ver}
BuildRequires: php-composer(doctrine/dbal)         <  %{doctrine_dbal_max_ver}
BuildRequires: php-composer(doctrine/dbal)         >= %{doctrine_dbal_min_ver}
BuildRequires: php-composer(psr/log)               <  %{psr_log_max_ver}
BuildRequires: php-composer(psr/log)               >= %{psr_log_min_ver}
BuildRequires: php-composer(symfony/security-core) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/security-core) >= %{symfony_min_ver}
%endif
BuildRequires: php-composer(phpunit/phpunit)
## phpcompatinfo (computed from version 2.8.0)
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:     (php-composer(symfony/security-core) >= %{symfony_min_ver} with php-composer(symfony/security-core) <  %{symfony_max_ver})
%else
Requires:      php-composer(symfony/security-core) <  %{symfony_max_ver}
Requires:      php-composer(symfony/security-core) >= %{symfony_min_ver}
%endif
# phpcompatinfo (computed from version 2.8.0)
Requires:      php-pcre
Requires:      php-reflection
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Weak dependencies
%if 0%{?fedora} >= 21
Suggests:      php-composer(doctrine/dbal)
Suggests:      php-composer(symfony/finder)
%endif

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

# Extracted from Symfony as of version 2.8.0
Conflicts:     php-symfony-security < 2.8.0

%description
%{summary}.

Autoloader: %{phpdir}/Symfony/Component/Security/Acl/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
cat <<'AUTOLOAD' | tee autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Symfony\\Component\\Security\\Acl\\', __DIR__);

\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/Doctrine/DBAL/autoload.php',
    array(
        '%{phpdir}/Symfony3/Component/Security/autoload.php',
        '%{phpdir}/Symfony/Component/Security/autoload.php',
    ),
));

\Fedora\Autoloader\Dependencies::optional(array(
    '%{phpdir}/Doctrine/DBAL/autoload.php',
    array(
        '%{phpdir}/Symfony3/Component/Finder/autoload.php',
        '%{phpdir}/Symfony/Component/Finder/autoload.php',
    ),
));
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/Symfony/Component/Security/Acl
cp -rp * %{buildroot}%{phpdir}/Symfony/Component/Security/Acl/


%check
%if %{with tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require_once '%{buildroot}%{phpdir}/Symfony/Component/Security/Acl/autoload.php';

\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/Doctrine/Common/autoload.php',
    '%{phpdir}/Psr/Log/autoload.php',
));
BOOTSTRAP

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in "" %{?rhel:php54 php55 php56 php70} php71 php72 php73 php74; do
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
%{phpdir}/Symfony/Component/Security/Acl
%exclude %{phpdir}/Symfony/Component/Security/Acl/*.md
%exclude %{phpdir}/Symfony/Component/Security/Acl/composer.json
%exclude %{phpdir}/Symfony/Component/Security/Acl/LICENSE
%exclude %{phpdir}/Symfony/Component/Security/Acl/phpunit.*
%exclude %{phpdir}/Symfony/Component/Security/Acl/Tests


%changelog
* Tue Feb 07 2023 Shawn Iwinski <shawn@iwin.ski> - 2.8.0-17
- Disable tests by default
- FTBFS (RHBZ #2046835)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-13
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 12 2019 Remi Collet <remi@remirepo.net> - 2.8.0-9
- use range dependencies

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 21 2017 Shawn Iwinski <shawn@iwin.ski> - 2.8.0-4
- Add max versions to BuildRequires
- Switch autoloader to fedora/autoloader
- Remove Conflicts for Suggests
- Test with SCLs if available

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri May 20 2016 Shawn Iwinski <shawn@iwin.ski> - 2.8.0-1
- Initial package
