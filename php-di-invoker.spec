#
# Fedora spec file for php-di-invoker
#
# Copyright (c) 2016-2021 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%bcond_without           tests

%global github_owner     PHP-DI
%global github_name      Invoker
%global github_version   2.3.2
%global github_commit    5214cbe5aad066022cd845dbf313f0e47aed928f

%global composer_vendor  php-di
%global composer_project invoker

# "php": "^7.1 || ^8.0"
%global php_min_ver 7.3
# "psr/container": "^1.0|^2.0"
%global psr_container_min_ver 1.0
# version 2 is not yet available
%global psr_container_max_ver 2.0

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          %{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       3%{?github_release}%{?dist}
Summary:       Generic and extensible callable invoker

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests.
# Run php-di-invoker-get-source.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires:(php-composer(psr/container) >= %{psr_container_min_ver} with php-composer(psr/container) < %{psr_container_max_ver})
BuildRequires: phpunit9
## phpcompatinfo (computed from version 2.0.0)
BuildRequires: php-reflection
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:     (php-composer(psr/container) >= %{psr_container_min_ver} with php-composer(psr/container) <  %{psr_container_max_ver})
# phpcompatinfo (computed from version 2.0.0)
Requires:      php-reflection
# Autoloader
Requires:      php-composer(fedora/autoloader)

# php-{COMPOSER_VENDOR}-{COMPOSER_PROJECT}
Provides:      php-%{composer_vendor}-%{composer_project} = %{version}-%{release}
# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
%{summary}.

Autoloader: %{phpdir}/Invoker/autoload.php


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

\Fedora\Autoloader\Autoload::addPsr4('Invoker\\', __DIR__);

\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/Psr/Container/autoload.php',
]);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/Invoker
cp -rp src/* %{buildroot}%{phpdir}/Invoker/


%check
%if %{with tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require_once '%{buildroot}%{phpdir}/Invoker/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Invoker\\Test\\', __DIR__.'/tests');
BOOTSTRAP

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit9)
for PHP_EXEC in php php73 php74 php80 php81; do
    if which $PHP_EXEC; then
        VER=$($PHP_EXEC -r 'echo PHP_VERSION_ID;')
        if [ $VER -ge 80100 ]; then
            FILTER="--filter '^((?!(should_invoke_callable_with_optional_parameter_before_required_parameter)).)*$'"
        else
            FILTER=""
        fi
        $PHP_EXEC $PHPUNIT $FILTER --verbose --bootstrap bootstrap.php \
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
%{phpdir}/Invoker


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug  3 2021 Remi Collet <remi@remirepo.net> - 2.3.2-1
- update to 2.3.2

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Mar 31 2021 Remi Collet <remi@remirepo.net> - 2.3.0-1
- update to 2.3.0
- raise dependency on PHP 7.3
- switch to phpunit9

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 26 2019 Shawn Iwinski <shawn@iwin.ski> - 2.0.0-1
- Update to 2.0.0 (RHBZ #1434817)
- Add range version dependencies for Fedora >= 27 || RHEL >= 8

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 10 2017 Valentin Collet <valentin@famillecollet.com> - 1.3.3-3
- Switch to fedora/autoloader

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jul 23 2016 Shawn Iwinski <shawn@iwin.ski> - 1.3.3-1
- Updated to 1.3.3 (RHBZ #1341396)

* Sun Mar 27 2016 Shawn Iwinski <shawn@iwin.ski> - 1.3.0-1
- Updated to 1.3.0 (RHBZ #1319537)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 03 2016 Shawn Iwinski <shawn@iwin.ski> - 1.2.0-1
- Initial package
