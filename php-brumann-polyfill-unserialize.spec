#
# Fedora spec file for php-brumann-polyfill-unserialize
#
# Copyright (c) 2019-2021 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     dbrumann
%global github_name      polyfill-unserialize
%global github_version   1.0.4
%global github_commit    8ed1cd343ddc134a7ef649aca0aa0fe2a1b45008

%global composer_vendor  brumann
%global composer_project polyfill-unserialize

# "php": "^5.3|^7.0"
%global php_min_ver 5.3

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       7%{?github_release}%{?dist}
Summary:       Backports unserialize options introduced in PHP 7.0

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests.
# Run php-brumann-polyfill-unserialize-get-source.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
## phpcompatinfo for version 1.0.4
BuildRequires: php-pcre
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo for version 1.0.4
Requires:      php-pcre
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Backports unserialize options introduced in PHP 7.0 to older PHP versions. This
was originally designed as a Proof of Concept for Symfony Issue
[#21090](https://github.com/symfony/symfony/pull/21090).

You can use this package in projects that rely on PHP versions older than PHP
7.0. In case you are using PHP 7.0+ the original unserialize() will be used
instead.

From the
[documentation](https://secure.php.net/manual/en/function.unserialize.php):

> Warning: Do not pass untrusted user input to unserialize(). Unserialization
> can result in code being loaded and executed due to object instantiation and
> autoloading, and a malicious user may be able to exploit this.

This warning holds true even when `allowed_classes` is used.

Autoloader: %{phpdir}/Brumann/Polyfill/autoload.php


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

\Fedora\Autoloader\Autoload::addPsr4('Brumann\\Polyfill\\', __DIR__);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/Brumann
cp -rp src %{buildroot}%{phpdir}/Brumann/Polyfill


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require '%{buildroot}%{phpdir}/Brumann/Polyfill/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Tests\\Brumann\\Polyfill\\', __DIR__.'/tests');
BOOTSTRAP

# SKIP test_with_parent_not_allowed_serialized_class_is_not_accessible: notice promoted to warning

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in php php73 php74 php80; do
    if [ "php" == "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT \
          --bootstrap bootstrap.php \
          --filter '^((?!(test_with_parent_not_allowed_serialized_class_is_not_accessible)).)*$' \
          --verbose || RETURN_CODE=1
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
%dir %{phpdir}/Brumann
     %{phpdir}/Brumann/Polyfill


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Apr  6 2021 Remi Collet <remi@remirepo.net> - 1.0.4-4
- skip 1 test failing with PHP 8

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Apr 05 2020 Shawn Iwinski <shawn@iwin.ski> - 1.0.4-1
- Update to 1.0.4 (RHBZ #1742087)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 08 2019 Shawn Iwinski <shawn@iwin.ski> - 1.0.3-1
- Initial package
