#
# Fedora spec file for php-behat-gherkin
#
# Copyright (c) 2016-2020 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     Behat
%global github_name      Gherkin
%global github_version   4.6.2
%global github_commit    51ac4500c4dc30cbaaabcd2f25694299df666a31

%global composer_vendor  behat
%global composer_project gherkin

%if 0%{?fedora} >= 32 || 0%{?rhel} >= 8
%global with_symfony2 0
%else
%global with_symfony2 1
%endif

# "php": ">=5.3.1"
%global php_min_ver 5.3.1
# "symfony/yaml": "~2.3|~3|~4"
%if %{with_symfony2}
#     NOTE: Min version not 2.3 because autoloader required
%global symfony_min_ver %{?el6:2.3.31}%{!?el6:2.7.1}
%else
%global symfony_min_ver 3.0
%endif
%global symfony_max_ver 5.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

# Range dependencies supported?
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
%global with_range_dependencies 1
%else
%global with_range_dependencies 0
%endif

%global phpdir   %{_datadir}/php

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       8%{?dist}
Summary:       Gherkin DSL parser for PHP

License:       MIT
URL:           http://behat.org/
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
%if %{with_range_dependencies}
BuildRequires: (php-composer(symfony/yaml) >= %{symfony_min_ver} with php-composer(symfony/yaml) < %{symfony_max_ver})
%else
BuildRequires: php-composer(symfony/yaml) >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/yaml) <  %{symfony_max_ver}
%endif
## phpcompatinfo (computed from version 4.6.1)
BuildRequires: php-ctype
BuildRequires: php-date
BuildRequires: php-mbstring
BuildRequires: php-pcre
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 4.6.1)
Requires:      php-ctype
Requires:      php-date
Requires:      php-mbstring
Requires:      php-pcre
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# composer.json: suggest
%if 0%{?fedora} >= 21
Suggests:      php-composer(symfony/yaml)
%endif

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
%{summary}.

Autoloader: %{phpdir}/Behat/Gherkin/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create library autoloader
cat <<'AUTOLOAD' | tee src/Behat/Gherkin/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Behat\\Gherkin\\', __DIR__);

\Fedora\Autoloader\Dependencies::optional(array(
    array(
        '%{phpdir}/Symfony4/Component/Yaml/autoload.php',
        '%{phpdir}/Symfony3/Component/Yaml/autoload.php',
%if %{with_symfony2}
        '%{phpdir}/Symfony/Component/Yaml/autoload.php',
%endif
    ),
));
AUTOLOAD


%install
mkdir -p  %{buildroot}%{phpdir}/Behat
cp -pr src/Behat/Gherkin %{buildroot}%{phpdir}/Behat/


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'AUTOLOAD' | tee bootstrap.php
<?php
require_once '%{buildroot}%{phpdir}/Behat/Gherkin/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Tests\\Behat\\', __DIR__.'/tests/Behat');
AUTOLOAD

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in php %{?rhel:php54 php55} php56 php70 php71 php72 php73 php74; do
    if [ "php" = "$PHP_EXEC" ] || which $PHP_EXEC; then
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
%dir %{phpdir}/Behat
     %{phpdir}/Behat/Gherkin


%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar 18 2020  Shawn Iwinski <shawn@iwin.ski> - 4.6.2-1
- Update to 4.6.2 (RHBZ #1808131)

* Tue Mar 17 2020  Shawn Iwinski <shawn@iwin.ski> - 4.6.1-2
- Conditional Symfony 2 or not

* Tue Mar 17 2020  Shawn Iwinski <shawn@iwin.ski> - 4.6.1-1
- Update to 4.6.1 (RHBZ #1808131)
- Conditionally use range dependencies
- Drop Symfony 2 interoperability

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 20 2017 Shawn Iwinski <shawn@iwin.ski> - 4.4.5-1
- Update to 4.4.5
- Switch autoloader to fedora/autoloader
- Test with SCLs if available

* Mon Aug 15 2016 Shawn Iwinski <shawn@iwin.ski> - 4.4.1-1
- Initial package
