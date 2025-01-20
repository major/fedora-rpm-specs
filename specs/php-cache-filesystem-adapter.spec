#
# Fedora spec file for php-cache-filesystem-adapter
#
# Copyright (c) 2017-2021 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     php-cache
%global github_name      filesystem-adapter
%global github_version   1.1.0
%global github_commit    1501ca71502f45114844824209e6a41d87afb221

%global composer_vendor  cache
%global composer_project filesystem-adapter

# "php": "^5.6 || ^7.0 || ^8.0"
%global php_min_ver 5.6
# "cache/adapter-common": "^1.0"
%global cache_adapter_common_min_ver 1.0
%global cache_adapter_common_max_ver 2.0
# "cache/integration-tests": "^0.16"
%global cache_integration_tests_min_ver 0.16
%global cache_integration_tests_max_ver 1.0
# "league/flysystem": "^1.0"
%global league_flysystem_min_ver 1.0
%global league_flysystem_max_ver 2.0
# "psr/cache": "^1.0"
%global psr_cache_min_ver 1.0
%global psr_cache_max_ver 2.0
# "psr/simple-cache": "^1.0"
%global psr_simple_cache_min_ver 1.0
%global psr_simple_cache_max_ver 2.0

# Build using "--without tests" to disable tests
%bcond_without tests

# Range dependencies supported?
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
%global with_range_dependencies 1
%else
%global with_range_dependencies 0
%endif

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       9%{?github_release}%{?dist}
Summary:       A PSR-6 cache implementation using filesystem

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests
# Run php-cache-filesystem-adapter-get-source.sh to create full source
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
%if %{with_range_dependencies}
BuildRequires: (php-composer(cache/adapter-common) >= %{cache_adapter_common_min_ver} with php-composer(cache/adapter-common) < %{cache_adapter_common_max_ver})
BuildRequires: (php-composer(cache/integration-tests) >= %{cache_integration_tests_min_ver} with php-composer(cache/integration-tests) < %{cache_integration_tests_max_ver})
BuildRequires: (php-composer(league/flysystem) >= %{league_flysystem_min_ver} with php-composer(league/flysystem) < %{league_flysystem_max_ver})
BuildRequires: (php-composer(psr/cache) >= %{psr_cache_min_ver} with php-composer(psr/cache) < %{psr_cache_max_ver})
BuildRequires: (php-composer(psr/simple-cache) >= %{psr_simple_cache_min_ver} with php-composer(psr/simple-cache) < %{psr_simple_cache_max_ver})
%else
BuildRequires: php-composer(cache/adapter-common) <  %{cache_adapter_common_max_ver}
BuildRequires: php-composer(cache/adapter-common) >= %{cache_adapter_common_min_ver}
BuildRequires: php-composer(cache/integration-tests) <  %{cache_integration_tests_max_ver}
BuildRequires: php-composer(cache/integration-tests) >= %{cache_integration_tests_min_ver}
BuildRequires: php-composer(league/flysystem) <  %{league_flysystem_max_ver}
BuildRequires: php-composer(league/flysystem) >= %{league_flysystem_min_ver}
BuildRequires: php-composer(psr/cache) <  %{psr_cache_max_ver}
BuildRequires: php-composer(psr/cache) >= %{psr_cache_min_ver}
BuildRequires: php-composer(psr/simple-cache) <  %{psr_simple_cache_max_ver}
BuildRequires: php-composer(psr/simple-cache) >= %{psr_simple_cache_min_ver}
%endif
## phpcompatinfo (computed from version 1.1.0)
BuildRequires: php-date
BuildRequires: php-pcre
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
%if %{with_range_dependencies}
Requires:      (php-composer(cache/adapter-common) >= %{cache_adapter_common_min_ver} with php-composer(cache/adapter-common) < %{cache_adapter_common_max_ver})
Requires:      (php-composer(league/flysystem) >= %{league_flysystem_min_ver} with php-composer(league/flysystem) < %{league_flysystem_max_ver})
Requires:      (php-composer(psr/cache) >= %{psr_cache_min_ver} with php-composer(psr/cache) < %{psr_cache_max_ver})
Requires:      (php-composer(psr/simple-cache) >= %{psr_simple_cache_min_ver} with php-composer(psr/simple-cache) < %{psr_simple_cache_max_ver})
%else
Requires:      php-composer(cache/adapter-common) <  %{cache_adapter_common_max_ver}
Requires:      php-composer(cache/adapter-common) >= %{cache_adapter_common_min_ver}
Requires:      php-composer(league/flysystem) <  %{league_flysystem_max_ver}
Requires:      php-composer(league/flysystem) >= %{league_flysystem_min_ver}
Requires:      php-composer(psr/cache) <  %{psr_cache_max_ver}
Requires:      php-composer(psr/cache) >= %{psr_cache_min_ver}
Requires:      php-composer(psr/simple-cache) <  %{psr_simple_cache_max_ver}
Requires:      php-composer(psr/simple-cache) >= %{psr_simple_cache_min_ver}
%endif
# phpcompatinfo (computed from version 1.1.0)
Requires:      php-date
Requires:      php-pcre
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}
Provides:      php-composer(psr/cache-implementation) = 1.0
Provides:      php-composer(psr/simple-cache-implementation) = 1.0

%description
A PSR-6 cache implementation using filesystem. This implementation supports
tags.

Autoloader: %{phpdir}/Cache/Adapter/Filesystem/autoload.php


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

\Fedora\Autoloader\Autoload::addPsr4('Cache\\Adapter\\Filesystem\\', __DIR__);

\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/Cache/Adapter/Common/autoload.php',
    '%{phpdir}/League/Flysystem/autoload.php',
    '%{phpdir}/Psr/Cache/autoload.php',
    '%{phpdir}/Psr/SimpleCache/autoload.php',
]);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/Cache/Adapter/Filesystem
cp -rp * %{buildroot}%{phpdir}/Cache/Adapter/Filesystem/


%check
%if %{with tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require '%{buildroot}%{phpdir}/Cache/Adapter/Filesystem/autoload.php';

\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/Cache/IntegrationTests/autoload.php',
]);
BOOTSTRAP

: Skip tests known to fail
find Tests -type f |
    xargs sed 's|use CreatePoolTrait;|use CreatePoolTrait;\npublic function testBasicUsageWithLongKey() { $this->markTestSkipped("Skipping test known to fail with \\"Failed to open stream: File name too long\\""); }|' -i

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in "" %{?rhel:php70 php71 php72 php73 php74} php80 php81; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose --bootstrap bootstrap.php \
            || RETURN_CODE=1
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
%{phpdir}/Cache/Adapter/Filesystem
%exclude %{phpdir}/Cache/Adapter/Filesystem/*.md
%exclude %{phpdir}/Cache/Adapter/Filesystem/composer.json
%exclude %{phpdir}/Cache/Adapter/Filesystem/LICENSE
%exclude %{phpdir}/Cache/Adapter/Filesystem/phpunit.*
%exclude %{phpdir}/Cache/Adapter/Filesystem/Tests


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Sep 18 2021 Shawn Iwinski <shawn@iwin.ski> - 1.1.0-1
- Update to 1.1.0 (RHBZ #1907647)
- Fix "FTBFS in Fedora rawhide/f35" (RHBZ #1987808)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 01 2019 Shawn Iwinski <shawn@iwin.ski> - 1.0.0-1
- Update to 1.0.0 (RHBZ #1471569)
- Add range version dependencies for Fedora >= 27 || RHEL >= 8

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 30 2017 Shawn Iwinski <shawn@iwin.ski> - 0.4.0-2
- Fix directory ownership

* Fri Apr 14 2017 Shawn Iwinski <shawn@iwin.ski> - 0.4.0-1
- Initial package
