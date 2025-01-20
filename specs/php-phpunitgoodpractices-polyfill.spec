# remirepo/fedora spec file for php-phpunitgoodpractices-polyfill
#
# Copyright (c) 2018-2022 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without       tests

# Polyfill
# https://github.com/PHPUnitGoodPractices/polyfill/releases
%global gh_commit    625622fc35e922c04f28e448b43d85972be95040
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     PHPUnitGoodPractices
%global gh_project   polyfill
# Packagist
%global pk_vendor    phpunitgoodpractices
%global pk_project   %{gh_project}
# Namespace
%global ns_vendor    PHPUnitGoodPractices
%global ns_project   Polyfill
%global php_home     %{_datadir}/php
# Traits
# https://github.com/PHPUnitGoodPractices/Traits/releases
%global tr_commit    067b87ddc903231f07f89161f10f1ab8b393a6a1
%global tr_short     %(c=%{tr_commit}; echo ${c:0:7})
%global tr_version   1.9.2
# Legacy
# https://github.com/sanmai/phpunit-legacy-adapter/releases
%global lg_owner     sanmai
%global lg_project   phpunit-legacy-adapter
%global lg_commit    3db58a31847d803f76cab3da14e334a2d090c067
%global lg_short     %(c=%{lg_commit}; echo ${c:0:7})
%global lg_version   8.2.1

Name:           php-%{pk_vendor}-%{pk_project}
Version:        1.6.0
Release:        7%{?dist}
Summary:        Lacking future-compat polyfills for PHPUnit

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
# git snapshot to get upstream test suite (none for now)
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        php-%{pk_vendor}-traits-%{tr_version}-%{tr_short}.tgz
Source2:        php-%{lg_owner}-%{lg_project}-%{lg_version}-%{lg_short}.tgz
Source3:        makesrc.sh

BuildArch:      noarch
%if %{with tests}
# For tests
BuildRequires:  php(language) >= 5.5
%if 0%{?fedora} >= 32 || 0%{?rhel} >= 9
%global phpunit %{_bindir}/phpunit9
%else
%global phpunit %{_bindir}/phpunit8
%endif
BuildRequires: %{phpunit}
# From polyfill, composer.json,     "require-dev": {
#        "friendsofphp/php-cs-fixer": "^2",
#        "php-coveralls/php-coveralls": "^2.4"
# From traits, composer.json,     "require-dev": {
#        "phpspec/prophecy": "^1.10",
#        "phpunitgoodpractices/polyfill": "^1.1",
#        "sanmai/phpunit-legacy-adapter": "^6.1 || ^8.0"
%endif
BuildRequires:  php-cli
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From polyfill, composer.json,     "require": {
#        "php": "^5.5 || ^7.0 || ^8.0",
#        "phpunit/phpunit": "^4.8.36 || ^5.7.27 || ^6.5.14 || ^7.5.20 || ^8.0 || ^9.0"
# From traits, composer.json,     "require": {
#        "php": "^5.5 || ^7.0 || ^8.0",
#        "phpunit/phpunit": "^4.8.36 || ^5.7.27 || ^6.5.14 || ^7.5.20 || ~8.5 || ~9.4"
Requires:       php(language) >= 5.5
Requires:      (phpunit9 or phpunit8 or phpunit7 or phpunit6 or php-phpunit-PHPUnit)
# From phpcompatinfo report for version polyfill 1.5.0 and traits 1.9.1
# nothing
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-%{pk_vendor}-traits = %{tr_version}-%{release}
Provides:       php-composer(%{pk_vendor}/traits) = %{tr_version}
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
Lacking future-compat polyfills for PHPUnit.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit} -a 1 -a 2
mv composer.json composer-polyfill.json
mv LICENSE LICENSE-polyfill

mv Traits-%{tr_commit}/src           src2
mv Traits-%{tr_commit}/composer.json composer-traits.json
mv Traits-%{tr_commit}/LICENSE       LICENSE-traits
mv Traits-%{tr_commit}/tests         tests/Traits
mv %{lg_project}-%{lg_commit}/src    src3

cat << 'EOF' | tee src/autoload.php
<?php
/* autoloader for %{name} */

require_once '%{php_home}/Fedora/Autoloader/autoload.php';
if (!class_exists('PHPUnit\\Framework\\TestCase')) { // Call outside of phpunit command
    \Fedora\Autoloader\Dependencies::required([
        [
            '%{php_home}/PHPUnit9/autoload.php',
            '%{php_home}/PHPUnit8/autoload.php',
            '%{php_home}/PHPUnit7/autoload.php',
            '%{php_home}/PHPUnit6/autoload.php',
            '%{php_home}/PHPUnit/Autoload.php',
        ],
    ]);
}
\Fedora\Autoloader\Autoload::addPsr4('PHPUnitGoodPractices\\Polyfill\\', __DIR__);
\Fedora\Autoloader\Autoload::addPsr4('PHPUnitGoodPractices\\Traits\\', dirname(__DIR__) . '/Traits');
require_once __DIR__ . '/aliases.php';
EOF


%build
# Empty build section, most likely nothing required.


%install
: Library
mkdir -p    %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src  %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}
cp -pr src2 %{buildroot}%{php_home}/%{ns_vendor}/Traits


%check
: Minimal check for our autoloader
php -r '
require "%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}/autoload.php";
var_dump(PHPUnit\Runner\Version::id());
if (!trait_exists("PHPUnitGoodPractices\\Polyfill\\PolyfillTrait")) {
   echo("PolyfillTrait missing\n");
   exit(1);
}
if (!class_exists("PHPUnitGoodPractices\\Traits\\PHPUnitVersionRetriever")) {
   echo("PHPUnitVersionRetriever missing\n");
   exit(1);
}
'

%if %{with tests}
: Upstream test suite
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require '%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}/autoload.php';
require dirname(__DIR__) . '/src3/TestCase.php';
\Fedora\Autoloader\Autoload::addPsr4('PHPUnitGoodPractices\\Traits\\Tests\\', dirname(__DIR__) . '/tests/Traits');
EOF

ret=0
for cmdarg in "php %{phpunit}" php74 php80 php81 php82
do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit9} \
      --filter '^((?!(testThatThereIsProperPHPUnitInComposer)).)*$' \
      --verbose || ret=1
  fi
done

exit $ret
%else
: Test suite disabled
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE-*
%doc composer-*.json
%dir %{php_home}/%{ns_vendor}
     %{php_home}/%{ns_vendor}/%{ns_project}
     %{php_home}/%{ns_vendor}/Traits


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Sep 12 2022 Remi Collet <remi@remirepo.net> - 1.6.0-1
- update phpunitgoodpractices/polyfill to 1.6.0
- update phpunitgoodpractices/traits to 1.9.2

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec  8 2020 Remi Collet <remi@remirepo.net> - 1.5.0-2
- enable upstream test suite

* Tue Dec  8 2020 Remi Collet <remi@remirepo.net> - 1.5.0-1
- update phpunitgoodpractices/polyfill to 1.5.0

* Tue Oct 20 2020 Remi Collet <remi@remirepo.net> - 1.4.0-1
- update phpunitgoodpractices/polyfill to 1.4.0
- update phpunitgoodpractices/traits to 1.9.1
- allow PHPUnit 9

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 26 2019 Remi Collet <remi@remirepo.net> - 1.2.0-1
- update phpunitgoodpractices/polyfill to 1.2.0
- update phpunitgoodpractices/traits to 1.8.0
- allow PHPUnit 8

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 29 2018 Remi Collet <remi@remirepo.net> - 1.1.0-5
- update phpunitgoodpractices/traits to 1.7.0

* Tue Sep  4 2018 Remi Collet <remi@remirepo.net> - 1.1.0-4
- update phpunitgoodpractices/traits to 1.6.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 25 2018 Remi Collet <remi@remirepo.net> - 1.1.0-2
- add mandatory dependency on one PHPUnit version
- add phpunitgoodpractices/traits 1.5.1
- fix autoloader #1594663

* Mon Jun 11 2018 Remi Collet <remi@remirepo.net> - 1.1.0-1
- update to 1.1.0 (no change)
- add LICENSE file

* Mon Jun  4 2018 Remi Collet <remi@remirepo.net> - 1.0.0-1
- initial package, version 1.0.0
- open https://github.com/PHPUnitGoodPractices/polyfill/issues/1 - LICENSE file
