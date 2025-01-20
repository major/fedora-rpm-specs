# remirepo/fedora spec file for php-league-mime-type-detection
#
# Copyright (c) 2020-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
# Github
%global gh_commit    2d6702ff215bf922936ccc1ad31007edc76451b9
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     thephpleague
%global gh_project   mime-type-detection
# Packagist
%global pk_vendor    league
%global pk_name      mime-type-detection
# Namespace
%global ns_vendor    League
%global ns_project   MimeTypeDetection

Name:           php-%{pk_vendor}-%{pk_name}
Version:        1.16.0
Release:        2%{?dist}
Summary:        Mime-type detection for Flysystem

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
# Create git snapshot as tests are excluded from official tarball
Source1:        makesrc.sh

BuildArch:      noarch

BuildRequires:  php(language) >= 7.4
BuildRequires:  php-fileinfo
BuildRequires:  php-json
# From composer.json, "require-dev": {
#        "phpunit/phpunit": "^8.5.8 || ^9.3 || ^10.0",
#        "phpstan/phpstan": "^0.12.68",
#        "friendsofphp/php-cs-fixer": "^3.2"
BuildRequires:  phpunit10
%global phpunit %{_bindir}/phpunit10
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require": {
#        "php": "^7.4 || ^8.0",
#        "ext-fileinfo": "*"
Requires:       php(language) >= 7.4
Requires:       php-fileinfo
# From phpcompatifo report for 1.4.0
Requires:       php-json
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_name}) = %{version}


%description
This package supplies a generic mime-type detection interface with a finfo
based implementation.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
: Create classmap autoloader
phpab \
  --template fedora \
  --output src/autoload.php \
  src


%install
# Restore PSR-0 tree
mkdir -p   %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr src %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}


%check
: Generate a simple autoloader
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
// Installed library
require '%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php';
EOF

# We don't want PHPStan
sed -e 's/PHPStan\\Testing\\TestCase/PHPUnit\\Framework\\TestCase/' -i src/OverridingExtensionToMimeTypeMapTest.php

: Run upstream test suite
# the_generated_map_should_be_up_to_date is online
ret=0
for cmdarg in "php %{phpunit}" php81 php82 php83 php84; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit10} \
      --filter '^((?!(the_generated_map_should_be_up_to_date)).)*$' \
      --no-coverage \
      || ret=1
  fi
done
exit $ret


%files
%license LICENSE
%doc *.md
%doc composer.json
%{_datadir}/php/%{ns_vendor}
%exclude %{_datadir}/php/%{ns_vendor}/%{ns_project}/*Test.php


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 23 2024 Remi Collet <remi@remirepo.net> - 1.16.0-1
- update to 1.16.0

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 29 2024 Remi Collet <remi@remirepo.net> - 1.15.0-1
- update to 1.15.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Oct 18 2023 Remi Collet <remi@remirepo.net> - 1.14.0-1
- update to 1.14.0

* Fri Aug 25 2023 Remi Collet <remi@remirepo.net> - 1.13.0-1
- update to 1.13.0
- raise dependency on PHP 7.4
- use phpunit10

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Apr 19 2022 Remi Collet <remi@remirepo.net> - 1.11.0-1
- update to 1.11.0

* Mon Apr 11 2022 Remi Collet <remi@remirepo.net> - 1.10.0-1
- update to 1.10.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 22 2021 Remi Collet <remi@remirepo.net> - 1.9.0-1
- update to 1.9.0

* Mon Sep 27 2021 Remi Collet <remi@remirepo.net> - 1.8.0-1
- update to 1.8.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 19 2021 Remi Collet <remi@remirepo.net> - 1.7.0-1
- update to 1.7.0

* Mon Oct 19 2020 Remi Collet <remi@remirepo.net> - 1.5.1-1
- update to 1.5.1

* Tue Sep 22 2020 Remi Collet <remi@remirepo.net> - 1.5.0-1
- update to 1.5.0
- add patch for test suite from upstream and from
  https://github.com/thephpleague/mime-type-detection/pull/3
- open https://github.com/thephpleague/mime-type-detection/pull/4 phpunit 9
- switch to phpunit9

* Mon Aug 24 2020 Remi Collet <remi@remirepo.net> - 1.4.0-1
- initial package
