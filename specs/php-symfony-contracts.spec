# remirepo/fedora spec file for php-symfony-contracts
#
# Copyright (c) 2019-2022 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    9e27f5c175ecbd6fff554d839ff4a432da797168
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     symfony
%global gh_project   contracts
# Packagist
%global pk_vendor    %{gh_owner}
%global pk_project   %{gh_project}
# Namespace
%global ns_vendor    Symfony
%global ns_project   Contracts
%global php_home     %{_datadir}/php
# Test
%global with_tests   0%{!?_without_tests:1}

Name:           php-%{pk_vendor}-%{pk_project}
Version:        1.1.13
Release:        9%{?gh_date:.%{gh_date}git%{gh_short}}%{?dist}
Summary:        A set of abstractions extracted out of the Symfony

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{?gh_short}.tar.gz

BuildArch:      noarch
%if %{with_tests}
# For tests
BuildRequires:  php(language) >= 7.1.3
BuildRequires:  php-reflection
BuildRequires:  php-json
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires:  php-intl
# From composer.json, "require-dev": {
#        "symfony/polyfill-intl-idn": "^1.10"
BuildRequires: (php-composer(psr/cache)     >= 1.0  with php-composer(psr/cache)     < 4)
BuildRequires: (php-composer(psr/container) >= 1.0  with php-composer(psr/container) < 2)
%global phpunit %{_bindir}/phpunit7
BuildRequires: %{phpunit}
# Autoloader
BuildRequires:  php-composer(fedora/autoloader)
%endif

# From composer.json, "require": {
#        "php": ">=7.1.3"
#        "psr/cache": "^1.0|^2.0|^3.0",
#        "psr/container": "^1.0"
Requires:       php(language) >= 7.1.3
# From composer.json, "suggest": {
#        "psr/event-dispatcher": "When using the EventDispatcher contracts",
#        "symfony/cache-implementation": "",
#        "symfony/event-dispatcher-implementation": "",
#        "symfony/http-client-implementation": "",
#        "symfony/service-implementation": "",
#        "symfony/translation-implementation": ""
Requires:      (php-composer(psr/cache)            >= 1.0  with php-composer(psr/cache)            < 4)
Requires:      (php-composer(psr/container)        >= 1.0  with php-composer(psr/container)        < 2)
Recommends:    (php-composer(psr/event-dispatcher) >= 1.0  with php-composer(psr/event-dispatcher) < 2)
# From phpcompatinfo report for version 1.1.0
Requires:       php-reflection
Requires:       php-json
Requires:       php-pcre
Requires:       php-spl
Requires:       php-intl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project})   = %{version}
Provides:       php-composer(%{pk_vendor}/cache-contracts) = %{version}
Provides:       php-composer(%{pk_vendor}/event-dispatcher-contracts) = %{version}
Provides:       php-composer(%{pk_vendor}/http-client-contracts) = %{version}
Provides:       php-composer(%{pk_vendor}/service-contracts) = %{version}
Provides:       php-composer(%{pk_vendor}/translation-contracts) = %{version}


%description
A set of abstractions extracted out of the Symfony components.

Can be used to build on semantics that the Symfony components
proved useful - and that already have battle tested implementations.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

for i in */composer.json */LICENSE */README.md
do
  mv $i $(dirname $i)_$(basename $i)
done


%build
: Create autoloader
cat <<'AUTOLOAD' | tee autoload.php
<?php
/* Autoloader for %{name} and its dependencies */
require_once '%{php_home}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\%{ns_project}\\', __DIR__);
\Fedora\Autoloader\Dependencies::optional([
    [
        '%{php_home}/Psr/Cache3/autoload.php',
        '%{php_home}/Psr/Cache2/autoload.php',
        '%{php_home}/Psr/Cache/autoload.php',
    ],
    '%{php_home}/Psr/Container/autoload.php',
    '%{php_home}/Psr/EventDispatcher/autoload.php',
]);
AUTOLOAD


%install
mkdir -p    %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}
for i in autoload.php Cache EventDispatcher HttpClient Service Translation
do
  rm -f $i/.gitignore
  cp -pr $i %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}/$i
done


%check
%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\%{ns_project}\\Tests\\Fixtures\\', dirname(__DIR__)."/Tests/Fixtures/");
EOF

ret=0
for cmd in php php74 php80 php81; do
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
%license *LICENSE
%doc *composer.json
%doc *.md
%dir %{php_home}/%{ns_vendor}/
     %{php_home}/%{ns_vendor}/%{ns_project}


%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.13-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 29 2022 Remi Collet <remi@remirepo.net> - 1.1.13-1
- update to 1.1.13

* Tue Apr  5 2022 Remi Collet <remi@remirepo.net> - 1.1.12-1
- update to 1.1.12

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 23 2021 Remi Collet <remi@remirepo.net> - 1.1.11-1
- update to 1.1.11
- allow psr/cache v2 and v3

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep  9 2020 Remi Collet <remi@remirepo.net> - 1.1.10-1
- update to 1.1.10

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 21 2019 Remi Collet <remi@remirepo.net> - 1.1.8-1
- update to 1.1.8
- psr/cache and psr/container are mandatory

* Tue Nov  5 2019 Remi Collet <remi@remirepo.net> - 1.1.7-1
- update to 1.1.7
- add missing EventDispatcher and HttpClient directories
- add weak dependency on psr/event-dispatcher

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 21 2019 Remi Collet <remi@remirepo.net> - 1.1.5-1
- update to 1.1.5
- psr/cache and psr/container are now required

* Thu Jun  6 2019 Remi Collet <remi@remirepo.net> - 1.1.3-1
- update to 1.1.3

* Tue May 28 2019 Remi Collet <remi@remirepo.net> - 1.1.1-1
- update to 1.1.1

* Thu May 16 2019 Remi Collet <remi@remirepo.net> - 1.1.0-1
- update to 1.1.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan  7 2019 Remi Collet <remi@remirepo.net> - 1.0.2-1
- initial package, version 1.0.2
