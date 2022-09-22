#
# Fedora spec file for php-codeception-verify
#
# Copyright (c) 2017-2019 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     Codeception
%global github_name      Verify
%global github_version   1.0.0
%global github_commit    f45b39025b3f5cfd9a9d8fb992432885ff5380c1

%global composer_vendor  codeception
%global composer_project verify

# "php": ">= 7.0"
%global php_min_ver 7.0
# "phpunit/phpunit": "> 6.0"

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       8%{?github_release}%{?dist}
Summary:       BDD assertion library for PHPUnit

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Autoloader
BuildRequires: php-fedora-autoloader-devel
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
# "phpunit/phpunit": "> 6.0"
# NOTE: Using PHPUnit 7 to be compatible with php-codeception-specify 1.1.0 ("phpunit/phpunit": "^7.0")
BuildRequires: phpunit7
## phpcompatinfo (computed from version 1.0.0)
##     <none>
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

#composer.json
Requires:      php(language) >= %{php_min_ver}
# "phpunit/phpunit": "> 6.0"
# NOTE: Using PHPUnit 7 to be compatible with php-codeception-specify 1.1.0 ("phpunit/phpunit": "^7.0")
Requires:      phpunit7
# phpcompatinfo (computed from version 1.0.0)
#     <none>
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
BDD Assertions for PHPUnit and Codeception

This is very tiny wrapper for PHPUnit assertions, that are aimed to make tests
a bit more readable. With BDD assertions influenced by Chai, Jasmine, and
RSpec your assertions would be a bit closer to natural language.

Autoloader: %{phpdir}/Codeception/autoload-verify.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
%{_bindir}/phpab --template fedora --output src/Codeception/autoload-verify.php src/
cat <<'AUTOLOAD' | tee -a src/Codeception/autoload-verify.php

\Fedora\Autoloader\Dependencies::required([
    __DIR__.'/function.php',
    '%{phpdir}/PHPUnit7/autoload.php',
]);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/Codeception
cp -rp src/Codeception/* %{buildroot}%{phpdir}/Codeception/


%check
%if %{with_tests}
: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit7)
for PHP_EXEC in php %{?rhel:php54 php55} php56 php70 php71 php72 php73 php74; do
    if [ "php" == "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose \
            --bootstrap %{buildroot}%{phpdir}/Codeception/autoload-verify.php \
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
%dir %{phpdir}/Codeception
     %{phpdir}/Codeception/Verify.php
     %{phpdir}/Codeception/autoload-verify.php
     %{phpdir}/Codeception/function.php


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

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

* Mon May 27 2019 Shawn Iwinski <shawn@iwin.ski> - 1.0.0-1
- Update to 1.0.0 (RHBZ #1512283)
- Add range version dependencies for Fedora >= 27 || RHEL >= 8

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 20 2017 Shawn Iwinski <shawn@iwin.ski> - 0.4.0-1
- Initial package
