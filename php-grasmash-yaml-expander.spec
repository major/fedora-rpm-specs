#
# Fedora spec file for php-grasmash-yaml-expander
#
# Copyright (c) 2017 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     grasmash
%global github_name      yaml-expander
%global github_version   1.1.1
%global github_commit    720c54b2c99b80d5d696714b6826183d34edce93

%global composer_vendor  grasmash
%global composer_project yaml-expander

# "php": ">=5.4"
%global php_min_ver 5.4
# "dflydev/dot-access-data": "^1.1.0"
%global dot_access_data_min_ver 1.1.0
%global dot_access_data_max_ver 2.0
# "symfony/yaml": "^2.8.11|^3"
%global symfony_min_ver 2.8.11
%global symfony_max_ver 4.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       11%{?github_release}%{?dist}
Summary:       Expands internal property references in a yaml file

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
BuildRequires: php-composer(dflydev/dot-access-data) <  %{dot_access_data_max_ver}
BuildRequires: php-composer(dflydev/dot-access-data) >= %{dot_access_data_min_ver}
BuildRequires: php-composer(symfony/yaml) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/yaml) >= %{symfony_min_ver}
## phpcompatinfo (computed from version 1.1.0)
BuildRequires: php-pcre
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-composer(dflydev/dot-access-data) <  %{dot_access_data_max_ver}
Requires:      php-composer(dflydev/dot-access-data) >= %{dot_access_data_min_ver}
Requires:      php-composer(symfony/yaml) <  %{symfony_max_ver}
Requires:      php-composer(symfony/yaml) >= %{symfony_min_ver}
# phpcompatinfo (computed from version 1.1.0)
Requires:      php-pcre
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
%{summary}.

Autoloader: %{phpdir}/Grasmash/YamlExpander/autoload.php


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

\Fedora\Autoloader\Autoload::addPsr4('Grasmash\\YamlExpander\\', __DIR__);

\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/Dflydev/DotAccessData/autoload.php',
    [
        '%{phpdir}/Symfony3/Component/Yaml/autoload.php',
        '%{phpdir}/Symfony/Component/Yaml/autoload.php',
    ],
]);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/Grasmash
cp -rp src %{buildroot}%{phpdir}/Grasmash/YamlExpander


%check
%if %{with_tests}
: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in php %{?rhel:php55} php56 php70 php71 php72; do
    if which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose \
            --bootstrap %{buildroot}%{phpdir}/Grasmash/YamlExpander/autoload.php \
            || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE.md
%doc README.md
%doc RELEASE.md
%doc composer.json
%dir %{phpdir}/Grasmash
     %{phpdir}/Grasmash/YamlExpander


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 20 2017 Shawn Iwinski <shawn@iwin.ski> - 1.1.1-1
- Initial package
