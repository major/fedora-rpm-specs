# remirepo/fedora spec file for php-sabre-xml2
#
# Copyright (c) 2016-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without      tests

# Github
%global gh_commit    01a7927842abf3e10df3d9c2d9b0cc9d813a3fcc
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sabre-io
%global gh_project   xml
# Packagist
%global pk_vendor    sabre
%global pk_project   %{gh_project}
# Namespace
%global ns_vendor    Sabre
%global ns_project   Xml
%global major        2

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Summary:        XML library that you may not hate
Version:        2.2.11
Release:        2%{?dist}

URL:            https://github.com/%{gh_owner}/%{gh_project}
License:        BSD-3-Clause
# Git snapshot with tests, because of .gitattributes
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
%if %{with tests}
BuildRequires:  php(language) >= 7.1
BuildRequires:  php-xmlwriter
BuildRequires:  php-xmlreader
BuildRequires:  php-dom
BuildRequires: (php-composer(sabre/uri) >= 1.0   with  php-composer(sabre/uri) <  3)
BuildRequires:  php-libxml
BuildRequires:  php-pcre
BuildRequires:  php-spl
# From composer.json, "require-dev": {
#        "friendsofphp/php-cs-fixer": "~2.17.1||3.63.2",
#        "phpstan/phpstan": "^0.12",
#        "phpunit/phpunit" : "^7.5 || ^8.5 || ^9.6"
BuildRequires:  phpunit9 >= 9.6
%global phpunit %{_bindir}/phpunit9
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require" : {
#        "php" : "^7.1 || ^8.0",
#        "ext-xmlwriter" : "*",
#        "ext-xmlreader" : "*",
#        "ext-dom" : "*",
#        "lib-libxml" : ">=2.6.20",
#        "sabre/uri" : ">=1.0,<3.0.0"
Requires:       php(language) >= 7.1
Requires:       php-xmlwriter
Requires:       php-xmlreader
Requires:       php-dom
Requires:      (php-composer(sabre/uri) >= 1.0   with  php-composer(sabre/uri) <  3)
# From phpcompatinfo report for version 2.1.2
Requires:       php-libxml
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
The sabre/xml library is a specialized XML reader and writer.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

phpab -t fedora -o lib/autoload.php lib
cat << 'EOF' | tee -a lib/autoload.php

// Dependencies
\Fedora\Autoloader\Dependencies::required([
    [
        '%{_datadir}/php/Sabre/Uri2/autoload.php',
        '%{_datadir}/php/Sabre/Uri/autoload.php',
    ],
]);

// Functions
if (!function_exists('Sabre\\Xml\\Serializer\\enum')) {
    require_once __DIR__ . '/Deserializer/functions.php';
    require_once __DIR__ . '/Serializer/functions.php';
}
EOF


%build
# nothing to build


%install
# Install as a PSR-0 library
mkdir -p %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr lib %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}


%check
: Check version
php -r '
require "%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php";
echo  Sabre\Xml\Version::VERSION . "\n";
exit (Sabre\Xml\Version::VERSION === "%{version}" ? 0 : 1);
'

%if %{with tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Sabre\\Xml\\', dirname(__DIR__).'/tests/Sabre/Xml/');
EOF
cd tests

: Run upstream test suite against installed library
ret=0
for cmdarg in "php %{phpunit}" php81 php82 php83 php84; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit9} || ret=1
  fi
done
exit $ret
%else
: Skip upstream test suite
%endif


%files
%license LICENSE
%doc *md
%doc composer.json
%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Sep  6 2024 Remi Collet <remi@remirepo.net> - 2.2.11-1
- update to 2.2.11

* Wed Aug 28 2024 Remi Collet <remi@remirepo.net> - 2.2.10-1
- update to 2.2.10 (no change, CS only)

* Fri Jul 26 2024 Remi Collet <remi@remirepo.net> - 2.2.9-1
- update to 2.2.9

* Thu Jul 25 2024 Remi Collet <remi@remirepo.net> - 2.2.8-1
- update to 2.2.8

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 18 2024 Remi Collet <remi@remirepo.net> - 2.2.7-1
- update to 2.2.7

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 28 2023 Remi Collet <remi@remirepo.net> - 2.2.6-1
- update to 2.2.6

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Nov  4 2021 Remi Collet <remi@remirepo.net> - 2.2.5-1
- update to 2.2.5

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct  5 2020 Remi Collet <remi@remirepo.net> - 2.2.3-1
- update to 2.2.3

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 11 2020 Remi Collet <remi@remirepo.net> - 2.2.1-1
- update to 2.2.1

* Sat Feb  1 2020 Remi Collet <remi@remirepo.net> - 2.2.0-1
- update to 2.2.0
- raise dependency on PHP 7.1
- switch to phpunit8

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Remi Collet <remi@remirepo.net> - 2.1.3-1
- update to 2.1.3

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul  5 2019 Remi Collet <remi@remirepo.net> - 2.1.2-3
- fix autoloader

* Fri Jul  5 2019 Remi Collet <remi@remirepo.net> - 2.1.2-2
- fix autoloader for sabre/uri v1 and v2

* Mon Jul  1 2019 Remi Collet <remi@remirepo.net> - 2.1.2-1
- update to 2.1.2
- rename to php-sabre-xml2
- move to /usr/share/php/Sabre/Xml2
- raise dependency on PHP 7
- switch to classmap autoloader

* Wed Jan  9 2019 Remi Collet <remi@remirepo.net> - 1.5.1-1
- update to 1.5.1

* Tue Jun  5 2018 Remi Collet <remi@remirepo.net> - 1.5.0-6
- fix project URL

* Sat Oct 29 2016 Remi Collet <remi@fedoraproject.org> - 1.5.0-2
- switch from symfony/class-loader to fedora/autoloader

* Mon Oct 10 2016 Remi Collet <remi@fedoraproject.org> - 1.5.0-1
- update to 1.5.0
- raise dependency on PHP 5.5

* Fri May 20 2016 Remi Collet <remi@fedoraproject.org> - 1.4.2-1
- update to 1.4.2

* Tue Mar 29 2016 Remi Collet <remi@fedoraproject.org> - 1.4.1-1
- update to 1.4.1

* Fri Mar 11 2016 Remi Collet <remi@fedoraproject.org> - 1.4.0-1
- Initial packaging

