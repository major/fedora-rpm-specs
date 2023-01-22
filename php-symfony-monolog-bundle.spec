# remirepo/fedora spec file for php-symfony-monolog-bundle
#
# Copyright (c) 2018 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    572e143afc03419a75ab002c80a2fd99299195ff
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     symfony
%global gh_project   monolog-bundle
# Packagist
%global pk_vendor    %{gh_owner}
%global pk_project   %{gh_project}
# Namespace
%global ns_vendor    Symfony
%global ns_sub       Bundle
%global ns_project   MonologBundle
%global php_home     %{_datadir}/php
# Test
%global with_tests   0%{!?_without_tests:1}

Name:           php-%{pk_vendor}-%{pk_project}
Version:        3.3.1
Release:        10%{?gh_date:.%{gh_date}git%{gh_short}}%{?dist}
Summary:        Symfony MonologBundle

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{?gh_short}.tar.gz

BuildArch:      noarch
%if %{with_tests}
# For tests
BuildRequires:  php(language) >= 5.6
BuildRequires:  php-json
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires: (php-composer(%{pk_vendor}/monolog-bridge)       >= 2.7    with php-composer(%{pk_vendor}/monolog-bridge)       < 5)
BuildRequires: (php-composer(%{pk_vendor}/dependency-injection) >= 2.7    with php-composer(%{pk_vendor}/dependency-injection) < 5)
BuildRequires: (php-composer(%{pk_vendor}/config)               >= 2.7    with php-composer(%{pk_vendor}/config)               < 5)
BuildRequires: (php-composer(%{pk_vendor}/http-kernel)          >= 2.7    with php-composer(%{pk_vendor}/http-kernel)          < 5)
BuildRequires: (php-composer(monolog/monolog)                   >= 1.22   with php-composer(monolog/monolog)                   < 2)
# From composer.json, "require-dev": {
#        "symfony/yaml": "~2.7|~3.3|~4.0",
#        "symfony/console": "~2.7|~3.3|~4.0",
#        "symfony/phpunit-bridge": "^3.3|^4.0"
%global phpunit %{_bindir}/phpunit7
BuildRequires: (php-composer(%{pk_vendor}/yaml)                 >= 2.7    with php-composer(%{pk_vendor}/yaml)                 < 5)
BuildRequires: (php-composer(%{pk_vendor}/console)              >= 2.7    with php-composer(%{pk_vendor}/console)              < 5)
BuildRequires: (php-composer(%{pk_vendor}/phpunit-bridge)       >= 2.7    with php-composer(%{pk_vendor}/phpunit-bridge)       < 5)
BuildRequires: %{phpunit}
# Autoloader
BuildRequires:  php-composer(fedora/autoloader)
%endif

# From composer.json, "require": {
#        "php": ">=5.6",
#        "symfony/monolog-bridge": "~2.7|~3.3|~4.0",
#        "symfony/dependency-injection": "~2.7|~3.4.10|^4.0.10",
#        "symfony/config": "~2.7|~3.3|~4.0",
#        "symfony/http-kernel": "~2.7|~3.3|~4.0",
#        "monolog/monolog": "~1.22"
Requires:       php(language) >= 5.6
Requires:      (php-composer(%{pk_vendor}/monolog-bridge)       >= 2.7    with php-composer(%{pk_vendor}/monolog-bridge)       < 5)
Requires:      (php-composer(%{pk_vendor}/dependency-injection) >= 2.7    with php-composer(%{pk_vendor}/dependency-injection) < 5)
Requires:      (php-composer(%{pk_vendor}/config)               >= 2.7    with php-composer(%{pk_vendor}/config)               < 5)
Requires:      (php-composer(%{pk_vendor}/http-kernel)          >= 2.7    with php-composer(%{pk_vendor}/http-kernel)          < 5)
Requires:      (php-composer(monolog/monolog)                   >= 1.22   with php-composer(monolog/monolog)                   < 2)
# From phpcompatinfo report for version 3.3.1
Requires:       php-json
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
The MonologBundle provides integration of the Monolog library
into the Symfony framework.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_sub}/%{ns_project}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
: Create autoloader
cat <<'AUTOLOAD' | tee autoload.php
<?php
/* Autoloader for %{name} and its dependencies */
require_once '%{_datadir}/php/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\%{ns_sub}\\%{ns_project}\\', __DIR__);
\Fedora\Autoloader\Dependencies::required([
    [
        '%{_datadir}/php/Symfony4/Bridge/Monolog/autoload.php',
        '%{_datadir}/php/Symfony3/Bridge/Monolog/autoload.php',
        '%{_datadir}/php/Symfony/Bridge/Monolog/autoload.php',
    ],
    [
        '%{_datadir}/php/Symfony4/Component/DependencyInjection/autoload.php',
        '%{_datadir}/php/Symfony3/Component/DependencyInjection/autoload.php',
        '%{_datadir}/php/Symfony/Component/DependencyInjection/autoload.php',
    ],
    [
        '%{_datadir}/php/Symfony4/Component/Config/autoload.php',
        '%{_datadir}/php/Symfony3/Component/Config/autoload.php',
        '%{_datadir}/php/Symfony/Component/Config/autoload.php',
    ],
    [
        '%{_datadir}/php/Symfony4/Component/HttpKernel/autoload.php',
        '%{_datadir}/php/Symfony3/Component/HttpKernel/autoload.php',
        '%{_datadir}/php/Symfony/Component/HttpKernel/autoload.php',
    ],
    '%{_datadir}/php/Monolog/autoload.php',
]);
AUTOLOAD


%install
mkdir -p                   %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_sub}/%{ns_project}
for i in *php DependencyInjection Resources SwiftMailer
do
  cp -pr $i                 %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_sub}/%{ns_project}/$i
done


%check
%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_sub}/%{ns_project}/autoload.php';
\Fedora\Autoloader\Dependencies::required([
    [
        '%{_datadir}/php/Symfony4/Component/Yaml/autoload.php',
        '%{_datadir}/php/Symfony3/Component/Yaml/autoload.php',
        '%{_datadir}/php/Symfony/Component/Yaml/autoload.php',
    ], [
        '%{_datadir}/php/Symfony4/Component/Console/autoload.php',
        '%{_datadir}/php/Symfony3/Component/Console/autoload.php',
        '%{_datadir}/php/Symfony/Component/Console/autoload.php',
    ], [
        '%{_datadir}/php/Symfony4/Bridge/PhpUnit/autoload.php',
        '%{_datadir}/php/Symfony3/Bridge/PhpUnit/autoload.php',
        '%{_datadir}/php/Symfony/Bridge/PhpUnit/autoload.php',
    ],
]);
EOF

ret=0
for cmd in php php71 php72 php73; do
  if which $cmd; then
    $cmd %{phpunit} \
      --no-coverage \
      --verbose
  fi
done
exit $ret
%else
: Test suite disabled
%endif


%files
%license LICENSE
%doc composer.json
%doc *.md
%dir %{php_home}/%{ns_vendor}/
%dir %{php_home}/%{ns_vendor}/%{ns_sub}
     %{php_home}/%{ns_vendor}/%{ns_sub}/%{ns_project}


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 28 2018 Remi Collet <remi@remirepo.net> - 3.3.1-1
- initial package, version 3.3.1
